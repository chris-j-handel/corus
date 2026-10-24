# State and flow in chemistry (equilibrium, state functions, rates, steady states, transport): observings kept apart from explainings

## Key gathered points

- **Labels.** [OBS] observing · [REC] reconstruction from observings · [CONV] convention or definition · [MODEL] model construct · [SIM] simulation. The shared web-search budget for this session ran out partway through. Anything I could not check is marked [unverified] and listed under Gaps.
- **State description.** Instruments record path quantities (heat, work, charge) or differences (cell EMF, vapour pressures). State functions are defined only for equilibrium states. Every tabulated "absolute" value rests on a declared zero: ΔfH° and ΔfG° of elements set to 0, the SHE set to 0 V at every temperature, Planck's S(0) = 0, p° = 1 bar, and hypothetical standard states. Single-ion activities cannot be measured at all.
- **Ice.** Calorimetry in 1936 left 0.82 ± 0.05 cal K⁻¹ mol⁻¹ of entropy unaccounted for. Pauling's 1935 proton count gives R ln(3/2) ≈ 0.806. A series expansion (1966) and a simulation (2007) give about 0.815, which is far more precise than any measurement I found.
- **2019 SI.** Fixing N_A, k and h turned the molar mass constant into a measured quantity. This had no practical effect on chemical measurement.
- **Equilibrium.** Guldberg and Waage observed that one limiting composition is reached from both sides, and they posited equal opposing "forces" to explain it. The observing is constant composition. "Dynamic equilibrium" (anticipated by Williamson in 1850) is an interpretation. It has been observed directly only where a marker tracks the identity of molecules: radiolead exchange (Hevesy and Paneth, from 1913), exchange current at zero net current, fluorescence correlation (1972), exchange NMR (1979) and single-molecule FRET (2003).
- **Detailed balance** (Wegscheider 1901; Onsager 1931) is a stronger condition than stationarity. In 2016, net probability flux measured in flagella and cilia gave an operational test that separates a steady state from equilibrium.
- **Kinetics.** Rate laws are empirical, and k, Ea, ΔH‡, ΔS‡ and Km are fitted parameters. The transition state (about 10⁻¹³ s) is a model construct. Femtochemistry (1987), anion photodetachment and the 2023 F + NH₃ resonances all produce spectra that are assigned to it through simulated potential surfaces. Michaelis and Menten assumed rapid equilibrium, and their constant was Vmax/Km (shown by a 2011 reanalysis).
- **Onsager reciprocity** is well verified for transport cross-effects (1960 review). For reactions the evidence is thin: inconclusive in 1965, one confirmation in 2011.
- **Conflations.** "Mass action" names both an equilibrium law and a rate law. "Dynamic equilibrium" is filed as a kind of steady state. Engineering, physiology and a 2016 press release call steady states "equilibria". Le Chatelier's principle has exceptions. Students read constant composition as a stopped reaction or as equal amounts (2023 survey).

## 1. Thermodynamic state description: state and path functions, U, H, S, G, A, chemical potential, activity and fugacity, standard states and reference zeros, and what instruments measure

### Takeaway
Chemists measure heats, works, cell EMFs, vapour pressures, compositions and temperatures under stated constraints. State functions, chemical potentials and activities are constructs defined on equilibrium states. Every number tabulated for them is a difference from a declared zero: formation values of elements, the SHE, Planck's third-law zero, standard states, and since 2019 the fixed SI constants. The residual entropy of ice is the clearest case where the calorimetric record and the statistical model diverged. A counting model reconciled them, not a new measurement.

### Cited Findings

