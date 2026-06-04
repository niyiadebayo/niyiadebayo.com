# AGENTS.md

Operating guide for AI agents (Claude, Codex, any other) working on niyiadebayo.com. Read this before drafting, editing, or shipping anything. Update it at the end of any session that teaches something durable.

## Site in one paragraph

Static site. Pure HTML + one CSS file. No JS framework. Hosted on GitHub Pages from `main`. One HTML file per article. One `index.html` (two-column grid: primary column for bio + the full writing list grouped by thematic arc with bold Title-case sub-heads; right-rail sidebar for press, investments, bookshelf). Single `style.css` handles dark/light via `prefers-color-scheme`. `feed.xml` (RSS 2.0) and `sitemap.xml` are maintained by hand.

## Author voice (non-negotiable)

Adeniyi writes like an operator who has been in the markets he describes. Hard rules:

1. **Brevity as skeleton, data as muscle, story as skin.** Short sentences. Numbers embedded in prose. Ground-level anchor for every abstract claim within two sentences.
2. **No AI-speak — scan twice.** The pattern `"X is not Y. It is Z."` is the single biggest tell. It survives a first-pass edit easily. After the first voice pass, grep for `is not .*\. It is` and `are not .*\. They are` and rewrite every hit. Natural contrasts are fine when the contrast *is* the insight — prefer `"not only X but Y"` or fragment constructions over the paired-sentence contrast. Max one paired-sentence contrast per essay, and it has to earn it.
3. **Em dashes are rare.** Ghost-written and LLM prose leans hard on em dashes (`—`). Adeniyi's published voice uses almost none. Rewrite them: period + fragment, comma, or parentheses. The only em dash that belongs on a page is the one in `<title>Article — Adeniyi Adebayo</title>`. After drafting, grep the body for `—` and eliminate every one unless you can defend it.
4. **No hollow adjectives:** innovative, exciting, unique, transformative, groundbreaking, seamless, robust.
5. **No academic transitions:** Moreover, Furthermore, Additionally, It is worth noting, Indeed, In conclusion.
6. **Active voice default.** Passive only when the object is genuinely more important than the actor.
7. **Thinker references are scaffolding, not decoration.** State the finding, not the CV. `"Glaeser quantified the mechanism"` not `"Glaeser's research at Harvard quantified."` One thinker per section maximum.
8. **First-person sparingly and specifically.** `"I have watched this play out across thirty markets"` is a boast and reads cheesy. When first-person is needed, anchor it: `"I have watched the pattern from Dakar to Karachi to Lima"` or `"In Lusaka, we watched transport companies that started with a handful of vehicles…"`. Prefer reciprocal framing over detached observation: `"Ridehail taught me this clearly"` reads more like him than `"I observed this across markets."` The markets teach; the operator learns. Never open an essay with first-person.
9. **Ground anchors:** Lagos, Accra, Dakar, Nairobi, Abidjan, Addis, Lusaka, Kumasi, Kasoa, Prampram, Bolgatanga, Tamale, specific streets, specific prices in local currency. No "emerging markets generally."
10. **Vehicle and brand vocabulary.** Use globally-recognized brands when they fit: **Bajaj Boxer, Honda, Suzuki** for motorcycles. **Toyota Vitz, Toyota Corolla** for cars. Avoid local-only brands (Apsonic, Haojue) unless the point is specifically about the local commercial stock — and even then, lead with the recognizable brand.
11. **Vocabulary nits.** *Credit score* (not bureau score). *Farmgate price* (not producer price) for cocoa. *Cedi* lowercase except at sentence start.
12. **Personal arc reads personable, not operator.** The Personal essays (e.g. boy-from-saki) are memoir, not analysis. Prefer first-person lived detail over generalized takeaways. No paragraph-closing aphorisms (the "and the lesson is…" cap), no product/scale boasts ("the largest super-app on the continent"), no second-person advice ("tear each problem down" should be "I tore each problem down"). When the author hands you raw phrasing ("something I couldn't be scared of", "pushing the envelope on when what is possible"), keep it; do not polish it into operator-speak — that polishing was the exact regression caught on this arc. Footnotes were dropped here at the author's request; cite inline and lightly, if at all.

