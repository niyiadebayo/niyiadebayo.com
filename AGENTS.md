# AGENTS.md

Operating guide for AI agents (Claude, Codex, any other) working on niyiadebayo.com. Read this before drafting, editing, or shipping anything. Update it at the end of any session that teaches something durable.

## Site in one paragraph

Static site. Pure HTML + one CSS file. No JS framework. Hosted on GitHub Pages from `main`. One HTML file per article. One `index.html` (two-column grid: primary column for bio + writing list, sidebar for press, investments, bookshelf). Single `style.css` handles dark/light via `prefers-color-scheme`. `feed.xml` (RSS 2.0) and `sitemap.xml` are maintained by hand.

## Author voice (non-negotiable)

Adeniyi writes like an operator who has been in the markets he describes. Hard rules:

1. **Brevity as skeleton, data as muscle, story as skin.** Short sentences. Numbers embedded in prose. Ground-level anchor for every abstract claim within two sentences.
2. **No AI-speak — scan twice.** The pattern `"X is not Y. It is Z."` is the single biggest tell. It survives a first-pass edit easily. After the first voice pass, grep for `is not .*\. It is` and `are not .*\. They are` and rewrite every hit. Natural contrasts are fine when the contrast *is* the insight — prefer `"not only X but Y"` or fragment constructions over the paired-sentence contrast. Max one paired-sentence contrast per essay, and it has to earn it.
3. **Em dashes are rare.** Ghost-written and LLM prose leans hard on em dashes (`—`). Adeniyi's published voice uses almost none. Rewrite them: period + fragment, comma, or parentheses. The only em dash that belongs on a page is the one in `<title>Article — Adeniyi Adebayo</title>`. After drafting, grep the body for `—` and eliminate every one unless you can defend it.
4. **No hollow adjectives:** innovative, exciting, unique, transformative, groundbreaking, seamless, robust.
5. **No academic transitions:** Moreover, Furthermore, Additionally, It is worth noting, Indeed, In conclusion.
6. **Active voice default.** Passive only when the object is genuinely more important than the actor.
7. **Thinker references are scaffolding, not decoration.** State the finding, not the CV. `"Glaeser quantified the mechanism"` not `"Glaeser's research at Harvard quantified."` One thinker per section maximum.
8. **First-person sparingly and specifically.** `"I have watched this play out across thirty markets"` is a boast and reads cheesy. When first-person is needed, anchor it: `"I have watched the pattern from Dakar to Karachi to Lima"` or `"In Lusaka, we watched transport companies that started with a handful of vehicles…"`. Never open an essay with first-person.
9. **Ground anchors:** Lagos, Accra, Dakar, Nairobi, Abidjan, Addis, Lusaka, Kumasi, Kasoa, Prampram, Bolgatanga, Tamale, specific streets, specific prices in local currency. No "emerging markets generally."
10. **Vehicle and brand vocabulary.** Use globally-recognized brands when they fit: **Bajaj Boxer, Honda, Suzuki** for motorcycles. **Toyota Vitz, Toyota Corolla** for cars. Avoid local-only brands (Apsonic, Haojue) unless the point is specifically about the local commercial stock — and even then, lead with the recognizable brand.
11. **Vocabulary nits.** *Credit score* (not bureau score). *Farmgate price* (not producer price) for cocoa. *Cedi* lowercase except at sentence start.

## Article HTML template

Every article starts with this exact head structure (copy from the most recent article — currently `inflations-uneven-tax.html`):

- `<title>` = "Article Name — Adeniyi Adebayo"
- `<meta description>` = ~25 words, hook-oriented
- `<link rel="canonical">` = full URL
- OG tags: title, description, type=article, url, article:author, og:image (always `/headshot.jpg`)
- Twitter card: summary, @niyiadebayo, title, shorter description
- JSON-LD Article schema with author Person object
- `<link rel="icon" href="/favicon.svg">`, apple-touch-icon, RSS alternate
- `<link rel="stylesheet" href="style.css">`

Body structure:
```
<main>
  <p class="back"><a href="/">&larr; Home</a></p>
  <article>
    <h1>Title</h1>
    <p>Opening hook — specific, grounded, one or two numbers.</p>
    ...
    <h2>Section header</h2>
    ...
    <section class="footnotes"><ol>...</ol></section>
    <div class="share">X, LinkedIn, Copy link buttons</div>
  </article>
</main>
```

Section headers are short nouns or noun phrases, not sentences. Lowercase-style ("The vault", "The urban ladder", "When the pattern breaks"), not title case.

## Q&A interview process

Drafting an essay is a conversation, not a monologue.

1. **One question at a time.** Journalistic, not survey-batch. CLAUDE.md enforces this globally.
2. **Start with the thesis hook.** "What do you see about X that most people get wrong?"
3. **Push for data as muscle.** Every claim needs a number the author can stand behind. When the author gives a number, cross-check it (see Data discipline below).
4. **Ask one sharpening question per round.** After each answer, identify the weakest part of the reasoning and push there.
5. **Propose structure before drafting.** Title options, section list, word target, thinker scaffolding, cross-links. Get a yes before writing.
6. **Draft in one pass.** Do not draft section-by-section with back-and-forth approval. Write the whole thing, then revise against the voice rules and data.

