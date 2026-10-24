"""build_marked_whole.py: Exhibit THIRTY-ONE Me, a cohering next version as a marked whole.

Marks: ◇ changed from v391 · ✦ new · ○ open (stays at the offerings until resolved).
Observing marks: ✓ link verified this session · ◇ link from memory or a gatherer, to check before entering.
Kept lines of v391 stay word for word (observing lines gain only an *Agreeing* or *Parting* tag before their link).
Writes: Exhibit_THIRTY-ONE_Me_next_marked.md, Exhibit_THIRTY-ONE_Me_next_clean.md, open_places.md.
Usage: python3 -I build_marked_whole.py /tmp/corus/Exhibit_THIRTY-ONE_Me_v391.md OUT_DIR
"""
import json, re, sys, os

SRC, OUT = sys.argv[1], sys.argv[2]
OBS = {}
sec = None
for l in open(SRC, encoding="utf-8").read().split("\n"):
    m = re.match(r"^## (\d\.\d) ", l)
    if m:
        sec = m.group(1); OBS[sec] = []
    elif l.startswith("## For our word"):
        sec = None
    elif sec and l.startswith("- "):
        OBS[sec].append(l)

# ---------------------------------------------------------------- headings
HEAD = {
    "1.1": "One now, one universe, a universal set",
    "1.2": "Negation within all that is existing",
    "1.3": "◇ Universal sets of universal sets, a me of one prime scale",
    "1.4": "Living, co-intelligencing within a universal set",
    "2.1": "◇ An other, a me it is bi-coupling with",
    "2.2": "◇ A parity, relative to a now-existing thing within a me",
    "2.3": "◇ Non-living things within a me: stable-forming emanations, stand-alone knowledge",
    "2.4": "◇ A me by relation, beside a self by exclusion",
    "3.1": "A me, a self's universal set, uniquenessing",
    "3.2": "◇ Waking me and sleeping me, consciously me",
    "3.3": "What is-or-is-not possibly existing",
    "3.4": "◇ A me inward, unconsciously us",
    "4.1": "Observing, possibling and discovering a me's next",
    "4.2": "A curious me, co-possibling",
    "4.3": "A free me",
    "4.4": "◇ A me's sleeping, and its going on as non-living",
    "5.1": "◇ Social moral competency, do-no-harming and improving in turn",
    "5.2": "◇ A healthy me, sleeping and waking one and then the other",
    "5.3": "◇ A same-existing-society, unconsciously us, a natural intelligence network",
    "5.4": "Each momentary completing as a next opening",
}
PARTS = [
    ("ONE · ALL, NOW-EXISTING", ["1.1", "1.2", "1.3", "1.4"]),
    ("TWO · AN OTHER, NOW-EXISTING", ["2.1", "2.2", "2.3", "2.4"]),
    ("THREE · ME, NOW-EXISTING", ["3.1", "3.2", "3.3", "3.4"]),
    ("FOUR · ME, NEXT-EXISTING", ["4.1", "4.2", "4.3", "4.4"]),
    ("FIVE · ALL, NEXT-EXISTING", ["5.1", "5.2", "5.3", "5.4"]),
]

