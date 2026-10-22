# CS Interactive Hub

Interactive Computer Science curriculum with visual explanations, hands-on labs, and checkpoint quizzes.

## Structure
- index.html — curriculum homepage
- pipeline_manifest.json — chapter metadata
- class09/ch01_hardware_memory.html — Class 9 Chapter 1
- class10/, class11/, class12/ — reserved for future chapters

## GitHub Pages
Repository Settings → Pages → GitHub Actions. The sync workflow builds and deploys a static site artifact after a source change.

## Content note
Class 9 Chapter 1 has been checked against the publicly accessible Google Drive outline. The published lesson includes the IPO cycle, CU/ALU/register explanations, a hardware classification lab, an interactive memory hierarchy, binary/decimal unit clarification, and a five-question quiz. Editorial improvements can continue independently of source changes.


## Automatic public Drive → GitHub Pages synchronization

- Source folder: https://drive.google.com/drive/folders/1Y3vRy7pwCa3Oj2FSoF7QIb4hlwIjc65H
- Workflow: `.github/workflows/sync-public-drive.yml` runs every 15 minutes and can also be started manually from GitHub Actions.
- Sync script: `scripts/sync_public_drive.py` reads the publicly shared Drive folder and exports supported Google Docs to `drive-source/`. It compares content hashes, so unchanged sources do not create commits.
- When a source document named in the Drive `pipeline_manifest.json` changes, the corresponding chapter's live source outline is refreshed. New manifest chapters get a generated starter page and the homepage chapter links are rebuilt. The interactive authored lesson is preserved when its page already exists.
- Source changes are committed to `main`, then a GitHub Pages artifact is published. The automation never writes to Google Drive; it uses public read access only. The source documents remain owned and editable in Drive, while the portal copy is managed in GitHub.
- If a public Drive file becomes private, moves, or the folder listing format changes, the workflow fails visibly rather than silently overwriting lesson content. Check the Actions run log for the error.
- Editorial quality remains an explicit review responsibility: generated starter pages are useful drafts, not a substitute for a teacher/content review. Existing lessons can be further improved without waiting for a source edit.
