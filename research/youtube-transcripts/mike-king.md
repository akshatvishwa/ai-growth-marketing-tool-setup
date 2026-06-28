# Mike King — YouTube Transcript Notes

## Expert
Name: Mike King
Role: CEO and founder of iPullRank; chief relevance engineer
Primary Area: Relevance Engineering, enterprise SEO, AI search systems, query fan-out, semantic retrieval

## Source
Title: Mike King on relevance engineering and the end of SEO as we know it
Format: YouTube video / interview (Search Engine Land)
Link: https://www.youtube.com/watch?v=eS4kfPUfFog
Transcript Collection Method: Collected using tools/youtube_transcript_collector.py with youtube-transcript-api
Raw Transcript: Stored locally in research/youtube-transcripts/raw/eS4kfPUfFog.txt and not republished in full

## Why This Source Was Selected
Mike King is one of the most technical voices in modern SEO—combining a computer science background with enterprise client work—and he coined **Relevance Engineering** as a framework for operating in AI-driven search. This interview directly addresses how Google’s systems now understand meaning through embeddings, query expansion, knowledge graph context, and chunk retrieval—not keyword matching alone. For a B2B SaaS AI SEO playbook, King’s perspective is essential because he explains *why* legacy SEO tooling and tactics fail, what **query fan-out** means in practice, and how practitioners must shift from ranking pages to engineering relevance across passages, entities, and brand surfaces.

## Summary
- **Relevance Engineering** is King’s proposed reinvention of SEO: a more scientific, engineering-led discipline that blends AI, information retrieval, content strategy, UX, and digital PR—replacing checklist optimization built on outdated lexical models.
- Google moved beyond keyword matching roughly a decade ago, but most SEO software still counts word presence and approximates link graphs—leaving the industry **~10 years behind** how search actually works today.
- **Query fan-out** is central to AI Mode and AI Overviews: Google hands the user query to a customized Gemini model, which returns expanded sub-queries plus knowledge graph signals; background searches run, **chunks** are pulled from pages, and Gemini synthesizes the final answer—meaning visibility depends on expanded queries, not the visible head term alone.
- A page ranking #52 for the surface query may still be cited if it ranks strongly for one **fan-out sub-query**—explaining why traditional rank-tracking and “optimize what ranks #1” advice misleads AI search strategists.
- King advocates **embedding-based content audits** (e.g., site focus score from the Google leak): represent the whole site as an embedding, measure page distance from the site’s topical center, and prune off-topic content to lift overall performance.
- Search is increasingly a **branding channel**: zero-click AI surfaces still influence purchase decisions (e.g., seeing “Apple AirPods” in an overview), drive branded follow-up searches, and can yield more qualified clicks when users do visit—conversions may rise even as traffic falls.
- The path forward is **engineering, not optimization**—building open-source tools that replicate fan-out behavior, measure chunk relevance, and surface retrieval signals—because Google will not expose enough telemetry for practitioners to rely on blog-post best practices alone.
- SEO will **split**: one camp clings to 25-year-old best practices; another tests rigorously, builds tooling, and treats search as a volatile systems problem requiring reinvention.

## Tactical Takeaway
- Map **query fan-out paths** for priority topics—identify the sub-queries AI systems generate in the background and ensure you have strong, chunk-ready content ranking for those expansions, not only the parent prompt.
- Audit content with **semantic/site-embedding distance**, not just traffic or keywords: remove or consolidate pages that sit too far from your core topical focus to strengthen entity clarity for Google and AI retrieval.
- Reframe client reporting around **brand influence, citations, impressions, and qualified conversions**—not rankings and raw clicks alone—because AI surfaces decouple visibility from traditional SERP position.

## B2B SaaS Relevance
- iPullRank serves **enterprise B2B clients** (e.g., SAP mentioned elsewhere in King’s work); his framing applies to complex buying journeys where search influences consideration even when it does not drive immediate self-serve conversion.
- B2B SaaS teams relying on keyword-stuffed blogs and legacy SEO platforms are optimizing for a **lexical search model that no longer governs** AI Overviews, AI Mode, or agentic retrieval—creating a false sense of progress while fan-out sub-queries go uncovered.
- Enterprise content libraries with sprawling, off-topic blog volume hurt **site-level topical coherence** in embedding space—especially risky for B2B brands trying to be cited as authoritative in narrow categories (security, analytics, HR tech, etc.).
- For B2B, the strategic conversation King describes—traffic down, conversions stable or up, search as **mindshare**—helps SEO/content leaders justify AI-era investment to executives still measured on organic sessions.
- B2B SaaS should invest in **passage-level relevance** for product, integration, comparison, and category pages that fan-out queries will retrieve—rather than publishing generic thought leadership disconnected from entity relationships buyers and agents explore.

## AI SEO / Content Relevance
- AI search is a **retrieve-then-synthesize pipeline**: expanded queries → background SERP fetches → chunk extraction → LLM answer—so content strategy must optimize **chunks and passages** for extractability across many related queries, not one keyword per page.
- **Meaning, entities, and context** replace keyword density: knowledge graph data, personal context, reasoning, deep search, and multimodality (video, translation) mean Google matches intent and entity relationships—not word lists.
- Industry guidance to “look at what ranks and optimize” fails because practitioners cannot see **which fan-out query** earned a citation; a page invisible on the head term may still win a sub-query slot.
- King is building tooling to **replicate fan-out behavior** (Gemini-based query expansion)—signaling that AI SEO maturity requires custom engineering, not off-the-shelf rank trackers with ChatGPT bolted on.
- **Structured data, technical accessibility, and site focus** remain foundational inputs, but how Google “chops and screws” content in AI responses means operators lose direct control over presentation—making entity clarity and chunk relevance the levers that remain.

## Risk or Limitation
- Relevance Engineering is an **emerging framework**, not a standardized practice—teams adopting it need internal technical capability or agency partners willing to build tooling, not just audit checklists.
- Google provides **limited transparency** on AI search behavior changes, forcing SEOs to prove traffic declines to clients without official guidance—creating credibility and budget risk for B2B marketing leaders.
- Embedding-based pruning and fan-out content expansion can be misapplied: deleting useful mid-funnel pages or over-expanding thin pages without engineering rigor could harm both classic search and AI retrieval.
- King’s critique of the SEO software industry is accurate but leaves **most teams without ready-made tools**—implementation gap is wide for mid-market B2B SaaS without enterprise SEO budgets.

## Use in Future Playbook
- **Relevance Engineering pillar:** Define the discipline for the playbook as AI + retrieval + content + UX + PR—explicitly moving B2B SaaS teams beyond keyword SEO and AI content slop.
- **Query fan-out research module:** Step-by-step workflow to discover fan-out sub-queries, map current rankings/citations per sub-query, and build an omnimedia content plan covering the expansion set.
- **Semantic content audit chapter:** Include site-embedding distance audits, topical pruning rules, and entity-consistency checks before scaling AI-assisted content production.
- **AI visibility measurement:** Document citation tracking, impression interpretation, branded search lift, and conversion-quality metrics as replacements for rank-and-traffic-only reporting to B2B executives.
- **Engineering vs. optimization mindset:** Recommend when B2B SaaS teams should build or adopt fan-out/chunk-relevance tooling versus relying on legacy platforms—and tie passage structure guidelines to extractability in AI answers.
