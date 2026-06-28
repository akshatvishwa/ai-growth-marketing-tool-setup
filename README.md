# AI Growth Marketing Tool Setup

## Project Overview

This repository documents my portfolio project for the Junior Growth Marketing Specialist application at 100Hires.

The project started with setting up AI-assisted work tools such as Cursor, Claude Code, Codex, and GitHub. It then expanded into a research project on **AI-powered SEO content production for B2B SaaS**.

The goal of this repository is to demonstrate that I can:

* follow instructions carefully
* learn new tools independently
* troubleshoot technical issues
* use AI-assisted workflows
* collect and organize research
* document work clearly
* synthesize research into practical marketing insights

---

# Step 1: AI Tool Setup

## Tools Used

### 1. Cursor IDE

I installed and opened Cursor IDE as the main AI-assisted workspace.

Purpose:

* To explore an AI-native work environment
* To understand how modern AI tools can support project execution
* To manage project files and documentation
* To create and edit project files

---

### 2. Claude Code

I searched for Claude Code inside Cursor.

Status:

* Claude Code was found inside Cursor's marketplace/plugins area.
* I explored the available option as part of the setup process.

Purpose:

* To understand how Claude Code can support AI-assisted execution inside Cursor
* To explore how AI tools can help with documentation, research, and technical workflows

---

### 3. Codex

I searched for Codex inside Cursor.

Status:

* Codex did not appear as a normal plugin in the same way as Claude Code.
* When I searched for "Codex" inside Cursor, I found "Codex 5.3" under "New Agent with Model."
* I documented this because the Cursor interface was slightly different from the original instruction wording.

Purpose:

* To explore how Codex-style AI assistance can support technical and structured execution tasks
* To understand how different AI tools may appear in different parts of the Cursor interface

---

### 4. GitHub

I created a public GitHub repository to host this project.

Repository purpose:

* To document the setup process publicly
* To demonstrate comfort with basic GitHub workflow
* To create a portfolio asset that can be shared with employers

---

## Step 1 Work Completed

1. Installed Cursor IDE.
2. Opened Cursor and explored the main interface.
3. Opened the Customize section in Cursor.
4. Checked Cursor's marketplace/plugins area.
5. Searched for Claude Code.
6. Found Claude Code in Cursor.
7. Searched for Codex.
8. Found Codex 5.3 as a "New Agent with Model" option inside Cursor search.
9. Created a public GitHub repository.
10. Added a README.md file.
11. Documented the setup process, issues faced, and learnings.

---

## Issues Faced and How I Solved Them

### Issue 1: Cursor interface was different from the instruction wording

The instruction mentioned installing add-ons/extensions, but the Cursor interface I saw showed sections like Customize, Plugins, MCPs, Skills, Subagents, Rules, Commands, and Hooks.

How I handled it:

* I explored the visible Cursor interface instead of stopping.
* I opened the Customize section.
* I checked the available marketplace/plugins area.
* I searched manually for the required tools.

---

### Issue 2: Finding Claude Code

I searched for Claude Code inside Cursor.

How I handled it:

* I used Cursor's marketplace/plugins search.
* I was able to find Claude Code.
* I documented it as part of the completed setup process.

---

### Issue 3: Codex appeared differently inside Cursor

When I searched for Codex, I did not find it as a normal plugin listing in the same way as Claude Code. However, Cursor showed "Codex 5.3" under "New Agent with Model."

How I handled it:

* I searched directly for "Codex."
* I reviewed the results that appeared.
* I avoided installing unrelated tools.
* I documented the exact result I found: "Codex 5.3" under "New Agent with Model."

This helped me understand that tool interfaces can differ from written instructions, and it is important to document what was actually found.

---

### Issue 4: GitHub workflow was new to me

I do not come from a traditional software development background, so creating a repository and documenting the workflow on GitHub was a useful learning step.

How I handled it:

* I created a public GitHub repository.
* I added a README.md file.
* I used GitHub's editor and Cursor to document the work clearly.
* I treated the task as a practical learning exercise.

---

## Step 1 Learnings

This task helped me understand the basics of working with AI-assisted tools and GitHub documentation.

Key learnings:

* How to install and open Cursor IDE
* How to explore Cursor's Customize and marketplace areas
* How to search for AI tools inside Cursor
* How to document issues clearly instead of ignoring them
* How to create a public GitHub repository
* How to edit and organize a README.md file
* How to present a technical setup process in a structured way

From a growth marketing perspective, this workflow is useful because modern growth roles increasingly require comfort with AI tools, documentation, experimentation, and fast independent learning.

---

# Step 2: Research Project

## Topic Chosen

