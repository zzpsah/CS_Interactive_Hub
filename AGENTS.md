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

## Mandatory English–Hindi toggle and formatting parity

- The shared **Add Hindi / English only** control must update every supported Hindi translation on the page, including regular HTML text, headings, lists, tables, and labels inside SVG diagrams. Do not leave Hindi text permanently visible in English-only mode or hidden in Hindi mode.
- Hindi counterparts must preserve the same semantic structure and visual hierarchy as English: headings remain headings, paragraphs remain paragraphs, list items retain bullets/indentation, table rows/cells retain table layout, and SVG labels toggle without breaking diagram positioning.
- Prefer explicit `lang="hi"` and `.lang-hi` markup for translated content. When the shared script wraps inline bilingual text, preserve English text and isolate only the Hindi segment. Do not flatten formatted content into generic inline text.
- Before committing language changes, inspect every affected class/chapter page and check the toggle in both directions, including Study & Copy, headings, lists, quizzes, and SVG diagrams. Confirm spacing, indentation, colours, emphasis and responsive behavior remain equivalent in both languages.
- Shared toggle fixes belong in `assets/js/app.js` and `assets/css/style.css` where appropriate, so they propagate to all chapter pages using the shared assets.

## Class 9 Chapter 1 is the canonical chapter benchmark

`class09/ch01_hardware_memory.html` is the reference implementation for the student-facing chapter experience. Use its current Study & Copy section as the benchmark for every other chapter page. This is a shared standard, not permission to clone its computer-specific content or force every topic into identical teaching visuals.

### Study & Copy standard for every chapter

- Keep the section named **Study & Copy** with the appropriate bilingual label and a visible notebook-inspired writing sheet. The notebook presentation is the default, not a hidden mode; retain the established Clean/Writing view behavior where present.
- Start each major topic with a clear one- or two-sentence explanation/definition in English and Hindi when the page is bilingual. Follow with concise, indented bullets for essential facts, comparisons, steps or terms. The notes must be understandable, not just a keyword list, but short enough to copy into a notebook.
- Use the benchmark’s visual hierarchy: numbered topic headings, consistent coloured/underlined headings, readable spacing, clear bullet indentation, accessible contrast, and responsive styling.
- Use topic-specific teaching visuals when they improve understanding: a labelled flow diagram, component sketch, annotated illustration or small learner-controlled visual. Include a short explanation of what the student should notice, in both languages where appropriate. Prefer editable text and repository-local SVG/HTML over a decorative or unexplained image.
- Do **not** add an example to every topic. Include a worked example only when it meaningfully clarifies a concept, process or application. Avoid repeated example boxes, filler, duplicated Q&A, oversized decoration and repeated theory.
- Keep Questions & Answers and Quick Revision separate from Study & Copy. Preserve each page’s working Writing view, Print and Copy text controls, plus language, quiz, navigation and other existing interactions.
- Check notebook appearance, diagrams, bilingual parity, mobile layout, writing view, print, accessibility and all existing controls before marking a chapter complete.

### Benchmark-change propagation rule

- When the owner approves a change to Class 9 Chapter 1’s shared chapter or Study & Copy presentation, treat it as a **design-system change**. Identify every other chapter page and the corresponding section, component, CSS rule, or interaction affected by that change.
- Apply the equivalent change to all affected pages, including Class 10, Class 11 and Class 12, and any additional chapter pages added later. Keep the teaching content and visuals specific to each chapter; propagate the rule and behavior, not unrelated Class 9 content.
- Update shared CSS/JavaScript once when the behavior is genuinely shared; update page-specific markup/content on each affected page. Do not leave inconsistent versions or implement a change only on the benchmark page without explicitly recording why another page is exempt.
- Before committing, compare the benchmark and affected pages, verify the corresponding sections and actions, and record any remaining exceptions in `AI-HANDOFF.md`. Do not claim every page has been updated unless each affected page has actually been inspected and changed.


## Official curriculum alignment and no-duplication policy

- Treat `CURRICULUM.md` as the source-of-truth map for the target chapter architecture. Use current official curriculum sources and record the academic year and subject code when applicable.
- Do not label a hub-designed module as an official NCERT chapter. For Class VIII, verify against the current CT & AI framework; for Class IX, distinguish the NCERT ICT textbook sequence from the current CBSE Computer Applications syllabus.
- Class XI and XII Computer Science (083) and Informatics Practices (065) must be separate learning tracks, not merged into one chapter sequence.
- Each concept must have one canonical chapter. If existing pages overlap, consolidate and cross-link rather than adding another full duplicate lesson. Revisit a concept in a later class only to teach a clearly stated new level of depth or skill.
- The Class IX target sequence follows the eight NCERT ICT chapters listed in `CURRICULUM.md`. Existing pages on hardware, OS, files, bits/bytes and algorithms should be consolidated into appropriate canonical chapters or marked as optional enrichment, not treated as extra NCERT chapters.
- Every chapter must be visually instructional: topic-specific diagrams/animations, working touch-friendly interactions, meaningful feedback, concise bilingual explanation, useful practice, and Study & Copy. Hover-only effects or decorative motion do not satisfy this requirement.
- Update `CURRICULUM.md` whenever a chapter map changes. Keep the live site, class index pages and curriculum map consistent; never mark planned pages as complete before they are implemented and checked.


