# Vocabulary banlist

Words and phrases that mark text as machine-written. The fix is never a synonym swap: restructure the sentence to say the concrete thing, or leave the fact bare. English first, Indonesian second. Arrows (→) read as "replace with".

Before: "The festival serves as a vibrant testament to the region's rich cultural heritage, showcasing the intricate tapestry of traditions."
After, with facts from the source: "The festival has been running since 1987. Locals sell handmade pottery and goat cheese from stalls they build themselves each spring."
After, without facts: "The festival is an annual event in the region." Nothing invented; see `SKILL.md`, Never invent facts.

## English

### Highest-signal in current models (2026)

Padding verbs: ensuring, ensures, highlights, supports, reflects, plays a role in, contributes to → name the concrete action, or cut.
Top trigram: "plays a [crucial / critical / important] role in shaping" → delete on sight.
Swaps: capable of → able to; rather than (overused) → rewrite the comparison; conversely → but; nevertheless → still.
Empty intensifiers: significantly, effectively, directly, increasingly, remarkably, notably → cut unless a number backs them.
Claude signature: comprehensive, nuanced, fundamentally, paradigm, in essence, essentially, worth noting, inherent tensions, thoughtful approach, metacognitive.
Hedging adverbs, a tell when clustered: typically, often, sometimes, potentially, usually.
Closers: one thing is clear; the key takeaway; at the end of the day; as X continues to evolve.
Legacy tells now largely absent from current models (delve, tapestry, vibrant, myriad; em dashes in GPT): their absence is not evidence of human writing.

### Significance puffers

pivotal, crucial, vital, key (adjective), significant, significance, essential, groundbreaking, remarkable, transformative, indelible, profound, testament, enduring, lasting, ongoing (legacy, commitment), deeply rooted, focal point, (key) turning point, milestone, paramount, indispensable, invaluable, quintessential

### Analytical and emphasis verbs

underscore, highlight (as emphasize), showcase, foster, garner, bolster, delve, embark, leverage, facilitate, utilize, encompass, cultivate, emphasize (as tack-on), illuminate, elucidate, navigate (figurative), exemplify, embody, transcend, harness, spearhead, streamline, galvanize, demonstrate (prefer show)

### Promotional adjectives

vibrant, rich (figurative), comprehensive, robust, seamless, innovative, dynamic, cutting-edge, meticulous, intricate, nuanced, nestled, breathtaking, renowned, diverse array, bustling, stunning, state-of-the-art, multifaceted, holistic, overarching, compelling, must-visit

### Buzzword compounds (docs, READMEs, PRs, design docs)

robust, scalable, end-to-end, data-driven, high-quality, real-time, cross-functional, client-facing, best-in-class, mission-critical, future-proof, production-ready, enterprise-grade, plug-and-play, battle-tested. One that carries a real property is fine ("read-only replica"); a stack of them names nothing → the concrete property or number.

### Puffery adverbs

seamlessly, meticulously, profoundly, intrinsically, fundamentally, remarkably, notably, crucially, undeniably, inherently, poignantly, relentlessly, tirelessly, vividly

### Figurative nouns

tapestry, landscape, realm, paradigm, ecosystem, journey, nexus, interplay, mosaic, fabric (of society), bedrock, cornerstone, beacon, pillar, catalyst, crucible, linchpin, hallmark, confluence, odyssey, trajectory, underpinning

### Copula avoidance

serves as → is; stands as → is; marks a → describe directly; represents a shift → is, or describe; boasts → has; features (as has) → has; offers (as has) → has; holds the distinction of → is; emerged as → became; constitutes → is; ventured into → entered

### Formal connectives

furthermore, moreover, additionally → also; consequently, accordingly, thus, hence → so; nonetheless, nevertheless → still; henceforth → from now on; thereby → this way; wherein → where

### Opening and closing crutches

In today's [world / society / landscape]; In today's fast-paced world; In the ever-evolving landscape of; In an era of; As we navigate the complexities of; In conclusion; In summary; Overall; To recap; It is important to note that; It's worth noting that; It should be mentioned that; At the end of the day; Without further ado; In a nutshell; The bottom line is; Last but not least; No discussion of X would be complete without; Crucially; As a matter of fact

### Signposting

Let's dive in; let's explore; let's break this down; here's what you need to know; now let's look at; take a closer look at; dive deep into

### Fake candor hooks (standalone)

Honestly?; But honestly?; Look,; Here's the truth:; Here's the thing:; The thing is,; Let me be clear:; Let's be honest; Real talk; But here's where it gets interesting; Think about it this way. Mid-sentence "honestly" is fine.

