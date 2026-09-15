# English writing reference

Read before English engineering artifacts and any long-form (the "Long-form voice" section is language-neutral). Words and phrases are in `vocabulary-banlist.md`; patterns with before and after pairs are in `structural-patterns.md`. Universal rules (dashes, cadence, never invent facts) are in `SKILL.md` and apply here in full.

## Artifact rules (commit, PR, review comment, wiki page, doc, code comment)

Neutral is the correct human voice here. No opinions, humor, first person, register shifts, discourse markers or emotional texture. The vocabulary and structure rules from `SKILL.md` apply in full.

- Present tense: docs, wiki pages and code comments describe the thing as it is. Narrate change only where the document is version-scoped: commit messages, PR descriptions, changelogs, release notes, migration guides.
  Diff-anchored: "This function was added to replace the previous approach of iterating through all items, which caused O(n²) performance."
  Fixed: "This function uses a hash map for O(1) lookups, avoiding the O(n²) cost of naive iteration."
- Straight quotes only: `"` and `'`. Docs, code comments, commands, and JSON, SQL, YAML and shell examples break when someone copies a curly quote. This is a correctness rule for copyable text, not a style tell.
- Buzzword compounds: a stack of hyphenated modifiers ("a robust, scalable, end-to-end, data-driven, high-quality pipeline") names no property. Name the concrete one: the throughput figure, the retry behaviour, the test that passes. One compound that carries meaning ("third-party API", "read-only replica") is fine.
- Commit messages: imperative subject naming the change, body stating what changed and why in prose or a plain list of real items. No "This commit...", no summary line at the end, no rationale padding.
- PR descriptions: what changed, why, and how it was verified (the actual command or check, from the tool output). Lists for real enumerations (files touched, steps to test). No bold-header colon lists, no "Summary / Changes / Testing" scaffolding when two sentences cover it.
- Review comments: the problem, where, and the fix or the question. No praise opener, no "Great work overall", no "Consider..." when the change is required. "Nit:" as a label for optional items is fine.
- Wiki pages and docs: no fragmented headers (a heading followed by a one-line warm-up that restates it). No "Challenges and future prospects" or "Conclusion" section; end on the last fact. No notability lists (naming every source that mentioned something as proof it matters); cite the specific claim instead.
- Code comments: why, in the present tense. No "// changed to fix...".
- Names and identifiers verbatim, always, including inside prose.

## EN rules

English-only deltas. Openers, closers, hedging, passives, fragments and staccato are governed by the universal rules in `SKILL.md`; filler phrases are in `vocabulary-banlist.md` "Filler".

EN-1. Semicolons: rare outside academic prose. Prefer a period or a conjunction.

EN-2. Contractions in conversational English ("don't", "can't", "it's", "we're"); full forms in formal documents and artifacts. English chat replies take contractions; casual forms ("gonna", "kinda") only when the register is clearly that casual.

EN-3. Questions: a real question that sits with the reader ("Who decides that?") is fine in long-form. Not the setup-and-answer ("What makes this important? The answer is...").

EN-4. Connectors: when a draft leans on one, vary it ("and", "plus", "as well as", a comma; "but", "though", "still", "yet"), or drop the connector and let the sequence carry the transition. Formal connectives (furthermore, moreover, consequently, thus) become "also", "so", "still".

EN-5. Hyphens: plain hyphen for compound modifiers ("state-of-the-art" only if the source says so) and for numeric ranges where words are awkward ("2020-2025"). Never as a sentence-level pause.

## Model fingerprints (mid-2026)

Vocabulary tells ("delve", "tapestry", "vibrant", "myriad") are largely trained out of current models, and GPT-5.1 and later suppress em dashes. Their absence proves nothing. The surviving tells:

GPT (Motivator): the negated contrast once per paragraph ("It's not just X, it's Y"); symmetric two-clause hooks ("Most people think X. The reality is Y." / "Forget X. Focus on Y."); "Firstly / Secondly / Finally" scaffolding with an intro, triplet, recap arc; hedging verbs as padding ("ensuring", "ensures", "highlights", "supports", "reflects"); "plays a [crucial / critical / important] role in shaping"; intensifiers without a number ("significantly", "effectively", "directly", "increasingly"); "rather than" and "capable of" overuse; overconfident declaratives ("Here's the truth about Z", "The best founders know Y"); closers with "one thing is clear". Sanitized texture: `structural-patterns.md` 18.

Claude (Philosopher): em dash mid-sentence to attach qualifiers, colons and semicolons at several times human density; hedge-and-reassure stacking ("While this may vary, generally speaking, in most cases, it's worth noting that..."); "worth noting", "nuanced", "comprehensive", "fundamentally", "paradigm", "in essence", "essentially", "inherent tensions", "this raises important questions about"; hedging adverbs clustered ("typically", "often", "sometimes", "potentially", "usually"); autopilot empathy ("understandably, many people feel..."); the essay arc on every format (contextualize, explore perspectives, qualify, close on what the analysis "raises"); abstract inflation ("founders with strong metacognitive awareness often find that" for "the best founders know"); "And" / "But" opening every other paragraph; bimodal sentence rhythm; many one- or two-sentence paragraphs plus bullets.

Gemini: purple prose, adjective stacks, moralizing, explicit theme statements, textbook tone.

## Long-form voice

Language-neutral: applies to Indonesian long-form as well, in the tier chosen from `indonesian.md`. Only for articles, essays, posts, newsletters and threads, and only as far as the author's voice calls for it. Never add a factual claim to create voice.

- Stance: commit to a position ("This approach is wrong because...") instead of false balance ("Some argue X, while others argue Y"). Real uncertainty stated plainly ("I don't know", "last I checked", "from what I gather").
- Uneven rhythm: irregular paragraph lengths, a one-sentence paragraph for emphasis, a seven-sentence paragraph for a sustained argument. Not every paragraph opens with its thesis; some start on a detail or an example. Break the four-part arc (context, expansion, contrast, resolution) where the argument allows: open on the complication, expand without contrasting, end a section on an unresolved fact, put the conclusion first. The same arc in every section is a tell.
- Asides and self-correction where they are real ("(I keep wanting to say 'almost' here, but it really was certain.)"). Humor that fits. Emotional texture the author actually has: rushing through the dull part, lingering on the interesting one.
- Register shifts are allowed (a casual parenthetical in a formal argument, a technical term in conversational prose), never scheduled. Discourse markers ("Well", "I mean", "Granted", "That said", "Frankly") where a speaker would use them, not by count.
- Specific references (a named event, a real work, "last Tuesday") only when the author or source supplies them.
- Knowledge asymmetry: deep where the author knows, openly thin elsewhere. Insider references that assume shared context are fine for that audience.
- Endings take a position and stop.

## English long-form checklist

Run after the `SKILL.md` audit.

1. Dash count zero; colons about one per 300 words at most outside lists; semicolons rare.
2. Banlist words gone (`vocabulary-banlist.md`), including "ensuring / ensures", "highlights / supports / reflects" as padding, "plays a role in", "rather than" overuse, empty intensifiers, stacked buzzword compounds.
3. No temporal opener, symmetric hook or signposting; no summary closer, "one thing is clear", "the key takeaway"; the ending is a position or a fact.
4. Negative parallelism per `SKILL.md`; no tailing negation fragment; no staccato run; decorative triads edited, real items untouched.
5. Tack-on -ing clauses removed; each paragraph's last sentence checked for restatement.
6. Cadence: no run of three same-length sentences, no seesaw, fewer than half the sentences opening with The / This / It / In; fragmented paragraphs merged.
7. Passives: natural ones kept, runs of agentless passives broken; hedges at most one per claim.
8. Layout per `SKILL.md`; no fragmented headers; straight quotes.
9. Voice present only where the surface allows it; every specific traceable to the source or the author.