## Data discipline

Adeniyi's writing lives or dies on numbers.

- **Verify every number before it lands in prose.** Memory is not a source. The web is. Use a background research agent for fact-checks that span multiple sources — Jiji/Tonaton prices, COCOBOD announcements, World Bank CPI, exchange rate series, etc.
- **Cite in footnotes, not inline.** Inline citations clutter voice. Use superscript footnote refs and a `<section class="footnotes">` block at the end.
- **Be honest about uncertainty.** If a 2022 archived listing is unavailable, say so and use the best proxy (contemporaneous press guide, inferred from CPI+FX). Do not fabricate specificity.
- **Prefer primary sources** (Ghana Statistical Service, COCOBOD announcements, Bank of Ghana, World Bank, company annual reports) over aggregators where available.
- **USD translations belong next to local-currency anchors** when writing about soft-currency economies. The essay loses its teeth without the FX overlay.

## Cross-link conventions

- **Bidirectional.** Every new essay that references an existing one should have at least one backlink added to the referenced article — in a spot that fits the existing voice, not shoehorned.
- **One link per idea.** Do not link "financing loop" three times in one essay.
- **Link text carries meaning.** Prefer `<a href="/financing-loop.html">The financing loop</a>` over `<a href="/financing-loop.html">here</a>`.
- **Keep shared stats in the primary article.** When a stat (e.g. $9.3T dead capital, 1.15 superlinear exponent, 30% density wage premium) appears in multiple essays, the full version lives in the primary article and other essays link to it instead of repeating the framing.

## Publishing checklist

Every new article, every time:

1. Draft via Q&A interview.
2. AI-speak pass — scan for banned patterns (see Voice).
3. Voice consistency check — read against the two most recent articles.
4. Data verification pass — every number has a footnote or explicit source.
5. Cross-links added inside the new essay.
6. Cross-links added bidirectionally into referenced articles.
7. Add to `index.html` writing list (correct position in thematic arc).
8. Prepend `<item>` to `feed.xml`, update `<lastBuildDate>`.
9. Add `<url>` to `sitemap.xml`, update homepage `<lastmod>` and new-article `<lastmod>`.
10. Bookshelf updated in `index.html` if a new thinker is cited heavily.
11. Commit with a descriptive message. Push.

## Thematic arc in the index

The `index.html` writing list is not chronological. It is a thesis arc:

1. **Thesis** — cities, density-dividend
2. **Ground-level** — first-72-hours, pricing-as-language
3. **Systems** — second-player, no-float-expected, financing-loop, informal-stack, inflations-uneven-tax, boring-businesses
4. **Macro** — entropy-and-marketplaces, addis-ababa, leapfrog
5. **Personal** — know-thyself

When adding a new article, slot it by theme, not date. The reader should be able to read top-to-bottom as a developing argument.

## Thinker registry

Avoid re-citing. When a thinker appears in more than one article, state the finding in the primary and link/reference lightly in others.

| Thinker | Primary article | Concept |
|---|---|---|
| Geoffrey West | density-dividend | Superlinear 1.15 exponent |
| Edward Glaeser | density-dividend | 30% wage premium, 50% urbanization threshold |
| Jane Jacobs | density-dividend | Four conditions, import replacement, "new work" |
| Hernando de Soto | informal-stack | $9.3T dead capital, 289-day registration |
| James Scott | informal-stack | Metis, thin simplifications, legibility |
| Acemoglu & Robinson | informal-stack | Extractive vs inclusive institutions |
| Thomas Piketty | inflations-uneven-tax | r > g amplified by FX + urbanization in EMs |

Add a row here whenever a new thinker is cited heavily for the first time.

## Session kickoff protocol

Before starting a new essay session:

1. `ls *.html` to see current article inventory.
2. `git log --oneline -20` to see what shipped recently.
3. Check `index.html` writing list for the current arc.
4. Do **not** trust memory files for "what's next" — the cadence drifts.
5. Ask the author what they want to write. Do not assume from a stale plan.

## Known constraints

- **Preview server:** macOS App Sandbox prevents Claude Preview's python3 from accessing `~/Documents`. The author opens files directly in a browser or runs a server from their terminal.
- **Headshot path:** Uses absolute `/headshot.jpg`. Does not render from `file://` URLs, works on GitHub Pages.
- **No JS:** Site is pure HTML/CSS. No analytics, no interactivity. The only JS in the repo is the one-line Copy Link button.
- **No auto-build:** `feed.xml` and `sitemap.xml` are hand-maintained. There is no generator.

## Updating this file

Update `AGENTS.md` at the end of any session that:

- Adds a voice rule (because you caught the author correcting you on phrasing)
- Adds a structural convention (new footer pattern, new SEO tag, new share button)
- Adds a thinker to the registry
- Uncovers a gotcha worth preserving (path issue, rendering bug, tool quirk)
- Changes the thematic arc of the index

Commit the update in the same commit as the thing it describes, with a short note in the commit message.
