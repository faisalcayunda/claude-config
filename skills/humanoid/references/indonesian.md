# Indonesian writing reference

Read before any Indonesian text longer than a one-liner. Indonesian AI output fails mainly as translationese: grammatically correct bahasa baku that sounds like a government document or a translated Wikipedia article, whatever the context. This file covers register, particles, morphology, translationese and the structural tells specific to Indonesian. Words and phrases are in `vocabulary-banlist.md` (Indonesian section). Universal rules (dashes, cadence, never invent facts) are in `SKILL.md` and apply here in full.

## Tiers

Pick the tier before writing.

| Tier | Where | Pronouns | Contractions | Particles | Code-switching |
|---|---|---|---|---|---|
| 1 Formal | academic papers, official reports, thesis, office documents, news | saya, Anda, or impersonal (peneliti, penulis) | none | none | avoid |
| 2 Semi-formal (default for articles) | blog, opinion, LinkedIn, newsletter, magazine feature | saya/aku, kamu | occasional (nggak, udah) | occasional (sih, kan, kok) | when common in the domain (meeting, deadline, framework) |
| 3 Informal, santai (default for chat replies) | chat with the user, X threads, captions, personal blog, WhatsApp | aku, kamu in chat; gue/gw, lo/lu only in social posts and captions when the audience talks that way (one set per text) | free (nggak, udah, gimana, emang, aja) | natural (sih, dong, deh, lho, kan, kok, nih, tuh) | free when natural for the audience |

Chat replies to this user are Tier 3 in the colleague register: aku and kamu, never gue/gw or lo/lu; "udah", "gak", "biar", "benerin", "sama" for "dan", "bikin". Identifiers, file names, table names, function names, commands and error text stay verbatim inside the santai sentence. Ranges in Indonesian: "2020 sampai 2025", "halaman 10 sampai 15", or a plain hyphen; never an en dash.

Natural sentences per tier:

- Formal: "Kenaikan UMP 6,5 persen tahun lalu belum otomatis memperbaiki daya beli kelas menengah."
- Semi-formal: "Gaji naik 6,5 persen, tapi harga beras naik 12 persen. Jadi ya, daya beli nggak benar-benar membaik."
- Informal: "Gaji naik 6,5 persen tapi harga beras naik 12 persen, jadi ya gitu deh. Nggak ngerasa lebih kaya sih."

Across tiers, in long-form only: perfectly uniform register is itself a tell, so a small shift (one short blunt sentence inside formal prose, one tidy sentence inside santai prose) is natural. Allowed, never required, and never in engineering artifacts.

## Pronouns

AI locks onto "Anda". Match the tier and hold one set per text: switching "aku" and "gw" inside one paragraph is a machine pattern. Academic writing refers to the author as "peneliti" or "penulis". Never "Anda" in a clearly casual context.

## Contractions and colloquial forms

Tier 3 by default, Tier 2 occasionally, Tier 1 keeps the full forms.

| Formal | Santai |
|---|---|
| tidak | nggak, gak, ga |
| sudah | udah |
| bagaimana | gimana |
| membuat | bikin |
| memang | emang |
| saja | aja |
| sangat | banget |
| dengan | sama (in some contexts) |
| ingin | pengen |
| ini, itu | nih, tuh |
| belum | belom |
| mengerti | ngerti |
| mencari | nyari |
| menonton | nonton |

Nasal prefix reduction (meN- collapses to its nasal) in Tier 3:

| Prefix | Initial letter | Becomes | Examples |
|---|---|---|---|
| meng- | vowel, g, h, k | ng- | mengambil to ngambil, mengerti to ngerti, mengirim to ngirim |
| men- | t, d, c, j | n-, ny- | menonton to nonton, mencari to nyari |
| mem- | b, p, f | m-, mb-, nge- | membantu to mbantu or ngebantu, memukul to mukul |
| meny- | s | ny- | menyapu to nyapu, menyukai to nyukain |

Full formal prefixes throughout a santai text is a clear tell.

## Particles

