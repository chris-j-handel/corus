# Sequencing in chemistry: orders of steps, stages, series and chains, and how each is observed or inferred

**Key gathered points** (read first)

Legend for every item below: **[OBS]** observing; **[RECON]** reconstruction from observings; **[CONV]** convention or definition; **[MODEL]** model construct; **[SIM]** simulation. Status tags: **[prior]** is an older state of a claim; **[2023–26]** is a recent development; **[unverified]** means not checked against a source in this session. The session's web-search budget and hourly fetch limit both ran out, which is why some items carry [unverified].

1. A mechanism is an ordered list of elementary steps, but the steps themselves are usually not observed. What is measured is rate laws, product ratios, isotope effects, stereochemistry, and spectra or trapped samples of intermediates that live long enough. A reaction counts as "elementary" when no intermediate has been detected or needs to be postulated, so every mechanistic sequence can be revised.
2. IUPAC treats rate-determining, rate-limiting and rate-controlling as synonyms. It defines the controlling step by a sensitivity coefficient (∂ln v/∂ln k_i), and that step can change with concentrations. Catalysis theory moved control from steps to states: Campbell's degree of rate control (2009) and Kozuch and Shaik's TOF-determining intermediate and transition state (2011).
3. Transition states are saddle points on computed surfaces. Intermediates are minima that last longer than one vibration. The IRC is a static path of steepest descent in mass-weighted coordinates, not a trajectory. Post-transition-state bifurcations (reviewed 2017; biosynthetic cases reviewed November 2025) let one transition state lead to two products, so what comes next can be a distribution set by dynamics.
4. The steady-state (Bodenstein) and pre-equilibrium approximations are modelling choices. For enzymes they give the same form of rate law, and initial-rate data cannot tell them apart.
5. Chain steps are classified by counting radicals: initiation raises the count, propagation keeps it, termination lowers it. The H2/O2 explosion boundary has three limits. A 2018 analysis found the third limit needs radical–radical (nonlinear) chains.
6. Syntheses are planned backward (Corey's retrosynthesis) and carried out forward. What counts as a "step" is a convention, and it was publicly disputed (Chemistry World, about 2016). Planning moved from rule-based software (2018–2020) to neural and LLM systems: Coscientist (2023), template-generative planning (2024), and LLM-steered planners (December 2025, evaluated computationally only).
7. Template-directed copying gives uniform sequences (dispersity 1). Statistical copolymers follow reactivity-ratio statistics (Mayo–Lewis, 1944), a Markov model.
8. Time-resolved methods (pump–probe, ultrafast electron diffraction, XFEL crystallography, attosecond pulses) record a signal against a delay. The ordered intermediates are a fitted model. Read-out methods (Sanger elution ladders, Edman cycles, mass-spectrometry fragment ladders, nanopore current) turn a physical order into a sequence of symbols, with a decoding model in between.
9. The Madelung filling order is empirical and has exceptions. Ionization order differs from filling order (4s electrons are lost before 3d).
10. 2026: atomic electron tomography showed nuclei whose order fades gradually toward their edge, which contradicts the sharp interface assumed by classical nucleation theory.

---

## Mechanism as sequence: elementary steps, intermediates vs transition states, rate- and turnover-determining steps, arrow-pushing, reaction coordinate and IRC, More O'Ferrall–Jencks diagrams, energy profiles, microscopic reversibility

### Takeaway
A mechanism is a model sequence (reactants → TS → intermediate → TS → products). Only intermediates that live long enough and reach detectable amounts can be observed as members of that sequence. Transition states, IRCs, energy profiles and More O'Ferrall–Jencks paths are computed or inferred. IUPAC and catalysis theory define "rate-determining" as a sensitivity of the model, and that sensitivity can move with conditions. Bifurcation dynamics, reported more often since the 2010s and reviewed again in 2025, weaken the assumption that each step has a single next step.

### Cited Findings
**Definitions (membership criteria as chemistry states them)**
- **[CONV] Elementary reaction.** A reaction is elementary when it goes in one step through one transition state. It is treated as elementary when no intermediate has been detected or needs to be postulated, and an apparently elementary reaction may turn out to be stepwise. The criterion is therefore negative evidence. Sequence: reactants (prior) → one TS (now) → products (next). — [Wikipedia: Elementary reaction](https://en.wikipedia.org/wiki/Elementary_reaction) (cites Gold Book doi:10.1351/goldbook.E02035)
- **[CONV] Reaction intermediate.** IUPAC's criterion is a lifetime longer than a molecular vibration, formed from the reactants and reacting further. A transition state's lifetime is close to one vibration. Reactive intermediates are often hard to tell apart from transition states. Intermediates are detected by fast spectroscopy, by chemical trapping, or by isolation at low temperature or in matrices. — [Wikipedia: Reaction intermediate](https://en.wikipedia.org/wiki/Reaction_intermediate) (cites Gold Book doi:10.1351/goldbook.I03096, doi:10.1351/goldbook.R05171)
- **[MODEL] Transition state.** It is the highest-energy configuration along the reaction coordinate: a first-order saddle point with negligible population that always decays, on the femtosecond timescale of bond vibrations. Transition-state theory was developed independently in 1935 by Eyring, Evans and Polanyi. Indirect observation: structure-correlation, which reads reaction paths from distortions in ground-state crystal structures (Bürgi and Dunitz 1983, doi:10.1021/ar00089a002), is [RECON]. Transition-state analogues act as enzyme inhibitors. — [Wikipedia: Transition state](https://en.wikipedia.org/wiki/Transition_state)
- **[CONV] Concerted (IUPAC 2021).** Two or more primitive changes happen within the same elementary reaction. They are energetically coupled, so the joint path has a lower-energy transition state than the changes taken one after another. The changes may be synchronous or asynchronous. The 2021 glossary (published 23 May 2022) revises the 1994 glossary and is meant to replace older entries in the Gold Book. In the portion read, synchronous and asynchronous were not defined separately. — [Perrin et al., IUPAC Recommendations 2021, doi:10.1515/pac-2018-1010](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html?lang=en)
- **[CONV] Curly arrows (IUPAC 2021).** The tail marks where an electron pair starts and the head where it goes. Single-headed arrows track unpaired electrons. The same arrows are used to generate resonance forms. — [IUPAC 2021 glossary](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html?lang=en)
  - History [prior]: Kermack and Robinson, 1922 (J. Chem. Soc. Trans. 121, 427). Lapworth proposed a similar notion the same year. The arrow explained why additions such as bromine to butadiene give specific products. — [Chemistry World, "A century of curly arrows"](https://www.chemistryworld.com/opinion/a-century-of-curly-arrows/4015168.article); DOI 10.1039/CT9222100427 is listed at [Wikipedia: Arrow pushing](https://en.wikipedia.org/wiki/Arrow_pushing), which also cites Ghosh and Wamser 2022 (doi:10.1511/2022.110.6.338).
  - Order encoded: arrow sequences give the order of bond events, for example SN1 in two steps and SN2 in one concerted step. Arrows used for resonance are bookkeeping, with no electron movement. — [Wikipedia: Arrow pushing](https://en.wikipedia.org/wiki/Arrow_pushing)
- **[CONV/MODEL] Rate-determining step.** IUPAC recommends treating rate-determining, rate-limiting and rate-controlling as synonyms. Some authors reserve "rate-determining" for an initial slow step followed by fast steps, and IUPAC discourages that special sense as confusing (PAC 1994, 66, 1077). — [Gold Book R05140](https://goldbook.iupac.org/terms/view/R05140)
- **[MODEL] Rate-controlling step (IUPAC).** It is the elementary step whose rate constant has the strongest effect on the overall rate. The measure is the control function CF = ∂ln v/∂ln k_i, taken with every K_j and every other k held fixed. IUPAC notes the definition is tied to how kinetic isotope effects are interpreted. Worked case: A + B ⇌ C (k1, k−1), then C + D → products (k2), giving v = k1k2[A][B][D]/(k−1 + k2[D]). If k2[D] ≫ k−1, step 1 controls (k_obs = k1). If k2[D] ≪ k−1, step 2 controls after a pre-equilibrium (k_obs = Kk2). So which step controls depends on conditions. — [Gold Book R05139](https://goldbook.iupac.org/terms/view/R05139)
- **[RECON] How a rate-determining step is assigned in standard examples.** For NO2 + CO the observed rate law is r = k[NO2]², zero order in CO. A mechanism with a slow first step, NO2 + NO2 → NO + NO3, fits. The alternative with a slow second step predicts a rate law that contradicts experiment, so it is rejected. Caveats: the rate-determining step is not necessarily the highest point on the Gibbs-energy diagram; it is the largest Gibbs-energy rise measured from the start or from any earlier intermediate. Chain reactions usually have no single rate-determining step. — [Wikipedia: Rate-determining step](https://en.wikipedia.org/wiki/Rate-determining_step) (cites Murdoch 1981, doi:10.1021/ed058p32; Kozuch and Martin 2011, doi:10.1002/cphc.201100137)
  - Which step limits the rate can change with concentration (mixed-order rate laws, the Lindemann scheme, catalysed hexacyanoferrate(III) oxidation). — [Wikipedia: Rate equation](https://en.wikipedia.org/wiki/Rate_equation) (cites doi:10.1021/ed083p1643)
- **[MODEL] Degree of rate control (2009).** Stegelmann, Andreasen and Campbell argue that it is more useful to identify the few rate-controlling transition states and rate-controlling intermediates than a single rate-determining step. Their energies should be measured or calculated most accurately. — [JACS 131, 8077, doi:10.1021/ja9000097](https://orbit.dtu.dk/en/publications/degree-of-rate-control-how-much-the-energies-of-intermediates-and/)
- **[MODEL] Turnover-determining states: the energetic span model (Kozuch and Shaik, Acc. Chem. Res. 2011, 44, 101–110).**
  - Turnover frequency is likened to Ohm's law: a chemical potential divided by a chemical resistance. The model rests on Eyring theory and assumes a steady state.
  - Control sits with one TOF-determining transition state (TDTS) and one TOF-determining intermediate (TDI). These need not be adjacent, and need not be the highest or lowest points.
  - The energetic span is the TDTS–TDI energy gap, with the reaction's driving force added when the TDTS comes before the TDI.
  - Only reactants or products that enter or leave between the TDI and the TDTS affect the rate.
  - The authors' thesis is that catalytic cycles have rate-determining states rather than rate-determining steps.
  - Source: [record](https://cris.iucc.ac.il/en/publications/how-to-conceptualize-catalytic-cycles-the-energetic-span-model/) (DOI not shown there; [unverified])
- **[MODEL] Reaction coordinate.** An abstract one-dimensional progress variable. It may be a bond length, a bond order or a committor (splitting probability). Plotting free energy against it gives an energy profile, which is a cross-section of the potential energy surface. In simulations, collective variables are biased to sample rare barrier crossings. — [Wikipedia: Reaction coordinate](https://en.wikipedia.org/wiki/Reaction_coordinate) (cites Gold Book doi:10.1351/goldbook.R05168; Peters 2016, doi:10.1146/annurev-physchem-040215-112215)
- **[MODEL/SIM] Potential energy surface.** It is computed, not measured: energies are calculated for each atomic arrangement or interpolated between calculated points. Minima are stable species and saddle points are transition states. History [prior]: suggested by Marcelin in 1913; Eyring and Polanyi made the first semi-empirical surface for H + H2 in 1931; Eyring used surfaces for TST rates in 1935. — [Wikipedia: Potential energy surface](https://en.wikipedia.org/wiki/Potential_energy_surface)
- **[CONV/SIM] Intrinsic reaction coordinate.**
  - IUPAC definition: the minimum-energy reaction path on the potential energy surface, in mass-weighted coordinates, from reactants through the transition state to products. Source: the 1999 glossary of theoretical organic chemistry. — [Gold Book IT07057](https://goldbook.iupac.org/terms/view/IT07057/plain)
  - Maeda et al. 2015 (Int. J. Quantum Chem. 115, 258; doi:10.1002/qua.24757):
    - Fukui proposed the IRC in 1970, and the first ab initio IRC was computed in 1977 (Morokuma).
    - Fukui described it as a path without vibration or rotation, so it is not a dynamical trajectory.
    - Uses: confirming which minima a transition state connects, breaking a multistep mechanism into elementary steps, and building IRC networks.
    - Failure modes: near a valley–ridge inflection, trajectories from one transition state split between products. Trajectories also leave the IRC through exit channels, roaming and tunnelling.
    - Source: [PDF](https://glaserr.missouri.edu/vitpub/teaching/8330f16/Maeda_et_al-2015-IRC.pdf)
- **[CONV/MODEL] More O'Ferrall–Jencks diagram.**
  - Gold Book definition: potential energy surfaces drawn against two chosen coordinates, used to discuss how structure shifts transition-state geometry in stepwise versus concerted routes. It was first used for eliminations and later for acid–base catalysis. Shifts along the reaction coordinate follow the Hammond principle; shifts perpendicular to it (anti-Hammond) go the opposite way. The entry is cited as Gold Book 5th edition, 2025, v5.0.0. — [Gold Book M04030](https://goldbook.iupac.org/terms/view/M04030/plain)
  - Origins [prior]: More O'Ferrall 1970 (doi:10.1039/J29700000274) and Jencks 1972 (Chem. Rev., doi:10.1021/cr60280a004).
  - For E2, the axes are C–H cleavage and C–leaving-group cleavage. The corners are reactants, products, the E1 carbocation and the E1cB carbanion. A concerted route crosses the interior; a stepwise route runs along the edges through a corner intermediate. Harris et al. applied the diagram to SN2 in 1979 (doi:10.1021/ja00506a026).
  - Source: [Wikipedia: More O'Ferrall–Jencks plot](https://en.wikipedia.org/wiki/More_O%27Ferrall%E2%80%93Jencks_plot)
- **[MODEL] Curtin–Hammett principle.** For isomers that interconvert rapidly, the product ratio is not set by the isomer populations. It is set by the difference in standard Gibbs energies of the competing transition states. The observed product distribution is thus read as transition-state energies, not as the order in which earlier species are populated. — [IUPAC 2021 glossary](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html?lang=en)
- **[CONV] Microscopic reversibility (equilibrium statement).** At equilibrium, every molecular process and its reverse run at the same average rate. This is Tolman's 1924 statement, and IUPAC now treats it as synonymous with detailed balance (PAC 1996, 68, 149). The entry does not discuss applying the principle to sequences of mechanistic steps. — [Gold Book M03916](https://goldbook.iupac.org/terms/view/M03916)

**Evidence that constrains a mechanistic sequence**
- **[OBS→RECON] Kinds of evidence.** The page lists kinetics and rate laws; spectroscopic detection or isolation of intermediates; product stereochemistry; isotope effects; temperature, pressure and ionic-strength effects; pump–probe spectroscopy; infrared chemiluminescence; electrospray-ionization mass spectrometry; crossover experiments; and computed surfaces. It describes a mechanism as a theoretical conjecture whose steps are usually not directly observable. — [Wikipedia: Reaction mechanism](https://en.wikipedia.org/wiki/Reaction_mechanism) (cites an ESI-MS review, doi:10.1016/j.ijms.2005.08.016)
- **[OBS→RECON] Kinetic isotope effects.**
  - Measured quantity: the ratio k_L/k_H, from parallel runs or from intermolecular or intramolecular competition.
  - Typical sizes: primary C–H/C–D effects about 6–10. Secondary α effects about 1.1–1.2 (normal) or 0.8–0.9 (inverse).
  - What is inferred: a sizeable primary effect suggests the bond to the isotope breaks at or before the rate-determining step. It can also come from a product-determining step after it, and pre-equilibria can give small or inverse values.
  - Singleton's natural-abundance ¹³C/²H NMR method, applied to isoprene + maleic anhydride, supported an asynchronous concerted pathway.
  - Source: [Wikipedia: Kinetic isotope effect](https://en.wikipedia.org/wiki/Kinetic_isotope_effect) (cites Simmons and Hartwig 2012, doi:10.1002/anie.201107334)
- **[OBS→RECON] Matrix isolation.** Reactive species are trapped in solid noble gases or N2 at cryogenic temperature and studied mainly by IR. Pimentel's group developed the method in the 1950s (doi:10.1063/1.1739957). Matrix spectra are compared with computed spectra, so assigning the identity of an intermediate also depends on computation. — [Wikipedia: Matrix isolation](https://en.wikipedia.org/wiki/Matrix_isolation)

**Where "next" is not unique: bifurcations [reopened]**
- **[SIM, with experimental tests] Post-transition-state bifurcations (PAC 2017, from ICPOC-23, 2016).**
  - A single transition-state structure leads to several products with no minimum or second barrier in between. Such cases were once thought rare and are now reported much more often.
  - Even when an intermediate exists, the product mix need not be statistical if energy does not redistribute faster than the system crosses on.
  - "Dynamic matching": the phase of a vibration set up at the transition state steered the product in one case.
  - A Diels–Alder reaction related to spinosyn A is called "dynamically stepwise" because of a long gap between its two bond formations.
  - The bifurcation for the singlet-oxygen ene reaction disappeared in explicit solvent. Simulated selectivities are sensitive to the surroundings.
  - Source: [doi:10.1515/pac-2017-0104](https://www.degruyterbrill.com/document/doi/10.1515/pac-2017-0104/html) (authors not shown on the page)
- **[SIM vs OBS; 2023–26] Ambimodal transition states in biosynthesis (Hussain, Houk, Lam, Sarker, Nahar; RSC, first published 18 Nov 2025; covers literature to June 2025).**
  - SpnF: simulations give about 11:1 [4+2]:[6+4] in the enzyme, but the [6+4] adduct has never been observed.
  - StmD/NgnD: the [6+4] adduct is stable and has been isolated, with about 3:1 predicted.
  - IccD: 99:1 measured against 98:2 from gas-phase trajectories.
  - Sativene/ylangene: the proposed bifurcation is still only a computational hypothesis.
  - Delitschiapyrones: computation calls the proposed cascade unlikely, which conflicts with the isolated product.
  - Source: [Nat. Prod. Rep. (inferred) d5np00064e](https://pubs.rsc.org/en/content/articlehtml/2026/np/d5np00064e)

### Inferences
- A mechanistic sequence has three layers. (a) Observed: rate orders, product ratios, isotope effects, stereochemistry, and spectra of detectable intermediates. (b) Reconstructed: the kinetic scheme that fits these. (c) Modelled: transition states, PES, IRC, More O'Ferrall–Jencks paths. Only species with lifetimes beyond one vibration and enough concentration can be "observed" as members of the sequence.
- "Elementary" is assigned on negative evidence, so any list of elementary steps is provisional. Several definitions (rate-controlling CF, degree of rate control, energetic span) locate the controlling point by sensitivity analysis of a model, not by direct inspection of a step.
- The bifurcation literature shows that "prior → now → next" can branch after a single transition state. The order of events is then a matter of dynamics and timing ("dynamically stepwise"), and measured product ratios test the simulations.
- In the More O'Ferrall–Jencks picture, concerted versus stepwise is a question of path geometry in a two-coordinate model. Experimental proxies (isotope effects, Hammett or Brønsted slopes) are mapped onto positions in it.

### Gaps
- Microscopic reversibility applied to mechanisms (the reverse reaction passing through the same intermediates and transition states in reverse order) is not covered by the Gold Book entry read and was not checked [unverified].
- Fukui's 1970 IRC paper, Hammond 1955 and Leffler were not read directly. The Hammond–Leffler page returned "not found".
- The Kozuch–Shaik DOI and the authors of the 2017 PAC review are [unverified]. The 2021 glossary was read only up to about 100,000 of 104,896 characters.
- No source was checked for "principle of least nuclear motion" or other ordering heuristics.

---

## Kinetic sequences: consecutive reactions, steady-state and pre-equilibrium approximations, chain reactions and explosion limits, autocatalysis and induction periods

### Takeaway
The observed quantities are concentration–time curves, rate orders, quantum yields and the pressure–temperature boundary of explosions. Kinetic sequences such as A→B→C, chains, and autocatalytic loops are model schemes fitted to these curves. The approximations used to reduce them (steady state, pre-equilibrium) are choices with stated conditions of validity. IUPAC warns that "steady state" does not mean constant concentration.

### Cited Findings
- **[CONV/MODEL] Steady-state (Bodenstein) approximation (IUPAC).** For unstable intermediates at low concentration, each intermediate's rate of change is set to zero, so the rate law contains only species present in macroscopic amounts. The note stresses that this does not mean [X] stays nearly constant, only that its rate of change is much smaller than that of reactants and products. In a stirred-flow reactor, "steady state" means every concentration is time-independent. — [Gold Book steady state](https://goldbook.iupac.org/S05963.html) (page gives doi:10.1351/goldbook.S05962)
- **[OBS→MODEL; prior] Bodenstein.** In 1899 he heated H2 + I2 in sealed tubes, quenched them and measured HI, which confirmed Guldberg–Waage equilibrium. He explained the high efficiency of the photochemical H2 + Cl2 reaction as a chain (Bodenstein and Dux 1913, Z. Phys. Chem. 85, 297). His 1913 paper on photochemical reaction rates (Z. Phys. Chem. 85, 390) belongs to his kinetics work, and he used the quasi-steady-state assumption. The page does not give the year he introduced it. — [Wikipedia: Max Bodenstein](https://en.wikipedia.org/wiki/Max_Bodenstein). A separate page credits Bodenstein (1913) with first proposing chemical chains. — [Wikipedia: Chain reaction](https://en.wikipedia.org/wiki/Chain_reaction)
- **[MODEL] Pre-equilibrium versus steady state, the enzyme case.** Michaelis and Menten (1913) assumed rapid equilibrium, so K_M is a dissociation constant. Briggs and Haldane (1925, doi:10.1042/bj0190338) assumed quasi-steady state, giving K_M = (k−1 + k_cat)/k1. Both produce the same equation form. Measured initial rates cannot decide whether K_M is a dissociation constant. Henri's earlier form is dated 1902 or 1903 depending on the source. Segel and Slemrod (1989, doi:10.1137/1031091) analysed when the quasi-steady-state assumption holds. — [Wikipedia: Michaelis–Menten kinetics](https://en.wikipedia.org/wiki/Michaelis%E2%80%93Menten_kinetics)
  - The general pre-equilibrium limit (k_obs = Kk2) appears in IUPAC's rate-controlling example. — [Gold Book R05139](https://goldbook.iupac.org/terms/view/R05139)
- **[MODEL] Consecutive reactions A → B → C.** In consecutive reactions the rate-determining step often controls the kinetics. The steady-state approximation simplifies the rate law for consecutive first-order steps. — [Wikipedia: Chemical kinetics](https://en.wikipedia.org/wiki/Chemical_kinetics)
  - Standard closed forms [unverified; not checked against a source in this session]: [B](t) = k1[A]0(e^(−k1t) − e^(−k2t))/(k2 − k1), with the maximum of [B] at t = ln(k1/k2)/(k1 − k2). Observed: the rise and fall of B, if B is detectable. Model: which rate constant belongs to which step.
- **[RECON] Steady-state treatments matched to observed orders.** Acetaldehyde pyrolysis (Rice–Herzfeld): a steady state in methyl radicals gives the observed 3/2 order. — [Wikipedia: Rate equation](https://en.wikipedia.org/wiki/Rate_equation). H2 + Br2: 3/2-order mixed rate law, with an inhibition step that reverses the first propagation step. — [Wikipedia: Chain reaction](https://en.wikipedia.org/wiki/Chain_reaction)
- **[CONV] Chain reaction (IUPAC 2021).** Reactive intermediates, often radicals, are continuously regenerated by a repeated cycle of elementary steps (propagation). Methane chlorination is the example given. — [IUPAC 2021 glossary](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html?lang=en)
  - Step classes are defined by counting radicals: initiation raises the count (for example, light-driven homolysis of a halogen or peroxide), propagation keeps it, termination lowers it (2 Cl• → Cl2). — [Wikipedia: Free radical](https://en.wikipedia.org/wiki/Free_radical)
  - Chain length is the overall rate divided by the initiation rate. Branching means one carrier produces two or more. Chain transfer moves activity to a new molecule. — [Wikipedia: Chain reaction](https://en.wikipedia.org/wiki/Chain_reaction)
- **[OBS→MODEL; prior] History of chain kinetics.**
  - Nernst (1918) explained the H2 + Cl2 quantum yield, up to about 10⁶ HCl per photon, by a chain.
  - Christiansen and Kramers (1923) added thermal initiation, and proposed that branching gives exponential growth, the mechanism of explosions.
  - Semenov published a quantitative theory in 1934. — [Wikipedia: Chain reaction](https://en.wikipedia.org/wiki/Chain_reaction)
  - Semenov's degenerate branching explained induction periods in oxidations. His 1934 book appeared in English in 1935. — [Wikipedia: Nikolay Semyonov](https://en.wikipedia.org/wiki/Nikolay_Semyonov)
  - Nobel 1956 to Hinshelwood and Semenov, for research into the mechanism of chemical reactions. — [nobelprize.org](https://www.nobelprize.org/prizes/chemistry/1956/summary/)
- **[OBS + MODEL; 2018] H2/O2 explosion limits (Liang and Law, PCCP 20, 742; doi:10.1039/c7cp05639g).**
  - Observed: the ignition boundary is Z-shaped in pressure–temperature space, with three explosion limits.
  - Model, first and second limits: competition between linear branching and linear termination, plus destruction of radicals at the wall.
  - Model, third limit: linear chains alone underpredict it, and radical–radical (nonlinear) chains must be included. HO2 dominates at intermediate pressure and H2O2 at high pressure, through H + O2 + M → HO2 + M and HO2 + HO2 → H2O2 + O2.
  - Coupling between linear and nonlinear chains matters; coupling among nonlinear chains is negligible.
  - Source: [Princeton record](https://collaborate.princeton.edu/en/publications/an-analysis-of-the-explosion-limits-of-hydrogenoxygen-mixtures-wi/)
  - Terminology conflict: one page says termolecular steps are generally not treated as elementary ([Wikipedia: Elementary reaction](https://en.wikipedia.org/wiki/Elementary_reaction)), while combustion kinetics treats the three-body step H + O2 + M as a controlling elementary step (Liang and Law).
- **[CONV] Induction period (IUPAC).** The initial slow phase of a reaction that later speeds up. It is common in radical reactions, and can include the delay before steady-state concentrations are reached. — [Gold Book I03019](https://goldbook.iupac.org/terms/view/I03019)
  - Causes listed: a precatalyst must activate first (Wilkinson's catalyst losing PPh3); autocatalysis; self-heating. Grignard initiation is slow because of the oxide film, with a risk of thermal runaway. — [Wikipedia: Induction period](https://en.wikipedia.org/wiki/Induction_period)
- **[CONV/MODEL] Autocatalysis.** A product catalyses its own formation. Progress curves are sigmoidal (logistic), and the early slow phase comes from scarce catalyst. Ostwald introduced the idea in 1890 for an ester hydrolysis. Examples: Belousov–Zhabotinsky oscillations, crystal growth, the Soai reaction, the formose reaction, and self-replicating molecules. — [Wikipedia: Autocatalytic reaction](https://en.wikipedia.org/wiki/Autocatalytic_reaction) (cites Gold Book doi:10.1351/goldbook.A00525; Bissette and Fletcher 2013, doi:10.1002/anie.201303822; Blackmond 2020, doi:10.1021/acs.chemrev.9b00557)
- **[OBS → open MODEL] Soai reaction (1995, doi:10.1038/378767a0).** Pyrimidine-5-carbaldehyde is alkylated by iPr2Zn, and the chiral alcohol product catalyses its own formation. A small enantiomeric excess is amplified to a high one. The page does not report an agreed mechanism; its explanation of how chirality is induced is speculative. — [Wikipedia: Soai reaction](https://en.wikipedia.org/wiki/Soai_reaction) (cites Blackmond 2004, doi:10.1073/pnas.0308363101)
- **[OBS→RECON] Reaction progress kinetic analysis (Blackmond, formalised late 1990s; Angew. 2005, doi:10.1002/anie.200462544).**
  - Observed: in-situ heat flow, IR, NMR or UV profiles.
  - "Same-excess" runs: if the curves overlay, the catalyst is robust. A curve below suggests activation (an induction period); a curve above suggests deactivation. Adding product to a same-excess run tests for product inhibition.
  - Source: [Wikipedia: Reaction progress kinetic analysis](https://en.wikipedia.org/wiki/Reaction_progress_kinetic_analysis)

### Inferences
- In every kinetic sequence the observation is a set of curves (concentration or heat flow against time, or explosion boundaries). The order of steps and the identity of intermediates are reconstructed by fitting, and the choice of approximation (steady state or pre-equilibrium) can leave the fitted form unchanged while changing what the constants mean. The Michaelis–Menten case is the clearest documented instance.
- Chain and autocatalytic schemes are cyclic in the model. On the timeline they show up as phases (induction, then acceleration, then decay, or ignition) defined by thresholds such as the explosion limits.

### Gaps
- The integrated A→B→C solution and the well-known ambiguity in assigning k1 and k2 were not source-checked [unverified].
- The year Bodenstein introduced the steady-state approximation was not confirmed from a primary source.
- Semenov's phosphorus-vapour critical-pressure experiments and Hinshelwood's H2/O2 work were not retrieved.
- No 2023–26 developments on chain kinetics were found in this session.

---

## Synthetic sequences: total synthesis, retrosynthesis, step and redox economy, cascades and multicomponent reactions, automated and AI-planned synthesis, iterative synthesis, biosynthetic assembly lines, template-directed copying, sequence-defined polymers, copolymer statistics

### Takeaway
Synthetic sequences are planned backward and carried out forward. Their step counts are conventions, and the rules for counting were openly disputed. Automated planning since 2018 has moved from rule-based software to neural and LLM agents. As far as the checked sources show, only some of these planners have been tested in a laboratory. Living systems and template copying produce exact, uniform sequences. Chain copolymerisation produces statistical sequences described by a Markov model with reactivity ratios.

### Cited Findings
**Planning order versus execution order**
- **[CONV/MODEL] Retrosynthesis.** Corey starts from the target and works backward to simpler building blocks. — [nobelprize.org: The logic of chemical synthesis](https://www.nobelprize.org/prizes/chemistry/1990/8830-the-logic-of-chemical-synthesis/)
  - The 1990 presentation speech: the prize covered retrosynthetic analysis, new reactions, and syntheses of biologically important natural products.
  - "Strategic bonds" are broken repeatedly until known or commercially available compounds are reached, and Corey showed this logic could be programmed.
  - About 100 natural products were synthesised and about 50 reactions were new or improved.
  - Source: [nobelprize.org: ceremony speech](https://www.nobelprize.org/prizes/chemistry/1990/ceremony-speech/)
  - Book: Corey and Cheng, *The Logic of Chemical Synthesis* — [listing](https://www.abebooks.com/9780471509790/Logic-Chemistry-Synthesis-Corey-Cheng-0471509795/plp) (year [unverified]).
  - Order: in planning, the precursor is "next" after the target. In execution the same compound is "prior".
- **[CONV] Economies of synthesis.** Newhouse, Baran and Hoffmann treat atom, step and redox economy as practical design guidelines. — [Chem. Soc. Rev. 38, 3010 (2009), doi:10.1039/B821200G](https://pubs.rsc.org/en/content/articlehtml/2009/cs/b821200g)
  - Hendrickson (1975): an ideal synthesis uses only construction reactions, with no intermediate refunctionalisations.
  - Wender (1993): the ideal is one simple, safe, resource-effective operation from available materials. Wender's cedrene route took 4 steps where the earlier one took 25.
  - Bryostatin 1 total synthesis: 57 steps.
  - Compounding loss: 20 steps at 80% each turn 1 kg into about 11 g.
  - Baran calls protecting-group and functional-group-interconversion steps "concession steps".
  - Source: [Chemistry World, "Stepping toward ideality"](https://www.chemistryworld.com/features/stepping-toward-ideality/5190.article)
- **[CONV; disputed, about 2016] What counts as a step.** In Baran's thapsigargin route, a protection and a second hydroxylation were done in one pot. Baran counts a step as ending at a work-up or purification. Critics prefer to call this "one pot", not one step. In a straw poll of about 500 Twitter responses, 73% sided with Baran. Reviewers had the step count moved from the paper's title into its body. — [Chemistry World opinion](https://www.chemistryworld.com/opinion/what-counts-as-a-step-during-chemical-synthesis/2500261.article)
- **[CONV] Domino, cascade and tandem reactions.** Tietze (Chem. Rev. 1996, 96, 115): two or more bond-forming steps under the same conditions, with no added reagents or catalysts, each arising from functionality made in the previous step. "Domino", "cascade" and "tandem" are often used for the same idea. Robinson's tropinone synthesis (1917) is cited as the first, and Johnson's progesterone polyene cyclization (1971) as a classic. Cascades are classed by mechanism: electrophilic, nucleophilic, radical, pericyclic, transition-metal. — [EPFL group seminar PDF](https://www.epfl.ch/labs/lspn/wp-content/uploads/2018/10/Domino.pdf)
  - Jones, May, Sarpong and Stoltz (Angew. 2014, doi:10.1002/anie.201302572):
    - "Consecutive" processes add reagents without isolating intermediates.
    - They propose counting cascades as "duet", "trio", "quartet", and admit judgement calls such as whether tautomerizations count.
    - Examples: Davies cyclopropanation/Cope toward (−)-5-epivibsanin; Snapper ring-opening metathesis/Cope toward (+)-asteriscanolide.
    - Source: [PDF](https://www.stoltz2.caltech.edu/publications/149-2014.pdf)

**Iterative and automated sequences**
- **[OBS] Iterative cross-coupling (Burke).** Iterative Suzuki–Miyaura coupling of B-protected haloboronic acids, explicitly compared with peptide synthesis, and an automated "synthesis machine". Extension to C(sp³) couplings is in progress. — [Burke group page](https://burke-group.chemistry.illinois.edu/?p=64)
- **[OBS] Oligonucleotides.** Solid-phase phosphoramidite synthesis adds one nucleotide per repeated cycle, running 3'→5'. Per-cycle yields below 100% and side reactions keep typical products at 13–25 nt, rarely above about 200. — [Wikipedia: Oligonucleotide](https://en.wikipedia.org/wiki/Oligonucleotide)
- **[2018–2025] Computer and AI planning.**
  - [prior] Segler et al., "Planning chemical syntheses with deep neural networks and symbolic AI", Nature 555 (2018). — [index](https://ideas.repec.org/r/nat/nature/v555y2018i7698d10.1038_nature25978.html) (details [unverified])
  - [prior] Klucznik et al. 2018, a title on computer-planned syntheses of medicinal targets executed in the laboratory, seen in search results only (details [unverified]). — [record](https://pr.ibs.re.kr/handle/8788114/5005?mode=full)
  - [prior] Nature, about 20 Oct 2020 (Grzybowski, Młynarski and Mrksich groups): computer-planned multistep syntheses of complex natural products. Experts reportedly could not tell machine plans from human ones, and Chematica took about 20 years to build. — [Polish Science news](https://www.polishscience.pl/en/?p=150668); paper link [nature.com/articles/s41586-020-2855-y](https://www.nature.com/articles/s41586-020-2855-y) (not fetched)
  - [2023] Coscientist (Boiko, MacKnight, Kline, Gomes; Nature, online 20 Dec 2023; doi:10.1038/s41586-023-06792-0): an LLM agent that read documentation, controlled liquid handlers and a cloud lab, and optimised and ran Suzuki and Sonogashira couplings. — [CMU news](https://www.cmu.edu/news/stories/archives/2023/december/cmu-designed-artificially-intelligent-coscientist-automates-scientific-discovery); [ChemistryViews](https://www.chemistryviews.org/?p=76389)
  - [2024] Shee et al. (Nat. Commun. 15; doi:10.1038/s41467-024-52048-4): generates reaction templates for user-chosen bonds and scores plausibility with a CKAE. A three-step route was designed for a target where earlier approaches needed five to nine steps. — [index](https://ideas.repec.org/a/nat/natcom/v15y2024i1d10.1038_s41467-024-52048-4.html)
  - [Dec 2025] Synthelite (Xuan-Vu, …, Schwaller; arXiv:2512.16424): LLMs propose retrosynthetic steps and chemists steer with text, with up to 95% success on constrained tasks. The abstract reports no laboratory validation. — [arXiv](https://arxiv.org/abs/2512.16424v1)
  - Titles seen in a citing-works index, content [unverified]:
    - RSGPT, a retrosynthesis transformer pretrained on about 10¹⁰ datapoints (Nat. Commun. 2025)
    - "Autonomous platforms for data-driven organic synthesis" (2022)
    - A roboticised microfluidic photocatalysis platform running up to 10,000 reactions per day (2024)
    - "Merging enzymatic and synthetic chemistry with computational synthesis planning" (2022)
    - Source: [ideas.repec listing](https://ideas.repec.org/r/nat/nature/v555y2018i7698d10.1038_nature25978.html)

**Biological and template-directed sequences**
- **[OBS + MODEL] Nonribosomal peptides and polyketides.** Nonribosomal peptides are made by modular enzyme complexes in which successive modules perform different chemical changes on the growing product. The machinery is related to fatty-acid and polyketide synthesis, so hybrid products are common. — [Wikipedia: Peptide](https://en.wikipedia.org/wiki/Peptide) (cites Finking and Marahiel 2004, doi:10.1146/annurev.micro.58.030603.123615). The colinearity rule (module order predicts residue order) is [unverified].
- **[OBS/MODEL] DNA polymerase.** Each addition is dNTP + DNA_n ⇌ PPi + DNA_(n+1). Synthesis runs 5'→3' while the template is read 3'→5'. Proofreading uses a 3'→5' exonuclease. Pol I adds about 15–20 nt/s; phage T4 elongation is 749 nt/s at 37 °C. — [Wikipedia: DNA polymerase](https://en.wikipedia.org/wiki/DNA_polymerase)
- **[RECON] Replication as an ordered programme.**
  - Initiation: ORC, Cdc6 and Cdt1 load the Mcm helicase, which is activated in S phase.
  - Elongation: primase lays primers; the leading strand is continuous and the lagging strand is made as Okazaki fragments; primers are removed and ligase seals the nicks.
  - Termination: Tus–Ter sites in bacteria.
  - Errors: below 1 in 10⁷ for the polymerase alone, below 1 in 10⁹ with proofreading plus mismatch repair. The polymerase page instead gives about 1 in 10⁹ for the enzyme, so the two pages scope the figure differently.
  - Source: [Wikipedia: DNA replication](https://en.wikipedia.org/wiki/DNA_replication) (cites McCulloch and Kunkel 2008, doi:10.1038/cr.2008.4)
- **[OBS] PCR as a cyclic sequence.** Each cycle denatures (94–98 °C), anneals (50–65 °C) and extends (about 72 °C), and in theory doubles the target. Products are checked by gel or by quantitative PCR. — [Wikipedia: Polymerase chain reaction](https://en.wikipedia.org/wiki/Polymerase_chain_reaction)
- **[OBS + MODEL] Translation.**
  - Codons are read three nucleotides at a time, and proteins are always made from N- to C-terminus. — [Wikipedia: Protein](https://en.wikipedia.org/wiki/Protein)
  - The ribosome is a ribozyme: its RNA carries out peptidyl transfer. Atomic structures appeared in 2000 (doi:10.1126/science.289.5481.905; doi:10.1126/science.289.5481.920), and the 2009 Nobel followed.
  - Stages: initiation → elongation (A/P/E sites, decoding, peptide-bond formation, translocation) → termination (UAA, UAG, UGA, release factors) → recycling. — [Wikipedia: Ribosome](https://en.wikipedia.org/wiki/Ribosome)
- **[CONV] Sequence conventions and dispersity.** Template-directed biopolymers are "all alike" (dispersity 1). Peptides are written N→C and nucleic acids 5'→3'. — [Wikipedia: Biopolymer](https://en.wikipedia.org/wiki/Biopolymer)

**Synthetic polymer sequences**
- **[CONV] Sequence-controlled polymers.** Lutz, Ouchi, Liu and Sawamoto, Science 2013 (doi:10.1126/science.1238149). Alternating, periodic and block copolymers are the simple cases. — [Wikipedia: Polymer](https://en.wikipedia.org/wiki/Polymer)
- **[CONV/OBS] Living polymerization.**
  - IUPAC: a chain polymerization with no chain transfer and no termination (Jenkins 1996, doi:10.1351/pac199668122287).
  - Szwarc showed it in 1956 (doi:10.1021/ja01592a101).
  - Adding monomers one after another builds blocks; PS-b-PMMA is made by polymerizing styrene and then MMA.
  - ATRP, NMP and RAFT do not strictly meet the IUPAC definition, and the naming is still debated.
  - Source: [Wikipedia: Living polymerization](https://en.wikipedia.org/wiki/Living_polymerization)
- **[MODEL + OBS] Copolymer sequence statistics (Mayo and Lewis 1944, JACS 66, 1594; doi:10.1021/ja01237a052).**
  - Model: a chain ending in M1 or M2 adds M1 or M2, giving four propagation steps, with active centres at steady state. r1 = k11/k12 and r2 = k22/k21.
  - Both r near 0: alternating. Both above 1: blocky. Both near 1: statistical. An azeotrope is possible. Composition drifts as conversion rises.
  - Measurement: several low-conversion runs at different feed ratios, with composition by ¹H/¹³C NMR or FTIR. Fitting by Fineman–Ross (1950), Kelen–Tüdős (1980) or, preferred, nonlinear least squares, because linearising biases the result.
  - Q–e scheme: Alfrey and Price, 1947.
  - Source: [Wikipedia: Mayo–Lewis equation](https://en.wikipedia.org/wiki/Mayo%E2%80%93Lewis_equation)
  - The model is Markov: only the last unit matters. A penultimate model exists but is rarely needed. Sequence is characterised by NMR. — [Wikipedia: Copolymer](https://en.wikipedia.org/wiki/Copolymer)
  - Conflict: the styrene/maleic anhydride ratios are given as 0.097/0.001 on the Copolymer page and about 0.01/0.02 on the Mayo–Lewis page.

### Inferences
- Synthetic chemistry runs two opposite orders over the same compounds: planning (target first) and execution (starting material first). Counting steps or reactions in a cascade is explicitly a convention, and the sources disagree on its rules.
- Iterative synthesis (phosphoramidite cycles, iterative couplings) and iterative read-out (Edman, below) share one limit: the per-cycle yield compounds, and that caps sequence length.
- Template-directed processes produce one defined sequence. Statistical copolymerisation produces a distribution, inferred from composition and NMR through a Markov model. Living polymerisation sits between them: it controls the order of blocks but not the exact sequence within a block.

### Gaps
- Not checked in this session [unverified]:
  - Multicomponent reactions (Ugi, Passerini).
  - Transcription chemistry.
  - The colinearity rule for PKS/NRPS assembly lines and DEBS (erythromycin).
  - Exactly sequence-defined synthetic polymers and molecular data storage (Lutz's digital polymers read by MS/MS; DNA data storage).
  - Merrifield's solid-phase peptide synthesis.
  - Disputes over 2023–2025 autonomous-lab claims.
- Full texts of Klucznik 2018 and the 2020 Nature paper were not retrieved, so their numbers (targets planned and executed) are missing.

---

## Ordering sequences among the elements (brief): Aufbau/Madelung filling order and ionization sequences

### Takeaway
The filling order is an empirical rule. Its exceptions are documented, and heavy elements need relativistic corrections. Ionization order differs from filling order, which shows the order is a property of each species' electronic structure, not one fixed sequence.

### Cited Findings
- **[CONV/MODEL, empirical] Madelung (n + l) rule.** Subshells fill in order of increasing n + l, with ties going to lower n: 1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s 4f 5d 6p 7s 5f 6d 7p.
  - The rule is called empirical. It works very well for the ground states of the 118 known elements but is sometimes slightly wrong.
  - Exceptions include Cr, Cu, Nb, Mo, Ru, Rh, Pd, Ag, Pt, Au and some f-block elements, with most in the 4d series. Heavy cases need relativistic effects.
  - Janet stated the rule in 1929, Madelung rediscovered it in 1936, and Klechkowski justified it. Bohr's 1923 aufbau built on Langmuir.
  - Source: [Wikipedia: Electron configuration](https://en.wikipedia.org/wiki/Electron_configuration) (cites Bohr 1923, doi:10.1007/BF01328209; Wong 1979, doi:10.1021/ed056p714; Meek and Allen 2002, doi:10.1016/S0009-2614(02)00919-3)
- **[OBS→MODEL] Ionization order differs from filling order.** Transition-metal atoms lose 4s electrons before 3d; for example Cr is [Ar]4s¹3d⁵ and Cr²⁺ is [Ar]3d⁴. The explanation is that orbital energies depend on nuclear charge and on the other electrons present (Melrose and Scerri 1996, doi:10.1021/ed073p498). — [Wikipedia: Electron configuration](https://en.wikipedia.org/wiki/Electron_configuration); [Wikipedia: Atomic orbital](https://en.wikipedia.org/wiki/Atomic_orbital)

### Inferences
- Configurations come from spectroscopy, but the filling "sequence" is a rule fitted to them. Exceptions and ion configurations show that no single order describes all atoms and ions.

### Gaps
- The spectroscopic basis of ground-state assignments and the trends in ionization energies were not source-checked. Another researcher covers ranked series in depth.

---

## Phase and assembly sequences: Ostwald's step rule, crystallization pathways, folding pathways and intermediates, self-assembly pathway complexity, Bowen's reaction series

### Takeaway
Nucleation, crystallization and folding are each described as staged sequences, such as nucleation then growth, or unfolded through intermediates to native. The stages that are actually observed are bulk or single-molecule signals, waiting times, and, since 2026, atomic tomography of nuclei. Classical nucleation theory's sharp-interface sequence has documented failures and was directly challenged in 2026. Folding theory replaced the idea of a single pathway with an ensemble funnel. AlphaFold-type prediction gives end states, not the order of folding events.

### Cited Findings
- **[CONV] Crystallization in two phases.** Nucleation (a crystalline phase appears) and then growth, both driven by supersaturation. Metastable polymorphs are kinetically stable and need energy to convert, as in anatase → rutile. — [Wikipedia: Crystallisation](https://en.wikipedia.org/wiki/Crystallisation)
- **[MODEL] Classical nucleation theory.**
  - It treats a nucleus as a droplet with a sharp surface and bulk interfacial tension, so the rate falls exponentially with the barrier ΔG*.
  - Limits: the capillarity assumption for nuclei of tens of molecules; growth only by single-particle steps; spherical shape. The rate is extremely sensitive to the free energy, so models are usually fitted to data.
  - Vapour–liquid rates can be off by orders of magnitude (doi:10.1063/1.2186327). Agreement is good for hard-sphere colloids (doi:10.1063/1.1638740).
  - Sources: [Wikipedia: Classical nucleation theory](https://en.wikipedia.org/wiki/Classical_nucleation_theory); [Wikipedia: Nucleation](https://en.wikipedia.org/wiki/Nucleation)
- **[OBS] Nucleation is stochastic.** Pound and La Mer studied tin droplets in 1952 (doi:10.1021/ja01129a044). Pure water droplets stay liquid to about −35 °C. CaCO₃ nucleation depends on both supersaturation and the Ca²⁺:CO₃²⁻ ratio (doi:10.1021/acs.cgd.0c01403). — [Wikipedia: Nucleation](https://en.wikipedia.org/wiki/Nucleation)
- **[SIM] Ice nucleation (Sanz et al. 2013, doi:10.1021/ja4028814).** Simulations with the TIP4P/2005 water model at 19.5 °C of supercooling imply about 10⁷⁶ years per m³ for one nucleus. The page notes this cannot be measured directly. — [Wikipedia: Classical nucleation theory](https://en.wikipedia.org/wiki/Classical_nucleation_theory)
- **[OBS; 2026; reopened] Yuan et al., Nature Materials 2026 (doi:10.1038/s41563-026-02727-y).** Atomic electron tomography of high- and medium-entropy alloy nanoparticles shows structural order fading gradually toward the edge of a nucleus. A gradient model of nucleation reduces to classical theory in the sharp-interface limit. — [Wikipedia: Classical nucleation theory](https://en.wikipedia.org/wiki/Classical_nucleation_theory)
- **[RECON] Order before nucleation.** Chemical ordering in undercooled liquids before crystals nucleate may lower the barrier (doi:10.1016/j.matdes.2018.07.013; doi:10.1016/j.jnoncrysol.2006.02.074). — [Wikipedia: Nucleation](https://en.wikipedia.org/wiki/Nucleation)
- **[CONV, unverified] Ostwald's step rule (1897).** The first phase to form is often a metastable one, not the most stable, with stepwise conversion afterwards. It is an empirical rule with exceptions. No source was checked in this session.
- **[OBS] Staged self-assembly.** Fmoc-DOPA goes from spheres to fibres to gels to crystals (Fichman 2016, doi:10.1126/sciadv.1500827). Microscopic assembly is described as diffusion → nucleation → seed growth → Ostwald ripening. Static self-assembly approaches equilibrium; dynamic self-organisation does not (Whitesides and Grzybowski 2002, doi:10.1126/science.1070821). — [Wikipedia: Self-assembly](https://en.wikipedia.org/wiki/Self-assembly)
- **[OBS + MODEL + SIM] Protein folding.**
  - Levinthal (1969 estimate: 3³⁰⁰ ≈ 10¹⁴³ conformations) concluded folding must be guided. Landscape theory instead describes a funnel with many routes, local minima from frustration, and a transition-state saddle (nucleation–condensation).
  - Timescales: helices form in about 100 ns and β-turns in about 1 µs; the fastest folders take microseconds. Slow folders pass through intermediates and can be limited by proline isomerisation. Small single-domain proteins often fold in one step.
  - Observing:
    - Trp/Tyr fluorescence and CD, with stopped-flow mixing giving chevron plots.
    - Phi-value analysis; laser temperature jump; photochemical triggers.
    - Optical tweezers and AFM, where the src SH3 domain shows several unfolding paths.
    - NMR CPMG relaxation dispersion for sparsely populated intermediates (SOD1).
  - Simulation: molecular dynamics (Levitt and Warshel 1975; Anton reached 2.936 ms for NTL9).
  - AlphaFold (CASP 2020) scored above 90 GDT on about two-thirds of targets but does not reveal the physical folding mechanism.
  - Folding often starts co-translationally.
  - Source: [Wikipedia: Protein folding](https://en.wikipedia.org/wiki/Protein_folding) (cites Anfinsen 1973, doi:10.1126/science.181.4096.223; Dobson 2003, doi:10.1038/nature02261)
- **[RECON, unverified] Bowen's reaction series (1920s; 1928 book).**
  - Discontinuous branch: olivine → pyroxene → amphibole → biotite.
  - Continuous branch: Ca-rich → Na-rich plagioclase.
  - Late phases: K-feldspar, muscovite, quartz.
  - It is an idealised order derived from experimental phase equilibria and rock textures, and real magmas depart from it.
  - No source page could be fetched in this session.

### Inferences
- Assembly "sequences" are stated as stage orders: nucleus before growth, metastable before stable, unfolded before intermediate before native. The stages most directly observed are bulk signals over time and, recently, single-particle tomography. The stage order itself is mostly model-assigned, and the 2026 tomography work bears directly on the classical model's assumption of a sharp-edged nucleus.
- Folding shows the field moving from a pathway (one sequence) to an ensemble (many sequences with a shared funnel). In that shift, what is observable (rates, phi values, force-extension traces) stays the same while the interpretation changes.

### Gaps
- Not checked in this session [unverified]:
  - Ostwald's step rule, beyond the general statement above.
  - Non-classical calcium carbonate pathways (amorphous precursors, prenucleation clusters) and liquid-cell TEM evidence.
  - Pathway complexity, kinetic traps and seeded or living supramolecular polymerisation in self-assembly (Meijer, Würthner, Takeuchi and Sugiyasu).
  - Bowen's series.
  - Molten-globule and hydrogen-exchange pulse-labelling evidence for folding intermediates.
  - The 2024 Nobel for protein structure prediction.

---

## Observing sequences in time: femtochemistry, pump–probe, ultrafast electron diffraction, attosecond science, time-resolved serial crystallography at XFELs, single-molecule kinetics, stopped-flow, flash photolysis

### Takeaway
Every time-resolved method records an observable (absorbance, fluorescence, diffraction intensity, photoelectron yield, force, current) against a controlled delay or real time. The order of states that appears is reconstructed by fitting kinetic or structural models. The sources say this often needs several techniques, because overlapping signals must be separated. Instrument limits set which "nows" can be seen: millisecond mixing, microsecond jumps, femtosecond pulses (below 50 fs in UED), 43 as optical pulses, and 30 fs XFEL pulses.

### Cited Findings
- **[OBS] Mixing and relaxation methods.**
  - Stopped-flow mixes in about a millisecond, so it is unsuitable for half-lives below about 0.01 s.
  - Temperature- and pressure-jump methods perturb an equilibrium and observe its relaxation. Shock tubes raise gas temperatures by more than 1000 K, and H₃O⁺ + OH⁻ neutralisation has a half-life of 1 µs or less.
  - Flash photolysis makes radicals with a pulse.
  - History [prior]: Wilhelmy (1850) used an integrated rate law for sucrose inversion.
  - Source: [Wikipedia: Chemical kinetics](https://en.wikipedia.org/wiki/Chemical_kinetics)
- **[OBS] Flash photolysis.** A strong pump pulse (flash lamp, or ns, ps or fs laser) excites the sample and weaker probe pulses record absorption over time. It dates from 1949 and is linked to the 1967 Nobel. The page credits Eigen, Norrish and Porter jointly with developing it; standard accounts attribute flash photolysis to Norrish and Porter and relaxation methods to Eigen [unverified in session]. — [Wikipedia: Flash photolysis](https://en.wikipedia.org/wiki/Flash_photolysis)
- **[OBS→RECON] Femtochemistry.**
  - Pump–probe: the pump starts the reaction and the probe samples it after a set delay. Scanning the delay reconstructs how the reaction progresses.
  - Zewail coined the term in 1988 (Science, doi:10.1126/science.242.4886.1645).
  - Example: in Br₂ dissociated at 400 nm, the electrons localise on the atoms after 140 fs and the atoms are 6.0 Å apart by 160 fs (Li et al. 2010, doi:10.1073/pnas.1014723107).
  - Caveats: intermediate steps cannot always be deduced from start and end products, and claims of controlling reactions are still controversial.
  - Source: [Wikipedia: Femtochemistry](https://en.wikipedia.org/wiki/Femtochemistry)
  - Zewail's Nobel lecture (1999 prize) was titled "Femtochemistry: Atomic-Scale Dynamics of the Chemical Bond Using Ultrafast Lasers" (Angew. 2000, doi:10.1002/1521-3773(20000804)39:15<2586::AID-ANIE2586>3.0.CO;2-O). He also contributed to ultrafast electron diffraction (doi:10.1002/hlca.200390147). — [Wikipedia: Ahmed Zewail](https://en.wikipedia.org/wiki/Ahmed_Zewail)
- **[OBS→MODEL] Transient-absorption analysis.** Ground-state bleach, excited-state absorption and stimulated-emission bands overlap and must be deconvolved. Several rate constants can be extracted by nonlinear least squares, but identifying which process each belongs to is hard and often needs several ultrafast techniques together. Fluorescence decays are fitted as the instrument response convolved with the sample's response. — [Wikipedia: Ultrafast laser spectroscopy](https://en.wikipedia.org/wiki/Ultrafast_laser_spectroscopy)
- **[OBS→RECON] Ultrafast electron diffraction.**
  - Diffraction patterns recorded at many pump–probe delays make a "motion picture".
  - Radio-frequency compression has brought resolution well below 50 fs. Sub-10 fs pulses are needed for the fastest gas-phase and solid-state dynamics.
  - Weak signals from reversible processes may need up to about 10⁸ shots. Packing more charge into a pulse broadens it, trading signal against time resolution.
  - Source: [Wikipedia: Ultrafast electron diffraction](https://en.wikipedia.org/wiki/Ultrafast_electron_diffraction) (cites Filippetto et al. 2022, doi:10.1103/RevModPhys.94.045004; Ischenko et al. 2017, doi:10.1021/acs.chemrev.6b00770)
- **[OBS→RECON] Time-resolved crystallography.** A pump (usually a laser) starts the reaction in the crystal and X-ray probes record diffraction at set delays. The time resolution is the probe pulse length. Conventional repeated pump–probe needs a reaction that resets.
  - The alternative is diffusion and trapping, by pH, inhibitors, low temperature or flash-freezing, which can only see intermediates that can be trapped.
  - Requirements: the protein must be active in the crystal, the reaction triggerable there, and the intermediate well populated, preferably above 25%.
  - Source: [Wikipedia: Time-resolved crystallography](https://en.wikipedia.org/wiki/Time_resolved_crystallography) (cites Hajdu et al. 2000, doi:10.1038/80911; β-lactam synthetase snapshots, doi:10.1073/pnas.232361199)
- **[OBS; instrument] X-ray free-electron lasers.**
  - LCLS had first light in April 2009. The LCLS-II upgrade (2022 per the page) runs at up to about 10⁶ pulses per second (the exponent was lost in the page rendering).
  - XFELs use self-amplified spontaneous emission (SASE). Facilities include the European XFEL, SACLA, SwissFEL and PAL-XFEL.
  - "Diffraction before destruction": pulses short enough to record a pattern before the sample is destroyed (Chapman et al. 2014, doi:10.1098/rstb.2013.0313). 30 fs pulses gave 0.8 nm in protein imaging.
  - Source: [Wikipedia: Free-electron laser](https://en.wikipedia.org/wiki/Free-electron_laser) (also cites Doerr 2018, doi:10.1038/s41592-018-0205-x; Wang et al. 2024 on millijoule femtosecond X-ray pulses, doi:10.1103/PhysRevLett.132.035002)
- **[OBS; 2023 Nobel context] Attosecond science.**
  - The 2023 Nobel Prize in Physics went to L'Huillier, Krausz and Agostini for methods that generate attosecond light pulses to study electron dynamics in matter.
  - Isolated attosecond pulses came from high-harmonic generation in 2004 and 2006. The shortest light pulse on record is 43 as (doi:10.1364/OE.25.027506).
  - Observed in atoms: photoemission delays (doi:10.1126/science.1189401).
  - Observed in molecules: electron localisation after photoionisation (doi:10.1038/nature09084); dynamics in phenylalanine (Calegari 2014, doi:10.1126/science.1254061); IBr curve crossing (doi:10.1126/science.aax0076).
  - Reviews: Nisoli et al. 2017 (doi:10.1021/acs.chemrev.6b00453); "The Birth of Attochemistry" (2019, doi:10.1364/OPN.30.7.000032).
  - Source: [Wikipedia: Attosecond physics](https://en.wikipedia.org/wiki/Attosecond_physics)
- **[OBS] Single-molecule kinetics, as seen in this session.**
  - SMRT sequencing watches one polymerase in a zero-mode waveguide (about 70 nm wide, about 20 zL observation volume). The timing between incorporations reveals base methylation (doi:10.1038/nmeth.1459). — [Wikipedia: PacBio SMRT](https://en.wikipedia.org/wiki/PacBio_SMRT)
  - Single-molecule data give replisome exchange times: Pol III* about 10 s, β2 clamp 47 s, DnaB helicase about 15 min. — [Wikipedia: DNA polymerase](https://en.wikipedia.org/wiki/DNA_polymerase)
  - Optical tweezers show several unfolding paths for src SH3. — [Wikipedia: Protein folding](https://en.wikipedia.org/wiki/Protein_folding)

### Inferences
- What is observed in time-resolved work is always a delay-indexed signal. "Molecular movies" are reconstructions in which a frame order (prior, now, next) comes from the delay axis, and the identities of the frames come from fitting structures or kinetic schemes. Where signals overlap (transient absorption) or occupancy is partial (crystallography, preferably above 25%), the assigned sequence depends on the model.
- Instrument limits work as membership filters. A state shorter than the probe pulse, or populated below detection, is averaged out and cannot enter the observed sequence. This matches why transition states remain inferred even in femtochemistry.

### Gaps
- Not checked in this session [unverified]:
  - The 1999 Nobel citation wording.
  - Zewail's ICN and NaI experiments.
  - Landmark time-resolved serial crystallography "movies" (photoactive yellow protein, bacteriorhodopsin, photosystem II, myoglobin, mix-and-inject enzymes).
  - The debate over multiphoton excitation in XFEL pump–probe work.
  - Gas-phase ultrafast diffraction movies (for example, cyclohexadiene ring-opening).
  - Whether attosecond charge migration has been shown to decide a chemical outcome.
  - Single-molecule FRET and single-molecule Michaelis–Menten work (English et al. 2006).

---

## Reading sequences chemically: Edman, Sanger, sequencing-by-synthesis, nanopore, mass-spectrometric fragment ladders, chromatographic elution order

### Takeaway
Each read-out converts a physical order into a sequence of symbols. Sanger sorts chain-terminated fragments by size so that elution order becomes base order. Edman removes one residue per cycle. Mass-spectrometry ladders read mass differences between successive fragments. Illumina, pyrosequencing and SMRT detect one incorporation at a time. Nanopores give a current trace that a trained model decodes. Per-cycle chemistry yields limit read length, and decoding models (base callers, de novo algorithms) sit between the signal and the sequence.

### Cited Findings
- **[OBS→RECON] Sanger (1977, doi:10.1073/pnas.74.12.5463).**
  - Chemistry: dideoxynucleotides lack the 3'-OH, so each one stops extension.
  - Separation: fragments are sorted by size, first on gels and later by capillary electrophoresis. Fluorescence peaks recorded in order of elution give the base order.
  - Performance: about 99.99% accurate (the DNA sequencing page's table gives 99.9%, a conflict). Reads reach about 800 bp, with poor quality in the first 15–40 bases.
  - Fluorescent automation: 1985–86 (doi:10.1038/321674a0), commercialised 1987.
  - Source: [Wikipedia: Sanger sequencing](https://en.wikipedia.org/wiki/Sanger_sequencing)
- **[OBS→RECON] Other DNA read-outs.** — [Wikipedia: DNA sequencing](https://en.wikipedia.org/wiki/DNA_sequencing)
  - Maxam–Gilbert (1976/77): base-specific chemical cleavage in four reactions (G, A+G, C, C+T), read from autoradiographs of gels.
  - Illumina: reversible terminators added one base per cycle; clusters are imaged, then the dye and 3' block are removed.
  - Pyrosequencing (1996): each incorporation releases light through luciferase.
  - SMRT: phosphate-linked dyes detected in real time; raw error 5–15%, with high-fidelity circular-consensus reads above Q20. — [Wikipedia: PacBio SMRT](https://en.wikipedia.org/wiki/PacBio_SMRT); Eid et al. 2009 (doi:10.1126/science.1162986)
- **[OBS→MODEL] Nanopore.**
  - Observed: ionic current through a pore while a motor protein ratchets the strand through, at about 450 nt/s per the page.
  - Several bases (a k-mer) shape each current level, and neural networks decode the signal.
  - Single-read accuracy is about 92–97% (table on the DNA sequencing page).
  - The 2020 CsgG:CsgF pore improved accuracy in homopolymers (doi:10.1038/s41587-020-0570-8). In 2021 MspA reread single proteins at single-amino-acid resolution (doi:10.1126/science.abl4381).
  - Source: [Wikipedia: Nanopore sequencing](https://en.wikipedia.org/wiki/Nanopore_sequencing) (cites Kasianowicz et al. 1996, doi:10.1073/pnas.93.24.13770)
- **[OBS] Edman degradation (1950, doi:10.3891/acta.chem.scand.04-0283).**
  - Each cycle: PITC couples to the N-terminus under mild base; acid cleaves off a thiazolinone; this is converted to the PTH-amino acid, which is identified by chromatography. Then the cycle repeats.
  - Automated sequenator: 1967 (doi:10.1111/j.1432-1033.1967.tb00047.x).
  - Length: modern instruments reach above 99% per cycle and read about 30 residues reliably.
  - Limits: blocked N-termini (acetyl, pyroglutamate) prevent it, and isoaspartate stops it.
  - Sources: [Wikipedia: Edman degradation](https://en.wikipedia.org/wiki/Edman_degradation); also [Wikipedia: Protein sequencing](https://en.wikipedia.org/wiki/Protein_sequencing), which gives about 98% per cycle, about 50 residues, and about 1 pmol needed.
- **[OBS→RECON] Mass-spectrometric fragment ladders.**
  - CID breaks backbone bonds to give N-terminal ions (a, b, c) and C-terminal ions (x, y, z). The b-ion mass is the sum of residues + 1; the y-ion is the sum + 19; the a-ion is b − 28.
  - Successive ions differ by one residue mass, and complementary b + y pairs sum to the peptide mass + 2.
  - ETD and ECD give mainly c and z ions.
  - Ion nomenclature: Roepstorff and Fohlman 1984 (doi:10.1002/bms.1200111109). De novo software: Novor 2015 (doi:10.1007/s13361-015-1204-0); DeepNovo 2017 was the first deep-learning tool.
  - Source: [Wikipedia: De novo peptide sequencing](https://en.wikipedia.org/wiki/De_novo_peptide_sequencing)
  - Standard fragmentation cannot tell Leu from Ile. Mass spectrometry is now the most widely used method for protein sequencing. — [Wikipedia: Protein sequencing](https://en.wikipedia.org/wiki/Protein_sequencing)
- **[OBS→RECON] Chromatographic elution order.**
  - Observed: a chromatogram, detector signal against retention time. Stronger affinity for the stationary phase means later elution.
  - Reversed-phase reverses the normal-phase order; HILIC elution generally runs opposite to reversed-phase.
  - Identity is assigned by comparison with references or by mass spectrometry.
  - Origin: Tsvet, 1901–1905, with plant pigments. IUPAC chromatography nomenclature: 1993 (doi:10.1351/pac199365040819).
  - Source: [Wikipedia: Chromatography](https://en.wikipedia.org/wiki/Chromatography)

### Inferences
- All of these read-outs turn spatial or chemical order into temporal order (an elution sequence, a cycle number, a current trace) or into mass order, and then decode it with a model. The read sequence is a reconstruction whose error rate depends on per-cycle chemistry and on the decoder.
- Elution order is a convention tied to conditions: the same mixture comes off in a different order on a different phase.

### Gaps
- Single-molecule protein sequencing beyond 2021, nanopore modified-base calling, and 2023–26 accuracy figures were not checked [unverified].
- Sanger's insulin sequencing (1950s) was not retrieved.

---

## For each sequence: what is prior, now and next, and where the order is assigned by observation versus by model

### Takeaway
Across chemistry, the order of events is directly observed only where a clock, a cycle counter or a separation axis is part of the experiment. Examples: pump–probe delays, Edman cycle numbers, elution times, PCR cycles, single-molecule traces. Everywhere else (mechanisms, rate-determining or turnover-determining states, intermediates between detectable species, filling orders, assembly stages) the order is assigned by a model fitted to such observations, or fixed by convention.

### Cited Findings (summary map, each row drawn from sources cited above)
| Sequence | Prior → now → next | Order assigned by | Label |
|---|---|---|---|
| Elementary-step mechanism | reactant → TS → intermediate → TS → product | Rate law, isotope effects, intermediates detected; the TS itself is inferred ([Reaction mechanism](https://en.wikipedia.org/wiki/Reaction_mechanism)) | RECON + MODEL |
| Rate-controlling step / TDI–TDTS | the controlling state can sit anywhere in the cycle and can switch with concentrations ([Gold Book R05139](https://goldbook.iupac.org/terms/view/R05139); [Kozuch–Shaik](https://cris.iucc.ac.il/en/publications/how-to-conceptualize-catalytic-cycles-the-energetic-span-model/)) | Sensitivity of a kinetic model | MODEL |
| IRC / MOJ path | reactant minimum → saddle → product minimum | Computed PES ([Maeda 2015](https://glaserr.missouri.edu/vitpub/teaching/8330f16/Maeda_et_al-2015-IRC.pdf)) | SIM/MODEL |
| Bifurcating reactions | one TS → product distribution | Trajectories, tested against product ratios ([PAC 2017](https://www.degruyterbrill.com/document/doi/10.1515/pac-2017-0104/html); [NPR 2025](https://pubs.rsc.org/en/content/articlehtml/2026/np/d5np00064e)) | SIM vs OBS |
| Chain reaction | initiation → propagation/branching → termination | Radical-count convention plus fitted rate law ([Free radical](https://en.wikipedia.org/wiki/Free_radical); [Liang & Law](https://collaborate.princeton.edu/en/publications/an-analysis-of-the-explosion-limits-of-hydrogenoxygen-mixtures-wi/)) | CONV + MODEL |
| Autocatalysis / induction | slow → accelerating → saturating | Observed sigmoid; the cause is inferred ([Gold Book I03019](https://goldbook.iupac.org/terms/view/I03019); [RPKA](https://en.wikipedia.org/wiki/Reaction_progress_kinetic_analysis)) | OBS + RECON |
| Total synthesis | planning target→precursor; execution reversed | Design convention; step count disputed ([Chemistry World](https://www.chemistryworld.com/opinion/what-counts-as-a-step-during-chemical-synthesis/2500261.article)) | CONV |
| Template copying | template position n → n+1 (5'→3'; N→C) | Fixed by the template; checked by sequencing ([Biopolymer](https://en.wikipedia.org/wiki/Biopolymer)) | OBS |
| Statistical copolymer | terminal unit → next unit with probability set by r1, r2 | Markov model fitted to composition and NMR ([Mayo–Lewis](https://en.wikipedia.org/wiki/Mayo%E2%80%93Lewis_equation)) | MODEL |
| Madelung filling | 1s→2s→2p→… | Empirical rule with exceptions ([Electron configuration](https://en.wikipedia.org/wiki/Electron_configuration)) | CONV/MODEL |
| Nucleation → growth | supersaturated → nucleus → crystal | Classical theory; challenged by 2026 tomography ([CNT](https://en.wikipedia.org/wiki/Classical_nucleation_theory)) | MODEL vs OBS |
| Folding | unfolded → (intermediates) → native | Ensemble funnel model plus kinetic and single-molecule observing ([Protein folding](https://en.wikipedia.org/wiki/Protein_folding)) | OBS + MODEL + SIM |
| Time-resolved "movie" | frame t → t + Δt | The delay axis is observed; frame identities are fitted ([UED](https://en.wikipedia.org/wiki/Ultrafast_electron_diffraction); [Ultrafast spectroscopy](https://en.wikipedia.org/wiki/Ultrafast_laser_spectroscopy)) | OBS + RECON |
| Read-outs (Sanger, Edman, MS, nanopore) | fragment/cycle/ion/current k → k+1 | The separation axis or cycle count is observed; symbols are decoded by models ([Sanger](https://en.wikipedia.org/wiki/Sanger_sequencing); [Edman](https://en.wikipedia.org/wiki/Edman_degradation); [De novo](https://en.wikipedia.org/wiki/De_novo_peptide_sequencing); [Nanopore](https://en.wikipedia.org/wiki/Nanopore_sequencing)) | OBS + RECON |

### Inferences
- Membership criteria for sequence-defining classes are mostly stated in chemistry's own definitions:
  - Elementary: no intermediate detected or needed.
  - Intermediate: lifetime longer than one vibration.
  - Concerted: changes within one elementary reaction.
  - Chain step: by change in radical count.
  - Domino: same conditions, each step dependent on the one before.
  - Living polymerisation: no transfer and no termination.
  - Rate-controlling step: the largest control function.
  
  Several of these are negative criteria (absence of evidence) or model sensitivities, which is why membership can be reassigned when detection improves or the model changes.
- Status markers gathered:
  - Reopened: classical nucleation's sharp interface (2026); single-pathway mechanisms (bifurcations, 2017 → 2025).
  - Recent: step-economy counting conventions (disputed about 2016); AI planning (2018 → 2025, with laboratory execution reported for some systems — Coscientist 2023; the Chematica papers per news reports — and not for the December 2025 LLM planner).
  - Prior: the "rate-determining step" vocabulary, kept by IUPAC as synonyms but refined by catalysis theory.

### Gaps
- Gathering stopped because both the shared web-search budget and the hourly fetch limit ran out. Items marked [unverified] above, and the XFEL-movie, supramolecular-pathway, Ostwald-rule, Bowen-series, molecular-data-storage and multicomponent-reaction topics, need follow-up searches to be properly sourced.