## Operator worldview (keep essays coherent with it)

Adeniyi writes from a consistent strategic position, stated plainly in how he frames the work publicly (e.g. Bloomberg, May 2026: "a lot of capital chasing the same goal... a race to the bottom"; "we don't work directly with drivers... we work with transport operators"). New essays should reinforce these convictions, not contradict them. Keep the conviction, vary the evidence:

- **Density over headcount; secondary cities over the top four.** Capital piles into Lagos, Cairo, Johannesburg, and Nairobi and bids itself into a race to the bottom. The opening is the secondary cities the top four crowd out. (Primary: cities, density-dividend, second-player.)
- **Work through local operators, not gig workers directly.** Partnering with transport operators lowers subsidy burn and builds on trust that already exists. (Primary: distribution-stack, financing-loop, no-float-expected.)
- **Mobility is the wedge; the ecosystem is the prize.** One daily-use service is the entry point, then transport, commerce, payments, and credit connect into a platform people depend on. (Primary: identity-premium, distribution-stack.)
- **Instrument the informal economy, don't formalize it.** Add the data layer that makes informal assets and actors legible to capital without stripping the metis that makes them work. (Primary: informal-stack, financing-loop.)
- **Subsidy is a tax on getting the model wrong.** Daily cash, dense agent meshes, and local operators beat burning capital to paper over a model that fights the market. (Primary: no-float-expected.)

His public register is blunt and operator-first ("we've barely started"), the same voice rule 8 asks for: the markets teach, the operator learns.

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
  <p class="back"><a href="/">&larr; Home</a><span class="crumb">Bucket &middot; N of M</span></p>
  <article>
    <h1>Title</h1>
    <p>Opening hook — specific, grounded, one or two numbers.</p>
    ...
    <h2>Section header</h2>
    ...
    <section class="footnotes"><ol>...</ol></section>
    <div class="share">X, LinkedIn, Copy link buttons</div>
    <nav class="arc-nav">
      <a class="prev" href="/PREV.html"><span class="lbl">Previous</span><span class="ttl">Prev title</span></a>
      <a class="next" href="/NEXT.html"><span class="lbl">Next</span><span class="ttl">Next title</span></a>
    </nav>
  </article>