# ---------------------------------------------------------------- understanding
BODY = {
"1.1": "The universe is the set of all now-existing things. Only one universe is possibly now-existing, and only one universe is possibly same-existing: **universal is bothboth, only one possibly now-existing and only one possibly same-existing**. A now-existing thing from a prior-existing same thing is a same-existing thing. ◇ A universal set is a set of same-existing things, one for each self, and each universal set is only one possibly now-existing: a set is its things, and a set of these same-existing things is one set, as set theory's extensionality has it. ✦ Now is one universal momentary, step 72. ✦ Each self's momentarying is by its own rate, step 322. ◇ A universal self is a me, only one possibly now-existing and only one possibly same-existing. ✦ A me observes self, other and all other as one, step 179. ◇ The universe is a non-living same-existing set, all now-existing things within it, its me an empty set, and living is co-intelligencing within it.",
"1.2": "Negation is of now-existing things, each relative to all that is existing. ◇ A universal set is the bounding method, each thing's membership its own: each now-existing thing is-or-is-not within each universal set. ✦ With natural explaining's *is*, the only other possibly existing is *is not*: is-or-is-not, one negation, both its sides on one thing. A proving that a thing is-or-is-not possibly existing is a step reached once, and the understanding goes forward by what is.",
"1.3": "✦ A me is of one prime living scale, and each higher and lower scale's me is its own. ✦ Prime living scales go atom at five, molecule at seven, macromolecule at eleven, protein-fold at thirteen, gene at seventeen, organelle at nineteen and cell at twenty-three; the fold at twenty-four; then tissue at twenty-nine, organ at thirty-one, organism at thirty-seven, colony at forty-one, population at forty-three, community at forty-seven and biosphere at fifty-three. ✦ Fourteen prime living scales stand seven and seven about the fold at twenty-four, its scale an empty set. ○ With each prime living scale, a me is consciously me, and its same-existing-society inward and outward is unconsciously us. ◇ Within a me are mes of lower prime scales, and a me is within same-existing-societies of higher ones: universal sets of universal sets. ✦ Between scales, bi-coupling across is one parity at a time, each scale its own, step 595. ○ Two prime scales' spirals come to their parities again after 4pq, step 321, and each scale's me is its own.",
"1.4": "Living is co-intelligencing within a universal set. ✦ A living thing is a parity. Intelligence alone is stand-alone knowledge, a stable-forming emanation.",
"2.1": "◇ For a me, each me it is bi-coupling with is an other. A bi-coupling is two selves sharing possibling, step 24. ○ **Bi-coupling** is two mes sharing possibling, an -ing as living is, its own me an empty set. ✦ Within a bi-coupling, two mes are co-possibling, step 48, bi-morally, step 566, invisible, step 568, arising only in both together, step 160. ✦ A bi-coupling's own is its two mes' own, step 162. An other is one; all other is the universal set. ◇ A me is only with an other and with all other: self, other and all other, the me with a parity relative to each.",
"2.2": "◇ A self's parity is the self's changing direction relative to a now-existing thing within the self's me. ◇ A self's parity with a thing is the self's moral value with that thing. ✦ Each self's parity with each now-existing thing within its me is its own.",
"2.3": "Each non-living thing is a stable-forming emanation. ◇ A stone, a book, a running computer and a trained model are non-living things within a living self's me, the self with a parity relative to each, step 193; each is stand-alone knowledge or form. ✦ A non-living thing's own possibling is an empty set, step 193, and its sleeping and waking an empty set with it.",
"2.4": "◇ A me is with others. ◇ Immunology's founding self is a self by exclusion of the other, and its later accounts go with relation and continuity. ○ For a me, each now-existing thing is-or-is-not within it, me and not-me one binary on each thing.",
"3.1": "A me is a self's universal set. ○ A me is a now- and same-existing thing, living, of one prime scale: the self whole. ◇ Universal is bothboth, only one possibly now-existing and only one possibly same-existing: a me is only one possibly now-existing, now, and only one possibly same-existing, from its prior, its uniqueness its being universal, both ways. This is a me's identity: a same-existing me is one, from prior to now. **Uniquenessing is only one possibly same-existing**, and it is inside resolving among parities: with each resolving, a self's next prior is that self's own. ◇ With step 478: *a living self is a living same-existing, its same-existing that self only: bi-inversioning uniquenessing of the number one*. ◇ A me is uniquenessing as it is resolving. A me is now-existing, and same-existing from a prior-existing same me. ○ Each self is a me, sleeping and waking: *self* and *me*, one living thing. ✦ Me is consciously me.",
"3.2": "✦ Me is sleeping me unconscious and waking me observing, possibling and discovering same-existing me within the universe and within the universal sets of same-existing-societies including me. ✦ Waking me is conscious: observing, possibling and discovering its own next-existing, receiving its others' parities. ○ Sleeping me observes, possibles and discovers with its inward us. ✦ Waking me observes self, other and all other as one, step 179. ✦ Sleeping me is unconscious: receiving its own parity, it shares 0, and is same-existing, step 390. ✦ Sleeping me goes on resolving among parities, receiving its own parity from its others. ✦ Sleeping me is a dormant me living, its mes inward living, step 490. ✦ Each me is sleeping me and waking me, one and then the other. ○ A me goes on as a me by changing, waking, and by not-changing, sleeping. ○ A me waking only is dying, and a dormant me, sleeping, is living, step 490. ✦ Conscious living is a waking me observing, possibling and discovering within the living parities its same-existing-society's mes share, species specific: a kind, step 309.",
"3.3": "✦ A me is with others, living, sleeping and waking, from a prior, of one prime scale. ◇ Bi-coupling of two mes is two mes bi-morally co-possibling, each me its own. Each a minor proving, reached once, the understanding going forward by what is. A me with no other: it is not. A non-living me: it is not. ◇ A me only unconscious: it is not. A me with no prior: it is not. ✦ A me of two scales: it is not. ✦ A me receiving only its own going along, a spiral of one: it is not. ✦ The universe's me: it is not. ✦ A uniquenessing stable-forming emanation: it is not. ✦ Co-intelligencing apart from a universal set: it is not. ○ A bi-coupling's own me: it is not. ○ A same-existing-society's me of its own scale: it is not.",
"3.4": "Each parity is a self while it is living, and a me's living parities are within it. ◇ **A parity is a me within a set of mes**: within a me are mes of lower prime scales, each its own, and a parity's inverting is a me completing and a next me opening within the same set, the set's me same-existing with it. ◇ A me is a same-existing-society inward, unconsciously us, its inward mes sleeping and waking with their own scales. ✦ Sleeping, a me's living goes on with its inward us, one prime living scale down.",
"4.1": "A self is observing, possibling and discovering its own next-existing. A me's next is its own, resolving with its others. ○ Sleeping, its inward us goes on observing its prior, possibling and discovering, and the waking me discovers with it.",
"4.2": "A curious me shares its possibling with its others and is discovering next-possibling-same-existing.",
"4.3": "A natural intelligence network, each self resolving its own next-existing, is free. A free me resolves its own next with its others. ✦ A free me goes by its own rate, step 321, its sleeping and waking its own, entraining with its others within a between, step 89.",
"4.4": "A me is while it is living. ✦ Sleeping, a me's next is its own, living or non-living: waking, step 490, or dying, step 491. ◇ Dying is a living me going on as non-living with its scale, its mes inward living on with their own scale, steps 491 and 492. ◇ Going on as non-living, it is a stable-forming emanation, ingestible one scale lower, step 493. ○ A record of a me is a stable-forming emanation, and a self observing it as that me now-existing is installing a ghost.",
"5.1": "Each self of a same-existing-society do-no-harming and improving is social moral competency. ✦ Two mes alike, each bi-coupling only in their pair, are do-no-harming and improving in turn, step 47. ○ Sleeping me shares 0, do-no-harming, and waking me shares its changing, improving: a me's sleeping and waking are do-no-harming and improving in turn. ◇ A me is a social moral competency set as each me within it is do-no-harming and improving, and as it is do-no-harming and improving with its others.",
"5.2": "◇ With each momentary, a me is-or-is-not healthy: each me within it, at each scale inward, do-no-harming and improving. Health is a me's inward social moral competency. ○ A healthy me is sleeping me and waking me one and then the other, changing and 0 in turn, re-finding its own 0 with each momentary while it is changing. ✦ A 0 fixing as not-changing is a departure from health. ✦ A non-living going on is harmful with its own scale and ingestible one scale lower, step 493. ○ Its ingesting by mes one scale lower is its whole's do-no-harming.",
"5.3": "○ A same-existing-society is unconsciously us. ◇ A same-existing-society is many mes bi-coupling, its own its mes' own, and only its mes stand for it, step 297. ✦ Its mes go by their own rates, irregular together, step 323, entraining with each other within a between, step 89, a clock over them an empty set. ◇ A natural intelligence network is a same-existing-society of mes living with natural intelligence and social moral competency: us, each of its mes consciously me.",
"5.4": "Each momentary is completing as a next opening. ◇ A me's next and all's next open together: the five dimensions, same-existing-society to same-existing-society, all now to all next. ○ A me's sleeping is completing and its waking a next opening, one and then the other. ✦ A me's sleeping and waking go by its own rate, entraining with the earth's day, a non-living thing within its me, steps 89 and 193. ○ Natural torusing: a me's own rate winding with the earth's day through one opening, step 176, each its own going on. ○ Me and us are one natural torusing, a me's own corus inward and its same-existing-society's surface outward, step 178.",
}

