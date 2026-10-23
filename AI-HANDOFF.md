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

## Topic-driven UI/UX rule

Preserve both parts of the design contract:

1. **Consistent product experience across the site:** navigation, typography, spacing, color system, accessibility, language switch, responsive behavior, and familiar interaction patterns should remain coherent.
2. **Topic-specific teaching experience:** individual chapters should use visuals and interactions that fit their actual subject. For example, hardware can use labelled component diagrams and a virtual hardware lab; algorithms can use step-by-step traces or flowcharts; networking can use packet/path visualizations; data topics can use suitable tables or charts. These are examples, not mandatory templates.

Do not apply a single generic visual layout to every topic, and do not add decorative visuals that do not teach the concept. Match illustration size to available space and learning value; keep text editable and images responsive. Reuse the shared design system, but choose each topic's examples, diagrams, activities, and emphasis deliberately. A topic-specific UI/UX change must preserve accessibility, mobile usability, language behavior, and existing working controls. Significant redesigns still require the owner's explicit approval.

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


## Study & Copy and distraction-free writing contract (2026-10-23)

- Keep the dedicated **Study & Copy** section separate from visual teaching, activities, and explanations. Its content must be precise, concise, ambiguity-free, editable, printable, and easy for students to copy.
- **Illustrated notebook is the default**: white paper, clear separated writing, readable handwritten-style or notebook-like treatment, coloured pen-style headings/arrows/icons and relevant small illustrations. Preserve print legibility; decorations must not overwhelm the writing.
- Keep a simple **Clean view** option, but do not make it the default.
- Provide a **Writing view** that hides unrelated page content and gives the copy-ready material most of the screen. Keep only essential notebook/clean mode controls and Copy, Print, and Exit controls visible. It should be responsive and usable on mobile; scrolling, if needed for long material, stays inside the focused writing surface rather than the full lesson page.
- Keep **Quick Revision**, quizzes/question sets, and optional reference links collapsed by default. The main explanations and essential activities remain open.
- The full virtual-lab launch/reference card is optional and collapsed by default; do not hide the chapter's inline learning activities.
- Apply these patterns to future chapters while preserving topic-specific teaching UI/UX. Do not flatten every topic into one generic lesson layout.

## Beginner-first teaching standard (approved for Class 9 Chapter 1)

- Assume the learner is starting with no computing knowledge. Do not ask the user to define the chapter or teaching sequence; design the sequence from first principles.
- Start with “What is a computer?”: an accurate academic definition, then a plain-language explanation, examples of data versus information, and a labelled visual.
- Teach in this order: definition and familiar computer setup; basic architecture/functional units; input, processing, output and storage; characteristics and limitations; IPO process; hardware versus software; CPU, memory and storage; everyday examples; interactive practice; study-and-copy and examination revision.
- Remove a standalone learning-goals section when it delays the first explanation. Keep chapter navigation compact/collapsible and remove redundant hero tags, metadata badges, repeated warnings and lengthy introductory prose.
- Use visuals as teaching aids, not decoration. Label parts and arrows, explain how to read each diagram, make it legible on mobile, and pair it with concise text.
- Pair simple language with correct academic terminology. Define technical terms on first use and provide short, examination-ready definitions, comparisons, labelled diagrams and practice questions.
- Keep the existing interactive hardware lab available; lab enhancement is a separate next phase after the teaching layout is reviewed.
- “Add Hindi” means show Hindi translations alongside the English content. It must work consistently across the whole page, including headings, lists, diagrams, tables, activities and feedback, without hiding the English text or duplicating digits/punctuation.
- Treat Chapter 1 as the layout prototype for review. Do not roll the design out to other chapters until the user approves this chapter’s final structure.

## Visual presentation standard

- Use purposeful topic icons, restrained color coding, labelled diagrams, dashed outlines for diagram/worksheet areas, and responsive cards to improve scanning without clutter.
- Use subtle motion only when it clarifies progression; always respect `prefers-reduced-motion` and keep all content available without animation.
- Interactive controls must perform a real action and provide clear feedback; never add decorative or inert buttons. Quizzes should provide score feedback and explain incorrect answers when the behavior is implemented and tested.
- Maintain sufficient contrast, keyboard access, readable mobile diagrams, and printable study content. Visual effects must not replace academic explanations or examination terminology.


## Animated teaching flow and compact Chapter 1 hero (2026-10-23)

- The Chapter 1 hero is intentionally compact and includes a small, decorative animated gear/circuit motif. The motion is supplementary and hidden from assistive technology.
- The architecture and IPO diagrams use restrained moving arrows and a subtle sequential highlight to help learners follow data flow; reduced-motion preferences disable these animations.
- The Practice lab section is collapsed by default with an explicit summary control; its activities remain in the page and can be expanded at any time.
- Verify at desktop and mobile widths, test the open/close interaction and language switch, and check reduced-motion behavior before considering browser QA complete. Connector-based edits alone do not constitute live browser testing.


## Site-wide explanatory motion system (2026-10-23)

