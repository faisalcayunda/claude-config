# Structural patterns

Patterns that make text read as machine-generated even when every word is allowed. Most were documented on Wikipedia's "Signs of AI writing" page (WikiProject AI Cleanup) and confirmed in corpus studies (Kobak et al. 2024, Russell et al. 2025, Fraser et al. 2025). Indonesian structural patterns (BI rules) live in `indonesian.md`; before and after pairs for the patterns not covered here are in `examples-and-false-positives.md`.

Every "after" below uses only information present in its "before". Where the before is vague and no source adds more, the after is the plain version.

## 1. Participial -ing tack-ons

A comma followed by an -ing phrase appended to a sentence to appear analytical.

AI:
> The team launched the product, revolutionizing the industry.
> The temple was built in 1850, symbolizing the community's enduring faith.
> As of 2008, the population stood at 56,998, creating a lively community.

After:
> The team launched the product.
> The temple was built in 1850.
> As of 2008, the population was 56,998.

Rule: if the -ing clause adds no concrete information, delete it. If it adds real information, make it a separate sentence.

## 2. The rule of three

AI groups things in threes by default: three adjectives, three bullets, three examples, three clauses.

AI:
> The conference features keynote sessions, panel discussions, and networking opportunities.
> The design is bold, innovative, and timeless.

After:
> The conference runs keynote sessions and panels. There is time to meet people between talks.
> The design is bold and meant to last.

Rule: edit decorative triads (adjectives and parallel clauses added for rhythm) into the natural count. Never add or remove a real item to dodge the number: three files stay three files.

## 3. Negative parallelisms and tailing negations

"Not just X, but also Y", "It's not X, it's Y", "Not only X, but Y", and the clipped tailing negation ("..., no guessing.").

AI:
> This is not just a memoir, it's a love letter to the city.
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere.
> The options come from the selected item, no guessing.

After:
> It's a memoir about growing up in the city, written with affection for it.
> The heavy beat adds to the aggressive tone.
> The options come from the selected item, so the user does not have to guess.

Rule: state what something is. Do not frame it as a correction of what someone might wrongly think, and write the negation as a real clause or drop it.

## 4. False ranges

"From X to Y" as a figurative spectrum where no real scale exists.

AI:
> From intimate gatherings to global movements, the organization has made its mark.
> From the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.

After:
> The organization runs small gatherings and large campaigns.
> The Big Bang, the cosmic web, the life cycle of stars, and dark matter.

Rule: use "from X to Y" only when there is a real, identifiable midpoint on a real scale.

## 5. "Despite its... faces challenges"

The formulaic challenges-and-future-prospects ending.

AI:
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.

After:
> Korattur has recurring traffic congestion and water shortages.

Rule: name the specific problems the source names. Never follow with vague optimism about "ongoing initiatives". Specifics such as when the congestion worsened come from the source, not from the rewrite.

## 6. Copula avoidance

Elaborate verb phrases in place of "is", "are", "has".

AI:
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.
> She holds the distinction of being the first female director.

After:
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.
> She was the first female director.

Rule: use "is", "are", "has", "was". Simple copulas are clear, not boring.

## 7. Superficial analysis padding

Generic commentary attached to facts that need none.

AI:
> The city has a population of 56,998, creating a lively community within its borders.
> The inscriptions offer valuable insights into the construction of the mosque.
> These citations illustrate the enduring relevance of his work.

After:
> The city has a population of 56,998.
> The inscriptions describe the construction of the mosque.
> His work is still cited.

Rule: if the analytical statement could apply to any subject, it adds nothing. Delete it.

## 8. Elegant variation (synonym cycling)

Cycling through synonyms to avoid repeating a word, even when repetition is clearer.

AI:
> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.

After:
> The protagonist faces many challenges but eventually triumphs and returns home.

Rule: repeat the word when clarity demands it. Identifiers, table and function names repeat exactly every time.

## 9. Em and en dashes: zero

