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

11. **Topic-driven design, not one generic template.** For each chapter or topic, preserve the shared site-wide design system while tailoring the learning presentation to the subject matter. Choose diagrams, illustrations, analogies, interactive labs, examples, and visual emphasis based on what best teaches that specific topic. Do not force every topic into an identical card layout or reuse unrelated imagery. Before changing a topic's presentation, inspect its existing learning goals and assets; make changes that improve understanding without breaking the established site-wide UI/UX.

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


## Student copy and focus-view rules

- The chapter's **Study & Copy** area must be distinct from explanation and activity content. Make the illustrated notebook the default presentation; keep Clean view as an alternate.
- Provide a distraction-free Writing view: hide unrelated lesson chrome/content, emphasize the writing surface, and retain only mode selection plus copy, print, and exit actions. Keep it responsive and keyboard accessible.
- Quick Revision, quiz/question sets, and optional reference links start collapsed. Keep core teaching explanations and inline activities visible.
- If a full lab is supplementary, collapse its launch card/reference by default without collapsing the chapter's inline activities.
- Keep copy-ready material short, accurate, clearly sectioned, printable, and free from extra commentary that students would not copy.


## Mandatory curriculum-wide visual teaching standard (owner-approved 2026-10-23)

**The whole CS Interactive Hub must be developed as a visual, animated, concept-driven learning experience—not a static textbook with occasional decorative animation.** This is a project-wide rule for every class, chapter, lesson, lab, and future curriculum addition.

- Whenever an explanation describes a process, transformation, relationship, sequence, or state change, choose a visual explanation that makes that change visible: animated diagrams, moving arrows/packets/data, highlighted components, step-by-step traces, state changes, or learner-controlled simulations.
- Make the animation specific to the concept. Examples: hardware data moving through input/CPU/memory/output; network packets moving between devices; binary bits and place values changing; memory reads/writes; Python values flowing through variables, functions, lists and code lines; algorithms comparing/swapping/traversing items.
- A typical concept should combine: a concise explanation; a labelled visual or animation; Play/Pause, Next/Previous, Reset or step controls where they materially help; a worked example; and a short learner check. Do not force every concept into the same template—select the interaction that teaches it best.
- Animation must explain academic content, not merely decorate the page. Avoid continuous movement without instructional meaning, excessive motion, long introductory hero sections, and generic animated cards that do not demonstrate the concept.
- Preserve the established site-wide UI/UX, navigation, language switch, responsive layout, English–Hindi translations, existing functionality and topic-specific presentation. Use shared motion conventions, not a single generic page design.
- Keep content available without animation; support keyboard and touch; provide visible focus and meaningful labels; respect prefers-reduced-motion; avoid essential information conveyed only by color or movement; keep mobile diagrams legible and print output useful.
- Use portable repository-local HTML/CSS/JavaScript/SVG and relative paths. Keep explanatory text editable and accessible. Do not copy Log2Base2 source code, branding, course text, illustrations, or videos. Study its publicly visible learning patterns and independently create original experiences suited to our curriculum and students.
- Develop the curriculum using **theory → visual/process explanation → worked example → learner-controlled practice/lab → understanding check → Study & Copy/revision**. Adapt the sequence when the topic warrants it. Quick Revision, quiz sets and optional references should remain collapsed by default; keep essential teaching visible. Keep the Chapter 1 hero compact and supplementary practice labs collapsed by default where already established.
- **No chapter is considered visually complete merely because shared scroll-reveal effects exist.** Review every concept and verify that the important process or state changes are actually demonstrated. Document each chapter’s visual teaching plan and completed interactions in AI-HANDOFF.md or chapter-specific documentation.
- Before building a chapter, identify its conceptual transformations and choose the appropriate visual model. Before closing work, check educational accuracy, language parity, responsive behavior, keyboard/touch controls, reduced motion, print, links/assets, and actual browser behavior where tools allow. Report what was actually tested; never claim unverified deployment or browser QA.


## Shared chapter design system — mandatory for every chapter