### Authority tropes and aphorism formulas

the real question is; at its core; in reality; what really matters; the deeper issue; the heart of the matter; X is the Y of Z; X becomes a trap; X is not a tool but a mirror; the language of; the currency of; the architecture of

### Vague attribution

Experts argue / say / note; Observers have cited; Industry reports suggest; Some critics argue; Several sources / publications; Many believe; According to some; It is widely regarded; It is generally accepted; Studies show, Research suggests (without naming the study)

### Promotional phrases

commitment to excellence / innovation / sustainability; natural beauty; in the heart of; rich cultural heritage; a testament to; setting the stage for; contributing to the broader; reflects broader trends; shaping the future of; paving the way for; at the forefront of; pushing the boundaries of; redefining what it means to; the landscape of X is evolving; in the realm of; shed light on; a game-changer; diverse range of experiences

### Formulaic sentence shapes

It's not just X, it's Y; It's not about X, it's about Y; Not only X, but also Y; No X. No Y. Just Z.; Whether you're X or Y...; From X to Y (as a sweeping range); Most people think X. The reality is Y.; Forget X. Focus on Y.

### Formulaic pairs

challenges and opportunities; on one hand... on the other hand; pros and cons; risks and rewards

### Filler

plays a [crucial / key / important] role → state the action; when it comes to → rewrite with a verb; in order to → to; a wide range of → name them; needless to say, it goes without saying → cut; more often than not → usually, or a number; at this point in time → now; in recent years → the actual years; navigate the complexities of → name them; due to the fact that → because; in the event that → if; has the ability to → can

### Passive hedging frames

It should be noted that; It must be emphasized that; It has been observed that (say who); It can be argued that (argue it or drop it); It is important to remember that; There are several factors that (name them)

### Speculative gap-fillers

likely [grew up / studied / began]; it is believed that; presumably; maintains a low profile; keeps personal details private; prefers to stay out of the spotlight; while specific details are limited; based on available information; not publicly available → state what is unknown, or cut.

### Chat artifacts and sycophancy

I hope this helps!; Of course!; Certainly!; You're absolutely right!; Great question!; That's an excellent point; Would you like me to...; Want me to...?; Should I continue?; Is there anything else...; Let me know if...; Here is a...; As an AI language model...; I'd be happy to...

### Formatting tells

layout tells are in `SKILL.md` "Layout"; curly quotes in copyable text are a correctness issue, see `english.md`

## Indonesian

Indonesian AI text fails as translationese: bahasa baku that sounds like a government document even in casual contexts. Same rule: restructure, do not swap synonyms.

Before: "Festival ini merupakan salah satu momen penting yang tidak hanya menampilkan kekayaan budaya lokal, tetapi juga memperkuat ikatan sosial antar masyarakat, menjadikannya sebagai ajang yang sangat krusial dalam pelestarian tradisi."
After, with facts from the source: "Festival ini sudah jalan sejak 1987. Warga bikin lapak sendiri. Keju kambing dan gerabah habis sebelum tengah hari."
After, without facts: "Festival ini acara tahunan yang menampilkan budaya lokal."

### Sinyal tertinggi (2026)

memastikan as padding (calque of ensuring) → the concrete action, or cut; "berperan [penting / krusial / kunci] dalam membentuk" → state what it does; mencerminkan, menunjukkan, mendukung, menyoroti as hedging verbs → a concrete verb, or delete; "mampu untuk X" → the verb; alih-alih overuse → rewrite the comparison; sebaliknya opening a sentence → tapi, or restructure; pada intinya, pada dasarnya, secara fundamental → cut; intensifiers without numbers (secara signifikan, secara efektif, semakin) → data, or delete; satu hal yang pasti, satu hal yang jelas, intinya adalah (as closers) → cut; ketegangan inheren; ini memunculkan pertanyaan penting tentang; perlu dicatat; bernuansa; hedging adverb clusters (biasanya, sering kali, umumnya, berpotensi, terkadang stacked) → commit or quantify

### Penggelembung kepentingan

sangat penting; sangat krusial, krusial; sangat signifikan, signifikan; sangat relevan; fundamental, mendasar (as vague praise); luar biasa (generic praise); mendalam (without substance); berarti, bermakna (as vague praise) → say specifically why it matters, or drop the qualifier

### Kata kerja analitis

menyoroti, menyorot → menunjukkan, or state the finding; menggarisbawahi → menunjukkan, or drop; memfasilitasi → membantu, memungkinkan; mengoptimalkan → memperbaiki, or name what changes; memanfaatkan → menggunakan when it means "to use" (keep it when it means "take benefit from"); mengimplementasikan → menerapkan, menjalankan; berkontribusi pada → the concrete action and result; berperan dalam → the specific action; mengedepankan → mengutamakan; mewujudkan, merealisasikan → membuat, menciptakan; menyelami (calque of delve) → bahas