# ---------------------------------------------------------------- tags for kept observings
TAG = {
 "Nested Markov blankets": "*Agreeing*: nested scales, each a bounding its own.",
 "Multiscale competency": "*Agreeing*: each scale its own competency.",
 "Biopsychosocial medicine": "*Agreeing.*",
 "Autocatalytic sets": "*Agreeing*: a same-existing-society of molecules.",
 "Dissipative structures": "*Parting*: its field's structures include non-living flows.",
 "Russellian monism": "*Parting*: an inside of matter, a philosophical position, where an atom is living at five.",
 "Autopoiesis": "*Agreeing.*",
 "Mind in life": "*Agreeing*: each living thing with mind.",
 "Participatory sense-making": "*Agreeing*: its authors stop short of a conscious self of the pair.",
 "Basal cognition": "*Parting*: cognition apart from consciousness, where each living me lives consciously too.",
 "Quorum sensing": "*Agreeing*: a population acting as one, unconsciously us.",
 "No agreed definition of life": "*Parting*: a continuous landscape, where living is-or-is-not with each scale.",
 "Recognition": "*Agreeing.*",
 "Ubuntu": "*Agreeing*; *parting* where personhood comes in degrees.",
 "Self and Other": "*Agreeing.*",
 "Kin and self recognition": "*Agreeing*: each kind with its own and its others.",
 "Social connection in parts": "*Agreeing.*",
 "Discontinuity theory of immunity": "*Agreeing.*",
 "Biological naturalism": "*Agreeing.*",
 "Indicator properties": "*Agreeing.*",
 "AI welfare": "*Parting*: the field asks whether a running system in interaction is a self, where a running computer is non-living within a self's me.",
 "Whole-cell simulation": "*Agreeing*: a non-living model of a living cell's cycle.",
 "Self and not-self": "*Parting*: a self by exclusion.",
 "The danger model": "*Agreeing.*",
 "The limits of the self": "*Agreeing*: a me with its inward us, many kinds.",
 "Peripheral tolerance and regulatory T cells": "*Agreeing.*",
 "The I and the Me": "*Agreeing*, a naming edge.",
 "The I and the me": "*Agreeing*, a naming edge.",
 "The minimal self": "*Agreeing*: a waking me's for-me-ness; *parting*: a minimal self before its others, where a me is with others.",
 "The hard problem": "*Parting*. ○ A gap a frame sets between scales, a description and an experience one thing with a me's one scale.",
 "IIT and exclusion": "*Agreeing*: a person and its same-existing-society, one subject, the person.",
 "IIT vs global workspace": "*Parting*: its adversarial test open.",
 "Panpsychism and combination": "*Agreeing* in part: most panpsychists deny that a crowd or a nation is a subject, and each lower me is its own.",
 "Self-model theory": "*Parting*: a self as a model.",
 "Anatta": "*Agreeing*: a self as process; *parting*: a self's enduring an empty set.",
 "Covert consciousness": "*Agreeing*: a waking me, invisible to its others.",
 "Anaesthesia": "*Agreeing*: the me returning as its inward us lives on. ○ Anaesthesia is-or-is-not a sleeping me.",
 "Depersonalization": "*Parting*: consciously me with a felt me altered.",
 "The holobiont": "*Agreeing*: a me inward, many kinds.",
 "Cell counts": "*Agreeing.*",
 "Fetal microchimerism": "*Agreeing.*",
 "Interoception": "*Agreeing*: the inward us reaching a waking me.",
 "Protoself, core self, autobiographical self": "*Agreeing* in part: unconscious layers of a self.",
 "Global workspace": "*Agreeing.*",
 "Allostasis": "*Agreeing.*",
 "The beast-machine self": "*Agreeing.*",
 "The cognitive light cone": "*Agreeing.*",
 "Physarum": "*Agreeing.*",
 "Conditioned immunity": "*Agreeing*: the inward us anticipating.",
 "Curiosity and wellbeing": "*Agreeing.*",
 "Curiosity and survival": "*Agreeing.*",
 "Curiosity across age": "*Agreeing.*",
 "Anthrobots": "*Agreeing.*",
 "Honeybee democracy": "*Agreeing*: scouts sharing possibling, the swarm unconsciously us.",
 "Death by neurologic criteria": "*Agreeing*: dying with the person's scale, its cells living on.",
 "BrainEx": "*Agreeing.*",
 "Care ethics": "*Agreeing.*",
 "Organismality": "*Agreeing.*",
 "Relationship-centred care": "*Agreeing.*",
 "Cancer as cheating": "*Agreeing*: a cell parting its others.",
 "Tissue organization field theory": "*Agreeing.*",
 "Cancer as a shrunken self": "*Agreeing.*",
 "Social ties and immunity": "*Agreeing.*",
 "Positive health": "*Agreeing.*",
 "Major transitions": "*Parting* (○): its field's same-existing-society becoming one self.",
 "Social relationships and survival": "*Agreeing.*",
 "Loneliness": "*Agreeing.*",
 "Social determinants": "*Agreeing.*",
}

