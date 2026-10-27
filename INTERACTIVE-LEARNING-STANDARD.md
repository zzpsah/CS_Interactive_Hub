# Interactive Learning, Simulation & Character Standard

This document is mandatory for every AI agent and contributor adding interactive lessons, animations, mascots, or simulations to CS Interactive Hub. Read it together with `AGENTS.md`, `AI-HANDOFF.md`, and `CURRICULUM.md`.

## Goal

Teach processes by showing them in motion. A learner should be able to see what changes, control the pace, try an action, make a mistake safely, and understand why the result occurred. Static diagrams are useful support, but they do not replace an interactive process when the concept is inherently dynamic.

## 1. Simulation quality rules

- Build simulations around the lesson's actual learning objective; do not add motion just for decoration.
- Show a visible state transition, such as data moving through Input → Processing → Output → Storage. Clearly indicate the current stage and explain the change in simple English and Hindi.
- Include learner controls where they add learning value: Start/Play, Next step, Pause/Reset, and replay. Every displayed control must work.
- Let learners experiment with a value or choice and see a meaningful result. Explain errors kindly and tell the learner how to recover.
- Use motion that communicates cause and effect. Keep it lightweight and usable on low-end Android phones; do not require WebGL, heavy frameworks, a backend, login, or network services for core interactions.
- Drag-and-drop must have a tap/click alternative. Keep touch targets comfortable, keyboard access available, and focus states visible.
- Respect `prefers-reduced-motion`; provide a useful non-animated or step-by-step mode. Avoid flashing, rapid movement, and motion that can distract or cause discomfort.
- Use semantic HTML, accessible labels, useful `aria-live` announcements for changing feedback, and readable contrast. Do not make essential information hover-only.
- Keep bilingual text consistent with the site's language behavior. If a simulation has no working translation mechanism, do not pretend that it is bilingual.
- Make the first view useful on mobile. No clipped controls, forced horizontal page scrolling, or huge blank areas.
- Use local HTML/CSS/JavaScript/SVG and relative asset paths. Avoid external image CDNs, copyrighted third-party assets, and new dependencies without approval.

## 2. Original mascot / cartoon buddy

- An original, friendly cartoon companion may guide lessons and react to learner actions. **It must be a complete, visibly humanoid character**: expressive face/head, torso/body, two arms with hands, and two legs with feet. The default direction is a cute, approachable cat-like humanoid computer buddy (anthropomorphic cat-person/mascot), not merely a floating cat head, emoji, or icon. Give it readable facial expressions, clear hand/arm gestures, and body poses that can support lightweight CSS/SVG animation. Keep the silhouette and details original; the owner may later choose a different original humanoid animal character.
- Provide **2–3 selectable original characters** in the first design iteration (for example: a cat-like humanoid, a small robot student, and a fox-like humanoid). These are provisional concepts, not final assets. Show visible character choices and let the learner switch by tapping/clicking; selection must also be keyboard accessible. Switching should update the active character consistently across the page and all lessons that use the shared buddy system. Keep the lesson progress and current simulation state when switching characters. Use original designs, not copies of famous cartoon/anime characters. If persistent preferences are implemented, use a lightweight local preference and provide a safe default; do not add accounts or a backend.
- Do not copy a famous character's distinctive appearance, name, voice, animation, costume, or branding (for example, Talking Tom or a specific anime character). Popularity is not permission to reproduce protected characters. Make an original character inspired only by broad traits such as friendliness, humor, and expressiveness.
- The mascot must support learning rather than interrupt it. Keep it small, non-blocking, dismissible or quiet when needed, and never cover instructions, controls, or content.
- Reactions must be contextual and age-appropriate. Suggested moods include: happy/proud for success; curious/thinking while processing; gently confused for an incorrect choice; encouraging after a mistake; surprised at a discovery; sleepy/bored only as a brief optional joke during a pause or idle state. Never shame, mock, or label a learner as bad or stupid.
- Use short, helpful English/Hindi speech bubbles or captions. Do not autoplay audio. Sound and voice, if later approved, must be opt-in with visible mute/stop controls and text captions.
- Prefer a small defined mood set with purposeful state changes over random, constant motion. Idle animation must stop or reduce when the user is interacting, the page is hidden, or reduced motion is requested.
- Do not imply AI-generated live conversation or speech recognition unless those features actually exist. The first version should work entirely offline with deterministic reactions.

## 3. Recommended first release for Class 9 ICT Part 2

Implement a small, complete learning interaction in `class09/ch01_part2_computer_workflow.html` before spreading the pattern to other lessons.

1. A visible data token (for example, a mark or number) enters the Input stage.
2. The learner starts the journey or advances one step at a time.
3. The token visibly moves/highlights through Processing (CPU), Output, and Storage; stage labels and explanations update in English and Hindi.
4. A learner can change the input and replay the flow.
5. Add an original, complete humanoid cat-like buddy with a head/face, torso, arms/hands, and legs/feet, using contextual happy, thinking, encouraging, surprised, and optional idle/sleepy poses/reactions. Keep reactions short and tied to real events.
6. Provide tap-to-select as an alternative to dragging; explain an incorrect sequence without punishment.
7. Provide pause/step/reset controls, reduced-motion behavior, keyboard access, and a compact mobile layout.

## 4. Acceptance checklist

A change is not complete merely because its HTML contains the word “simulation” or a diagram.

- [ ] The learner can see a process or state change, not just a static image.
- [ ] The learner can control or replay the process.
- [ ] Every control works on touch; drag has a non-drag alternative.
- [ ] Correct and incorrect actions produce clear, encouraging feedback.
- [ ] The mascot changes mood in response to actual lesson events and does not obscure learning content.
- [ ] English/Hindi behavior is correct and verified.
- [ ] Keyboard, visible focus, labels, reduced motion, and mobile layout are checked.
- [ ] JavaScript syntax and runtime behavior are tested; errors are fixed.
- [ ] Existing page navigation, language switch, Study & Copy, Quick Revision, questions, and print/copy actions still work.
- [ ] Local assets and links work without external service dependencies.
- [ ] GitHub Actions/Pages deployment is checked; the published page is inspected when tools allow it.
- [ ] Report clearly which checks were actually performed and which remain unverified.

## 5. Implementation workflow

Follow the repository workflow in `AGENTS.md`: READ → UNDERSTAND → PLAN → IMPLEMENT → TEST → REVIEW → FIX → COMMIT → UPDATE DOCUMENTATION → VERIFY DEPLOYMENT. Inspect the current page and styles before editing. Keep the change scoped to the approved lesson. Do not replace existing working interactions or redesign the overall site without explicit approval.