</main>
```

Body text renders in a **reading serif** (Charter/Georgia system stack; headings stay sans). The `.crumb` shows the essay's position in its arc bucket (e.g. `Systems · 3 of 8`); a single-item bucket shows just the name (e.g. `Personal`). The `.arc-nav` gives **previous/next in arc order** so the collection reads as one developing argument — the first essay omits `.prev`, the last omits `.next`. All styled in `style.css` under the "Delight" block. Content links animate an underline on hover; footnotes glow via `:target` when jumped to.

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

**Show the rendered prose inline in the chat before you commit or publish.** The author reviews
essay text *in the chat as plain text* — not via a styled preview server, and not after it is
already pushed. Paste the full draft for a read-through and wait for the go-ahead before
committing. *(Recurring ask: sessions 84c96ff3, a11e7a5b, f47c47f6, 3507c64c.)*

Every new article, every time:

1. Draft via Q&A interview.
2. AI-speak pass — scan for banned patterns (see Voice).
3. Voice consistency check — read against the two most recent articles.
4. Data verification pass — every number has a footnote or explicit source.
5. Cross-links added inside the new essay.
6. Cross-links added bidirectionally into referenced articles.
7. Add to `index.html` writing list — slot into the correct bucket's `<ul>` by theme, not date.
8. Wire the new essay's `.crumb` (`Bucket &middot; N of M`) and `.arc-nav`. Adding at the end of the arc: the new essay's `.prev` = the old last essay, and that old last essay gains a `.next` pointing to the new one. Inserting mid-arc: fix both neighbours' nav. First essay has no `.prev`, last has no `.next`. Hand-maintained — there is no generator, so this is easy to forget and the nav will silently rot if you do.
9. Prepend `<item>` to `feed.xml`, update `<lastBuildDate>`.
10. Add `<url>` to `sitemap.xml`, update homepage `<lastmod>` and new-article `<lastmod>`.
11. Bookshelf updated in `index.html` if a new thinker is cited heavily.
12. Commit with a descriptive message. Push.

## Thematic arc in the index

The `index.html` writing list is not chronological. It is a thesis arc — ordered so the reader can read top-to-bottom as a developing argument. The full list is shown on the homepage, split into one `.arc-group` per bucket; each bucket's label is a `<h2 class="arc">` **bold Title-case sub-head** (styled in `style.css` under "Writing: thematic arc sub-heads"). This treatment replaced earlier faint uppercase labels that didn't read as grouping.

1. **Thesis** (= "Start here") — cities, density-dividend, the-fiftieth-user
2. **Ground level** — first-72-hours, pricing-as-language
3. **Systems** — second-player, no-float-expected, distribution-stack, identity-premium, financing-loop, informal-stack, inflations-uneven-tax, boring-businesses
4. **Macro** — entropy-and-marketplaces, rails-before-marketplaces, addis-ababa, leapfrog
5. **Personal** — boy-from-saki, mr-fabiyi, know-thyself

When adding a new article, slot it into the right bucket's `<ul>` (by theme, not date), so the reader can read top-to-bottom as a developing argument. Add a new `<h2 class="arc">` bucket only if a genuinely new theme emerges. The page is two-column (writing left, references rail right); the full list is what balances the sidebar at full width. A single-column landing, a "Start here" trio, and a same-page `<details>` "show all" toggle were each tried (May 2026) and reverted — the full two-column list is the chosen layout. Revisit only if the list grows unwieldy.

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
| Marcel Fafchamps | distribution-stack | Relational contracting, <5% use courts in SSA |
| Jack & Suri | distribution-stack | Nonlinear agent density and M-PESA adoption |
| W. Brian Arthur | identity-premium | Increasing returns, lock-in, path dependence |
| Kingsley Davis | the-fiftieth-user | Urban transition, attenuated S-curve |
| Gollin, Jedwab & Vollrath | the-fiftieth-user | Consumption vs production cities, urbanization without industrialization |
| Carlota Perez | rails-before-marketplaces | Installation of infrastructure precedes the deployment era of applications |

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
- **No JS framework:** Site is pure HTML/CSS with no interactivity to speak of. Two small scripts only: the one-line Copy Link button on each article, and the cookieless **Cloudflare Web Analytics** beacon on every page (`data-cf-beacon` token `2859…1538`). Traffic is read at dash.cloudflare.com &rarr; Web Analytics &rarr; niyiadebayo.com (visits, page views, per-article top-path hits, referrers). It is JS-based so it undercounts script/ad-blocked visitors, and GitHub Pages exposes no server logs. Do not add further JS.
- **No auto-build:** `feed.xml` and `sitemap.xml` are hand-maintained. There is no generator.
- **Share row must wrap:** The `.share` footer (X / LinkedIn / Copy link) is a flexbox and must keep `flex-wrap: wrap`. Without it the row fits at &ge;360px but the third button overflows the right edge on the smallest phones (&le;~340px, e.g. the original iPhone SE). Verified at 320px after the fix: it drops to a second line cleanly. The style is shared across every article footer, so test footer width at 320px when touching `.share`.

## Updating this file

Update `AGENTS.md` at the end of any session that:

- Adds a voice rule (because you caught the author correcting you on phrasing)
- Adds a structural convention (new footer pattern, new SEO tag, new share button)
- Adds a thinker to the registry
- Uncovers a gotcha worth preserving (path issue, rendering bug, tool quirk)
- Changes the thematic arc of the index

Commit the update in the same commit as the thing it describes, with a short note in the commit message.