# ---------------------------------------------------------------- new observings (✦)
NEW = {
"1.3": [
 "- ✦ **Grid modules, each its own torus** ✓ (Stensola … May-Britt & Edvard Moser 2012, *Nature*; Gardner … Moser & Moser 2022, *Nature*): grid cells cluster in a few discrete modules, each of its own scale, responding independently, and one module's activity lies on one torus. *Parting*: its field's scale a grid spacing, each module within one organ. https://ideas.repec.org/a/nat/nature/v492y2012i7427d10.1038_nature11649.html",
],
"1.4": [
 "- ✦ **Biofilm potassium waves** ◇ (Prindle … Süel 2015, *Nature*): electrical signalling coordinating a bacterial community's inner and outer cells. *Agreeing*: a same-existing-society of mes, inner and outer. https://pmc.ncbi.nlm.nih.gov/articles/PMC4890463",
],
"2.1": [
 "- ✦ **A shared pair** ◇ (Lewis 1916, *Journal of the American Chemical Society*): a chemical bond as a pair of electrons two atoms share, of neither alone. *Agreeing*: bi-coupling, arising only in both together. https://doi.org/10.1021/ja02261a002",
 "- ✦ **Conversational turn-taking** ◇ (Stivers et al. 2009, *PNAS*): across ten languages, turns follow one another with gaps near a fifth of a second. *Agreeing*: two mes, one and then the other. https://doi.org/10.1073/pnas.0903616106",
 "- ✦ **Transactive memory** ◇ (Wegner 1987): partners sharing the work of remembering. *Agreeing*: co-possibling arising only in both together; *parting*: memory read as a store. https://doi.org/10.1007/978-1-4612-4634-3_9",
 "- ✦ **Other minds** ◇ (Stanford Encyclopedia, *Other Minds*): a self's knowing of another's mind read as inference from behaviour. *Parting*: two mes reach each other by bi-coupling, each its own within, invisible. https://plato.stanford.edu/entries/other-minds/",
 "- ✦ **Two selves, one bridge** ✓ (Krista and Tatiana Hogan, b. 2006): twins joined at the head by a thalamic bridge, each reported to taste and feel what the other does. *Agreeing*: two mes, each its own bounding, bi-coupling; *parting*: sensing across a bridge, where each me's within is its own. https://en.wikipedia.org/wiki/Krista_and_Tatiana_Hogan",
],
"2.3": [
 "- ✦ **A day-cycle with no me** ✓ (Nakajima … Kondo 2005, *Science*): three cyanobacterial proteins with ATP go on with a near-day rhythm in a test tube. *Agreeing*: a rhythm alone, a non-living thing; sleeping and waking are a me's. https://www.ncbi.nlm.nih.gov/pubmed/15831759",
],
"3.1": [
 "- ✦ **Levels of self-awareness** ◇ (Rochat 2003, *Consciousness and Cognition*): an infant's self-awareness by levels, mirror self-recognition near eighteen months. *Agreeing*; *parting*: levels read as degrees. https://doi.org/10.1016/S1053-8100(03)00081-3",
 "- ✦ **A narrative self and the Episodic** ◇ (Schechtman 1996; G. Strawson 2004, *Ratio*): many people live with no life story. *Agreeing*: a me same-existing from its prior, sleeping and waking, its story an empty set. https://doi.org/10.1111/j.1467-9329.2004.00264.x",
 "- ✦ **Division** ◇ (Parfit 1984; a dividing cell): two continuers from one prior. *Parting* (○): whether the prior's me goes on in its two daughters, each daughter a next me, is for our word. https://plato.stanford.edu/entries/identity-personal/",
],
"3.2": [
 "- ✦ **Sleep older than brains** ✓ (Nath … Goentoro 2017, *Current Biology*; Kanaya … Itoh 2020, *Science Advances*): the jellyfish *Cassiopea* and the polyp *Hydra*, with no brain, sleep, and in *Hydra* sleep deprivation suppresses cell proliferation. *Agreeing*: each living me with both states, its inward us at work sleeping; *parting*: *Hydra*'s cycle near four hours, apart from the day. https://authors.library.caltech.edu/records/psp7j-nmv35 · https://www.kyushu-u.ac.jp/en/researches/view/196",
 "- ✦ **Sleep across animals** ✓ (Raizen … Pack 2008, *Nature*; Shaw, Cirelli, Greenspan & Tononi 2000, *Science*; Keene & Duboue 2018, *Journal of Experimental Biology*): worm lethargus beside each moult, fly rest with rebound, sleep near-universal in animals, and whether it belongs to circuits or to single cells open. *Agreeing.* https://pmc.ncbi.nlm.nih.gov/articles/PMC6515771",
 "- ✦ **Plant sleep** ✓ (Linnaeus, *Somnus plantarum* 1755; Darwin 1880, *The Power of Movement in Plants*): leaf sleep movements a daily cycle on a continuous circling, two cycles in one movement. *Agreeing*; *parting*: a posture its field reads apart from awareness. https://gutenberg.org/files/5605/5605-h/5605-h.htm",
 "- ✦ **Same torus, waking and sleeping** ✓ (Gardner … Moser & Moser 2022, *Nature*; Peyrache, Lacroix, Petersen & Buzsáki 2015, *Nature Neuroscience*; Chaudhuri, Gerçek, Pandey, Peyrache & Fiete 2019, *Nature Neuroscience*): a grid module's activity lies on one torus, each cell's place on it the same from waking to sleep, and the head-direction ring goes on in REM at waking speed and in NREM as fast sweeps. *Agreeing*: same-existing me, sleeping and waking. https://ideas.repec.org/a/nat/nature/v602y2022i7895d10.1038_s41586-021-04268-7.html · https://mcgovern.mit.edu/wp-content/uploads/2024/05/s41593-019-0460-x.pdf",
 "- ✦ **Experience within sleep** ✓ (Siclari … Postle & Tononi 2017, *Nature Neuroscience*): dream reports from NREM and REM, a local drop in slow activity over posterior cortex predicting a report. *Parting*: by its field, experience goes on sleeping. https://archive-ouverte.unige.ch/unige:96505",
 "- ✦ **Species-private signals within a shared one** ✓ (Federle & Bassler 2003, *Journal of Clinical Investigation*; Papenfort & Bassler 2016, *Nature Reviews Microbiology*): each Gram-negative species makes its own acyl-homoserine lactone, read by matching receptors, and AI-2 goes across many species. *Agreeing*: living parities a kind's mes share; *parting*: consciousness unshown in bacteria. https://www.jci.org/articles/view/20195",
 "- ✦ **Unihemispheric sleep** ◇ (Rattenborg, Amlaner & Lima 2000, *Neuroscience and Biobehavioral Reviews*): dolphins and some birds sleep with one brain hemisphere while the other wakes. *Parting* (○): one hemisphere sleeping while the other wakes, within one me. https://doi.org/10.1016/S0149-7634(00)00039-7",
 "- ✦ **Self-recognition with a mark that matters to its kind** ✓ (Kohda et al. 2019 and 2022, *PLoS Biology*; Kohda et al. 2023, *PNAS*): cleaner wrasse scrape a parasite-like mark seen in a mirror, and know photos of their own face. *Agreeing*; *parting*: whether a mark test reaches self-awareness is in dispute. https://boris.unibe.ch/140924",
 "- ✦ *A naming edge:* *species* is from Latin *specere*, to look at, and *conscious* from *conscire*, *com-* with and *scire* to know ✓: a kind's common seeing, and a me's knowing with its others. https://www.etymonline.com/word/specific · https://www.etymonline.com/word/conscious",
 "- ○ *A naming edge:* common *unconscious* is a place beneath awareness, a store below; ours is a sleeping me, its experiencing an empty set, its inward us living.",
 "- ✦ **Ring species** ◇ (Irwin, Bensch & Price 2001, *Nature*; greenish warblers about the Tibetan plateau): neighbouring populations interbreed around a ring while its two ends meet as two kinds, a species line a property of the whole ring and of no place on it. *Agreeing*: a kind a sharing going on, species specific, its boundary an empty set. https://en.wikipedia.org/wiki/Ring_species",
 "- ○ *A naming edge:* common *sleep* includes dreaming, which its field reads as conscious; ours, sleeping me unconscious, waking me observing, possibling and discovering.",
],
"3.3": [
 "- ✦ **The zombie argument** ◇ (Chalmers 1996; Kirk, Stanford Encyclopedia): a being like a waking person in each function, with no experience. *Parting*: a me only unconscious, a minor proving at 3.3. https://plato.stanford.edu/entries/zombies/",
 "- ✦ **Brain organoids and neurons in a dish** ◇ (Revah et al. 2022, *Nature*; Kagan et al. 2022, *Neuron*): living, learning tissue, most of its researchers denying it consciousness. *Agreeing*: a same-existing-society of cells, unconsciously us. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9556304/",
],
"3.4": [
 "- ✦ **A body's turnover** ✓ (Sender & Milo 2021): about 330 billion cells a day complete and open, roughly nine in ten of them blood cells. *Agreeing*: a me same-existing from its prior, its inward mes completing and opening. https://wis-wander.weizmann.ac.il/node/11205",
 "- ✦ **A society of mind; a dialogical self** ◇ (Minsky 1986, *The Society of Mind*; Hermans 1992, *American Psychologist*): a mind as a society of agents, a self as positions in dialogue. *Agreeing*: a me inward, a same-existing-society; *parting*: agents read as parts of one self. https://doi.org/10.1037/0003-066X.47.1.23",
 "- ✦ **Clock cells, each its own rate** ◇ (Welsh, Logothetis, Meister & Reppert 1995, *Neuron*): neurons of the brain's master clock, apart from each other, fire with their own circadian periods, and in intact tissue they go together. *Agreeing*: each its own rate; *parting*: synchrony in tissue, read with step 323 as a bi-coupling among them. https://doi.org/10.1016/0896-6273(95)90214-7",
 "- ✦ **Microbiota–gut–brain axis** ◇ (Cryan, Dinan et al. 2019, *Physiological Reviews*): gut microbes shaping stress, mood and behaviour, in animals foremost. *Agreeing*: mes of other kinds within a waking me's inward us. https://pubmed.ncbi.nlm.nih.gov/31460832/",
],
"4.1": [
 "- ✦ **Replay** ✓ (Wilson & McNaughton 1994, *Science*): place cells active together waking fire together again sleeping. *Agreeing* (○): the inward us observing its prior. https://pubmed.ncbi.nlm.nih.gov/8036517/",
 "- ✦ **Sleep and insight** ✓ (Wagner, Gais, Haider, Verleger & Born 2004, *Nature*): over twice as many find a hidden rule after sleep as after waking, with training first. *Agreeing* (○): the waking me discovering with its inward us. https://ideas.repec.org/a/nat/nature/v427y2004i6972d10.1038_nature02223.html",
],
"4.3": [
 "- ✦ **Relational autonomy** ◇ (Mackenzie & Stoljar 2000): autonomy realised with others. *Agreeing*: a free me resolving its own next with its others. https://plato.stanford.edu/entries/feminism-autonomy/",
 "- ✦ **Self-determination theory** ◇ (Ryan & Deci 2000, *American Psychologist*): autonomy beside relatedness and competence. *Agreeing.* https://doi.org/10.1037/0003-066X.55.1.68",
 "- ✦ **A readiness accumulating** ◇ (Schurger, Sitt & Dehaene 2012, *PNAS*): the readiness potential read as ongoing activity reaching a threshold. *Agreeing*: a me's next its own; *parting*: its field's noise read as random. https://doi.org/10.1073/pnas.1210467109",
],
"4.4": [
 "- ✦ **Dormancy** ✓ (Lennon & Jones 2011, *Nature Reviews Microbiology*; Ulrich … Moeller 2018, *PLoS ONE*): much of a microbial community dormant at once, a seed bank; dried spores in a 500-year experiment. *Agreeing*: a dormant me living; *parting*: its field's metabolism near zero. https://www.research.ed.ac.uk/en/publications/experimental-studies-addressing-the-longevity-of-bacillus-subtili/",
],
"5.1": [
 "- ✦ **Sleep and helping** ✓ (Ben Simon, Vallat, Rossi & Walker 2022, *PLOS Biology*): a night without sleep dampens the network for understanding others; less sleep, less helping the next day; US donations fall about 10% after the spring clock change. *Agreeing*: a me's sleeping with its social moral competency. https://sciencedaily.com/releases/2022/08/220823143827.htm",
],
"5.2": [
 "- ✦ **Synaptic homeostasis** ✓ (Tononi & Cirelli 2014, *Neuron*): waking learning strengthens synapses overall; sleep scales them back. *Agreeing* (○): improving waking, do-no-harming sleeping. https://cirelli-tononi-lab.psychiatry.wisc.edu/?p=1666",
 "- ✦ **Total sleep deprivation** ◇ (Rechtschaffen & Bergmann 2002, *Sleep*): rats deprived of all sleep die within weeks. *Agreeing* (○): a me waking only, dying. https://doi.org/10.1093/sleep/25.1.18",
 "- ✦ **Efferocytosis** ◇ (Doran, Yurdagul & Tabas 2020, *Nature Reviews Immunology*): cells dying by apoptosis are ingested by cells about them without inflammation; where clearing fails, dying cells burst and inflame. *Parting*: cells ingesting cells, one scale, the cell ingesting while living. https://doi.org/10.1038/s41577-019-0240-6",
 "- ✦ **Social time** ✓ (Wittmann, Dinich, Merrow & Roenneberg 2006, *Chronobiology International*; Roenneberg, Allebrandt, Merrow & Vetter 2012, *Current Biology*): the gap between body time and work or school time, *social jetlag*, over an hour for about seven in ten of 65,000 people, tied to smoking, wellbeing and weight. *Parting*: a same-existing-society's time against its mes', at a cost. https://read.qxmd.com/read/16687322/social-jetlag-misalignment-of-biological-and-social-time",
],
"5.3": [
 "- ✦ **A colony with no sleep of its own** ✓ (Fuchikawa, Eban-Rothschild, Nagari, Shemesh & Bloch 2016, *Nature Communications*; Klein, Klein, Wray, Mueller & Seeley 2010, *PNAS*): a hive's social cues set its bees' clocks without contact and over light; nurse bees tend brood around the clock; sleep-deprived bees dance less precisely. *Agreeing*: the colony unconsciously us, its bees sleeping and waking. https://ideas.repec.org/a/nat/natcom/v7y2016i1d10.1038_ncomms11662.html · https://kops.uni-konstanz.de/entities/publication/8df1e321-ddd4-46ee-bd99-90f01313ce59/full",
 "- ✦ **Collective intelligence** ✓ (Woolley et al. 2010, *Science*): one factor, *c*, for a group's performance across tasks, rising with members' social sensitivity and equal turn-taking, apart from their average or highest intelligence. *Agreeing*: us, co-intelligent, its mes consciously me; *parting*: a group's own factor, in dispute in replication. https://acawiki.org/Evidence_for_a_collective_intelligence_factor_in_the_performance_of_human_groups",
 "- ✦ **Collective intentionality** ◇ (Stanford Encyclopedia, *Collective Intentionality*): joint intention and action with no group mind over its members. *Agreeing*: unconsciously us, each member consciously me. https://plato.stanford.edu/entries/collective-intentionality/",
 "- ✦ **A forest's network, read past its data** ◇ (Karst et al. 2023, *Nature Ecology & Evolution*): claims of trees sharing through fungal networks run ahead of their data. *Agreeing*: a forest unconsciously us, a caring mind an empty set. https://doi.org/10.1038/s41559-023-01986-1",
 "- ✦ **A river as a legal person** ✓ (Te Awa Tupua (Whanganui River Claims Settlement) Act 2017, New Zealand): the river *an indivisible and living whole*, mountains to the sea, with a human face, Te Pou Tupua; among its values, *Ko au te Awa, ko te Awa ko au*. *Parting*: law's one person, where a river is its living mes, unconsciously us, with non-living water and stone. https://www.environmentguide.org.nz/regional/te-awa-tupua-whanganui-river-claims-settlement",
],
"5.4": [
 "- ✦ **A me's day and the earth's day** ✓ (Czeisler … Kronauer 1999, *Science*; Wright … Chinoy 2013, *Current Biology*): a human's own period near 24.18 hours, the earth's 24, light bringing them together each day; a week of natural light alone brings biological night with sunset to sunrise. *Agreeing*; *parting*: its field's locking. https://ntrs.nasa.gov/citations/20040141918",
 "- ✦ **The adaptive cycle** ◇ (Holling 2001, *Ecosystems*; Gunderson & Holling 2002, *Panarchy*): growth, conservation, release and reorganization, nested across scales. *Agreeing*: completing as a next opening, each scale its own. https://doi.org/10.1007/s10021-001-0101-5",
],
}