Every chapter must inherit the same established visual language and learning affordances as Class 9 Chapter 1. This is a project-wide implementation rule, not an optional topic-level preference. Use the shared stylesheet and shared lesson patterns for the notebook-inspired Study & Copy area, coloured hierarchy, consistent heading treatment, accessible icons, explanatory callouts, bullets/lists, diagrams, interactive states, bilingual labels, responsive layouts, print and reduced-motion support. Topic-specific visuals and animations must differ when the concept differs, while typography, spacing, colour tokens, section framing, and study-note experience remain coherent. Do not mark a chapter complete because it has text and one animation. Inspect the rendered page against Chapter 1, check every control and notes section, and fix cross-chapter drift before adding more isolated features.

## Mandatory content separation: Theory, Questions & Answers, and Quick Revision

This rule applies to every chapter, not only Class 9 Chapter 1.

- **Theory / Study & Copy:** Teach the complete chapter content as connected, well-organised theory. Use meaningful topic headings, clear explanatory paragraphs, correct academic terminology, examples, relevant diagrams or visual explanations, and bilingual English–Hindi explanations where the chapter supports both languages. This section must be suitable for students to study and write into their notebooks. Do **not** format it as a list of exam questions with model answers.
- **Questions and Answers:** Keep exam-style questions and their model answers in their own dedicated section. This is the place for short-answer, long-answer, and other assessment questions. Do not duplicate the Q&A bank inside Study & Copy.
- **Quick Revision:** Keep it concise and revision-focused—key terms with brief definitions. Do not put full theory, duplicate Q&A, extra question banks, “points to remember,” or “common mistakes” here unless explicitly requested.
- **No content duplication:** The three sections must serve distinct purposes: learn the concepts (Theory / Study & Copy), practise written responses (Questions and Answers), and quickly recall terminology (Quick Revision). Reuse the same subject matter only when needed for a brief cross-reference; do not repeat the same material in another format merely to fill a section.
- **Before committing any chapter:** inspect all three sections together, confirm their roles are distinct, remove repeated content, and verify that Study & Copy contains actual explanatory theory rather than Q&A. Treat this as a required review check.

## Mandatory notebook-style Study & Copy presentation

- Keep the student-facing section named **Study & Copy** (with the appropriate bilingual label). Do not label it “Study Notes” or replace the notebook experience with a plain article.
- The complete theory inside Study & Copy must be presented as a notebook-inspired writing sheet: ruled-paper or notebook-like background, handwritten/sketch-style heading treatment, clear topic headings, readable paragraphs and key facts, plus original illustrative diagrams or labelled sketches that explain the chapter concepts.
- Include meaningful concept-specific sketches where they improve understanding (for example, computer functional units and the IPO cycle in Class 9 Chapter 1). Do not rely on decorative doodles alone; diagrams must teach.
- Keep the notebook appearance responsive, accessible, bilingual where relevant, and printable. Keep the Writing view, Print and Copy text actions working. The notebook is part of the visible lesson, not a mode that may silently disappear.
- Before committing changes to Study & Copy, verify the section heading is visible, the notebook styling is active by default, illustrative diagrams render, and the theory remains separate from Q&A and Quick Revision. Never remove or flatten this notebook presentation during content refactors.


## Mandatory concise, copy-ready Study & Copy notes

- Study & Copy is a compact summary students can copy into their notebooks, not a second full lesson. Keep only essential definitions, facts, comparisons, steps and exam-useful points.
- Prefer crisp bullet points over long explanatory paragraphs. Use a clear hierarchy: chapter heading, numbered topic headings, short subheadings and consistently indented bullets.
- Style topic headings visibly with colour and underlining. Maintain readable spacing, accessible contrast and responsive layout.
- Put each essential example in a distinct, compact **Example / उदाहरण** box; keep the English and Hindi versions together where bilingual content is provided.
- Use only small, useful diagrams when they improve recall. Avoid oversized illustrations, filler introductions, repeated theory, duplicated Q&A, and decorative clutter.
- Preserve Writing view, Print and Copy text actions. Check mobile, writing-view and print layouts before committing.