**AI-powered SEO content production for B2B SaaS**

---

## Why I Chose This Topic

I chose this topic because B2B SaaS SEO is changing quickly.

Search is no longer limited to ranking blog posts on Google. Buyers now discover and evaluate brands across Google Search, AI Overviews, ChatGPT, Gemini, Perplexity, YouTube, LinkedIn, Reddit, review sites, comparison pages, communities, newsletters, podcasts, and third-party sources.

The goal of this research project is to understand how modern SEO and content teams can build AI-visible content systems that support business outcomes, not just traffic.

---

## Research Thesis

B2B SaaS SEO is shifting from keyword-only content production to AI-visible content systems built around:

* expert insight
* audience research
* prompt research
* content quality
* topical authority
* off-site visibility
* E-E-A-T
* third-party citations
* AI visibility measurement
* business impact beyond traffic

---

## Experts Researched

This project includes research from 10 experts:

1. Kevin Indig
2. Aleyda Solis
3. Ryan Law
4. Eli Schwartz
5. Ross Simmonds
6. Bernard Huang
7. Mike King
8. Amanda Natividad
9. Alex Birkett
10. Lily Ray

---

## Research Structure

The research is organized inside the `research/` folder.

### Core Research Files

* `research/sources.md` — expert list, topic thesis, and collection summary
* `research/source-quality-scorecard.md` — scoring and reasoning for expert selection
* `research/collection-method.md` — how sources were collected and organized
* `research/patterns-and-insights.md` — synthesis of patterns across all sources

---

### LinkedIn Research Notes

Five LinkedIn expert files were collected manually because LinkedIn API access is limited:

* `research/linkedin-posts/kevin-indig.md`
* `research/linkedin-posts/aleyda-solis.md`
* `research/linkedin-posts/ryan-law.md`
* `research/linkedin-posts/ross-simmonds.md`
* `research/linkedin-posts/amanda-natividad.md`

These files summarize selected LinkedIn posts, including:

* source links
* topic summaries
* tactical takeaways
* B2B SaaS relevance
* AI SEO/content relevance
* risks and limitations
* future playbook use cases

---

### YouTube Transcript Notes

Five YouTube transcript-note files were created:

* `research/youtube-transcripts/eli-schwartz.md`
* `research/youtube-transcripts/bernard-huang.md`
* `research/youtube-transcripts/mike-king.md`
* `research/youtube-transcripts/alex-birkett.md`
* `research/youtube-transcripts/lily-ray.md`

These files summarize YouTube videos and interviews related to SEO, AI search, AEO/GEO, E-E-A-T, B2B SaaS content strategy, and AI visibility.

---

## API / Technical Collection Workflow

To support the YouTube research workflow, I created a Python transcript collection script:

* `tools/youtube_transcript_collector.py`

The script uses:

* `youtube-transcript-api`

The dependency is listed in:

* `requirements.txt`

The script accepts a YouTube URL or video ID, extracts the video ID, fetches the English transcript where available, and saves the transcript locally inside:

* `research/youtube-transcripts/raw/`

Raw transcript files were not republished in full. Instead, I created structured research notes summarizing the relevant ideas, tactical takeaways, B2B SaaS relevance, AI SEO relevance, risks, and future playbook use cases.

A `.gitignore` file was added inside the raw transcript folder to avoid accidentally committing full transcript text.

---

## Key Research Output

The main synthesis file is:

* `research/patterns-and-insights.md`

This file identifies:

* key patterns across all experts
* areas of agreement
* differences between experts
* implications for B2B SaaS teams
* practical frameworks
* open questions and limitations
* a future playbook outline

---

## Main Research Insight

The strongest pattern from this research is that AI-powered SEO content production is not about replacing writers with AI.

It is about building a better system for:

* understanding buyers
* mapping prompts
* creating expert-led content
* earning trust across third-party sources
* measuring AI visibility
* improving representation accuracy
* connecting SEO to business outcomes

For B2B SaaS, the winning teams will not be the ones that publish the most AI-generated articles. The winning teams will be the ones that use AI to build more useful, more trusted, more visible, and more strategically distributed content systems.

---

# Current Status

The project currently includes:

* Cursor, Claude Code, Codex, and GitHub setup documentation
* 10 selected experts
* 5 LinkedIn research files
* 5 YouTube transcript-note files
* YouTube transcript collector script
* Requirements file for the transcript tool
* Source quality scorecard
* Collection method documentation
* Cross-source research synthesis

The core research collection phase is complete.

---

# Next Step

The next step would be to turn the research synthesis into a practical playbook for B2B SaaS teams on AI-powered SEO content production.