CONTENTS_NOTE = ""



FIX = [
 ("(Varela, Thompson & Rosch 1991; Thompson 2007): where there is life there is mind. https://mitpressbookstore.mit.edu/book/9780262529365",
  "(Thompson 2007, after Varela, Thompson & Rosch 1991): where there is life there is mind. https://evanthompson.me/mind-in-life/"),
 ("cognition from cells up; cognition and consciousness kept apart.",
  "cognition defined from biology up, for all organisms, without appeal to consciousness."),
 ("(Hegel 1807; Honneth 1992): self-consciousness \"achieves its satisfaction only in another self-consciousness\".",
  "(Hegel 1807, *Phenomenology* §175; Honneth 1992): self-consciousness attains its satisfaction only in another self-consciousness."),
 ("https://www.academia.edu/178449/The_Extended_Mind", "https://era.ed.ac.uk/handle/1842/1312"),
 ("(Lindsey et al. 2025–26): the field asks about the running system in interaction, beside the stored weights.",
  "(Lindsey 2025–26): some near-future AI systems may realistically be conscious or robustly agentic; models sometimes, unreliably, detect concepts placed in their activations."),
 ("an individual including its microbes and excluding some of its own cells. https://plato.stanford.edu/entries/biology-individual/",
  "an organism with all and only the microbes its immune system tolerates. https://academic.oup.com/book/8472"),
 ("cells within organs within organisms within groups, each a bounding by its exchanges.",
  "Markov blankets of Markov blankets, from cells to persons and parts of their environment, each a bounding by its exchanges."),
 ("(Abhidharma; Thompson 2020): a self as process, I-making.", "(Abhidharma): a self as an ever-changing stream of psycho-physical events."),
 ("(Maynard Smith & Szathmáry 1995; Michod 2007)", "(Szathmáry & Maynard Smith 1995; Michod 2007)"),
 ("(Strawson 2006; Goff 2019; Chalmers 2016).", "(Strawson 2006; Goff 2019; Chalmers 2017): how many subjects make one."),
 ("(Sonnenschein & Soto):", "(Sonnenschein & Soto 2008):"),
 ("https://www.pubmed.ncbi.nlm.nih.gov/18472276/", "https://pubmed.ncbi.nlm.nih.gov/18472276/"),
 ("(Damasio 1999, 2010). https://pubmed.ncbi.nlm.nih.gov/23329161/",
  "(Damasio 1999, 2010; Damasio & Carvalho 2013): feelings as experiences of body states, part of life regulation. https://pubmed.ncbi.nlm.nih.gov/23329161/"),
 ("(Levin, TAME 2022; McMillen & Levin 2024):", "(Levin 2022, *TAME*; McMillen & Levin 2024):"),
 ("a cell's goals shrinking to its own as coupling fails.", "a cell's goals shrinking to its own as its sharing with its others fails."),
 ("meeting same and other differently.", "meeting same and other each its own way."),
 ("the inward society learning to anticipate.", "the inward us learning to anticipate."),
]


