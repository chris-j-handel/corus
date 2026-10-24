# Properties, property scales, and observables versus constructs in chemistry

Compiled 23 Oct 2026. Labels: **OBS** observing · **REC** reconstruction from observings · **CONV** convention or definition · **MOD** model construct · **SIM** simulation. "Observed:" is the measured quantity (method, sample, conditions). "Adds:" is what theory, model, convention or interpretation contributes. [unverified] means not checked against a source in this session. Research limits: the shared web-search budget ran out after the first batch of queries, and the hourly fetch limit was reached later. Many publisher pages could not be fetched (ACS, RSC HTML, Nature, Frontiers, SEP, several Gold Book term pages). Wikipedia and IUPAC pages therefore serve as secondary sources. The primary DOIs they cite are marked "listed", and their content was not opened unless stated.

## Key gathered points

- Chemistry sorts properties on independent axes, each with a stated criterion and a validity domain:
  - scaling with amount (intensive vs extensive), which fails for interacting or nanoscale subsystems;
  - path dependence (state vs path functions), which fails with hysteresis;
  - dependence on particle number rather than identity (colligative), which is exact only in ideal dilute solution;
  - flux–gradient response (transport), which is non-equilibrium;
  - whether measuring changes the substance's identity (physical vs chemical), a boundary that sources concede depends on perspective.
- Magnetic and electrical classes are sign or threshold classes on measured responses: susceptibility, spontaneous magnetization, resistivity and its temperature coefficient, and zero resistance together with flux expulsion. Exchange and band models explain them afterwards. Semiconductor versus insulator has no sharp cutoff. Altermagnetism (zero net moment with spin-split bands) was predicted in 2018–2021 and reported in MnTe and CrSb by several groups in 2024.
- In two superconductivity claims, interpretation outran observation. LK-99's resistivity drop was traced to a first-order Cu2S transition (2023), and Dias's hydride papers were retracted (2022, 2023).
- Every scale examined combines three parts: a probe's measured response, an anchoring convention, and a model for transferring the number elsewhere. Examples are pKa (solvent-specific and levelled), H0 (indicator ratios), Mayr N/E (rate constants anchored to reference compounds), ET(30) (one dye's band), and donicity or acceptor parameter (one reference partner each).
- Single-number scales break where the notion has several dimensions. There is no single order of Lewis acid strength, solvent polarity needs three or four parameters, and permittivity misranks THF against CH2Cl2.
- Electronegativity has a dozen or more scales; boron alone spans 1.90–2.275 in Pauling-like units. Allen's scale ranks Ne highest. Rahm–Zeng–Hoffmann (2019; 96 elements) moves O and Cr. The IUPAC oxidation-state rules adopt Allen's scale. None of these scales is directly measurable.
- Lattice energies, single-electrode potentials and average bond energies are reconstructions or conventions, not measurements.
- Electron density and dipole moments are observables. Partial charges, oxidation states, bond orders, aromaticity indices, orbitals and resonance structures are constructs whose rival definitions disagree by design. Coulson's benzene bond order is 5/3, not 1.5. NICS is a shielding computed at an empty point in space.
- Drug-likeness classes (Lipinski, Ghose, QED) are statistical conventions; many best-selling drugs fail them.
- Structure–property rules fail at mechanism changes, steric effects, changes of medium or phase, microstructure, dopant thresholds, size effects and activity cliffs.

## 1. Property kinds: intensive/extensive, state/path, colligative, transport, physical/chemical; optical, magnetic and electrical classes

### Takeaway
Each property kind is defined by how a quantity behaves under a stated operation: dividing the system, changing the path, swapping solute identity, imposing a gradient, or reacting. Each definition carries an explicit domain of validity. Material classes are sign or threshold rules applied to measured response functions and explained afterwards by models. Some boundaries are openly conventional, and in 2024 the field admitted a new magnetic class after observation confirmed prediction.

### Cited Findings