### Kata sifat promosi

komprehensif → what is covered; holistik → name the parts; inovatif → what is new; dinamis → what changes and how; inklusif → who is included; berbagai macam, beragam (as filler) → list them; terkini (without a date) → the date; kolaboratif; berkelanjutan (as buzzword)

### Buzzword

transformasi digital; ekosistem (figurative); paradigma; optimalisasi; sinergi; lanskap; kompleksitas (without saying what is complex); dinamika (without saying what changes); inovasi (as jargon)

### Kata penghubung formal

selain itu → juga; di sisi lain → tapi, namun (not as a hollow pivot); lebih lanjut → restructure; dengan demikian → jadi, maka; oleh karena itu → jadi, makanya (santai), karena itu; tak kalah penting, tidak kalah pentingnya → state what it is; menariknya → lead with the fact; sehubungan dengan hal tersebut → restructure; berkaitan dengan hal ini, dalam hal ini → say what "this" is

### Pembuka dan penutup klise

Di era modern ini; Dalam konteks [X] yang semakin [Y]; Seiring perkembangan zaman; Perlu diketahui bahwa; Penting untuk diingat; Sebagai kesimpulan; Dapat disimpulkan bahwa; Dengan demikian, dapat disimpulkan; Pada akhirnya; Perlu kita sadari bersama; Tidak dapat dipungkiri; Mari kita telusuri lebih dalam; Mari kita bahas; Secara keseluruhan; Singkatnya; Untuk merangkum

### Penghindaran kopula

merupakan → adalah, or restructure (default); berperan sebagai → adalah for identity, otherwise a concrete verb; berfungsi sebagai → berfungsi untuk, for purpose; memiliki peran penting → the exact role; menjadi salah satu... → quantify; "menjadi [X] yang [Y] dalam / bagi [Z]" → state directly

### Atribusi samar

para ahli menyatakan; penelitian menunjukkan; banyak kalangan berpendapat; menurut beberapa sumber; studi menunjukkan; komunitas ilmiah sepakat → name who, or cut

### Frasa promosi

memiliki komitmen untuk; memberikan dampak positif; berperan penting dalam; dalam rangka [tujuan]; dalam upaya [X]; guna meningkatkan; untuk mencapai tujuan tersebut; berkontribusi pada kemajuan; membangun sinergi; memiliki potensi besar; menjadi landasan penting; menjadi sorotan utama; tidak bisa dipandang sebelah mata; memberikan kontribusi yang signifikan

### Pengisi

memainkan peran [penting / krusial / kunci] → the action; dalam rangka untuk → untuk; tidak perlu dikatakan, sudah jelas bahwa → cut; lebih sering daripada tidak → biasanya, or a number; dalam beberapa tahun terakhir → the actual years; hal ini menunjukkan betapa pentingnya → state the fact; dapat dilihat bahwa, dapat dipahami bahwa, perlu dipahami bahwa → state the finding

### Pasangan formulaik

tantangan dan peluang; di satu sisi... di sisi lain; meskipun demikian... namun perlu diingat bahwa; kelebihan dan kekurangan

### Hedging

meskipun demikian → tapi, or drop; namun perlu diingat bahwa → cut; bisa jadi diargumentasikan bahwa → take a position; ada baiknya jika → state it

### Pengisi celah spekulatif

kemungkinan; diperkirakan; tampaknya; sepertinya (when filling an undocumented fact, not as polite hedging); "informasi mengenai X tidak tersedia secara luas, menunjukkan bahwa..." → state what is unknown, or cut

### Candor palsu dan trope otoritas

Jujur aja?; Gini deh.; Nah, ini dia.; Sebenarnya begini:; pertanyaan sebenarnya adalah; inti masalahnya; X adalah Y-nya Z; X adalah bahasa dari Y; X adalah mata uang Z. Mid-sentence "jujur" or "sebenarnya" is fine.

### Artefak chat dan sycophancy

Semoga membantu!; Tentu saja!; Tentu!; Baik, berikut adalah...; Pertanyaan bagus!; Betul sekali!; Anda benar sekali!; Apakah ada yang ingin Anda tanyakan?; Jika ada pertanyaan, jangan ragu untuk bertanya.; Mau saya lanjutkan?; Mau saya bantu...?; Silakan beri tahu saya jika...; Sebagai AI, saya...
