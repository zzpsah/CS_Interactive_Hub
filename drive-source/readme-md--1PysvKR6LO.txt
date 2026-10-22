CS Interactive Hub • System Architecture & ChatGPT Deployment Guide
1. Overview
This repository serves as an autonomous, interactive, choice-based Computer Science learning portal covering the NCERT / CBSE curriculum from Class 9 through Class 12.


All lesson decks are authored by Gemini (Tutor & System Architect) as standalone, responsive, single-file HTML decks equipped with:


* Interactive Choice Paths: Express Mode vs. Deep Dive.
* Embedded Visuals: Inline SVGs (zero network latency, no external image storage bloat).
* Interactive Simulations & Quizzes: Self-checking logic puzzles with emoticon feedback (•‿•).


Deployment and GitHub synchronization are managed by ChatGPT (Repo Operator).


________________


2. Shared Google Drive Information
* Root Shared Folder Name: CS_Interactive_Hub
* Drive Folder ID: 1Y3vRy7pwCa3Oj2FSoF7QIb4hlwIjc65H
* Drive URL: https://drive.google.com/drive/folders/1Y3vRy7pwCa3Oj2FSoF7QIb4hlwIjc65H


________________


3. Directory Layout Standard
In your local repository and on GitHub, maintain this exact hierarchy:


CS_Interactive_Hub/


│


├── README.md                          # Architecture guidelines & agent contract


├── pipeline_manifest.json             # Sync state tracker between Gemini & ChatGPT


├── index.html                         # Master grade & chapter navigation dashboard


│


├── class09/                           # Class 9 (ICT, Hardware, Cyber Safety, Scratch)


│   ├── ch01_hardware_memory.html


│   └── ch02_cyber_safety.html


│


├── class10/                           # Class 10 (Networking, HTML/CSS, DBMS)


│   ├── ch01_networking.html


│   └── ch02_html_css.html


│


├── class11/                           # Class 11 (Architecture, Python Core, Lists)


│   ├── ch01_computer_systems.html


│   ├── ch02_number_systems.html


│   ├── ch05_conditionals.html


│   └── ch06_loops.html


│


└── class12/                           # Class 12 (Stacks, SQL, Networks, Capstone)


    ├── ch03_stacks.html


    └── ch09_sql.html


________________


4. ChatGPT Execution Workflow
Whenever a new chapter is announced or placed in the shared Google Drive:


1. Read pipeline_manifest.json:
   * Locate any module where "status": "ready_for_chatgpt_sync".
2. Fetch the HTML File:
   * Retrieve the HTML content corresponding to the document listed in pipeline_manifest.json.
3. Commit to Repository:
   * Save the file under the appropriate classXX/ directory.
   * Update index.html so the corresponding card/link points to the newly added chapter.
4. Update pipeline_manifest.json in Google Drive:
   * Change "status" from "ready_for_chatgpt_sync" to "deployed_to_github".
   * Update "last_updated" with current timestamp.
5. Output a Deployment Report to the User:


--------------------------------------------------


DEPLOYMENT STATUS: SUCCESS


TARGET PATH: classXX/chXX_name.html


COMMIT HASH: [git commit hash]


LIVE / GITHUB URL: [URL]


MANIFEST STATUS: Updated to deployed_to_github


--------------------------------------------------


________________


5. Verification Rules
* No External Broken Assets: Never convert inline SVGs to external file dependencies.
* Strictly Sequential: Progress from Class 9 Chapter 1 forward; do not skip ahead without manifest sign-off.
* Zero Syntax Errors: Ensure all JavaScript event handlers (onclick) and CSS variables render reliably on mobile and desktop viewports.
