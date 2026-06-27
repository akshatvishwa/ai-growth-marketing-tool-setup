# YouTube Transcript Collector Plan

## 1. Goal of the Workflow

This workflow collects **research notes** from YouTube videos published by SEO, content, and B2B SaaS growth practitioners.

The project topic is **AI-powered SEO content production for B2B SaaS**. YouTube is a strong source for this research because many experts share tactical advice on AI search visibility, content systems, audience research, distribution, and measurement.

The goal is **not** to copy entire videos into this repository. The goal is to:

- Capture enough transcript-based material to understand what each expert recommends
- Turn that material into structured notes that support a future playbook
- Keep a consistent file format so many videos can be reviewed and compared later

This workflow supports technical collection where APIs or transcript tools are available, with a clear manual fallback when they are not.

---

## 2. Input Fields

Before collecting a video, fill in these fields. They become the top of each research note file.

| Field | Description | Example |
| --- | --- | --- |
| **Expert name** | The practitioner speaking in the video | Kevin Indig |
| **YouTube URL** | Full link to the video | `https://www.youtube.com/watch?v=...` |
| **Video title** | Exact title as shown on YouTube | How AI Search Is Changing SEO |
| **Topic** | Short label for why this video matters to the project | AI search visibility for B2B SaaS |

Optional but useful when available:

- Channel name
- Published date
- Video length

---

## 3. Collection Method

Use transcript-based collection first. Try methods in this order.

### Option A: YouTube Transcript API / transcript extraction tools

Many YouTube videos include auto-generated or uploaded captions. Common approaches:

- **Python libraries** such as `youtube-transcript-api` (community tool; not an official Google API)
- **Browser or CLI transcript extractors** that read publicly available caption tracks
- **Cursor / Claude Code / Codex** to run a small script that fetches the transcript and saves it locally for note-taking

Basic steps:

1. Paste the YouTube URL and confirm captions exist on the video page.
2. Run the transcript tool against the video ID.
3. Save the raw transcript temporarily for your own review (local only).
4. Convert the transcript into structured research notes (see Section 6).
5. Store the final note in `research/youtube-transcripts/`.

### Option B: Supadata API

