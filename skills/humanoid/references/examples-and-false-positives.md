# Examples and detection

Read when editing text someone else wrote, or when a draft feels off. Part 1: before and after pairs for the patterns that `structural-patterns.md` does not illustrate. Part 2: what not to flag, the cluster rule, and signs of a real writer to preserve.

Every after labelled "After" keeps only information from its before. An after labelled "After, with facts from the source" adds detail that in a real session would come from the source or the author, never from the rewrite; where no source exists, write the plain version.

## Before and after

### Significance inflation

Before:
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain. This initiative was part of a broader movement across Spain to decentralize administrative functions and enhance regional governance.

After:
> The Statistical Institute of Catalonia was established in 1989, part of a wider decentralization of administrative functions in Spain.

### Promotional language

Before:
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.

After:
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia.

### Vague attribution

Before:
> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.

After:
> Researchers and conservationists study the Haolai River for its unusual characteristics.

If a real source exists, name it. An unsupported claim gets cut, not decorated.

### AI vocabulary cluster

Before:
> Additionally, a distinctive feature of Somali cuisine is the incorporation of camel meat. An enduring testament to Italian colonial influence is the widespread adoption of pasta in the local culinary landscape, showcasing how these dishes have integrated into the traditional diet.

After:
> Somali cuisine also includes camel meat. Pasta dishes, introduced during Italian colonization, remain common.

### Subjectless marketing fragments

Before:
> No configuration file needed. The results are preserved automatically.

After:
> You do not need a configuration file. The system preserves the results automatically.

### Title Case and fragmented headers

Before:
> ## Strategic Negotiations And Global Partnerships
>
> ## Performance
>
> Speed matters.
>
> When users hit a slow page, they leave.

After:
> ## Strategic negotiations and global partnerships
>
> ## Performance
>
> When users hit a slow page, they leave.

### Emojis and bold labels

Before:
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting

After:
> The product launches in Q3. Users prefer simplicity. Next step: schedule a follow-up meeting.

### Chat artifacts, sycophancy and trailing offers

Before:
> Great question! You're absolutely right that this is a complex topic. Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.

After (plain: the overview itself follows, with nothing around it):
> [the overview of the French Revolution, starting on its first fact]

After, with facts from the source:
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

Before (Indonesian chat reply):
> Pertanyaan bagus! Betul sekali, tabelnya memang perlu di-partition. Semoga membantu ya. Mau saya lanjutkan ke migration script-nya?

After:
> Iya, tabelnya perlu di-partition. Langkah berikutnya migration script-nya.

The reply ends on the fact (what comes next), not on an offer. Chat register is aku/kamu; the source's "saya" and any gue/lo are both wrong here.

### Speculative gap-filling

Before:
> Information about her early life is not publicly available, suggesting she maintains a low profile and keeps personal details private. She likely grew up in a middle-class household, which shaped her later interest in education reform.

After:
> Her early life is not documented in the available sources.

Before (Indonesian):
> Informasi mengenai pendiri perusahaan tidak tersedia secara luas. Kemungkinan perusahaan ini didirikan pada awal 2000-an oleh sekelompok profesional teknologi.

After:
> Tanggal dan pendiri perusahaan tidak tercatat di sumber yang ada.

### Filler and hedging

- "In order to achieve this goal" → "To achieve this"
- "Due to the fact that it was raining" → "Because it was raining"
- "The system has the ability to process" → "The system can process"
- "It is important to note that the data shows" → "The data shows"
- "It could potentially possibly be argued that the policy might have some effect on outcomes." → "The policy may affect outcomes."

### Generic positive conclusion

Before:
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.

After: cut the paragraph. End on the last concrete fact. If the source states real plans, use those.

### Authority tropes

Before:
> The real question is whether teams can adapt. At its core, what really matters is organizational readiness.

After:
> The question is whether teams can adapt, which depends on whether the organization is ready to change its habits.

Before (Indonesian):
> Pertanyaan sebenarnya adalah apakah tim siap. Inti masalahnya, yang benar-benar penting adalah kesiapan organisasi.

After:
> Pertanyaannya apakah tim siap, dan itu tergantung organisasinya mau ubah kebiasaan atau nggak.

### Signposting

