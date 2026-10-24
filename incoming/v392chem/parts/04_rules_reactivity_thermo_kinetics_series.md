# Rules, laws and ordered series in chemical reactivity, selectivity, kinetics, thermodynamics, electrochemistry, solution and surface chemistry (status 23 Oct 2026)

## Key gathered points

- **Labels** on every entry: observing · reconstruction from observings · convention or definition · model construct · simulation. **[unverified]** means the item was entered from prior knowledge and not checked against a source in this session.
- **How the rules were made.** Most named rules generalize measured product ratios, rate constants, spectra or equilibrium data (reconstructions from observings), and later received mechanistic or quantum models.
  - A minority are theorems derived under stated conditions: Gibbs phase rule, Nernst, Eyring/TST, Curtin–Hammett, detailed balance.
  - Several are conventions that define a scale: Hammett σ, SHE = 0 V, the Swain–Scott and Mayr reference sets, BET area.
- **Terminology baseline** is the 2021 IUPAC glossary of physical organic chemistry (Pure Appl. Chem. 94(4), 353–534, 2022). It:
  - describes Bell–Evans–Polanyi as a relation sometimes found within closely related reaction series;
  - discourages the name "Brønsted catalysis law";
  - writes Curtin–Hammett as [Y]/[X] = Kc·kY/kX;
  - keeps a revised entry for the anti-Hammond (perpendicular) effect.
- **Documented breaks with primary evidence:**
  - Curtin–Hammett fails when conformers do not interconvert (conformer-specific H-tunnelling, 2017).
  - Le Chatelier's principle gives wrong answers for additions at constant pressure, inert-gas additions, finite changes and mole fractions.
  - Polanyi rules fail for several polyatomic reactions (2024 review).
  - Woodward–Hoffmann-forbidden paths become accessible under mechanical force (2015 experiments). In 2025 calculations the allowed transition state disappears above about 1.4 nN.
  - The reactivity–selectivity principle is regarded as obsolete.
  - Breaking adsorption scaling relations is necessary but not sufficient for better catalysts (2018).
- **Marcus inverted region.** Rates fall at very large driving force. This prediction was confirmed intramolecularly in 1988, and it sets a limit on linear free-energy extrapolation.
- **Verified 2023–2026 items:**
  - Contact history orders nominally identical materials into a triboelectric series (Nature 2025).
  - The Felkin–Anh preference is attributed to strain rather than Pauli repulsion (Chem. Sci. 2024, computational).
  - Mechanical force removes the allowed transition state in aziridine ring opening (Chem. Sci. 2025).
  - A critique of single-number TOF (arXiv 2025 preprint, not peer reviewed).
- **Ordered series** each rank members by one measured property under stated conditions, and most have documented reversals:
  - Hofmeister: low salt, pH, surface charge
  - leaving groups: SNAr, Friedel–Crafts
  - nucleophilicity: protic vs aprotic solvent
  - Irving–Williams: protein design, 2022
  - eluotropic: depends on the adsorbent
  - triboelectric: contact history
- **Session limits.** The search and fetch budgets ran out. Many classical laws were therefore entered from prior knowledge and are marked [unverified].

## 1. Selectivity and mechanism rules (Markovnikov, Zaitsev/Hofmann, Cram/Felkin–Anh, Bürgi–Dunitz, Woodward–Hoffmann, Fukui, Hammond, Curtin–Hammett, Le Chatelier, Polanyi)

### Takeaway
These rules are mostly empirical regioselectivity, stereoselectivity or response generalizations with a mechanistic model attached. Each comes in a pair or family whose member is selected by a stated condition: mechanism type, leaving group or base, the direction of a perturbation on the energy surface, or applied force. The principles that fail most often are the loosely worded ones (Le Chatelier, reactivity–selectivity) or ones whose preconditions are violated (Curtin–Hammett).

### Cited Findings