[Supadata](https://supadata.ai/) and similar services provide transcript endpoints for YouTube URLs when direct extraction is awkward or blocked.

Use Supadata when:

- A script fails because of rate limits, region blocks, or missing caption metadata
- You want a single API-style workflow for many URLs
- You are documenting a technical collection method for the portfolio assignment

Basic steps:

1. Send the YouTube URL to the Supadata transcript endpoint (per their docs).
2. Receive transcript text or timed segments.
3. Summarize into structured notes; do not commit full raw transcript text unless required for assignment proof—and prefer summaries in the final repo.

### Option C: Manual collection inside Cursor

If APIs and tools work inconsistently, use Cursor to:

- Open the video in a browser
- Copy key sections from the transcript panel or auto-captions
- Ask the AI agent to help structure takeaways into the note template

This still counts as a valid workflow as long as the process and limitations are documented.

---

## 4. Output Folder

All finished YouTube research notes go here:

```text
research/youtube-transcripts/
```

### Suggested file naming

Use a consistent, readable pattern:

```text
research/youtube-transcripts/{expert-slug}--{short-topic-slug}.md
```

Examples:

- `research/youtube-transcripts/kevin-indig--ai-search-visibility.md`
- `research/youtube-transcripts/aleyda-solis--seo-ai-overviews.md`

Each file should contain metadata, key takeaways, B2B SaaS relevance, and playbook potential—not a full transcript dump.

---

## 5. Fallback Method If Transcript Is Unavailable

Some videos have no captions, disabled transcripts, or blocked access. When that happens:

1. **Watch the video** and take timestamped notes manually.
2. **Capture from description and chapters** if the creator listed key points.
3. **Check for alternate formats** by the same expert (blog recap, LinkedIn post, podcast show notes).
4. **Record the limitation** in the note file under a `Collection status` field, for example:
   - `Transcript unavailable — manual notes from video`
   - `Partial captions only — summary based on first 10 minutes`
5. **Still save a structured note** so the source is not lost from the research set.

Do not skip the video entirely just because automation failed. The fallback keeps the research complete and honest about what was possible.

---

## 6. Metadata to Collect

Every YouTube research note should include these sections.

### Required metadata

- Expert name
- YouTube URL
- Video title
- Topic (project-specific label)
- Collection method used (YouTube transcript tool, Supadata, manual)
- Transcript availability (yes / partial / no)
- Date collected

### Recommended metadata

- Channel name
- Video published date
- Video duration
- Speaker role or company (if stated)
- Source quality check (see `research/source-quality-scorecard.md`)

### Research content fields

- **Main idea** — one or two sentences on what the video is about
- **Key takeaways** — bullet list of the most useful points
- **Tactical steps** — anything that could become a playbook step
- **B2B SaaS relevance** — why this matters for SaaS teams specifically
- **AI SEO / content relevance** — connection to AI search, AI-assisted production, or content systems
- **Risks or limitations** — where the advice may not apply
- **Playbook hook** — which future playbook section this could support (strategy, production, distribution, measurement, etc.)
- **Notable quotes** — short phrases only, with timestamp if possible (not long blocks of text)

### Example note skeleton

```markdown
# {Video title}

## Metadata
- **Expert:** {name}
- **URL:** {youtube url}
- **Topic:** {topic}
- **Channel:** {channel}
- **Published:** {date}
- **Collected:** {date}
- **Method:** YouTube transcript API / Supadata / manual
- **Transcript:** available | partial | unavailable

## Main idea

## Key takeaways

## Tactical steps

## B2B SaaS relevance

## AI SEO / content relevance

## Risks or limitations

## Playbook hook

## Notable quotes
```

---

## 7. Why Full Transcripts Should Not Be Republished Publicly

Full YouTube transcripts should **not** be republished in this public GitHub repository.

Reasons:

1. **Copyright** — Video transcripts are part of the creator's content. Copying and republishing entire transcripts can infringe on their rights, even when captions are publicly viewable on YouTube.
2. **Platform terms** — Automated bulk downloading or redistribution may conflict with YouTube's terms of service or third-party API rules.
3. **Research purpose** — This project needs **analysis**, not a transcript archive. Employers and reviewers care about structured thinking, not raw text dumps.
4. **Quality and readability** — Auto-captions are often noisy. Summarized notes are more useful for building a playbook.
5. **Ethical use** — Experts share videos to build audience and authority. The respectful approach is to cite the source, summarize insights, and link back to the original video.

**What to do instead:**

- Link to the original YouTube URL
- Save short quotes with attribution and timestamps when needed
- Write original summaries and tactical takeaways in your own words
- Keep full raw transcripts local and private if you need them temporarily for analysis

---

## 8. How This Supports a Future B2B SaaS AI SEO Playbook

This workflow is the **YouTube intake layer** for a larger research system documented in:

- `research/sources.md` — expert list and research focus
- `research/collection-method.md` — overall collection approach
- `research/source-quality-scorecard.md` — expert evaluation criteria

YouTube notes feed the playbook by:

| Playbook need | What YouTube collection provides |
| --- | --- |
| **Strategy** | How practitioners frame AI search, topical authority, and B2B buying journeys |
| **Production** | Workflows for AI-assisted drafting, editing, QA, and human expertise |
| **Audience research** | Methods for ICP research, zero-click content, and message validation |
| **Distribution** | LinkedIn, YouTube, newsletters, and multi-channel organic growth tactics |
| **Measurement** | Metrics beyond traffic: visibility in AI answers, engagement, pipeline influence |
| **Risk awareness** | Where generic AI content fails and what guardrails experts recommend |

Over time, patterns across many videos will show:

- Repeated frameworks worth turning into playbook chapters
- Conflicting advice that needs context for B2B SaaS
- Gaps where your playbook can add original structure

The end state is not a folder of transcripts. The end state is a **practical B2B SaaS AI SEO playbook** built from verified practitioner insight—with YouTube as one structured evidence source.

---

## Quick Start Checklist

1. Pick an expert from `research/sources.md`.
2. Choose a relevant YouTube video and fill in the four input fields (expert, URL, title, topic).
3. Try transcript collection (YouTube transcript tool → Supadata → manual fallback).
4. Create a note file in `research/youtube-transcripts/` using the skeleton above.
5. Score usefulness against `research/source-quality-scorecard.md`.
6. Link the note back to the broader research plan in `research/collection-method.md`.
