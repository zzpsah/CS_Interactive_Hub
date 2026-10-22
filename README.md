# CS सीखें — Computer Science Learning Hub

A free bilingual (English–Hindi), student-first Computer Science learning website for Classes 9–12. Built with static HTML, CSS, JavaScript and SVG for GitHub Pages.

## Student experience
- White background, black text, mobile-friendly layout.
- English/Hindi language switch.
- Clear theory, examples, diagrams, interactive activities, quizzes and exam-ready answers.
- No account, database, backend or Google Drive dependency.

## Curriculum policy
This is a Bihar-oriented learning path. Bihar SCERT official textbook and e-resource portals are linked from the homepage. A current, class-specific BSEB Computer Science scope for all four classes—especially Classes IX–X—was not independently confirmed in this initial release. Topics must not be labelled officially examinable until checked against the current school/board syllabus. See CURRICULUM.md.

## Run locally
Open index.html in a browser or use any static web server.

## Publish
GitHub Pages deploys the main branch through .github/workflows/pages.yml. The repository is the source of truth; no Drive sync is required.

## Contribution and AI-agent rules

- **Mandatory instructions for every AI/coding agent:** [AGENTS.md](AGENTS.md)
- **Project brain, current context, and AI handoff:** [AI-HANDOFF.md](AI-HANDOFF.md)
- **Curriculum accuracy and syllabus caveats:** [CURRICULUM.md](CURRICULUM.md)

The existing UI/UX and working student workflows are protected project decisions. Agents must use the documented READ → UNDERSTAND → PLAN → IMPLEMENT → TEST → REVIEW → FIX → COMMIT → UPDATE DOCUMENTATION → VERIFY DEPLOYMENT workflow. No redesigns or architecture changes without explicit approval. GitHub `main` is the source of truth; commits alone do not prove GitHub Pages has deployed successfully.

## Official references
- Bihar SCERT textbooks: https://scert.bihar.gov.in/textbooks
- Bihar SCERT e-resources: https://scert.bihar.gov.in/eresources
- Bihar SCERT homepage: https://scert.bihar.gov.in/


## Class 9 image assets and portability
- Class 9 Chapter 1 includes repository-local SVG hardware illustrations with a mobile-friendly zoom dialog.
- Image files live in `assets/images/class09/`; the chapter does not depend on Google Drive or an external image CDN.
- See `assets/images/class09/ASSET-MANIFEST.md` for the illustration inventory and portability notes.
- Keep image references relative to the HTML file so the entire repository can be migrated as a package to Vercel or another static host.