**1a. Scaling with amount**
- **Intensive quantity** (CONV). Criterion: the quantity's magnitude does not depend on the extent of the system. IUPAC source: Green Book, 2nd ed., p. 7 — [IUPAC Gold Book, intensive quantity, doi:10.1351/goldbook.I03074](https://goldbook.iupac.org/terms/view/I03074/plain)
- **Extensive quantity** (CONV). Criterion: the quantity is additive over subsystems (Green Book; PAC 1986, 58, 1405) — [IUPAC Gold Book, extensive quantity, doi:10.1351/goldbook.E02281](https://goldbook.iupac.org/E02281.html)
- Derived rules (CONV):
  - The ratio of two extensives is intensive (density; specific and molar quantities, subscript m).
  - Some derived quantities are neither: √V grows by only √2 when the system doubles.
  - Quantities can be graded by scaling degree (0 = intensive, 1 = extensive).
  - The terms trace to Helm (1898) and Tolman (1917).
  - At small sizes, nominally intensive properties become size-dependent (quantum-dot optical response), and viscosity may be ill-defined.
  - Source: [Wikipedia, Intensive and extensive properties](https://en.wikipedia.org/wiki/Intensive_and_extensive_properties)
- Scope condition: the labels hold only if the divided samples do not interact physically or chemically when recombined — [Wikipedia, Physical property](https://en.wikipedia.org/wiki/Physical_property)
- Observed vs added. Observed: how a measured value changes when a sample is divided or merged. Adds: a definitional tag that is then attached to quantities generally.

**1b. Path dependence**
- **State vs path functions** (CONV within thermodynamic theory).
  - A state function depends only on the current equilibrium state (U, H, S, G, p, T, V). Heat and work depend on the route taken.
  - State functions have exact differentials (d); path quantities have inexact ones (δ).
  - The description breaks down for quantities that show hysteresis.
  - Source: [Wikipedia, State function](https://en.wikipedia.org/wiki/State_function)
- Observed: heats and work along particular paths (calorimetry, p–V work). Adds: the first and second laws guarantee that state functions exist, so changes measured along any path can be combined in cycles (see Born–Haber, §2).

**1c. Colligative properties**
- **Colligative** (REC + MOD limit).
  - Criterion: the property depends on the ratio of solute to solvent particles, not on the solute's identity. The term is Ostwald's (1891).
  - Members: vapour-pressure lowering; boiling-point elevation ΔTb = i·Kb·m; freezing-point depression ΔTf = i·Kf·m; osmotic pressure Π = iRT·n/V.
  - The relations are exact only for ideal solutions. At higher concentration the chemical identity of solvent and solute re-enters.
  - The van 't Hoff factor i is measured below the formula count because ions associate.
  - Used to infer molar mass (including of polymers) or degree of dissociation.
  - Source: [Wikipedia, Colligative properties](https://en.wikipedia.org/wiki/Colligative_properties)
- Observed: temperature shifts and osmotic pressure differences. Adds: the ideal-dilute model, from which particle counts and molar masses are inferred.

**1d. Transport properties**
- **Transport coefficients** (OBS within MOD laws).
  - Viscosity (Newton), thermal conductivity (Fourier), diffusion coefficient (Fick) and electrical conductivity (Ohm) are each the proportionality constant between a flux and a gradient.
  - Transport stops at equilibrium.
  - Onsager (1931; doi:10.1103/physrev.37.405, listed) derived reciprocal relations between cross-coefficients from microscopic reversibility.
  - Heat–mass transfer analogies (Chilton–Colburn) are empirical.
  - Source: [Wikipedia, Transport phenomena](https://en.wikipedia.org/wiki/Transport_phenomena)
- Observed: fluxes under imposed gradients. Adds: linear flux–force laws, valid near equilibrium, and Onsager symmetry, which is theory.

**1e. Physical vs chemical**
- **Physical property** (CONV): measurable without changing the substance's composition; measurable quantities are called observables. Sources concede the boundary is not sharp; colour, for example, is an interpretation of reflectance — [Wikipedia, Physical property](https://en.wikipedia.org/wiki/Physical_property)
- **Chemical property** (CONV): can be established only by changing the substance's chemical identity. Examples given are flammability, toxicity, enthalpy of formation, preferred oxidation states, corrosion, acidity and basicity, and catalytic activity. The page says the line can depend on the researcher's perspective, and it also lists QSAR results and the Rule of Five among chemical properties — [Wikipedia, Chemical property](https://en.wikipedia.org/wiki/Chemical_property)

**1f. Optical properties**
- **Refractive index** (OBS + MOD link).
  - Observed: the refraction angle or critical angle in a refractometer (an Abbe instrument reads to about 0.0002), at a stated vacuum wavelength, usually the sodium D line at 589 nm.
  - Also observed: dispersion (the Sellmeier fit is empirical), the complex index in absorbing media, and birefringence (Δn = n_e − n_o) in anisotropic crystals.
  - Adds: the Lorentz–Lorenz relation, which converts n into polarizability or molar refractivity.
  - Source: [Wikipedia, Refractive index](https://en.wikipedia.org/wiki/Refractive_index)
- **Solvatochromism** (OBS): an absorption band moves with the solvent. It is negative (hypsochromic) or positive (bathochromic) as polarity rises; Brooker's merocyanine and Michler's ketone are the standard examples. This is the raw observation behind the dye-based solvent scales in §2 — [Wikipedia, Solvatochromism](https://en.wikipedia.org/wiki/Solvatochromism)

**1g. Magnetic classes**
- **Diamagnet / paramagnet** (OBS classes; MOD explanation).
  - Paramagnets have a small positive susceptibility (about 10⁻⁵ to 10⁻³). It follows the Curie law (χ ∝ 1/T) until high field or low temperature, and no magnetization remains when the field is removed.
  - Model: unpaired electrons. Conduction electrons give a temperature-independent Pauli paramagnetism, opposed by Landau diamagnetism of about one-third its size.
  - Diamagnets have a negative susceptibility. In metals the dia- and paramagnetic contributions compete, and the net sign decides the class; gold is net diamagnetic.
  - Measured with sensitive balances or a SQUID.
  - Source: [Wikipedia, Paramagnetism](https://en.wikipedia.org/wiki/Paramagnetism)
- **Ferromagnet** (OBS).
  - Spontaneous magnetization below the Curie temperature (Co 1388 K, Fe 1043 K, Ni 627 K, Gd 292 K), hysteresis, domains and Barkhausen jumps.
  - Model: the exchange interaction, about 1000 times the dipolar interaction in iron.
  - Class membership depends on crystal structure and microstructure, not composition alone. Ru was reported as a fourth room-temperature ferromagnetic element (Quarterman 2018, doi:10.1038/s41467-018-04512-1, listed).
  - Source: [Wikipedia, Ferromagnetism](https://en.wikipedia.org/wiki/Ferromagnetism)
- **Néel's 1948 scheme** (doi:10.1051/anphys/194812030137, listed): ferromagnet = parallel moments; ferrimagnet = antiparallel sublattices of unequal size, leaving a net moment; antiferromagnet = equal antiparallel moments that cancel — [Wikipedia, Ferromagnetism](https://en.wikipedia.org/wiki/Ferromagnetism)
- **Antiferromagnet** (OBS + REC).
  - Landau (1933). Order vanishes above the Néel temperature, where the susceptibility peaks.
  - First shown directly by neutron diffraction on transition-metal oxides (Shull, Strauser & Wollan 1951, doi:10.1103/physrev.83.333, listed).
  - Spin canting can leave a weak net moment, as in hematite.
  - Source: [Wikipedia, Antiferromagnetism](https://en.wikipedia.org/wiki/Antiferromagnetism)
- **Altermagnet** (2024 addition).
  - Criterion: the opposite-spin sublattices are related by a real-space rotation, not by a translation or an inversion. The result is zero net magnetization with spin-split electronic bands — [Charles University news](https://kfkl.mff.cuni.cz/en/news/unveiling-altermagnets-experimental-evidence-and-spin-symmetry-characteristics); [APS Physics synopsis](https://physics.aps.org/articles/v17/s10)
  - Prediction (MOD/SIM): Šmejkal and colleagues predicted an unconventional anomalous Hall effect in 2018 and gave a spin-symmetry classification in 2021 — [IDW, Feb 2025](https://nachrichten.idw-online.de/2025/02/25/altermagnetism-recognised-among-top-10-breakthroughs-of-2024)
  - Observings:
    - Lee et al., PRL 132, 036702 (published 18 Jan 2024): in-situ ARPES on MnTe thin films showed Kramers degeneracy lifted, with spin splitting up to 370 meV coinciding with the magnetic transition — [PRL abstract page](https://link.aps.org/doi/10.1103/PhysRevLett.132.036702). The synopsis puts that transition below 267 K — [APS Physics](https://physics.aps.org/articles/v17/s10)
    - A Nature 2024 paper ("Altermagnetic lifting of Kramers spin degeneracy"; DOI 10.1038/s41586-023-06907-7 from the link) used ARPES, including spin-resolved ARPES, on MnTe single crystals with ab initio support. The sign of the spin polarization alternates — [Charles University news](https://kfkl.mff.cuni.cz/en/news/unveiling-altermagnets-experimental-evidence-and-spin-symmetry-characteristics)
    - Osumi et al. (PRB 109, 115102, 2024): ARPES on hexagonal MnTe (T_N 307 K) found anisotropic splitting of about 0.8 eV away from high-symmetry points — [arXiv 2308.10117](https://arxiv.org/abs/2308.10117v2)
    - Orlova et al. (JETP Lett. 120, 360, 2024): magnetization of α-MnTe showed a low-field anomaly below about 85 K, which the authors read as altermagnetic — [arXiv 2403.15348](https://www.arxiv.org/abs/2403.15348)
    - CrSb was also reported in 2024 — [IDW](https://nachrichten.idw-online.de/2025/02/25/altermagnetism-recognised-among-top-10-breakthroughs-of-2024)
  - Status: reproduced across groups and methods in 2024 and listed by Science among the top breakthroughs of 2024 — [IDW](https://nachrichten.idw-online.de/2025/02/25/altermagnetism-recognised-among-top-10-breakthroughs-of-2024)
  - Unresolved discrepancies: 267 K (films) vs 307 K (bulk T_N), and 0.37 eV vs about 0.8 eV splitting, which likely refer to different samples and bands; no source seen reconciles them.

**1h. Electrical classes**
- **Classes by resistivity** (OBS thresholds; MOD band explanation).
  - Metals: about 10⁻⁸ Ω·m; resistivity rises with temperature and levels off at a defect-set residual value.
  - Semiconductors: intermediate; resistivity falls with temperature (roughly Arrhenius) and is very sensitive to doping.
  - Insulators: about 10¹⁶ Ω·m (glass 10¹¹–10¹⁵).
  - Electrolytes conduct through ions.
  - Superconductors have exactly zero resistivity below Tc.
  - Band model: the Fermi level lies inside a band in metals and in a gap in semiconductors and insulators.
  - Source: [Wikipedia, Electrical resistivity and conductivity](https://en.wikipedia.org/wiki/Electrical_resistivity_and_conductivity)
- **Semiconductor vs insulator** (CONV boundary): there is no numeric cutoff. Wide-gap "semi-insulators" such as GaAs exist, and TiO2 is used as either. Doping changes conductivity by factors of thousands to millions; 0.001% As in Ge gives about 10⁴ times — [Wikipedia, Semiconductor](https://en.wikipedia.org/wiki/Semiconductor)
- **Superconductor** (OBS criterion: zero resistance plus Meissner flux expulsion).
  - Other observables: London penetration depth of about 100 nm; Tc; critical fields (type I has one, Hc; type II has Hc1 and Hc2 with vortices); critical current.
  - Adds: BCS/Eliashberg theory for conventional superconductors.
  - The cuprate pairing mechanism remains unclear and its symmetry controversial (status: open). H2S reached 203 K at about 90 GPa (Drozdov 2015, doi:10.1038/nature14964, listed).
  - Source: [Wikipedia, Superconductivity](https://en.wikipedia.org/wiki/Superconductivity)

**1i. Superconductivity claims, 2020–2025: observing vs interpretation**
- **CSH** (Dias group, Nature 2020; about 288 K at about 260 GPa): retracted Sept 2022 over a non-standard background subtraction, which all nine authors disputed at the time — [Physics World](https://physicsworld.com/a/superconductivity-damaged-as-researchers-look-to-move-on-from-retractions/)
- **Lu–N–H** (Nature, March 2023; 294 K at 1 GPa):
  - Editor's note 1 Sept 2023; 8 of 11 authors requested retraction; retracted 7 Nov 2023 — [Smithsonian](https://www.smithsonianmag.com/smart-news/paper-that-claimed-a-room-temperature-superconductor-breakthrough-is-retracted-by-the-journal-nature-180981774/)
  - Reported reproduction success of about 35%; independent attempts failed — [Physics World](https://physicsworld.com/a/superconductivity-damaged-as-researchers-look-to-move-on-from-retractions/)
  - An investigation found evidence of data fabrication — [Peplow 2024, Engineering, doi:10.1016/j.eng.2024.06.005](https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2024.06.005)
  - Status: retracted.
- **LK-99** (Cu-substituted lead apatite, July 2023; claimed Tc up to about 400 K at ambient pressure).
  - Observed in the original work: partial levitation and abrupt resistance changes — [Peplow 2024](https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2024.06.005)
  - Reinterpretation (IOP-CAS, published in *Matter*): pure Cu2S and Cu2S-containing LK-99 both drop sharply near 385 K, with thermal hysteresis. The cause is a first-order hexagonal-to-monoclinic transition, with resistivity falling 3–4 orders of magnitude but never reaching zero — [IOP-CAS](https://english.iop.cas.cn/rh/rp/202311/t20231127_645009.html)
  - Later work: the pure phase is insulating; neutron data show no superconductivity down to 10 K; removing Cu2S removes the drop. Consensus is negative, but one original author still maintains the claim (status Dec 2025) — [Liu et al., RSC Adv. 2025, doi:10.1039/d5ra07404e](https://pubs.rsc.org/en/content/articlepdf/2025/ra/d5ra07404e)
  - In January 2024 two Chinese teams reported "hints" in a similar material; this is not established — [Peplow 2024](https://www.engineering.org.cn/engi/EN/10.1016/j.eng.2024.06.005)

### Inferences
- Most class criteria come with an explicit validity domain: ideal-dilute (colligative), near-equilibrium (linear transport), non-interacting subdivisions (intensive/extensive), above a size threshold, and no hysteresis (state functions).
- Magnetic and electrical class membership depends on conditions (T, P, field, frequency, microstructure). The same composition can belong to different classes under different conditions.
- In practice, acceptance of superconductivity separates observation from interpretation. A resistance drop or partial levitation alone is not enough; zero resistance plus flux expulsion, independently reproduced, is required.

### Gaps
- Primary altermagnetism papers (Šmejkal et al. 2022 PRX; the CrSb reports) were not opened. The contested status of RuO2 as an altermagnet was not checked [unverified].
- The Wikipedia diamagnetism page could not be fetched. The universality of a diamagnetic contribution in all matter is [unverified].
- Nickelate superconductivity (La3Ni2O7 near 80 K under pressure, 2023; ambient-pressure films reported 2025) is [unverified].

## 2. Property scales and their disagreements

### Takeaway
Every scale examined breaks into three parts:
1. an observed response of a probe or reference reaction;
2. an anchoring convention (reference compound, zero point, solvent, temperature, units);
3. a model that licenses carrying the number to new contexts.

Disagreements between scales for "the same" notion mostly arise in parts 1 and 2. They are largest where the notion has several dimensions (Lewis acidity, solvent polarity, hardness, electronegativity). IUPAC's recent changes renamed conventions ("donor number" and "acceptor number" are now called misnomers) but left the observings untouched.

### Cited Findings

**2a. Brønsted acidity**
- **Aqueous pKa** (REC + CONV).
  - Observed: glass-electrode EMF against titrant volume (reliable only between about pH 2 and 11); absorbance or fluorescence against pH; NMR shift against pH (time-averaged); ITC heats.
  - Conditions: usually a high-ionic-strength medium such as 0.1 M NaNO3, so values belong to that medium.
  - Adds: the HA ⇌ H⁺ + A⁻ equilibrium model; activity conventions that make the constant dimensionless; extrapolation from mixed solvents; computed values for strong acids (aqueous HCl about −9.3).
  - Source: [Wikipedia, Acid dissociation constant](https://en.wikipedia.org/wiki/Acid_dissociation_constant)
- **Solvent and levelling disagreements.**
  - Usable windows: about −2 to 12 in water and 1 to 30 in DMSO.
  - Acetic acid: 4.756 (water) / 12.6 (DMSO) / 23.51 (MeCN). Phenol: 9.99 / 18.0 / 29.14.
  - Homoconjugation boosts acidity in aprotic solvents.
  - Water levels acids below about pKa 0 to H3O⁺.
  - The article states that no universal, solvent-independent scale has been developed.
  - Source: [Wikipedia, Acid dissociation constant](https://en.wikipedia.org/wiki/Acid_dissociation_constant)
  - In anhydrous acetic acid, HClO4 is about 5000 times stronger than HCl; superacids are studied in SO2 or SO2ClF — [Wikipedia, Leveling effect](https://en.wikipedia.org/wiki/Leveling_effect)
- **Water's own pKa**: 14 in water but 32 in DMSO. The page concludes that pKa is not an intrinsic molecular property, whereas proton affinity is — [Wikipedia, Proton affinity](https://en.wikipedia.org/wiki/Proton_affinity). The textbook 14 vs 15.7 dispute is treated by Silverstein & Heller 2017 (J. Chem. Educ., doi:10.1021/acs.jchemed.6b00623, listed there); that they favour 14.0 on standard-state grounds is [unverified].
- **pH** (CONV): defined through hydrogen-ion activity. The practical scale is traceable by international agreement to IUPAC primary standards (Covington, Bates & Durst 1985, doi:10.1351/pac198557030531, listed). A cross-phase "unified pH scale" was proposed by Himmel et al. 2010 (doi:10.1002/anie.201000252, listed) — [Wikipedia, pH](https://en.wikipedia.org/wiki/PH). Its basis, the absolute chemical potential of the proton, is [unverified]. The pKa article's statement that no universal scale has been developed conflicts with that proposal.
- **Hammett acidity function H0** (REC + CONV).
  - Observed: the protonation ratio of indicator bases (primary aromatic amines) in concentrated acids.
  - Adds: an extension of the pH idea to concentrated media. IUPAC defines an acidity function as a measure of a solvent system's ability to donate or accept hydrons — [IUPAC Glossary of physical organic chemistry 2021 (Perrin et al., publ. 2022)](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html)
  - H0 and pKa rankings usually agree but can diverge. Neat HF has H0 ≈ −15, which makes it a superacid — [Wikipedia, Acid strength](https://en.wikipedia.org/wiki/Acid_strength)
  - H₋ is the companion function for superbasic media — [Wikipedia, Acid dissociation constant](https://en.wikipedia.org/wiki/Acid_dissociation_constant)
- **Superacid** (CONV): membership requires being more acidic than 100% H2SO4 — [IUPAC Glossary 2021](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html). All of the following are [unverified]: H0 of 100% H2SO4 ≈ −12; HSO3F ≈ −15; HF–SbF5 quoted anywhere from about −21 to −28 depending on composition and source; carborane acids called the strongest isolable acids but ranked by IR or gas-phase scales because, as solids, they lack H0 values.
- **Gas-phase acidity and basicity** (OBS ion thermochemistry + REC).
  - IUPAC allows acidity to be quantified by the enthalpy or Gibbs energy of gas-phase deprotonation — [IUPAC Glossary 2021](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html)
  - Proton affinity (PA) = −ΔH of protonation; gas-phase basicity = −ΔG.
  - F⁻ has PA 1554 kJ/mol, yet HF is weak in water (pKa 3.15) because hydration stabilizes F⁻. Other values: OH⁻ 1635; He 178 (weakest base); o-diethynylbenzene dianion 1843 (strongest; Poad 2016, doi:10.1039/C6SC01726F, listed).
  - The page warns that some table entries may be mislabelled.
  - Source: [Wikipedia, Proton affinity](https://en.wikipedia.org/wiki/Proton_affinity)
  - The gas-phase amine order Me3N > Me2NH > MeNH2 > NH3 changes in water — [Wikipedia, Acid dissociation constant](https://en.wikipedia.org/wiki/Acid_dissociation_constant)

**2b. Nucleophilicity and electrophilicity**
- **Swain–Scott (1953)** (REC + CONV): log(k/k_water) = s·n in water at 25 °C, with s = 1 for MeBr. Values of n: acetate 2.7, Cl⁻ 3.0, N3⁻ 4.0, OH⁻ 4.2, I⁻ 5.0, S2O3²⁻ 6.4.
- **Ritchie (1972)** (REC + CONV): N+ with no substrate term ("constant selectivity").
- **Mayr–Patz (1994; doi:10.1002/anie.199409381, listed)** (REC + CONV + MOD separability).
  - Observed: second-order rate constants at 20 °C.
  - Equation: log k = s(N + E), with s = 1 anchored on 2-methyl-1-pentene.
  - Benzhydrylium E runs from +6.2 (Cl) to −7.02 (NMe2). N (s): piperidine 15.63 (0.64), methoxide 10.49 (0.68), water 5.20 (0.89).
  - A later unified form adds sE and sN.
- Basicity is thermodynamic and nucleophilicity kinetic. Halide nucleophilicity order reverses between protic solvents (I⁻ strongest) and aprotic solvents (F⁻ strongest).
- Source for this group: [Wikipedia, Nucleophile](https://en.wikipedia.org/wiki/Nucleophile)
- **Parr electrophilicity index ω** (1999, doi:10.1021/ja983494x, listed) (MOD/SIM): built from electronegativity and hardness and described as an "electrophilic power". Unitless values: F 3.86, Cl 3.67, Br 3.40, I 3.09, SO2 2.01, benzene 1.45, Na 0.88 — [Wikipedia, Electrophile](https://en.wikipedia.org/wiki/Electrophile)
- **Kinds of disagreement.** Mayr's E is calibrated on measured rates in stated solvents. ω is a gas-phase quantity from conceptual DFT. No source seen compares them. Mayr's 2011 critique of HSAB treatments of ambident reactivity, which favours Marcus-type analysis with kinetic and thermodynamic control, is [unverified]; the Mayr database page could not be fetched.

**2c. Lewis acidity and basicity**
- **Donor number** (REC + CONV).
  - Gutmann 1976: −ΔH of the 1:1 adduct with SbCl5 in dilute 1,2-dichloroethane (which has DN 0), in kcal/mol for historical reasons. It is often measured by NMR, which assumes a complexation model.
  - Values: MeCN 14.1, acetone 17, THF 20, DMF 26.6, DMSO 29.8, pyridine 33.1, Et3N 61.
  - A critical review found serious limitations — [Wikipedia, Donor number](https://en.wikipedia.org/wiki/Donor_number)
  - IUPAC 2021 prefers "donicity" and calls "donor number" a misnomer — [IUPAC Glossary 2021](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html)
- **Acceptor number** (OBS NMR shift + CONV two-point anchor).
  - Gutmann 1975, adapted by Beckett 1996: the ³¹P shift of Et3PO, with AN = 2.21 × (δ − 41.0). Anchors: hexane AN 0 (41.0 ppm) and SbCl5 AN 100 (86.1 ppm).
  - Values: BF3 89, BI3 115, B(C6F5)3 82, AlCl3 87, TiCl4 70.
  - The page itself says two parameters are needed and that no universal order exists — [Wikipedia, Gutmann–Beckett method](https://en.wikipedia.org/wiki/Gutmann%E2%80%93Beckett_method)
  - IUPAC deprecates "acceptor number" in favour of "acceptor parameter" — [IUPAC Glossary 2021](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html)
- **Drago ECW model** (MOD fitted to measured enthalpies): −ΔH = EA·EB + CA·CB + W. The source concludes there is no single order of Lewis acid or base strength. Measured BF3 adduct enthalpies range from about 150 kJ/mol (quinuclidine) to about 52 kJ/mol (tetrahydrothiophene) — [Wikipedia, Lewis acids and bases](https://en.wikipedia.org/wiki/Lewis_acids_and_bases)

**2d. Solvent polarity**
- **Relative permittivity εr** (OBS bulk response used as a proxy).
  - Observed: a capacitance ratio (static) or RF and resonance methods. εr is complex and frequency-dependent.
  - Values: water 78.4 (25 °C), MeCN 37.5, MeOH 32.7, EtOH 24.3, CH2Cl2 9.1, THF 7.6, Et2O 4.3, benzene 2.3, hexane 1.89. "Dielectric constant" is a deprecated name.
  - Misrankings: CH2Cl2 (9.08) mixes poorly with water while THF (7.52) is miscible, because THF accepts hydrogen bonds. Iodoethane (7.6) exceeds acetic acid (6.25) through polarizability rather than polarity.
  - Source: [Wikipedia, Relative permittivity](https://en.wikipedia.org/wiki/Relative_permittivity)
- **ET(30)** (OBS single probe → CONV scale).
  - Defined from the longest-wavelength intramolecular charge-transfer band of a specific pyridinium-N-phenolate betaine (Reichardt's) dye — [IUPAC Glossary 2021](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html)
  - Expressed as a transition energy in kcal/mol. The Nile-red ET(33) scale correlates only roughly — [Wikipedia, Solvent](https://en.wikipedia.org/wiki/Solvent)
  - [unverified]: ETN normalized to TMS = 0 and water = 1; water's ET(30) ≈ 63.1 kcal/mol; the dye is insoluble in some nonpolar solvents.
- **Multi-probe and other scales.**
  - Kosower Z: the pyridinium iodide charge-transfer band.
  - Grunwald–Winstein Y: solvolysis rates, reflecting positive-charge build-up.
  - Kamlet–Taft π*, α, β: from dye wavelength shifts; π* is anchored at cyclohexane 0 and DMSO 1 [unverified]. Key paper: Kamlet et al. 1983, J. Org. Chem. 48, 2877, doi:10.1021/jo00165a018, listed — [Wikipedia, Solvatochromism](https://en.wikipedia.org/wiki/Solvatochromism)
  - Hildebrand δ: the square root of cohesive energy density; usable only for nonpolar systems.
  - Hansen δD, δP, δH: mixture values are volume-weighted averages.
  - Sources: [Wikipedia, Solvent](https://en.wikipedia.org/wiki/Solvent)
  - Catalán: four parameters (H-bond donor, H-bond acceptor, polarizability, dipolarity) — [IUPAC Glossary 2021](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html)
  - The Hansen distance Ra² = 4(ΔδD)² + (ΔδP)² + (ΔδH)², with an empirical factor of 4, is [unverified].
- **2024 development (SIM)**: Gregory, Wanless, Webber, Craig & Page (PCCP 26, 20750, doi:10.1039/D4CP01975J) proposed a first-principles charge-density parameter (ϸ) as an alternative to empirical solvent parameters. Wikipedia says only that it seems to reproduce many experimental scales. Status: proposed — [Wikipedia, Solvent](https://en.wikipedia.org/wiki/Solvent)
- **Internal inconsistency**: the same page lists THF as nonpolar in one table and polar aprotic in another, and labels CH2Cl2 polar despite εr below its own stated cutoff of 15 — [Wikipedia, Solvent](https://en.wikipedia.org/wiki/Solvent)

**2e. Hardness and softness**
- **HSAB** (MOD, qualitative).
  - Hard means small and weakly polarizable; soft means large and polarizable. Hard–hard and soft–soft adducts are favoured.
  - The source says the scheme was never quantified. Its later enthalpy-vs-entropy reading carries a "citation needed" flag — [Wikipedia, Lewis acids and bases](https://en.wikipedia.org/wiki/Lewis_acids_and_bases)
  - Lewis base strength needs at least two parameters: hardness plus strength (HSAB), or electrostatic plus covalent terms (ECW) — [Wikipedia, Donor number](https://en.wikipedia.org/wiki/Donor_number)
- **Absolute hardness** (REC from I and A under a MOD finite-difference reading).
  - Pearson 1985 (JACS 107, 6801, doi:10.021/ja00310a009, listed) — [Wikipedia, Electronegativity](https://en.wikipedia.org/wiki/Electronegativity). The negative of Mulliken electronegativity is sometimes equated with the chemical potential — same source.
  - Pearson's absolute electronegativity for boron is 4.29 eV — [KnowledgeDoor, boron](https://knowledgedoor.com/2/elements_handbook/boron.html)
  - The working formula η ≈ (I − A)/2 and the Parr–Pearson 1983 paper are [unverified].

**2f. Electronegativity**
- **Concept**: "the power of an atom to attract electrons to itself" (Pauling) — [IUPAC Gold Book, doi:10.1351/goldbook.E01990, v5.0.0, 2025](https://goldbook.iupac.org/terms/view/E01990/plain). Electronegativity "cannot be directly measured"; it is computed from other properties — [Wikipedia, Electronegativity](https://en.wikipedia.org/wiki/Electronegativity). Karol says the same — [Karol 2020, Chem. Int.](https://www.degruyterbrill.com/document/doi/10.1515/ci-2020-0305/html?lang=en)
- **Pauling** (REC from thermochemistry + CONV).
  - The excess bond dissociation energy of A–B over the mean of A–A and B–B fixes only differences.
  - Conventions: hydrogen anchor, units, and the sign of the square root, which Pauling chose intuitively. The Gold Book formula still anchors H at 2.1 (prior) — [Gold Book](https://goldbook.iupac.org/terms/view/E01990/plain)
  - Current tables use H = 2.20 (Allred 1961 revision), Cs 0.79 and F 3.98. Each element needs at least two bond types, and values depend on environment — [Wikipedia, Electronegativity](https://en.wikipedia.org/wiki/Electronegativity)
- **Mulliken** (REC): the mean of first ionization energy and electron affinity, in eV, usually linearly rescaled. It requires measured electron affinities, which exist for 72 elements — [Gold Book](https://goldbook.iupac.org/terms/view/E01990/plain); [Wikipedia, Electronegativity](https://en.wikipedia.org/wiki/Electronegativity)
- **Allred–Rochow** (MOD + observed radius): Zeff from Slater's rules divided by the covalent radius squared.
- **Sanderson** (MOD): based on atomic volume; source of electronegativity equalization. Source for both: [Wikipedia, Electronegativity](https://en.wikipedia.org/wiki/Electronegativity)
- **Allen** (REC from spectra).
  - The average one-electron energy of valence electrons in ground-state free atoms; χ = (mεs + nεp)/(m + n) — [WebElements, Allen](https://webelements.co.uk/periodicity/eneg_allen/)
  - Ne ranks highest, then F, He, O. Fr 0.67; Cs 0.66 (against Pauling 0.79). The valence count is ambiguous in the d and f blocks — [Wikipedia, Electronegativity](https://en.wikipedia.org/wiki/Electronegativity)
  - IUPAC's 2014 and 2016 oxidation-state documents adopt Allen's scale.
  - Karol extended it to Z = 120 with Dirac–Fock energies (SIM): Nh 2.09, Fl 2.21, Og 3.04. The usual downward group trend reverses for the heaviest elements, which the author attributes to relativity. Allen's scale is problematic for transition elements.
  - Karol reports that the Rahm–Zeng–Hoffmann, Allen and Pauling scales agree closely for main-group elements — [Karol 2020](https://www.degruyterbrill.com/document/doi/10.1515/ci-2020-0305/html?lang=en)
- **Rahm–Zeng–Hoffmann (RZH)** (REC + SIM gap-filling; the energy partition is MOD).
  - JACS 2019, 141, 342; doi:10.1021/jacs.8b10246; online 30 Nov 2018.
  - Definition: the ground-state average valence-electron binding energy, mostly from experimental NIST atomic data, with GMC-QDPT calculations where data are missing. It covers H to Cm (96 elements); f-block values are qualitative.
  - Against Allen (69 elements): slope 0.9686, SD 0.88 eV/e (9.3%). Oxygen is the largest outlier (18.6 vs 21.4 eV/e). One Pauling unit ≈ 6 eV/e.
  - Partition: ΔE = Δ(nχ̄) + ΔV_NN − ΔE_ee. Δχ̄ can be positive even for exothermic change when multielectron terms dominate, which the authors link to polar, ionic and metallic bonding.
  - Source: [RZH paper PDF](https://old.roaldhoffmann.com/sites/all/files/644%20jacs.8b10246%20Electronegativity%20seen.pdf)
  - O and Cr move relative to their neighbours, and some elements receive values for the first time — [Cornell news, Jan 2019](https://as.cornell.edu/news/chemists-develop-new-scale-electronegativity)
  - The 2016 Rahm–Hoffmann origin paper is [unverified].
- **Spread for one element (boron)**: Pauling 2.04; Allred 2.04; Allred–Rochow 2.01; Allen 2.051 (configuration energy 12.13 eV); Mulliken–Jaffé 2.04 (sp²) or 1.90 (sp³); Sanderson 2.275, 2.19 or 1.53 (oxidation states 3, 2, 1); Boyd–Edgecombe 1.90; Nagle 2.02; Smith 1.9; Ghosh–Gupta 4.9686 eV; Pearson 4.29 eV — [KnowledgeDoor, boron](https://knowledgedoor.com/2/elements_handbook/boron.html)
- **Later work**: Karol notes Rahm and colleagues proposed extending electronegativity to compressed atoms — [Karol 2020](https://www.degruyterbrill.com/document/doi/10.1515/ci-2020-0305/html?lang=en). Thermochemical electronegativities (Tantardini & Oganov, Nat. Commun. 2021) are [unverified]; the page could not be fetched.

**2g. Polarizability**
- (REC via MOD relation.) Observed: refractive index, converted through Lorentz–Lorenz to molar refractivity — [Wikipedia, Refractive index](https://en.wikipedia.org/wiki/Refractive_index); and permittivity. Polarizability can inflate εr without "polarity", as with iodoethane — [Wikipedia, Relative permittivity](https://en.wikipedia.org/wiki/Relative_permittivity). In HSAB, softness tracks polarizability — [Wikipedia, Lewis acids and bases](https://en.wikipedia.org/wiki/Lewis_acids_and_bases)

**2h. Redox potentials**
- (OBS cell EMF + CONV zero.) Only the EMF of a complete galvanic cell can be measured. The SHE is set to 0 V (Gold Book S05912). Values are reported as reductions, link to free energy through ΔG = −nFE, and vary with T, concentration and pressure — [Wikipedia, Standard electrode potential](https://en.wikipedia.org/wiki/Standard_electrode_potential)
- **Absolute SHE potential** (REC with extra-thermodynamic assumptions): 4.44 ± 0.02 V at 25 °C (Trasatti, IUPAC 1986). It involves the work-function and Volta-potential terms and is best obtained at the point of zero charge on mercury — [Wikipedia, Absolute electrode potential](https://en.wikipedia.org/wiki/Absolute_electrode_potential). Rival values such as about 4.28 V are [unverified].

**2i. Bond dissociation energies**
- **Definitions** (CONV): D0 (0 K) versus DH°298; for example ethane C–H is 101.1 kcal/mol. D0 is less than De by the zero-point energy, and D0 ≈ DH298 − 1.5 kcal/mol for hydrocarbons.
- **Observed** (REC): spectroscopic levels, radicals from pyrolysis or photolysis, kinetics and equilibria, calorimetry, electrochemistry, combined through cycles. Typical uncertainty is ±1–2 kcal/mol.
- **Average bond energy is a bookkeeping convention**: water's O–H values of 118.8 and 101.8 average to 110.3, and methane's successive 105, 110, 101 and 81 average to 99, which none of them equals.
- **Revisions**: benzene C–H went from 103 (1965, prior) to 112.9(5). Pre-1970 values may be off by about 10. Phenol O–H spread over 85.8–91.0 between 1990 and 2004 (Mulder 2005, doi:10.1021/jp047148f, listed). H2 is known to 104.1539(1) kcal/mol.
- Source: [Wikipedia, Bond-dissociation energy](https://en.wikipedia.org/wiki/Bond-dissociation_energy)

**2j. Lattice energy**
- **Definition and sign** (CONV): the energy of forming a crystal from infinitely separated gaseous ions. Both sign conventions are in use (NaCl −786 or +786 kJ/mol). Models: Born–Landé (1918), Born–Mayer (1932), Kapustinskii (1956) — [Wikipedia, Lattice energy](https://en.wikipedia.org/wiki/Lattice_energy)
- **Not directly measurable** (REC): the Born–Haber–Fajans cycle (1919) builds it from measured enthalpy of formation, sublimation, dissociation, ionization energy and electron affinity. The basic cycle assumes full ionicity; an extended cycle handles covalency and estimates charges — [Wikipedia, Born–Haber cycle](https://en.wikipedia.org/wiki/Born%E2%80%93Haber_cycle)

**2k. logP and hydrophobicity**
- **Observed** (OBS): un-ionized solute concentrations in n-octanol and water by shake-flask (UV/VIS). HPLC retention correlated with standards is unreliable across compound classes. A two-phase pH-metric titration needs known pKa values.
- **Adds** (CONV + MOD/SIM):
  - Octanol stands in for lipid. logD (at a stated pH, often 7.4) includes ionized forms. IUPAC discourages the term "partition coefficient".
  - Calculated logP: atom-based (AlogP, XlogP, MlogP) is the most general and generally the least accurate. Fragment-based (cLogP) is better but fails for unparameterized groups. Data-mining methods are good only near their training data.
  - Benchmark: Mannhold 2009, more than 96,000 compounds (doi:10.1002/jps.21494, listed).
  - Source: [Wikipedia, Partition coefficient](https://en.wikipedia.org/wiki/Partition_coefficient)

### Inferences
- Anchors used across scales:
  - reference media: water, 1,2-dichloroethane, hexane;
  - reference partners: SbCl5, Et3PO, benzoic acid, 2-methyl-1-pentene, MeBr, H2;
  - reference temperatures: 20 °C (Mayr), 25 °C (Swain–Scott, Hammett).
  
  Moving a number off its anchor requires a model.
- Disagreements between scales for one notion fall into four kinds:
  1. different probes sense different interaction components (ET(30) vs εr; DN vs ECW);
  2. different reference phases (gas vs solution acidity);
  3. different definitions of the notion itself (electronegativity as bond-energy excess, orbital-energy average, or electrostatic force);
  4. different anchors and units.
- Electronegativity scales agree on main-group trends and disagree where definitions need choices: noble gases, transition metals, the f block, and superheavy elements.

### Gaps
- Primary scale papers were not opened: Reichardt (Chem. Rev. 1994), Kamlet–Taft, Catalán (2009), the Mayr database papers, Pearson 1963, Parr–Pearson 1983. Superacid H0 values and carborane rankings are [unverified].
- No source compared Mayr E against Parr ω.

## 3. Observables vs constructs: charges, oxidation states, bond orders, aromaticity, orbitals, density, electronegativity, hardness, resonance

### Takeaway
What is measured: diffraction intensities, giving electron density after phasing and modelling; spectroscopic energies and intensities; dipole moments; NMR shifts; magnetic susceptibilities; bond lengths; and thermochemical energies. Atomic charges, oxidation states, bond orders, aromaticity, orbitals, electronegativity, hardness and resonance structures are constructs. Each requires one of the following:
- a partition (of density into atoms, or of energy into bonds);
- a hypothetical reference state;
- an approximate one-electron description of a many-electron system.

Rival choices give rival numbers. "Images" of orbitals or bonds record densities, local densities of states or force maps, which are then read through these constructs.

### Cited Findings

**3a. Electron density**
- **Definition**: ρ(r) is the electron number density obtained from the N-electron wavefunction. It fixes the wavefunction up to a phase, which is the basis of DFT — [Wikipedia, Electron density](https://en.wikipedia.org/wiki/Electron_density)
- **Observed**: X-ray reflection intensities are proportional to |F|², but phases are not measured (the phase problem). Phases are estimated by direct methods, molecular replacement or anomalous scattering. Models are then refined against the data (R, and R-free from about 10% of reflections held back). Hydrogen is often invisible — [Wikipedia, X-ray crystallography](https://en.wikipedia.org/wiki/X-ray_crystallography). Quantum crystallography yields charge-density distributions; ESR and neutron diffraction give spin density — [Wikipedia, Electron density](https://en.wikipedia.org/wiki/Electron_density)
- Label: OBS (intensities) → REC (a density map that depends on phasing and the model). The Hansen–Coppens multipole formalism is [unverified].
- **QTAIM** (MOD on an observable).
  - Atoms are basins bounded by zero-flux surfaces of ∇ρ. Bonds are bond critical points and bond paths. QTAIM presents these as natural features of the observable density — [Wikipedia, Atoms in molecules](https://en.wikipedia.org/wiki/Atoms_in_molecules)
  - Dispute: H···H bond paths in phenanthrene, chrysene and planar biphenyl were read as stabilizing (Matta 2003, doi:10.1002/chem.200204626, listed). Critics attribute the stability to resonance or π overlap instead (Poater 2007, doi:10.1021/jo061637p, listed). Status: unresolved in the sources seen.

**3b. Atomic partial charges**
- **Observed**: no direct measurement. The nearest observables are molecular dipole moments (H2O 1.86 D in the gas phase and larger in liquid and ice; gaseous KBr about 10.4 D; Br2 zero) — [Wikipedia, Chemical polarity](https://en.wikipedia.org/wiki/Chemical_polarity) — and the electron density.
- **Adds** (MOD): partition schemes.
  - Mulliken: assigns density to atoms through their basis functions — [Wikipedia, Electron density](https://en.wikipedia.org/wiki/Electron_density)
  - QTAIM: integrates the zero-flux basins — [Wikipedia, Atoms in molecules](https://en.wikipedia.org/wiki/Atoms_in_molecules)
  - Natural population analysis: via the chain of natural atomic orbitals → hybrid orbitals → bond orbitals → localized MOs (NAO → NHO → NBO → NLMO), building on Löwdin's 1955 natural orbitals — [Wikipedia, Natural bond orbital](https://en.wikipedia.org/wiki/Natural_bond_orbital)
  - Extended Born–Haber cycles: estimate charges from thermochemistry — [Wikipedia, Born–Haber cycle](https://en.wikipedia.org/wiki/Born%E2%80%93Haber_cycle)
- **Brackets**: formal charge splits each bonding pair equally (the covalent limit). Oxidation state gives the pair to the more electronegative atom (the ionic limit). The real distribution lies between — [Wikipedia, Formal charge](https://en.wikipedia.org/wiki/Formal_charge)
- **Polarity cutoffs** (CONV): Δχ below about 0.5 is nonpolar, 0.5–2.0 polar, above 2.0 ionic; Pauling equated Δχ ≈ 1.7 with about 50% ionic character — [Wikipedia, Chemical polarity](https://en.wikipedia.org/wiki/Chemical_polarity)
- **Why the schemes disagree** [unverified]:
  - There is no quantum-mechanical operator for "the charge on an atom in a molecule".
  - Each scheme defines the atom differently: by basis-function ownership (Mulliken, Löwdin); by a promolecule-weighted "stockholder" share (Hirshfeld); by zero-flux basins (QTAIM); by orbital localization (NPA); or by fitting the electrostatic potential (CHELPG, RESP).
  - CM5 rescales Hirshfeld charges to reproduce dipoles.
  - Mulliken charges depend strongly on basis set. Hirshfeld magnitudes tend to be smallest and QTAIM largest.

**3c. Oxidation states**
- **IUPAC 2016 definition** (CONV).
  - Karen, McArdle & Takats, PAC 88, 831, doi:10.1515/pac-2015-1204; 2014 technical report doi:10.1515/pac-2013-0505.
  - The oxidation state is the charge an atom carries once every bond to a different element is treated as fully ionic.
  - Criteria considered: electronegativity difference, dipole moments, quantum-chemical charges, MO contributions. Pauling or Mulliken electronegativities and dipole moments gave anomalies (CO, NO, and Pt −6 in PtH4²⁻), so Allen electronegativity was adopted.
  - Two algorithms are given: one postulate-based, one Lewis-structure-based.
  - Source: [Wikipedia, Oxidation state](https://en.wikipedia.org/wiki/Oxidation_state)
- **Cases needing experiment**: valence tautomerism in Mn catecholate; the S–S bond order in thiosulfate, settled from distances; P in H3PO3 as +3 (pedagogical) or +5 (by Allen electronegativity) — [Wikipedia, Oxidation state](https://en.wikipedia.org/wiki/Oxidation_state)
- **Extremes**: Ir +9 in IrO4⁺ (Wang 2014, doi:10.1038/nature13795, listed) is an observed gas-phase ion with its state then assigned; the method is [unverified]. Pt +10 in PtO4²⁺ is predicted only (SIM) — [Wikipedia, Oxidation state](https://en.wikipedia.org/wiki/Oxidation_state)
- **Non-innocent ligands**.
  - Jørgensen (1966; doi:10.1016/S0010-8545(00)80170-8, listed) divided ligands into "innocent" and "suspect".
  - A "physical" or spectroscopic oxidation state, read from the d-electron configuration, can differ from the formal one. Examples:
    - neutral [Ni(S2C2Ph2)2] = Ni(II) with two radical-anion ligands, antiferromagnetically coupled;
    - Cr(bipy)3 = Cr(III) with three bipy•⁻;
    - bent NO (NO⁻) vs linear NO (NO⁺);
    - a porphyrin radical in P450 Compound I.
  - Key reference: Chirik & Wieghardt 2010 (doi:10.1126/science.1183281, listed).
  - Source: [Wikipedia, Non-innocent ligand](https://en.wikipedia.org/wiki/Non-innocent_ligand)
  - [unverified]: the specific methods (XAS edges, Mössbauer, EPR, metrical oxidation states from bond lengths) and the Cu(CF3)4⁻ "d8 vs d10" debate (2016–2019).

**3d. Bond orders**
- **Definitions**.
  - Lewis pair count (CONV): N≡N 3; nitrate 4/3.
  - MO (bonding − antibonding)/2 (MOD): fails for stretched bonds.
  - Coulson π bond order from Hückel coefficients: gives benzene 5/3, not 1.5. This is a disagreement between definitions.
  - No single quantum-mechanical definition is agreed.
  - Manz (2017, RSC Adv., doi:10.1039/c7ra07400j, listed) offers a comprehensive method.
  - Pauling 1947 (REC from measured lengths): bond order from bond length with an ad hoc constant (b = 0.353 Å for C–C).
  - Source: [Wikipedia, Bond order](https://en.wikipedia.org/wiki/Bond_order)
- **2025–2026**: cubene and quadricyclene alkenes are reported to have bond orders near 1.5 without resonance, attributed to hyperpyramidalization (Ding et al., Nat. Chem. 2026, doi:10.1038/s41557-025-02055-9, listed; C&EN 2025) — [Wikipedia, Bond order](https://en.wikipedia.org/wiki/Bond_order). Primary paper not checked.
- **Bond types**: no clear line separates bond types; VB and MO are "competing but complementary". Frenking & Krapp 2007, "Unicorns in the world of chemical bonding models" (doi:10.1002/jcc.20543), is listed — [Wikipedia, Chemical bond](https://en.wikipedia.org/wiki/Chemical_bond)
- [unverified]: the Wiberg (1968) and Mayer (1983) density-matrix indices. Gross et al. 2012 (CO-tip non-contact AFM) linked apparent bond length and contrast to Pauling bond order. Hapala et al. 2014 showed that tip relaxation can sharpen features or create apparent bonds.

**3e. Aromaticity indices**
- **IUPAC 2021**: aromaticity is extra stabilization of a cyclically conjugated system relative to a localized reference, supported by bond-length equalization and by a magnetically induced ring current estimated through NICS — [IUPAC Glossary 2021](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html)
- **Magnetic** (OBS).
  - ¹H shifts: benzene 7.3 vs cyclohexene vinyl 5.6 ppm; [18]annulene inner protons −3 ppm; its dianion 20.8 and 29.5 (inner) and −1.1 (outer).
  - Exaltation Λ (REC: measured χ minus an additivity estimate): benzene −13.4, borazine −1.7, cyclohexane 1.1, cyclobutadiene +18.
  - Li⁺ shifts are also used. Λ and Li⁺ shifts depend on ring size.
  - Source: [Wikipedia, Aromatic ring current](https://en.wikipedia.org/wiki/Aromatic_ring_current)
  - [12]annulene: inner 7.86 ppm, outer 5.91 ppm (paratropic) — [Wikipedia, Antiaromaticity](https://en.wikipedia.org/wiki/Antiaromaticity)
- **NICS** (SIM).
  - Computed shielding at the ring centre or above it (NICSzz scans), with the sign reversed.
  - Values: pyrrole −15.1, benzene −9.7, cyclohexane −2.2, cyclobutadiene +27.6. NICS thus ranks pyrrole above benzene; whether other criteria share that order is [unverified].
  - Key references: Schleyer 1996, doi:10.1021/ja960582d; Chen 2005 review, doi:10.1021/cr030088+; Stanger 2020, doi:10.1002/ejoc.201901829 (all listed).
  - Source: [Wikipedia, Aromatic ring current](https://en.wikipedia.org/wiki/Aromatic_ring_current)
- **HOMA** (REC + CONV): a normalized squared deviation of bond lengths from d_opt = 1.388 Å, with constant 257.7 Å⁻²; aromatic = 1, non-aromatic = 0 (Kruszewski 1972, doi:10.1016/S0040-4039(01)94175-9, listed) — [Wikipedia, HOMA](https://en.wikipedia.org/wiki/Harmonic_oscillator_model_of_aromaticity)
- **Energetic** (REC + MOD reference choice): resonance energy and aromatic stabilization energy (ASE) — [Wikipedia, Aromaticity](https://en.wikipedia.org/wiki/Aromaticity)
- **Disputes and status**.
  - Global vs local aromaticity: phenanthrene's central ring is less aromatic.
  - "Y-aromaticity" in guanidinium is controversial.
  - Möbius: a Möbius aromatic hydrocarbon was claimed in 2003 (Ajami, doi:10.1038/nature02224) and reanalysed in 2005 (Castro, doi:10.1021/ja0458165). Wikipedia says none had been proven by 2012 (prior).
  - Krygowski & Szatyłowicz 2015, "Aromaticity: what does it mean?", is listed.
  - Source: [Wikipedia, Aromaticity](https://en.wikipedia.org/wiki/Aromaticity)
  - Cyclobutadiene is rectangular, and its destabilization is attributed mainly to strain and Pauli repulsion, so its antiaromaticity is debated. Baird's rule makes the triplet cyclopentadienyl cation aromatic, and 2007 work (Wörner & Merkt, doi:10.1063/1.2748049, listed) found a triplet ground state — [Wikipedia, Antiaromaticity](https://en.wikipedia.org/wiki/Antiaromaticity)
  - Solà 2017 and the 2023 "Aromaticity: quo vadis" assessment are [unverified].

**3f. Orbitals**
- **Atomic orbitals** (MOD): a one-electron wavefunction, exact only for one-electron systems; for many-electron atoms it is an independent-particle approximation. The familiar pictures are |ψ|² contour surfaces drawn to enclose, for example, 90% probability — [Wikipedia, Atomic orbital](https://en.wikipedia.org/wiki/Atomic_orbital)
- **Molecular orbitals** (MOD).
  - Canonical and localized MOs are related by transformation, and the energies of localized orbitals have no physical meaning.
  - Highly accurate configuration-interaction (CI) wavefunctions have no single set of orbitals.
  - Photoelectron spectroscopy measures ionization energies, which match orbital energies only through Koopmans' approximation (Gold Book k03411) — [Wikipedia, Molecular orbital](https://en.wikipedia.org/wiki/Molecular_orbital)
  - Ionization energy ≈ −E_HOMO; adiabatic and vertical ionization energies differ — [Wikipedia, Ionization energy](https://en.wikipedia.org/wiki/Ionization_energy)
- **Imaging claims**.
  - STEM with EDX mapped 1s and 2p "orbitals" in SrTiO3 (Jeong 2016, PRB 93, 165140, doi:10.1103/PhysRevB.93.165140, listed), with the caveat that the beam–orbital Coulomb interaction (impact-parameter effect) enters the signal — [Wikipedia, Atomic orbital](https://en.wikipedia.org/wiki/Atomic_orbital)
  - In STM, the tunnelling current is proportional to the local density of states (LDOS) at the Fermi level (Tersoff–Hamann). Tip–sample convolution can invert contrast, so images need first-principles modelling — [Wikipedia, Scanning tunneling microscope](https://en.wikipedia.org/wiki/Scanning_tunneling_microscope)
- **Historic claims and critiques** [all unverified]: Zuo et al. 1999 on Cu2O ("d-orbital holes"), publicized as orbitals observed, and Scerri 2000, which argued only densities are observable. Later cases: Itatani 2004 (high-harmonic tomography of N2) and Puschnig 2009 (photoemission orbital tomography). Schwarz 2006 argued that what such methods reconstruct are Dyson orbitals or density differences, under approximations.

**3g. Electronegativity and hardness as constructs**
- Electronegativity is not directly measurable — [Wikipedia, Electronegativity](https://en.wikipedia.org/wiki/Electronegativity); [Karol 2020](https://www.degruyterbrill.com/document/doi/10.1515/ci-2020-0305/html?lang=en). It rises with oxidation state and with s-character (sp³ < sp² < sp) — [Wikipedia, Electronegativity](https://en.wikipedia.org/wiki/Electronegativity). Sanderson's boron values change with oxidation state — [KnowledgeDoor, boron](https://knowledgedoor.com/2/elements_handbook/boron.html)
- The electrophilicity index ω composes electronegativity and hardness — [Wikipedia, Electrophile](https://en.wikipedia.org/wiki/Electrophile)
- Label: MOD anchored to OBS (ionization energy, electron affinity, bond energies, spectra).

**3h. Resonance**
- (MOD.) VB theory combines VB structures, each corresponding to a Lewis structure; this is resonance (Pauling 1928). Fully expanded VB and MO calculations approach mathematical equivalence — [Wikipedia, Valence bond theory](https://en.wikipedia.org/wiki/Valence_bond_theory). IUPAC treats "resonance form" as a synonym of "canonical form" and "contributing structure" — [IUPAC Glossary 2021](https://www.degruyterbrill.com/document/doi/10.1515/pac-2018-1010/html)
- [unverified]: contributing structures are not species in equilibrium. Benzene's resonance energy is a REC relative to a hypothetical cyclohexatriene, from hydrogenation enthalpies. A Soviet critique of resonance theory (around 1949–1951) is historically notable but was ideological.

### Inferences
- Constructs come from partitioning a whole: density into atoms, energy into bonds, the wavefunction into orbitals, stabilization against a hypothetical reference. Partitions are not unique, so rival numbers are expected and are not measurement error.
- Oxidation state is distinctive: it is defined as a convention (IUPAC 2016) but cross-checked by spectroscopy ("physical" oxidation state). Two quantities therefore share one name.

### Gaps
- Comparative charge studies (CM5, Hirshfeld, QTAIM, NPA), the 2018 Nature Materials perspective on oxidation states and ionicity, the AFM bond-order papers, and the orbital-tomography debates were not opened.
- A 2020s method reported to refine per-atom partial charges from 3D electron diffraction is [unverified].

## 4. Cheminformatics and chemical space

### Takeaway
Cheminformatic properties are computed from a chosen representation (a graph or a SMILES string), so they are conventions or model constructs. Class memberships such as drug-like or lead-like are statistical rules fitted to historical compound sets. They are explicitly approximate, and successful drugs often fail them. Similarity holds only relative to a fingerprint and a metric.

### Cited Findings
- **Field and tools** (CONV representation; MOD prediction).
  - Brown defined cheminformatics for drug discovery in 1998. SMILES (Weininger 1988, doi:10.1021/ci00057a005, listed) is a text encoding of the chemical graph.
  - Virtual libraries are built by algorithms such as FOG (Markov chains trained on compound classes).
  - QSAR and QSPR predict activity or properties from structure. Matched-molecular-pair analysis (MMPA) combined with QSAR identifies activity cliffs (Sushko 2014, doi:10.1186/s13321-014-0048-0, listed).
  - Source: [Wikipedia, Cheminformatics](https://en.wikipedia.org/wiki/Cheminformatics)
- **Drug-likeness** (CONV derived by REC from historical sets).
  - Most marketed drugs fall between about 200 and 600 Da.
  - Lipinski's Rule of Five covers H-bond groups, molecular weight and logP (Lipinski 2001, doi:10.1016/S0169-409X(00)00129-0, listed).
  - Ghose (1999): logP −0.4 to 5.6, MW 160–480, molar refractivity 40–130, 20–70 atoms.
  - QED (Bickerton 2012, Nat. Chem., doi:10.1038/nchem.1243): a 0–1 desirability composite with a threshold near 0.5–0.6; it tolerates one poor property.
  - Criticisms: the indices do not measure activity, may narrow the chemical space searched, and many best-selling drugs score poorly; they are irrelevant for biologics.
  - Source: [Wikipedia, Druglikeness](https://en.wikipedia.org/wiki/Druglikeness)
  - Wikipedia also files QSAR and the Rule of Five under "chemical property" — [Wikipedia, Chemical property](https://en.wikipedia.org/wiki/Chemical_property)
- **Computed logP** as a descriptor (atom, fragment and ML methods with different accuracy) — [Wikipedia, Partition coefficient](https://en.wikipedia.org/wiki/Partition_coefficient)
- **Unverified items**:
  - Rule-of-Five thresholds (≤5 H-bond donors, ≤10 acceptors, MW ≤500, logP ≤5), derived from about 2,245 compounds that reached phase II.
  - The Tanimoto coefficient for bit vectors, c/(a + b − c), and the dependence of similarity values on the fingerprint (ECFP/Morgan vs MACCS); fixed cutoffs such as 0.85 are not portable across fingerprints.
  - Chemical-space size of about 10⁶⁰ drug-like molecules; GDB-17 with about 1.66 × 10¹¹ molecules of up to 17 heavy atoms; maps (PCA, t-SNE, TMAP) that depend on descriptor choice.
  - Ertl's natural-product-likeness score, based on fragment frequencies in natural-product vs synthetic sets.
  - The Todeschini–Consonni definition of a molecular descriptor as a number produced by a stated procedure from a symbolic representation.

### Inferences
- Cheminformatic class membership is either a threshold rule (Rule of Five) or a continuous score with a chosen cutoff (QED). These rules rest on statistics of past compounds, not on mechanism.
- Similarity is a property of a pair, a representation and a metric together, not of the pair alone.

### Gaps
- Primary cheminformatics sources were not opened (search budget exhausted).
- Developments in 2023–2026 were not checked: learned representations, property-prediction foundation models, and reassessments of similarity metrics.

## 5. Structure–property principles and where they fail

### Takeaway
Structure–property principles (linear free-energy relationships, the similarity principle, QSAR) are empirical correlations with documented failure modes:
- mechanism changes and steric (ortho) effects;
- dependence on medium or phase;
- microstructure, dopant thresholds and size effects;
- hysteretic first-order transitions;
- activity cliffs.

Collective properties such as superconductivity and magnetic order are observed robustly while parts of their explanation remain open.

### Cited Findings
- **Hammett equation** (REC + CONV reference reaction + MOD separability).
  - Hammett (1937, doi:10.1021/ja01280a022, listed): log(k/k0) = ρσ, anchored on benzoic acid ionization in water at 25 °C (σ_H = 0, ρ = 1). The relation is empirical, not derived from thermodynamics or kinetics alone.
  - Examples: σ_p(NO2) +0.778, σ_p(NMe2) −0.83; ethyl benzoate hydrolysis ρ ≈ +2.498.
  - σ⁺ (cumyl chloride solvolysis) and σ⁻ (phenol ionization) are needed when charge develops in conjugation with the substituent.
  - Failures: ortho substituents (sterics), and curved plots when the mechanism or rate-determining step changes. Refinements: Swain–Lupton, Taft, Yukawa–Tsuno.
  - Compilation: Hansch, Leo & Taft 1991 (doi:10.1021/cr00002a004, listed).
  - Source: [Wikipedia, Hammett equation](https://en.wikipedia.org/wiki/Hammett_equation)
- **Rankings that reverse with medium**: amine basicity order differs between gas phase and water, and HCl is a weak acid in acetic acid — [Wikipedia, Acid dissociation constant](https://en.wikipedia.org/wiki/Acid_dissociation_constant). F⁻ is a strong gas-phase base yet HF is weak in water — [Wikipedia, Proton affinity](https://en.wikipedia.org/wiki/Proton_affinity). The halide nucleophilicity order reverses between protic and aprotic solvents — [Wikipedia, Nucleophile](https://en.wikipedia.org/wiki/Nucleophile)
- **Composition is not enough**: ferromagnetism depends on crystal structure and microstructure — [Wikipedia, Ferromagnetism](https://en.wikipedia.org/wiki/Ferromagnetism). 0.001% As raises Ge's conductivity about 10⁴ times — [Wikipedia, Semiconductor](https://en.wikipedia.org/wiki/Semiconductor)
- **Size**: optical properties of quantum dots depend on size — [Wikipedia, Intensive and extensive properties](https://en.wikipedia.org/wiki/Intensive_and_extensive_properties)
- **History and hysteresis**: the state-function description fails for hysteretic quantities — [Wikipedia, State function](https://en.wikipedia.org/wiki/State_function). A hysteretic first-order transition in Cu2S mimicked superconductivity — [IOP-CAS](https://english.iop.cas.cn/rh/rp/202311/t20231127_645009.html)
- **Activity cliffs**: identified with MMPA plus QSAR — [Wikipedia, Cheminformatics](https://en.wikipedia.org/wiki/Cheminformatics). The standard definition (a small structural change giving a large potency change) and Maggiora's 2006 "why QSAR often disappoints" are [unverified].
- **Electronegativity-based reasoning has stated limits**: Δχ̄ need not predict exothermicity when multielectron terms dominate — [RZH PDF](https://old.roaldhoffmann.com/sites/all/files/644%20jacs.8b10246%20Electronegativity%20seen.pdf)
- **Collective or emergent properties**:
  - Superconductivity is defined by bulk observables. Conventional cases are explained by BCS theory, but the cuprate mechanism is still unclear — [Wikipedia, Superconductivity](https://en.wikipedia.org/wiki/Superconductivity)
  - Altermagnetism's symmetry-based prediction preceded its observation — [IDW](https://nachrichten.idw-online.de/2025/02/25/altermagnetism-recognised-among-top-10-breakthroughs-of-2024)
  - Colligative properties are deliberately blind to structure in the ideal-dilute limit — [Wikipedia, Colligative properties](https://en.wikipedia.org/wiki/Colligative_properties)
  - Anderson 1972, "More is different" (broken symmetry; each level of organization needs new concepts), is [unverified].
- **Drug-likeness scores do not ensure activity**: first-pass metabolism can defeat a drug-like compound — [Wikipedia, Druglikeness](https://en.wikipedia.org/wiki/Druglikeness)

### Inferences
- The failures sort into two types:
  1. the property depends on variables the structural representation does not encode (medium, temperature, phase, microstructure, size, history);
  2. the property responds non-linearly or by threshold to structural change (cliffs, doping, phase transitions, mechanism switches).
- Linear free-energy scales survive failures by adding parameters or reference reactions: σ, σ⁺ and σ⁻; s, N and E; π*, α and β.

### Gaps
- The emergence and activity-cliff literature and the philosophy-of-chemistry sources (the SEP entry; Scerri; Hendry) could not be fetched.
- Much of the evidence here rests on Wikipedia summaries; the primary DOIs listed there should be opened before anything is presented as settled.