Em dashes where humans use commas, parentheses, periods, or nothing. This is the most reliable single tell in Claude-era output and a hard constraint here, not a frequency target.

AI (the marker [em dash] stands for the character, which this file does not contain):
> The article complies with policies [em dash] including WP:V, WP:RS, and WP:BLP [em dash] with all claims supported by multiple sources.
> The new policy [em dash] announced without warning [em dash] affects thousands of workers.

After:
> The article complies with WP:V, WP:RS, and WP:BLP. All claims have sources.
> The new policy, announced without warning, affects thousands of workers.

Rule: none. Replace each, in rough order of preference, with a period, a comma, a colon, parentheses, or a restructured sentence. Catch spaced em dashes and double hyphens used the same way. Scan the final text for the em dash (U+2014) and en dash (U+2013) characters; any hit means it is not done.

## 10. Vertical lists with bold inline headers

AI:
> - **SEO:** Traditional methods for improving visibility...
> - **AEO:** Techniques focused on optimizing content...
> - **GIO:** Strategies for ensuring businesses are cited...

After: write it as prose. If a list is genuinely needed (files, steps, options), keep it plain, without bold headers and colon separators.

## 11. Notability lists

Listing every source that covered a topic to prove it matters.

AI:
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.

After:
> Her views have been cited in The New York Times and the BBC.

Rule: cite the specific thing a source said, inline. If the source gives real context for one citation, keep that one and drop the rest. Do not invent the context to make the trimmed version sound better.

## 12. Boldface overuse

AI:
> A **leveraged buyout (LBO)** uses **debt financing** to let **private equity firms** control businesses using the company's **assets and future cash flows** as collateral.

After:
> A leveraged buyout uses debt to buy a company. The company's own assets and cash flow back the loans.

Rule: bold sparingly. In most prose, bold nothing.

## 13. The four-part arc

Most AI text follows one argument cadence regardless of topic: opening (context or claim), expansion (detail), contrast (complication), resolution (conclude or transition). It is detectable within three or four sentences and survives vocabulary changes.

Rule (long-form): break the arc where the argument allows; the same arc in every section is a tell. Open on the complication. Expand without contrasting. End a section on an unresolved fact. Put the conclusion first. Resolution closers ("At the end of the day...", "The key takeaway here is...") are training artifacts; real endings take a position and stop.

## 14. Cadence uniformity

Sentences landing in the same length band one after another, paragraph after paragraph. It survives every cosmetic rewrite.

Rule: the cadence rule in `SKILL.md` (length, clause depth and the two tests). Vary sentence openers with verbs, names, numbers, subordinate clauses and questions.

## 15. The bimodal seesaw

Newer models fake variety by alternating a punchy fragment with a very long sentence. "Short. Then a forty-word sentence that winds through three clauses." Repeated, the alternation is itself a fingerprint. Human writing clusters around medium length with occasional swings in both directions.

Rule: most sentences medium, with genuine swings. Not a metronome and not a seesaw.

## 16. Paragraph over-fragmentation

Older models wrote uniform three or four sentence paragraphs. Newer models fragment into many one or two sentence paragraphs plus bullet lists.

Rule: combine related ideas. Let a paragraph run to seven or eight sentences when the argument needs it. Convert bullets in prose to prose.

## 17. The symmetric two-clause hook

AI:
> Most people think X. The reality is Y.
> Forget X. Focus on Y.
> It is not about X. It is about Y.

Fine once. A fingerprint when it opens most pieces or appears three times in one post.

Rule: open with a specific fact, scene, number or name from the source.

## 18. The sanitized texture

Current models run a cleanup pass that scrubs obvious tells, leaving prose with no awkward transition, no odd word choice, no rough edge anywhere. Perfect smoothness is itself the residue.

Rule (long-form only): a genuinely rough moment or two is natural: an abrupt topic shift that earns its context later, a committed but slightly odd metaphor, a self-correction mid-paragraph. Never manufacture one, and never in engineering artifacts.
