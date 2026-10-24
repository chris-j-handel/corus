# Frontiers of life's chemistry: origins, homochirality, protein folding, biomolecular mechanism (standing as of 23 October 2026)

## Key gathered points

- **Access limits.** Web search was exhausted before any query ran, and most publisher domains were blocked. Claims were checked on a few Wikipedia pages (which cite primary DOIs) and in the project's own files; no primary paper was opened. Background-knowledge items are marked [unverified]. No 2026-dated development could be verified.
- **Cleanest binaries (observings with a stated criterion):**
  - F1, ribozyme self-replication: narrowing. A 45-nt polymerase ribozyme (QT45, 2024) reportedly copied itself and its complement with fair accuracy; sustained multi-round replication is not shown.
  - F12, asteroid amino acids: Bennu's (2025) show no chiral bias.
  - F13, thermodynamic vs kinetic control: settled protein by protein. Anfinsen holds for many small proteins; serpins and α-lytic protease are kinetically controlled [details unverified].
  - F21, FMO beats: reassessed in 2017–2020 as mainly vibrational [unverified].
  - F23b, Drosophila magnetoreception: reopened by a large 2023 null replication [unverified].
- **Most consequential explaining binaries:**
  - F2, strict RNA world vs peptide–RNA co-dependence: a 2017 polymerase ribozyme needed a lysine decapeptide; RNA–peptide coacervates enhance joining.
  - F3/F4, metabolism-first: non-enzymatic reverse-TCA fragments run under harsh conditions; full closure is not shown, and a 2007 kinetic and thermodynamic critique stands.
  - F5, vents vs wet–dry surface: unresolved.
  - F10/F11, homochirality: spin selectivity on magnetite (2023) is a directed mechanism with a locally set sign; the parity-violating energy difference (about 10⁻¹⁷ relative) is unmeasured.
- **Folding beyond entries 33, 177, 178:** fold switching estimated at 0.5–4% of PDB proteins (2018); disorder strains the structure–function paradigm; AlphaFold scored above 90 GDT on about two-thirds of CASP14 targets but reveals no folding mechanism.
- **Mechanism:** sources do not rank MWC against KNF; prefibrillar amyloid species are favoured as toxic, but fibrils are not innocuous; lecanemab's 27% slowing (−0.45 CDR-SB) does not separate oligomer from fibril causation; condensate necessity stays contested [unverified].
- **Genetic code:** "one in a million" error robustness and affinities for 6 of 8 amino acids are measured; structure alone does not separate the accounts.
- **Reading key.** [obs] observing · [recon] reconstruction from observings · [conv] convention or definition · [model] model construct · [sim] simulation. *Field adds* marks interpretation. "via WP" means read on that Wikipedia page, which cites the DOI shown. Proponent names are from general knowledge [unverified as positions].

## 1. Origins of life

### Takeaway
Origins binaries mostly explain one unobserved history. Laboratory capability results (near-self-copying ribozymes, non-enzymatic metabolic fragments, prebiotic nucleotide routes) narrow it without choosing. These go beyond project entries 12 and 208.

### Frontier binaries