- The owner explicitly requested an animated teaching experience across the entire project, not just a compact animated hero or one interactive widget.
- Shared motion is implemented in `assets/css/style.css` and `assets/js/app.js`: lesson sections, diagrams, worked examples, component cards and concept visuals reveal as learners scroll; diagrams receive a subtle motion-aware treatment; cards provide restrained hover feedback.
- This is a shared baseline, not a mandate to make every page identical. Future topic-specific animations should teach the concept: e.g. data packets travelling through a network, bits toggling in number systems, memory read/write movement, and Python values flowing through functions/lists.
- Preserve the existing UI and topic-specific teaching layouts. Add motion where it explains change or sequence; avoid motion on every paragraph or continuous distracting animation. Respect reduced-motion preferences, keep content readable without animation, and make all interactive steps keyboard/touch accessible.
- All HTML pages should use the `site-motion-1` cache-buster for the shared stylesheet and script until the shared motion layer changes again.
- Browser-level motion QA remains outstanding; verify mobile and desktop, language toggle, keyboard/touch interactions, collapsed details, print mode, and reduced-motion settings before claiming visual QA complete.


## Owner-approved visual curriculum doctrine and Log2Base2 reference (2026-10-23)

### Non-negotiable project-wide direction
The owner wants the entire Classes 9–12 curriculum and future project work to feel like a visual learning show: when a concept explains something happening, learners should be able to see the process unfold. This applies to every chapter and all supporting documentation—not only the hero or one demonstration. A few global reveal effects are only foundational motion, not fulfillment of this goal.

Use this teaching pattern as the default, adapting to the topic:
1. **Explain** the idea in concise, student-friendly English and Hindi.
2. **Show** it with a topic-specific animated diagram, simulation, or step-by-step visual trace.
3. **Walk through** one concrete worked example with the active component/state/line highlighted.
4. **Let the learner control it** with appropriate Play/Pause, Next/Previous, Reset, value input, or toggles.
5. **Check understanding** with a short prediction or question and feedback.
6. **Consolidate** with accurate Study & Copy and revision material.

### Reference study: Log2Base2
Reference: https://www.log2base2.com/ and https://www.log2base2.com/dsa. Publicly indexed descriptions emphasize animated visual teaching, short focused lessons, step-by-step code walkthroughs, seeing changes in computer memory as code executes, and linking complex ideas to real-world examples. The reference is useful for learning design principles, not for copying its expression. Its full interactive experience is JavaScript-driven and could not be inspected through a static page open, so conclusions here are limited to publicly visible page descriptions and course listings.

Adopt the following principles, independently implemented for our free, bilingual, beginner-first school curriculum:
- **Show state changes:** values, nodes, bits, packets, memory cells, components and outputs visibly change at each step.
- **One step at a time:** learners can advance/rewind/reset a process and see what changed and why; keep the current step and result explicit.
- **Code-to-state mapping:** for programming topics, highlight the executing line and show variable/list/memory state side-by-side.
- **Short, purposeful visual lessons:** break complicated processes into focused, manageable demonstrations rather than one long video or long page intro.
- **Real-life anchors:** use familiar examples (marks, school records, messages, files, classroom networks) before increasing abstraction.
- **Active learning:** ask learners to predict the next state, try their own input when suitable, then give clear feedback and explain errors.
- **Curriculum-wide consistency with topic-specific visuals:** shared controls, accessibility, spacing and interaction conventions; different visual metaphors for different concepts.
- **Original, open and portable implementation:** keep source text editable, use local SVG/HTML/CSS/JS, avoid paid-service dependencies, and create original visuals and wording. Do not reuse Log2Base2's protected video, text, branding, graphics, or code.

### Topic implementation map
- Class 9 hardware: moving data through input, CPU/ALU, memory, output and persistent storage; component focus and state.
- Class 9 software/OS: user action → operating system → application/hardware, process and file-state walkthroughs.
- Class 10 networks/web: packet travel, router hops, client/server request-response, browser-to-webpage flow.
- Class 10 digital safety: interactive scenario choices with visible consequences and safe explanations.
- Class 11 number systems: place-value columns, toggling bits, stepwise decimal/binary conversion.
- Class 11 computer memory: address/cell selection, read/write and volatile-vs-persistent state.
- Class 12 Python functions: line-by-line execution, call stack/arguments/return values and variable state.
- Class 12 lists/data: index-based access, insertion/deletion and before/after state.
- Future algorithms, loops, databases and files: trace iterations, rows/records, data movement and state changes step by step.

### Implementation status discipline
- The shared motion layer in assets/css/style.css and assets/js/app.js provides a foundation for scroll reveals and subtle interaction feedback. It does **not** mean every concept is animated yet.
- Topic-specific animation coverage is a staged curriculum project. Track it chapter by chapter; do not claim complete coverage until each chapter has a reviewed visual teaching plan and its core process demos implemented and tested.
- For each completed chapter, record the visual demo(s), learner controls, language support, reduced-motion behavior, and browser tests in this handoff or chapter notes.
- Existing site contract remains in force: preserve UI/UX and navigation, keep hero sections compact, maintain English–Hindi parity, collapse optional revision/reference/lab launch sections by default, keep essential teaching visible, and respect reduced-motion, keyboard, touch, mobile and print behavior.