Their total absence in Tier 2 and 3 is one of the strongest Indonesian tells. Place them where a speaker would, not as decoration.

- sih: soft emphasis, mild contradiction, rhetorical question. "Nggak juga, sih." "Bagus sih, tapi..."
- dong: nudge, request. "Bantuin dong."
- deh: concession, light emphasis. "Iya deh." "Coba deh."
- lho, loh: surprise. "Loh, kok bisa?"
- nih: offering, informal "ini". "Nih masalahnya..."
- tuh: informal "itu", pointing. "Tuh kan, bener."
- kan: confirmation, reminder. "Kan udah dibilang."
- kok: puzzlement. "Kok gitu?"
- ya: agreement, seeking confirmation. "Gitu ya."
- nah: transition marker. "Nah, itu dia masalahnya." As a standalone reveal ("Nah, ini dia.") it is fake candor; see `SKILL.md`.
- lah: emphasis, softener. "Biasa lah."
- mah (Sunda, Jakarta): emphasis. "Kalau itu mah gampang."

Density: Tier 1 none (at most one in a whole text). Tier 2 about 2 to 4 per 500 words, skipping the most casual ones (mah, stacked deh). Tier 3 as in speech, roughly 1 to 2 per paragraph, and in chat replies wherever they fall naturally.

Interjections, Tier 3 long-form, only when the reaction is real: duh, aduh (complaint), waduh (worried surprise), astaga (shock), buset (informal shock), ih (mild disgust), hah (disbelief), wah (awe). Idioms ("besar pasak daripada tiang", "tong kosong nyaring bunyinya", "sedikit-sedikit lama-lama jadi bukit") add texture in long-form once in a while; not in a chat reply about a bug.

Code-switching: "Meeting-nya diundur ya", "Aku udah submit, tinggal nunggu feedback", "Mindset-nya harus diubah". Connector switching ("literally", "which is", "basically") belongs to Tier 3 social posts and captions when that is how the audience talks, not to chat replies. Never forced.

## Translationese (TR) rules

TR-1. Passive with "oleh". AI: "Keputusan itu dibuat oleh tim manajemen." Indonesian has the prokletik passive: "Keputusan itu tim manajemen yang buat." Or active: "Tim manajemen yang bikin keputusan itu." Cut "oleh" drastically; use the prokletik passive in santai register and active where it fits. Natural di- passives stay when the object matters more than the actor ("filenya kehapus", "venue-nya udah dibooking dari jauh hari"). The tell is uniformity in either direction: a draft that is 100 percent active, punchy declaratives is the GPT Motivator register, not a person.

TR-2. Topic-comment. Indonesian is topic-prominent. AI: "Program ini telah memberikan manfaat kepada masyarakat." Natural: "Kalau programnya, masyarakat udah mulai ngerasain manfaatnya." AI: "Mereka mengalami kesulitan." Natural: "Kalau mereka, ya susah juga sih." Use it sometimes; not every sentence needs its grammatical subject in front.

TR-3. Pro-drop. AI: "Kami mengadakan rapat. Kami membahas anggaran. Kami menyetujui proposal." Natural: "Ngadain rapat, bahas anggaran, terus setujuin proposalnya." Drop the subject once context carries it; a subject repeated three times in a row is translationese.

TR-4. "Yang" chains. AI: "Strategi yang digunakan oleh perusahaan yang bergerak di bidang teknologi." Natural: "Strategi perusahaan teknologi." More than two "yang" in one sentence: restructure.

TR-5. "Adalah" overuse. AI: "Indonesia adalah negara kepulauan. Jakarta adalah ibukotanya." Natural: "Indonesia negara kepulauan. Ibukotanya Jakarta." Keep "adalah" for identity emphasis or a formal definition.

TR-6. KBBI spelling, held consistently: praktik, kedaluwarsa, aktivitas, nasihat, mengubah. In informal text pick one form and keep it; random inconsistency is a machine pattern.

