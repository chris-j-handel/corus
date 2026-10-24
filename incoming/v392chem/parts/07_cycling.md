# Cycling in chemistry: processes, participants and systems that change and change back

Labels on every finding: **[Obs]** observing (instrument or method, sample, conditions, quantity) · **[Rec]** reconstruction from observings · **[Conv]** convention or definition · **[Mod]** model construct · **[Sim]** simulation. Status tags: *settled*, *reproduced*, *reopened*, *contested*, *prior* (a state of the field older than 2023 that was not re-checked here).

Session note for the writer: the shared web-search budget ran out partway through, and so did the hourly fetch limit. PubMed Central pages were CAPTCHA-gated, and several Wikipedia and primary pages were outside the fetch allowlist. Anything not read in this session is marked [unverified] and kept in the Gaps sections. Where a DOI is given as "inferred", it comes from a manuscript code or file path rather than a publisher record.

## Key gathered points

- **Six senses of "cycle".** Chemistry calls at least six kinds of thing a cycle:
  - catalytic cycles: closed loops of steps that regenerate a catalyst;
  - metabolic and biogeochemical cycles: loops of carriers (oxaloacetate, RuBP, Cl atoms) through which matter flows;
  - accounting cycles over state functions (Hess, Born–Haber, alchemical), which close by definition;
  - engine cycles, which return a working substance but export heat and entropy;
  - recurrence in time (oscillators, modelled as limit cycles);
  - conformational and mechanical cycles (ring flips, pseudorotation, molecular motors), some of them degenerate and some driven.
- **The loop itself is rarely observed.** What is measured are proxies:
  - a turnover number above one;
  - a resting state seen by in-situ IR;
  - O2 yields that repeat every fourth flash;
  - an actin filament seen to rotate;
  - Ce(IV)/Ce(III) colour swings;
  - C¹⁶O¹⁸O coming off labelled ceria;
  - ring distributions measured by NMR.

  The closed diagram, the limit cycle and the "rate-determining states" are reconstructions or models built from these.