#### F1 · Has a ribozyme replicated itself? [observing, laboratory]
- **Claim:** some ribozyme, given only mononucleotide or short-oligomer substrates, makes full-length functional copies of both itself and its complement, with fidelity sufficient for repeated rounds.
- **Negation:** no ribozyme under any tested condition does so.
- **Observings toward the claim:**
  - Primer-extension lengths grew over 1996–2021 [obs: gel and sequencing of in-vitro products]. All via [WP: Ribozyme](https://en.wikipedia.org/wiki/Ribozyme):
    - 6 nt ([Ekland & Bartel 1996](https://doi.org/10.1038/382373a0))
    - 14 nt ([Johnston 2001](https://doi.org/10.1126/science.1060786)), by a 189-nt ribozyme with 1.1% error per nucleotide
    - 95 nt at 0.0083 mutations per nucleotide ([Wochner 2011](https://doi.org/10.1126/science.1200752))
    - 206 nt in eutectic ice ([Attwater 2013](https://doi.org/10.1038/nchem.1781))
    - more than 177 nt at near-physiological Mg²⁺, which needed a lysine decapeptide ([Tagami 2017](https://doi.org/10.1038/nchem.2739))
  - Horning & Joyce's 24-3 amplified some RNAs up to 10⁴-fold and made a tRNA ([doi](https://doi.org/10.1073/pnas.1610103113)) [obs]. Its descendant 52-2 made functional class I ligase, its own ancestor, with fidelity below T7 RNA polymerase ([Portillo 2021](https://doi.org/10.7554/eLife.71557)) [obs].
  - 2024: QT45, a 45-nt polymerase ribozyme from random pools, reportedly synthesised its complement and a copy of itself with fair accuracy ([WP: RNA world](https://en.wikipedia.org/wiki/RNA_world); the page names no authors, and attribution to the Holliger lab is [unverified]).
  - A 2024 Joyce-lab PNAS paper reports a polymerase ribozyme replicating and evolving hammerhead ribozymes [unverified].
  - Ligation replicators work from pre-made halves: cross-replicating ligases double in about an hour ([Lincoln & Joyce 2009](https://doi.org/10.1126/science.1167856)), and a 20-nt ligase self-reproduces from two 10-mers ([Mizuuchi & Ichihashi 2023](https://doi.org/10.1039/d3sc01940c)) [obs]. *Field adds:* these replicators carry little information [interpretation].
- **Observings toward the negation:**
  - 38-6 cannot copy itself and mutates heavily ([Tjhung 2020](https://doi.org/10.1073/pnas.1914282117)) [obs].
  - Strand separation of long duplexes remains the obstacle. Ligation of 2′,3′-cyclic phosphates under strand-separation-compatible conditions gives high-fidelity copying ([Calaça Serrão 2024](https://doi.org/10.1021/jacs.3c10813), via WP) [obs].
- **Why hard:** products fold and stay paired to templates. Evolved polymerases (about 165–200 nt) are long relative to what they copy. The error threshold tightens as length grows [model].
- **Standing 2026:** narrowing. QT45 has not been independently reproduced in the sources seen here.
- **What would settle it:** two or more full rounds of copying of both strands from monomers or trimers, with sequence and activity of the copies verified, reproduced by an independent laboratory.
- **Proponents:** Joyce, Holliger, Unrau, Bartel and Szostak expect success. Skeptics of prebiotic relevance include Shapiro (prior) and Krishnamurthy [unverified].

#### F2 · Strict RNA world vs peptide–RNA co-dependence [explaining]
- **Claim:** there was a stage when RNA (or a nucleic-acid relative) was the sole heritable polymer and the main catalyst, before genetically encoded peptides.
- **Negation:** there was no such stage. From the first heritable polymer onward, non-encoded or encoded peptides were functionally required beside it.
- **Scope note:** lipid-first is a third account (see F9). The binary concerns only whether a peptide-free genetic stage existed.
- **Observings toward the claim:**
  - Ribozymes catalyse ligation, polymerisation and peptidyl transfer [obs] (F1).
  - Activated pyrimidine ribonucleotides (2′,3′-cyclic) form under plausible prebiotic conditions ([Powner, Gerland & Sutherland 2009](https://doi.org/10.1038/nature08013), via [WP: RNA world](https://en.wikipedia.org/wiki/RNA_world)) [obs].
  - *Field adds:* the ribosome's RNA catalytic core is read as a relic [interpretation].
- **Observings toward the negation:**
  - tC9-4M needed a lysine decapeptide at low Mg²⁺ ([Tagami 2017](https://doi.org/10.1038/nchem.2739)) [obs].
  - RNA–polylysine coacervates enhanced RNA joining, while excess long polylysine inhibited it (30 °C, pH 8.6, 10 mM MgCl₂) ([Le Vay 2023](https://doi.org/10.7554/eLife.83543), per the project's incoming report) [obs].
  - Glycine-spaced charged peptides keep ribozymes active in coacervates by raising RNA mobility and shifting Mg²⁺ partitioning ([Iglesias-Artola 2022](https://doi.org/10.1038/s41557-022-00890-8)) [obs].
  - Cyanosulfidic chemistry gives precursors of RNA, peptides and lipids together ([Patel 2015](https://doi.org/10.1038/nchem.2202)) [obs]. *Field adds:* co-synthesis is read as co-evolution [interpretation].
  - Sutherland himself calls the strict RNA world a restrictive hypothesis (via WP).
- **Why hard:** both pictures fit the ribosome and fit ribozyme capability. Co-presence of the molecules does not show co-dependence.
- **Standing 2026:** open and drifting toward co-dependence. In WP's account, the peptide–RNA view's cost is the coincident formation of two complex molecules.
- **What would settle it:** a peptide-free ribozyme system replicating and evolving under prebiotic conditions would make the claim possible. A demonstration that no RNA replicase works without peptides would favour the negation. Neither settles the history.
- **Proponents:** Gilbert (named the RNA world), Joyce, Orgel (prior), Szostak. On the co-dependence side: Carell, Krishnamurthy, Lehman, Carter & Wills [unverified].

#### F3 · Does a non-enzymatic reverse-TCA cycle close? [observing, laboratory]
- **Claim:** a non-enzymatic network containing the reductive TCA cycle (or a homologous cycle) runs closed and autocatalytic in one aqueous milieu under one geochemically plausible set of conditions. Closed means every intermediate is regenerated with net amplification.
- **Negation:** under no single such set of conditions does such a cycle close.
- **Observings toward the claim** (all via [WP: Reverse Krebs cycle](https://en.wikipedia.org/wiki/Reverse_Krebs_cycle)):
  - Metal ions, with iron as reductant, promoted 2- and 3-step sequences of the cycle in 1 M HCl or H₂SO₄ at 80–140 °C ([Muchowska 2017](https://doi.org/10.1038/s41559-017-0311-7)) [obs].
  - Mineral photochemistry drove some non-consecutive steps ([Zhang & Martin 2006](https://doi.org/10.1021/ja066103k)) [obs].
  - Aqueous microdroplets promoted reductive carboxylation and C–C bond formation ([Ju 2023](https://doi.org/10.1038/s41559-023-02193-8)) [obs].
  - Oxidation and reduction steps can cooperate toward a precursor of the glyoxylate and reverse Krebs cycles ([Muchowska 2019](https://doi.org/10.1038/s41586-019-1151-1)). The Fe²⁺ network from glyoxylate and pyruvate is [unverified in detail].
  - *Field adds:* iron sulfides at alkaline vents could have catalysed thioesterification and hydrolysis steps ([Akbari & Palsson 2023](https://doi.org/10.1073/pnas.2300687120)) [model]. Mineral catalysis may have persisted into LUCA ([Muchowska, Varma & Moran 2020](https://doi.org/10.1021/acs.chemrev.0c00191); [Harrison 2022](https://doi.org/10.1016/j.bbabio.2022.148597)) [interpretation].
- **Toward the negation:**
  - A complete non-enzymatic cycle is not viable on kinetic and thermodynamic grounds, and pyruvate → oxaloacetate is too endergonic to be driven by pyrophosphate ([Ross 2007](https://doi.org/10.1007/s11084-006-9017-6), via WP) [model].
  - Orgel argued in 2008 that metabolic cycles are implausible on the prebiotic Earth [unverified].
  - No closure is reported in the sources seen.
- **Why hard:** different steps want different conditions, side reactions drain intermediates, and yields are low. "Plausible" has no agreed criterion [conv].
- **Standing 2026:** open. Fragments are shown and closure is not.
- **What would settle it:** isotope-labelled, one-pot net amplification of all cycle intermediates under conditions with a stated geological analogue.
- **Proponents:** Wächtershäuser (prior), Moran, Martin, Russell, Lane, Ralser, and Krishnamurthy & Springsteen (glyoxylate variant). Critics: Orgel (prior), Ross [unverified].

#### F4 · Order: did template replication precede self-sustaining metabolism? [explaining, historical]
- **Scope note:** "genes-first vs metabolism-first" mixes capability (F1, F3) with order, and co-emergence is a third account. The proper binary is about order only.
- **Claim:** template-directed replication of an informational polymer arose before any self-sustaining autocatalytic reaction network.
- **Negation:** it did not arise before one. It arose together with one or after one.
- **Observings, both sides indirect:**
  - LUCA reconstructions: 355 likely genes from 6.1 million prokaryotic genes (2016). A LUCA age of about 4.2 Ga (4.09–4.33) was estimated in 2024 from pre-LUCA gene duplicates (both via [WP: Abiogenesis](https://en.wikipedia.org/wiki/Abiogenesis)) [recon]. Attribution to Weiss 2016 and Moody 2024 is [unverified].
  - More than 30 chemical events may separate a pre-RNA world from near-LUCA (WP) [recon].
  - Autocatalytic sets arise above a diversity threshold in model chemistries (project entry 12) [model].
  - Compositional networks may lack evolvability (Vasas, Szathmáry & Santos 2010) [unverified].
- **Why hard:** a single historical event with no chemical fossil. Both capabilities are partly shown in the laboratory.
- **Standing 2026:** open. The drift toward co-emergence ("systems chemistry") is an interpretation, not a result.
- **What would settle it:** strictly, nothing short of a historical record. Partial: a laboratory system in which one capability arises spontaneously and generates the other.
- **Proponents:**
  - genes-first: Gilbert, Orgel, Joyce, Szostak
  - metabolism-first: Wächtershäuser, Russell, Martin, Kauffman
  - co-emergence: Sutherland, Krishnamurthy [unverified]

#### F5 · Submarine vent vs subaerial origin [explaining, historical]
- **Scope note:** the sites are not exhaustive (ice, impact-crater systems), and stages may have differed in site. The proper binary is "submarine" vs "not submarine".
- **Claim:** the first compartmentalised replicating system arose at a submarine (alkaline) hydrothermal setting.
- **Negation:** it arose at an exposed land-surface setting (hot-spring pools, ponds, lakes with wet–dry cycling).
- **Vent-side observings** (via WP: Abiogenesis; [WP: Hydrothermal vent](https://en.wikipedia.org/wiki/Hydrothermal_vent)):
  - Alkaline vents carry natural pH gradients [obs]. *Field adds:* these could substitute for membrane pumps [model].
  - Vent-like mineral surfaces made methanol, formate, acetate and pyruvate from CO₂ under applied voltage or with H₂/H₂S [obs].
  - RNA oligomers up to 4 units formed in synthetic alkaline chimneys (2016) [obs].
  - Heat flow through cracked sapphire concentrated building blocks up to about 10³-fold (2024; no authors on WP) [obs].
  - Early cells may have been autotrophs with a Wood–Ljungdahl pathway [recon].
- **Surface-side observings** (via WP: Abiogenesis):
  - Wet–dry cycling with UV made RNA-like polymers that became encapsulated in vesicles (Deamer 2021) [obs; "RNA-like" is undefined].
  - Near-seawater NaCl destabilises fatty-acid membranes [obs].
  - LUCA's inferred intracellular ions (high K⁺/Na⁺, Mn²⁺, Zn²⁺, phosphate) match hot springs (Mulkidjanian) [recon].
  - Vents "do not concentrate" because of dilution, and no experiment has made sugars, amino acids, nucleotides or fatty acids under plausible vent conditions [stated absence].
  - Cyanosulfidic chemistry needs UV ([Patel 2015](https://doi.org/10.1038/nchem.2202)) [obs].
- **Exchange:** natural pH gradients could not have powered early life ([Jackson 2016](https://doi.org/10.1007/s00239-016-9756-6)). Lane replied that the critique misreads the work ([Lane 2017](https://doi.org/10.1002/bies.201600217)) (via [WP: Protocell](https://en.wikipedia.org/wiki/Protocell)).
- **Why hard:** no Hadean site survives. Each chemistry is shown in its own model setting, and the question merges several stages.
- **Standing 2026:** open.
- **What would settle it:** a continuous laboratory sequence under one site's conditions, from feedstocks to a replicating compartment. Partial: geological constraints on Hadean exposed land.
- **Proponents:** vents: Russell, Martin, Lane, Barge. Surface: Deamer, Damer, Mulkidjanian, Sutherland, Szostak, Benner [unverified].

#### F6 · Ribonucleotides via free ribose (formose) or not (cyanosulfidic)? [explaining]
- **Scope note:** other routes exist (Carell's purine route, borate routes), so the strict binary is "through free ribose" vs "not through free ribose".
- **Claim:** the first genetic polymer's ribonucleotides formed by attaching nucleobases to free ribose made by formose-type aldol chemistry.
- **Negation:** they formed by a route that never passes through free ribose.
- **Observings:**
  - Activated pyrimidine ribonucleotides form while bypassing free ribose and free base ([Powner 2009](https://doi.org/10.1038/nature08013)) [obs]. Selective 2′-phosphorylation of α-cytidine is a listed problem (WP: RNA world).
  - HCN, H₂S and UV give a cyanosulfidic network ([Patel 2015](https://doi.org/10.1038/nchem.2202)) [obs].
  - Formose: glycolaldehyde at about 3 ppm triggers autocatalytic sugar formation ([Breslow 1959](https://doi.org/10.1016/S0040-4039(01)99487-0)). Alkaline Cannizzaro reactions destroy aldoses, no selective way to isolate ribose is known, and attaching a pre-made sugar to a pre-made base is hard (all via [WP: Formose reaction](https://en.wikipedia.org/wiki/Formose_reaction)) [obs + interpretation].
  - Borate stabilises ribose ([Ricardo 2004](https://doi.org/10.1126/science.1092464)) [obs].
  - Ribose is present in carbonaceous meteorites ([Furukawa 2019](https://doi.org/10.1073/pnas.1907169116), via [WP: Murchison meteorite](https://en.wikipedia.org/wiki/Murchison_meteorite)) [obs]. Ribose reported in Bennu samples (2025) is [unverified].
  - WP says formose's origin-of-life importance is "no longer an accepted belief", citing [Omran 2020](https://doi.org/10.3390/life10080125) and [Sutton 2025](https://doi.org/10.1016/j.chempr.2025.102553). That is an editorial judgement whose source wording was not checked.
- **Why hard:** each route needs staged reagent additions or special minerals. Selectivity, not formation, is the crux.
- **Standing 2026:** open.
- **What would settle it:** a geochemically continuous synthesis giving ribonucleotides selectively, plus a discriminating trace such as an isomer or regiochemistry signature carried into later chemistry.
- **Proponents:** cyanosulfidic: Sutherland, Powner, Sasselov. Free ribose: Benner, Ricardo [unverified].

#### F7 · The water paradox: does polymerisation need a non-bulk-water step? [explaining, testable as observing]
- **Claim:** prebiotic polymerisation of nucleotides or amino acids to functional lengths needs a step outside dilute bulk water: drying, eutectic freezing, mineral surfaces, low water activity or a non-aqueous solvent.
- **Negation:** chemical activation alone, in dilute bulk water, reaches functional lengths.
- **Observings:**
  - RNA hydrolysis is aided by the 2′-OH. Cytosine's half-life is 19 days at 100 °C and about 17,000 years in freezing water (via WP: RNA world) [obs].
  - Wet–dry cycling gives polymers (F5) [obs].
  - A ribozyme made 206-nt strands in eutectic ice ([Attwater 2013](https://doi.org/10.1038/nchem.1781)) [obs].
  - 2′,3′-cyclic phosphate ligation copies RNA in water ([Calaça Serrão 2024](https://doi.org/10.1021/jacs.3c10813)) [obs].
  - Diamidophosphate phosphorylates and links components in water (2017; reference truncated on WP; Krishnamurthy attribution [unverified]).
  - Supercritical CO₂ is proposed as a dehydrating medium at vents (WP: Hydrothermal vent) [model].
- **Why hard:** condensation is uphill in water. Every escape (drying, freezing) also degrades or separates. "Functional length" is a convention.
- **Standing 2026:** open, with the field leaning to the claim [interpretation].
- **What would settle it:** functional-length polymers made in dilute water with only geochemically available activators. Their existence would establish the negation.
- **Proponents:** non-bulk steps: Deamer, Damer, Benner, Braun (thermophoresis). Aqueous activation: Krishnamurthy, Sutherland [unverified].

#### F8 · Phosphorus: reduced minerals or orthophosphate settings? [explaining]
- **Scope note:** the sources are not exclusive, so the binary concerns which was predominant.
- **Claim:** most phosphorus in the first nucleotides came via reduced phosphorus minerals (schreibersite, (Fe,Ni)₃P, meteoritic or lightning-formed).
- **Negation:** most came from orthophosphate or condensed phosphates made available in special settings.
- **Observings:**
  - Apatite weathering is the most common phosphate source, and modern Last Chance Lake concentrates phosphate (WP: Abiogenesis) [obs].
  - Schreibersite corrosion phosphorylates organics (Pasek) [unverified]. The schreibersite page was blocked.
  - Lightning fulgurites contain schreibersite (Hess 2021) [unverified].
  - Carbonate-rich lakes reach high phosphate (Toner & Catling 2020) [unverified].
  - Trimetaphosphate and diamidophosphate are activators (WP) [obs].
- **Why hard:** phosphate's insolubility with Ca²⁺. Yields in each scenario are measured under conditions that differ from scenario to scenario.
- **Standing 2026:** open.
- **What would settle it:** comparative phosphorylation yields under one shared geochemical scenario, plus Hadean mineralogical evidence.
- **Proponents:** Pasek (reduced P). Catling, Toner and Krishnamurthy (orthophosphate and activators) [unverified].

#### F9 · Can compositional (lipid) inheritance evolve? [observing in models/laboratory; explaining for history]
- **Claim:** assemblies without templates (lipid or compositional genomes) show heritable variation and selection over many generations.
- **Negation:** they do not, because variation is not heritable enough to accumulate.
- **Observings:**
  - GARD models show compositional replication [sim] (WP: Abiogenesis).
  - Fatty-acid vesicles grow by taking up micelles and divide under gentle shear while retaining contents ([Zhu & Szostak 2009](https://doi.org/10.1021/ja900919c)) [obs].
  - Montmorillonite speeds vesicle formation about 100-fold (WP: Protocell; popular-press source) [obs].
  - Citrate protects membranes while keeping Mg²⁺-assisted copying ([Adamala & Szostak 2013](https://doi.org/10.1126/science.1241888)) [obs].
  - Activated nucleotides cross fatty-acid membranes ([Mansy 2008](https://doi.org/10.1038/nature07018)) [obs].
  - No laboratory protocell has shown Darwinian evolution (WP) [stated absence].
- **Why hard:** compositional "genomes" have few heritable states. Vesicle fusion and fission scramble lineages.
- **Standing 2026:** open, theory leaning to the negation [unverified source].
- **What would settle it:** a multi-generation lineage experiment with measured heritability and response to selection.
- **Proponents:** Segré, Lancet (GARD). Critics: Szathmáry, Vasas [unverified].

### Inferences (origins)
- Every origins binary that is an observing (F1, F3, F9) concerns chemical capability. Every explaining binary (F2, F4–F8) concerns one unobserved history. Capability results narrow the histories without selecting one, which matches the project's entry 12 reach/unreachability note.
- Peptide dependence (F2) and non-bulk-water steps (F7) recur across sites, so the vent–surface binary (F5) may decompose by stage.

### Gaps (origins)
- 2025–2026 primary reports were not seen: the QT45 paper, the 2024 Joyce PNAS paper, Bennu sugars or brines, and any 2026 rTCA closure claims. Search budget and allowlist prevented it.

## 2. Homochirality

### Takeaway
L-amino acids and D-sugars are an observing; universal vs local choice of hand, and its amplification, are the explaining. In 2023–2025: spin-selective crystallisation on magnetite was shown (sign set by local magnetisation), Bennu's amino acids were racemic, and the PVED stayed unmeasured. Project entry 63 and the SIXTEEN carryings (Kondepudi 1990, Viedma 2005) hold prior material.

### Frontier binaries

#### F10 · Universal vs local sign [explaining]
- **Claim:** the biological sign (L-amino acids, D-sugars) was fixed by an asymmetry favouring the same hand everywhere in the universe, such as weak-force parity violation or a universally biased radiation source.
- **Negation:** the sign was fixed by a local, contingent event, a fluctuation or a local chiral field, and would have been the opposite hand with equal probability elsewhere.
- **Observings toward the claim:**
  - Parity is violated in weak interactions [obs, physics] (via [WP: Homochirality](https://en.wikipedia.org/wiki/Homochirality)).
  - The parity-violating energy difference (PVED) between enantiomers is calculated at about 10⁻¹⁷ in relative terms (project entry 63) [model]. WP finds no demonstrated link between PVED and molecular chirality.
  - **F10a (observing): has a PVED been measured in any molecule?** No measurement is reported in the sources seen. Precision vibrational spectroscopy attempts on chiral molecules are [unverified].
  - The Vester–Ulbricht hypothesis (beta-decay chirality biasing biomolecules) is historically notable and not established (WP) [model].
- **Observings toward the negation:**
  - Stirred NaClO₃ crystallisation gives batches of nearly one hand, the hand varying between batches ([Kondepudi, Kaufman & Singh 1990](https://doi.org/10.1126/science.250.4983.975), project SIXTEEN carryings) [obs].
  - Viedma: a racemic NaClO₃ slurry ground with glass balls at 24 °C reached total symmetry breaking within 24 h, L or D at random; without balls it stayed unchanged for days ([Viedma 2005](https://arxiv.org/abs/cond-mat/0407479), project carryings) [obs].
  - A stirred suspension of a nearly racemic, solution-racemising amino-acid derivative went to a single-enantiomer solid (WP; [Noorduin 2008](https://doi.org/10.1021/ja7106349) in its references) [obs].
  - The Soai autocatalysis amplifies low ee to high ee ([Soai 1995](https://doi.org/10.1038/378767a0)). Its sign is steered by cryptochiral hydrocarbons ([Kawasaki 2006](https://doi.org/10.1021/ja061429e)) and by a ligand chiral only through ¹⁴N/¹⁵N (45% ee as a stoichiometric ligand; [Matsumoto 2016](https://doi.org/10.1002/anie.201608955)). Its kinetics are analysed by [Islas 2005](https://doi.org/10.1073/pnas.0503171102) (all via [WP: Soai reaction](https://en.wikipedia.org/wiki/Soai_reaction)) [obs].
  - A slight proline excess gives a large product ee ([Mathew, Iwamura & Blackmond 2004](https://doi.org/10.1002/anie.200453997)) [obs].
  - Mirror faces of calcite adsorb D- and L-aspartate differently ([Hazen, Filley & Goodfriend 2001, PNAS 98:5487](https://api.openalex.org/works/pmid:11331767), project SIXTEEN carryings) [obs].
  - Autocatalysis with mutual inhibition gives symmetry breaking ([Frank 1953](https://doi.org/10.1016/0006-3002(53)90082-1)) [model]. Noise alone can drive self-replicators to homochirality ([Jafarpour, Biancalani & Goldenfeld 2015](https://doi.org/10.1103/PhysRevLett.115.158101)) [model; content unverified].
- **Why hard:** the amplifiers act on any seed, so amplification erases the seed's origin. A bias near 10⁻¹⁷ falls below statistical fluctuations at any feasible pool size [model]. Earth's single lineage gives no second sample.
- **Standing 2026:** open. Amplification is settled in the laboratory; the source of the sign is not.
- **What would settle it:** a measured PVED with a shown mechanism that carries it into amplification. Alternatively, homochiral biochemistry of the opposite hand, or of the same hand, found in an independent origin elsewhere. A second sample from Mars or the icy moons could decide.
- **Proponents:** universal: Quack, and the Mason–Tranter PVED calculations [unverified]. Local: Blackmond, Soai, Viedma, Kondepudi [unverified as positions].

#### F11 · Spin-selective crystallisation on magnetite: a prebiotic route to the hand? [observing in laboratory; explaining for history]
- **Claim:** under early-Earth-plausible conditions, chirality-induced spin selectivity (CISS) at magnetised magnetite enantioenriches an RNA precursor to near-homochirality.
- **Negation:** it does not, under any early-Earth-plausible conditions.
- **Scope note:** the sign is set by the local magnetisation direction, so even a true claim lies on F10's local side unless a planet-wide aligning field is added [model].
- **Observings toward the claim:**
  - A spin-polarised magnetite surface preferentially adsorbed one enantiomer of ribo-aminooxazoline (RAO) and seeded its crystallisation. RAO crystallises as a conglomerate, and dissolution–recrystallisation reached full enantiopurity in two steps ([Ozturk et al. 2023, Science Advances](https://doi.org/10.1126/sciadv.adg8274), via [WP: Homochirality](https://en.wikipedia.org/wiki/Homochirality)) [obs]. Crystallisation conditions and ee per step are [unverified].
  - Related papers: [Ozturk & Sasselov 2022 PNAS](https://doi.org/10.1073/pnas.2204765119) (spin-polarised electrons) and [Ozturk, Sasselov & Sutherland 2023 J. Chem. Phys.](https://doi.org/10.1063/5.0156527) (a "central dogma" passing chirality from RNA precursors onward) [model]. [Ozturk & Sasselov 2025 PNAS](https://doi.org/10.1073/pnas.2505126122) content [unverified].
  - CISS itself: chiral films scatter polarised electrons asymmetrically ([Ray 1999](https://doi.org/10.1126/science.283.5403.814)) [obs].
  - Magnetite is present in Bennu samples ([WP: 101955 Bennu](https://en.wikipedia.org/wiki/101955_Bennu)) [obs; this establishes only that the mineral exists in such bodies].
- **Toward the negation:**
  - CISS theory: spin–orbit models explain the effect qualitatively, but predicted magnitudes are orders of magnitude below those measured ([WP: CISS](https://en.wikipedia.org/wiki/Chirality-induced_spin_selectivity); review [Evers 2022](https://doi.org/10.1002/adma.202106629)) [model gap].
  - Natural magnetite's domain orientation, and RAO's place in a continuous prebiotic sequence, are not shown [stated absence in sources seen].
- **Why hard:** the mechanism lacks a quantitative theory. Scale-up from a laboratory surface to a lake is untested.
- **Standing 2026:** narrowing at laboratory scale. No independent reproduction was seen.
- **What would settle it:** independent replication; enrichment with natural magnetite under a geomagnetic-strength field; and demonstrated transfer of RAO's ee to ribonucleotides and then to amino acids.
- **Proponents:** Sasselov, Ozturk, Sutherland, Naaman (CISS). Skeptics include CISS theorists who question the magnitude [unverified].

#### F12 · Did extraterrestrial organics carry a biased hand to Earth? [observing for samples; explaining for seeding]
- **Claim (observing):** indigenous chiral amino acids in pristine asteroid-return samples show L-excesses.
- **Negation:** they are racemic within measurement error.
- **Observings:**
  - **Bennu.** OSIRIS-REx returned about 121.6 g on 24 September 2023 ([WP: 101955 Bennu](https://en.wikipedia.org/wiki/101955_Bennu)) [obs]. The January 2025 reports found 14 of the 20 protein amino acids and all five nucleobases, with amino acids of mixed chirality [obs; method LC-MS presumed, [unverified]]. Primary source: [Glavin et al. 2025, Nature Astronomy](https://doi.org/10.1038/s41550-024-02472-9), cited by WP.
  - WP: Bennu and Ryugu amino acids show no chiral bias [obs]. Ryugu primary source [unverified].
  - **Murchison.** L-excesses were reported in several non-protein amino acids ([Cronin & Pizzarello 1997](https://doi.org/10.1126/science.275.5302.951)) [obs]. An early alanine L-excess ([Engel & Nagy 1982](https://doi.org/10.1038/296837a0)) was questioned as contamination ([Bada 1983](https://doi.org/10.1038/301494a0)) (via [WP: Murchison meteorite](https://en.wikipedia.org/wiki/Murchison_meteorite)).
  - **Conflict:** WP's Homochirality page says Murchison contained only racemic amino acids. That contradicts the Cronin & Pizzarello report as WP's own Murchison page gives it. The conflict is recorded here, not resolved.
  - *Field adds:* circularly polarised light in star-forming regions could bias photolysis (project entry 63) [model + astronomical obs].
- **Why hard:** terrestrial contamination with L-amino acids. Excesses appear in non-protein amino acids such as isovaline, possibly enhanced by aqueous alteration [unverified]. Sample-to-sample variation is large.
- **Standing 2026:** for Bennu, racemic, settled as an observing pending further aliquots. Meteoritic seeding as an explanation is weakened, though excesses in some meteorites stand.
- **What would settle it:** compound-specific isotope analyses tying excesses to indigenous origin across many bodies, and a laboratory or astrophysical source producing the observed sign.
- **Proponents:** Glavin, Dworkin, Pizzarello (meteoritic excesses); Bada (contamination critique) [unverified as positions].

### Inferences (homochirality)
- F10's two sides predict different things about a second origin: universal bias predicts the same hand, local choice a coin flip. That makes F10 the one homochirality binary a future observing could close.
- The amplifiers (Soai, Viedma, Frank-type) are settled observings and models, but they are sign-agnostic. They narrow the question to the seed.

### Gaps (homochirality)
- The primary Ozturk 2023 and Glavin 2025 texts were not opened (the allowlist blocked them), so per-step ee values, isovaline values for Bennu, and Ryugu data are unverified.
- PVED measurement status after 2020 could not be checked.

## 3. Protein folding beyond Levinthal, fold-as-kind and the single native state

### Takeaway
Entries 33, 177 and 178 already carry the three-question framing, ensemble refinement and fold continuity. Added here: minimum vs kinetic trap per protein (F13), fold-switch prevalence (F14), disorder and function (F15), and what learned prediction shows (F16).

### Frontier binaries

#### F13 · Is the functional native state the global free-energy minimum, or a kinetically trapped state? [observing, per protein]
- **Claim:** for a given natural protein under physiological conditions, the functional native state is the global free-energy minimum and is reached reversibly from the unfolded chain without assistance. This is Anfinsen's thermodynamic hypothesis.
- **Negation:** for that protein, the functional state is not the global minimum. It is separated from a more stable or equally stable state by barriers that make it kinetically controlled.
- **Scope note:** as a universal law this is an explaining binary. Per protein it is an observing, and only the per-protein form can be settled.
- **Observings toward the claim:**
  - Denatured ribonuclease refolds to its active form once denaturant and reductant are removed ([Anfinsen 1972](https://doi.org/10.1042/bj1280737); [1973](https://doi.org/10.1126/science.181.4096.223), via [WP: Protein folding](https://en.wikipedia.org/wiki/Protein_folding)) [obs]. The details (urea, β-mercaptoethanol, activity recovery) come from general knowledge [unverified].
  - Many small domains fold reversibly and two-state in vitro [obs; general, unverified].
- **Observings toward the negation:**
  - Serpins: the active inhibitory form is metastable. The latent form of PAI-1, with the reactive loop inserted into the sheet, is more stable [unverified].
  - α-Lytic protease: the unfolded and intermediate states are reported to be more stable than the native state. Folding needs the pro-region, and unfolding is extremely slow (Sohl, Jaswal & Agard 1998, Nature) [unverified].
  - Prions: the host protein PrP adopts a self-propagating alternative fold ([Selkoe 2003](https://doi.org/10.1038/nature02264); [Soto 2006](https://doi.org/10.1016/j.tibs.2006.01.002), via WP) [obs + model].
  - Kuru: the PrP V127 variant resisted conversion and inhibited wild-type prion propagation in a dose-dependent way in transgenic mice ([Asante 2015](https://www.nature.com/articles/nature14510), project SEVENTEEN carryings) [obs].
  - Chaperones assist folding in cells ([Hartl 2011](https://doi.org/10.1038/nature10317)) [obs]. *Field adds:* whether they change the end state or only the rate is model-dependent [interpretation].
- **Why hard:** stability is measured relative to the reference states that happen to be accessible. Aggregated states such as amyloid may be lower in free energy than the native state at high concentration [model]. In vivo, folding starts co-translationally (project entry 33 cites Cassaignau 2020).
- **Standing 2026:** settled per protein. The thermodynamic hypothesis holds for many small proteins and fails for documented cases. As a general law it is narrowed, not refuted.
- **What would settle it:** for each protein, measure folded, unfolded and alternative-state free energies under the same conditions and test refolding from the denatured state without chaperones or pro-regions.
- **Proponents:** Anfinsen (prior), Baldwin, Dill. Kinetic control: Agard, and serpin structural biologists such as Carrell and Whisstock [unverified].

#### F14 · Is fold switching a widespread property of natural proteins? [observing, with a definitional dependence]
- **Claim:** a non-negligible fraction of natural proteins, at least about 1%, remodel their secondary structure reversibly between distinct folds under physiological conditions, as part of their function.
- **Negation:** fold switching is confined to rare, idiosyncratic cases, well below 1%.
- **Observings toward the claim:**
  - Porter & Looger searched PDB entries with the same sequence but different secondary structure and estimated that about 0.5–4% of PDB proteins switch folds ([2018](https://doi.org/10.1073/pnas.1800168115), via WP) [recon].
  - KaiB switches folds over the day in the cyanobacterial clock (WP) [obs].
  - RfaH's C-terminal domain refolds from an α-helical hairpin to a β-barrel on recruitment to a paused transcription complex, binds ribosomal protein S10, and returns after release. Seen by NMR and functional assays ([Zuber 2019](https://doi.org/10.1038/s41467-019-08567-6), as summarised in the project's incoming chemistry report) [obs].
  - Lymphotactin, Mad2 and CLIC1 are other examples [unverified].
- **Toward the negation:** the estimate depends on PDB coverage and on calling a "switch" from secondary-structure differences, so crystal contacts or truncations could produce artefacts [interpretation]. There is no independent census.
- **Why hard:** the second fold is often visible only under particular partners or conditions. Learned predictors usually return one fold. Whether AlphaFold-based approaches recover alternative folds (Chakravarty & Porter, 2022–2025) is [unverified].
- **Standing 2026:** narrowing toward the claim at the 2018 estimate's lower bound. No consensus figure exists.
- **What would settle it:** a proteome-scale assay, for example NMR or HDX-MS screening under several partner conditions, with an agreed definition of "distinct fold". That definition is a convention, linked to entry 177.
- **Proponents:** Porter, Looger, Artsimovitch (RfaH), Golden (KaiB). Skeptics are not identified in the sources seen.

#### F15 · Does disorder break the one-structure, one-function link? [explaining; observing sub-binary]
- **Claim:** for a substantial class of proteins, function is carried by conformational ensembles without a dominant folded structure, such as disordered regions, fuzzy complexes and coupled folding and binding, so a single structure does not specify the function.
- **Negation:** for every functional protein region, a dominant structure, at least in the bound state, specifies the function.
- **F15a (observing): do disordered regions stay heterogeneous in their functional bound complexes?** Fuzzy complexes are reported [unverified].
- **Observings:**
  - Ensemble refinement fits crystallographic data better than single models for 20 datasets at 1.1–3.1 Å ([Burnley 2012](https://doi.org/10.7554/eLife.00311), project entry 178) [obs + model].
  - Disorder is functional and widespread in signalling (Wright & Dyson 2015, Nat Rev Mol Cell Biol 16:18–29, cited in project entry 178) [recon].
  - Young de novo genes tend to encode disordered proteins ([Wilson 2017](https://doi.org/10.1038/s41559-017-0146)), with hydrophobic patterning that differs from globular folds ([Foy 2019](https://doi.org/10.1534/genetics.118.301719)) (via WP) [recon].
  - Proteome disorder fractions (eukaryotes higher than prokaryotes) are [unverified]: they depend on the predictor.
- **Why hard:** "disordered" depends on method (NMR, SAXS, CD, protease sensitivity, predictors) [conv]. Many regions fold on binding, which supports the negation in its bound-state form.
- **Standing 2026:** open as a paradigm question. That disordered regions exist is settled.
- **What would settle it:** for representative disordered-region complexes, ensemble-resolved structures in the bound state, showing whether heterogeneity persists and whether function tracks the ensemble rather than one conformer.
- **Proponents:** Wright, Dyson, Uversky, Tompa, Fuxreiter, Pappu. Partisans of the classical structure–function view are not named in the sources seen [unverified].

#### F16 · Does learned structure prediction capture folding physics, or reproduce known structures? [explaining; observing sub-binary]
- **Claim:** AlphaFold-class networks encode transferable physical determinants of structure. They predict accurately for sequences and folds without close training homologues, and they predict structural responses to mutations and alternative states.
- **Negation:** they mainly reproduce structural regularities in the training database. Accuracy drops for orphan sequences and novel folds, and mutation-induced or alternative states are not reliably predicted.
- **F16a (observing):** is accuracy on targets with no detectable training homologue statistically indistinguishable from accuracy on targets with homologues? CASP-style blind tests can answer this.
- **Observings:**
  - At CASP14 (2020), AlphaFold ranked first and scored above 90 GDT for about two-thirds of targets. For about a third accuracy was not high enough, and it does not reveal the physical folding mechanism, so the folding problem is not considered solved (WP: Protein folding) [obs + interpretation].
  - Jumper et al. 2021, Nature 596:583, and the 2024 Nobel Prize in Chemistry (project entry 33).
  - Failures on orphan sequences and novel folds are cited as evidence in the "solution vs interpolation" dispute (project entry 33) [interpretation; primary sources unverified].
  - AlphaFold3 (2024) extends to ligands and nucleic acids with diffusion; low-similarity ligand cases are the reported edge (project entry 33) [unverified].
  - Weak prediction of point-mutation effects and of fold-switch states [unverified].
- **Why hard:** "physics" and "regularities" may not separate, because physics produced the regularities. There is no agreed out-of-distribution benchmark.
- **Standing 2026:** open. Prediction accuracy is settled as an observing; what is captured is not.
- **What would settle it:** blind prediction of de novo folds absent from training, of designed fold switchers, and of the thermodynamic effects of mutations, scored against experiment.
- **Proponents:** Jumper, Hassabis, Baker (design as inverse test). Critics who stress the limits: Dill, Moult, Porter [unverified as positions].

### Inferences (folding)
- F13 and F14 together turn entry 178's question into a measurable one. The native state is a protein-specific relation among free energies, barriers, partners and conditions, not a property of the sequence alone. That fits the project's rule of stating each class's membership criterion: "native" needs its criterion.
- F16a is the one observing that could narrow entry 33's third question.

### Gaps (folding)
- Serpin and α-lytic protease primary data, the 2023–2026 fold-switch prediction papers, and CASP15/16 results were not verified.

## 4. Mechanism in biomolecules

### Takeaway
F17 and F18 are explaining choices between schemes that fit the same binding curves and separate only in kinetics or intermediates; as ensembles they are often limiting cases of one model. F19 and F20 are causal questions where interventions do not yet isolate the agent.

### Frontier binaries

#### F17 · Allostery: concerted (MWC) or sequential (KNF)? [explaining, per protein]
- **Claim:** for a given oligomeric protein, cooperative ligand binding results from a concerted equilibrium between whole-oligomer states, all subunits in T or all in R, as in [Monod, Wyman & Changeux 1965](https://doi.org/10.1016/s0022-2836(65)80285-6).
- **Negation:** for that protein, cooperativity results from ligand-induced changes in individual subunits passed sequentially to neighbours, with mixed-conformation oligomers populated ([Koshland, Némethy & Filmer 1966](https://doi.org/10.1021/bi00865a047)).
- **Scope note:** further accounts are not binary partners, so these are recorded here and kept out of the binary:
  - ensemble allostery ([Motlagh 2014](https://doi.org/10.1038/nature13001); [Hilser 2012](https://doi.org/10.1146/annurev-biophys-050511-102319))
  - dynamic allostery without conformational change ([Cooper & Dryden 1984](https://doi.org/10.1007/BF00276625))
  - morpheein dissociative allostery ([Jaffe 2005](https://doi.org/10.1016/j.tibs.2005.07.003))
  - All via [WP: Allosteric regulation](https://en.wikipedia.org/wiki/Allosteric_regulation).
- **Observings:**
  - Haemoglobin's binding curve is sigmoidal, and 2,3-BPG lowers its affinity ([Edelstein 1975](https://doi.org/10.1146/annurev.bi.44.070175.001233)) [obs].
  - Crystal structures of T and R haemoglobin (Perutz; [5.5 Å, 1960](https://doi.org/10.1038/185416a0), via [WP: Hemoglobin](https://en.wikipedia.org/wiki/Hemoglobin)) [obs].
  - Tertiary changes within the T quaternary state (Eaton's tertiary two-state model) are [unverified].
  - Negative cooperativity is often cited as possible only under KNF [unverified; WP does not state it].
- **Why hard:** both schemes fit sigmoidal curves with few parameters. Telling them apart needs populations of mixed states, which most methods cannot resolve. WP says many effects can be explained by either.
- **Standing 2026:** open as a general question. Per protein it is often resolved, but only by intermediate-resolving methods [unverified].
- **What would settle it:** single-molecule or native mass-spectrometry counts of mixed-ligation, mixed-conformation oligomers across ligand concentration, protein by protein.
- **Proponents:** MWC: Changeux, Edelstein, Eaton. KNF: Koshland (prior). Ensemble view: Hilser, Kern, Nussinov [unverified].

#### F18 · Ligand binding: conformational selection or induced fit? [explaining, testable per system]
- **Claim:** for a given protein–ligand pair under given concentrations, most binding flux passes through a binding-competent conformation already present before the ligand binds (conformational selection).
- **Negation:** most flux passes through the ligand first binding a non-competent conformation, which then changes (induced fit).
- **Scope note:** both pathways can run in parallel. Which one dominates depends on concentrations and rate constants (Hammes, Chang & Oas 2009) [unverified]. The binary is properly about dominant flux under stated conditions.
- **Observings:** relaxation-dispersion NMR shows minor states [obs; unverified examples]. The concentration dependence of the observed relaxation rate is used as a diagnostic, but it is ambiguous [model]. No primary sources were opened; the WP pages were blocked.
- **Why hard:** the same equilibrium fits both, and kinetic signatures overlap.
- **Standing 2026:** reframed rather than settled. The question is now posed per system.
- **What would settle it:** per system, single-molecule trajectories that show the order of events at stated concentrations.
- **Proponents:** Koshland (induced fit, prior); Nussinov, Kern, Boehr & Wright (conformational selection); Hammes, Oas (flux framing) [unverified].

#### F19 · Amyloid toxicity: oligomers or fibrils? [explaining]
- **Claim:** in amyloid diseases, cell and synapse damage comes mainly from soluble prefibrillar oligomers rather than mature fibrils.
- **Negation:** it comes mainly from mature fibrils and deposits, including their surfaces and bulk effects.
- **Scope note:** fibrils make oligomers through secondary nucleation, so the agents are coupled. Multi-agent toxicity is a third account.
- **Observings toward the claim** (all via [WP: Amyloid](https://en.wikipedia.org/wiki/Amyloid)):
  - Oligomers form membrane channels and activate NMDA and AMPA receptors ([Kagan 2004](https://doi.org/10.1007/s00232-004-0709-4)) [obs, in vitro].
  - Calcium dysregulation appears early ([Demuro 2005](https://doi.org/10.1074/jbc.M500997200)) [obs].
  - An "emerging consensus" ([Ferreira 2007](https://doi.org/10.1080/15216540701283882)) [interpretation].
- **Observings toward the negation:**
  - Fibrils are not innocuous: they release oligomers and catalyse oligomer formation by secondary nucleation ([Chiti & Dobson 2017](https://doi.org/10.1146/annurev-biochem-061516-045115)) [model + obs].
  - Two α-synuclein fibril polymorphs differ in toxicity ([Gath 2014](https://doi.org/10.1371/journal.pone.0090659)) [obs].
  - Deposits disrupt tissue architecture [obs].
- **Clinical and population evidence:**
  - Lecanemab (CLARITY AD): in 1,795 people with early Alzheimer's disease over 18 months, CDR-SB worsened by 1.21 on drug vs 1.66 on placebo. The difference, −0.45 (−0.67 to −0.23), is 27% of the placebo change. Amyloid fell by 59.1 centiloids more on drug (n=698). ARIA with oedema occurred in 12.6% ([van Dyck 2023, NEJM 388:9](https://doi.org/10.1056/NEJMoa2212948), via project ELEVEN carryings) [obs].
  - Lecanemab's preferential binding to protofibrils is [unverified].
  - Amyloid positivity in cognitively normal people rose from 10% at age 50 to 44% at age 90 ([Jansen 2015](https://doi.org/10.1001/jama.2015.4668)) [obs].
  - The Aβ*56 oligomer paper (Lesné 2006) was retracted in 2024 [unverified]. That retraction removes one oligomer agent but does not decide the binary.
- **Why hard:** oligomers are heterogeneous and transient, hard to isolate in tissue, and their preparations are defined by protocol [conv]. Antibodies bind several species.
- **Standing 2026:** open, with a lean toward the claim [interpretation]. Trials support a role for aggregated Aβ without separating oligomers from fibrils.
- **What would settle it:** species-selective interventions in vivo, such as agents clearing only fibrils or only defined oligomers, with outcome measures, plus quantified oligomer burden in human tissue.
- **Proponents:** oligomers: Klein, Selkoe, Walsh, Glabe, Dobson (prior), Knowles. Fibril or deposit roles and multi-agent views: Eisenberg (structures), Jucker & Walker [unverified as positions].

#### F20 · Are condensates required for function, or by-products? [explaining; observing per case]
- **Claim:** for a given cellular process, formation of a phase-separated or percolated condensate is required for the process's normal rate or specificity, and abolishing condensation alone, with composition preserved, impairs the process.
- **Negation:** condensation is incidental. Abolishing it, with composition and interactions preserved, leaves the process unchanged.
- **Observings:**
  - Liquid-like P granules (Brangwynne & Hyman, 2009) are the founding observation [unverified].
  - Evidence standards for in-vivo phase separation were questioned (McSwiggen 2019) [unverified].
  - 1,6-hexanediol has non-specific effects, and fixation can create puncta [unverified].
  - RNA–peptide coacervates enhance ribozyme joining in vitro ([Le Vay 2023](https://doi.org/10.7554/eLife.83543)) [obs]. This is an in-vitro analogue only.
- **Why hard:** separating condensation from the multivalent interactions that cause it means mutations that remove one also remove the other. Concentration, viscosity and partitioning all change together.
- **Standing 2026:** open, settled case by case at best [unverified]. No primary or WP condensate source could be opened this session.
- **What would settle it:** separation-of-function mutants or designed condensation-only perturbations, such as optogenetic seeding with constant binding valence, and quantitative rate measurements in cells.
- **Proponents:** functional: Hyman, Brangwynne, Rosen, Pappu, Banani. Skeptics on evidence standards: McSwiggen, Darzacq, Tjian; also Mittag [unverified as positions].

### Inferences (mechanism)
- F17 and F18 share one structure: two kinetic schemes that coincide at equilibrium. Each reduces to an observing only when intermediates are counted. In the project's terms they are binaries of sequence (prior, now, next), not of end state [framing note only].

### Gaps (mechanism)
- The WP pages on condensates, induced fit and conformational selection were blocked. No 2023–2026 condensate or allostery primary sources were verified.

## 5. Quantum-biology binaries

### Takeaway
Each question splits into an observing (is the signal there, with what lifetime or spin dependence?) and an explaining (does it serve a function?). Nearly every source here was blocked, so these entries rest mainly on background knowledge, marked [unverified].

### Frontier binaries

#### F21 · Are the long-lived FMO beats electronic or vibrational? [observing]
- **Claim:** the oscillations in two-dimensional electronic spectra of the Fenna–Matthews–Olson (FMO) complex that last several hundred femtoseconds at 77 K are mainly electronic (excitonic) coherence.
- **Negation:** they are mainly vibrational or vibronic coherence, ground-state or excited-state, and the electronic coherence decays far faster.
- **Observings:**
  - Engel et al. 2007 (Nature 446:782) reported quantum beating lasting at least about 660 fs at 77 K by 2D electronic spectroscopy [unverified].
  - Later claims extended it to room temperature (Panitchayangkoon 2010, PNAS) [unverified].
  - Duan et al. 2017 (PNAS 114:8493) measured electronic coherence decaying within about 60 fs at 77 K and assigned the long-lived beats to vibrations [unverified].
  - Thyrhaug 2018 and Cao et al. 2020 (Science Advances, "Quantum biology revisited") are reassessments [unverified].
  - [WP: Photosynthesis](https://en.wikipedia.org/wiki/Photosynthesis) asserts a "quantum walk" efficiency gain, tagged citation-needed; unsourced, not to be relied on.
- **Why hard:** spectral overlap of vibrational and electronic signals, inhomogeneous broadening, and sample and pulse differences between laboratories.
- **Standing 2026:** narrowing toward the negation since 2017–2020 [unverified].
- **What would settle it:** polarisation-controlled and isotope-substituted 2DES, reproduced across laboratories, with assignments checked against vibronic models.
- **Proponents:** claim: Engel, Fleming. Reassessment: Miller (Duan), Thorwart, Cao, Scholes on vibronic mixing [unverified].

#### F22 · Does coherence raise transfer efficiency in vivo? [explaining]
- **Claim:** quantum coherence among pigment excitations measurably increases light-harvesting efficiency in living photosynthetic organisms compared with incoherent hopping.
- **Negation:** under physiological conditions transfer is adequately described by incoherent (Förster-type) or noise-assisted hopping, with no functional gain from coherence.
- **Observings:** none direct in vivo. 2DES is done on isolated complexes, and efficiency gains come from models such as environment-assisted transport [model] [unverified].
- **Why hard:** natural sunlight is incoherent, so whether coherent excitation dynamics apply in vivo is itself disputed [unverified]. No knock-out of coherence exists.
- **Standing 2026:** open, leaning to the negation for "long-lived" coherence. Vibronic mixing remains a live functional idea [unverified].
- **What would settle it:** a mutant or isotope variant that changes coherence lifetimes without changing energetics, with measured transfer efficiency.
- **Proponents:** Fleming, Engel, Aspuru-Guzik (models); critics: Miller, Cao, Wang [unverified].

#### F23 · Is animal magnetoreception radical-pair (cryptochrome) or magnetite-based? [explaining, per taxon]
- **Scope note:** this is not one binary across animals. Both mechanisms, and others, may operate in different taxa. It is split per taxon and modality:
  - **F23a (explaining):** in night-migratory songbirds, is the light-dependent magnetic compass a radical-pair mechanism in retinal cryptochrome, or not?
  - **F23b (observing):** does Drosophila show reproducible cryptochrome-dependent magnetic behaviour?
- **F23a observings:**
  - The radical-pair compass was proposed by Schulten in 1978 and Ritz in 2000 [unverified].
  - Weak broadband radio-frequency noise disrupts robin orientation (Engels et al. 2014, Nature 509:353) [unverified].
  - Purified European robin Cry4a showed magnetically sensitive photochemistry stronger than chicken or pigeon Cry4 (Xu et al. 2021, Nature 594:535) [unverified].
  - Magnetite-based alternative: the iron-rich cells in the pigeon beak were shown to be macrophages (Treiber et al. 2012, Nature 484:367), undermining that candidate [unverified].
- **F23b observings:** cryptochrome-dependent magnetic responses were reported (Gegear 2008, Nature) [unverified]. A large 2023 replication effort reported no reproducible magnetic-field effects in several Drosophila behavioural assays (Bassetto et al. 2023, Nature 620:595) [unverified].
- **Why hard:** the signals are small and behaviour is noisy. Magnetic contamination in laboratories, plus a radical-pair sensitivity in vitro that is weaker than behavioural thresholds seem to require [unverified].
- **Standing 2026:** F23a narrowing toward the radical pair for songbirds, without the receptor shown in vivo. F23b reopened after 2023 [unverified].
- **What would settle it:** for F23a, in-vivo cell-type-specific cryptochrome knockouts in migratory birds with blinded orientation tests. For F23b, pre-registered, multi-laboratory replication.
- **Proponents:** radical pair: Hore, Mouritsen, Schulten (prior). Magnetite: Kirschvink, Winklhofer. Drosophila replication: Bassetto, Mouritsen, Hore [unverified].

#### F24 · Smell: shape or vibration? [explaining; historically notable, largely rejected]
- **Claim:** olfactory receptors discriminate odorants partly by their molecular vibrational spectra, through inelastic electron tunnelling (Turin 1996).
- **Negation:** receptors discriminate by shape and chemical features, with no dependence on vibrational frequency beyond its effects on structure.
- **Observings (all unverified):**
  - Humans did not discriminate acetophenone from its deuterated form in the tested setting (Keller & Vosshall 2004, Nature Neuroscience).
  - Drosophila distinguished deuterated from normal odorants (Franco et al. 2011, PNAS).
  - Humans distinguished some musk isotopologues (Gane et al. 2013, PLoS ONE).
  - Receptor assays found no isotope discrimination by a musk receptor (Block et al. 2015, PNAS), followed by Turin's rebuttal.
- **Label:** fringe or minority view, recorded for history. In the sources the field treats it as unsupported for mammals, because receptor-level tests were negative [unverified]. The WP pages on this theory and on Turin were blocked.
- **Standing 2026:** largely rejected but not formally closed [unverified].
- **What would settle it:** receptor-level isotope discrimination reproduced across laboratories, with steric confounds controlled.

### Gaps (quantum biology)
- No source for F21–F24 was opened in this session apart from the uncited WP Photosynthesis sentence. Every citation above needs checking.

## 6. Origin of the genetic code (beyond project entry 149)

### Takeaway
Entry 149 holds the three accounts and the frozen accident (Koonin & Novozhilov 2009). Added: verified numbers and a split into proper binaries, since the accounts are not exclusive.

### Frontier binaries

#### F25 · Code origin, split into proper binaries [explaining]
- **Scope note:** four accounts that are not exclusive, so each is posed against its own negation.
  - **F25a (observing-based):** do specific amino acids show selective affinity for RNA sequences containing their own codons or anticodons, beyond chance? Aptamer selections found codon or anticodon associations for 6 of 8 amino acids tested (Yarus 2009/2010, via [WP: Genetic code](https://en.wikipedia.org/wiki/Genetic_code)) [obs]. Statistical treatment is contested (entry 149). Standing: open.
  - **F25b (explaining):** was the code's error robustness a product of selection, or a by-product of an origin fixed for other reasons? Holding block structure fixed, the natural assignment is about "one in a million" in robustness (Freeland 1998, via WP) [obs + model]. Selection vs by-product is not separable by structure (entry 149). Standing: open.
  - **F25c (explaining):** does the block structure record biosynthetic coevolution? Amino acids with similar properties or shared biosynthesis sit at related codons (Wong 1980; Taylor 1989, via WP) [recon]. Standing: open.
  - **F25d (observing):** is the code frozen? Crick's frozen accident ([1968](https://doi.org/10.1016/0022-2836(68)90392-6)) predicted near-universality. Variant codes exist, the first found in human mitochondria in 1979 ([Barrell 1979](https://doi.org/10.1038/282189a0)) [obs]. Natural and engineered reassignments show the code is not frozen absolutely (entry 149). Standing: settled as "not absolutely frozen".
- **Further observings:**
  - First-position codon changes matter more globally than second-position changes, and charge reversal is possible only via the first position ([Fricke 2019](https://doi.org/10.1093/bioinformatics/bty678)) [recon].
  - A proposed order of amino acid recruitment for LUCA (Wehbi et al. 2024: Val, Gly, Ile, Met, Ala, …) [recon; DOI not seen].
- **Why hard:** a single historical event, and the present structure fits several origins.
- **What would settle it:** a feature one account predicts and others do not (entry 149's own persistence condition). An example would be affinity patterns predicting the codons of late-added amino acids, or ancestral reconstructions with independent chemical support.
- **Proponents:** Yarus (stereochemical); Wong (coevolution); Freeland, Hurst, Koonin (error minimisation with frozen accident); Crick (prior) [unverified as positions beyond WP].

## Further candidates (one line each)

- Chemical evolution in the laboratory: has any non-biological replicator shown open-ended evolution? Observing; open (Otto-type fibre replicators, [Jin 2024](https://doi.org/10.1021/jacs.4c09114)).
- Amino acids in the Miller–Urey framework: was the Hadean atmosphere reducing enough? Explaining; leaning weakly reducing, with impact-generated H₂ as an exception ([Johnson 2008](https://doi.org/10.1126/science.1161527); [Cleaves 2008](https://doi.org/10.1007/s11084-007-9120-3), via [WP: Miller–Urey](https://en.wikipedia.org/wiki/Miller%E2%80%93Urey_experiment)).
- Earliest life traces (Nuvvuagittuq, 4.32 Ga claim): observing, disputed (via WP: Abiogenesis).
- Did a pre-RNA genetic polymer (TNA, PNA, GNA) precede RNA? Explaining; plausible prebiotic syntheses undemonstrated (via WP: RNA world).
- Is Levinthal's search solved by funnelled landscapes, or only made consistent? Explaining; see project entry 33.
- Are amyloid fibril polymorphs disease-specific strains? Observing; cryo-EM supports disease-specific folds ([Fitzpatrick 2017](https://doi.org/10.1038/nature23002)); the generalisation is open.
- Functional amyloids vs pathological amyloids: same cross-β fold, different control? Explaining (via WP: Amyloid).
- Enzyme catalysis: do protein dynamics drive the chemical step (promoting vibrations, tunnelling), or only sample conformations? Explaining; contested [unverified].
- Mirror-image life: could L-sugar, D-protein biochemistry work equally well? Model and laboratory; partial mirror enzymes made [unverified].

## Method notes for the report writer
- DOIs and URLs marked "via WP" were seen this session on Wikipedia pages, or in the project's carryings and incoming report; the primary papers were not opened. [unverified] items come from background knowledge.
- Fetches of nature.com, science.org, pnas.org, PMC and doi.org were refused, so "Standing 2026" reflects the newest item seen, mostly 2023–2025.
- Conflict kept: WP's Homochirality page calls Murchison's amino acids racemic; WP's Murchison page reports L-excesses (Cronin & Pizzarello 1997).
- Project cross-references: TWENTY-ONE entries 12, 33, 63, 149, 177, 178, 208; SIXTEEN carryings (Kondepudi 1990, Viedma 2005, Hazen 2001); ELEVEN carryings (lecanemab, amyloid); SEVENTEEN carryings (kuru, PrP V127).