## Class IX NCERT ICT canonical chapter set

The Class IX index must link to exactly these eight canonical chapter files, in this order:
1. `class09/ch01_introduction_ict.html` — Introduction to ICT
2. `class09/ch02_textual_communication.html` — Creating Textual Communication
3. `class09/ch03_visual_communication.html` — Creating Visual Communication
4. `class09/ch04_audio_video_communication.html` — Creating Audio-Video Communication
5. `class09/ch05_presenting_ideas.html` — Presenting Ideas
6. `class09/ch06_getting_connected_internet.html` — Getting Connected: Internet
7. `class09/ch07_cyber_safety.html` — Safety and Security in the Cyber World
8. `class09/ch08_fun_with_logic.html` — Fun with Logic

- `class09/index.html` is the student-facing canonical chapter list. Do not add old hardware/OS/files/bits/algorithm pages as extra NCERT chapters.
- Legacy `ch01_hardware_memory.html`, `ch02_software_os.html`, `ch03_files_folders.html`, `ch04_internet_cyber_safety.html`, `ch05_algorithms_flowcharts.html`, `ch06_data_bits_bytes.html`, and old `ch07`–`ch10` topic pages redirect to the appropriate canonical chapter. Keep standalone labs as optional practice where linked.
- Class VIII is a separate CBSE CT & AI track (2026–27) and must be clearly labelled as such. Do not mix it into the Class IX NCERT ICT chapter list.
- CBSE circular Acad-18/2026 says NCERT CT&AI modules for Classes IX–XII are intended for internal assessment in 2026–27. Verify module availability and applicability before claiming the eight-chapter ICT sequence is the complete current assessment syllabus.
- For Classes IX–XII, follow the user's NCERT-first requirement. Use current CBSE documents as a scope/applicability cross-check, not as a reason to merge distinct subject tracks or mislabel a resource.
- Do not mark Class IX complete until all eight canonical pages have been individually checked for source alignment, complete content, working interactions, English/Hindi formatting, mobile/touch behaviour, reduced-motion accessibility, Study & Copy, print, and internal links.

## Interactive simulation and cartoon buddy requirements

Before creating or modifying any simulation, animation, draggable activity, or mascot, read [INTERACTIVE-LEARNING-STANDARD.md](INTERACTIVE-LEARNING-STANDARD.md). These requirements are mandatory: teach visible state changes rather than relying on static images alone where a process is being taught; provide learner-controlled step/play/reset behavior; make drag-and-drop usable by touch/click alternatives; support keyboard and reduced-motion preferences; keep all controls functional; and use an original, context-aware cartoon buddy whose reactions encourage rather than shame learners. Do not reproduce copyrighted characters such as Talking Tom or specific anime characters. For the first release, implement and test the complete information journey in `class09/ch01_part2_computer_workflow.html` before propagating the pattern. Apply the acceptance checklist in the standard and report only checks actually performed.

### Site-wide humanoid learning buddy

The original cartoon learning buddy is intended to be a **site-wide companion across the learning page**, not an element confined to one simulation. It must be a complete humanoid character with a head/expressive face, torso, arms and hands, and legs and feet—not just a floating head, emoji, or tiny icon. Prefer an original cat-like humanoid mascot unless the owner changes the direction. It should react contextually to learning progress and use purposeful, lightweight poses/expressions without obscuring content or distracting from the lesson. Follow `INTERACTIVE-LEARNING-STANDARD.md`; do not copy protected characters or voices.
- The learning buddy system is a course-wide feature for Classes 9–12, not only one simulation/page. Offer 2–3 original, switchable full-body humanoid characters (e.g. cat-like buddy, robot, fox-like buddy) through a reusable shared component. Learners can tap/click or use keyboard to switch; preserve lesson/simulation progress. Provide a broad but purposeful expression/gesture library (happy, proud, excited, laughing, curious, thinking, concentrating, confused, surprised, celebrating, encouraging, empathetic/sad, playful, sleepy, bored, relieved, cheering, etc.) and contextual reactions to lesson events and optional character taps. Keep humour kind, animation lightweight, and provide reduced-motion/quiet behavior. Follow `INTERACTIVE-LEARNING-STANDARD.md`; do not imitate famous protected characters.

- Add a fourth selectable character option: an original, full-body humanoid monkey buddy. Keep it playful, expressive, and educational; do not imitate any famous monkey/cartoon character. Character selection remains course-wide and switching preserves lesson/simulation state. See `INTERACTIVE-LEARNING-STANDARD.md`.
