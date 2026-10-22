# AI Handoff and Project Brain

This file is the durable handoff point for AI agents continuing work in this repository. Read it together with `AGENTS.md`, `README.md`, and `CURRICULUM.md` before editing.

## Project identity

- **Repository:** `zzpsah/CS_Interactive_Hub`
- **Primary branch:** `main`
- **Published site:** https://zzpsah.github.io/CS_Interactive_Hub/
- **Source of truth:** repository files on GitHub `main`; GitHub Pages is the published output, not a separate editing surface.
- **Purpose:** a free, bilingual (English–Hindi), student-first Computer Science learning hub for Classes 9–12, built primarily with static HTML, CSS, JavaScript, and SVG.

## Product and design contract

- Preserve the existing UI/UX and established workflows. No redesign, major restyling, navigation changes, or information-architecture changes without explicit user approval.
- Make the smallest change that satisfies the task; avoid unrelated refactors and dependency additions.
- Maintain white backgrounds, readable dark text, responsive/mobile-friendly layouts, and English/Hindi support.
- Keep educational explanations concise and student-friendly. Use editable HTML for text and local SVGs for illustrations.
- Prefer relevant icons and small/medium illustrations next to the concept they explain, sized to available space and adapted for mobile without crowding the text.
- Keep the site portable: use relative paths and repository-local assets. No Google Drive dependency or external image CDN for core lesson assets.
- Preserve interactive controls and test them when changed. Keep keyboard accessibility and meaningful labels.
- Keep print output legible and preserve authored colors; the user's printer settings determine whether output is printed in color or grayscale.
- Do not introduce student-facing wording that the project owner has rejected. In particular, the owner has asked to avoid using the word “notes” in student-facing section labels; use labels such as “Study & Copy” and “Quick Revision” where appropriate.

## Chapter 1 current working context

- Main lesson: `class09/ch01_hardware_memory.html`
- Virtual lab: `class09/hardware_lab.html`
- Shared stylesheet: `assets/css/style.css`
- Shared JavaScript: `assets/js/app.js`
- Local illustrations: `assets/images/class09/`; see `assets/images/class09/ASSET-MANIFEST.md`.
- Public lesson URL: https://zzpsah.github.io/CS_Interactive_Hub/class09/ch01_hardware_memory.html
- Chapter 1 includes learning path, IPO, hardware/software, CPU, RAM, ROM/firmware, SSD/HDD, real-life examples, labelled illustrations, zoomable local SVGs, virtual lab, revision, model answer, quiz, and Hindi summary.
- Study & Copy section provides clean and illustrated notebook display modes, copy and print controls, and concise editable study content.
- The CPU, RAM, and SSD topic cards include corresponding local SVG illustrations. When adding more, keep them relevant, appropriately sized, and responsive.
- Quick Revision and question/quiz content use collapsible sections. Preserve this interaction unless explicitly asked to change it.
- CSS changes require updating the stylesheet cache-buster query in the relevant HTML when needed; inspect the current value instead of assuming it has not changed.

## Required delivery workflow

Use the workflow defined in `AGENTS.md`:

**READ → UNDERSTAND → PLAN → IMPLEMENT → TEST → REVIEW → FIX → COMMIT → UPDATE DOCUMENTATION → VERIFY DEPLOYMENT**

Before a change, inspect the latest branch and current files. After a change, report:
1. What changed and why.
2. Exact files changed.
3. Commit SHA and message.
4. Tests/checks actually run and their outcomes.
5. Whether GitHub Pages deployment and the published page were actually verified.
6. Anything still pending or not verifiable.

Do not say “done,” “tested,” “live,” or “verified” beyond the evidence. If browser testing or deployment-status access is unavailable, state that limitation rather than guessing.

## Handoff template

Use this when passing the task to another AI or a human contributor:

- **Goal / acceptance criteria:**
- **Repository / branch / latest commit:**
- **Files inspected:**
- **Files changed:**
- **User constraints / decisions to preserve:**
- **Tests actually run and results:**
- **Deployment status / evidence:**
- **Known risks or unresolved issues:**
- **Next safe step:**

The next agent must read `AGENTS.md` and this file first. Do not revert established decisions or perform broad UI/UX changes as part of an unrelated task.