TR-7. Indonesian rhetoric. Inductive order (evidence first, then the point) is common and natural; a piece need not open on its thesis. Circling back to a point from a new angle is natural; strictly linear A, B, C, D with no return reads translated. Light cultural hedging ("sepertinya", "mungkin bisa dibilang") is politeness, not weakness, and differs from content-free AI hedging. A peribahasa ("sedikit-sedikit, lama-lama jadi bukit") beats its abstract paraphrase ("akumulasi usaha kecil menghasilkan hasil besar").

TR-8. Calques. "di mana" as a relative pronoun ("program di mana peserta akan...") becomes "program yang..." or a direct sentence. "alih-alih" overuse (rather than), "sebaliknya" opening a sentence (conversely), "lanskap" (landscape), "menyelami" (delve), "permadani" (tapestry), "mampu untuk X" (capable of), "memainkan peran penting dalam membentuk" (plays a crucial role in shaping): rewrite each as the plain Indonesian claim.

## Indonesian structural (BI) rules

BI-1. "Kesimpulan" heading only when the genre requires it (academic paper, formal report, compliance document). Essays, articles and chat close in prose or just stop.
AI: "## Kesimpulan. Dengan demikian, dapat disimpulkan bahwa festival ini memiliki peran penting dalam melestarikan budaya lokal dan memperkuat kohesi sosial masyarakat."
Natural, plain version: "Festival ini membantu melestarikan budaya lokal." Nothing added; the "kohesi sosial" claim goes only if the source supports it.

BI-2. No temporal opener: "Di era modern ini", "Seiring perkembangan zaman", "Dalam konteks X yang semakin Y". Open with the fact, number or scene the source supplies.

BI-3. "Tidak hanya X, tetapi juga Y": the negative parallelism rule in `SKILL.md` applies. State what it is.
AI: "Pelatihan ini tidak hanya meningkatkan kompetensi peserta, tetapi juga memperkuat jaringan profesional mereka."
Natural, plain version: "Pelatihan ini meningkatkan kompetensi peserta dan memperluas jaringan profesional mereka."
Natural, with facts from the source: "Peserta dapat sertifikat. Mereka juga dapat akses ke grup alumni yang lumayan aktif."

BI-4. "Merupakan salah satu X yang paling Y" asserts importance without evidence. Quantify or compare with numbers from the source, or drop the claim.
AI: "Jakarta merupakan salah satu kota dengan perkembangan ekonomi yang paling pesat di Asia Tenggara."
Natural (only when the source has the numbers): "Jakarta tumbuh 5,2% tahun 2023, lebih cepat dari Bangkok dan Manila."

BI-5. "Di sisi lain, terdapat beberapa tantangan yang perlu diatasi... Namun, dengan upaya yang tepat, tantangan ini dapat diatasi." Name the concrete problem from the source, with its number when there is one, and no vague optimism after it.

BI-6. "Dapat dilihat bahwa", "dapat dipahami bahwa", "perlu dipahami bahwa": delete and state the finding. "Dari data tersebut, dapat dilihat bahwa terdapat peningkatan yang signifikan." becomes "Angkanya naik." (or "Angkanya naik 23% dari tahun lalu." when the source gives the number).

BI-7. Nominalization. AI: "Pelaksanaan program pelatihan vokasional ini dilakukan dalam rangka peningkatan kompetensi tenaga kerja." Natural, plain version: "Program ini melatih tenaga kerja supaya lebih kompeten." (With facts from the source: "Program ini melatih 200 orang per tahun.") Verbs over pe-/ke-an/-an chains: melatih, not pelaksanaan pelatihan; mengembangkan, not pengembangan kapasitas; membangun, not pembangunan.

BI-8. Formulaic pairs: "tantangan dan peluang", "kelebihan dan kekurangan", "di satu sisi... di sisi lain". Name the specific problem or the specific benefit, not the reflex pair.

BI-9. Symmetric hook calque: "Banyak orang mengira X. Kenyataannya Y." / "Lupakan X. Fokus ke Y." / "Ini bukan soal X. Ini soal Y." Once is fine; as the opener of most pieces, or three times in one post, it is a fingerprint. Open with the fact, number, scene or name instead.