**Markovnikov / anti-Markovnikov**
- **Label:** reconstruction from observings (original rule) + model construct (extended form). Empirical.
- **Domain:** polar additions to unsymmetrical alkenes and alkynes.
- **Statement.** The original rule: in HX addition to an unsymmetrical unsaturated hydrocarbon, the halogen goes to the carbon with fewer hydrogens.
  - Extended form: the nucleophilic part of any polar reagent goes to that carbon. IUPAC reads this as an indirect statement that the electrophile adds so as to give the more stable carbenium ion, whether or not that ion is a real intermediate.
  - The opposite orientation is called anti-Markovnikov.
  - Source: [Gold Book M03707](https://old.goldbook.iupac.org/html/M/M03707.html) (PAC 1994, 66, 1077, p. 1137; doi 10.1351/goldbook.M03707).
- **Observed:** which constitutional isomer forms (product analysis).
- **Model adds:** the carbocation-stability order.
- **Exceptions:**
  - Radical (peroxide-initiated) HBr addition [unverified].
  - Hydroboration–oxidation [unverified].
  - Modern catalytic and photoredox anti-Markovnikov hydrofunctionalizations [unverified].
- **Standing 2026:** an IUPAC regiochemical descriptor for polar mechanisms. No revision found.

**Zaitsev (Saytzeff) and Hofmann rules** (opposite orientations for the same reaction class)
- **Label:** reconstruction from observings. Empirical.
- **Domain:** β-eliminations.
- **Zaitsev:** dehydrohalogenation of secondary and tertiary alkyl halides preferentially removes the β-H from the carbon with the fewest H. It was later generalized to "the thermodynamically more stable alkene predominates", and the entry notes that exceptions exist ([Gold Book S05481](https://goldbook.iupac.org/terms/view/S05481)).
- **Hofmann:**
  - Original: quaternary ammonium hydroxides bearing different primary alkyl groups give ethylene if an ethyl group is present.
  - Generalized: the alkene with the fewest alkyl groups on its double-bond carbons predominates. This is typical of quaternary ammonium and tertiary sulfonium salts ([Gold Book H02830](https://goldbook.iupac.org/terms/view/H02830)).
- **Observed:** alkene isomer ratios as a function of leaving group, base and solvent.
- **Model adds:**
  - product-stability control for Zaitsev;
  - β-H acidity and steric access in carbanion-like transition states for Hofmann [unverified];
  - bulky bases push toward Hofmann products [unverified].
- **Standing:** both rules are IUPAC terms. Which applies depends on conditions.

**Cram, Cram-chelate, Felkin, Felkin–Anh(–Eisenstein), Cornforth / polar Felkin–Anh**
- **Label:** reconstruction from observings (diastereomer ratios) + model construct (transition-state conformations) + simulation (2024).
- **Domain:** nucleophilic addition to carbonyls with an α-stereocentre.
- **Observed** ([Asymmetric induction](https://en.wikipedia.org/wiki/Asymmetric_induction); primary sources doi 10.1021/ja01143a007 and 10.1016/S0040-4039(00)89719-1):
  - Cram & Elhafez (1952): PhMgBr with 2-phenylpropionaldehyde gave mainly the threo product. LiAlH4 reduction of 1,2-diphenyl-1-propanone gave mainly the erythro product.
  - Felkin (1968): selectivity rose as the other carbonyl substituent grew from Me to t-Bu. Cram's model does not predict this.
- **Models** (same source):
  - Cram: eclipsed conformer, attack from the least hindered side.
  - Chelate: a Lewis-acidic metal bridges the carbonyl O and an α-heteroatom. The chelate was observed directly in 1987.
  - Felkin: a staggered, reactant-like transition state.
  - Anh–Eisenstein (1976–77): adds the antiperiplanar σ* effect and a Bürgi–Dunitz-type approach.
  - Cornforth (1959) and polar Felkin–Anh: an electronegative α-group sits anti to the incoming nucleophile.
- **Exceptions** (same source):
  - chelation and electron-withdrawing α-groups give anti-Felkin products;
  - haloketones deviate;
  - Felkin's substituent minimization cannot apply to aldehydes;
  - Felkin–Anh and Evans 1,3-models can conflict.
- **2024 reinterpretation (simulation).** Activation-strain plus energy-decomposition analysis of cyanide addition to (S)-2-phenylpropanal and (S)-3-phenylbutan-2-one.
  - The preference comes mainly from lower strain in the favoured transition state, not lower Pauli repulsion. Electrostatics also helps.
  - Source: [González-Pinardo, Bickelhaupt & Fernández, Chem. Sci. 2024, 15, 12380](https://docta.ucm.es/entities/publication/04d418de-0d2c-46e1-9c15-fca4f111d3d6/full) (doi 10.1039/d4sc03176h).
- **Standing 2026:** still the working predictive model. Its physical explanation was revised in 2024; predictions did not change.

**Bürgi–Dunitz trajectory**
- **Label:** observing (X-ray) + reconstruction from observings (structure correlation) + simulation.
- **Observed:** in crystals of amino-ketones (protopine, methadone), the amine N sits near the carbonyl C at obtuse angles. In protopine the N···C distance is 2.555 Å at 101.58° ([Bürgi–Dunitz angle](https://en.wikipedia.org/wiki/B%C3%BCrgi%E2%80%93Dunitz_angle)). The primary paper is Bürgi, Dunitz & Shefter, JACS 1973, 95, 5065, as listed in [Asymmetric induction](https://en.wikipedia.org/wiki/Asymmetric_induction).
- **Model adds:**
  - static structures are read as snapshots along a reaction path;
  - the obtuse angle is explained by maximal HOMO–π* overlap;
  - the computed optimum is 107° for hydride adding to formaldehyde.
- **Deviations:** angles in protein active sites cluster near 89 ± 7° (subtilisin 88°). In transaldolase complexes, reaching the trajectory requires large structural rearrangement (Light et al. 2014, doi 10.1107/S1399004713030666), per the same page.
- **Standing:** a geometric heuristic whose value depends on the environment.

**Woodward–Hoffmann rules / conservation of orbital symmetry**
- **Label:** model construct (symmetry derivation) checked against reconstruction from observings (stereochemistry of products).
- **Statement** ([Woodward–Hoffmann rules](https://en.wikipedia.org/wiki/Woodward%E2%80%93Hoffmann_rules); doi 10.1021/ja01080a054, 10.1002/anie.196907811):
  - A thermal pericyclic change is allowed when the number of (4q+2)s plus (4r)a components is odd.
  - Thermal 4n electrocyclizations are conrotatory and photochemical ones disrotatory. This is reversed for 4n+2.
  - Thermal [π2s+π2s] is forbidden; the Diels–Alder reaction is allowed.
- **IUPAC 2021 definition:** a path is allowed if every occupied reactant orbital correlates with an occupied product orbital. The entry warns that such treatments are usually simplified ([IUPAC 2021](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html?lang=en)).
- **Observed:** product stereochemistry and activation barriers.
- **Model adds:**
  - correlation diagrams, frontier orbitals and Hückel/Möbius aromatic transition states, which give equivalent predictions;
  - a conceptual-DFT reading (doi 10.1021/ar200192t).
- **Exceptions** (Wikipedia):
  - a strained bicyclic cyclobutene opens disrotatorily at 400 °C;
  - photochemical "pericyclic" steps often run through diradicals;
  - dioxetanedione is computed to decompose by a formally forbidden asynchronous retro-[2+2] (doi 10.1021/acs.jpca.6b10365);
  - force from ultrasound biases cyclobutene opening (doi 10.1038/nature05681).
- **Mechanochemistry, observing.** Single-molecule AFM force spectroscopy on polymer-embedded mechanophores, on a ~0.1 s timescale ([Wang et al., Nat. Chem. 2015, 7, 323](https://www.nature.com/articles/nchem.2185)):
  - the forbidden benzocyclobutene opening needed about 130 pN *less* force than the allowed one;
  - forbidden gem-difluoro- and gem-dichlorocyclopropane openings needed about 560 and 1,000 pN *more*.
- **Mechanochemistry, simulation.** Force-modified surfaces (DFT/CASPT2, ab initio steered MD) for cis-dipropylaziridine ([Germann & Meisner, Chem. Sci. 2025](https://pubs.rsc.org/en/content/articlehtml/2025/sc/d5sc04954g)):
  - the allowed conrotatory transition state survives up to 1.4 nN;
  - the disrotatory path becomes a true transition state from 1.2 nN;
  - above 1.4 nN only the forbidden path remains.
  - The authors judge the allowed/forbidden boundary more diffuse than assumed.
- **Standing 2026:** valid for concerted reactions on unperturbed surfaces. Under force, the outcome depends on relative barriers; this is active research.

**Fukui frontier-orbital theory**
- **Label:** model construct (perturbational molecular-orbital approximation).
- **Statement:** the HOMO–LUMO interaction dominates reactivity. The justification is the Klopman–Salem expression, with its filled–filled repulsion, Coulomb and filled–empty terms ([FMO theory](https://en.wikipedia.org/wiki/Frontier_molecular_orbital_theory); Fukui, Yonezawa & Shingu 1952, doi 10.1063/1.1700523).
- **Built on:** position-specific reactivity of aromatic hydrocarbons, endo Diels–Alder selectivity and suprafacial [1,5] shifts. It was widely criticized at first.
- **Exceptions:** charge-controlled reactions [unverified].
- **Standing:** Nobel 1981, shared with Hoffmann ([WH page](https://en.wikipedia.org/wiki/Woodward%E2%80%93Hoffmann_rules)). Still a standard heuristic.

**Hammond postulate / Leffler; anti-Hammond (perpendicular) effect**
- **Label:** model construct (a postulate that cannot be derived).
- **Statement:**
  - A transition state and an adjacent intermediate of similar energy interconvert with little structural change.
  - It is usually stated in Leffler's form: the transition state resembles the less stable neighbour.
  - Corollary: anything that stabilizes an intermediate also stabilizes the transition state leading to it.
  - IUPAC uses the mnemonic "Bemahapothle" for the contributors (Bell, Marcus, Hammond, Polanyi, Thornton, Leffler).
  - Source: [Gold Book H02734](https://goldbook.iupac.org/terms/view/H02734).
- **Observed:** transition-state structure is not observed directly. It is inferred from LFER slopes, isotope effects and computation [inference].
- **IUPAC 2021 Leffler α:** the sensitivity of the activation Gibbs energy to the reaction Gibbs energy ([eScholarship copy](https://escholarship.org/content/qt2rx9m9pg/qt2rx9m9pg_noSplash_871a62f61ba4b58a20c995d9ec4b4983.pdf)).
- **Break:** stabilizing a structure that lies *off* the minimum-energy path moves the transition state *toward* it. This anti-Hammond entry was revised in 2021 ([IUPAC provisional text](https://iupac.org/wp-content/uploads/2021/05/PAC-REC-18-10-10.R6_PR20210507.pdf)). In More O'Ferrall–Jencks diagrams, changes along the reaction coordinate follow Hammond, and perpendicular changes go the opposite way ([Gold Book M04030](https://goldbook.iupac.org/terms/view/A00395)).

**Curtin–Hammett principle / Winstein–Holness**
- **Label:** model construct derived from kinetics under stated conditions, tested by observings.
- **Statement:**
  - For isomers that interconvert faster than they form products irreversibly, the product ratio depends on the difference in transition-state Gibbs energies: [Y]/[X] = Kc·kY/kX.
  - Winstein–Holness: the overall rate is the mole-fraction-weighted sum of the individual rate constants.
  - Source: [IUPAC 2021](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html?lang=en). The 1994 wording is at [Gold Book C01480](https://old.goldbook.iupac.org/plain/C01480-plain.html).
  - IUPAC also keeps "A value" as a defined conformational quantity: the equatorial-to-axial Gibbs energy, 7.28 kJ mol⁻¹ for methyl ([provisional](https://iupac.org/wp-content/uploads/2021/05/PAC-REC-18-10-10.R6_PR20210507.pdf)).
- **Observed:** product ratios compared with NMR conformer populations ([Curtin–Hammett principle](https://en.wikipedia.org/wiki/Curtin%E2%80%93Hammett_principle); review Seeman 1983, doi 10.1021/cr00054a001):
  - N-methylpiperidine oxidation, 95:5;
  - tropane alkylation, where the minor conformer gives the major product;
  - Ti-mediated epoxidation, 91:9 against a computed 1.43 kcal/mol.
- **Conditions:** interconversion much faster than product formation (about a 10× margin is suggested), and irreversible products.
- **Break.** Trifluoromethylhydroxycarbene, made by thermolysis of 3,3,3-trifluoro-2-oxopropanoic acid:
  - the trans conformer rearranges by H-atom tunnelling while the cis conformer is inert (IR time-course plus CCSD(T) surface);
  - the high barrier between conformers makes Curtin–Hammett inapplicable;
  - source: [Mardyukov, Quanz & Schreiner, Nat. Chem. 2017, 9, 71](https://www.nature.com/articles/nchem.2609).

**Le Chatelier's principle**
- **Label:** reconstruction from observings / heuristic model construct. Not a theorem as usually worded.
- **Statement:** a disturbed equilibrium shifts so as to partly offset the disturbance. Le Chatelier 1884 and Braun 1887 [unverified dates].
- **Failures** documented by [Cheung, J. Chem. Educ. 2009, 86, 514](https://www.ifi.unicamp.br/~mtamash/f320_termo/jchemeduc86_514.pdf):
  - Adding a reactant at constant T and P to a gas reaction with Δn ≠ 0 can *raise* rather than offset that reactant's concentration.
  - Any version can mispredict for finite (non-infinitesimal) changes.
  - Adding CS2 at constant T and P to CH4 + 2H2S ⇌ CS2 + 4H2: the added gas also dilutes the other species, so the principle cannot give the direction; only Q versus K can.
  - Adding argon at constant T and P to CO + 2H2 ⇌ CH3OH shifts toward reactants.
  - Compressing NO2/N2O4 shifts toward N2O4, but the final [NO2] still exceeds its value before compression.
  - In Cheung's survey only 3, 4 and 2 of 33 teachers answered the last three cases correctly.
- **Mole-fraction non-moderation** ([Solaz-Portolés & Sanjosé 2013](https://journals.azbuki.bg/science/chemical-reactions-do-not-always-moderate-changes-in-concentration-of-an-active-component/view)). For ideal gases aA + bB ⇌ cC with A added at constant T and V:
  - the molar concentration of A is always moderated;
  - its mole fraction is not when y_A ≥ a/|Δν| (Δν < 0);
  - for NH3 synthesis this means y(N2) ≥ ½.
- **Teaching trend:** replace the principle with Q-versus-K reasoning. It is criticized as teleological ([Underwood, ChemEd X, c. 2017](https://chemedx.org/node/3902)).

**Polanyi rules / mode specificity**
- **Label:** reconstruction from observings (originally) + simulation (modern QCT).
- **Statement:** for atom + diatom reactions, translational energy drives early (reactant-like) barriers and vibrational energy drives late barriers. There is no guarantee this holds for polyatomic systems ([Czakó et al., PCCP 2024, 26, 15818](https://www.staff.u-szeged.hu/~pappdo/PCCP25_Persp_2024.pdf); doi 10.1039/d4cp00417e).
- **Observed / simulated** (same source):
  - QCT on high-level potential energy surfaces;
  - crossed-beam velocity-map imaging of F + CD4 and Cl + CHD3;
  - Crim and Zare's H + HOD work.
- **Follow the rules:** F + C2H6 and Cl + C2H6.
- **Violate the rules:**
  - OH + C2H6 has an early barrier, yet many vibrational modes promote reaction at least as well as translation;
  - F + H2O, OH + H2S and Cl + CHD3 are also cited.
- **Generalization:** the sudden vector projection model. It applies only to direct reactions and ignores intramolecular vibrational energy redistribution (IVR).

**Reactivity–selectivity principle**
- **Label:** reconstruction from observings. Now rejected as a general law.
- **Statement:** more reactive means less selective.
- **Status:** accepted until the 1970s and now regarded as obsolete. Constant or inverse relationships are about as common as the predicted one. Its early support came from intermediates reacting near diffusion control ([RSP](https://en.wikipedia.org/wiki/Reactivity%E2%80%93selectivity_principle); Mayr & Ofial 2006, titled "...An Imperishable Myth...", doi 10.1002/anie.200503273). Ritchie N⁺ is an explicitly constant-selectivity scale ([Nucleophile](https://en.wikipedia.org/wiki/Nucleophile)).

### Inferences
- **Paired rules.** Markovnikov/anti-Markovnikov, Zaitsev/Hofmann, Hammond/anti-Hammond and allowed/forbidden are each one mechanism class with two opposite outcomes. The condition that selects between them should be stated as part of each rule's membership criterion.
- **Explanation revised, prediction kept.** Felkin–Anh 2024 and Woodward–Hoffmann under force show that the explanation can change while the predictive rule stays: the energy-decomposition terms are model-dependent, not observed.
- **Two kinds of "failure".** Curtin–Hammett failures are violated preconditions. Le Chatelier failures expose an imprecisely stated heuristic.

### Gaps
- Not verified: original papers and dates for Le Chatelier/Braun, Hammond (1955), Leffler (1953), the Kharasch peroxide effect and Polanyi's chemiluminescence work.
- No 2023–26 primary work checked on Le Chatelier-type responses in non-equilibrium reaction networks.
- One Curtin–Hammett application paper was seen by title only ([PMC9127809](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9127809/)).

## 2. Linear free-energy and energy relationships (Brønsted, Bell–Evans–Polanyi, Hammett/Taft/Swain–Scott/Mayr, Marcus, Sabatier, scaling and d-band, energetic span)

### Takeaway
Linear free-energy relationships are empirical correlations anchored to conventions (reference reactions and reference sets). Marcus theory and the energetic-span model are derived constructs that explain or bound them. In catalysis, scaling relations both simplify design and cap performance; breaking them is necessary but not sufficient.

### Cited Findings

**Brønsted relation**
- **Label:** reconstruction from observings + convention (statistical factors p and q).
- **Statement:** within a series, the log of the reduced rate coefficient is linear in the log of the reduced acid (or base) constant, with slope α or β. IUPAC 2021 discourages "catalysis law" because the relation also covers uncatalysed proton transfers ([IUPAC 2021](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html?lang=en)).
- **Model adds:** α and β are read as the degree of proton transfer at the transition state ([Brønsted catalysis equation](https://en.wikipedia.org/wiki/Br%C3%B8nsted_catalysis_equation)).
- **Exceptions** [unverified]:
  - curvature near diffusion control;
  - the "nitroalkane anomaly", with α outside 0–1;
  - origin: Brønsted & Pedersen 1924 on nitramide decomposition.

**Bell–Evans–Polanyi**
- **Label:** reconstruction from observings.
- **Statement:** EA = a + bΔrH, sometimes found within closely related reaction series ([eScholarship copy of IUPAC 2021](https://escholarship.org/content/qt2rx9m9pg/qt2rx9m9pg_noSplash_871a62f61ba4b58a20c995d9ec4b4983.pdf)).
- **Catalysis use** [unverified]: transition-state energies scale with reaction energies across metal surfaces in DFT ("Brønsted–Evans–Polanyi").
- **Limit:** the quadratic Marcus form implies the slope changes with driving force, so linear BEP is only local [inference].

**Hammett equation (σ⁺, σ⁻, Yukawa–Tsuno)**
- **Label:** convention (σ fixed by a reference reaction) + reconstruction from observings. Empirical: neither thermodynamics nor kinetics predicts it.
- **Statement** ([Hammett equation](https://en.wikipedia.org/wiki/Hammett_equation); doi 10.1021/ja01280a022; compilation doi 10.1021/cr00002a004):
  - log(k/k0) = ρσ for meta- and para-substituted aromatics.
  - σ is defined by ionization of benzoic acids in water at 25 °C, where ρ ≡ 1.
  - The sign of ρ diagnoses whether charge builds up.
  - σ⁺ comes from cumyl chloride solvolysis in 90% aqueous acetone. σ⁻ is used for through-conjugated negative charge.
- **Exceptions:**
  - ortho groups are excluded because of steric effects;
  - curved plots indicate a change of mechanism or rate-limiting step;
  - bicyclo[2.2.2]octane acids show substituent effects without π transmission (Roberts & Moreland 1953).
- **Standing:** the entry appears in the Gold Book 5th edition (2025), doi 10.1351/goldbook.H02732.

**Taft equation** [unverified]
- Separates polar (σ*) and steric (Es) contributions using rates of acid- versus base-catalysed ester hydrolysis (1950s).

**Swain–Scott, Ritchie, Mayr–Patz scales** ([Nucleophile](https://en.wikipedia.org/wiki/Nucleophile); doi 10.1021/ja01097a041, 10.1021/ar50058a005, 10.1002/anie.199409381, 10.1021/ja010890y, 10.1002/anie.200600542)
- **Label:** convention (reference sets) + reconstruction from observings (second-order rate constants).
- **Swain–Scott (1953):** log(k/k0) = s·n, with s = 1 for MeBr and water as the reference nucleophile. Values of n: I⁻ 5.0, N3⁻ 4.0, AcO⁻ 2.7.
- **Ritchie (1972):** N⁺ with no substrate term, i.e. constant selectivity. In MeOH: CN⁻ 5.9, MeO⁻ 7.5, N3⁻ 8.5, PhS⁻ 10.7.
- **Mayr–Patz (1994–2006):** log k = s(N + E), with benzhydrylium ions as references.
  - Examples: piperidine N 15.63 (s 0.64), methoxide 10.49 (0.68), water 5.20 (0.89).
  - The unified form reduces to Swain–Scott and Ritchie as special cases.
  - α-effect nucleophiles are usually excluded.
- **Conditions** [unverified]: Mayr data at 20 °C, solvent-specific, held in a public LMU database.

**Marcus theory**
- **Label:** model construct (derived from crossing parabolic free-energy surfaces) + observing.
- **Statement** ([Roussel lecture, 2021](https://people.uleth.ca/~roussel/C4000foundations/slides/21etransfer.pdf)):
  - ΔG‡ = (ΔG° + λ)²/4λ, where λ is the reorganization energy.
  - The non-adiabatic rate includes |H_DA|².
  - The rate is maximal at −ΔG° = λ and falls beyond it: the inverted region.
- **Observed:** Closs & Miller, Science 1988, 240, 440. Donor–bridge–acceptor molecules with varied acceptors; rate constants over ~10⁶–10¹⁰; both regions seen. The curve is asymmetric, which is attributed to high-frequency acceptor vibrations (same source).
  - Earlier key papers: Miller, Beitz & Huddleston (JACS 1984) and Closs et al. (J. Phys. Chem. 1986), listed in [Piotrowiak 1999](https://pubs.rsc.org/en/content/articlehtml/1999/cs/a707029b); content not checked.
  - Rehm–Weller bimolecular quenching (1970) did not show inversion; the diffusion-limit explanation is [unverified].
- **Standing:** a confirmed prediction. Nobel 1992 and the Marcus–Hush–Chidsey electrode extension [unverified].

**Sabatier principle / volcano plots** [mostly unverified]
- **Label:** reconstruction from observings + model construct.
- **Statement:** the best catalyst binds intermediates neither too strongly nor too weakly, giving a volcano-shaped plot of activity against binding (Sabatier, early 20th century; Balandin) [unverified].
- **Current practice:** volcanoes are built from computed descriptors combined with scaling and BEP relations [unverified].
- **Proposed limits:** dynamic or "programmable" catalysis is claimed to exceed the static maximum (Dauenhauer group, 2019 onward) [unverified].

**Adsorption-energy scaling relations; d-band model**
- **Label:** simulation (DFT) + reconstruction from observings.
- **Statement** ([Govindarajan, Garcia-Lastra, Meijer & Calle-Vallejo, Curr. Opin. Electrochem. 2018, 8, 110](https://dare.uva.nl/id/e22fe4be-d8ae-4d49-b249-f943677063c3); doi 10.1016/j.coelec.2018.03.025):
  - Adsorption energies of many species scale linearly with one another on homogeneous and heterogeneous catalysts. This reduces the number of variables but constrains performance.
  - For OER and ORR, the *OOH–*OH separation is about 3.20 eV on most catalysts, against an ideal 2.46 eV.
  - Breaking this relation is "a necessary yet insufficient condition"; the authors propose the ESSI descriptor instead.
- **Arithmetic** [inference]: (3.20 − 2.46)/2 ≈ 0.37 V, the minimum OER overpotential usually quoted for catalysts bound by this relation.
- **d-band model** [unverified]: binding strengthens as the d-band centre rises toward the Fermi level (Hammer & Nørskov, 1990s).

**Energetic span model**
- **Label:** model construct (transition-state theory + steady state) linking simulation (computed energy profiles) to observing (TOF).
- **Statement** ([Kozuch & Shaik, Acc. Chem. Res. 2011, 44, 101](https://cris.iucc.ac.il/en/publications/how-to-conceptualize-catalytic-cycles-the-energetic-span-model/)):
  - TOF is set by a TOF-determining transition state and intermediate (TDTS and TDI), chosen by their degree of TOF control.
  - The span between them (plus ΔGr if the TDTS comes before the TDI) acts as the apparent activation energy.
  - The rate is set by "rate-determining states", not a single rate-determining step. TDTS and TDI need not be adjacent or extreme.
  - Only species located between TDI and TDTS change the rate.
- **2025 critique** (preprint, not peer reviewed): TOF° = (kBT/h)·exp(−δE/RT) reduces catalysis to a single scalar and assumes one dominant pathway under ideal, uniform conditions ([Crespilho, arXiv:2505.01213](https://arxiv.org/pdf/2505.01213)).

### Inferences
- Every one of these scales is relative to a reference convention: benzoic acid in water at 25 °C, MeBr, benzhydrylium ions, or the SHE. The resulting rankings are therefore defined relative to a chosen reference set.
- The Marcus inverted region and curvature in Hammett and Brønsted plots mark where linearity ends. They signal either a change of mechanism or the quadratic shape of free-energy surfaces.

### Gaps
- Not verified: Sabatier and d-band specifics, catalysis BEP data, Taft parameters, and 2023–26 "scaling-breaking" papers. A 2025 Chem. Soc. Rev. review on scaling relations could not be retrieved.

## 3. Kinetic and thermodynamic laws (Arrhenius, Eyring, Lindemann, Michaelis–Menten, Langmuir/BET/Freundlich, Raoult/Henry, phase rule, Trouton, Kopp, Dulong–Petit, Hess, Kirchhoff, stoichiometric laws, Graham)

### Takeaway
Rate laws began as empirical forms and were later derived from mechanistic models, whose assumptions mark where they fail. Thermodynamic items divide into derived theorems (phase rule, Kirchhoff, Hess as a consequence of a state function) and empirical regularities with exceptions (Trouton, Kopp, Dulong–Petit). The stoichiometric laws became membership criteria for "compound". They hold only in the classical limit (mass) and not for berthollides (composition).

### Cited Findings

**Arrhenius equation**
- **Label:** reconstruction from observings (empirical); partly derived by later models.
- **Statement** ([Arrhenius equation](https://en.wikipedia.org/wiki/Arrhenius_equation); doi 10.1515/zpch-1889-0408; history doi 10.1021/ed061p494):
  - k = A·exp(−Ea/RT), from Arrhenius 1889 following van 't Hoff 1884.
  - The page regards it as best treated as empirical.
  - Collision theory needs a steric factor; transition-state theory gives the Eyring form.
- **Observed:** ln k against 1/T is linear. The rule of thumb is roughly 2–3× per 10 °C.
- **Deviations:**
  - super-Arrhenius slowing near the glass transition;
  - T^n prefactors and stretched exponentials;
  - surface kinetics;
  - barrierless reactions;
  - tunnelling curvature and negative apparent Ea [unverified].

**Eyring equation / transition-state theory**
- **Label:** model construct (statistical-mechanical derivation) fitted to observed k(T).
- **Statement** ([Eyring equation](https://en.wikipedia.org/wiki/Eyring_equation); doi 10.1063/1.1749604, 10.1039/tf9353100875):
  - k = κ(kBT/h)·exp(−ΔG‡/RT), from Eyring and Evans–Polanyi, 1935.
  - κ is often set to 1 (no recrossing) but is usually below 1. It is estimated by reactive-flux (Bennett–Chandler) simulations.
  - A plot of ln(k/T) against 1/T gives ΔH‡ and ΔS‡, assuming both are constant.
- **Limits:** tunnelling and non-statistical dynamics [unverified].

**Lindemann–Hinshelwood mechanism**
- **Label:** model construct + observing (pressure-dependent k).
- **Statement:** collisional activation followed by decay of A* gives first-order kinetics at high pressure and second-order at low pressure, with a fall-off region between. It was proposed by Lindemann and Christiansen in 1921–22; Hinshelwood added multiple vibrational modes.
- **Observed failure:** the plot of 1/k against 1/[M] is curved, not linear. RRKM theory is needed.
- **Source:** [Lindemann mechanism](https://en.wikipedia.org/wiki/Lindemann_mechanism) (doi 10.1039/TF9221700598).

**Michaelis–Menten kinetics**
- **Label:** model construct + reconstruction from observings.
- **Statement** ([Michaelis–Menten kinetics](https://en.wikipedia.org/wiki/Michaelis%E2%80%93Menten_kinetics); doi 10.1042/bj0190338, 10.1111/febs.12598, 10.1137/1031091):
  - v = Vmax[S]/(Km + [S]).
  - 1913 version: equilibrium assumption. Briggs–Haldane (1925): steady state, Km = (k₋₁ + kcat)/k₁.
  - Assumptions: one substrate, [E] much less than [S], quasi-steady state.
- **Observed:** initial rates. Nonlinear regression is preferred over linearized plots.
- **Limits:**
  - molecular crowding;
  - most enzymes have more than one substrate;
  - Km depends on T and pH;
  - cooperativity and substrate inhibition [unverified].

**Langmuir, Freundlich, Temkin, BET isotherms**
- **Labels:** Langmuir is a model construct, Freundlich is empirical, and BET is a model construct now used as a convention for surface area.
- **Langmuir (1916–18):** equivalent sites, a monolayer and no lateral interactions. Measured as adsorbed volume against pressure at fixed T, reaching saturation ([Langmuir model](https://en.wikipedia.org/wiki/Langmuir_adsorption_model); doi 10.1021/ja02242a004).
- **Failures:** heterogeneous sites, lateral interactions (visible in heats of adsorption) and multilayers, which BET (1938, doi 10.1021/ja01269a023) addresses.
- **Freundlich:** empirical, linear on a log–log plot. A good fit does not prove heterogeneity.
- **Temkin:** the heat of adsorption falls linearly with coverage.
- **Surface area** is scale-dependent.
- **BET details** [unverified]: N2 at 77 K over p/p0 ≈ 0.05–0.3; IUPAC 2015 physisorption report; 2022 inter-laboratory reproducibility study of BET areas.

**Microscopic reversibility / detailed balance**
- **Label:** model construct (time-reversal symmetry).
- At equilibrium, detailed balancing of each elementary process with its reverse follows from microscopic reversibility ([IUPAC 2021](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html?lang=en)).

**Raoult and Henry laws** [unverified]
- **Label:** reconstruction from observings; limiting laws.
- **Raoult (1887):** pᵢ = xᵢ·pᵢ* for ideal solutions.
- **Henry (1803):** a dilute solute's partial pressure is proportional to its mole fraction, with a solute-specific constant.
- In the dilute limit the solvent follows Raoult and the solute Henry; Gibbs–Duhem links the two.
- **Deviations:** positive or negative deviations and azeotropes; reactive gases (CO2, NH3, SO2); high pressure; salting-out (Sechenov).

**Gibbs phase rule** [unverified]
- **Label:** model construct (theorem derived from equilibrium thermodynamics) + convention (how components are counted).
- F = C − P + 2 (Gibbs, 1875–78), where C counts components after subtracting independent reactions and constraints.
- At fixed pressure F = C − P + 1. Fields, curved surfaces and similar factors add terms.

**Trouton; Neumann–Kopp; Dulong–Petit** [unverified]
- **Label:** reconstructions from observings.
- **Trouton (1884):** ΔvapS at the normal boiling point is about 85–88 J K⁻¹ mol⁻¹. Exceptions are H-bonded liquids (water about 109) and very low-boiling liquids. Hildebrand's refinement compares at equal vapour concentration.
- **Neumann–Kopp (1831/1864):** a solid compound's Cp is about the sum of its elements' values. It fails at low T and for light elements.
- **Dulong–Petit (1819):** Cp of many solid elements is about 3R ≈ 25 J K⁻¹ mol⁻¹, and was used to fix atomic weights.
  - It fails at low T and for diamond, B, Be and Si at room temperature.
  - Einstein (1907) and Debye (1912) explained this: classical equipartition gives 3R only above the characteristic temperature.

**Hess and Kirchhoff**
- **Hess (1840)** [date unverified]: the overall reaction enthalpy equals the sum over steps. It is used, for example, to derive lattice enthalpy in the Born–Haber cycle ([Born–Haber cycle](https://en.wikipedia.org/wiki/Born%E2%80%93Haber_cycle)). Today it is read as a consequence of enthalpy being a state function [unverified].
- **Kirchhoff (1858):** d(ΔrH)/dT = ΔrCp [unverified].
- **Label:** Hess is a reconstruction from observings that was later derived; Kirchhoff is derived.

**Stoichiometric laws**
- **Conservation of mass** ([Conservation of mass](https://en.wikipedia.org/wiki/Conservation_of_mass); doi 10.1021/ed052p658, 10.1179/amb.1962.10.3.119):
  - History: Rey 1630, Lomonosov 1756 (contested), Lavoisier 1773.
  - Observed by weighing sealed vessels. Stas bounded any change to at most 2–4 parts in 100,000.
  - Modern status: valid only in the classical limit. Mass changes from chemical energy are too small to measure; nuclear reactions do not conserve mass (Cockcroft & Walton 1932).
  - Arithmetic [inference; the 286 kJ/mol tabulated value is unverified]: forming 18 g of water releases about 286 kJ, i.e. about 3×10⁻¹² kg, or about 2×10⁻¹⁰ of the mass.
  - **Label:** observing → reconstruction; now subsumed by mass–energy conservation.
- **Definite proportions** ([Law of definite proportions](https://en.wikipedia.org/wiki/Law_of_definite_proportions)):
  - Proust 1797, contested by Berthollet. Berthollet's variable-composition view was historically rejected for molecular compounds.
  - Exceptions:
    - non-stoichiometric solids, e.g. wüstite with 0.83–0.95 Fe per O;
    - isotopic variation, especially of hydrogen;
    - polymers.
  - **Label:** reconstruction from observings, now also partly a convention that defines "compound" [inference].
- **Multiple proportions (Dalton), combining volumes (Gay-Lussac 1808), Avogadro (1811)** [unverified]:
  - Small whole-number ratios; equal gas volumes contain equal numbers of molecules. This is exact only for ideal gases; real gases deviate through Z.
  - N_A has been fixed exactly since the 2019 SI.
  - Exceptions: berthollides and large molecules.

**Graham's law** [unverified]
- **Label:** reconstruction from observings, later derived from kinetic theory.
- Effusion rate is proportional to M^−½ (1846–48). It holds for free-molecular flow, not ordinary interdiffusion. It was the basis of UF6 gaseous-diffusion enrichment.

### Inferences
- **Where the derived laws fail.** The failure regimes of derived kinetic laws can be read from their assumptions: no recrossing (Eyring), single activated species (Lindemann), [E] much less than [S] (Michaelis–Menten), uniform sites (Langmuir).
- **Pass/fail tests.** Definite proportions and Avogadro's law now act partly as tests of whether something counts as a "compound" or an "ideal gas", rather than as laws that could be falsified [inference].

### Gaps
- Primary sources for Raoult, Henry, the phase rule, Trouton, Kopp, Dulong–Petit, Kirchhoff, Graham, Gay-Lussac and Avogadro were not checked (blocked fetches).
- BET reproducibility work after 2022 was not checked.

## 4. Electrochemistry and solutions (Faraday, Nernst, Butler–Volmer/Tafel, Debye–Hückel, Kohlrausch, Ostwald dilution, Schulze–Hardy, Traube, Ostwald ripening, Kelvin, Pourbaix, Ellingham, Born–Haber, Kapustinskii)

### Takeaway
Equilibrium electrochemistry (Nernst, Pourbaix, Ellingham, Born–Haber) is derived thermodynamics applied to tabulated data, with conventions for the reference states. Kinetic and solution laws (Tafel, Debye–Hückel, Kohlrausch, Schulze–Hardy, Traube) are empirical limiting laws with model derivations valid only in dilute or low-overpotential ranges.

### Cited Findings

**Faraday's laws** [mostly unverified]
- **Label:** reconstruction from observings (coulometry); now an identity backed by definitions.
- **Statement:** the amount changed is Q/(zF), from 1833–34 [unverified].
- F ≈ 96,485 C mol⁻¹ ([Standard electrode potential](https://en.wikipedia.org/wiki/Standard_electrode_potential)).
- F = N_A·e has been exact since the 2019 SI [unverified].
- Apparent deviations arise from side reactions (faradaic efficiency below 100%) [unverified].

**Nernst equation**
- **Label:** model construct (thermodynamic derivation) + convention (SHE = 0) + observing (EMF).
- **Statement** ([Nernst equation](https://en.wikipedia.org/wiki/Nernst_equation)):
  - E = E° − (RT/zF)·ln Q, i.e. 0.05916 V per decade at 25 °C.
  - It holds only at zero net current. ΔG° = −zFE°.
- **Conditions:**
  - activities, not concentrations;
  - a formal potential E°′ absorbs activity coefficients, pH and complexation, and must be measured for each medium.
- **Breaks:**
  - at very low concentrations of potential-determining ions the predicted potential diverges and the electrode is "unpoised";
  - overpotential and resistive losses appear when current flows.

**Butler–Volmer and Tafel** [unverified]
- **Label:** Tafel is a reconstruction from observings; Butler–Volmer is a model construct.
- **Tafel (1905, H2 evolution):** η = a + b·log j, with b ≈ 118 mV/decade for α = 0.5 at 25 °C.
- **Butler–Volmer:** Butler 1924; Erdey-Grúz & Volmer 1930.
- **Limits:**
  - mass transport, multistep mechanisms and adsorption;
  - Marcus–Hush–Chidsey theory predicts curved Tafel plots at large η.

**Debye–Hückel and extensions**
- **Label:** model construct tested against measured activity coefficients.
- **Statement:** Debye & Hückel 1923 (Phys. Z. 24, 185). The limiting law gives the log of the mean activity coefficient as proportional to z²√I, and holds only at low concentration ([Debye–Hückel equation](https://en.wikipedia.org/wiki/Debye%E2%80%93H%C3%BCckel_equation)).
- **Extensions** [unverified]:
  - extended Debye–Hückel with ion size;
  - Davies, to about 0.5 mol kg⁻¹;
  - Pitzer and SIT for concentrated media.
- **Assumptions** [unverified]: point ions in a continuum, linearized Poisson–Boltzmann.

**Kohlrausch and Ostwald dilution** [unverified]
- **Label:** reconstruction from observings (AC conductance) + model construct.
- **Kohlrausch:**
  - Λm = Λ°m − K√c for dilute strong electrolytes;
  - independent ionic migration, Λ°m = Σνλ°;
  - the slope was derived by Debye–Hückel–Onsager.
- **Ostwald dilution (1888):** Ka = α²c/(1 − α), with α = Λm/Λ°m. It holds for weak electrolytes and fails for strong ones.

**Schulze–Hardy rule** [unverified]
- **Label:** reconstruction from observings + model construct (DLVO).
- **Statement:** the critical coagulation concentration falls steeply with counter-ion valence (Schulze 1882; Hardy 1900).
- DLVO gives roughly z⁻⁶ at high surface potential and z⁻² at low potential.
- **Deviations:** specific adsorption and charge reversal by multivalent ions.

**Traube's rule** [unverified]
- **Label:** reconstruction from observings.
- **Statement:** in a homologous series, each added CH2 cuts by about 3× the concentration needed for the same surface-tension lowering (1891).
- **Arithmetic** [inference]: RT·ln 3 ≈ 2.7 kJ mol⁻¹ per CH2 at 298 K.

**Kelvin / Gibbs–Thomson; Ostwald ripening** [unverified]
- **Label:** model construct (curvature thermodynamics) + observing.
- **Kelvin (1871):** ln(p/p∞) = 2γVm/(rRT).
- **Ostwald ripening (1896–1900):** larger particles grow at the expense of smaller ones.
- **LSW theory (1961):** r̄³ ∝ t when diffusion limits the rate.
- **Exceptions:** "digestive" (inverse) ripening when ligands or charge alter the size dependence.

**Pourbaix and Ellingham diagrams** [unverified]
- **Label:** reconstructions from thermochemical data drawn with conventions (standard states, dissolved activity of about 10⁻⁶, per mole O2). Purely thermodynamic, with no kinetics.
- **Pourbaix:** maps of potential against pH (Atlas 1963/1966). A region marked "passive" does not guarantee that the film protects.
- **Ellingham (1944):** ΔG° of oxide formation against T.
  - Slopes equal −ΔS°, with kinks at phase changes.
  - The 2C + O2 → 2CO line has a negative slope, so carbon reduces many oxides at high T.

**Born–Haber cycle and Kapustinskii equation**
- **Born–Haber**
  - **Label:** reconstruction from observings (Hess cycle).
  - **Statement:** published in 1919 by Born, Haber and also Fajans; "Born–Fajans–Haber" is the more accurate name. The lattice enthalpy is derived from the measured formation, sublimation, dissociation, ionization and electron-affinity terms. The basic cycle assumes a fully ionic solid; extended cycles handle covalency ([Born–Haber cycle](https://en.wikipedia.org/wiki/Born%E2%80%93Haber_cycle); doi 10.1038/224950a0).
- **Kapustinskii (1956)** [unverified]
  - **Label:** model construct.
  - **Statement:** estimates lattice energy from ion count, charges and radii without knowing the structure.
  - Gaps between cycle and model values (e.g. for Ag halides) are read as covalency.

### Inferences
- **Cycles.** Hess-type cycles (Born–Haber, Ellingham, Pourbaix) turn measured state-function differences into quantities that cannot be measured directly. The cycle closes because enthalpy and Gibbs energy are state functions; that is a model premise, not an observation.

### Gaps
- Every item marked [unverified] above (blocked fetches). No 2023–26 electrochemical-kinetics developments were checked, e.g. inverted-region electrode kinetics or the IUPAC conventions for the transfer coefficient.

## 5. Photochemistry and spectroscopy rules (Grotthuss–Draper, Stark–Einstein, Beer–Lambert, Kasha, Vavilov, Franck–Condon, Laporte, spin, El-Sayed, Woodward–Fieser)

### Takeaway
Selection rules (Laporte, spin, El-Sayed, Franck–Condon) are model constructs derived from symmetry and the Born–Oppenheimer separation. Each is relaxed by coupling: vibronic, spin–orbit or Herzberg–Teller. Beer–Lambert and Woodward–Fieser are empirical, with stated validity windows. Kasha's rule has a known class of exceptions.

### Cited Findings

**Grotthuss–Draper law** [unverified]
- **Label:** reconstruction from observings.
- **Statement:** only absorbed light causes photochemical change (1817/1842). Absorption is necessary but not sufficient.

**Stark–Einstein law** [unverified]
- **Label:** reconstruction from observings + model construct.
- **Statement:** one absorbed photon produces at most one primary act (1908–12). It is measured as the quantum yield.
- **Exceptions:** multiphoton absorption at high intensity. Chain reactions such as H2 + Cl2 have overall Φ much greater than 1 without breaking the rule for the primary act.

**Beer–Lambert (Bouguer–Beer–Lambert) law**
- **Label:** reconstruction from observings; conventions define absorbance.
- **Statement:** A = εlc (Bouguer 1729; Lambert 1760; Beer 1852, doi 10.1002/andp.18521620505). The modern form dates from about 1913.
- **Validity conditions:**
  - independent absorbers;
  - homogeneous, non-scattering medium;
  - parallel rays with equal path;
  - monochromatic light;
  - no saturation or optical pumping.
- **Deviations:** real, chemical and instrumental. It becomes nonlinear at high concentration (interactions, scattering) and at high intensity. Absorbance of about 0.2–0.5 is the ideal working range.
- **Sources:** [Beer–Lambert law](https://en.wikipedia.org/wiki/Beer%E2%80%93Lambert_law); critical review Mayerhöfer, Pahlow & Popp 2020, doi 10.1002/cphc.202000464. The electromagnetic-theory critique in that review was not checked [unverified].

**Kasha's rule and the Kasha–Vavilov rule** [unverified]
- **Label:** reconstruction from observings.
- **Statement:**
  - Emission comes, in appreciable yield, from the lowest excited state of a given multiplicity (Kasha 1950).
  - The quantum yield does not depend on excitation wavelength (Vavilov, 1920s).
- **Model adds:** internal conversion between upper states is much faster than radiative decay (energy-gap law).
- **Exceptions:** S2 fluorescence of azulene (large S2–S1 gap); some thioketones; "anti-Kasha" photochemistry (review, Chem. Rev. 2017).

**Franck–Condon principle** [unverified]
- **Label:** model construct.
- **Statement:** electronic transitions are vertical, and vibronic band intensities are proportional to squared vibrational overlaps (Franck 1926; Condon 1926–28; Born–Oppenheimer basis).
- **Breakdown:** Herzberg–Teller and other non-Condon effects.

**Laporte and spin selection rules** [unverified]
- **Label:** model construct (symmetry of the dipole operator) + observing (ε values).
- **Statement:**
  - Laporte (1925): in centrosymmetric species, electric-dipole transitions must change parity (g↔u). Octahedral d–d bands are therefore weak, roughly ε 1–100 M⁻¹ cm⁻¹, against about 10²–10³ for tetrahedral complexes.
  - Spin rule: ΔS = 0.
- **Relaxed by:** vibronic coupling, loss of the inversion centre, and spin–orbit coupling (heavy atoms).

**El-Sayed rule** [unverified]
- **Label:** model construct + reconstruction from observings.
- **Statement:** intersystem crossing is fast when the orbital type changes, e.g. ¹(n,π*)→³(π,π*), and slow between ¹(π,π*) and ³(π,π*) (El-Sayed 1963). The reason is that spin–orbit coupling needs a change in orbital angular momentum.
- **Exceptions:** heavy atoms and spin–vibronic coupling (e.g. TADF emitters).

**Woodward–Fieser rules** [unverified]
- **Label:** reconstruction from observings (additive increments) + convention (reference solvent).
- **Statement:** λmax of dienes is predicted from base values plus increments (Woodward 1941–42; Fieser):
  - homoannular base 253 nm, heteroannular or acyclic 214 nm;
  - +30 nm per extending C=C, +5 nm per alkyl or ring residue, +5 nm per exocyclic C=C.
  - Enone bases are about 215 nm (six-membered ring or acyclic).
- **Fails:** for strained or twisted chromophores and for more than four conjugated C=C (Fieser–Kuhn).

### Inferences
- Each spectroscopic selection rule names a forbidden pair of states, and is relaxed by a stated coupling. Its observable content is a band intensity (ε) or a rate, not a yes/no answer.

### Gaps
- Everything here except Beer–Lambert is [unverified] (blocked fetches). No 2023–26 anti-Kasha or El-Sayed-exception primary papers were checked.

## 6. Ordered series (order · measured property · conditions and membership criterion · reversals)

### Takeaway
Every series is a ranking by one measured property, valid for a stated member set and conditions: reference metal, solvent, adsorbent, temperature, contact history. "Series" that look universal (Hofmeister, triboelectric, activity) have the most documented reversals because their measured property bundles several interactions.

### Cited Findings

**Electrochemical series / activity series / galvanic series**
- **Label:** convention (SHE ≡ 0 V, reduction convention) + reconstruction from observings (cell EMFs; only cell potentials can be measured).
- **Values:** F2 +2.87, Cu²⁺/Cu +0.34, H⁺/H2 0, Zn²⁺/Zn −0.76, Li⁺/Li −3.05 V ([Standard electrode potential](https://en.wikipedia.org/wiki/Standard_electrode_potential); doi 10.1351/goldbook.S05912).
- **Conditions:** reversible, near-equilibrium measurement, which is hard to achieve. The values are thermodynamic only.
- **Activity series** [unverified]: roughly Li, K, Ba, Ca, Na, Mg, Al, Zn, Fe, Ni, Sn, Pb, (H), Cu, Ag, Hg, Pt, Au. Observed vigour with water places Li below Na and K despite Li having the most negative E°: kinetics against thermodynamics. Al is passivated by its oxide film.
- **Galvanic series** [unverified]: corrosion potentials in flowing seawater. Stainless steels hold different positions when active or passive. Zn and Fe reverse polarity in hot water above about 60 °C.

**Spectrochemical series**
- **Label:** reconstruction from observings (d–d absorption energies) + model construct.
- **Ligand order:** I⁻ < Br⁻ < S²⁻ < SCN⁻(S) < Cl⁻ < NO3⁻ < N3⁻ < F⁻ < OH⁻ < H2O < C2O4²⁻ < NCS⁻(N) < CH3CN < py < NH3 < en < bipy < phen < NO2⁻(N) < PPh3 < CN⁻ < CO.
- **Metal order:** Mn²⁺ < Ni²⁺ < Co²⁺ < Fe²⁺ < V²⁺ < Fe³⁺ < Cr³⁺ < V³⁺ < Co³⁺. Δ rises with oxidation state and down a group.
- **Origin:** Tsuchida (1938), from absorption spectra of Co complexes ([Spectrochemical series](https://en.wikipedia.org/wiki/Spectrochemical_series); doi 10.1246/bcsj.13.388).
- **Model adds:** σ-donor, π-donor and π-acceptor classes. The order is roughly the reverse of what point-charge crystal-field theory expects.
- **Caveat:** whether a ligand is strong- or weak-field cannot be predicted generally for every metal.

**Nephelauxetic series**
- **Label:** reconstruction from observings (reduction of the Racah B parameter in the complex) + model construct (covalency, cloud expansion).
- **Origin:** Schäffer & Jørgensen 1958 (doi 10.1016/0022-1902(58)80176-1).
- **Relation to the spectrochemical series:** partly parallel, but Cl⁻, Br⁻ and I⁻ sit in very different positions ([Nephelauxetic effect](https://en.wikipedia.org/wiki/Nephelauxetic_effect)).
- **Approximate ligand order** [unverified]: F⁻ < H2O < NH3 < en ≈ ox < NCS⁻ < Cl⁻ ≈ CN⁻ < Br⁻ < I⁻.
- β = B(complex)/B(free ion) [unverified convention].

**Trans-effect series**
- **Label:** reconstruction from observings (substitution rates and product distributions at square-planar Pt(II)) + model construct.
- **Order:** F⁻, H2O, OH⁻ < NH3 < py < Cl⁻ < Br⁻ < I⁻, SCN⁻, NO2⁻, SC(NH2)2, Ph⁻ < SO3²⁻ < PR3, AsR3, SR2, CH3⁻ < H⁻, NO, CO, CN⁻, C2H4.
- **Origin:** Chernyaev 1926.
- **Trans effect vs trans influence:** the kinetic trans effect differs from the ground-state trans influence. A hydride, for example, lengthens the bond trans to it by up to 0.2 Å (X-ray).
- **Model adds:** π-acidity stabilizing the trigonal-bipyramidal intermediate.
- **Caveat:** terminology is not uniform.
- **Use:** cisplatin synthesis exploits the order.
- **Source:** [Trans effect](https://en.wikipedia.org/wiki/Trans_effect); doi 10.1016/S0010-8545(99)00184-8.

**Irving–Williams series**
- **Label:** reconstruction from observings (stability constants for replacing aqua ligands) + model construct.
- **Order:** Mn(II) < Fe(II) < Co(II) < Ni(II) < Cu(II) > Zn(II). It is almost independent of the ligand.
- **Explanations:** ionic radius, CFSE (maximum at Ni) and Jahn–Teller stabilization (Cu). None fully accounts for the series.
- **2022 override:** a designed protein binds other metals over Cu ([Irving–Williams series](https://en.wikipedia.org/wiki/Irving%E2%80%93Williams_series); doi 10.1039/JR9530003192; Choi & Tezcan, Nature 2022, doi 10.1038/s41586-022-04469-8).

**Hofmeister series**
- **Label:** reconstruction from observings (salt effects on protein solubility, Hofmeister 1888, doi 10.1007/bf01918191) + contested model constructs.
- **Typical order** [unverified]:
  - anions: SO4²⁻ > HPO4²⁻ > F⁻ > Cl⁻ > Br⁻ > NO3⁻ > I⁻ > ClO4⁻ > SCN⁻;
  - cations: roughly NH4⁺ > K⁺ > Na⁺ > Li⁺ > Mg²⁺ > Ca²⁺ > guanidinium.
- **Model status** ([Hofmeister series](https://en.wikipedia.org/wiki/Hofmeister_series)):
  - the "water-structure" (kosmotrope/chaotrope) explanation is weakened;
  - direct ion–protein and ion–surface binding, solvation energetics and electrostatic potential (Gregory et al. 2021, doi 10.1039/D1SC03568A) are favoured;
  - the mechanism remains unclear.
- **Reversals:**
  - lysozyme at low salt, where electrostatics dominate (Zhang & Cremer 2009, doi 10.1073/pnas.0907616106);
  - carboxylate surfaces, depending on pH (Schwierz et al. 2015, doi 10.1021/la503813d);
  - surface charge and polarity ("Reversed anionic Hofmeister series", Schwierz, Horinek & Netz, Langmuir 2010, 26, 7370; [record](https://www.physik.fu-berlin.de/en/einrichtungen/ag/ag-netz/Publications/schwierz_2010/index.html), title only);
  - NH4⁺ against alkylated ammonium ([title seen](https://asep.lib.cas.cz/arl-cav/en/detail-cav_un_epca-0347167-Reversal-of-Hofmeister-Ordering-for-Pairing-of-NH4-vs-Alkylated-Ammonium-Cations-with-Halide-Anions)).

**Eluotropic series**
- **Label:** reconstruction from observings (elution strength), relative to a fixed adsorbent and analyte.
- **Order on polar (normal-phase) adsorbents:** hexane/pentane < cyclohexane < benzene < CH2Cl2 < CHCl3 < ether < EtOAc < acetone < MeOH < EtOH < pyridine < AcOH < water ([Eluotropic series](https://en.wikipedia.org/wiki/Eluotropic_series)).
- **Reversal** [unverified]: roughly inverted in reversed phase. Snyder's ε° scale differs between silica and alumina.

**Triboelectric series**
- **Label:** observing + model construct + simulation.
- **Classic series:** materials ranked by the sign of charge acquired on contact. Irreproducibility is long known [unverified history].
- **2025 finding** ([Sobarzo et al., Nature 2025, 638, 664](https://ideas.repec.org/a/nat/nature/v638y2025i8051d10.1038_s41586-024-08530-6.html); doi 10.1038/s41586-024-08530-6):
  - Nominally identical insulating samples first exchanged charge randomly and intransitively.
  - With repeated contacts they spontaneously ordered into a series: samples with more contacts charged negative.
  - A minimal "contact bias" model reproduced this, and the authors could impose a series of their choosing.
  - Surface analysis showed only nanoscale morphological changes, pointing to a mechanically coupled mechanism.
- **Standing 2026:** order is partly a property of contact history, not only of the material.

**Bowen's reaction series** [unverified]
- **Label:** observing (melt crystallization experiments) + reconstruction from observings (an idealized sequence).
- **Discontinuous branch:** olivine → pyroxene → amphibole → biotite.
- **Continuous branch:** Ca- → Na-plagioclase.
- **Then:** K-feldspar → muscovite → quartz.
- **Conditions:** falling T in a basaltic melt under fractional crystallization. Pressure, H2O and composition change the sequence, and real magmas often depart from it.

**Goldich dissolution (weathering-stability) series** [unverified]
- **Label:** reconstruction from observings (weathering profiles, Goldich 1938).
- **Order of increasing stability:** olivine < pyroxene < amphibole < biotite; Ca- < Na-plagioclase; then K-feldspar < muscovite < quartz. This roughly reverses Bowen's order.
- **Caveats:** laboratory dissolution rates and climate can reorder parts of it.

**Nucleophilicity orders**
- **Label:** reconstruction from observings (rates) + conventions (scales).
- **Halides:** in protic solvents I⁻ > Br⁻ > Cl⁻ > F⁻; the order reverses in polar aprotic solvents.
- **Kinetic vs thermodynamic:** nucleophilicity is kinetic and basicity thermodynamic. They track each other for the same attacking atom.
- **Special cases:**
  - ambident nucleophiles such as SCN⁻;
  - "supernucleophiles" such as Ph3Sn⁻, about 10⁴ × I⁻ toward MeI;
  - α-effect nucleophiles.
- **Source:** [Nucleophile](https://en.wikipedia.org/wiki/Nucleophile); doi 10.1002/chem.200500639.

**Leaving-group (nucleofuge) order**
- **Label:** reconstruction from observings (relative rate constants k_X/k_Br).
- **Approximate order:** N2⁺ > dialkyl ether > triflate > I⁻ > tosylate/mesylate > Br⁻ > H2O/ROH > Cl⁻ > nitrate/phosphate > thioethers > amines > F⁻ > carboxylate > phenoxide > HO⁻/RO⁻ > amide > hydride > alkanide.
- **Correlation:** with conjugate-acid pKa, but imperfectly.
- **Reversals:**
  - SNAr: F fastest, because addition is rate-limiting;
  - Friedel–Crafts: RF > RCl > RBr > RI;
  - the order depends on the nucleophile (ethoxide favours tosylate; thiocresolate favours I and Br);
  - and on the mechanism (E1cB vs E2).
- **Source:** [Leaving group](https://en.wikipedia.org/wiki/Leaving_group); doi 10.1351/goldbook.L03493.

**Ostwald's step rule (a sequence of phases)** [unverified]
- **Label:** reconstruction from observings.
- **Statement:** the first phase to crystallize is often a metastable one nearer in free energy to the parent. It then transforms stepwise toward the stable phase (Ostwald 1897).
- **Examples:** CaCO3 (ACC → vaterite → calcite); anatase before rutile.
- **Explanations:** lower interfacial energy lowers the nucleation barrier; size-dependent stability crossovers.
- **Status:** an empirical tendency with many exceptions.

### Inferences
- **Membership criteria.** Each series has an explicit criterion: ligands at a fixed metal (spectrochemical), M(II) aqua complexes (Irving–Williams), Pt(II) square-planar complexes (trans effect), solvents on one adsorbent (eluotropic). Where the criterion is loose (Hofmeister: "salt effects" on any solute or surface), reversals are common.
- **A mirrored pair.** Bowen's and Goldich's series run in near-opposite orders over the same mineral set: one is a crystallization order, the other a stability order at the surface.

### Gaps
- Hofmeister ion lists, the activity and galvanic series, Bowen, Goldich and Ostwald's step rule were not verified (blocked fetches).
- No 2023–26 Hofmeister mechanism papers were checked. Seen by title only: [Murdoch lysozyme reversal](https://researchportal.murdoch.edu.au/esploro/outputs/journalArticle/Hofmeister-series-reversal-for-lysozyme-by/991005543366207891) and [ANU "present state of affairs"](https://researchportalplus.anu.edu.au/en/publications/the-present-state-of-affairs-with-hofmeister-effects/).

## 7. Which rules break, and where

### Takeaway
Breaks fall into four kinds:
- a precondition is violated (Curtin–Hammett, Michaelis–Menten, Debye–Hückel, Nernst at low concentration);
- the rule was worded loosely (Le Chatelier, reactivity–selectivity principle);
- a linear model meets the curvature of the real surface (Marcus inverted region, Hammett/Brønsted curvature, Lindemann fall-off);
- external fields or history create new conditions (force on Woodward–Hoffmann, contact history in triboelectric charging).

### Cited Findings
- **Hammond → anti-Hammond.** Perpendicular structural changes move the transition state opposite to Hammond's prediction ([IUPAC provisional 2021](https://iupac.org/wp-content/uploads/2021/05/PAC-REC-18-10-10.R6_PR20210507.pdf); [Gold Book M04030](https://goldbook.iupac.org/terms/view/A00395)).
- **Curtin–Hammett.** Fails for conformer-specific tunnelling when the interconversion barrier is high ([Nat. Chem. 2017](https://www.nature.com/articles/nchem.2609)).
- **Le Chatelier.** Fails for constant-P reactant addition with Δn ≠ 0, inert-gas addition, finite changes ([Cheung 2009](https://www.ifi.unicamp.br/~mtamash/f320_termo/jchemeduc86_514.pdf)) and mole fractions above a/|Δν| ([Solaz-Portolés & Sanjosé 2013](https://journals.azbuki.bg/science/chemical-reactions-do-not-always-moderate-changes-in-concentration-of-an-active-component/view)).
  - My own Q-versus-K check: for N2 + 3H2 ⇌ 2NH3 at constant T and P, d ln Q/dn(N2) ∝ (2 − 1/x_N2). So adding N2 when x(N2) > ½ drives the reaction back toward N2 [inference, consistent with Cheung].
- **Marcus inverted region.** Rate falls once −ΔG° > λ; confirmed intramolecularly in 1988 ([Roussel slides](https://people.uleth.ca/~roussel/C4000foundations/slides/21etransfer.pdf)). This breaks naive linear free-energy extrapolation, not Marcus theory.
- **Scaling relations.** Breaking them is required but not sufficient ([Govindarajan 2018](https://dare.uva.nl/id/e22fe4be-d8ae-4d49-b249-f943677063c3)).
- **Polanyi rules.** Violated by OH + C2H6, F + H2O, OH + H2S and Cl + CHD3 ([Czakó 2024](https://www.staff.u-szeged.hu/~pappdo/PCCP25_Persp_2024.pdf)).
- **Woodward–Hoffmann.** Forbidden paths are reached under force ([Wang 2015](https://www.nature.com/articles/nchem.2185); [Germann & Meisner 2025](https://pubs.rsc.org/en/content/articlehtml/2025/sc/d5sc04954g)), and through strain, diradicals or asynchronous paths ([WH page](https://en.wikipedia.org/wiki/Woodward%E2%80%93Hoffmann_rules)).
- **Reactivity–selectivity principle.** Obsolete ([RSP page](https://en.wikipedia.org/wiki/Reactivity%E2%80%93selectivity_principle)).
- **Hammett.** Fails for ortho substituents and gives curved plots when mechanism changes ([Hammett page](https://en.wikipedia.org/wiki/Hammett_equation)).
- **Arrhenius.** Super-Arrhenius behaviour in glass-formers ([Arrhenius page](https://en.wikipedia.org/wiki/Arrhenius_equation)).
- **Lindemann.** Curved reciprocal plots ([Lindemann page](https://en.wikipedia.org/wiki/Lindemann_mechanism)).
- **Michaelis–Menten.** Fails under crowding and with multiple substrates ([MM page](https://en.wikipedia.org/wiki/Michaelis%E2%80%93Menten_kinetics)).
- **Langmuir.** Fails for heterogeneous surfaces and multilayers ([Langmuir page](https://en.wikipedia.org/wiki/Langmuir_adsorption_model)).
- **Beer–Lambert.** Fails at high concentration, with scattering and at high intensity ([Beer–Lambert page](https://en.wikipedia.org/wiki/Beer%E2%80%93Lambert_law)).
- **Nernst.** Unpoised at low concentration; formal potentials depend on the medium ([Nernst page](https://en.wikipedia.org/wiki/Nernst_equation)).
- **Debye–Hückel.** Dilute solutions only ([DH page](https://en.wikipedia.org/wiki/Debye%E2%80%93H%C3%BCckel_equation)).
- **Definite proportions.** Fails for berthollides such as wüstite ([page](https://en.wikipedia.org/wiki/Law_of_definite_proportions)).
- **Conservation of mass.** Holds only in the classical limit ([page](https://en.wikipedia.org/wiki/Conservation_of_mass)).
- **Series reversals:**
  - Hofmeister ([page](https://en.wikipedia.org/wiki/Hofmeister_series));
  - leaving groups in SNAr and Friedel–Crafts ([page](https://en.wikipedia.org/wiki/Leaving_group));
  - halide nucleophilicity between protic and aprotic solvents ([page](https://en.wikipedia.org/wiki/Nucleophile));
  - Irving–Williams overridden by design ([page](https://en.wikipedia.org/wiki/Irving%E2%80%93Williams_series));
  - triboelectric order set by history ([Nature 2025](https://ideas.repec.org/a/nat/nature/v638y2025i8051d10.1038_s41586-024-08530-6.html)).
- **Explanation revised, prediction unchanged.** The Felkin–Anh origin was reassigned from Pauli repulsion to strain ([Chem. Sci. 2024](https://docta.ucm.es/entities/publication/04d418de-0d2c-46e1-9c15-fca4f111d3d6/full)); the Hofmeister water-structure explanation has weakened ([page](https://en.wikipedia.org/wiki/Hofmeister_series)).
- **[unverified] breaks:**
  - Kasha: azulene;
  - Dulong–Petit: light elements, low T;
  - Trouton: H-bonded liquids;
  - Ostwald step rule: direct nucleation of the stable phase;
  - Graham: outside free-molecular flow;
  - Schulze–Hardy: specific adsorption.

### Inferences
- **Which rules are most robust.** Rules stated as theorems with explicit preconditions break only when a precondition fails, and a failure points to the stated condition: Curtin–Hammett, Nernst, phase rule. Heuristics without stated domains break unpredictably: Le Chatelier, RSP, Hofmeister.
- **Settled, reopened, revised** (as of Oct 2026):
  - Settled: the Marcus inverted region (1988).
  - Reopened: triboelectric ordering (2025).
  - Revised, explanation only: Felkin–Anh (2024).
  - Retired: RSP (by about 2006 per Mayr & Ofial).

### Gaps
- No 2023–26 primary sources were checked on: Le Chatelier in non-equilibrium steady states; Kasha exceptions; BET reproducibility; new scaling-relation-breaking catalysts; Hofmeister mechanism.
- This session's web-search budget and hourly fetch limit were exhausted, so every [unverified] entry should be checked in a follow-up.
