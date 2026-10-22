# Instructions for AI Coding Agents

These instructions apply to every AI assistant, coding agent, human contributor, and automated tool working in this repository. Read this file and `AI-HANDOFF.md` before changing anything.

## Non-negotiable project rules

1. **Preserve the existing UI and UX.** Treat the current design, navigation, language switch, responsive behavior, content structure, interactions, and visual hierarchy as intentional product decisions. Do not redesign, replace, simplify away, or restyle them just because another design seems preferable.
2. **Minimal, scoped changes only.** Change only what the requested task requires. Avoid unrelated refactors, broad find-and-replace operations, framework migrations, new dependencies, and changes to working flows.
3. **No silent product decisions.** A change that materially alters the visual design, information architecture, navigation, student workflow, language behavior, or project architecture requires explicit user authorization. If the request is ambiguous on one of these points, ask before making that change.
4. **Respect the repository's source of truth.** Work from the latest `main` branch. Keep the source files in GitHub synchronized with the published GitHub Pages experience. Do not treat a deployed page, generated copy, external Drive file, or local cache as the authoritative source.
5. **Keep it portable.** Prefer static HTML, CSS, JavaScript, and repository-local SVG/image assets. Use relative paths. Do not add a backend, database, account system, Google Drive dependency, external image CDN, or build framework without explicit approval.
6. **Protect educational accuracy.** Keep language student-friendly and concise. Do not claim a topic is officially examinable unless verified against the current applicable syllabus; follow `CURRICULUM.md`.
7. **Keep accessibility and responsiveness.** Preserve keyboard operation, semantic HTML, visible focus, meaningful labels/alt text, readable contrast, and mobile layouts. Do not make controls decorative or inert.
8. **Do not overwrite unseen work.** Fetch and inspect the current file before editing it. Use the latest file SHA for updates. Avoid concurrent writes to the same file. Review diffs and existing conventions before making broad edits.
9. **No false verification claims.** Distinguish static code inspection from a real browser test, automated test, and live deployment check. Report exactly what was checked and what remains unverified.
10. **No secrets in Git.** Never commit passwords, API keys, OAuth secrets, tokens, personal data, or private credentials. Do not weaken security to make a test pass.

## Required DevOps / vibe-coding workflow

Follow this order for every non-trivial change:

**READ → UNDERSTAND → PLAN → IMPLEMENT → TEST → REVIEW → FIX → COMMIT → UPDATE DOCUMENTATION → VERIFY DEPLOYMENT**

- **READ:** Inspect `AGENTS.md`, `AI-HANDOFF.md`, `README.md`, `CURRICULUM.md`, relevant HTML/CSS/JS/assets, and recent changes.
- **UNDERSTAND:** Identify the existing behavior and dependencies; find the exact page and files involved.
- **PLAN:** State the smallest safe change and the acceptance criteria. Ask first if the plan changes established UI/UX or architecture.
- **IMPLEMENT:** Make scoped edits using existing patterns. Keep text editable in HTML and diagrams/illustrations in SVG where appropriate; do not rasterize text as a substitute for real page content.
- **TEST:** Check HTML structure, local/relative links, asset paths, JavaScript behavior, language toggles, keyboard use, mobile responsiveness, and print behavior when affected. Run available automated checks. Never claim a check was run if it was not.
- **REVIEW:** Inspect the actual diff for unrelated edits, broken links, duplicate IDs, inaccessible controls, console errors (if browser testing is available), and regressions.
- **FIX:** Resolve detected failures before calling the task complete. If a check cannot be performed, say so clearly.
- **COMMIT:** Use a descriptive commit message. Keep changes focused and avoid bundling unrelated work.
- **UPDATE DOCUMENTATION:** Update the README or `AI-HANDOFF.md` if project behavior, conventions, assets, or workflows changed.
- **VERIFY DEPLOYMENT:** Confirm the GitHub Pages workflow/deployment status and inspect the published page when the required tools allow it. A successful commit alone does not prove the live page is updated.

## UI/UX baseline

- Free, bilingual English–Hindi, student-first learning for Classes 9–12.
- White background, black/readable text, mobile-friendly responsive layout.
- Preserve existing language switch, navigation, page layout, chapter interactions, quizzes, revision sections, and virtual labs.
- Keep explanations concise, clear, and age-appropriate; use relevant icons and appropriately sized local illustrations where they help comprehension.
- Keep student-facing wording intentional. Avoid terms the project owner has explicitly rejected; check existing decisions before introducing labels.
- Keep content accessible and legible in print. Do not force grayscale or remove authored colors from print styles unless explicitly requested.
- Reuse existing design tokens, CSS patterns, and assets before inventing new ones.

## When handing work to another AI

Give the next agent the exact repository and branch, task objective, relevant files, user constraints, latest commit, changes already made, tests actually run, known failures/uncertainties, and next safe step. Explicitly repeat: preserve UI/UX, make minimal changes, do not undo prior decisions, and do not claim unverified work is complete.

If these instructions conflict with a task interpretation or an agent's default preferences, preserve the established project behavior and ask the user rather than silently changing it.
