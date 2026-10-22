#!/usr/bin/env python3
"""Sync the public CS_Interactive_Hub Google Drive folder into this static site.

Read-only on Google Drive: the public link is used for source reads. Changes are
committed to GitHub by the scheduled workflow; no Drive credentials are needed.
"""
from __future__ import annotations
import codecs, datetime as dt, hashlib, html, json, re, sys, urllib.error, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DRIVE_ROOT_ID = "1Y3vRy7pwCa3Oj2FSoF7QIb4hlwIjc65H"
DRIVE_ROOT_URL = f"https://drive.google.com/drive/folders/{DRIVE_ROOT_ID}"
UA = "CS-Interactive-Hub-Public-Drive-Sync/1.0"


def get(url: str, timeout: int = 25) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        if r.status != 200:
            raise RuntimeError(f"HTTP {r.status} while reading public Drive source")
        return r.read()


def drive_entries(folder_id: str) -> list[dict]:
    page = get(f"https://drive.google.com/drive/folders/{folder_id}").decode("utf-8", "replace")
    match = re.search(r"window\['_DRIVE_ivd'\] = '(.*?)';", page, re.S)
    if not match:
        raise RuntimeError(f"Could not parse public Drive listing for folder {folder_id}")
    raw = codecs.decode(match.group(1).replace("\\/", "/"), "unicode_escape")
    data = json.loads(raw)
    found: dict[str, dict] = {}

    def walk(node):
        if not isinstance(node, list):
            return
        # Drive's public folder bootstrap contains file records in this shape:
        # [file_id, parent_ids, name, mime_type, ...].
        if (len(node) > 4 and isinstance(node[0], str) and len(node[0]) > 15
                and isinstance(node[1], list) and isinstance(node[2], str)
                and isinstance(node[3], str) and node[3].startswith("application/")):
            fid, parents, name, mime = node[:4]
            if folder_id in parents:
                found[fid] = {"id": fid, "name": name, "mime_type": mime, "parents": parents}
        for child in node:
            walk(child)
    walk(data)
    return list(found.values())


def discover_all() -> list[dict]:
    queue = [DRIVE_ROOT_ID]
    seen_folders = set()
    files: dict[str, dict] = {}
    while queue:
        folder_id = queue.pop(0)
        if folder_id in seen_folders:
            continue
        seen_folders.add(folder_id)
        for item in drive_entries(folder_id):
            files[item["id"]] = item
            if item["mime_type"] == "application/vnd.google-apps.folder":
                queue.append(item["id"])
    return list(files.values())


def export_text(item: dict) -> str:
    fid, mime = item["id"], item["mime_type"]
    if mime == "application/vnd.google-apps.document":
        url = f"https://docs.google.com/document/d/{fid}/export?format=txt"
    elif mime == "application/vnd.google-apps.spreadsheet":
        url = f"https://docs.google.com/spreadsheets/d/{fid}/export?format=csv"
    elif mime == "application/vnd.google-apps.presentation":
        url = f"https://docs.google.com/presentation/d/{fid}/export/txt"
    elif mime.startswith("text/"):
        url = f"https://drive.google.com/uc?export=download&id={fid}"
    else:
        return ""
    return get(url).decode("utf-8-sig", "replace").replace("\r\n", "\n").strip() + "\n"


def safe_slug(value: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9_-]+", "-", value.strip()).strip("-").lower()
    return value[:70] or "source"


def chapter_path(module: dict) -> Path:
    grade, chapter = int(module["grade"]), int(module["chapter"])
    drive_doc = str(module.get("drive_doc", ""))
    prefix = f"class{grade:02d}_ch{chapter:02d}_"
    slug = drive_doc[len(prefix):] if drive_doc.startswith(prefix) else safe_slug(module.get("title", f"chapter-{chapter}"))
    return ROOT / f"class{grade:02d}" / f"ch{chapter:02d}_{safe_slug(slug)}.html"