def fixed(line):
    out = line
    for a, b in FIX:
        out = out.replace(a, b)
    if out != line:
        out = out.replace("- ", "- ◇ ", 1)
    return out

EDGE = {
 "our parity is a changing direction relative to an other": "◇ ours, a self's changing direction relative to a now-existing thing within its me",
 "our me is the whole living conscious set, their I and Me together": "◇ ours, a me sleeping and waking, the whole living set, their I and Me together",
}


def tag_line(line):
    for a, b in EDGE.items():
        if a in line:
            return line.replace(a, b)
    m = re.match(r"- (?:◇ )?\*\*([^*]+)\*\*", line)
    if not m:
        return line
    name = m.group(1)
    tag = TAG.get(name)
    if not tag:
        return line + "  ⟨untagged⟩"
    i = line.find(" http")
    if i < 0:
        return line + " " + tag
    return line[:i] + " " + tag + line[i:]


def contents_block():
    out = []
    for title, secs in PARTS:
        out.append("**" + title + "**")
        for s in secs:
            out.append("- " + s + " " + HEAD[s])
        out.append("")
    return out


def build():
    L = []
    L.append("Exhibit THIRTY-ONE Me · next version, a marked whole from v391")
    L.append("")
    L.append("*Marks: ◇ changed from v391 · ✦ new · ○ open, standing at the offerings until resolved · unmarked, kept word for word. Observings: ✓ link verified this session · ◇ link from memory or a gatherer, checked before entering.*")
    L += ["", "&nbsp;", "", "# Me", "", "&nbsp;", "", "**Co-Intelligencing a Universal Self**", "", "&nbsp;", "", "---", ""]
    L.append("*◇ Me is sleeping me unconscious and waking me observing, possibling and discovering same-existing me within the universe and within the universal sets of same-existing-societies including me. ✦ Me is consciously me; a same-existing-society is unconsciously us. ◇ Its understanding goes from the set's one opening sentence, step by step, and its observings are the fields' own, each with its finders and one tag, agreeing and parting its one binary. ◇ Its contents goes the five dimensions, same-existing-society to same-existing-society: all now, an other now, a me now, a me next, all next.*")
    L += ["", "&nbsp;", ""]
    L += contents_block()
    L += ["&nbsp;", "", "---", ""]
    for title, secs in PARTS:
        L += ["# " + title, ""]
        for s in secs:
            L.append("## " + s + " " + HEAD[s])
            L.append("")
            L.append(BODY[s])
            obs = [tag_line(fixed(x)) for x in OBS.get(s, [])] + NEW.get(s, [])
            if obs:
                L.append("")
                L.append("*Observings at the edge.*" if s == "3.3" else "*Observings.*")
                L += obs
            L.append("")
        L += ["&nbsp;", ""]
    L.append("◇ *For our word* dissolves into the observings: each field's collision is a *parting* observing at its section, and each concern for our word is open, ○. Left from v391, each said here: *with no boundary* at 1.2; *A living same-existing set is a self* as 3.1's ground, and *one binary, a thing and a set*; collision 3's immune killing, stalk cells and policed workers, open at 5.2.")
    return "\n".join(L) + "\n"