- **Formal backbone.** At equilibrium, detailed balance forbids net circulation (Wegscheider 1901; Kolmogorov's loop criterion). The clockwise and counter-clockwise products of rate constants around a loop are equal, which means the equilibrium constants around a closed cycle multiply to one. Net directional cycling requires coupling to reservoirs at different chemical potentials. For molecular machines, Astumian argues that direction is set by kinetic asymmetry, not by a power stroke.
- **Efficiency formalisms assume a steady state.**
  - TON/TOF: under first-order decay, TON = initial TOF × catalyst half-life / ln 2.
  - Energetic span: TOF is set by one TOF-determining transition state and one TOF-determining intermediate.
  - Degree of rate control, with its sum rules.
  - Hill's cycle fluxes.

  A 2025 paper says earlier proofs of the steady-state sum rules were incomplete, and that the sums are not conserved in transients.
- **Oscillating reactions were resisted at first.** Bray's (1921) and Belousov's (1951, published 1959) oscillators met resistance partly because oscillation about equilibrium would breach the second law. The accepted resolution: intermediates oscillate far from equilibrium while Gibbs energy keeps falling, and a closed system eventually stops.
- **Developments in 2023–2026.**
  - XFEL crystallography and time-resolved FTIR (2023) resolved photosystem II's S3→S0 step, with O2 onset near 1.2 ms.
  - A nitrogenase variant trapped the E4 "Janus" state.
  - Carbodiimide-fuelled cycles reached about 98% selectivity (2023).
  - The 2023 ozone assessment projects a return to 1980 levels around 2040 (most latitudes), 2045 (Arctic) and 2066 (Antarctic).
- **What returns and what does not.**
  - Returns: catalysts, carriers and conformers.
  - Does not return: fuel-derived waste (ureas, CO2, dibenzofulvene), side products (N-acylurea, Pd black, propionic acid), heat and entropy.
  - Interval per cycle: from about 10⁻⁵ s (cyclohexane ring flip) and microseconds (carbonic anhydrase turnover), through minutes (BZ oscillations), to years (stratospheric chlorine).

## 1. Catalytic cycles: kinds, how they are established, and their formalisms

### Takeaway
"Catalytic cycle" is a field convention: a loop of steps in which the catalyst is regenerated. What is observed is product per catalyst, resting-state spectra, isotope distributions and rate laws. The loop, its rate-controlling states and its efficiency figures are reconstructions or models. These are steady-state constructs, and 2025 work refined their sum rules.

### Cited Findings

**1a. The convention**
- [Conv] A catalytic cycle is a multistep mechanism in which the catalyst is regenerated, which is why it is drawn as a loop.
  - The first step is reactant binding; the last is product release and regeneration.
  - A cycle need not be a full mechanism: intermediates can be detected without the elementary steps being known.
  - Precatalysts must first be activated (e.g., TiCl3 by organoaluminium compounds).
  - "Sacrificial" catalysts that are consumed stoichiometrically are better named for their real role (e.g., reductant).
  — [Catalytic cycle, Wikipedia](https://en.wikipedia.org/wiki/Catalytic_cycle)
- [Conv] Reductive elimination is often the step that forms the product and regenerates the catalyst.
  - It is the microscopic reverse of oxidative addition and lowers the metal's oxidation state by two.
  - The two groups eliminated must be cis.
  - In Heck and Wacker chemistry, the product leaves by β-hydride elimination; reductive elimination then only regenerates the catalyst.
  — [Reductive elimination, Wikipedia](https://en.wikipedia.org/wiki/Reductive_elimination)

**1b. Homogeneous cycles**
- **Pd cross-coupling [Mod]**
  - The generic loop is oxidative addition of RX to LnM, then transmetalation of R′, then reductive elimination of R–R′, which regenerates LnM.
  - Nobel Prize 2010: Heck, Negishi, Suzuki — [Cross-coupling, Wikipedia](https://en.wikipedia.org/wiki/Cross-coupling_reaction).
  - Heck version:
    - Pd(OAc)2 is reduced in situ to Pd(0) by PPh3, which leaves as phosphine oxide (a sacrificial activation).
    - Steps: oxidative addition, syn migratory insertion, β-H elimination, then removal of HX by base.
    - The base is consumed stoichiometrically.
    - History: Mizoroki 1971 (120 °C autoclave); Heck 1972 (1 mol% Pd) — [Heck reaction, Wikipedia](https://en.wikipedia.org/wiki/Heck_reaction).
- **Wacker oxidation [Obs + Mod; *contested*, *prior*]**
  - Observed:
    - Aqueous PdCl2/CuCl2 converts ethylene and O2 to acetaldehyde in about 95% yield.
    - One-stage process: ~130 °C, 400 kPa. Two-stage: 105–110 °C, 900–1000 kPa. Developed 1956–1960.
    - Without CuCl2, Pd(0) precipitates after one turn. The Pd loop therefore closes only through nested Cu(II)/Cu(I) and Cu/O2 loops.
  - Isotope observations:
    - C2D4 in H2O gives CD3CDO; C2H4 in D2O gives CH3CHO, so no hydrogen exchanges with solvent.
    - kH/kD = 1.07 with perdeuterated reactants.
    - Competitive KIE with C2H2D2 ≈ 1.9.
    - Syn addition below 1 M Cl⁻, anti above 3 M Cl⁻.
    — [Wacker process, Wikipedia](https://en.wikipedia.org/wiki/Wacker_process)
  - Interpretation (Stirling, Nair, Lledós, Ujaque tutorial review, 2014 author version):
    - Experiments establish anti addition at high [Cl⁻]; the low-[Cl⁻] case remains disputed.
    - [Sim] Ab initio MD favours outer-sphere attack (~75 kJ/mol) and gives a path barrier of 90 kJ/mol against 94 kJ/mol measured.
    - The review gives the dideuterioethene ratio as 1.70, not 1.9 — a discrepancy with Wikipedia.
    — [Stirling et al., Chem. Soc. Rev. (DOI inferred 10.1039/C3CS60469A)](https://pubs.rsc.org/en/content/getauthorversionpdf/c3cs60469a)
- **Monsanto and Cativa methanol carbonylation [Obs + Mod]**
  - Monsanto (Rh):
    - Conditions: 150–200 °C, 30–60 atm; selectivity >99%; active species cis-[Rh(CO)2I2]⁻.
    - Loop: MeI oxidative addition → methyl migration → CO coordination → reductive elimination of CH3COI → hydrolysis to AcOH + HI.
    - HI turns MeOH back into MeI, closing a second, organic-iodide loop.
    - Rate is first order in MeI and in Rh; oxidative addition is rate-determining.
    — [Monsanto process, Wikipedia](https://en.wikipedia.org/wiki/Monsanto_process)
  - Cativa (Ir/Ru, BP): active species [Ir(CO)2I2]⁻; needs less water; less propionic acid; water–gas shift suppressed — [Cativa process, Wikipedia](https://en.wikipedia.org/wiki/Cativa_process).
  - [Obs] In-situ IR (Haynes et al. 2004):
    - The resting state is fac,cis-[Ir(CO)2I3Me]⁻ when water is ≥5% w/w.
    - Ru, W, Re and Os carbonyls and Zn, Cd, Hg, Ga and In iodides speed up methyl migration by abstracting iodide.
    - Neutral [Ir(CO)3I2Me] inserts about 700× faster than the anion (85 °C, PhCl), equivalent to ΔG‡ 20 kJ/mol lower.
    - Iodide salts poison the catalyst.
    — [Haynes et al., JACS 2004, doi:10.1021/ja039464y](https://acs.figshare.com/collections/Promotion_of_Iridium_Catalyzed_Methanol_Carbonylation_Mechanistic_Studies_of_the_Cativa_Process/3236929)
- **Hydroformylation [Obs/Conv]**
  - Discovered by Roelen in 1938; world capacity 6.6 Mt/yr (1995); 10–100 atm, 40–200 °C.
  - The Heck–Breslow mechanism (1960s) for HCo(CO)4 describes alkene insertion into M–H and CO migratory insertion, with β-H elimination competing. The page lists no spectroscopically observed intermediates.
  - Ruhrchemie/Rhône-Poulenc Rh process: linear:branched aldehyde 96:4; Rh loss <1 ppb per batch.
  — [Hydroformylation, Wikipedia](https://en.wikipedia.org/wiki/Hydroformylation)
- **Ziegler–Natta / Cossee–Arlman [Mod; *reproduced* in new systems]**
  - Cossee and Arlman (1964): a vacant site takes up monomer, migratory insertion follows, and the two sides alternate many times per chain; the coordination environment sets stereoregularity — [Cossee–Arlman, Wikipedia](https://en.wikipedia.org/wiki/Cossee%E2%80%93Arlman_mechanism).
  - [Obs] 2021, Ga³⁺ and Zn²⁺ single sites on SiO2:
    - IR and XAS showed ethylene inserting into Ga–H.
    - HD formed at 0.65 mol per mol Ga (250 °C).
    - Butene selectivity 76% (Ga), ~86% (Zn).
  - [Sim] DFT insertion barriers 1.47–2.06 eV.
  — [LiBretto et al., Nat. Commun. 12:2322 (2021)](https://doi.org/10.1038/s41467-021-22512-6)
- **Olefin metathesis [Obs → Mod; *settled*]**
  - Calderon's 1967 quasi-cyclobutane proposal was rejected: metathesis gives no cyclobutanes, and catalysts do not open cyclobutanes.
  - Chauvin and Hérisson (1971) proposed the metal-alkylidene/metallacyclobutane loop.
    - The decisive observation: cyclopentene plus 2-pentene gave C9:C10:C11 dienes in a 1:2:1 ratio.
  - Supporting work:
    - Grubbs isolated titanacyclobutanes, which are slow catalysts.
    - Schrock made the first stable alkylidene (Ta, 1974); in 1980 a Ta alkylidene metathesized cis-2-pentene.
  - Numbers:
    - W alkylidyne: several hundred turnovers per minute.
    - Hoveyda–Grubbs catalyst in water: TON up to 390.
    - Re/SiO2: 0.25 mol per mol Re per second at 25 °C.
    - Methyl oleate self-metathesis: TON 900.
  — [Astruc, New J. Chem. 2005 (DOI inferred 10.1039/B412198H)](https://pubs.rsc.org/en/content/articlehtml/2005/nj/b412198h)

**1c. Heterogeneous cycles**
- [Conv/Mod] Surface mechanisms and catalyst design
  - Langmuir–Hinshelwood: both reactants adsorb, react on the surface, and the product desorbs. Said to describe most heterogeneous reactions.
  - Eley–Rideal: an adsorbed species reacts directly with a gas-phase partner.
  - The Sabatier principle (intermediate binding strength), scaling relations and microkinetic modelling produce volcano plots, which are model-derived.
  - Catalysts deactivate by sintering, poisoning (e.g., S on Cu/ZnO) and coking.
  - Scale: Haber–Bosch made 144 Mt NH3 in 2016, using about 1% of world industrial energy.
  — [Heterogeneous catalysis, Wikipedia](https://en.wikipedia.org/wiki/Heterogeneous_catalysis)
- [Obs → Rec] Mars–van Krevelen read from isotopes (¹⁸O-enriched ceria, CO oxidation)
  - TG-MS shows lattice ¹⁸O exchange above ~400 °C.
  - The Raman F2g shift starts at ~400 °C for 9 nm grains and ~550 °C for 81 nm grains.
  - Pulsing ¹⁶O2 into CO/He gives C¹⁶O¹⁸O, so lattice oxygen is consumed and refilled.
  - About two unit cells (~30% of the oxygen in a 9 nm grain) take part.
  - Pt/CeO2 gives no C¹⁶O¹⁸O below 250 °C. The authors read this as Langmuir–Hinshelwood at low temperature, shifting toward Mars–van Krevelen above it.
  — [Penkala et al., Catal. Sci. Technol. (manuscript C5CY00842E)](https://pubs.rsc.org/en/content/getauthorversionpdf/C5CY00842E)
- An electrocatalytic analogue appears in the title "Evidence of Mars-van-Krevelen mechanism in the electrochemical oxygen evolution on Ni-based catalysts" (seen only as a search result; content [unverified]) — [PMC8251801](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8251801/)

**1d. Enzymatic cycles**
- [Mod/Conv] Michaelis–Menten
  - Scheme: E + S ⇌ ES → E + P, with E regenerated.
  - History: Henri 1902; Michaelis & Menten 1913 (invertase); Briggs–Haldane 1925 (steady state).
  - Rate law: v = kcat[E]0[S]/(KM+[S]).
  - kcat is the turnover number: the maximum number of substrate molecules converted per enzyme per unit time.
  - [Obs] What is measured is initial rates against [S].
  - Values:
    - Carbonic anhydrase: kcat 4.0×10⁵ s⁻¹, KM 2.6×10⁻² M.
    - Fumarase: kcat 8.0×10² s⁻¹, kcat/KM 1.6×10⁸ M⁻¹s⁻¹.
    - The diffusion limit is 10⁸–10¹⁰ M⁻¹s⁻¹.
  — [Michaelis–Menten kinetics, Wikipedia](https://en.wikipedia.org/wiki/Michaelis–Menten_kinetics)
- [Obs → Mod] Ping-pong (substituted-enzyme) mechanism
  - The first substrate converts E to E* and leaves; the second substrate restores E.
  - Diagnostic: parallel lines in double-reciprocal plots (ternary-complex mechanisms give intersecting lines).
  - The amplitude of the pre-steady-state "burst" equals one turnover per active enzyme.
  — [Enzyme kinetics, Wikipedia](https://en.wikipedia.org/wiki/Enzyme_kinetics)

**1e. How a cycle is established experimentally**
- [Obs] Resting states seen by in-situ spectroscopy (Cativa, above).
- [Obs] Off-cycle sinks that do not return:
  - Pd(0) precipitate in the Wacker process without Cu.
  - Iodide poisoning in Cativa.
  - N-acylurea in carbodiimide cycles (§5).
- [Obs] Intermediates trapped by freeze-quench EPR/ENDOR (nitrogenase, §2).
- [Obs/Conv] Kinetic isotope effects
  - Primary KIEs are large when a bond to the isotope is broken in the rate-limiting or product-determining step. Secondary KIEs are about 1.1–1.2.
  - Semiclassically, kH/kD rarely exceeds about 7–8 near room temperature; larger values point to tunnelling.
  - Of the three experiment designs (parallel rates, intermolecular competition, intramolecular competition), only parallel rates isolate the rate-determining step.
  — [Kinetic isotope effect, Wikipedia](https://en.wikipedia.org/wiki/Kinetic_isotope_effect)

**1f. Formalisms**
- **TON/TOF [Conv]**
  - Kozuch & Martin's 2012 analysis of "turning over" definitions (ACS Catal. 2:2787) — [record](https://cris.iucc.ac.il/en/publications/turning-over-definitions-in-catalytic-cycles/); [doi:10.1021/cs3005264](https://doi.org/10.1021/cs3005264). The abstract was not seen.
  - Steven (2025):
    - TOF(t) = (1/[Cat](t))·d[P]/dt; TOF0 is the initial value.
    - TON = ∫TOF dt; under first-order deactivation, TON = TOF0·t½/ln 2.
    - Both are meaningful mainly in the initial-rate region and should be compared only under like conditions.
    — [Front. Catal. 2025, doi:10.3389/fctls.2025.1720991](https://public-pages-files-2025.frontiersin.org/journals/catalysis/articles/10.3389/fctls.2025.1720991/pdf)
  - An unattributed page gives typical ranges: industrial TOF 10⁻²–10² s⁻¹, enzymes 10³–10⁷ s⁻¹, organometallic TON 10²–10⁶. Low reliability — [TOF.pdf](https://korobov.chem.msu.ru/uploads/TOF.pdf).
- **Energetic span [Mod]** (Kozuch & Shaik, Acc. Chem. Res. 44:101, 2011)
  - Computes TOF from a computed energy profile, at steady state.
  - Treats TOF like a current (Ohm's-law analogy).
  - A TOF-determining transition state (TDTS) and a TOF-determining intermediate (TDI) are identified by their degree of TOF control.
  - δE = E(TDTS) − E(TDI), plus the reaction energy if the TDTS comes before the TDI. TOF then takes an Eyring form.
  - The TDTS and TDI need not be the highest or lowest states, or adjacent. Only species between them affect the rate.
  - The authors replace "rate-determining step" with "rate-determining states".
  — [CRIS record](https://cris.iucc.ac.il/en/publications/how-to-conceptualize-catalytic-cycles-the-energetic-span-model/)
- **Degree of rate control [Mod; *reopened* 2025]**
  - Stegelmann, Andreasen & Campbell (2009) argue for identifying rate-controlling transition states and intermediates, not a single rate-determining step — [JACS 131:8077, doi:10.1021/ja9000097](https://orbit.dtu.dk/en/publications/degree-of-rate-control-how-much-the-energies-of-intermediates-and/).
  - Jørgensen & Grönbeck (2017):
    - χi = ∂ln r/∂ln ki at fixed Ki, obtained by 1% perturbations.
    - χi = 1 marks the rate-determining step; negative χi marks inhibition.
    - Reaction orders and apparent activation energy are χ-weighted sums.
    - Methane oxidation on Pd(100): CH4 dissociative adsorption dominates control, and the CH4 order rises from ~0 to ~1 with temperature.
    — [Catal. Sci. Technol. 7:4034, doi:10.1039/c7cy01246b](https://pubs.rsc.org/en/content/articlepdf/2017/cy/c7cy01246b)
  - Foley & Bhan (2020): kinetic DRCs sum to one, coverages map onto thermodynamic DRCs, and the approach links to De Donder relations — [J. Catal. 384:231, doi:10.1016/j.jcat.2020.02.008](https://experts.umn.edu/en/publications/degree-of-rate-control-and-de-donder-relations-an-interpretation-/).
  - Bamidele et al. (online December 2025):
    - At steady state, kinetic DRCs sum to +1 and thermodynamic DRCs to −1. Their total is zero in transients as well as at steady state.
    - The authors call earlier steady-state proofs incomplete.
    - In transients the separate sums are unbounded, reaching thousands near sign changes.
    - [Sim] Their DFT microkinetic model of ethane hydrogenolysis on Pt(111) (31 steps) underpredicts the measured rate (~0.015 s⁻¹) by about five orders of magnitude.
    — [Chem. Eng. J. 527:171357, doi:10.1016/j.cej.2025.171357](https://www.osti.gov/pages/servlets/purl/3009658)
- **Hill's cycle kinetics [Mod]**
  - Hill (1989) condenses his 1977 *Free Energy Transduction in Biology*.
  - Content: states, diagrams and cycles; thermodynamic forces; operational, cycle and transition fluxes; efficiency and dissipation; the diagram method for steady-state probabilities and cycle fluxes; free-energy levels of states.
  — [Springer, doi:10.1007/978-1-4612-3558-3](https://link.springer.com/book/9780387968360); [1977 listing](https://shop.elsevier.com/books/free-energy-transduction-in-biology/hill/978-0-12-348250-1)
  - Gawthrop & Crampin's transporter analysis:
    - A "loop" pathway transduces; a "slip" pathway changes conformation without transport.
    - Total dissipation is lowest at an intermediate flow.
    - Pathway dissipations can be negative where flows cross, even though the total stays positive.
    — [arXiv 1611.02332](https://arxiv.org/pdf/1611.02332)

### Inferences
- **Each node can be observed; the closure is inferred.** Single nodes are often observings (an IR resting state, an isolated metallacyclobutane). The closure of the loop is usually inferred from TON > 1 plus mass balance; no individual catalyst molecule is followed around.
- **Three distinct notions of "control".**
  - The classical rate-determining step.
  - Rate-determining states (energetic span).
  - Sensitivity (degree of rate control).

  They coincide only in limiting cases, and all three assume a steady state.
- **Membership criterion, in chemistry's own terms.** A species counts as a catalyst if it reappears unchanged after product release and more than one product molecule forms per catalyst. A precatalyst or sacrificial reagent fails this test.
- **Industrial cycles are nested.**
  - Wacker: Pd ← Cu ← O2.
  - Monsanto: Rh plus HI/MeI.
  - Cativa: Ir plus a promoter–iodide shuttle.

  The "catalyst" therefore returns only because other cycles turn alongside it.

### Gaps
- [unverified] Photoredox cycles: oxidative versus reductive quenching, Stern–Volmer studies, quantum yields above 1 indicating chains. Electrocatalytic cycle formalisms (Tafel analysis, foot-of-the-wave analysis). No sources read.
- [unverified] Blackmond's reaction-progress kinetic analysis ("same-excess" and catalyst-deactivation tests). Only vendor webinar pages were found.
- [unverified] The Kozuch–Shaik DOI (expected 10.1021/ar1000956) was not seen. Campbell's 2001 J. Catal. paper and the 2017 ACS Catal. review "The Degree of Rate Control: A Powerful Tool for Catalysis Research" were not read.
- [unverified] Molecular-beam discrimination of Langmuir–Hinshelwood from Eley–Rideal, and Ertl's surface-science cycles, were not read.

## 2. Biochemical, geochemical and atmospheric cycles

### Takeaway
Metabolic cycles regenerate a carrier (oxaloacetate, RuBP) or an enzyme state (S0, E0, a β-subunit conformation) while matter or energy flows through. They are evidenced by isotope tracing, flash-number patterns, single-molecule rotation, freeze-quench spectroscopy and XFEL snapshots. Geochemical cycles are reconstructions of reservoirs and fluxes. Atmospheric catalytic cycles are true chemical cycles, with chain lengths of about 10⁵.

### Cited Findings
- **TCA cycle [Rec; *settled*]**
  - Krebs & Johnson 1937 (pigeon breast muscle); Martius & Knoop the same year.
  - Each turn yields 3 NADH, 1 FADH2, 1 GTP/ATP and 2 CO2, and oxaloacetate is regenerated.
  - The CO2 released in a turn comes from oxaloacetate carbons; the incoming acetyl carbons are lost only over later turns.
  - Anaplerotic inputs (e.g., pyruvate carboxylation) and cataplerotic outputs (citrate exported for lipid synthesis) make the cycle amphibolic.
  - The page cites non-enzymatic analogue work (Keller 2017, persulfate radicals) and a 2025 abiotic-origin study (McAnally et al.).
  — [Citric acid cycle, Wikipedia](https://en.wikipedia.org/wiki/Citric_acid_cycle)
- **Reverse TCA and non-enzymatic analogues [Obs + Mod; *contested*]**
  - Evans, Buchanan & Arnon (1966) described a ferredoxin-dependent reductive cycle.
  - Enzyme replacements: citrate lyase, fumarate reductase, and 2-oxoglutarate:ferredoxin oxidoreductase (used because NADH is too weak a reductant).
  - Organisms: Aquificota, Chlorobaculum tepidum.
  - [Obs] Non-enzymatic results:
    - Muchowska et al. 2017 (Moran group): Fe and other metals promote two- and three-step rTCA sequences, but only under harsh conditions (1 M HCl or H2SO4, 80–140 °C).
    - Muchowska et al. 2019 (Nature): iron-promoted synthesis and breakdown of universal metabolic precursors.
    - Ju et al. 2023: aqueous microdroplets promote C–C bond formation and reductive carboxylation.
  - [Mod] Akbari & Palsson (2023, PNAS): FeS minerals in vents could have catalysed rTCA steps.
  - Critique: Ross (2007) argued that a complete rTCA cycle is untenable without enzymes for kinetic and thermodynamic reasons, and that pyrophosphate cannot drive pyruvate → oxaloacetate.
  — [Reverse Krebs cycle, Wikipedia](https://en.wikipedia.org/wiki/Reverse_Krebs_cycle)
  - [Rec] LUCA's inferred metabolism includes an incomplete reverse Krebs cycle. Intermediates of the Krebs cycle, glycolysis and the pentose phosphate pathway form without enzymes under vent-relevant conditions. No synthesis of sugars, amino acids, nucleotides or fatty acids has been shown under plausible vent conditions. The formose reaction (Butlerov 1861) was proposed to be autocatalytic by Breslow in 1959 — [Abiogenesis, Wikipedia](https://en.wikipedia.org/wiki/Abiogenesis).
- **Carbon fixation [Rec]**
  - Photosynthetic fixation is about 250 Gt CO2/yr, nearly half in the oceans; the Calvin cycle accounts for about 90% of biological fixation.
  - Pathways and costs: Calvin 9 ATP + 6 NADPH per triose phosphate; rTCA about 2 ATP per turn; 3-hydroxypropionate bicycle 10 ATP — [Carbon fixation, Wikipedia](https://en.wikipedia.org/wiki/Carbon_fixation).
  - Calvin cycle: 3 ATP + 2 NADPH per CO2; five of every six triose phosphates regenerate RuBP.
  - Photorespiration (RuBisCO acting as oxygenase) returns only 75% of phosphoglycolate carbon and releases NH3.
  - Global figures: ~130 TW captured and 91–104 Pg C/yr. This conflicts with the ~68 Gt C/yr implied by 250 Gt CO2; the gap is probably gross versus net fixation and is unresolved here.
  - Stage timescales run from femtoseconds (antenna) to seconds (fixation).
  — [Photosynthesis, Wikipedia](https://en.wikipedia.org/wiki/Photosynthesis)
- **Q cycle and proton bookkeeping [Mod]**
  - At complex III, QH2 is oxidized at the Qo site. One electron goes to each of two cytochrome c molecules; the other two electrons re-reduce a quinone at Qi. Net: 4 H⁺ translocated.
  - Complex I translocates 4 H⁺ per 2 e⁻. Complex IV takes up 8 matrix H⁺ but translocates only 4.
  - The human c8 ring implies 8 H⁺ per rotation.
  - Chemiosmosis is described as "proposed" (Mitchell). The details of complex IV pumping are still under study.
  — [Electron transport chain, Wikipedia](https://en.wikipedia.org/wiki/Electron_transport_chain)
- **Kok S-state cycle of PSII water oxidation**
  - [Obs] Flash yields of O2 repeat with period four, from the S-states; acceptor-side signals repeat with period two.
  - [Mod] The Kok model adds "misses" and "double hits". Shinkarev showed that period-two signals do not uniquely identify an acceptor-side origin.
  — [Shinkarev, Photosynth. Res. 48:411 (1996), doi:10.1007/BF00029473](https://link.springer.com/article/10.1007/BF00029473)
  - The cluster is Mn4Ca, and four charge separations are needed per O2 — [Photosynthesis, Wikipedia](https://en.wikipedia.org/wiki/Photosynthesis).
  - [Obs, 2023] Room-temperature XFEL serial crystallography of S3→[S4]→S0:
    - The extra oxygen Ox (inserted at S2→S3) disappears or moves at ~700 μs, as YZ is reduced.
    - The Mn1–Mn4 distance shortens at ~1,200 μs, at the onset of O2 release.
    - Protons leave through the Cl1 channel.
    - [Mod] The authors propose a reduced, possibly peroxide, intermediate before O2 release.
    — [Bhowmick et al., Nature 617:629 (2023), doi:10.1038/s41586-023-06038-z](https://impact.ornl.gov/en/publications/structural-evidence-for-intermediates-during-osub2sub-formation-i/)
  - [Obs + Sim, 2023] Greife et al. combined time-resolved FTIR with quantum chemistry. They report an early deprotonation (Asp61, or Glu65/Glu312) and assign an oxyl-radical character to the S4 intermediate that Kok postulated decades earlier. The two studies are called complementary — [SFB 1078 summary; doi:10.1038/s41586-023-06008-5](https://www.sfb1078.de/news/230504_Nature_Rana-Ali.html). *Reopened/advanced*: how the O–O bond forms is still model-dependent.
- **Nitrogenase Lowe–Thorneley cycle**
  - [Mod] The MoFe protein steps from E0 to E8, gaining one e⁻/H⁺ per Fe-protein delivery.
    - E0→E4 reduces no N2 and consumes about 8 ATP, i.e. about 2 ATP per electron (my derivation).
    - At E4 ("Janus"), the enzyme either binds N2 with reductive elimination of H2 (forward) or loses H2 and relaxes to E2/E0 (backward).
    - At least one H2 is therefore obligatory per N2.
    — [Hickey 2022, How Nitrogenase Works ch. 5](https://wisc.pb.unizin.org/nitrogencycle/?p=28)
  - [Obs] E4(4H) carries two bridging Fe–H–Fe hydrides (EPR/ENDOR).
    - The α-V70I variant suppresses hydride protonation, so E4(4H) accumulates.
    - Wild-type relaxations at −50 °C: ~6 min (E4) and ~330 min (E2).
    - [Sim] MD gives a 40 kJ/mol interconversion barrier and 88:12 conformer populations.
    — [Lukoyanov et al., Faraday Discuss. 243:231 (2023), doi:10.1039/d2fd00153e](https://par.nsf.gov/servlets/purl/10439202)
- **ATP synthase binding-change cycle**
  - [Obs] An actin filament attached to the γ subunit of single F1 molecules rotated anticlockwise (viewed from the membrane side) in ATP, for more than 100 revolutions, with torque above 40 pN·nm — [Noji et al., Nature 386:299 (1997), doi:10.1038/386299a0](https://ideas.repec.org/a/nat/nature/v386y1997i6622d10.1038_386299a0.html).
  - [Mod] Boyer's three postulates:
    - Energy is spent mainly on binding Pi and releasing tightly bound ATP.
    - Three catalytic sites pass sequentially through binding changes.
    - Rotation of an internal subunit drives those changes.

    Nobel 1997 (with Walker; Skou) — [Paul D. Boyer, Wikipedia](https://en.wikipedia.org/wiki/Paul_D._Boyer).
  - [Obs] The F1 crystal structure (Abrahams 1994, 2.8 Å) shows loose, tight and open β-subunit states. Chloroplast enzymes use 4–4.67 H⁺ per ATP — [ATP synthase, Wikipedia](https://en.wikipedia.org/wiki/ATP_synthase).
- **Atmospheric cycles**
  - [Mod/Obs] Chapman (1930): UV splits O2, O + O2 forms O3, and UV splits O3 again.
    - The ozone layer lies at 15–35 km, peaking at 8–15 ppm; about 90% of ozone is stratospheric; compressed to sea-level pressure the column is about 3 mm.
    - The Dobson network was built up between 1928 and 1958.
    — [Ozone layer, Wikipedia](https://en.wikipedia.org/wiki/Ozone_layer)
  - [Mod] Catalytic destruction: Cl + O3 → ClO + O2, then ClO + O → Cl + O2; net O3 + O → 2 O2.
    - OH and NO cycles were identified by Bates & Nicolet in the 1950s; NOx by Crutzen in 1970; CFC chlorine by Molina & Rowland in 1974.
    - Reservoir species are HCl and ClONO2. Polar stratospheric clouds (~−80 °C) convert them back to active Cl.
    - One Cl atom destroys about 10⁵ O3 molecules and stays in the cycle for up to ~2 years.
  - [Obs] Measured losses:
    - Farman et al. 1985: Antarctic spring column down by up to 70%.
    - Arctic 2011: ~80% loss at ~20 km.
    - March 2020: ~90% Arctic drop measured by balloons.
    - September 2023: ~26 million km² Antarctic hole.
  - [Mod] Projections: UN 2023 assessment gives 1980 levels around 2066 (Antarctic), 2045 (Arctic) and 2040 (elsewhere). Renewed CFC-11 emissions since 2013 could delay this by about a decade.
  — [Ozone depletion, Wikipedia](https://en.wikipedia.org/wiki/Ozone_depletion)

### Inferences
- **"Return" can be per turn or per cycle of four or eight.** The carrier returns each turn (oxaloacetate, RuBP). The Kok and Lowe–Thorneley cycles are counted in electrons: four flashes or eight e⁻/H⁺ before the enzyme returns to S0 or E0, with obligatory by-products along the way (O2 and 4 H⁺; H2).
- **Two ways to observe a closed cycle.**
  - Synchronize an ensemble and count the period: flash number gives period four.
  - Watch one molecule: F1 rotation.

  Metabolic cycles are instead reconstructed from labels, stoichiometry and enzyme assays.
- **Atmospheric chlorine is formally a catalyst.** Chain length and residence time play the role of TON and catalyst lifetime, and reservoir species are its resting states.

### Gaps
- [unverified] Urea cycle: Krebs & Henseleit 1932, the first metabolic cycle described; ornithine acted catalytically in liver slices. Not read.
- [unverified] Glyoxylate cycle: Kornberg & Krebs 1957; isocitrate lyase and malate synthase bypass the two TCA decarboxylations. Not read.
- [unverified] Details of the 2019 Moran-group result (glyoxylate + pyruvate + Fe²⁺ giving a network of TCA/rTCA intermediates). Also Springsteen et al. 2018 and Stubbs et al. 2020 on non-enzymatic cycle analogues. Not read.
- [unverified] Bacteriorhodopsin photocycle: all-trans to 13-cis retinal; K, L, M, N and O intermediates; roughly a 10 ms cycle with one proton per photon. Rhodopsin's visual cycle: the bleached chromophore is re-isomerized enzymatically outside the protein. The pages were not fetchable.
- [unverified] Nitrogen, sulfur, phosphorus, oxygen and rock cycles (reservoirs, fluxes, residence times, carbonate–silicate feedback); HOx, NOx and BrOx cycle equations; aircraft measurements of ClO. Not read.

## 3. Thermodynamic and accounting cycles

### Takeaway
Accounting cycles use state functions: the sum around a closed path is zero by definition. They let chemists compute steps that cannot be measured (lattice energies, differences in binding free energy) from steps that can be measured or simulated. Engine cycles return a working substance and export heat and entropy. Little specific material was read in-session here.

### Cited Findings
- [Conv] Heat engines and refrigerators are closed cyclic machines: their internal energy and entropy return each cycle. Entropy produced by irreversibility must therefore leave as heat. The ideal maximum efficiency is the Carnot efficiency, and ambient temperature × entropy production rate is the "dissipated power" — [Entropy production, Wikipedia](https://en.wikipedia.org/wiki/Entropy_production).
- [Conv] ΔG° and K are linked through −RT ln K, and ΔG = 0 at equilibrium — [Gibbs free energy, Wikipedia](https://en.wikipedia.org/wiki/Gibbs_free_energy).
- [Mod] Network models keep the cycle sums consistent by deriving each equilibrium constant from species thermodynamic constants through stoichiometry (Gawthrop & Crampin, eq. 28) — [arXiv 1611.02332](https://arxiv.org/pdf/1611.02332).
- [Mod] The energetic span model treats a catalytic cycle's driving force as a chemical potential and the mechanism as a resistance, so TOF is a current. This is an accounting analogy, not a physical circuit — [Kozuch & Shaik record](https://cris.iucc.ac.il/en/publications/how-to-conceptualize-catalytic-cycles-the-energetic-span-model/).

### Inferences
- **Three different things share the word "cycle" here.**
  - An accounting path (Hess, Born–Haber, alchemical) need never be traversed by any sample. It is pure convention plus measured or simulated legs.
  - An engine or thermochemical cycle is traversed by real matter.
  - A catalytic cycle is traversed by the catalyst while substrate passes through.
- **The state-function identity behind Hess cycles is the same one behind Wegscheider's condition (§7)**, written in ΔG° rather than K.

### Gaps
- [unverified] Hess (1840) and Born–Haber (1919) cycles, e.g. lattice enthalpy from sublimation, ionization, dissociation, electron affinity and formation enthalpy. Carnot (1824) and Stirling (1816, with a regenerator) cycles. Not read.
- [unverified] Sulfur–iodine water-splitting cycle: Bunsen reaction SO2 + I2 + 2H2O → H2SO4 + 2HI near 120 °C; H2SO4 decomposed above ~800 °C; HI decomposed near 450 °C. All reagents except water are recycled. Not read.
- [unverified] Alchemical free-energy cycles: ΔΔG(binding) obtained as ΔG(mutation in complex) − ΔG(mutation in solvent); cycle-closure hysteresis used as an error check. Not read.

## 4. Oscillation and recurrence

### Takeaway
What is observed is periodic colour, potential or absorbance in systems driven far from equilibrium. What is modelled is limit cycles produced by autocatalysis plus delayed negative feedback, beyond an instability threshold. The Brusselator is abstract; the Oregonator is a reduction of the Field–Körös–Noyes mechanism; Lotka's scheme gives neutral closed orbits rather than limit cycles. Oscillators were resisted on second-law grounds until the mid-1960s.

### Cited Findings
- **History and reception [Obs + historical; *settled*]**
  - Earlier oscillators: Fechner 1828 (oscillating current) and Ostwald 1899 (chromium dissolution, heterogeneous). Bray 1921 gave the first homogeneous example. Homogeneous oscillators met extreme scepticism — [Chemical oscillator, Wikipedia](https://en.wikipedia.org/wiki/Chemical_oscillator).
  - Bray's paper (JACS 43:1262) met indifference and some opposition as apparently contrary to the second law. Intensive study began only after Prigogine's group in the mid-1960s. Lotka had published oscillating schemes in 1910 and 1920 — [Cervellati 2022, doi:10.1007/s11144-021-02019-3](https://link.springer.com/doi/10.1007/s11144-021-02019-3).
  - Zhabotinsky's account:
    - Bray's oscillations were blamed on impurities.
    - Belousov saw colour oscillations in 1951; every journal he tried rejected the work, and it appeared in a 1959 institute booklet.
    - Zhabotinsky replaced citric acid with malonic acid, submitted to *Biofizika* in 1962 (published 1964), and showed the reaction is homogeneous.
    - The "Dark Age" ended in the mid-1960s; more than 1,500 BZ papers followed.
    - Oscillation requires operating outside the Onsager (near-equilibrium) domain.
    — [Zhabotinsky & Rossi, Int. J. Ecodynamics 1:324 (2006)](https://www.witpress.com/Secure/ejournals/papers/ECO0104001f.pdf)
  - Wikipedia's version:
    - Belousov was looking for an inorganic analogue of the Krebs cycle.
    - Two attempts were rejected (contrast "every journal" above).
    - The West learned of the work at a 1968 Prague meeting.
    — [BZ reaction, Wikipedia](https://en.wikipedia.org/wiki/Belousov%E2%80%93Zhabotinsky_reaction)
  - One editor judged the result impossible. A closed system cannot oscillate indefinitely because reagents are used up — [Straub, BU notes](https://people.bu.edu/straub/courses/demomaster/belousov.html).
- **Thermodynamic resolution [Conv/Mod]**
  - No system can oscillate about its final equilibrium. In a closed system at constant T and p, G must fall continuously, but intermediate concentrations and rates may still oscillate — [Chemical oscillator, Wikipedia](https://en.wikipedia.org/wiki/Chemical_oscillator).
  - Far from equilibrium, the near-equilibrium Lyapunov guarantee no longer holds. Autocatalysis beyond a threshold (a Hopf bifurcation) gives oscillation, and reaction–diffusion coupling gives spatial order (Prigogine, Nobel 1977) — [Dissipative structure, Wikipedia](https://en.wikipedia.org/wiki/Dissipative_structure).
  - There is no general extremal (minimum entropy production) principle far from equilibrium — [Non-equilibrium thermodynamics, Wikipedia](https://en.wikipedia.org/wiki/Non-equilibrium_thermodynamics).
- **BZ reaction [Obs]**
  - The Ce(IV)/Ce(III) ratio oscillates, so the solution alternates yellow and colourless.
  - Overall: 3 CH2(COOH)2 + 4 BrO3⁻ → 4 Br⁻ + 9 CO2 + 6 H2O.
  - The timescale is minutes. In dishes, the reaction forms rings and spirals that persist until reagents are spent — [BZ reaction, Wikipedia](https://en.wikipedia.org/wiki/Belousov%E2%80%93Zhabotinsky_reaction).
  - Mn variant: red and colourless phases, with visible CO2 evolution — [Straub](https://people.bu.edu/straub/courses/demomaster/belousov.html).
- **Briggs–Rauscher [Obs + Mod]**
  - Briggs & Rauscher, 1973 (Galileo High School, San Francisco).
  - Reagents: H2O2, iodate, Mn²⁺, acid, malonic acid and starch.
  - Colour sequence: colourless → amber → dark blue → colourless. Typical recipes give about 10 oscillations; dilute ones give more than 40 in 8 min.
  - An Ag/AgI electrode shows iodide swinging over several orders of magnitude.
  - [Mod] Mechanism: a non-radical process A and an autocatalytic radical process B.
  - Approximate net: IO3⁻ + 2H2O2 + CH2(COOH)2 + H⁺ → ICH(COOH)2 + 2O2 + 3H2O. Oscillation stops when the reagents are spent.
  — [BR reaction, Wikipedia](https://en.wikipedia.org/wiki/Briggs%E2%80%93Rauscher_reaction)
- **Bray–Liebhafsky [Obs + Mod]**
  - Two reactions alternate: 5H2O2 + I2 → 2IO3⁻ + 2H⁺ + 4H2O, and 5H2O2 + 2IO3⁻ + 2H⁺ → I2 + 5O2 + 6H2O. Net: 2H2O2 → 2H2O + O2.
  - The period is hours and shortens with temperature.
  - The mechanism involves both radical and non-radical steps; no consensus is stated.
  — [BL reaction, Wikipedia](https://en.wikipedia.org/wiki/Bray%E2%80%93Liebhafsky_reaction)
- **Clocks and autocatalysis [Conv]**
  - A chemical clock shows an abrupt change after a reproducible induction time. Classes: substrate-depletive, intermediate-species, autocatalysis-driven and "crazy" clocks. Briggs–Rauscher was derived from an iodine clock — [Chemical clock, Wikipedia](https://en.wikipedia.org/wiki/Chemical_clock).
  - Autocatalysis (Ostwald 1890) gives sigmoidal kinetics and multiple steady states, and underlies oscillators — [Autocatalysis, Wikipedia](https://en.wikipedia.org/wiki/Autocatalysis).
- **Models [Mod]**
  - Oregonator (Field & Noyes, Oregon), a reduction of the FKN mechanism:
    - A + Y → X + P
    - X + Y → 2P
    - A + X → 2X + 2Z
    - 2X → A + P
    - B + Z → ½fY

    The page's step and species counts for FKN are internally inconsistent — [Oregonator, Wikipedia](https://en.wikipedia.org/wiki/Oregonator).
  - Brusselator: explicitly theoretical. Its fixed point loses stability at a critical parameter, giving a limit cycle — [Brusselator, Wikipedia](https://en.wikipedia.org/wiki/Brusselator). Source paper: Prigogine & Lefever 1968 — [doi:10.1063/1.1668896](https://www.citedrive.com/en/discovery/symmetry-breaking-instabilities-in-dissipative-systems-ii).
  - Lotka (1910) began from autocatalytic chemistry. The equations conserve a quantity V, so their orbits are a neutral family of closed curves, not an attracting cycle (Volterra 1926) — [Lotka–Volterra, Wikipedia](https://en.wikipedia.org/wiki/Lotka–Volterra_equations).
  - A limit cycle is an isolated closed trajectory that neighbouring trajectories approach. Stable limit cycles are attractors and return after perturbation. Existence is governed by Poincaré–Bendixson. Sel'kov's glycolysis model is an example — [Limit cycle, Wikipedia](https://en.wikipedia.org/wiki/Limit_cycle).
- **Glycolytic oscillation [Obs + Mod]**
  - [Obs] NADH oscillated in cell-free yeast extracts (spectrophotometric and potentiometric measurement), along with pH and CO2; single cells also oscillate.
  - Frequency depends on flux, and oscillation occurs only inside a window spanning 1–5 orders of magnitude of flux.
  - PFK is the "oscillophore": Hill coefficients up to 4.9; activity 1–70% of maximum during a cycle.
  - An ADP pulse given at the NAD⁺ maximum shifts the phase by 180°.
  - [Mod] A 13-equation allosteric model reduces to 2. Positive feedback is needed for a limit cycle.
  — [J. Exp. Biol. 81:7 (author not shown on fetched page)](https://cob.silverchair.com/jeb/article/81/1/7/22630/The-glycolytic-oscillator)
- **Turing patterns [Obs + Mod]**
  - Turing (1952): a uniform state can become unstable if the inhibitor diffuses faster than the activator.
  - The first experimental case came from the Bordeaux group in 1990: the CIMA reaction in a polyacrylamide-gel open reactor.
    - Iodide is the activator and chlorite the inhibitor.
    - Starch, added only as an indicator, bound triiodide and slowed iodide's effective diffusion, so the patterns appeared by accident.
  - Later work: Lengyel–Epstein models (1991, 1992); the CDIMA reaction.
  - 2024: surfactant micelles and quaternary-ammonium gels produce hexagonal and labyrinth patterns.
  — [Aizawa & Asakura, Front. Phys. 12:1358766 (2024)](https://frontiersin.org/journals/physics/articles/10.3389/fphy.2024.1358766/full)

### Inferences
- **What returns in an oscillator.** Intermediates (HBrO2, Br⁻, Ce(IV); I⁻/I2; NADH) return along each period. Reactants and products (bromate, malonic acid, CO2, O2) do not.
- **Batch versus open systems.** A batch oscillator has a finite number of cycles; a fed reactor can sustain them.
- **Periodicity is observed; a limit cycle is inferred.** Calling a periodic signal a limit cycle requires evidence that it returns after perturbation; the 180° ADP phase-reset experiment is such a test. The Lotka scheme shows that closed orbits alone do not imply a limit cycle.
- **Bray–Liebhafsky is itself catalytic.** It is a catalytic cycle (I2 ⇌ IO3⁻ decomposing H2O2) whose two halves alternate in time, so catalytic cycling and temporal oscillation are nested.

### Gaps
- [unverified] Field–Körös–Noyes 1972 (JACS) and Field–Noyes 1974 (J. Chem. Phys.) originals. The Brusselator's Hopf condition B > 1 + A² (standard, not read in-session).
- [unverified] Ouyang & Swinney 1991. Turing wavelengths (~0.2 mm).
- [unverified] Electrochemical oscillators (mercury beating heart) and Pt CO-oxidation oscillations (Ertl).
- [unverified] Glycolytic periods in intact yeast (tens of seconds).

## 5. Molecular machines and conformational cycles

### Takeaway
What is observed: isomer populations, CD and UV changes, ring distributions by NMR, and NMR coalescence. What is modelled: rotary cycles, information and energy ratchets, kinetic asymmetry, pseudorotation pathways. Degenerate conformational exchanges run at equilibrium and do no net work. Directional motors need continuous light, fuel or electrical input, and leave waste or heat.

### Cited Findings
- **Feringa light-driven rotary motor [Obs + Mod; *reproduced* across generations]**
  - Koumura et al. (1999): each 360° turn takes four steps.
    - Two UV-driven cis–trans isomerizations each give 180°.
    - Each is followed by a thermal helix inversion that blocks reverse rotation.
    - Axial chirality and two stereocentres are essential, and the barriers are tunable.
    — [Nature 401:152, doi:10.1038/43646](https://ideas.repec.org/a/nat/nature/v401y1999i6749d10.1038_43646.html)
  - Step detail:
    1. Low-temperature photoisomerization (P,P)-trans → (M,M)-cis forces the methyls equatorial.
    2. Warming to 20 °C triggers helix inversion, restoring axial methyls.
    3. A second photoisomerization.
    4. Heating to 60 °C completes the turn.
  - Related numbers and history:
    - A fluorene lower-half motor has a helix-inversion half-life of 0.005 s.
    - Kelly's 1999 triptycene motor turned 120° in five steps, was not repeatable, and was abandoned.
    - Feringa reported a chemically driven 360° rotor in 2005.
    — [Synthetic molecular motor, Wikipedia](https://en.wikipedia.org/wiki/Synthetic_molecular_motor)
  - [Obs/Sim, 2024 preprint]:
    - Measured thermal helix inversion half-lives span about 15 orders of magnitude; the fastest listed is 1.6×10⁻⁴ s.
    - DFT/HTST predicts 3.4×10⁻⁶ s for a CF3 variant.
    - The agreement between gas-phase calculation and solution measurement is partly error cancellation.
    — [Tambovtsev et al., arXiv 2405.18345](https://arxiv.org/html/2405.18345v3)
- **Leigh ratchets [Obs + Mod]**
  - 2007: a light-driven rotaxane information ratchet (Nature 445:523), framed as a Maxwell's demon whose energy comes from light, so the second law holds — [Physics World](https://physicsworld.com/a/maxwells-demon-tamed/).
  - 2016 [2]catenane (Wilson et al.):
    - Fuel: Fmoc-Cl with NEt3. Waste: CO2, dibenzofulvene and Et3NHCl.
    - Gating: Fmoc attaches faster to the hydroxyl far from the ring, while cleavage does not depend on ring position.
    - [Obs] ¹H NMR showed the ring distribution move from 80:20 toward 55:45, and motion stopped when fuel stopped.
    - Ideally 2 Fmoc-Cl per 360°; in practice ~10 reactions gave ~3 net rotations, about 12 h per turn.
    — [Nature 534:235, doi:10.1038/nature18013](https://ideas.repec.org/a/nat/nature/v534y2016i7606d10.1038_nature18013.html); [accepted manuscript](https://eprints.soton.ac.uk/397244/1/Rvsd_207Apr2016AutonRotaryMolMotor_20Nature.pdf)
  - [Mod] Astumian (2019):
    - Direction comes from kinetic asymmetry. The power stroke is "incorrectly thought to be important for directional motion".
    - The ratchet constant r0 sets intrinsic directionality; doing work w modifies it to r = r0e^(±w).
    - Catalysis supplies Δμ.
    — [Nat. Commun. 10:3837, doi:10.1038/s41467-019-11402-7](https://pmc.ncbi.nlm.nih.gov/articles/PMC6707331)
- **Electrically driven [3]catenane motor (Nature, DOI inferred 10.1038/s41586-022-05421-6) [Obs + Mod]**
  - Two CBPQT⁴⁺ rings circulate when the electrochemical potential is oscillated (chemical reductants and oxidants also work).
  - Deuterium-labelled NMR showed about 85% of motors completing a 180° clockwise step per redox cycle, over a barrier above 25 kcal/mol, with no chemical waste.
  - During peer review the authors dropped an information-ratchet framing and kept "energy ratchet" (a *revised* claim).
  — [peer-review file](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-022-05421-6/MediaObjects/41586_2022_5421_MOESM4_ESM.pdf)
- **Carbodiimide-fuelled reaction cycle [Obs + Mod]** (Boekhoven group, 2023)
  - Cycle: EDC + carboxylate → O-acylisourea → transient anhydride → hydrolysis back to the acid. The fuel ends as urea.
  - Losses:
    - Rearrangement to N-acylurea is irreversible and removes catalyst.
    - Hydrolysis of the O-acylisourea returns the acid without doing work, wasting fuel.
  - [Obs] Anhydride half-life ~9 min at pH 6 and 21 °C; ~46 s with pyridine.
  - N-acylurea consumed 39% of EDC without pyridine and 1% with 35 mM pyridine. Selectivity reached ~98% at pH 5, 5 °C.
  - [Mod] More than 142 refuelings are predicted before catalyst falls below 1%, versus 5 under standard conditions.
  — [Chen et al., Chem. Sci. 2023, doi:10.1039/d3sc04281b](https://pubs.rsc.org/en/content/articlehtml/2023/sc/d3sc04281b)
- **Switches versus motors [Conv]**
  - A switch's work is undone when it returns to its original state; a motor needs continuous energy input.
  - First molecular shuttle 1991. Nobel 2016: Sauvage, Stoddart, Feringa.
  — [Molecular machine, Wikipedia](https://en.wikipedia.org/wiki/Molecular_machine)
  - Motors are modelled stochastically (Fokker–Planck, Monte Carlo) — [Molecular motor, Wikipedia](https://en.wikipedia.org/wiki/Molecular_motor).
- **Ring inversion [Obs + Mod]**
  - Cyclohexane chair–chair barrier 10.8 kcal/mol, about 10⁵ s⁻¹ at room temperature.
  - The half-chair is the transition state; the twist-boat is an intermediate (5.5 kcal/mol); the boat is a local maximum (6.9 kcal/mol).
  - [Obs] One ¹H signal at room temperature; coalescence at about −60 °C at 60 MHz.
  - The ring returns as the identical structure with axial and equatorial positions exchanged.
  — [Ring flip, Wikipedia](https://en.wikipedia.org/wiki/Ring_flip)
- **Fluxionality [Conv/Obs]**
  - "Fluxional" depends on the timescale of the measuring method.
  - PF5 shows a single ¹⁹F environment even at −100 °C, attributed to Berry pseudorotation.
  - Fe(CO)5 shows one ¹³C signal at room temperature and two signals in a 2:3 ratio when cold.
  - A 1 ppm splitting at 500 MHz corresponds to an exchange half-life of about 0.5 ms. Slower exchange is quantified by EXSY.
  — [Fluxional molecule, Wikipedia](https://en.wikipedia.org/wiki/Fluxional_molecule)

### Inferences
- **What "returns" differs by kind.**
  - Degenerate exchanges (ring flip, pseudorotation) return a structure identical in constitution, with atoms permuted. NMR detects exchange but not a direction.
  - Motors return a configuration that is identical but rotated, with net direction measured only through labels (deuterium, two fumaramide sites).
- **Quantified slippage.** Shortfalls from ideal coupling are measured inefficiencies, i.e. futile sub-cycles: 2 versus ~6.7 Fmoc-Cl per turn; 85% success per half-turn; N-acylurea formation.

### Gaps
- [unverified] Berry (1960) barrier for PF5; the Bartell mechanism for IF7.
- [unverified] Bullvalene: predicted by Doering & Roth in 1963; 10!/3 = 1,209,600 degenerate Cope tautomers. Not read.
- [unverified] MHz rotation claims for Feringa motors; Leigh's post-2017 pumps; Boekhoven's 2015 original.
- [unverified] Redox cycling in toxicology (quinones, paraquat generating superoxide).

## 6. Cycles in practice and measurement

### Takeaway
Laboratory and industrial practice imposes cycles from outside: temperature in PCR, potential in cyclic voltammetry and batteries, and reagent sequences in solid-phase and iterative synthesis. In these, the product accumulates geometrically or step by step, and the consumables and per-cycle losses set the limit.

### Cited Findings
- **PCR [Obs + Conv]**
  - Each cycle: denature at 94–98 °C (20–30 s), anneal at 50–65 °C (20–40 s), extend at about 72 °C.
  - Runs use 20–40 cycles. Copies grow as 2ⁿ (2³⁰ ≈ 1.07×10⁹ at 100% efficiency).
  - Amplification plateaus as polymerase activity is lost and dNTPs and primers are used up.
  - Templates are reused each cycle; primers and dNTPs are consumed.
  - Thermostable Taq (from *Thermus aquaticus*, 1976) ended the need to add enzyme each cycle.
  - History: Mullis 1983; Nobel 1993; Saiki 1985 and 1988.
  — [PCR, Wikipedia](https://en.wikipedia.org/wiki/Polymerase_chain_reaction)
- **Electrochemical cycling [Obs/Conv]**
  - The lead–acid battery was the first practical secondary cell. Its reaction is reversible enough to trade electrical and chemical energy repeatedly.
  - A Daniell cell can be driven backwards by an applied voltage.
  - Pt catalyses both H2 and O2 evolution in water electrolysis at about 2 V.
  — [Electrochemistry, Wikipedia](https://en.wikipedia.org/wiki/Electrochemistry)
- **Reuse metric [Conv]**: under first-order decay, TON = TOF0·t½/ln 2 — [Steven 2025](https://public-pages-files-2025.frontiersin.org/journals/catalysis/articles/10.3389/fctls.2025.1720991/pdf).

### Inferences
- **Per-cycle efficiency compounds.** An illustrative calculation of mine: 99% per cycle over 70 cycles leaves about 50%. In imposed cycles, the observed quantity is the yield after n cycles, and the per-cycle efficiency is reconstructed from it.

### Gaps
- [unverified] Cyclic voltammetry: Heyrovský's polarography as precursor; a reversible couple shows ΔEp ≈ 59/n mV at 25 °C. Not read.
- [unverified] Merrifield solid-phase peptide synthesis (1963; Nobel 1984); the phosphoramidite oligonucleotide cycle (detritylation, coupling, capping, oxidation). Not read.
- [unverified] Burke's MIDA-boronate iterative cross-coupling (2007 onward) and automated synthesis (~2015). Not read.
- [unverified] "Circular chemistry" (Keijer, Bakker & Slootweg, Nat. Chem. 2019); battery cycle life and SEI-driven capacity fade. Not read.

## 7. Formal conditions on cycles: detailed balance, Wegscheider, driven cycles, futile cycles, directionality

### Takeaway
At equilibrium every elementary step is balanced by its reverse, so no net circulation is possible. This fixes relations among rate constants around every loop (Wegscheider 1901; Kolmogorov's criterion). Net cycling needs reservoirs at different chemical potentials or temperatures. Its direction follows the cycle's affinity, while how efficiently that affinity is turned into directed motion depends on kinetic asymmetry. Futile cycles and slippage are flux that dissipates without doing the coupled work.

### Cited Findings
- **Detailed balance and its history [Conv]**
  - Detailed balance: each elementary process is balanced by its reverse at equilibrium.
  - Wegscheider (1901) brought it into kinetics and showed that irreversible cycles are impossible under it. For monomolecular cycles, the product of clockwise rate constants equals the product of counter-clockwise ones.
  - Kolmogorov's criterion: a Markov chain is reversible exactly when rate products around every loop are equal in both directions.
  - Boltzmann used detailed balance in 1872 for the H-theorem and introduced semi-detailed (cyclic) balance in 1887.
  - Onsager (1931) used Wegscheider's relations.
  - Detailed balance is sufficient but not necessary for entropy growth. Under local detailed balance, coupling to reservoirs at different T or μ sustains net cycle fluxes. Macroscopic detailed balance can fail even where microscopic detailed balance holds.
  — [Detailed balance, Wikipedia](https://en.wikipedia.org/wiki/Detailed_balance)
- [Conv] Near equilibrium, the Onsager reciprocal relations follow from microscopic reversibility and are closely tied to detailed balance (Nobel 1968). They fail in magnetic fields — [Onsager reciprocal relations, Wikipedia](https://en.wikipedia.org/wiki/Onsager_reciprocal_relations).
- [Mod] Direction in driven cycles: kinetic asymmetry together with Δμ supplied by catalysis; the ratchet constant r0 — [Astumian 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6707331). Cycle fluxes and their thermodynamic forces are central to Hill's framework — [Hill 1989](https://link.springer.com/book/9780387968360).
- **Futile and slip cycles [Obs/Mod]**
  - Transporter slip pathways dissipate without transducing; efficiency peaks at an intermediate flow — [Gawthrop & Crampin](https://arxiv.org/pdf/1611.02332).
  - Carbodiimide: hydrolysis of the O-acylisourea wastes fuel — [Chen et al. 2023](https://pubs.rsc.org/en/content/articlehtml/2023/sc/d3sc04281b).
  - Nitrogenase E4 relaxing backward releases H2 without fixing N2 — [Hickey](https://wisc.pb.unizin.org/nitrogencycle/?p=28).
  - RuBisCO oxygenation (photorespiration) — [Photosynthesis, Wikipedia](https://en.wikipedia.org/wiki/Photosynthesis).

### Inferences
- **Wegscheider's condition restated.** With ΔG° = −RT ln K ([Gibbs](https://en.wikipedia.org/wiki/Gibbs_free_energy)) and G a state function, any set of reactions that closes a loop with no net change has ΣΔG° = 0, i.e. ΠK = 1.
- **A catalytic cycle under turnover does not violate this.** The loop closes on the catalyst but not on the substrate, so the cycle affinity equals −ΔGr of the overall reaction. A catalyst cannot shift equilibrium.
- **Two classes of cycle follow.**
  - Equilibrium cycles: ring flips, pseudorotation, fluxional exchange, and catalysts at equilibrium. Detailed balance holds, forward and reverse traversals are equally frequent, and there is no net direction.
  - Driven cycles: catalysis under turnover, metabolism, motors, ozone chemistry driven by sunlight. These have net flux and are paid for by fuel, light or electricity, with entropy exported.
- **The oscillator controversy is the same distinction applied in time.** Oscillation is impossible about equilibrium, possible only in driven or not-yet-relaxed systems.

### Gaps
- [unverified] Glycolysis/gluconeogenesis substrate cycles (PFK-1 versus FBPase; bumblebee thermogenesis) and their reciprocal regulation. The page was not fetchable.
- [unverified] Fluctuation theorems and stochastic thermodynamics of cycles (Schnakenberg network theory). Not read.
- Considered and excluded: a 2026 single-author molecular-dynamics preprint claiming fluctuation rectification without driving or information ([arXiv 2603.01389](https://arxiv.org/pdf/2603.01389)). It is unreviewed, simulation-only and unreplicated, and its framing is in tension with standard thermodynamics.

## 8. Ledger: what returns, what does not, over what interval

### Takeaway
In every class, what returns is a designated carrier or configuration. What does not return is the fuel's spent form, side products, heat and entropy. Interval figures come either from direct timing (flashes, XFEL, NMR) or from inverting TOF, kcat or residence times.

### Cited Findings (the sources are those already cited for each row above; intervals marked "derived" are my arithmetic from cited values)

| Class | Returns | Does not return | Interval (label) |
|---|---|---|---|
| Rh/Ir carbonylation; Wacker | [Rh(CO)2I2]⁻ / [Ir(CO)2I2]⁻; iodide via HI/MeI; Pd(II) via Cu(II)/O2 | product; propionic acid and water–gas shift products (fewer in Cativa); Pd(0) precipitate if Cu is absent; heat | per turnover = 1/TOF (Rec) |
| Metathesis (W alkylidyne) | metal alkylidene | product alkenes; decomposed catalyst | several hundred turnovers/min → ~0.1–0.3 s each (derived) |
| Mars–van Krevelen on ceria | lattice O refilled from O2 | CO2 carrying lattice ¹⁸O; ~30% of grain oxygen exchanged | onset ~300–400 °C (Obs) |
| Enzyme (Michaelis–Menten) | E | P; heat | 1/kcat: carbonic anhydrase ~2.5 μs; fumarase ~1.25 ms (derived) |
| TCA | oxaloacetate | 2 CO2, 3 NADH, FADH2, GTP per turn; withdrawals for synthesis | per turn (Rec) |
| Calvin | RuBP (5 of 6 triose phosphates) | 1 triose phosphate exported; 3 ATP + 2 NADPH per CO2; 25% of photorespired carbon and NH3 | ms–s (Rec) |
| Kok cycle | S0 of Mn4CaO5 | O2, 4 H⁺, energy of 4 photons | four flashes; O2 onset ~1.2 ms after the third (Obs) |
| Lowe–Thorneley | E0 | 2 NH3, ≥1 H2, ~2 ATP→ADP per e⁻ | cryo-trapped relaxations 6–330 min at −50 °C (Obs) |
| F1 rotation | γ orientation | ATP hydrolysed (3 per turn per Boyer's model, Mod) | >100 turns observed (Obs) |
| Stratospheric ClOx | Cl atom | 2 O2 per O3 + O; Cl eventually removed to the troposphere | ~10⁵ O3 per Cl; ≤~2 yr in cycle (Rec) |
| Heat engine | working substance (U, S) | heat to the cold reservoir; exported entropy | one cycle (Conv) |
| BZ / Briggs–Rauscher / Bray–Liebhafsky | Ce(IV)/Ce(III), Br⁻; I⁻/I2; IO3⁻/I2 | CO2, Br⁻, O2, iodomalonic acid; reactants spent | minutes; ~10 (up to 40+) cycles in 8 min; hours (Obs) |
| Glycolytic oscillation | NADH and adenylate levels | glucose → products | flux-dependent period (Obs) |
| Feringa motor | configuration after 360° | photon energy as heat | thermal inversion t½ from 1.6×10⁻⁴ s upward, over ~15 orders (Obs) |
| Leigh 2016 catenane | ring position | CO2, dibenzofulvene, Et3NHCl; ~6.7 Fmoc-Cl per turn | ~12 h per turn (Obs) |
| Carbodiimide cycle | carboxylic acid | urea; N-acylurea (lost catalyst) | anhydride t½ 46 s–19 min (Obs) |
| Electric catenane motor | ring positions | electrical energy as heat; ~15% failure per half-turn | one redox cycle (Obs) |
| Cyclohexane ring flip | identical chair, positions swapped | nothing net (equilibrium) | ~10⁻⁵ s (derived from 10⁵ s⁻¹) |
| PCR | template strands (as templates) | primers, dNTPs, polymerase activity | ~1–2 min per cycle (derived from step times) |

### Inferences
- **Two senses of "returns".**
  - Material identity: the same catalyst molecule, the same oxaloacetate pool.
  - Configurational identity: the same chair, the same rotor angle, the same S-state. In degenerate exchanges, the atoms in each position are permuted.
- **The cumulative non-return is a hidden second ledger.** Heat, entropy and spent fuel accumulate over many turns. Only driven cycles have one.

### Gaps
- [unverified] Turnover intervals for photoredox and electrocatalysts, TCA turn times in vivo, and residence times for biogeochemical reservoirs were not obtained in-session.