def render_source_outline(title: str, text: str, synced_at: str) -> str:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    # Keep the source excerpt readable while avoiding an excessively long repeated dump.
    bits = []
    for line in lines[:45]:
        line = re.sub(r"^[_\-•*\s]+", "", line).strip()
        if not line:
            continue
        if len(line) > 360:
            line = line[:357].rstrip() + "…"
        bits.append(f"<li>{html.escape(line)}</li>")
    body = "\n".join(bits) if bits else "<li>Source document is currently empty.</li>"
    return (f'<!-- DRIVE_SOURCE_START -->\n<section class="card" id="drive-source-outline">'
            f'<h2>Source outline · synced from Google Drive</h2>'
            f'<p class="small muted">Source: {html.escape(title)} · Last source sync: {html.escape(synced_at)}. '
            f'The teaching lesson above adds explanations and activities to this source outline.</p>'
            f'<ul>{body}</ul></section>\n<!-- DRIVE_SOURCE_END -->')


def generated_chapter(module: dict, source_text: str, synced_at: str) -> str:
    title = html.escape(str(module.get("title", "Computer Science Chapter")))
    outline = render_source_outline(str(module.get("drive_doc", title)), source_text, synced_at)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="Interactive Computer Science lesson: {title}"><title>{title}</title><style>:root{{color-scheme:dark}}body{{margin:0;background:#09111f;color:#f1f6ff;font:16px/1.65 system-ui,sans-serif}}header,main,footer{{max-width:950px;margin:auto;padding:22px}}.card{{background:#14233a;border:1px solid #314967;border-radius:16px;padding:22px;margin:18px 0}}p,li{{color:#c1cfe3}}a{{color:#6ee7d2}}.pill{{color:#6ee7d2}}button{{padding:10px 14px;border-radius:8px;border:0;background:#6ee7d2;font-weight:bold}}@media(max-width:600px){{header,main,footer{{padding:15px}}}}</style></head><body><header><p class="pill">CS INTERACTIVE HUB · CLASS {int(module['grade']):02d}</p><h1>{title}</h1><p>Learn the core ideas, inspect the source outline, and check your understanding.</p><a href="../index.html">← Curriculum home</a></header><main><section class="card"><h2>Learning approach</h2><ol><li>Read the source outline and identify the key terms.</li><li>Explain each concept in your own words and connect it to a real example.</li><li>Use the questions below as a self-check; revisit any idea you cannot explain yet.</li></ol></section><section class="card"><h2>Quick self-check</h2><p>Without looking back, write or say three key ideas from this lesson. Then compare your explanation with the source outline.</p><label for="reflection">My explanation</label><textarea id="reflection" rows="5" style="display:block;width:100%;box-sizing:border-box;margin:8px 0;padding:10px;border-radius:8px;background:#09111f;color:#f1f6ff;border:1px solid #314967"></textarea><button id="count" type="button">Check reflection length</button><p id="feedback" aria-live="polite"></p></section>{outline}</main><footer>CS Interactive Hub · Source content synced {html.escape(synced_at)}</footer><script>document.getElementById('count').addEventListener('click',()=>{{const n=document.getElementById('reflection').value.trim().split(/\\s+/).filter(Boolean).length;document.getElementById('feedback').textContent=n>=25?'Good start: you have written '+n+' words. Check that you defined key terms and included an example.':'Add a little more detail: '+n+' words so far. Try defining a term and giving an example.'}})</script></body></html>'''



def update_homepage(modules: list[dict]) -> None:
    path = ROOT / "index.html"
    page = path.read_text(errors="replace")
    cards = []
    for grade in range(9, 13):
        grade_modules = sorted([m for m in modules if int(m.get("grade", 0)) == grade], key=lambda m: int(m.get("chapter", 0)))
        body = [f"<section class=\"card\"><h2>Class {grade}</h2>"]
        if grade_modules:
            body.append("<ul>")
            for module in grade_modules:
                target = chapter_path(module).relative_to(ROOT).as_posix()
                title = html.escape(str(module.get("title", "Computer Science")))
                number = int(module.get("chapter", 0))
                body.append(f'<li><a href=\"{html.escape(target, quote=True)}\">Chapter {number}: {title}</a></li>')
            body.append("</ul><p>Interactive lessons, visual models and self-check activities.</p>")
        else:
            body.append("<p>Coming soon · lessons will appear here when added to the shared curriculum manifest.</p>")
        body.append("</section>")
        cards.append("".join(body))
    block = "\n<!-- CHAPTER_CARDS_START -->\n" + "\n".join(cards) + "\n<!-- CHAPTER_CARDS_END -->\n"
    pattern = r"<!-- CHAPTER_CARDS_START -->.*?<!-- CHAPTER_CARDS_END -->"
    if re.search(pattern, page, re.S):
        page = re.sub(pattern, lambda _: block.strip(), page, count=1, flags=re.S)
        path.write_text(page)
    else:
        print("Warning: homepage chapter-card markers missing; not rewriting navigation.", file=sys.stderr)


def main() -> int:
    now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    source_dir = ROOT / "drive-source"
    source_dir.mkdir(exist_ok=True)
    items = discover_all()
    by_name = {item["name"]: item for item in items}
    old_index_path = source_dir / "source-index.json"
    old = json.loads(old_index_path.read_text()) if old_index_path.exists() else {"files": {}}
    current = {}
    changed = []
    text_by_id = {}
    for item in sorted(items, key=lambda x: (x["name"].lower(), x["id"])):
        mime = item["mime_type"]
        text = export_text(item)
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest() if text else hashlib.sha256((item["name"]+mime).encode()).hexdigest()
        current[item["id"]] = {"name": item["name"], "mime_type": mime, "parents": item.get("parents", []), "sha256": digest}
        text_by_id[item["id"]] = text
        if old.get("files", {}).get(item["id"]) != current[item["id"]]:
            changed.append({"id": item["id"], "name": item["name"], "mime_type": mime, "sha256": digest})
        if text:
            snapshot = source_dir / f"{safe_slug(item['name'])}--{item['id'][:10]}.txt"
            if not snapshot.exists() or snapshot.read_text(errors="replace") != text:
                snapshot.write_text(text)
    removed = [v.get("name", fid) for fid, v in old.get("files", {}).items() if fid not in current]
    manifest_item = by_name.get("pipeline_manifest.json")
    manifest = {}
    if manifest_item:
        try:
            manifest = json.loads(text_by_id.get(manifest_item["id"], "{}"))
        except json.JSONDecodeError:
            print("Warning: source manifest is not valid JSON; keeping existing chapter mappings.", file=sys.stderr)
    modules = manifest.get("modules", []) if isinstance(manifest, dict) else []
    modules_by_doc = {str(m.get("drive_doc", "")): m for m in modules if isinstance(m, dict) and m.get("drive_doc")}
    if modules:
        update_homepage(modules)
    if not changed and not removed:
        print("Public Drive source unchanged; no files need updating.")
        return 0
    for item in items:
        if item["name"] not in modules_by_doc:
            continue
        text = text_by_id.get(item["id"], "")
        if not text:
            continue
        module = modules_by_doc[item["name"]]
        path = chapter_path(module)
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            page = path.read_text(errors="replace")
            block = render_source_outline(item["name"], text, now)
            pattern = r"<!-- DRIVE_SOURCE_START -->.*?<!-- DRIVE_SOURCE_END -->"
            if re.search(pattern, page, re.S):
                page = re.sub(pattern, lambda _: block, page, count=1, flags=re.S)
            else:
                page = page.replace("</main>", block + "\n</main>")
            path.write_text(page)
        else:
            path.write_text(generated_chapter(module, text, now))
        print(f"Updated chapter page from public source: {path.relative_to(ROOT)}")

    # Keep a visible, compact change report on the homepage.
    report = {"synced_at": now, "source_folder": DRIVE_ROOT_URL,
              "changed_files": [x["name"] for x in changed], "removed_files": removed}
    (source_dir / "sync-report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    (source_dir / "source-index.json").write_text(json.dumps({"root_folder": DRIVE_ROOT_URL, "files": current, "last_changed_sync": now}, indent=2, ensure_ascii=False) + "\n")
    print(f"Detected {len(changed)} added/changed file(s); {len(removed)} removed file(s).")
    for item in changed:
        print(" -", item["name"])
    for name in removed:
        print(" - removed from public listing:", name)
    return 0

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"SYNC FAILED: {type(exc).__name__}: {exc}", file=sys.stderr)
        raise
