# Rules, principles and empirical regularities of chemical structure and bonding: a clustered catalogue

Compiled 23 October 2026. The search budget ran out partway through, and the fetch allowlist blocked several Wikipedia pages (VSEPR, Bent, Walsh, Zintl, isolobal, Slater, Koopmans, Fajans, Badger, Hume-Rothery, Pauling's rules, Hückel, Möbius, Bredt, Goldschmidt). Entries for those rules rely on the primary papers I did see. Anything I did not open in this session is marked [unverified].

Label legend, applied to each item:
- OBS: an observing (method, sample, conditions, quantity).
- RECON: a reconstruction from observings (a generalization, a fitted quantity, or a statistic over many measurements).
- CONV: a convention or definition.
- MODEL: a model construct (an interpretive entity or theory).
- SIM: a simulation (a computed number).

## Key gathered points

- Most rules here generalize from a skewed calibration set (light main-group atoms, closed-shell ground states, isolable compounds), with a model rationale added later. The regularity often outlives its rationale: Wade's n+1 count still fits tubular boranes although its textbook orbital derivation was judged misleading (Balakrishnarajan et al. 2003).
- Database-scale tests:
  - Pauling's rules: only 13% of ~5,000 oxides satisfy rules 2–5 together; the electrostatic valence rule fails most; rule 1 fits 66% of environments (George et al. 2020; reply, Gibbs et al. 2022).
  - Perovskites: Goldschmidt t is 74% accurate on 576 ABX3 compounds (33% for iodides); Bartel's τ is 92% (2019).
  - Alloys: Hume-Rothery size criteria are necessary but not sufficient; machine learning reaches ~93%.
- The 2022–2025 "breaks" move a rule's boundary rather than abolish it: anti-Bredt olefins generated and trapped (Garg, Science 2024); a 20-electron ferrocene (Takebayashi, Nat. Commun. 2025); an inverted singlet–triplet gap of −11 meV (Aizawa, Nature 2022), disputed in 2023 and supported by high-level theory in 2023–2025.
- Ca/Sr/Ba(CO)8: the data are agreed (one IR band each, neon matrix, 4 K); the reading is not. 18-electron d-backbonding (Wu and Frenking 2018) against ionic Ca2+[(CO)8]2− (Landis, Hughes, Weinhold 2019). Still open.
- Hypervalence: the d-orbital model was rejected in 1986–90; the term is still disputed (Durrant 2015; Harcourt and Klapötke 2016).
- HSAB: the global principle survives; local (ambident) use is judged to fail (Mayr 2011; Sheehy et al. 2020).
- Hund's first rule: observations stand, explanation reversed. High spin is lower because electron–nucleus attraction is stronger, while electron–electron repulsion rises (Katriel 1972; Hongo et al. 2004, quantum Monte Carlo).
- Aromaticity has no agreed definition (Merino et al. 2023) and its criteria can disagree; Clar's rule was the only test every index passed for benzenoids (Solà 2013).
- VSEPR and Walsh predict linear MX2, yet BaF2, SrF2 and BaH2 are bent; the explanation (core polarization plus (n−1)d participation; Kaupp 1991–93) has the same second-order form as pseudo-Jahn–Teller arguments.
- Pauli is the outlier: a postulate with experimental bounds, not an empirical rule.
- Shared feature of exceptions: they lie outside the calibration domain (heavy atoms, excited or open-shell states, transient species), at near-degeneracy (small gaps), or under counting conventions that can be redrawn.

## 1. Electron-counting rules (octet/duet, 18-electron and Tolman, Wade–Mingos, jellium/superatoms, Zintl–Klemm, Grimm–Sommerfeld, isolobal)

### Takeaway
Each counting rule says that a closed set of bonding and non-bonding levels holds a fixed number of electrons. Each works where a large gap separates filled from empty levels. Each fails, or turns into bookkeeping, where the ionic/covalent split, the ligand field or the cluster shape blurs that gap. The boundary cases of 2018–2025 (M(CO)8, 20-electron ferrocene, hypoelectronic osmaboranes, flat carboranes) contest where a rule applies, not what was measured.

### Cited Findings

#### Octet and duet rules
- **Organizes:** valence, stoichiometry and Lewis structures of s- and p-block compounds (especially C, N, O and the halogens) — [Octet rule, Wikipedia](https://en.wikipedia.org/wiki/Octet_rule).
- **Statement:** main-group atoms tend to bond until each has eight valence electrons, with shared pairs counted for both atoms. H and He, and Li in its first shell, follow a two-electron "duet" — same source.
- **History:**
  - Abegg (1904) noticed that an element's maximum positive and negative valences often differ by eight (doi:10.1002/zaac.19040390125).
  - Kossel and Lewis (1916) argued from the stability of the noble gases (doi:10.1002/andp.19163540302; doi:10.1021/ja02261a002).
  - Langmuir (1919) set out the "octet theory" (doi:10.1021/ja02227a002) — same source.
- **Empirical or derived:** both. It began as a generalization from valence patterns and noble-gas inertness, and was later rationalized as filling the s2p6 shell.
- **Exceptions:**
  - electron-deficient BCl3 and the boranes ("sextet");
  - radicals such as CH3• and ClO•;
  - "hypervalent" PF5 and SF6 (ab initio work finds that nearly all known cases satisfy the octet through resonance);
  - transition metals (12–18 electrons) — same source.
- **Labels:** noble-gas inertness = OBS (reactivity); "eight" = RECON; the s2p6 closed shell = MODEL; assigning shared electrons = CONV.
- **Standing in 2026:** a textbook guideline. The live disputes are about how to count (see hypervalence below and in §5).

#### 18-electron rule (Langmuir; Sidgwick's effective atomic number) and Tolman's 16/18-electron rule
- **Organizes:** stoichiometry, stability and reactivity of transition-metal complexes, especially carbonyls and other organometallics.
- **Statement:** a d-block metal's nine valence orbitals (five (n−1)d, one ns, three np) can hold 18 electrons as bonding or non-bonding pairs, and 18-electron complexes are noble-gas-like and stable. Langmuir proposed it first in 1921 (doi:10.1126/science.54.1386.59) — [18-electron rule, Wikipedia](https://en.wikipedia.org/wiki/18-electron_rule). Its history is reviewed in Jensen 2005 (doi:10.1021/ed082p28). Sidgwick's effective-atomic-number wording (1920s) is [unverified].
- **Tolman (1972):** Chem. Soc. Rev. 1, 337 (doi:10.1039/CS9720100337) — cited on the same page. The page notes that many catalytic cycles alternate between 18-electron and square-planar 16-electron complexes. The exact wording of Tolman's rule (elementary steps change the count by two; only 16- and 18-electron intermediates) is [unverified].
- **Empirical or derived:** a generalization from carbonyl stoichiometries, with a nine-orbital MO rationale.
- **Exception classes (from the page):**
  - low-spin square-planar d8 complexes at 16 electrons (Vaska's complex, [PtCl4]2−, Zeise's salt);
  - bulky ligands: Ti(neopentyl)4 (8e), Cp*2Ti(C2H4) (16e), V(CO)6 (17e), Pt(PtBu3)2 (14e), Co(norbornyl)4 (13e);
  - weak-field or π-donor ligands: [TiF6]2− (12e), TiCl4 (8e), [CrO4]2− (16e), Mo(=NR)2Cl2 (12e);
  - high-spin complexes;
  - more than 18 electrons: cobaltocene (19e), nickelocene (20e), [Cu(H2O)6]2+ (21e), [M(CO)8]− with M = Sc or Y (20e). The extra electrons sit in metal–ligand antibonding orbitals.
- **Labels:** composition, X-ray structure and magnetism = OBS; the electron count = CONV (it depends on the formalism chosen, ionic or covalent); the stability rationale = MODEL.
- **Standing in 2026:** reliable for low-valent complexes with π-acceptor ligands; taught as a rule of thumb.

#### 2025 test: 20-electron ferrocene derivatives
- **Source:** Takebayashi, Ariai, Kartashov, Fayzullin, Onoue, Mibu, Kang, Ishizu, "From 18- to 20-electron ferrocene derivatives via ligand coordination", Nat. Commun., 7 July 2025, doi:10.1038/s41467-025-61343-7 — [OIST release](https://www.oist.jp/node/46139).
- **Observed (as reported):**
  - a pyridine built into the ferrocene binds Fe through its nitrogen, reversibly, which raises the count to 20;
  - para-OMe and para-amine substituents strengthen the N donor and favour the Fe–N bond;
  - the compounds interconvert reversibly among Fe(II), Fe(III) and Fe(IV), and undergo a two-electron oxidation to a dication under mild conditions — [Chemistry World](https://www.chemistryworld.com/news/organometallic-compound-found-to-break-textbook-principle/4021839.article).
  - Bond distances and other crystallographic data were not checked [unverified].
- **Interpreted:** calculations indicate weaker Fe–Cp covalent bonding and partial occupation of high-lying antibonding orbitals — same source.
- **Reception:** an outside chemist (D. Mills) described it as an instructive exception that shows why the rule usually works. The authors call the rule a rule of thumb (OIST).
- **Labels:** redox behaviour and structure = OBS; "20 electrons" = CONV (the count includes the N donor); orbital occupation = SIM.
- **Standing:** reported in 2025; I found no independent replication.

#### "18-electron" main-group carbonyls M(CO)8 (M = Ca, Sr, Ba): open since 2018
- **Observed:** Wu, Zhao, Jin, Pan, Li, Jin, Wang, Zhou, Frenking, Science 361, 912 (2018), doi:10.1126/science.aau0839 — [paper PDF](https://www.cup.lmu.de/ac/kluefers/homepage/L/kc2/literature/pse2-m8co-2018.pdf); [Wikipedia](https://en.wikipedia.org/wiki/Alkaline_earth_octacarbonyl_complex).
  - Laser-ablated metal atoms were co-deposited with 0.02–2% CO in solid neon at 4 K and annealed at 10–13 K.
  - FTIR shows a single C–O stretch for each metal: Ca 1987, Sr 1995, Ba 2014 cm−1 (free CO absorbs at 2143 cm−1). Isotope mixtures were used; the splittings were resolved for Ca only.
  - Cations were studied in the gas phase by mass-selected IR photodissociation; coordination saturates at n = 8.
- **Interpreted (SIM and MODEL, not observed):** an Oh triplet (3A1g) ground state, backdonation from metal (n−1)d orbitals into CO π* (from an EDA-NOCV analysis), and an 18-electron count. The single band is only consistent with cubic symmetry.
- **Counter-reading:** Landis, Hughes, Weinhold, Science 365, eaay2355 (2019), doi:10.1126/science.aay2355 — [comment PDF](https://www.cup.lmu.de/ac/kluefers/homepage/L/kc2/literature/pse2-m8co-comment-2019.pdf).
  - The QTAIM charge on Ca is about +1.56.
  - The ~0.4 e "Ca d" occupancy in the NBO analysis is a basis-set artifact: the d function persists even when the Ca nucleus is removed.
  - The bonding is weak by transition-metal standards: Ca–C is 2.6 Å and the first CO dissociation costs 9 kcal/mol, against 1.91 Å and 37 kcal/mol for Cr(CO)6.
  - More than 90% of the triplet spin density sits on the CO ligands.
  - The apparent backbonding comes from choosing a Ca d2 reference state about 150 kcal/mol above the ground state.
- **Further exchange:** Van der Maelen (2020) found the bonding mainly electrostatic (doi:10.1021/acs.organomet.9b00699). A comment and reply followed (doi:10.1021/acs.organomet.0c00419; doi:10.1021/acs.organomet.0c00523). The Wikipedia page treats the question as unresolved.
- **Third reading:** [M(CO)8]2− has also been analysed as a jellium superatom with the magic number 20 (Wikipedia page), so two different counting rules claim the same object.
- **Standing in 2026:** the data are uncontested; the interpretation is open. I found no resolution from 2023–2026.

#### Wade–Mingos rules (polyhedral skeletal electron pair theory, PSEPT)
- **Organizes:** the shapes of boranes, carboranes, metallaboranes and transition-metal clusters, read from their electron counts.
- **Statement:** a cluster with n vertices and n+1 skeletal electron pairs (SEP) is closo. With n+2 it is nido, with n+3 arachno, with n+4 hypho. Examples: [B6H6]2− (closo), B5H9 (nido) and B4H10 (arachno) all have 7 SEP. The rules were built for boranes and carried over to metal clusters through the isolobal analogy. Organometallic chemists often use them alongside total cluster valence electron counts — Prakash, Halet, Ghosh, Molecules 25, 3179 (2020), doi:10.3390/molecules25143179 ([MDPI](https://www.mdpi.com/1420-3049/25/14/3179)). The original papers (Wade 1971; Mingos 1972) were not opened [unverified].
- **Empirical or derived:** empirical first, then given an MO rationale. That rationale has been questioned while the count still holds. Balakrishnarajan, Hoffmann, Pancharatna and Jemmis (Inorg. Chem. 42, 4650, 2003) found that n+1 still holds for tubular B17H17^2−, B22H22^2− and B27H27^2−. They also judged the textbook derivation (one radial plus n tangential bonding MOs) misleading even for B10H10^2− and B12H12^2−, while keeping the rule as useful — [PDF](https://old.roaldhoffmann.com/sites/all/files/489s_0.pdf). The DOI was not shown [unverified].
- **Exceptions:**
  - isocloso/hypocloso clusters with n SEP;
  - oblatocloso clusters with n−3 SEP, flattened and with metal–metal bonds across the cluster;
  - M2B5 "rule breakers": oblatonido type I species have 6 SEP where 9 are predicted;
  - King's non-Wadean rule for oblatoarachno clusters (n SEP).
  The review states that the rules are not universal and do not describe extensively delocalized 3D systems (Prakash et al. 2020).
- **2024 test:** Kar, Kar and Ghosh, Chem. Sci. 2024, doi:10.1039/d3sc06464f ([RSC](https://pubs.rsc.org/en/content/articlehtml/2024/sc/d3sc06464f)).
  - OBS: X-ray structures of [(Cp*Os)2BnHn] (n = 6–10); Os1–Os2 = 2.7688(3) Å in cluster 1; 11B/1H/13C NMR, IR, MS and UV-vis.
  - SIM: BP86/def2-SVP; Os···Os Wiberg indices 0.351–0.836.
  - CONV: the SEP counts come from the counting scheme. These clusters have n−1 SEP, two fewer than closo requires, and the authors say they do not follow Wade–Mingos.
- **2020 test:** Lu, Do and Kinjo, Nat. Commun. 11 (2020), doi:10.1038/s41467-020-17166-9 ([DOAJ](https://doaj.org/article/3d2dad4fdf8d47a2a30e33b48da288b1)). They report planar C2B4R4 carboranes that do not follow PSEPT and assign them multiple aromaticity.
- **Standing in 2026:** the working rule for clusters. Metal-rich and planar exceptions are a growing class, labelled with new prefixes (isocloso, oblato-) rather than treated as refutations.

#### Jellium shell model and superatom magic numbers
- **Organizes:** which sizes of metal cluster are abundant or stable, and the "element-like" chemistry of clusters.
- **OBS:** ionized gas-phase sodium clusters show abundance maxima at particular sizes (Knight et al., Phys. Rev. Lett. 52, 2141, 1984) — [Zeiger seminar abstract, UIUC](https://chemistry.illinois.edu/system/files/inline-files/Brad_Zeiger_Lit_Seminar_Abstract.pdf).
- **MODEL:** the nuclear charge is smeared into a uniform sphere, so the valence electrons fill spherical shells. The closed-shell counts listed are 2, 8, 18, 20, 34 and 40. The source notes that they depend slightly on the shape of the potential — same source. Another page lists the sodium magic sizes as 2, 8, 20, 40, 58 and 92 ([wikidoc](https://wikidoc.org/index.php/Superatom)). The two lists differ because the sequence depends on the potential.
- **Examples:**
  - Al13 has 39 valence electrons, one short of 40. Its reported electron affinity of 3.6 eV is close to chlorine's, so it is called a "superhalogen" (Zeiger).
  - In Al14I3−, three iodines each withdraw one electron, leaving 40 in the jellium shell, so Al14 behaves like an alkaline earth. Sources: Bergeron et al., Science 304, 84 (2004) and 307, 231 (2005) (wikidoc; DOIs not shown).
- **Limits:**
  - the model suits weakly bound valence electrons; non-spherical or doped clusters deviate (wikidoc; Zeiger);
  - the clusters are metastable toward coalescing into bulk metal, and KAl13 has never been isolated as a pure solid (Zeiger);
  - P. Ball cautions that the superatom analogies are partly speculative and that filled-shell comparisons need real electronic-structure analysis — [Chemistry World](https://chemistryworld.com/opinion/superatom-musings/3005065.article).
- **Labels:** abundance spectra = OBS; the magic numbers = RECON; jellium = MODEL; "superatom" = an analogy (MODEL or CONV).
- **Standing:** established for alkali and aluminium clusters. No 2023–2026 updates were checked.

#### Zintl–Klemm concept and Grimm–Sommerfeld rule
- **Zintl–Klemm:** the electropositive partner gives its valence electrons fully to the electronegative partner. The resulting polyanion then builds bonds like the isoelectronic element (a "pseudo-element", obeying the 8−N rule). The textbook case is the diamond-like Tl− network in NaTl. The concept is dated to Zintl in the 1930s and Klemm in the 1950s [unverified; the Wikipedia page was blocked by the allowlist]. Deltahedral Zintl ions such as Sn9^4− are counted by Wade's rules [unverified].
- **Grimm–Sommerfeld (1926):** AB compounds averaging four valence electrons per atom (III–V, II–VI) take tetrahedral, diamond-like structures [unverified; no source opened].
- **Labels:** both are CONV counting schemes applied to RECON structure data.
- **Standing:** both are used in solid-state chemistry, but none of the 2023–2026 literature on them was checked.

#### Isolobal analogy (Hoffmann)
- **Statement:** two fragments are isolobal when their frontier orbitals match in number, symmetry, approximate energy and shape, and hold the same number of electrons. Standard pairs are CH3/Mn(CO)5, CH2/Fe(CO)4 and CH/Co(CO)3. Through these pairs the octet rule and the 18-electron rule map onto each other. Source: Hoffmann's Nobel lecture, 1982 [unverified; Wikipedia page blocked].
- **Seen in this session:**
  - the analogy is the bridge that carried Wade's rules over to transition-metal clusters (Prakash et al. 2020);
  - Hoffmann et al. (2003) propose replacing B–H vertices with isolobal +SiH or Fe(Cp) to help stabilize tubular boranes.
- **Labels:** MODEL (a frontier-orbital correspondence). It is a heuristic for organizing structures, not a law.

### Inferences
- The counting rules share one template: twice the number of low-lying bonding plus non-bonding levels gives a closed count. That is 4 levels for s+p (8), 9 for s+p+d (18), n+1 for a deltahedral skeleton, and the spherical shells for jellium. Each rule works when a large gap separates the occupied levels from the next ones, and blurs as that gap shrinks: weak-field ligands, bulky ligands, metal-rich clusters, planar clusters.
- Every count depends on a partitioning convention: an ionic or covalent formalism, whether a donor's pair counts, and which reference state is used. M(CO)8 shows the consequence. Ca(0) + 8 CO gives 18 electrons, Ca2+ + [(CO)8]2− gives an ionic complex, and a third reading treats [M(CO)8]2− as a 20-electron superatom, all from the same IR band. So "is an 18-electron complex" is a membership criterion that has to name its counting convention.
- In the 2020s, exceptions are usually handled by renaming (isocloso, oblatonido, "increased-valence") rather than by retiring the rule.

### Gaps
- I did not open the primary sources for Zintl–Klemm, Grimm–Sommerfeld, the isolobal analogy, Sidgwick's effective atomic number or Tolman's 1972 wording. The allowlist blocked the Wikipedia pages, and the search budget ran out.
- I did not see crystallographic metrics (the Fe–N distance) for the 20-electron ferrocene.
- I found no 2023–2026 paper settling the M(CO)8 bonding question.

## 2. Aromaticity and ring rules (Hückel, Baird, Möbius, Clar, Glidewell–Lloyd, spherical, Bredt, Baldwin)

### Takeaway
The aromaticity rules are electron-count selection rules: 4n+2 or 4n, chosen by topology and by spin state. They are layered on a concept that has no agreed definition or single observable. Clar's rule is the best-corroborated rule for polycyclics. Ring-strain and ring-closure rules (Bredt, Baldwin) are kinetic or thermodynamic guidelines that were redrawn in 2011 and again in 2024.

### Cited Findings

#### The aromaticity concept and its criteria
- **CONV/MODEL:** a 2023 perspective by 13 leading authors says there is no consensus on what aromaticity is. It notes the multiplying qualifiers (σ, π, δ, spherical, Möbius, all-metal) and asks whether the concept is "a dubious concept". Merino, Solà, Fernández, Foroutan-Nejad, Lazzeretti, Frenking, Anderson, Sundholm, Cossío, Petrukhina, Wu, Wu, Restrepo, Chem. Sci. 14, 5569–5576 (2023), doi:10.1039/D2SC04998H — [ORA Oxford record](https://ora.ox.ac.uk/objects/uuid:e2553e49-db81-477c-b358-098be9c9cf53); [ICM record](https://open.icm.edu.pl/items/19e2f1fc-6ba3-430a-8c8b-208f2f376df4). I saw only the abstract; the full text was not accessible.
- **Criteria in use** ([Aromaticity, Wikipedia](https://en.wikipedia.org/wiki/Aromaticity)):
  - energetic: resonance energy and aromatic stabilization energy;
  - geometric: bond-length equalization, HOMA;
  - magnetic: ring-current shifts in 1H NMR (OBS), magnetic-susceptibility exaltation (OBS), and NICS (SIM, a computed shielding at a ghost point);
  - electronic: delocalization indices (SIM).
  Global and local measures can differ; in phenanthrene the central ring is less aromatic and more reactive than the outer rings (same page).
- **Labels:** NMR shifts, bond lengths and heats of hydrogenation are OBS. "Aromaticity" itself is a MODEL construct that sits on top of several observable and computed proxies. NICS and the delocalization indices are SIM.

#### Hückel 4n+2 rule
- **Statement:** planar, monocyclic, fully conjugated rings with 4n+2 π electrons are aromatic, and those with 4n are antiaromatic. Hückel, 1931. The rule is strictly valid only for monocycles — Solà, Front. Chem. 1, 22 (2013), doi:10.3389/fchem.2013.00022 ([Frontiers](https://www.frontiersin.org/articles/10.3389/fchem.2013.00022/full)).
- **Empirical or derived:** derived from Hückel MO theory (closed-shell π levels), and consistent with benzene, the cyclopentadienyl anion, the tropylium cation, the cyclopropenyl cation and the cyclooctatetraene dianion (Wikipedia, Aromaticity).
- **Limits:** polycyclic systems; pyrene (16π) and coronene (24π) are aromatic despite counts that break the rule [unverified for these examples; the Hückel page was blocked].
- **Standing:** foundational, with a clearly bounded domain.

#### Baird's rule: excited-state (anti)aromaticity
- **Statement:** in the lowest ππ* triplet state the count reverses, so 4n annulenes are aromatic and 4n+2 antiaromatic. Baird derived this in 1972 by perturbational MO theory. Computations extend it to S1 — Papadakis and Ottosson, "The excited state antiaromatic benzene ring: a molecular Mr Hyde?", Chem. Soc. Rev. 44, 6472–6493 (2015), doi:10.1039/C5CS00057B ([author PDF](https://pubs.rsc.org/en/content/getauthorversionpdf/C5CS00057B)).
- **Evidence (SIM):**
  - Hückel resonance energy of benzene goes from +0.273β (S0) to −0.692β (T1);
  - CASSCF NICS values for T1 and S1 are large and positive;
  - HOMA for the T1 antiquinoid structure is −0.545.
- **Evidence (OBS):**
  - S1 benzene is D6h with C–C bonds of 1.432–1.435 Å;
  - benzene's photoproducts (benzvalene, fulvene) form with low quantum yields;
  - fluorescence yield drops above the "channel 3" onset.
- **Limits stated in the review:** experimental support is largely indirect (reactivity read as relief of antiaromaticity); the CASSCF calculations lack dynamic correlation; and HOMA is parameterized on ground-state (S0) geometries.
- **Standing in 2026:** widely accepted as a design principle in photochemistry. The direct observational basis is still thin.

#### Möbius aromaticity
- **Statement:** a ring with one half-twist reverses the Hückel count, making 4n aromatic. Heilbronner, 1964 [unverified; page blocked]. The synthesis of a "Möbius aromatic hydrocarbon" was reported by Ajami et al., Nature (2003), doi:10.1038/nature02224. Its aromaticity was later contested (Castro et al. 2005, doi:10.1021/ja0458165; Rzepa 2005, doi:10.1021/ol0518333). As of its 2012 text, the Wikipedia page says no Möbius aromatic molecule had been proven synthesized — [Aromaticity, Wikipedia](https://en.wikipedia.org/wiki/Aromaticity).
- **OBS, 2022:** a Möbius carbon nanobelt, (25,25)MCNB, was made in 14 steps and its topological chirality confirmed by chiral HPLC and CD spectroscopy. NMR and calculations show the twist moves rapidly around the ring. The paper makes no aromaticity claim. Segawa, Watanabe, Yamanoue, Kuwayama, Watanabe, Itami, Nat. Synth. (2022), doi:10.1038/s44160-022-00075-8 — [Segawa lab](https://segawa.ims.ac.jp/?p=1677).
- **Standing:** the topology itself is now realized in all-carbon molecules. Whether the 4n Möbius count produces measurable aromaticity in neutral hydrocarbons remains disputed.

#### Clar's π-sextet rule
- **Statement:** among the Kekulé structures of a benzenoid polycyclic hydrocarbon, the most important is the one with the largest number of disjoint aromatic π-sextets. Rings are classed as sextet, migrating-sextet, empty or double-bond rings — Solà 2013 (above).
- **Empirical or derived:** empirical (Clar, 1972). Valence-bond calculations later confirmed that structures with the most sextets dominate (Havenith et al. 2001, cited by Solà).
- **OBS support (Solà):**
  - in phenanthrene, the bonds assigned as double and single in the Clar structure are the shortest and longest C–C bonds;
  - AFM of hexabenzocoronene and STM show bond-order differences that match Clar's assignments;
  - phenanthrene is about 5 kcal/mol more stable than anthracene;
  - λmax shifts from 840 to 326 nm as sextets are added along a heptacatafusene series;
  - the inner protons of kekulene appear above δ 7 ppm;
  - fully benzenoid hydrocarbons have HOMO–LUMO gaps above 2.1 eV.
- **SIM support:** in Feixas et al. (2008), PDI, FLU, MCI, I_ring, HOMA and several NICS variants all ranked the sextet rings as most aromatic. Solà calls this the only test that every index passed.
- **Limits:**
  - the rule is qualitative;
  - it covers only benzenoids;
  - anthracene has a migrating sextet, so the rule does not single out its most aromatic ring;
  - large benzenoids can have many Clar structures.
  The open-shell (diradical) ground states of acenes from n ≥ 6 are explained within the rule, because the open-shell form gains a sextet.
- **Standing in 2026:** the most robust local-aromaticity rule for benzenoids. No 2023–2026 update was checked.

#### Glidewell–Lloyd rule
- **Statement and status:** Glidewell and Lloyd (1984) extended Clar's rule to non-benzenoid polycyclic conjugated hydrocarbons (Solà 2013). The usual statement: the π electrons are shared so as to form the most 4n+2 groups in the smallest rings and to avoid 4n groups [unverified wording]. The search budget ran out before I could check 2023–2026 tests.

#### Spherical aromaticity, the 2(n+1)² rule
- Hirsch and co-workers (2000) proposed that spherical π systems with 2(n+1)² electrons (2, 8, 18, 32, 50…) are aromatic, by analogy with closed angular-momentum shells [unverified; no source opened]. Merino et al. (2023) list "spherical" among the qualifiers of aromaticity.
- The jellium shell counts (§1) are a related shell-closure sequence. That link is my inference, not a sourced claim.

#### Bredt's rule and the 2024 anti-Bredt olefins
- **Statement:** small bridged bicyclic molecules cannot carry a C=C double bond at a bridgehead, because the double bond would have to be trans within a small ring, which misaligns the p orbitals. Bredt, 1924 — [Oxford Scientist](https://oxsci.org/breaking-bredts-rule-a-century-later/); [UCLA](https://www.chemistry.ucla.edu/news/organic-chemists-take-on-bredts-rule-100-years-later/). The Fawcett S-number and Wiseman (1967) refinements, and earlier isolable anti-Bredt alkenes in larger bicycles, are [unverified].
- **OBS, 2024:** McDermott, Walters, French, Clark, Ding, Kelleghan, Houk, Garg, "A solution to the anti-Bredt olefin synthesis problem", Science 386, eadq3519 (2024), doi:10.1126/science.adq3519 — [Spectroscopy Online](https://www.spectroscopyonline.com/view/scientists-break-century-old-barrier-to-synthesizing-anti-bredt-olefins).
  - Anti-Bredt olefins were generated from silyl (pseudo)halide precursors with fluoride (Bu4NF, or CsF/Bu4NBr) in [3.2.1], [2.2.2] and [2.2.1] bicycles.
  - They were trapped by (4+2), (2+2), (3+2) and (5+2) cycloadditions, including with anthracene.
  - Chirality carried over from enantioenriched precursors into the products ([2.2.2] system), consistent with an axially chiral intermediate.
- **SIM:** DFT shows the alkenes are twisted and pyramidalized (same source).
- **RECON:** the olefins were never isolated. Their existence is inferred from the trapped products and the stereochemical transfer.
- **Framing:** Garg says such rules should be treated as guidelines, not rules (UCLA).
- **Standing in 2026:** a thermodynamic and kinetic guideline whose boundary has moved. It still holds for isolable compounds.

#### Baldwin's ring-closure rules
- **Statement:** a closure is named by ring size, by exo or endo, and by the geometry of the attacked atom (tet, trig, dig). Favoured cases follow from the orbital-overlap geometry of the approach: about 180° for exo-tet, about 109° (Bürgi–Dunitz) for exo-trig. Baldwin, J. Chem. Soc. Chem. Commun. 1976, 734, doi:10.1039/C39760000734 — [Baldwin's rules, Wikipedia](https://en.wikipedia.org/wiki/Baldwin%27s_rules).
- **Empirical or derived:** both. Collected from observed closures and rationalized stereoelectronically.
- **Limits:**
  - "disfavoured" is relative, not forbidden;
  - the rules assume second-row atoms, so S and other heavier atoms allow 5-endo-trig and 3-exo-dig;
  - cationic cyclizations often disobey them;
  - they also apply to radical closures (same page).
- **Revision of the dig rules (2011–2016):** the obtuse attack trajectory is preferred. Small rings therefore favour exo-dig, and endo-dig is disfavoured, contrary to Baldwin's original alkyne assignments — [Alabugin group page](https://chem.fsu.edu/~alabugin/newrulesalkynes.html). Sources:
  - Gilmore and Alabugin, Chem. Rev. 111, 6513 (2011), doi:10.1021/cr200164y;
  - Alabugin, Gilmore and Manoharan, JACS 133, 12608 (2011), doi:10.1021/ja203191f;
  - Gilmore, Mohamed and Alabugin, WIREs Comput. Mol. Sci. 6, 487 (2016), doi:10.1002/wcms.1261.
- **Standing in 2026:** the tet and trig rules are in use. The dig rules are superseded by the Alabugin revision.

### Inferences
- Hückel, Baird and Möbius form one family of selection rules. The topology of orbital overlap (normal or twisted) and the spin state (singlet ground state or triplet) each flip the preferred count between 4n+2 and 4n. Clar and Glidewell–Lloyd make the count local by partitioning electrons into rings. Spherical counting changes the shell symmetry from a ring to a sphere.
- "Aromatic" is not one set with a single membership criterion. Each criterion (energetic, magnetic, geometric, electronic) defines its own candidate set, and the sets overlap without coinciding. The 2023 perspective's question about whether this makes the concept dubious says the same thing at the field level.
- Bredt and Baldwin are sequencing rules: they say which pathway is fast and which product survives. The 2024 trapping experiments did not show that anti-Bredt olefins are stable, only that they can be formed. Under that reading the rule is unbroken.

### Gaps
- I did not open sources for the Hirsch 2(n+1)² rule, for the precise Glidewell–Lloyd wording, or for 2023–2026 tests of either.
- The full text of the 2023 "Quo vadis" perspective was not accessible, so its detailed treatment of the criteria was not checked.
- I did not check post-2022 claims of Möbius aromaticity in nanobelts or expanded porphyrins, or Fawcett and Wiseman's quantitative Bredt criteria.

## 3. Geometry and packing rules (VSEPR, Bent, Walsh, Jahn–Teller/pseudo-JT, radius ratio, Pauling's five rules, tolerance factors, Hume-Rothery, Kitaigorodsky, Etter)

### Takeaway
Local geometry rules (VSEPR, Walsh) are reliable for light main-group molecules. They fail in a structured way for heavy, polarizable, formally d0 centres, where second-order mixing (core polarization, (n−1)d participation, pseudo-Jahn–Teller coupling) takes over. Crystal-packing rules have now been tested at database scale: Pauling's rules hold poorly (13% joint), the Goldschmidt factor reaches 74%, and Hume-Rothery-type criteria are necessary but not sufficient. Fitted descriptors and machine learning do better but explain less.

### Cited Findings

#### VSEPR, and Walsh as its MO counterpart
- **Statement:** electron pairs, bonding and lone, around a central atom arrange to minimize mutual repulsion, which sets the geometry (Sidgwick–Powell 1940; Gillespie–Nyholm 1957) [unverified history; VSEPR page blocked]. Walsh diagrams track how orbital energies change with bond angle; for AB2, a 16-valence-electron count predicts linear [unverified wording; Walsh page blocked].
- **Seen in this session:** Kaupp, Schleyer, Stoll and Preuss state that VSEPR, Walsh diagrams, and simple ionic, MO and valence-bond models all predict linear 16-electron MX2 triatomics. Kaupp et al., JACS 113, 6012–6020 (1991) — [PDF](https://opus.bibliothek.uni-wuerzburg.de/files/5581/Kaupp24.pdf). The DOI was not shown in the text [unverified].
- **OBS (exceptions):**
  - gas-phase electric deflection of molecular beams (Klemperer et al., above 1000 K) shows permanent dipoles, hence bent structures, for CaF2, SrF2, SrCl2 and the Ba dihalides;
  - matrix-isolation IR and Raman isotope shifts give angle estimates: CaF2 ~142°, SrF2 ~108°, BaF2 ~95°, BaCl2 ~100°. Matrix effects are possible (Kaupp et al. 1991).
- **SIM:**
  - SDCI angles: BaF2 123.0°, SrF2 138.8°, BaCl2 141.4°, CaF2 157.5°;
  - BaF2, BaCl2, BaBr2 and SrF2 are definitely bent; CaF2, SrCl2 and BaI2 have very flat bending potentials; the Be, Mg and most Ca dihalides are linear (same source).
- **SIM (dihydrides):** at the CCSD(T) level, SrH2 is 134.9°, BaH2 117.3° and RaH2 112.6°, with linearization energies of 1.28, 7.04 and 7.72 kcal/mol. The metal d_yz orbital mixes into the HOMO when the molecule bends, and the HOMO–LUMO gap of the linear form shrinks down the group. Lim and Lee, J. Chem. Phys. 126, 104307 (2007), doi:10.1063/1.2437213 — [KAIST PDF](https://dspace.kaist.ac.kr/bitstream/10203/8230/1/000244895600016.pdf).
- **MODEL (explanation):** both core polarization of the metal's subvalence shell and small covalent contributions from (n−1)d orbitals favour bending, with d participation more important for the heavier metals (Kaupp 1991). In dimers the same factors yield pyramidal ML3 cations and odd bridged Ba2H4 structures. The lack of π bonding in hydrides contributes — Kaupp and Schleyer, JACS 115, 11202 (1993) ([PDF](https://opus.bibliothek.uni-wuerzburg.de/files/5484/Kaupp12.pdf)). In metallocenes, π bonding favours linearity, so MCp2 is less bent. Kaupp et al. caution that gas-phase electron diffraction angles for floppy molecules are thermal averages, which can be shrinkage artifacts — JACS 114, 8202 (1992) ([PDF](https://opus.bibliothek.uni-wuerzburg.de/files/5555/Kaupp21.pdf)).
- **Not checked:** trigonal-prismatic d0 WMe6 and stereochemically inactive lone pairs ([SeCl6]2−, [TeCl6]2−) are standard VSEPR failures that I did not verify [unverified].
- **Standing in 2026:** the default teaching model for main-group molecules, with documented failures for heavy, ionic, d0 and transition-metal centres. Ligand-field and second-order arguments replace it there.

#### Bent's rule
- **Statement:** an atom puts more s character into orbitals directed at electropositive substituents, and more p character toward electronegative ones. Bent, Chem. Rev. 1961 [unverified; page blocked]. It is usually tied to bond angles and to 13C–1H NMR coupling constants as observables (OBS) [unverified]. I gathered no source text, so this entry is a placeholder.

#### Jahn–Teller and pseudo-Jahn–Teller effects
- **Statement (JT):** a non-linear molecule in a spatially degenerate electronic state distorts to a lower-symmetry structure that removes the degeneracy. Linear molecules are excepted. Jahn and Teller, Proc. R. Soc. A 161, 220 (1937), doi:10.1098/rspa.1937.0142 — [Jahn–Teller effect, Wikipedia](https://en.wikipedia.org/wiki/Jahn%E2%80%93Teller_effect).
- **Empirical or derived:** derived from group theory, a theorem about vibronic coupling.
- **Observables (OBS):**
  - Cu(II) d9 octahedral complexes are overwhelmingly elongated;
  - low-temperature EPR shows anisotropy;
  - in the dynamic JT regime, observables show the undistorted symmetry;
  - in LaMnO3, cooperative distortions disorder as temperature rises, triggering a metal–insulator transition (same page).
- **Pseudo-JT (second-order JT):** vibronic mixing of a nondegenerate ground state with nearby excited states drives distortions. Bersuker argues it is the only source of instability in nondegenerate high-symmetry configurations, driven by "added covalence". His applications include ferroelectric BaTiO3, puckering in silicene and phosphorene, and the bending of linear molecules (Renner–Teller coupling alone cannot bend them). Bersuker, Chem. Rev. 113, 1351 (2013), doi:10.1021/cr300279n — [Pseudo JT, Wikipedia](https://en.wikipedia.org/wiki/Pseudo_Jahn%E2%80%93Teller_effect).
- **Caveat:** the universality claim rests largely on Bersuker's own publications, and the page presents no counter-views. Labels: MODEL with SIM support.
- **Standing:** the JT theorem is settled. Pseudo-JT universality is a strong programme claim, not a consensus finding.

#### Radius-ratio rule and Pauling's five rules for ionic crystals
- **Statement (Pauling 1929):**
  1. Coordination polyhedra form around cations, and the cation–anion distance and coordination number follow from radius sums and radius ratios.
  2. Electrostatic valence: the bond strengths reaching an anion sum to its charge.
  3. Shared edges, and especially shared faces, destabilize a structure.
  4. High-valent, low-coordination cations avoid sharing polyhedron elements.
  5. Parsimony: few kinds of site.
  Rules 1–3 as summarized in Gibbs et al. 2022 (below). The wording of rules 4–5 and the original 1929 JACS paper were not checked [unverified].
- **RECON, 2020 test:** George, Waroquiers, Di Stefano, Petretto, Rignanese, Hautier, "The Limited Predictive Power of the Pauling Rules", Angew. Chem. Int. Ed. 59 (2020), doi:10.1002/anie.202000829 — [UCLouvain record](https://research.dial.uclouvain.be/handle/2078.5/93572); [ChemRxiv](https://chemrxiv.org/engage/chemrxiv/article-details/60c74642567dfe134bec45b7).
  - About 5,000 oxides were analysed automatically, with coordination environments assigned algorithmically.
  - Only 13% satisfy rules 2–5 at once.
  - The electrostatic valence principle (rule 2) performs worst.
  - Rule 1 fits 66% of coordination environments (Gibbs et al. 2022's summary).
  - The authors call for new structural rules.
  - Chemistry World's subtitle misstates the 13% as "all five" rules; the body text and abstract say rules 2–5 — [Chemistry World](https://chemistryworld.com/news/textbook-structure-rules-formulated-by-linus-pauling-90-years-ago-prove-unreliable/4011236.article).
- **Reply, 2022:** Gibbs, Hawthorne and Brown, Am. Mineral. 107, 1219–1248 (2022), doi:10.2138/am-2021-7938 ([MSA abstract PDF](https://msaweb.org/MSA/AmMin/TOC/2022/Abstracts/AM107P1219.pdf)).
  - The departures are expected, because atoms are not spherical.
  - Bonded radii derived from the electron-density minimum vary: O ranges from ~1.38 Å (bonded to Na) to 0.64 Å (bonded to N).
  - Metal bonded radii match Shannon radii only for electropositive metals.
  - They propose a modified first rule, and tie Pauling bond strength to electron density at the bond critical point.
  - Pauling's rule 2 implicitly assumes bond strength does not depend on bond length; Brown and Shannon (1973) showed that it does, which led to bond valence.
- **Labels:** the coordination numbers and distances are RECON from X-ray structures in databases; the rules are MODEL; the radii are CONV (tabulated, fitted).
- **Standing in 2026:** taught as rationalizations, demoted as predictors. The bond-valence reformulation (§4) is the working successor.

#### Goldschmidt tolerance factor and the newer descriptor τ (Bartel 2019)
- **Statement:** t = (rA + rX)/[√2(rB + rX)]. Values near 1 favour the perovskite structure ABX3. Goldschmidt, 1926 [unverified for the 1926 paper].
- **RECON, 2019 test:** Bartel, Sutton, Goldsmith, Ouyang, Musgrave, Ghiringhelli, Scheffler, "New tolerance factor to predict the stability of perovskite oxides and halides", Sci. Adv. 5, eaav0693 (2019) — [arXiv PDF](https://arxiv.org/pdf/1801.07700v1.pdf); [NREL record](https://research-hub.nrel.gov/en/publications/new-tolerance-factor-to-predict-the-stability-of-perovskite-oxide/). The DOI 10.1126/sciadv.aav0693 is inferred from the article number [unverified].
  - 576 experimentally characterized ABX3 compounds (X = O, F, Cl, Br, I), using Shannon radii.
  - t is 74% accurate overall: oxides 83%, chlorides 51%, bromides 56%, iodides 33%.
  - The new τ = rX/rB − nA(nA − (rA/rB)/ln(rA/rB)), where nA is the A-site oxidation state, with perovskite predicted for τ < 4.18. It was found by SISSO among about 3×10⁹ candidate expressions.
  - τ is 92% accurate overall, and 90–93% for every halide.
  - τ gives monotonic probabilities through Platt scaling.
  - 57,542 of 259,296 A2BB′X6 double perovskites are predicted stable.
- **Labels:** which compounds are perovskites = OBS/RECON (from diffraction); the radii = CONV; t = MODEL (geometric packing); τ = RECON (a statistically selected formula with weak physical interpretation).
- **Standing:** τ is widely adopted as a screening descriptor. t remains the conceptual picture.

#### Hume-Rothery rules
- **Statement:** extensive substitutional solid solubility needs atomic radii within about 15%, the same crystal structure, similar electronegativity and similar valence. Electron-concentration (e/a) ratios mark the "Hume-Rothery phases" [unverified; page blocked; standard textbook wording].
- **RECON tests:**
  - Zhang, Yang and Evans, Acta Mater. 56, 1094 (2008), doi:10.1016/j.actamat.2007.10.059, used neural networks. The correlations fit best for Cu- and Ag-based systems, which suggests a limited scope — [Soton record](https://eprints.soton.ac.uk/165039).
  - Pei, Yin, Hawk, Alman and Gao, npj Comput. Mater. 6, 50 (2020), doi:10.1038/s41524-020-0308-7, used 1,252 multicomponent alloys. The size-misfit criterion δ ≤ ~6% is necessary but not sufficient; Gaussian-process classification reaches 93(2)%; earlier empirical rules rested on very limited data — [Springer](https://link.springer.com/article/10.1038/s41524-020-0308-7).
  - Wang, Zhong and Zhao, J. Alloys Compd. 915, 165173 (2022), doi:10.1016/j.jallcom.2022.165173, used 2,436 high-entropy alloys. Valence electron concentration was the top feature for separating fcc from bcc (VEC < 6.87 gives bcc/B2, VEC > 9.16 gives fcc). ML accuracy was 89–95% — [NSF PAR](https://par.nsf.gov/servlets/purl/10485156).
  - A random-forest model "rediscovered" the e/a ≈ 1.8 rule for Al-based quasicrystals. Liu et al., Adv. Mater. (2021), doi:10.1002/adma.202102507 — [TUS release](https://www.tus.ac.jp/en/mediarelations/archive/20210721_0830.html).
- **Standing:** still a good first-pass screen. Its electron-concentration part is recovered by data-driven models; its size part is necessary but not sufficient.

#### Kitaigorodsky's close-packing principle and Etter's hydrogen-bond rules
- **Kitaigorodsky:** organic molecules pack to minimize empty space, so protrusions fit into hollows (1960s–70s) [unverified; no source opened].
- **Etter (about 1990):** all good proton donors and acceptors are used. Six-membered intramolecular hydrogen bonds form in preference to intermolecular ones. The best donor pairs with the best acceptor. Graph-set notation describes the resulting patterns [unverified; no source opened].
- **Standing:** both are crystal-engineering heuristics. I gathered no 2015–2026 quantitative test of either this session, so this is a gap.

### Inferences
- The geometry failures share a mechanism. Second-order mixing appears wherever a low-lying empty or polarizable shell sits near the frontier orbitals. That includes heavy alkaline-earth d orbitals and core polarization, the pseudo-JT effect, and the Hund-violating near-degeneracy of §4. Rules built on first-order pictures (pair repulsion, rigid spheres) break exactly there.
- Database tests (Pauling, Goldschmidt, Hume-Rothery) split two functions that the classical rules once combined: understanding and prediction. Fitted descriptors (τ, ML) predict better but are RECON objects whose membership criteria are statistical, not mechanistic.
- Gibbs et al.'s reply shows how a rule's defenders respond to a database falsification. They argue that the rule's ingredients (spherical radii) were conventions, and they reformulate the rule on quantum-mechanical observables (electron density).

### Gaps
- I have no sourced text for Bent's rule, Walsh's original papers, WMe6, Kitaigorodsky or Etter; their pages were blocked or not reached before the search budget ran out.
- I did not see the per-rule percentages in George et al. 2020 beyond rule 1 (66%) and the joint 13%.
- I checked no 2023–2026 follow-ups to George et al. (for example bonding-analysis-based rules).

## 4. Atomic and electronic rules (Pauli, Aufbau/Madelung, Hund, Slater, Koopmans, Fajans, HSAB, electronegativity equalization, maximum hardness, bond valence, Pauling bond order–length, Badger)

### Takeaway
These rules fall into three tiers:
- a postulate tested to extreme precision (Pauli);
- orderings derived from the independent-electron (orbital) picture, which hold with well-catalogued exceptions (Aufbau/Madelung, 20 exceptions; Hund, whose standard explanation was reversed and whose molecular excited-state extension fails for azaphenalenes);
- parameter schemes (electronegativity, hardness, bond valence, screening constants) that make measurements comparable across elements. These are useful, but each depends on its scale. HSAB is the most contested of the parameter schemes.

### Cited Findings

#### Pauli exclusion principle
- **Statement:** two identical fermions cannot occupy the same quantum state, so no two electrons in an atom share all four quantum numbers. Pauli, Z. Phys. 31 (1925), doi:10.1007/BF02980631. It was generalized through the spin–statistics theorem (1940).
- **Role:**
  - it underlies shell structure and the periodic table;
  - the stability of matter rests on it: Dyson–Lenard (1967) gave the first rigorous proof, Lieb–Thirring (1975) a simpler one, and Lieb–Loss–Solovej (1995, doi:10.1103/PhysRevLett.75.985) extended it to intense magnetic fields — [Wikipedia](https://en.wikipedia.org/wiki/Pauli_exclusion_principle).
- **Status:** a postulate of quantum theory, not an empirical rule (CONV/MODEL at the level of axioms). Its violation is searched for experimentally (OBS).
  - Helium "paronic" state: upper limit of 5×10⁻⁶ on its statistical weight (Deilamian et al. 1995, doi:10.1103/PhysRevLett.74.4787; same page).
  - VIP-2 at Gran Sasso (underground) passes 100 A of DC current through copper and looks for the forbidden 2p→1s Kα line at 7746.73 eV, about 300 eV below the normal line, using silicon drift detectors.
  - From 2018 data the reported bound is β²/2 ≤ 4.5×10⁻⁴² (90% credibility), or <5.4×10⁻⁴² with systematics. Piscicchia et al., Entropy 22, 1195 (2020), doi:10.3390/e22111195 — [PDF](https://www.openaccessrepository.it/record/73490/files/entropy-22-01195-v2.pdf?download=1); [DOAJ](https://doaj.org/article/286d0a8a7aec483393f2ff5a2f7a7396).
  - An earlier VIP-2 overview lists 3.4×10⁻²⁹ for 2018 and a goal of about 10⁻³¹ — [arXiv 1903.08861](https://arxiv.org/pdf/1903.08861). The two figures differ by about 13 orders of magnitude, presumably because of different normalization or statistical treatment. I could not reconcile them, so check before use.
  - Tests in this "open system" design respect the Messiah–Greenberg superselection rule. Separate "closed system" tests target quantum-gravity models (Entropy 2020).
- **Standing in 2026:** no violation has been observed.

#### Aufbau principle and Madelung (n+l) rule
- **Statement:** in the ground state, electrons fill subshells in order of increasing n+l, with lower n first when n+l is equal. **Exceptions:** 20 elements. In the d-block: Cr, Cu, Nb, Mo, Ru, Rh, Pd, Ag, Pt, Au, Lr. In the f-block: La, Ce, Gd, Ac, Th, Pa, U, Np, Cm — [Aufbau principle, Wikipedia](https://en.wikipedia.org/wiki/Aufbau_principle).
- **Explanations on the page:** interelectronic repulsion and small energy differences. In every exception, the "regular" configuration is a low-lying excited state, and most anomalies disappear on ionization. One textbook calls Madelung's rule an approximate empirical rule with some justification from the Thomas–Fermi model. References include Ostrovsky 1981 (doi:10.1088/0022-3700/14/23/008), Vanquickenborne 1994 (doi:10.1021/ed071p469) and Jensen 2009 (doi:10.1021/ed086p1186).
- **Labels:** spectral lines and term energies (for example NIST level tables) = OBS; the ground term = RECON; "configuration" = MODEL (independent-particle picture); the n+l order = RECON/CONV.
- **Standing:** a teaching scheme with a precisely known list of exceptions.

#### Hund's rules: observation stable, explanation reversed
- **Statement (first rule):** within a configuration, the term with the highest multiplicity lies lowest; degenerate orbitals are singly occupied, with parallel spins, before any is doubly filled. Examples: O 2p⁴, Mn ⁶S, Cr ⁷S (NIST) — [Hund's rule, Wikipedia](https://en.wikipedia.org/wiki/Hund%27s_rule_of_maximum_multiplicity).
- **Explanation debate:**
  - The older account, that electrons in different orbitals stay farther apart and so repel less (attributed on the page to Levine's textbook), is described there as incorrect.
  - Katriel (1972) split term-energy differences into kinetic, nuclear-attraction and repulsion parts. He found the differences dominated by nuclear attraction, which he called an obvious contradiction of the traditional view. Theor. Chim. Acta 23, 309 — [Springer](https://link.springer.com/doi/10.1007/BF00526436).
  - Quantum Monte Carlo on the C atom shows the triplet stabilized by stronger electron–nucleus attraction, while electron–electron repulsion is actually larger in the triplet. Hongo et al. 2004, doi:10.1063/1.1795151 — [arXiv](https://arxiv.org/abs/cond-mat/0408147); [APS abstract](https://archive.aps.org/mar/2005/p32/2).
- **Molecular exceptions:**
  - 5-dehydro-m-xylylene, the first organic molecule shown to violate the rule (Slipchenko et al. 2004, doi:10.1002/anie.200352990);
  - non-Hund configurations in 4d/5d metal–metal bonding (Bjornsson et al. 2014, doi:10.1039/C4SC00337C; Wilson et al. 2024, doi:10.1021/jacs.3c12157) (Wikipedia page).
- **Inverted singlet–triplet gaps, 2022–2025 (reopened, then largely re-settled):**
  - OBS: Aizawa et al., Nature 609, 502 (2022), doi:10.1038/s41586-022-05132-y — [RePEc](https://ideas.repec.org/a/nat/nature/v609y2022i7927d10.1038_s41586-022-05132-y.html). Delayed fluorescence with time constants of about 0.2 µs that shorten on cooling. Fitting the kinetics gives ΔEST = −11 ± 2 meV (RECON). OLEDs reached 17% external quantum efficiency. The emitter is the heptazine analogue HzTFEX2 — [MRS 2026 abstract](https://www.mrs.org/meetings-events/annual-meetings/archive/meeting/presentations/view/2026-mrs-spring-meeting/2026-mrs-spring-meeting-4431358).
  - Dispute (SIM): Dreuw and Hoffmann, "a vanishing myth?", Front. Chem. 11, 1239604 (2023), doi:10.3389/fchem.2023.1239604 ([PDF](https://www.frontiersin.org/journals/chemistry/articles/10.3389/fchem.2023.1239604/pdf)). The heptazine gap depends on method: ADC(2) −0.24 eV, ADC(3) −0.07, CCSD −0.38, CCSD(T) +0.039. They concluded the sign was uncertain.
  - Answer (SIM): Loos, Lipparini and Jacquemin (2023) give best estimates for heptazine of S1 2.717 eV and T1 2.936 eV, a gap of −0.219 eV, and −0.131 eV for cyclazine. They report inverted vertical gaps for 8 of 10 triangulenes, claiming errors under 0.05 eV — [arXiv 2310.19768](https://www.arxiv.org/pdf/2310.19768).
  - A 2025 paper treats the inversion as experimentally confirmed for azaphenalene cores (Aizawa 2022; Wilson 2024). It attributes the inversion to vanishing exchange plus extra double-excitation character in the singlet. de Thieulloy, de Sousa, de Silva (2025), doi:10.1039/d5tc01155h — [RSC](https://pubs.rsc.org/en/content/articlehtml/2025/tc/d5tc01155h).
  - Earlier non-alternant cases (pentalene, heptalene) are noted in Blasco et al., PCCP 2024, doi:10.1039/d3cp05242g — [RSC](https://pubs.rsc.org/en/content/articlehtml/2024/cp/d3cp05242g).
- **Standing:** the rule holds for atomic ground terms. For molecular excited states it fails within a specific class, and the field accepted that failure after the 2023 dispute.

#### Slater's rules, Koopmans' theorem, Fajans' rules, Badger's rule (sources not reached)
- **Slater (1930):** empirical screening constants used to estimate effective nuclear charge; Clementi–Raimondi (1963) later supplied SCF-based values [unverified].
- **Koopmans (1934):** within Hartree–Fock with frozen orbitals, the ionization energy is approximately the negative of the orbital energy. Orbital relaxation and correlation errors partly cancel. It fails for some valence orderings, N2 being the textbook case [unverified].
- **Fajans (1923–24):** covalent character in a nominally ionic bond grows with a small, highly charged cation and a large, polarizable anion [unverified].
- **Badger (1934):** the force constant k and bond length r follow k(r − d)³ ≈ constant, with d depending on the periodic rows of the two atoms [unverified].
- All four pages were blocked by the allowlist and the search budget was spent. Labels: Slater = RECON (fitted); Koopmans = a derived approximation (MODEL); Fajans = RECON/MODEL; Badger = RECON.

#### HSAB (Pearson) and its quantification
- **Statement:** hard acids prefer hard bases and soft acids prefer soft bases. Pearson, JACS 85, 3533 (1963), doi:10.1021/ja00905a001.
- **Quantification:** absolute hardness from I and A by finite difference, where the factor ½ is arbitrary and hardness tracks the band gap (Parr and Pearson 1983, doi:10.1021/ja00364a005).
- **Rivals:** two-parameter E&C equations (Drago; Hancock–Martell for 34 metal ions) predict adduct and formation constants well (doi:10.1021/ic00248a003; doi:10.1021/cr00098a011) — [HSAB page mirror](https://bafybeiemxf5abjwjbikoz4mc3a3dla6ual3jsgpdr4cjr3oz3evfyavhwq.ipfs.4everland.io/wiki/HSAB.html).
- **Ambident reactivity (local HSAB):**
  - Mayr, Breugst and Ofial, "Farewell to the HSAB Treatment of Ambident Reactivity", Angew. Chem. Int. Ed. 50, 6470 (2011), doi:10.1002/anie.201007100. HSAB and Klopman–Salem mispredict the regioselectivity of SCN⁻, CN⁻ and NO2⁻; earlier treatments ignored conflicting data; MeI with nitrite actually gives a mixture. They propose instead: (1) establish kinetic or thermodynamic control; (2) for kinetic control, establish diffusion or activation control; (3) for activation control, apply Marcus theory with intrinsic barriers — [Breugst thesis](https://edoc.ub.uni-muenchen.de/12479/1/Breugst_Martin.pdf).
  - Sheehy et al., Chem. Sci. 2020, doi:10.1039/d0sc02834g ([RSC](https://pubs.rsc.org/en/content/articlehtml/2020/sc/d0sc02834g)). OBS: pyrazine and quinoxaline N-oxides alkylate on N with MeI, MeOTf and benzhydrylium ions; pyrimidine N-oxide gives about 93:7 O:N with MeOTf. SIM: Marcus, DFT and Zhu analyses reproduce the ratios (for 1 + MeOTf, 90:10 to 96:4 computed against 95:5 observed). Atomic-charge schemes disagree about which site is "hard". They separate the global principle (some theoretical support) from the local one (shakier) and urge that its continued use be ceased.
- **Inorganic critique:** Gerber et al., PCCP 2015, doi:10.1039/c4cp05294c ([RSC](https://pubs.rsc.org/en/content/articlehtml/2015/cp/c4cp05294c)) argue that the hard/soft split of cations comes from halide hydration energies. Speciation of [PtCl6−nBrn]2− makes Pt(IV) "hard". This rests on one system plus calculations.
- **Not reached:** the maximum hardness principle (Pearson 1987; Parr–Chattaraj 1991) [unverified].
- **Standing:** global HSAB survives as a qualitative classification of affinities. The local, ambident use is rejected by kinetics groups.

#### Electronegativity and its equalization (Sanderson)
- **Scales (each a RECON from a different OBS):**
  - Pauling 1932, from excess bond energies (doi:10.1021/ja01348a011);
  - Mulliken 1934, the mean of ionization energy and electron affinity (doi:10.1063/1.1749394);
  - Allen 1989, the average valence-electron energy from atomic spectroscopy, which gives Fr 0.67 (doi:10.1021/ja00207a003);
  - an evaluation of scales: Sproul 2020 (doi:10.1021/acsomega.0c00831) — [Wikipedia](https://en.wikipedia.org/wiki/Electronegativity).
- **Equalization:** electrons redistribute on bonding until the Mulliken electronegativity is equalized (Sanderson; JACS 105, 2259, 1983, doi:10.1021/ja00346a026). Electronegativity is sometimes identified with the negative of the chemical potential (doi:10.1021/acs.jpca.9b07468). The original 1951 principle and Parr's 1978 identification are [unverified].
- **Labels:** MODEL/CONV. The page gives no criticisms, so this is a gap.

#### Bond valence model, Pauling's bond order–length relation, and Badger
- **Statement:** an atom's valence equals the sum of its bond valences, s = exp((R0 − R)/b) with b ≈ 0.37 Å. Brown's axioms (1980) are the valence-sum rule, the path rule and valence matching (Gibbs et al. 2022). Sources: Altermatt and Brown 1985 (doi:10.1107/S0108768185002051); Brown, Chem. Rev. 109, 6858 (2009), doi:10.1021/cr900053k ([McMaster](https://experts.mcmaster.ca/scholarly-works/232734)); Pauling 1947, the length–strength correlation (doi:10.1021/ja01195a024) — [Wikipedia](https://en.wikipedia.org/wiki/Bond_valence_method).
- **RECON test:** bond-valence sums lie within about 0.1 valence units of the formal valence for most polyhedra, with deviations up to 1 unit, especially for anions. Lone-pair cations need an angle-dependent r0 (Liebau and Wang, Acta Cryst. A 60, s71, 2004) — [IUCr PDF](https://journals.iucr.org/a/issues/2004/a1/00/a31334/a31334.pdf).
- **Limits:** localized bonds only, so not metals or aromatic compounds; it cannot give energies; lone pairs and Jahn–Teller distortions need special handling (Wikipedia).
- **Pauling's 1947 relation:** the bond length–bond order formula itself (R(n) = R(1) − c·log n) was not displayed in what I saw [unverified].
- **Standing:** the working quantitative successor to Pauling's rule 2, used for structure validation and ion-transport mapping.

### Inferences
- Hund is the cleanest case in this catalogue of the observation surviving while the field's explanation was replaced. The term ordering seen in spectra never changed; the mechanism attached to it was reversed.
- The ground-state and excited-state Hund behaviours fit one picture. Exchange stabilization of the triplet scales with orbital overlap. Where the frontier orbitals are spatially disjoint (azaphenalenes), the exchange term nearly vanishes and configuration mixing in the singlet can invert the order. This is near-degeneracy again, as with the Aufbau exceptions, whose "regular" configurations are low-lying excited states.
- Parameter schemes (electronegativity, hardness, screening, radii, bond valence) are conventions that make different kinds of observation commensurable. Claims such as "X is harder" or "more electronegative" are well defined only once a scale is named.
- The bond-valence law (R = R0 − b ln s) has the same logarithmic form as Pauling's bond order–length relation, and Badger's rule extends "shorter, stronger, stiffer" to force constants. This is an inference; the Badger and Pauling formulas are [unverified].

### Gaps
- I reached no source pages for Slater, Koopmans, Fajans, Badger, the maximum hardness principle or Parr's 1978 work.
- The VIP-2 bound discrepancy (10⁻⁴² against 10⁻²⁹) is unresolved.
- I found no criticism of electronegativity equalization in the sources reached.

## 5. Where rules collide or fail, and what the exceptions share

### Takeaway
Rules collide where two counting or geometric conventions both claim the same object. Examples are the octet against hypervalence, 18 electrons against an ionic picture against jellium for M(CO)8, VSEPR against ligand-field or second-order geometry, and Hückel against Clar. In most cases the collision is settled by redefining the membership criterion, not by new observation. "Mostly true" rules fail together at near-degeneracy, at heavy or polarizable atoms, in excited or transient states, and wherever the calibration set ended.

### Cited Findings

#### Octet against hypervalence
- **The term:** Musher (1969) defined hypervalent as a group 15–18 central atom in a valence above its lowest one (doi:10.1002/anie.196900541).
- **Rejection of the d-orbital model:** the expanded-octet, d-orbital model was common in the 1950s. Later ab initio work showed minimal d participation: Reed and Weinhold 1986 on SF6 (doi:10.1021/ja00273a006); Magnusson 1990 (doi:10.1021/ja00178a014). Its replacement is the 3-centre-4-electron bond (Pimentel 1951, doi:10.1063/1.1748245; Rundle 1947, doi:10.1021/ja01198a028) together with ionic resonance — [Hypervalent molecule, Wikipedia](https://en.wikipedia.org/wiki/Hypervalent_molecule); [3c–4e bond, Wikipedia](https://en.wikipedia.org/wiki/Three-center_four-electron_bond).
- **The terminology dispute continues:**
  - Schleyer (1984) proposed "hypercoordinate";
  - Gillespie (2002) saw no reason to keep "hypervalent" (doi:10.1016/S0010-8545(02)00102-9);
  - Durrant (2015) defined a valence-electron-equivalent γ from atoms-in-molecules charges, with γ > 8 meaning hypervalent. On that criterion PCl5, SO4²⁻ and XeF4 are hypercoordinate but not hypervalent, while O3 and N2O are hypervalent (Chem. Sci. 6, 6614, doi:10.1039/C5SC02076J; [RSC blog](https://blogs.rsc.org/sc/?p=5189));
  - Harcourt and Klapötke (2016) replied that "increased-valence" structures with one-electron bonds are electronically hypervalent, and that γ depends on the wavefunction (Chem. Sci. 7, 3443, doi:10.1039/c5sc04866d; [RSC PDF](https://pubs.rsc.org/en/content/articlepdf/2016/sc/c5sc04866d)).
- **Valence-bond analysis:** ionic structures dominate the XeF2 wavefunction, with about 11% sp³d-type contribution (Braïda and Hiberty 2013, doi:10.1038/nchem.1619; Hypervalent page).
- **OBS:** in pentacoordinate Si and P, bonds are longer than in tetracoordinate analogues (doi:10.1021/ja00176a018).
- **Standing:** the octet survives as a "good first approximation" for s- and p-block atoms (3c–4e page). Whether a molecule is "hypervalent" depends on which criterion is chosen: formal valence, the count from a charge map, or VB structure.

#### VSEPR against ligand-field and second-order geometries
- Heavy MX2 are bent against VSEPR and Walsh (§3). VSEPR has no term for Cu(II) Jahn–Teller elongation or for square-planar 16-electron d8 complexes (§1, §3). The explanations proposed (core polarization, (n−1)d mixing, pseudo-JT covalence) are second-order arguments that scale inversely with a gap; for example, the shrinking HOMO–LUMO gap of linear MH2 favours bending (Lim and Lee 2007).

#### Hückel against Clar in polycyclics, and aromaticity criteria disagreeing
- Hückel's rule is strictly monocyclic. Clar's rule localizes sextets in polycyclics, and every index agrees with it for benzenoids (Solà 2013). Global and local measures diverge in phenanthrene (Wikipedia). There is no consensus definition (Merino et al. 2023). Baird's rule makes aromaticity a property of a state rather than a structure, and neither HOMA (parameterized on S0) nor NICS (dependent on ring size) carries over cleanly between domains (Papadakis and Ottosson 2015).

#### 18-electron rule against the ionic model against jellium: M(CO)8 (§1), and 20-electron ferrocene
- One IR band per metal is read three ways. Which rule "applies" depends on the reference fragments used in the energy decomposition (Ca d² against Ca2+ plus [(CO)8]2−). The ferrocene is called both a "break" (press) and an instructive exception (D. Mills, Chemistry World).

#### Rules "broken" in 2020–2025, and in what sense
- Bredt (2024) still holds for isolable compounds; the anti-Bredt olefins are transient, inferred from trapping and chirality transfer. Hund (2022) fails for azaphenalene excited states, measured indirectly from fluorescence kinetics. The 20-electron ferrocene (2025) puts the extra electrons in antibonding orbitals, as the rule's MO rationale already allows. The Wade–Mingos exceptions (2020, 2024) are crystallographic. Pauling's rules (2020) fail statistically and were defended in 2022 as a matter of radius conventions.

### Inferences
What the exceptions share:
1. **Near-degeneracy.** A small gap between the configurations or levels the rule assumes are well separated: Aufbau exceptions with low-lying "regular" excited configurations; vanishing exchange in Hund inversion; small HOMO–LUMO gaps in bent MH2; pseudo-JT mixing; open-shell acenes in Clar.
2. **Heavy, polarizable or d-capable atoms beyond the calibration set:** heavy alkaline earths (bent MX2, M(CO)8); lone-pair cations in bond valence; S in Baldwin closures; electronegative metals in radius-ratio tests.
3. **Non-ground or transient states:** Baird (T1/S1), Hund-inverted S1, anti-Bredt intermediates. Rules calibrated on isolable ground-state compounds do not carry over.
4. **Convention-dependence of the counted quantity.** Electron counts depend on the formalism; radii on the scale; "hard" on the charge scheme (Sheehy 2020); hypervalence on the criterion; aromaticity on the index. Many "failures" are failures of a convention, which is why defenders reformulate rather than retract (Gibbs et al. 2022; Harcourt and Klapötke 2016).
5. **Statistical scope.** Applied at database scale, the classical rules fall to 13–74% accuracy (Pauling, Goldschmidt), while fitted descriptors and ML reach about 90–93% (τ, HEA classifiers). So "mostly true" in the textbook sense means true for the textbook examples.

Further inferences:
- For the relational frame (descriptive only): several rules are formally pairings about a centre. Examples are paired electrons of opposite spin (Pauli), donor and acceptor (Etter, HSAB), cation and anion bond-valence sums, and the electron transfer behind the "pseudo-element" in Zintl–Klemm. Several are cycling or state-switching rules: Hückel and Baird flip on excitation and flip back on relaxation, and Bredt's olefins form and are consumed. The rules for stable forms (closed shells, magic numbers, closo polyhedra) all count to a closure. This is offered only as a mapping aid for the project. The chemistry sources do not use these terms.
- Membership criteria the project would need stated explicitly:
  - "n-electron complex": the counting formalism.
  - "aromatic": the index and the electronic state.
  - "hypervalent": formal valence, γ, or VB weight.
  - "perovskite-forming": τ < 4.18 with Shannon radii, as a statistical criterion.
  - "hard or soft": the scale (I − A, E&C, or empirical class).
  - "bent or linear": equilibrium against thermal-average geometry (Kaupp 1992).

### Gaps
- I found no single 2023–2026 review that cross-tabulates rule failures. The synthesis above is my inference from the individual sources.
- Planned searches for 2023–2026 developments were not run once the search budget was spent: tests of Etter or Kitaigorodsky, the Clar/Glidewell–Lloyd and spherical-aromaticity rules, M(CO)8 bonding, independent replication of the 20-electron ferrocene, and more inverted-gap emitters beyond HzTFEX2, the Wilson 2024 pentaazaphenalene, and the 2025 phenoxazine–heptazine ChemRxiv preprints ([v1](https://chemrxiv.org/engage/chemrxiv/article-details/67af3359fa469535b94cb24d), [v2](https://chemrxiv.org/engage/chemrxiv/article-details/684025001a8f9bdab59fc35f), not peer-reviewed; they report near-degenerate charge-transfer states and give no measured gap).
- Fetches of the IUPAC Gold Book and of the textbooks (Housecroft and Sharpe; Anslyn and Dougherty; Albright, Burdett and Whangbo) were not attempted, so no textbook wording is quoted.