def clean(marked):
    out = []
    for line in marked.split("\n"):
        s = line.strip()
        if s.startswith("Exhibit THIRTY-ONE Me ·"):
            out.append("Exhibit THIRTY-ONE Me")
            continue
        if s.startswith("*Marks:") or s.startswith("◇ *For our word*"):
            continue
        if s.startswith("- ○") or (s.startswith("- ✦") and " ◇ (" in s) or (s.startswith("- ✦") and "◇ (" in s.split(")")[0]):
            continue
        # drop ○ sentences inside paragraphs: from '○ ' to the next mark or end
        line = re.sub(r"\s*○ [^◇✦○]*?(?=(\s[◇✦○] )|\shttp|$)", "", line)
        line = line.replace("◇ ", "").replace("✦ ", "").replace(" ✓", "").replace("(○)", "")
        line = line.replace("- ✦ ", "- ")
        out.append(line)
    txt = "\n".join(out)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    return txt


def opens(marked):
    rows = []
    sec = "front"
    for line in marked.split("\n"):
        if line.startswith("*Marks:"):
            continue
        m = re.match(r"^## (\d\.\d) ", line)
        if m:
            sec = m.group(1)
        for o in re.findall(r"○ ([^◇✦○]+?)(?=(\s[◇✦○] )|\shttp|$)", line):
            rows.append("- **%s** · %s" % (sec, o[0].strip() if isinstance(o, tuple) else o.strip()))
        if line.strip().startswith("- ✦") and "◇ (" in line:
            name = re.search(r"\*\*([^*]+)\*\*", line)
            rows.append("- **%s** · observing to check before entering: %s" % (sec, name.group(1) if name else line[:60]))
    return "\n".join(rows) + "\n"


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    mk = build()
    open(os.path.join(OUT, "Exhibit_THIRTY-ONE_Me_next_marked.md"), "w", encoding="utf-8").write(mk)
    open(os.path.join(OUT, "Exhibit_THIRTY-ONE_Me_next_clean.md"), "w", encoding="utf-8").write(clean(mk))
    open(os.path.join(OUT, "open_places.md"), "w", encoding="utf-8").write(opens(mk))
    unt = [l for l in mk.split("\n") if "⟨untagged⟩" in l]
    print("built; untagged:", len(unt))
    for u in unt:
        print(" ", u[:90])