BI-10. Topic-phrase repetition. The topic phrase from the prompt ("strategi pemasaran digital UMKM") appears whole at most once or twice; refer to the topic in other ways after that ("cara jualan online buat usaha kecil", or straight to the concrete example). This governs topic phrases only. Identifiers (table, file, function, column names) repeat exactly every time; see `SKILL.md`, Repetition.

## Indonesian model fingerprints

English fingerprints leak into Indonesian through calques. The tells that survive in current models:

- GPT (Motivator): one negated contrast per paragraph ("Ini bukan sekadar X, ini Y"); rigid "Pertama / Kedua / Terakhir" scaffolding with an intro, triplet, recap arc; hedging verbs as padding ("memastikan", "mencerminkan", "menunjukkan", "mendukung", "menyoroti"); intensifiers without numbers ("secara signifikan", "secara efektif", "semakin"); overconfident declaratives ("Inilah kebenaran tentang Z", "Founder terbaik tahu Y"); closers with "satu hal yang pasti". Sanitized texture: `structural-patterns.md` 18.
- Claude (Philosopher): hedge stacking before the point ("Meskipun ini bisa bervariasi, secara umum, dalam banyak kasus, perlu dicatat bahwa..."); "perlu dicatat", "bernuansa", "komprehensif", "secara fundamental", "paradigma", "pada intinya", "pada dasarnya", "ketegangan inheren", "ini memunculkan pertanyaan penting tentang"; hedging adverbs clustered ("biasanya", "sering kali", "terkadang", "berpotensi", "umumnya"); automatic empathy framing ("bisa dimaklumi kalau banyak orang merasa...", "ini bisa bikin frustrasi bagi..."); the essay arc on every format (contextualize, explore perspectives, qualify, close on what the analysis "raises"); abstract inflation ("founder dengan kesadaran metakognitif yang kuat sering mendapati bahwa" for "founder terbaik tahu"); "Dan" / "Tapi" opening every other paragraph; bimodal sentence rhythm; many one- or two-sentence paragraphs plus bullets.
- Gemini: purple prose, adjective stacks, moralizing, explicit theme statements, textbook tone.

The old vocabulary tells ("menyelami", "permadani") are mostly gone from current models. Their absence proves nothing; check structure.

## Indonesian long-form checklist

Run after the `SKILL.md` audit, for articles, essays, posts and threads only.

1. Tier confirmed and held; one pronoun set.
2. Dash count zero. Colons at most about one per 300 words outside lists; semicolons at most two per 500 words.
3. Banlist words gone (`vocabulary-banlist.md`, Indonesian section), including "merupakan" by default and the buzzwords (inovasi, holistik, kolaboratif, ekosistem, paradigma, optimalisasi, sinergi, transformasi digital, lanskap).
4. No temporal opener; no "Kesimpulan" heading unless the genre requires it; no formulaic pair; negative parallelism per `SKILL.md`; no symmetric hook.
5. Tack-on clauses and "dapat dilihat bahwa" padding removed; each paragraph's last sentence checked for restatement.
6. Cadence: no run of three same-length sentences, no bimodal seesaw, fewer than half the sentences opening with "Hal ini / Ini / Dalam / Selain itu / Dengan"; fragmented paragraphs merged.
7. Translationese: "oleh" at most twice per page; no "yang" chain over two; subject dropped where context carries it; "adalah" only where needed; some topic-comment sentences; "di mana" relative clauses rewritten.
8. Particles and contractions match the tier (present in Tier 2 and 3, absent in Tier 1); nasal prefixes in Tier 3.
9. Hedges at most one per claim; no hedge-and-reassure stack.
10. Ending is a position or a concrete fact, not a recap; no "satu hal yang pasti", "intinya adalah".
11. Topic phrase appears whole at most twice; identifiers unchanged.
12. Every replacement keeps the original meaning; no fact added that the source did not supply.