**State and path**
- **State function vs path function [CONV/MODEL].**
  - *Observed:* heat and work exchanged in processes between equilibrium states. These are path quantities, written as inexact differentials.
  - *Explaining adds:* functions (U, H, S, G, A) whose changes depend only on the end states. Gibbs (1873) explicitly allowed such quantities to be called functions of the state; Clausius, Rankine and others used the idea more loosely in the 1850s–60s.
  - *Reaches past:* the description presupposes equilibrium states and fails for systems that show hysteresis.
  - Source: [State function](https://en.wikipedia.org/wiki/State_function) (citing Callen 1985; Mandl 1988; Gibbs 1873).
- **Gibbs and Helmholtz energies [CONV/MODEL].**
  - G = H − TS. At constant T and p, G is at a minimum at chemical equilibrium, and a decrease in G is the criterion for spontaneous change.
  - The maximum non-expansion work is reached only in a completely reversible process, which is a limit and never realised.
  - A plays the same role at constant T and V, and S does at constant U and V.
  - Sources: [Gibbs free energy](https://en.wikipedia.org/wiki/Gibbs_free_energy); [Chemical equilibrium](https://en.wikipedia.org/wiki/Chemical_equilibrium).
- **History of "free energy" [historical].**
  - Gibbs called it "available energy" (1873) and extended it to heterogeneous chemical systems (1876).
  - Helmholtz (1882) tied chemical affinity to maximum reversible work.
  - Lewis and Randall's 1923 textbook spread "free energy" in place of "affinity" in English.
  - Source: [Gibbs free energy](https://en.wikipedia.org/wiki/Gibbs_free_energy).
- **Links from measurement to G [CONV].**
  - ΔG = −nFE for a reversible cell, and ΔG° = −RT ln K.
  - By convention, the standard Gibbs energy of formation of an element in its standard state is zero.
  - Source: [Gibbs free energy](https://en.wikipedia.org/wiki/Gibbs_free_energy).

**Entropy: calorimetric (third-law) vs statistical**
- **Calorimetric entropy [OBS, then REC + CONV].**
  - *Observed:* Cp(T) measured from as close to 0 K as possible, plus the latent heats of transitions. These are integrated as ∫Cp/T dT.
  - *Explaining adds:* an integration constant fixed by convention. Nernst's heat theorem (1906) holds that reaction ΔS goes to zero as T goes to 0. Planck (cited from his 1917 text) set the entropy of a solid at 0 K to zero as a free choice, and only for solids. Nernst (1912) recast the theorem as the unattainability of 0 K, which Masanes and Oppenheim proved in general form in 2017.
  - *Reaches past:* 0 K is never reached, so the zero is extrapolated.
  - Source: [Marquet 2019, arXiv:1904.11696](https://arxiv.org/pdf/1904.11696).
- **Statistical entropy [MODEL].**
  - S = k ln W, with S₀ = 0. Sackur and Tetrode (1912) applied it to monatomic gases, and Gordon (1934) to steam.
  - Agreement between calorimetric and statistical values improved from 1912 to 1998, mostly through Giauque's low-temperature calorimetry.
  - For water, the statistical reference needs a correction for residual entropy.
  - Source: [Marquet 2019](https://arxiv.org/pdf/1904.11696).
- Giauque received the 1949 Nobel Prize for chemical thermodynamics at very low temperatures — [AIP Physics History Network](https://history.aip.org/phn/11511003.html).

**Residual entropy of ice (Pauling 1935)**
- **Measurement [OBS/REC].** Giauque and Stout (J. Am. Chem. Soc. 58, 1144, 1936) found that the calorimetric entropy of ice falls short of the statistical/spectroscopic value by S₀ = 0.82 ± 0.05 cal K⁻¹ mol⁻¹ — [Berg, Muguruma & Okamoto, arXiv cond-mat/0609211](https://arxiv.org/pdf/cond-mat/0609211); [Gingras, "Spin Ice", arXiv:0903.2772](https://arxiv.org/pdf/0903.2772).
- **Pauling's count [MODEL].** Pauling (J. Am. Chem. Soc. 57, 2680, 1935) took the protons to obey the ice rules: two near and two far per oxygen. Counting the allowed arrangements gives W = (3/2)^N and S₀ = R ln(3/2) ≈ 0.806 cal K⁻¹ mol⁻¹. This lies inside the 1936 error bar and is accurate to 1–2% by later estimates — [arXiv cond-mat/0609211](https://arxiv.org/pdf/cond-mat/0609211); [Gingras](https://arxiv.org/pdf/0903.2772).
- **Series refinement [MODEL].** Nagle (J. Math. Phys. 7, 1484, 1966) obtained W₁ = 1.50685(15) and S₀ = 0.81480(20) cal K⁻¹ mol⁻¹ — [arXiv cond-mat/0609211](https://arxiv.org/pdf/cond-mat/0609211).
- **Simulation [SIM].** Multicanonical Monte Carlo on two nearest-neighbour lattice models gave W₁ = 1.50738(16) and S₀ = 0.81550(21), about 0.09% above Nagle. It was published as Phys. Rev. B 75, 092202 (2007), doi:10.1103/PhysRevB.75.092202. The authors challenged experimentalists to improve on the Giauque–Stout precision by about tenfold, so that corrections to Pauling's value could be resolved. **Status: prior (2007); the experimental side is open.** I found no newer measurement, but I did not search for one (see Gaps) — [arXiv cond-mat/0609211](https://arxiv.org/pdf/cond-mat/0609211); [APS abstract](https://link.aps.org/doi/10.1103/PhysRevB.75.092202).
- **Doped ice [OBS].** Tajima, Matsuo and Suga (Nature 299, 810, 1982) found by calorimetry that KOH-doped hexagonal ice has a first-order transition that removes most of the residual entropy. This is read as proton ordering — [Nature](https://www.nature.com/articles/299810a0.pdf).
- **Spin-ice analogue [OBS + MODEL].**
  - Ramirez and co-workers integrated the magnetic Cp/T of Dy₂Ti₂O₇ powder from 0.3 to 10 K. They recovered about 3.9 J mol⁻¹ K⁻¹, against R ln 2 ≈ 5.76 expected for a two-state system.
  - The shortfall (about 1.86) is close to the Pauling-type value (R/2) ln(3/2) ≈ 1.68. Later single-crystal data agreed better.
  - The "two-in/two-out" rule for spins maps onto the ice rule for protons.
  - Source: [Gingras](https://arxiv.org/pdf/0903.2772).

**Chemical potential, activity, fugacity**
- **Chemical potential [MODEL/CONV].**
  - It is the partial molar Gibbs energy at constant T and p. A value is meaningful only relative to a stated reference.
  - At equilibrium, a species has the same μ in every phase, and Σνμ = 0 for a reaction.
  - Particles move from higher to lower μ. Ions move from higher to lower electrochemical potential.
  - Source: [Chemical potential](https://en.wikipedia.org/wiki/Chemical_potential) (citing Baierlein, "The elusive chemical potential", Am. J. Phys. 69, 423, 2001).
- **Activity [CONV + REC].**
  - G. N. Lewis coined the term in 1907. Activity is dimensionless and defined relative to a chosen standard state. Pure solids and liquids are assigned a = 1.
  - Single-ion activity coefficients cannot be measured, because cations cannot be added without anions; only mean ionic values are measurable. Guggenheim (1929) argued that single-ion activities are unmeasurable. IUPAC's activity-based pH is notional and tied to the Harned cell.
  - *Observed for activity:* vapour pressure (water activity equals the equilibrium relative humidity), solvent vapour pressure converted to solute activity through Gibbs–Duhem, EMF, and freezing-point depression.
  - Source: [Thermodynamic activity](https://en.wikipedia.org/wiki/Thermodynamic_activity).
- **Fugacity [CONV].** Fugacity is the effective pressure of a gas: fugacity coefficient × mole fraction × total pressure. Dividing by p° gives the activity — [Thermodynamic activity](https://en.wikipedia.org/wiki/Thermodynamic_activity).

**Standard states and reference zeros**
- **Standard state [CONV, often hypothetical].**
  - p° = 10⁵ Pa (IUPAC 1982 notation, doi:10.1351/pac198254061239).
  - Gas: a hypothetical pure ideal gas at p°. Solute: a hypothetical solution at 1 mol kg⁻¹ (or 1 mol dm⁻³) that behaves as at infinite dilution. Liquid or solid: the pure substance at 1 bar.
  - Temperature is not part of the definition, although tables are usually given at 298.15 K.
  - Many standard states cannot physically exist (for example, steam at 298.15 K and 1 bar). Their values are extrapolated from zero pressure or zero concentration.
  - Source: [Standard state](https://en.wikipedia.org/wiki/Standard_state) (citing IUPAC Gold Book 5th ed. 2025, doi:10.1351/goldbook.S05925; Green Book 3rd ed. 2008, p. 60).
- **ΔfH° = 0 for elements [CONV].** The zero applies to the most stable allotrope (graphite; white tin). White phosphorus is the exception: it is metastable but chosen because black phosphorus is hard to prepare pure — [Standard state](https://en.wikipedia.org/wiki/Standard_state).
- **Standard hydrogen electrode [CONV].** IUPAC defines it as the universal reference electrode for protic solvents, whose standard potential is zero at every temperature (PAC 1986, 58, 955) — [Gold Book S05917](https://goldbook.iupac.org/terms/view/S05917), doi:10.1351/goldbook.S05917.
- **Absolute electrode potential [REC + MODEL].**
  - Trasatti's IUPAC note (Pure Appl. Chem. 58, 955–966, 1986) put the SHE at 4.44 ± 0.02 V at 25 °C on an absolute scale. Here the reference is a universal system with no additional metal–solution interface.
  - The value is best obtained from a mercury electrode at its point of zero charge, and is hard to determine accurately.
  - Source: an archived encyclopedia mirror, so secondary: [Absolute electrode potential (mirror)](https://wikipedia.classicistranieri.com/en/articles/a/b/s/Absolute_electrode_potential.html).
- **2019 SI revision [CONV].**
  - The resolution was approved on 16 November 2018 and took effect on 20 May 2019.
  - The mole is fixed by N_A = 6.022 140 76 × 10²³ mol⁻¹, the kelvin by k = 1.380 649 × 10⁻²³ J K⁻¹, and the kilogram by h.
  - M(¹²C) and M_u lost their exactness and now carry a relative standard uncertainty of 4.5 × 10⁻¹⁰. Relative atomic masses are unchanged.
  - There is no short-term practical effect on analytical chemistry, because weighing and purity uncertainties are much larger — [RSC Analytical Methods Committee Technical Brief 86 (2019)](https://pubs.rsc.org/en/content/articlehtml/2019/ay/c9ay90028d).
  - Molar masses gain an uncertainty below 1 part in 10⁹, and the number fixed in N_A is now formally called the Avogadro number — [Mills & Marquardt, Chemistry International 2019](https://www.degruyterbrill.com/document/doi/10.1515/ci-2019-0108/html?lang=de).
  - There is no immediate effect on temperature-measurement practice — [A*STAR implementation guidance](https://www.a-star.edu.sg/docs/librariesprovider20/2019-news-articles/si-redef.pdf).
  - **Status: settled and in force.**

**What the instruments actually measure**
- **Cell EMF [OBS].** This is a potential difference between the two electrodes of a cell. A single-electrode "potential" is a value on the scale whose zero is the SHE convention. It is converted to ΔG through −nFE — [Gold Book S05917](https://goldbook.iupac.org/terms/view/S05917); [Gibbs free energy](https://en.wikipedia.org/wiki/Gibbs_free_energy).
- **Equilibrium constants [OBS, then REC].**
  - Glass-electrode potentiometry gives either an activity quotient or a concentration quotient, depending on how the electrode was calibrated.
  - Silver ion-selective electrodes have given log K to about ±0.001 for van 't Hoff analysis. IR and ¹³C NMR give micro-constants, and competition against a second ligand extends the measurable range.
  - Van 't Hoff fits of log K against T give ΔH° and ΔS° with errors much larger than those of the K values themselves.
  - Source: [Equilibrium constant](https://en.wikipedia.org/wiki/Equilibrium_constant).
- **Vapour pressure [OBS].** It gives the activity of a volatile component directly. The activity of a non-volatile solute comes from the solvent's vapour pressure through Gibbs–Duhem, which is a model step — [Thermodynamic activity](https://en.wikipedia.org/wiki/Thermodynamic_activity).
- **Kinetic parameter defined at equilibrium [CONV].** IUPAC defines an activation quantity for an electrode reaction from the temperature dependence of ln I₀ at equilibrium. A rate parameter is thus taken at a state of zero net reaction — [Gold Book E02109](https://goldbook.iupac.org/terms/view/E02109/plain).

### Inferences
- The reference zeros fall into three kinds:
  - physically realisable (a pure element in its reference form at 1 bar);
  - hypothetical but reachable by extrapolation (an ideal gas at 1 bar, an ideal-dilute 1 mol kg⁻¹ solute, Planck's S(0));
  - specified with a component that cannot be measured even in principle. The SHE requires unit activity of H⁺, which is a single-ion activity.
- Calorimetric "absolute" entropy is a record of the heat absorbed from the lowest temperature reached, plus a conventional zero. Ice shows that this record misses disorder frozen in for kinetic reasons. The agreement was restored by a counting model, refined later by series expansion and simulation. Experiment seems to remain at its 1936 precision (about ±6%), while theory is at about 0.03%. Here the explaining is roughly two orders of magnitude more precise than the observing.
- The 2019 redefinition moved a convention. The zero for amount of substance shifted from a mass of ¹²C to a counted number, and an exact constant (M_u) became a measured one. No new chemical observation was involved.
- Single-electrode potentials, chemical potentials and activities are all "relative-to" quantities. In each case the instrument measures a difference between two sides: two electrodes, two phases, or solvent against solution.

### Gaps
- Extensive/intensive classification (Green Book): no source fetched. It is definitional [unverified].
- The status of the triple point of water after 2019 (now measured rather than defined) and the role of ITS-90 [unverified].
- The ionic thermochemistry convention ΔfH°(H⁺, aq) = 0 [unverified].
- Haida et al. (J. Chem. Thermodyn. 6, 815, 1974), cited in the 2007 paper, was not read. I did not check for any 2023–2026 remeasurement of ice's residual entropy, because the search budget was exhausted.
- I did not access the IUPAC Green Book itself, Atkins, or Kondepudi & Prigogine.

## 2. Equilibrium: mass action, equilibrium constants, "dynamic equilibrium", detailed balance, Wegscheider, Le Chatelier, and the experiments that observe exchange at constant composition

### Takeaway
The founding observing of chemical equilibrium is a limiting composition that is reached from either side and then stays constant. "Dynamic equilibrium" (equal and opposite molecular traffic) is an interpretation that was proposed before it could be observed (Williamson, 1850). Since then it has been observed directly in particular systems, wherever a marker tracks molecular identity at constant composition: radiotracers, partial electrode currents, NMR magnetization, fluorescence fluctuations and single-molecule FRET. Detailed balance is a stronger claim that is tested separately: every elementary step is balanced by its own reverse. Its breakdown has been observed as net probability flux in active biological matter.

### Cited Findings

**Law of mass action and equilibrium constants**
- **Guldberg and Waage, 1864 [OBS + MODEL].**
  - *Observed:* the amount x converted at the limiting state, and how it depends on time, temperature, water content and starting masses. The same limit was approached from both directions.
    - Series II: BaSO₄ with K₂CO₃ and the reverse, mostly at 100 °C in platinum or silver vessels, because potash attacks glass.
    - Series I: Berthelot and Saint-Gilles's 1862 esterification data.
    - Series III: Scherer's silica–soda data.
  - *Explaining adds:* two opposing "forces", one forming products and one restoring reactants. Each is proportional to a product of masses raised to exponents, and equilibrium is where the forces are equal. They also stated a companion volume law, and found that only four of six coefficients are independent.
  - *Reaches past:* they stated that equilibrium is reached only after infinite time, so they worked from limiting values.
  - Source: [Abrash translation](https://web.chemteam.info/Chem-History/Concerning-Affinity.html).
- **Publication history.**
  - Waage presented the work to the Norwegian Academy on 14 March 1864 (printed 1865). A French version followed in 1867. The law became widely known after Ostwald adopted it in 1877. The DSB dates van 't Hoff's kinetic derivation to 1878 — [Kauffman, DSB](https://mathshistory.st-andrews.ac.uk/DSB/guldberg.pdf).
  - Aronson gives 1864, 1867 and 1879 as the publication years and dates van 't Hoff's independent work to 1877, so the sources conflict on 1877 vs 1878. "Active mass" meant effective concentration — [Aronson, BMJ blog, 2019](https://blogs.bmj.com/bmj/2019/08/23/jeffrey-aronson-when-i-use-a-word-the-law-of-mass-action).
- **1879 kinetic justification.**
  - Guldberg and Waage justified the rate form by collision frequency, identified the exponents with stoichiometric coefficients, and derived K by setting forward and reverse rates equal.
  - That derivation is no longer considered general: the rate law holds strictly only for elementary reactions. The equilibrium expression still stands.
  - The name is used for both laws inconsistently.
  - Source: [Law of mass action](https://en.wikipedia.org/wiki/Law_of_mass_action).
- **Thermodynamic K vs concentration quotient [CONV].**
  - K is the quotient of activities at equilibrium and is dimensionless. Kc = K/Γ (Γ = quotient of activity coefficients) varies with ionic strength, T and p.
  - A Kc extrapolated to zero ionic strength is, as the source puts it, paradoxically called a thermodynamic constant.
  - Fixing Γ = 1 in a constant ionic medium amounts to redefining the standard state, so numerical K values depend on conventions.
  - Sources: [Chemical equilibrium](https://en.wikipedia.org/wiki/Chemical_equilibrium); [Equilibrium constant](https://en.wikipedia.org/wiki/Equilibrium_constant).
- **Gibbs criterion [MODEL].** At constant T and p, equilibrium is the minimum of G with respect to extent of reaction. The minimum lies between pure reactants and pure products because of the entropy of mixing. ΔG° = −RT ln K — [Chemical equilibrium](https://en.wikipedia.org/wiki/Chemical_equilibrium).

**"Dynamic equilibrium": the interpretation and its history**
- **Berthollet, 1803 [OBS + MODEL].** Natron (sodium carbonate) deposits at Lake Natron led him to read the end state of a reaction as a balance of opposing processes — [Chemical equilibrium](https://en.wikipedia.org/wiki/Chemical_equilibrium).
- **Williamson, 1850 [MODEL].** In his theory of etherification (Phil. Mag. 37, 350–356; doi:10.1080/14786445008646627) he proposed a continual exchange of atoms among molecules. In HCl, for example, hydrogen atoms change partners. Clausius proposed similar ideas at about the same time. The source does not use the phrase "dynamic equilibrium" — [Alexander William Williamson](https://en.wikipedia.org/wiki/Alexander_William_Williamson).
- **Modern textbook form [MODEL].** Equilibrium means equal, non-zero forward and reverse rates with no net change, and equilibria are statistical averages. The source adds that equal rates are necessary but do not explain why equilibrium is reached — [Chemical equilibrium](https://en.wikipedia.org/wiki/Chemical_equilibrium).
- The encyclopedia entry "Dynamic equilibrium" treats it as a particular case of steady state. It cites no isotopic or other experimental evidence of continuing exchange and argues only from the CO₂ gas–liquid example — [Dynamic equilibrium](https://en.wikipedia.org/wiki/Dynamic_equilibrium).

**Detailed balance, microscopic reversibility, Wegscheider**
- **History [MODEL].**
  - Maxwell (1867) and Boltzmann (1872, the H-theorem) applied it to molecular collisions.
  - Wegscheider (1901; Monatsh. Chem. 32, 849; doi:10.1007/BF01517498) brought it into chemical kinetics and showed that it rules out irreversible cycles.
  - Onsager (1931) built his reciprocal relations on Wegscheider's relations.
  - Source: [Detailed balance](https://en.wikipedia.org/wiki/Detailed_balance).
- **Content.**
  - Detailed balance is stronger than mere stationarity.
  - It rests on three assumptions, any of which can fail: microscopic dynamics invariant under time reversal, an equilibrium invariant under time reversal, and distinguishable elementary processes. Boltzmann's collision case needs PT rather than T alone.
  - For a cycle of first-order steps, the product of rate constants taken one way round equals the product taken the other way (Wegscheider). In Markov terms this is Kolmogorov's criterion.
  - Source: [Detailed balance](https://en.wikipedia.org/wiki/Detailed_balance).
- Gorban and Yablonsky (Chem. Eng. Sci. 66, 5388, 2011; doi:10.1016/j.ces.2011.07.054) treated irreversible steps as limits of reversible ones. This gives an "extended" detailed balance: irreversible reactions may not lie on oriented cycles, and Wegscheider identities must hold for the reversible part — [arXiv:1101.5280](https://www.arxiv.org/pdf/1101.5280).
- Complex balancing (Horn, Jackson and Feinberg, 1970s) generalises the detailed-balanced equilibrium and rules out multistability and oscillation — [van der Schaft, Rao & Jayawardhana, arXiv:1503.01996](https://ar5iv.arxiv.org/html/1503.01996).
- **2025 work [MODEL].**
  - Franco and Velázquez argue that biochemical models often lack detailed balance because some concentrations are held fixed by exchange with reservoirs. Any bidirectional network can be extended, by adding species, into a closed network with detailed balance. The departure from detailed balance then measures distance from equilibrium. Closed detailed-balanced systems have a free-energy Lyapunov function, and open ones add a term for external flux — [arXiv:2502.04754](https://arxiv.org/abs/2502.04754).
  - A 2025 Springer article, apparently the published form of this work [inferred], states that adaptation cannot occur robustly in closed chemical systems and cites a companion paper for this — [doi:10.1007/s11538-025-01487-1](https://link.springer.com/10.1007/s11538-025-01487-1).
  - **Status: open, active.**

**Le Chatelier**
- **[MODEL; heuristic].** The 1884 statement: a disturbed equilibrium shifts so as to partly undo the change. Adding product leaves K unchanged. Catalysts speed up both directions equally — [Chemical equilibrium](https://en.wikipedia.org/wiki/Chemical_equilibrium).
- **Exceptions [REC; calculation from the equilibrium model].**
  - For ideal-gas ammonia synthesis at fixed T and P, adding an infinitesimal amount of N₂ shifts the mixture toward NH₃ decomposition whenever the initial N₂ mole fraction is above 0.5. At exactly 0.5 there is no shift. Finite additions can change the direction of the shift.
  - The authors call the principle not universally valid. A "principle of moderation" holds for infinitesimal changes at constant T and P, moderating the chemical potential of the added species, but it can fail for finite changes.
  - Source: [Corti & Franses, Chem. Eng. Educ. 2003](https://journals.flvc.org/cee/article/download/122716/121755).
  - **Status: settled as an exception (2003, and earlier literature).**

**Experiments observing molecular activity at constant composition**
1. **Radiotracer solubility and exchange: Hevesy and Paneth, from January 1913 [OBS].**
   - Instrument: a gold-leaf electroscope. Label: radium D (radio-lead) in lead nitrate, converted to PbS or PbCrO₄. Quantity: activity in the filtrate, giving the solubility — [IAEA Bulletin vol. 7(1) article on Hevesy](https://www.iaea.org/sites/default/files/publications/magazines/bulletin/bull7-1/07106481522.pdf).
   - Solid PbSO₄ shaken with its saturated solution containing labelled lead: the label spreads until the labelled fraction is the same on the crystal surface as in solution. The amounts do not change, so this is continuing exchange. Paneth used it to measure crystal surface areas, because only the top molecular layer took part. On metallic lead foil, hundreds of atomic layers exchanged, which Hevesy attributed to local electrode processes. On PbO₂, only the outermost layer exchanged — [Hevesy Nobel lecture](https://nobelprize.org/uploads/2018/06/hevesy-lecture.pdf); [IAEA Bulletin](https://www.iaea.org/sites/default/files/publications/magazines/bulletin/bull7-1/07106481522.pdf).
   - PbCl₂ and labelled Pb(NO₃)₂ dissolved together and recrystallised: the label ended up evenly distributed (c. 1920), which was read as support for ionic dissociation. Further cases: Pb²⁺/Pb⁴⁺ exchange in glacial acetic acid, and exchange between molten lead and its molten salts (1921) — [Hevesy Nobel lecture](https://nobelprize.org/uploads/2018/06/hevesy-lecture.pdf).
   - *Explaining adds:* that labelled and unlabelled atoms behave identically, and that the spreading of the label is two-way traffic.
   - *Reaches past:* the label shows that identities moved. It does not show the path, which could be dissolution and redeposition, surface diffusion, or local currents.
2. **Self-diffusion in a pure solid: Hevesy, c. 1920–29 [OBS + REC].**
   - Radio-lead soldered to ordinary lead and held at 280 °C for 140 days showed no detectable diffusion.
   - A recoil-ionisation method (with Seith) made coefficients down to about 10⁻¹² cm² day⁻¹ measurable. Extrapolating, lead atoms change places about once a day at room temperature.
   - Pb²⁺ self-diffusion in PbCl₂ and PbI₂ was compared with ionic conduction (1929).
   - Source: [Hevesy Nobel lecture](https://nobelprize.org/uploads/2018/06/hevesy-lecture.pdf).
   - Here composition is constant and motion is measured. This is the observing that lies under a single-component Fick coefficient.
3. **Exchange current [CONV + REC].**
   - IUPAC defines I₀ as the common magnitude of the anodic and cathodic partial currents when the electrode reaction is at equilibrium. With one reaction, the net current is zero. With several reactions, the net current is generally non-zero when only one of them is at equilibrium.
   - Source: [Gold Book E02238](https://goldbook.iupac.org/terms/view/E02238/plain) (PAC 1974, 37, 499; doi:10.1351/goldbook.E02238).
   - *Explaining adds:* the split of a zero net current into two equal and opposite partial currents. How I₀ is obtained in practice is not covered by these sources (see Gaps).
4. **Two-dimensional exchange NMR (EXSY) [OBS + MODEL].** Jeener, Meier, Bachmann and Ernst, "Investigation of exchange processes by two-dimensional NMR spectroscopy", J. Chem. Phys. 71, 4546–4553 (1979), doi:10.1063/1.438208. It built on Jeener's 1971 proposal of two-pulse 2D NMR — [Jean Jeener](https://en.wikipedia.org/wiki/Jean_Jeener). The pulse-sequence details were not verified from the primary paper (see Gaps).
5. **Fluorescence correlation spectroscopy: Magde, Elson and Webb, 1972 [OBS + MODEL].**
   - System: DNA with ethidium bromide, which forms a strongly fluorescent complex, held at chemical equilibrium. Observed: fluctuations in fluorescence intensity. Extracted: chemical rate constants, diffusion coefficients and the coupling between them.
   - It was reported at the time as the first measurement of fluctuations relaxing through a reaction mechanism — [Physics Today news, Dec 1972, doi:10.1063/1.3071135](https://physicstoday.aip.org/news/fluctuations-at-chemical-equilibrium).
   - Paper: vol. 29, pp. 705–708, September 1972 — [Wikidata mirror](https://wikidp.org/Q21563722). The journal name was not displayed; Phys. Rev. Lett. is [unverified].
   - Review: Webb, Q. Rev. Biophys. 9, 49–68 (1976), doi:10.1017/S0033583500002158 — [Cambridge](https://www.cambridge.org/core/journals/quarterly-reviews-of-biophysics/article/applications-of-fluorescence-correlation-spectroscopy/3EC403FF3A143CCDF92987F7E3051CA8).
6. **Single-molecule FRET: McKinney, Déclais, Lilley and Ha, 2003 [OBS + MODEL].**
   - Individual four-way (Holliday) DNA junctions switch repeatedly between two stacked conformers. Na⁺ and Mg²⁺ change the transition rates differently.
   - Conformer exchange and branch migration share an unstacked open intermediate but have different rate-limiting steps. The relative rates let a junction reach conformational equilibrium.
   - Published in Nat. Struct. Biol. 10, 93–97 (now Nat. Struct. Mol. Biol.), doi:10.1038/nsb883 — [Nature](https://www.nature.com/articles/nsb883).
   - *Explaining adds:* a kinetic state model. The constant fractions in the ensemble are read as time-averages of single-molecule switching.
7. **Contrast case, stationary but not at equilibrium: Battle et al., 2016 [OBS + MODEL].**
   - Microscopy of the shapes of an isolated *Chlamydomonas* flagellum and of primary cilia of epithelial cells. Quantity: probability flux in a coarse-grained shape space.
   - A non-zero circulating flux shows broken detailed balance, even where the motion looks random. The authors present the method as a general tool.
   - Published in Science 352, 604–607, doi:10.1126/science.aac8167 — [Duke Scholars](https://scholars.duke.edu/publication/1427814); [Göttingen Research Online](https://publications.goettingen-research-online.de/ID-47).

### Inferences
- Two different observings sit under "equilibrium":
  - (a) macroscopic constancy and approach from both sides (Guldberg and Waage);
  - (b) identity-tracking exchange at that constancy (tracers, I₀, EXSY, FCS, smFRET).
  
  For the systems actually studied, (b) moves the "dynamic" reading from model construct to reconstruction from observings. For slow or inert systems it is still an extrapolation.
- Every observation of exchange needs a marker that is assumed not to disturb the balance: an isotope, a spin state, a dye. That assumption is itself model content.
- Constant composition does not establish detailed balance. Testing it needs either a check for zero net cycle flux (as in Battle et al.) or Wegscheider-type relations among measured rate constants. I found no direct experimental test of a Wegscheider cycle condition in a chemical system (see Gaps).
- Le Chatelier's rule is a qualitative shorthand for stability conditions. Its exceptions arise where reading "the change" as a change in mole fraction and reading it as a change in chemical potential give different answers.

### Gaps
- H/D exchange in proteins (Linderstrøm-Lang, 1950s; EX1/EX2 regimes; protection factors read as opening fluctuations of the native state): [unverified], because the page was unreachable once the search budget ran out.
- Isotope exchange at equilibrium as a test of enzyme mechanism (Boyer, c. 1959): [unverified].
- Exchange measured by NMR line shape and saturation transfer (e.g., dimethylformamide rotation; Forsén–Hoffman, 1963): [unverified].
- The EXSY mixing-time and cross-peak mechanism, and its being run at chemical equilibrium, was not checked against the primary paper: [unverified].
- How I₀ is obtained in practice (Butler–Volmer or Tafel extrapolation, micropolarisation, impedance, radiotracer methods): [unverified].
- The numerical switching rates for the Holliday junction were not accessible (they are in the figures).
- No 2023–2026 developments in equilibrium-exchange experiments could be searched.

## 3. Kinetics as explaining: rate laws, rate constants, activation (Arrhenius vs Eyring), the transition state, steady states, Michaelis–Menten, flux, Onsager reciprocity, transport laws

### Takeaway
Kinetics measures concentrations, or signals, against time under fixed conditions. Rate laws, rate constants, activation energies and transition-state parameters are fitted or modelled additions. The transition state remains a model construct. Its "direct observation" by femtochemistry, anion photodetachment and the 2023 F + NH₃ resonances consists of spectra assigned to it through simulated potential surfaces. Onsager reciprocity is well verified for transport cross-effects but only thinly for chemical reactions.

### Cited Findings

**Rate laws and rate constants**
- **Rate law [REC].** IUPAC treats the rate equation as an empirical differential expression. Orders come from experiment, by initial-rate and integrated-law methods, and cannot be reliably read off the stoichiometry. Only for elementary reactions does the order equal the molecularity — [Rate equation](https://en.wikipedia.org/wiki/Rate_equation).
- **Rate constant [REC/CONV].** k depends on temperature, ionic strength and other conditions. For a reversible elementary step, K = k₁/k₋₁. Relaxation toward equilibrium has rate constant k₁ + k₋₁ (citing J. Chem. Educ. 84, 1499, 2007) — [Rate equation](https://en.wikipedia.org/wiki/Rate_equation).
- **Steady-state approximation [MODEL].** Applied to the acetaldehyde pyrolysis chain, with radical concentrations taken as constant, it gives an observed order of 3/2 — [Rate equation](https://en.wikipedia.org/wiki/Rate_equation).

**Activation: Arrhenius vs Eyring**
- **Arrhenius, 1889 [REC].**
  - It built on van 't Hoff's 1884 temperature dependence of K (Z. Phys. Chem., doi:10.1515/zpch-1889-0408) and is best regarded as empirical (Connors 1990). IUPAC gives an operational definition of Ea (Gold Book doi:10.1351/goldbook.A00446).
  - A modified form adds a temperature-dependent pre-factor, but Connors notes that temperature studies alone cannot establish that dependence. Glass formers deviate strongly (Phys. Rev. Lett. 111, 225702, 2013).
  - Source: [Arrhenius equation](https://en.wikipedia.org/wiki/Arrhenius_equation).
- **Curved Arrhenius plots.** Michel (Physica A 510, 188–199, 2018) used cis/trans-2-butene isomerisation data from 296–875 K. He attributes the curvature to temperature-dependent reactant energies and rejects one probabilistic model because it predicts almost no cis-2-butene below about 300 K, contrary to measurement — [arXiv:2402.00900](https://arxiv.org/pdf/2402.00900).
- **Transition-state theory, 1935 [MODEL].**
  - *Lineage:* Marcelin's standard Gibbs energy of activation (1910); Herzfeld's k_BT/h factor (1919); Tolman's "critical increment" (1920); the Eyring–Polanyi H + H₂ surface (1931); the Pelzer–Wigner saddle analysis; then Eyring (doi:10.1063/1.1749604) and Evans and Polanyi (doi:10.1039/tf9353100875).
  - *Assumptions:* activated complexes are in quasi-equilibrium with reactants. They are not Boltzmann-distributed, yet an equilibrium constant is still defined for them. Motion along the reaction coordinate is classical. Every crossing of the dividing surface counts as reaction, so conventional TST gives an upper bound; variational TST corrects this by moving the surface.
  - *Where it fails:* very short-lived intermediates, tunnelling, and high temperatures.
  - *Relation to Arrhenius:* Ea = ΔH‡ + RT for condensed-phase or unimolecular steps, and the pre-factor A tracks ΔS‡.
  - Source: [Transition state theory](https://en.wikipedia.org/wiki/Transition_state_theory) (citing Laidler & King 1983, doi:10.1021/j100238a002; Truhlar, Garrett & Klippenstein 1996, doi:10.1021/jp953748q).
- **Status of the transition state [MODEL].** Its proposed lifetime is about 10⁻¹³ s, roughly one vibration. For enzymatic reactions, no physical or spectroscopic method observes the transition-state structure directly — [Transition state theory](https://en.wikipedia.org/wiki/Transition_state_theory).

**Attempts to observe transition states**
- **Femtochemistry [OBS + MODEL].**
  - Dantus, Rosker and Zewail, "Real-time femtosecond probing of transition states in chemical reactions", J. Chem. Phys. 87, 2395–2397 (1987). A pump pulse starts ICN photodissociation, and delayed probe pulses take snapshots — [MSU publication record](https://www2.chemistry.msu.edu/faculty/dantus/publications/46.pdf).
  - The 1999 Nobel Prize (announced 12 October 1999) cited these results. ICN's bond breaks in about 200 fs. In NaI, the bond oscillates between ionic and covalent character, and near 6.9 Å the molecule either returns or dissociates. The pulses lasted tens of femtoseconds. The Academy described this as watching the barrier crossing in slow motion — [Nobel press release](https://www.nobelprize.org/prizes/chemistry/1999/press-release/).
- **Anion photodetachment transition-state spectroscopy [OBS + SIM].**
  - Method: a stable anion with a geometry close to the neutral transition state is photodetached, and its photoelectron spectrum recorded. Examples: FH₂⁻ for F + H₂, H₃O⁻ for OH + H₂, OHF⁻, IHI⁻, BrHI⁻ and ClH₂⁻.
  - Resolution: about 50–100 cm⁻¹ conventionally, and below 1 meV with slow-electron velocity-map imaging.
  - Observed: vibrational progressions in modes perpendicular to the reaction coordinate. A bend progression, for example, indicates a bent F–H–H transition state. Resonances are rarely resolved.
  - Assignment needs wave-packet simulations on potential surfaces. For H₃O⁻, surfaces with the saddle point about 0.14 Å farther out fitted better.
  - Limits: Franck–Condon access, "half-collision" geometry, averaging over angular momentum, and the accuracy of the surface.
  - Sources: [Neumark 2005, Phys. Chem. Chem. Phys. (journal inferred from URL)](https://pubs.rsc.org/en/content/articlehtml/2005/cp/b417886f); earlier perspective, Neumark, PhysChemComm 5, 76–81 (2002), doi:10.1039/B202218D — [RSC](https://pubs.rsc.org/en/content/articlepdf/2002/qu/b202218d).
- **2023 result [OBS + SIM].**
  - Babin et al., Nature Chem. 15, 194–199 (2023), doi:10.1038/s41557-022-01100-1, recorded cryogenic slow-electron velocity-map imaging spectra of FNH₃⁻.
  - The spectra show vibrational Feshbach resonances in the HF + NH₂ product well. At higher energies there are resonances that span the transition state into the reactant complex.
  - The assignment rests on reduced-dimensionality quantum dynamics on a global surface. The authors offer the influence of these resonances on bimolecular dynamics only as a possibility.
  - Source: [Springer link](https://link.springer.com/article/10.1038/s41557-022-01100-1).
  - **Status: active line; this is the 2023 state.**

**Steady state and Michaelis–Menten**
- **Michaelis and Menten (1913), re-read [OBS + REC + MODEL].**
  - *Observed:* the optical rotation of sucrose solutions with invertase, followed by polarimetry until the reaction was complete. Sucrose ran from about 20.8 to 333 mM. The enzyme was dosed only in relative amounts; its molar concentration was unknown and its source and preparation unreported.
  - *Their model:* substrate binding in rapid equilibrium, with rate proportional to [ES]. They used initial velocities to avoid product inhibition.
  - *Later readings:* Van Slyke and Cullen (1914) treated the steps as irreversible. Briggs and Haldane (1925) introduced the steady state.
  - *The 1913 constant:* it was Vmax/Km (written C/K_S), at 0.0454 ± 0.0032 min⁻¹. With K_S = 16.7 mM this implies Vmax ≈ 0.76 ± 0.05 mM min⁻¹. A modern global fit gives 0.80 ± 0.02.
  - **Status: reproduced by reanalysis (2011).**
  - Source: [Johnson & Goody, Biochemistry 50, 8264–8269 (2011), doi:10.1021/bi201284u](https://pmc.ncbi.nlm.nih.gov/articles/PMC3381512).

**Flux, Onsager reciprocity, transport laws**
- **Onsager, 1931 [MODEL].**
  - Near equilibrium, fluxes are linear in thermodynamic forces, with symmetric coefficients (L_ij = L_ji), derived from microscopic reversibility. The simple form fails with magnetic fields or Coriolis forces.
  - Fourier's, Fick's and Ohm's laws are the direct terms. The Seebeck, Peltier, Soret and Dufour effects are cross terms.
  - Onsager received the 1968 Nobel Prize.
  - Sources: [Onsager reciprocal relations](https://en.wikipedia.org/wiki/Onsager_reciprocal_relations); Phys. Rev. 37, 405, doi:10.1103/PhysRev.37.405.
- **Experimental tests [OBS, then REC].**
  - Miller's review (Chem. Rev. 60, 15–37, 1960, doi:10.1021/cr60203a003) found support in thermoelectricity, electrokinetics, transference in electrolytes, diffusion, anisotropic heat and electrical conduction, thermomagnetism and galvanomagnetism. For chemical reactions, the evidence was meagre and inconclusive — [Onsager reciprocal relations](https://en.wikipedia.org/wiki/Onsager_reciprocal_relations). Miller also wrote a 1974 chapter on experimental evidence — [Rard & Albright 2007](https://link.springer.com/article/10.1007/s10953-007-9187-5).
  - Nebeker (Caltech PhD, 1965) studied coupled gas-phase reactions of NO, I₂, Cl₂, ICl and NOCl. Rates and affinities measured photometrically showed non-zero coupling coefficients L₁₂ and L₂₁, but a conclusive test of reciprocity could not be made. Linear rate laws worked better nearer equilibrium — [Caltech thesis](https://thesis.caltech.edu/135/).
  - Yablonsky, Gorban, Constales, Galvita and Marin (EPL 93, 20004, 2011; doi:10.1209/0295-5075/93/20004) recast reciprocity for linear(ised) kinetics with detailed balance. Run one experiment starting from pure q and observe species r; run the dual experiment starting from pure r and observe q. After each curve is divided by its equilibrium value, the two time courses coincide, so no rate constants need to be fitted. They tested this by TAP pulse-response on part of the water–gas shift reaction over iron oxide at 780 K, and the ratio stayed constant across frequency within error. This is a single system — [arXiv:1008.1056](https://arxiv.org/pdf/1008.1056).
  - De Corato and Pagonabarraga (J. Chem. Phys. 157, 084901, 2022; doi:10.1063/5.0098425) studied a catalytic self-propelled colloid by perturbation theory and simulation. They find reciprocity near equilibrium (a force on the particle would induce a reaction rate) and a breakdown around a nonequilibrium steady state. No experiment was involved — [UB repository](https://diposit.ub.edu/items/df49337d-4e80-4dfb-bfcc-100b751e5a8b/full).
  - The validity of reciprocity for anisotropic heat conduction was re-examined by Arya and Verros, Axioms 11, 104 (2022), doi:10.3390/axioms11030104. Only the title and references were accessible — [MDPI mirror](https://0-www-mdpi-com.brum.beds.ac.uk/2075-1680/11/3/104).
  - **Status for chemical reactions: open. Prior states: meagre (1960), inconclusive (1965), one kinetic-curve confirmation (2011).** No 2023–2026 test was found, but this was not searched.
- **Transport laws [REC, then MODEL].**
  - Fourier's law is a linear approximation that holds for small gradients, with a conductivity that depends only on state variables — [Onsager reciprocal relations](https://en.wikipedia.org/wiki/Onsager_reciprocal_relations).
  - In chemical-potential form, particles move down μ gradients and ions move down electrochemical-potential gradients — [Chemical potential](https://en.wikipedia.org/wiki/Chemical_potential).
  - Tracer self-diffusion at constant composition (Hevesy, §2) is the observing under a single-component diffusion coefficient — [Hevesy Nobel lecture](https://nobelprize.org/uploads/2018/06/hevesy-lecture.pdf).

### Inferences
- Rate constants and activation parameters are fitted values tied to stated conditions. Their reading as molecular properties (barrier height, entropy of activation) comes from TST. TST itself rests on an equilibrium assumption (quasi-equilibrium with activated complexes) and on a cut (the dividing surface).
- Every cited transition-state "observation" concerns a few-atom gas-phase system or a photo-initiated half-reaction, and every one is assigned by comparison with simulations on computed surfaces. Saying that every reaction passes through a transition state is a model-level generalisation.
- The 1913 data fit a rapid-equilibrium derivation, and later texts derive the same hyperbolic form from a steady state. The functional form alone cannot tell the two assumptions apart; only the meaning of the constant differs. This is an inference from the 2011 reanalysis.
- For transport cross-effects, Onsager reciprocity is a reconstruction from observings. For coupled chemical reactions it remains mostly a model claim. The 2011 reformulation in terms of kinetic curves avoids the ill-posed step of fitting coefficients.

### Gaps
- Polanyi's transition-state emission spectroscopy (early 1980s): [unverified].
- The Curie (symmetry) principle, which forbids coupling of scalar reactions to vector fluxes in isotropic media, and its experimental status: [unverified].
- The Nernst–Planck equation, Fick's 1855 origin, and Bodenstein's steady-state approximation: [unverified].
- Variational TST, Kramers theory and tunnelling corrections were not covered beyond the TST summary.
- Experimental tests of Onsager reciprocity in chemistry from 2023–2026 were not searched (search budget exhausted).

## 4. Where chemistry's literature confuses or merges state and flow descriptions

### Takeaway
Equilibrium and steady state share the same observing: constant composition. The literature repeatedly lets that shared observing carry one word ("equilibrium") or one law ("mass action") across two different explainings. One is zero net flux with pairwise balance. The other is throughput, balanced by inflow and outflow, that dissipates. Operational separators exist (closing the system, net cycle flux, detailed balance), but the terminology often blurs them.

### Cited Findings
- **One name for two laws.**
  - "Law of mass action" is used inconsistently for both the equilibrium formula and the rate formula, and the rate version is generally wrong except for elementary reactions — [Law of mass action](https://en.wikipedia.org/wiki/Law_of_mass_action).
  - The Chemical-equilibrium entry says the Guldberg–Waage law is valid only for concerted one-step reactions, while the Law-of-mass-action entry holds that the equilibrium expression is correct in general. This source conflict mirrors the state/flow merger — [Chemical equilibrium](https://en.wikipedia.org/wiki/Chemical_equilibrium).
- **Dynamic equilibrium filed under steady state.** One entry defines dynamic equilibrium as a particular steady state. The Steady-state entry calls steady state the more general case, one that needs flow through the system. It adds that a steady state need not be a dynamic equilibrium, because some of its processes may be irreversible — [Dynamic equilibrium](https://en.wikipedia.org/wiki/Dynamic_equilibrium); [Steady state](https://en.wikipedia.org/wiki/Steady_state).
- **"Equilibrium" for steady states in neighbouring fields.** Electrical engineering calls a circuit's steady state an equilibrium condition. Fibre optics uses "equilibrium mode distribution". Solow–Swan growth theory calls its steady state an economic equilibrium — [Steady state](https://en.wikipedia.org/wiki/Steady_state).
- **Physiology.**
  - Homeostasis (Cannon, who coined the term in 1926; *The Wisdom of the Body*, 1932) maintains constancy by regulation.
  - The Steady-state entry says homeostasis works through multiple dynamic-equilibrium adjustments. The Homeostasis entry speaks of blood gases returning to equilibrium.
  - Bernard's internal-environment idea is dated 1849 in one entry and 1865 in the other (source conflict).
  - Sources: [Homeostasis](https://en.wikipedia.org/wiki/Homeostasis); [Steady state](https://en.wikipedia.org/wiki/Steady_state).
- **Press release vs paper.** The broken-detailed-balance result was announced with a headline saying the equilibrium of living cells is unsteady. The body of the release explains that energy-consuming cycles keep cells out of thermodynamic equilibrium — [NWO-I news, 29 April 2016](https://archief.nwo-i.nl/en/news/2016/04/29/researchers-find-that-the-equilibrium-of-living-cells-is-unsteady/).
- **Operational separator.** Detailed balance is stronger than stationarity — [Detailed balance](https://en.wikipedia.org/wiki/Detailed_balance). Net probability flux in a coarse-grained configuration space detects non-equilibrium in a stationary system — [Battle et al. 2016](https://scholars.duke.edu/publication/1427814).
- **Modelling produces steady states.** Holding some concentrations fixed (chemostatting) makes a network that has detailed balance look non-equilibrium. The failure of detailed balance then measures distance from equilibrium — [Franco & Velázquez 2025](https://arxiv.org/abs/2502.04754).
- **Equilibrium assumptions inside rate theories.**
  - TST assumes quasi-equilibrium between reactants and activated complexes that are not Boltzmann-distributed — [Transition state theory](https://en.wikipedia.org/wiki/Transition_state_theory).
  - Michaelis and Menten assumed rapid binding equilibrium where later texts use a steady state — [Johnson & Goody 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3381512).
  - The steady-state approximation treats short-lived radicals as having constant concentration — [Rate equation](https://en.wikipedia.org/wiki/Rate_equation).
- **Equal rates do not explain equilibrium.** The kinetic picture of equal forward and reverse rates is necessary, but it does not explain why equilibrium is reached; that comes from the free-energy minimum — [Chemical equilibrium](https://en.wikipedia.org/wiki/Chemical_equilibrium).
- **A naming paradox.** A concentration quotient extrapolated to zero ionic strength is called a thermodynamic constant — [Chemical equilibrium](https://en.wikipedia.org/wiki/Chemical_equilibrium).
- **Fluctuations at equilibrium.** The 1972 FCS work was framed as showing that average properties stay constant while microscopic concentrations fluctuate and relax through the reaction mechanism — [Physics Today 1972](https://physicstoday.aip.org/news/fluctuations-at-chemical-equilibrium).
- **Constant composition read as inactivity (education).**
  - A 2023 survey of UK GCSE and A-level students found:
    - 6% (GCSE) and 13% (A-level) held that reactions stop at equilibrium;
    - 48% and 25% confused constant concentrations with equal ones;
    - 83% and 75% took a closed system to be a feature of equilibrium rather than a condition for it;
    - 40% and 19% thought a catalyst raises yield.
  - The survey cites Hackling & Garnett 1985; Tyson et al., J. Chem. Educ. 76 (1999); Bergquist & Heikkinen, J. Chem. Educ. 67 (1990); Cheung, J. Chem. Educ. 86 (2009); and Quilez-Pardo & Solaz-Portoles, J. Res. Sci. Teach. 32 (1995).
  - Source: [Riddle & Lo-Fan-Hin, New Directions in the Teaching of Natural Sciences 18(1), 2023](https://journals.le.ac.uk/index.php/new-directions/article/download/3900/3677/13531).
  - Earlier, Kousathana and Tsaparlis (Chem. Educ. Res. Pract. Eur. 3, 5–17, 2002) sorted student errors on numerical equilibrium problems into five categories, one of which is the direction of a reaction that is not at equilibrium — [RSC](https://pubs.rsc.org/en/content/articlehtml/2002/rp/b0rp90030c).
  - **Status: persistent as of 2023.**
- **Le Chatelier treated as a law.** The principle is taught as general, but it has exceptions even for ammonia synthesis — [Corti & Franses 2003](https://journals.flvc.org/cee/article/download/122716/121755).

### Inferences
- Chemical writing uses "equilibrium" for at least three referents:
  - (i) thermodynamic: zero affinity, a minimum of G, detailed balance, no entropy production;
  - (ii) stationary: d/dt = 0 for the observed concentrations, possibly with net throughput and dissipation, i.e. a steady state;
  - (iii) regulatory: a maintained set point, as in homeostasis.
  
  All three share the observing of constant composition. What separates them (net throughput, pairwise balance, behaviour when the system is closed) cannot be seen in composition alone.
- A discriminating operation follows from the definitions. Isolate the system by cutting off inflow and outflow: an equilibrium persists, while a steady state relaxes. This is my inference, not a sourced protocol.
- The student belief that "the reaction stops" and the textbook statement that "equilibrium is dynamic" both rest on the same observing. The textbook adds traffic that is not observed in class. Tracer exchange experiments are the observings that could ground it in teaching.

### Gaps
- Secular equilibrium in radioactive decay chains, a steady state that is called an equilibrium: [unverified], because the page was unreachable.
- I did not open Journal of Chemical Education articles devoted to the wording "dynamic equilibrium"; they are seen only through citations in the 2023 paper.
- Cannon's own discussion of how homeostasis differs from physical equilibrium: [unverified].

## 5. Tentative placement beside the ten ways a conception can fix a changing thing as unchanging

### Takeaway
All placements below are tentative proposals by this researcher. No external source uses the registry's list, so the report writer should treat them as hypotheses to test.
- Most state concepts fall under way 2 (reference zeros), way 4 (conserved quantities read as stocks), and ways 3 and 5 (end states and middle states).
- Most flow concepts fall under ways 7, 8 and 9: one clock, rates as values, and reversible pairs read one way.
- The transition-state dividing surface and the electrode interface are the clearest cases of way 10.

### Cited Findings
These are the facts that anchor the placements; each is cited in full in §§1–4.
- **Declared zeros:** the SHE at 0 V at every temperature ([Gold Book S05917](https://goldbook.iupac.org/terms/view/S05917)); ΔfH° = 0 for reference allotropes, with white phosphorus as the exception, and p° = 1 bar ([Standard state](https://en.wikipedia.org/wiki/Standard_state)); Planck's choice of S(0) = 0 ([Marquet 2019](https://arxiv.org/pdf/1904.11696)).
- **End states:** equilibrium reached only after infinite time ([Abrash translation](https://web.chemteam.info/Chem-History/Concerning-Affinity.html)); 0 K unattainable ([Marquet 2019](https://arxiv.org/pdf/1904.11696)).
- **Middles:** the G minimum lies between pure reactants and pure products ([Chemical equilibrium](https://en.wikipedia.org/wiki/Chemical_equilibrium)); the transition state as a saddle point ([Transition state theory](https://en.wikipedia.org/wiki/Transition_state_theory)).
- **Cuts:** the TST dividing surface, whose placement changes the computed rate, which is why variational TST moves it ([Transition state theory](https://en.wikipedia.org/wiki/Transition_state_theory)); an absolute potential defined with no additional metal–solution interface ([mirror](https://wikipedia.classicistranieri.com/en/articles/a/b/s/Absolute_electrode_potential.html)); only the top layer of PbSO₄ exchanging ([Hevesy Nobel lecture](https://nobelprize.org/uploads/2018/06/hevesy-lecture.pdf)).
- **One clock:** the steady-state approximation and the relaxation rate k₁ + k₋₁ ([Rate equation](https://en.wikipedia.org/wiki/Rate_equation)); rapid-equilibrium binding ([Johnson & Goody 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3381512)).
- **Rates as values:** the originally temperature-independent Arrhenius pre-factor ([Arrhenius equation](https://en.wikipedia.org/wiki/Arrhenius_equation)); I₀ as a characteristic magnitude ([Gold Book E02238](https://goldbook.iupac.org/terms/view/E02238/plain)).
- **One side:** irreversible steps as limits of reversible ones ([Gorban & Yablonsky](https://www.arxiv.org/pdf/1101.5280)); irreversible steps assumed by Van Slyke and Cullen ([Johnson & Goody 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3381512)).
- **Stocks:** Gibbs's "available energy" ([Gibbs free energy](https://en.wikipedia.org/wiki/Gibbs_free_energy)); the mole as a counted number since 2019 ([RSC AMC brief](https://pubs.rsc.org/en/content/articlehtml/2019/ay/c9ay90028d)).

### Inferences
**Master table.** Columns: observed or measured | what the explaining adds | where it reaches past its observings | label | tentative registry placement. Registry ways: 1 a past record treated as the thing · 2 an initial condition or reference point treated as a location · 3 an end state treated as final · 4 a conserved quantity treated as a held stock · 5 an intermediate or optimum treated as a destination · 6 a direction treated as an amount · 7 two processes forced to one clock · 8 a rate treated as a constant property · 9 a reversible pair read one way · 10 an interface treated as a sharp partition.

| Conception | Observed / measured | Explaining adds | Reaches past | Label | Placement (tentative) |
|---|---|---|---|---|---|
| State functions U, H, S, G, A | Heat, work, EMF between equilibrium states | Functions of state alone (exact differentials) | Only equilibrium states; hysteresis excluded | CONV/MODEL | 4 (energy as a held stock); 1 (tabulated values read as the substance's own) |
| ΔfH°, ΔfG° | Reaction heats, EMFs, K values | Elements in reference forms set to zero | Choice of allotrope (white P) | CONV | 2 |
| Third-law entropy | Cp(T) down to the lowest T reached; latent heats | S(0) = 0 for a perfect crystal | 0 K unattainable; frozen-in disorder missed | REC + CONV | 2, 3, 1 |
| Residual entropy of ice | Calorimetric shortfall of 0.82 ± 0.05 | Proton-disorder count, series, simulation | Theory far more precise than experiment | MODEL/SIM | 4 (disorder held as entropy at 0 K), 3 |
| Chemical potential, activity, fugacity | Vapour pressure, EMF, freezing point | Partial molar G relative to a reference; activity relative to a standard state | Single-ion activity unmeasurable | CONV/MODEL | 2; 6 (a gradient's direction becomes a "driving force" magnitude) |
| Standard state | Nothing directly; extrapolated limits | Hypothetical ideal gas at 1 bar; ideal-dilute 1 mol kg⁻¹ | Non-physical states | CONV | 2 |
| SHE and absolute potential | Cell EMFs; Hg at its point of zero charge | 0 V at every T; 4.44 V absolute | Requires a single-ion activity | CONV/REC | 2, 10 |
| 2019 SI | None new | Fixed N_A, k, h | M_u becomes measured | CONV | 2; 4 (amount as a counted stock) |
| Equilibrium constant K | Concentration quotients in a medium; EMF; spectra | Thermodynamic K via activities; ΔG° = −RT ln K | Extrapolation to zero ionic strength; depends on conventions | REC + CONV | 3 (end composition as a fixed number), 1, 9 (how the equation is written fixes K or 1/K) |
| "Reaction stops at equilibrium" (misconception) | Constant composition | Inactivity | Contradicted by tracer exchange | — | 3, 9 |
| Dynamic equilibrium | Constant composition plus tracer, I₀, EXSY, FCS, smFRET exchange | Equal and opposite traffic | Assumed for systems never tested | MODEL → REC | Counters 3 and 9 |
| Detailed balance, Wegscheider | Zero net cycle flux; ratios of rate constants | Each step balanced by its own reverse | Rests on microreversibility assumptions | MODEL | 7 (each forward step and its reverse at one rate) |
| Le Chatelier | Composition change after a disturbance | A qualitative "shift that opposes" | Exceptions (N₂ fraction above 0.5) | MODEL (heuristic) | 6 (the direction of a shift taken as its size), 3 |
| Rate law, rate constant | Concentration–time data under fixed conditions | k as a constant of the reaction | Tied to conditions; order equals molecularity only for elementary steps | REC | 8 |
| Arrhenius Ea; Eyring ΔH‡, ΔS‡ | k(T) | Barrier height; activation parameters | Curved plots; pre-factor T-dependence cannot be determined | REC → MODEL | 8, 1 |
| Transition state | Femtosecond transients; photoelectron spectra | A saddle-point "species" in quasi-equilibrium | About 10⁻¹³ s; assigned via simulated surfaces | MODEL/SIM | 5 (a middle treated as a species), 10 (the dividing surface) |
| Steady-state approximation; rate-determining step | Overall rate law (e.g., order 3/2) | d[intermediate]/dt = 0 | Intermediates not literally constant | MODEL | 7 |
| Michaelis–Menten | Initial rates against [S] (polarimetry) | ES complex; Km, Vmax | Rapid equilibrium and steady state not distinguished by the form | MODEL | 7, 8, 5 |
| Exchange current I₀ | Currents near equilibrium (method unverified) | Two equal partial currents at zero net current | Partial currents not measured separately | CONV/REC | 8 (I₀ as an electrode constant), 10 (the interface); counters 9 |
| Onsager reciprocity | Cross-effect coefficients (thermoelectric, electrokinetic, diffusion) | Symmetric L matrix | Meagre evidence for reactions; linear regime only | REC (transport) / MODEL (reactions) | 7, 6 |
| Fick, Fourier, Ohm | Flux against gradient; tracer self-diffusion | Constant D, κ, σ | Linear regime only | REC → MODEL | 8, 6 |
| Steady state called "equilibrium"; homeostasis | Constant composition or variable with throughput | A set point; "balance" | Net flux hidden | MODEL (wording) | 5, 3 |
| G minimum | (Inferred from K and calorimetry) | A destination of the extent of reaction | The minimum lies between the two ends | MODEL | 5, 3 |
| Tracer exchange at a surface | Redistribution of the label | Molecular traffic; surface area | Assumes the label behaves like unlabelled atoms | OBS → REC | 10 (surface layer vs bulk); counters 3 |

**Reasoning for the less obvious placements**
- **Way 5 (a middle treated as an end).** The equilibrium composition is a minimum *between* pure reactants and pure products. Calling it the reaction's "position" or "endpoint" turns a middle into a destination. The transition state is a saddle, a middle along the reaction coordinate, yet TST gives it the standing of a species with its own equilibrium constant.
- **Way 10 (an interface treated as a sharp partition).** In TST the computed rate depends on where the dividing surface is placed: conventional TST over-counts recrossings, and variational TST moves the surface. The SHE convention and the absolute potential both rest on defining away, or isolating, a single metal–solution interface. Hevesy's surface-area method treats "top layer exchanges, bulk does not" as a sharp division.
- **Way 7 (two processes forced to one clock).** The steady-state and rapid-equilibrium approximations bind fast steps to the clock of a slow one. Detailed balance forces each forward step and its reverse to the same rate. The relaxation constant k₁ + k₋₁ merges two processes into a single beat.
- **Way 6 (a direction treated as an amount).** "Driving force" in ΔG, affinity and Onsager forces turns the sign and direction of a gradient into a magnitude. Le Chatelier's "shift" is a direction of change that is often read as an amount. The ammonia exception shows that the direction can reverse while the "amount" of disturbance stays the same.
- **Ways 3 and 9 together.** Reading constant composition as an end state (way 3) and reading a reversible reaction as running one way (way 9) go together in the student data. Tracer, EXSY, FCS, smFRET and I₀ observations are the chemical counter-observings to both.

**Membership criteria in chemistry's own terms**, for treating these classifications as candidate sets:
- **"State function":** a quantity whose change between two equilibrium states does not depend on the path, i.e. has an exact differential.
- **"System at equilibrium":** zero affinity for every reaction; uniform T, p and μ; and, as a stronger extra condition, detailed balance for every elementary step.
- **"Steady state":** all observed concentrations constant in time. Net throughput is allowed.
- **"Elementary reaction":** a reaction whose measured orders equal its stoichiometric molecularity. The test is partly circular, because molecularity is inferred from the mechanism the orders are meant to support.

### Gaps
- No literature applies the registry's ten ways to chemistry. All placements above are untested proposals.
- Ways 1 and 4 are the least specific in chemistry. Many tabulated quantities could be filed under either, and the report writer may need sharper criteria to separate them.