Before:
> Let's dive into how caching works in Next.js. Here's what you need to know.

After (plain):
> Next.js caches data at several layers.

After, with facts from the source:
> Next.js memoizes repeated requests within a render and keeps a separate data cache across requests.

Before (Indonesian):
> Mari kita bahas lebih dalam bagaimana partisi bekerja di Postgres. Berikut hal-hal yang perlu Anda ketahui.

After (plain):
> Partisi di Postgres kerjanya gini.

After, with facts from the source:
> Postgres membagi tabel berpartisi ke child table per range atau list, dan planner cuma baca partisi yang cocok sama filter.

### Manufactured punchlines and staccato drama

Before:
> Then AlphaEvolve arrived. It had no preference for symmetry. No aesthetic prior. No nostalgia for human taste. The old rules were gone.

After:
> AlphaEvolve changed the search because it did not favor symmetry or human-looking designs. That made some of the older assumptions less useful.

### Aphorism formulas

Before:
> Symmetry is the language of trust. Efficiency becomes a trap when teams forget the human layer.

After:
> Symmetric layouts often feel more predictable to users. Teams can over-optimize workflows and miss how people actually use them.

Before (Indonesian):
> Data adalah mata uang baru organisasi. Dashboard adalah cermin, bukan alat.

After:
> Data penting buat organisasi. Dashboard cuma nampilin data, bukan alat analisis.

### Fake candor openers

Before:
> Is it worth the price? Honestly? It depends on how often you'll use it.

After:
> Whether it's worth the price depends on how often you'll use it.

Before (Indonesian):
> Jujur aja? Gini deh. Nah, ini dia masalahnya: index-nya nggak kepake.

After:
> Masalahnya index-nya nggak kepake.

## What not to flag (false positives)

A clean human writer can hit several patterns without any model involved. Before rewriting, check that you are not gutting legitimate prose. None of these is a reliable indicator on its own:

- Perfect grammar and consistent style. Many writers are professionals or have been edited.
- Mixed casual and formal registers. Often a person in a technical field, a young writer, or someone with neurodivergent prose habits.
- Bland or dry prose. Model prose has specific tells; generic dryness without them is just dry writing.
- Formal or academic vocabulary. Models overuse specific fancy words, not all fancy words. Do not flatten "ostensibly" or "constituent" because they sound brainy.
- A letter-style opening or closing on a comment. Salutations predate chatbots by centuries.
- A common transition word in isolation. "Additionally", "moreover", "consequently" are model-coded only when piled up. One "however" is nothing.
- A single em dash in someone else's text. Many editors and journalists use them. In text you write, the count is still zero; in text you edit, one dash is evidence only alongside other tells.
- One short emphatic sentence. Flag staccato only when several fragments run in a row and inflate the tone.
- "Honestly" or "look" mid-sentence. The tell is the standalone theatrical opener, not the word.
- Unsourced claims. Most of the web is unsourced. Lack of citations proves nothing.
- Correct, complex formatting. Visual editors and templates produce clean output without any model.
- Secondhand text. Never rewrite watched phrases inside quotations, titles, proper names, identifiers, error text, or examples where the phrase is being discussed rather than used.

## The cluster rule

Look for clusters of tells, not isolated ones. A single dash means nothing. Dashes plus a decorative triad plus "vibrant tapestry" plus a "Conclusion" section is a confession. When in doubt, leave the sentence alone.

## Signs of a real writer (preserve these)

When you see these, lean toward leaving the prose alone. Over-editing destroys what makes the piece sound human.

- Specific, unusual, hard-to-fabricate detail. A real address. A weird quote. "The lawyer who used to work upstairs from my dentist." Models round off specifics; people hoard them.
- Mixed feelings and unresolved tension. "I think this is mostly good, but it bothers me, and I can't fully explain why."
- Dated, era-bound references. Slang, memes or in-jokes that map to a specific year and subculture.
- First-person editorial choices the writer can defend.
- Variety in sentence length that is irregular rather than alternating.
- Genuine asides, parentheticals or self-corrections. "(I keep wanting to say 'almost' here, but it really was certain.)"
- Text written before November 30, 2022, the public launch of ChatGPT. With rare exceptions, not model-written.
