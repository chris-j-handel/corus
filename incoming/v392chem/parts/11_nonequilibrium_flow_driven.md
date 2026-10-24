# Nonequilibrium and flow-driven chemistry: concepts, driven systems, observings and open disputes

## Key gathered points

- **Minimum entropy production (Prigogine)** is a theorem about a linear model: linear flux–force laws, constant Onsager-symmetric coefficients, and some forces fixed at the boundaries. Outside that model it fails, with explicit counterexamples even in ordinary heat conduction. For chemical reactions the linear window is narrow. It is not a general selection principle.
- **Glansdorff–Prigogine** nonlinear criteria have had their range and meaning questioned since 1974. A standard summary judges a general far-from-equilibrium extremal principle infeasible at present.
- **Maximum entropy production (MEP)** is several distinct principles (Ziegler, Paltridge, Dewar). Dewar's derivations drew published objections (2007, 2011), and Dewar (2009) recast MEP as an inference method, not a law. Model attractors exist that are neither maximum- nor minimum-dissipation. Prior status: an open heuristic.
- **Chemical reaction network theory (CRNT):** the deficiency-zero, deficiency-one, Horn–Jackson and Boros existence theorems hold for all rate constants.
  - The Global Attractor Conjecture is proved for two-dimensional compatibility classes, three species, three-dimensional classes, and single linkage classes.
  - Craciun posted a general proof (arXiv 2015; no journal reference shown). His 2019 preprint still calls toric inclusions an "approach".
  - The Persistence Conjecture is open in general (prior, 2018–19). Its 2026 status is [unverified].
- **Stochastic thermodynamics:** the thermodynamic uncertainty relation (TUR; 2015, proved for Markov steady states in 2016) sets the price of precision ε at no less than 2k_BT/ε² of dissipation.
  - A colloidal test satisfied it. It fails outside its scope (quantum, transient), and it had no underdamped proof as of 2020.
  - Kinetic proofreading lowers the error rate from about e^(−βΔ) to about e^(−2βΔ), at a cost in energy and speed.
- **Fuelled assembly:** Ragazzon & Prins (2018) separate three cases: fuel-templated transient assembly (no energy stored), dissipative self-assembly, and driven (energy-storing) assembly. Energy storage requires kinetic asymmetry.
- **Catalysis-driven motors** now show measured net directional bond rotation:
  - a carbodiimide-fuelled N–C rotor (Leigh group, 2022), with up to 71:29 directional bias and more than 97% of fuel passing through the motor cycle;
  - an enzyme-gated redox C–C rotor (2025).
- **Power stroke dispute:** Astumian holds that kinetic asymmetry, not a power stroke, sets the direction, stall force and optimal efficiency of chemically driven motors. Hwang & Karplus (2019) and Wagoner & Dill (2016) dissent, but on different observables and with a different definition of "power stroke".
- **Broken detailed balance** is directly observable as net probability flux in coarse-grained shape space (Battle et al. 2016, flagella and primary cilia).
- **England's dissipative adaptation** rests on bounds and simulations. Critics note it compares trajectories with their reverses, not with alternatives. Status: open.

### Labels, verification and coverage

- **Labels:**
  - **[OBS]** observing
  - **[REC]** reconstruction from observings
  - **[DEF]** convention or definition
  - **[MOD]** model construct, including theorems about models
  - **[SIM]** simulation
- **Entry format:** "Observed:" gives what was measured (method, sample, conditions, quantity). "Added:" gives what the field's model, convention or interpretation contributes.
- **Verification:**
  - A linked source was opened in this session (the page, its abstract, or its repository record).
  - "Reference entry seen in X" means the citation was read inside an opened page, but the work itself was not opened.
  - **[unverified]** marks background knowledge not checked in this session.
- **Coverage limits:**
  - The session's shared web-search allowance ran out after ten searches, and the hourly fetch limit was then reached. Many publisher DOI links could not be fetched.
  - Verified post-2022 items are Berreur et al. 2025 (*Nature*), Wang, Yuan & Hao 2024 (review), Timpanaro 2024 (arXiv), and Tadjibaev & Tadjibaev 2024 (preprint, not peer reviewed).
  - Every other standing below is **prior**, meaning as of the newest source seen. Other 2023–2026 developments are unverified.

---

## 1. Linear and nonlinear nonequilibrium thermodynamics: is minimum or maximum entropy production a general selection principle?

### Takeaway
Entropy production is a well-defined local balance quantity within the local-equilibrium framework. The minimum entropy production (MinEP) theorem holds only inside a linear model with stated constraints. The Glansdorff–Prigogine generalisations and the several maximum-entropy-production principles each face derivation critiques, model counterexamples, or a retreat to inference-only status. Neither MinEP nor MEP is established as a general selector of nonequilibrium steady states (prior: sources from 1957 to 2022, plus one 2024 preprint).

### Cited Findings

**Framework and definitions**
- [DEF] **Local equilibrium.**
  - Thermodynamic variables are defined locally and assumed to relax fast compared with macroscopic change.
  - The assumption has been tested at shock fronts, reacting surfaces and steep thermal gradients.
  - It fails when relaxation times are not well separated: very rarefied gases, the upper atmosphere, and low-temperature interacting fermions. Appreciable nonlinear effects can also occur locally.
  - Source: [Wikipedia: Non-equilibrium thermodynamics](https://en.wikipedia.org/wiki/Non-equilibrium_thermodynamics), citing Hafskjold et al. 2021, *Phys. Rev. E* 104, 014131, and De Groot & Mazur 1962.
- [MOD] **Onsager reciprocal relations** (Onsager 1931, *Phys. Rev.* 37, 405, doi:10.1103/PhysRev.37.405). Near equilibrium, fluxes are linear in forces. The second law requires a positive-definite coefficient matrix, and its symmetry rests on statistical arguments from microscopic reversibility.
  - Source: [Wikipedia: Non-equilibrium thermodynamics](https://en.wikipedia.org/wiki/Non-equilibrium_thermodynamics).
  - A later derivation of Onsager reciprocity from a fluctuation theorem is Andrieux & Gaspard 2004, *J. Chem. Phys.* 121, 6167 (reference entry seen in [Marsh, arXiv:2204.00416](https://arxiv.org/pdf/2204.00416)).
- [DEF] **Entropy production rate.** σ = Σ J_k X_k ≥ 0, the sum of fluxes times conjugate forces. For a reaction, the force is affinity/T and the flux is the net rate. This standard form was not displayed on the pages opened here [unverified].
- [DEF] **Dissipative structure.**
  - Definition: an open system that exchanges energy and matter and settles into a reproducible state, often far from equilibrium, with spontaneous symmetry breaking and long-range correlations.
  - Prigogine coined the term and received the 1977 Nobel Prize in Chemistry for nonequilibrium thermodynamics, especially this theory.
  - His Nobel lecture appeared in *Science* in 1978 (doi:10.1126/science.201.4358.777).
  - Sources: [Wikipedia: Dissipative system](https://en.wikipedia.org/wiki/Dissipative_system); [Wikipedia: Ilya Prigogine](https://en.wikipedia.org/wiki/Ilya_Prigogine).
  - Membership criterion in chemistry's terms: the order exists only while an external flux or drive is maintained, and it decays when the drive is removed.

**Prigogine's minimum entropy production theorem (MinEP)**
- [MOD] **Statement.** With constant external parameters, a linear system relaxes to a stationary state of minimal entropy production consistent with the constraints that hold it off equilibrium. Without such constraints, entropy production falls to zero. Source: [Wikipedia: Prigogine's theorem](https://en.wikipedia.org/wiki/Prigogine%27s_theorem).
- [MOD] **Assumptions.** Linear flux–force relations, valid Onsager reciprocity, constant phenomenological coefficients, and time-invariant boundary conditions. Source: [Su, Hua & Guo, arXiv:2202.08001](https://arxiv.org/pdf/2202.08001).
- [MOD] **Scope.**
  - The theorem holds only approximately for real systems.
  - Linearity spans a wide range for heat conduction and diffusion (Fourier, Fick), but for chemical reactions only a narrow region near equilibrium.
  - The principle is violated for systems odd under time reversal.
  - Source: [Wikipedia: Prigogine's theorem](https://en.wikipedia.org/wiki/Prigogine%27s_theorem), citing Jørgensen & Svirezhev 2004 and Kjelstrup & Bedeaux 2008.
- [MOD] **Microscopic extension (1957).**
  - The result was extended to the full microscopic density matrix at zero magnetic field.
  - The theorem rests on the vanishing of kinetic coefficients that couple time-even and time-odd variables. The paper notes limits when a magnetic field is present.
  - Source: [Phys. Rev. 105, 360 (1957)](https://dx.doi.org/10.1103/PhysRev.105.360). The author was not shown on the page; attribution to H. B. Callen is [unverified].
- [MOD/SIM] **Counterexamples.**
  - For heat conduction, MinEP requires conductivity proportional to 1/T², which few materials satisfy.
  - Under Fourier's law the time derivative of entropy production has an indefinite sign, so suitable initial temperature fields violate MinEP.
  - Fick's law violates it when ∇²φ > 0. Two parallel resistors at different temperatures give an electrical counterexample.
  - The authors call the "entropic constitutive relation" assumption circular, because it amounts to assuming MinEP.
  - [SIM] In a one-dimensional numerical test, entropy production rose until the system became stationary.
  - Source: [Su, Hua & Guo](https://arxiv.org/pdf/2202.08001).
- [MOD] **Conflict with balance equations** (Bertola & Cafaro 2008, *Int. J. Heat Mass Transfer* 51, 1907–1912, doi:10.1016/j.ijheatmasstransfer.2007.06.041).
  - MinEP field equations conflict with continuum balance equations for heat conduction in a fluid at rest and for shear flow with heat conduction.
  - No assumed temperature dependence of conductivity or viscosity restores agreement.
  - Their review of the proof concludes that the stationary minimum must be zero.
  - Source: [Edinburgh Research Explorer record](https://www.research.ed.ac.uk/en/publications/a-critical-analysis-of-the-minimum-entropy-production-theorem-and/).
- [MOD] **Further cited limits.**
  - Radiative transfer: Essex 1984, *Astrophys. J.* 285, 279, doi:10.1086/162504.
  - Grandy (2008) cautions that the internal entropy-production rate is hard to define.
  - Both cited in [Wikipedia: Non-equilibrium thermodynamics](https://en.wikipedia.org/wiki/Non-equilibrium_thermodynamics); contents not opened.
  - Jaynes 1980, *Annu. Rev. Phys. Chem.*, is listed by [Su et al.](https://arxiv.org/pdf/2202.08001) (not opened).

**Glansdorff–Prigogine (GP) criteria**
- [MOD] **General evolution criterion.**
  - The part of the change in entropy production due to changing forces, d_XP/dt, is non-positive regardless of linearity.
  - Critics call it ambiguous and without clear physical meaning. They also note it is not specific to entropy, since it holds for non-entropic constitutive relations too.
  - Originals: Glansdorff & Prigogine 1954 (*Physica*); book 1971.
  - Source: [Su, Hua & Guo](https://arxiv.org/pdf/2202.08001).
- [MOD] **Stability criterion (second-order "excess entropy production").**
  - Keizer & Fox 1974 (*PNAS* 71, 192–196, doi:10.1073/pnas.71.1.192) questioned its range of validity.
  - Later treatments (Lebon, Jou & Casas-Vázquez 2008; Šilhavý 1997) judged the prospects for global extremal principles clouded.
  - Source: [Wikipedia: Non-equilibrium thermodynamics](https://en.wikipedia.org/wiki/Non-equilibrium_thermodynamics). Keizer & Fox not opened.
- [MOD] **Stability far from equilibrium.**
  - Near equilibrium, a Lyapunov function guarantees stability. Far from it, stability can be lost, for example through Hopf bifurcations in autocatalytic models such as the Brusselator (Lemarchand & Nicolis 1976, doi:10.1016/0378-4371(76)90079-0).
  - Attempts to extend the Onsager and MinEP results far from equilibrium failed, and some gave opposite results.
  - Source: [Wikipedia: Dissipative system](https://en.wikipedia.org/wiki/Dissipative_system).
- [DEF/assessment] **Summary verdict.**
  - No general law for stationary nonequilibrium states comparable to the second law is known. A general extremal principle "seems infeasible in the current state of knowledge".
  - Bodenschatz et al. 1992 (*Physica D* 61, 77) is cited for experiments on systems with non-variational aspects.
  - Source: [Wikipedia: Non-equilibrium thermodynamics](https://en.wikipedia.org/wiki/Non-equilibrium_thermodynamics).

**Chemical oscillators as observed dissipative structures**
- [OBS] **Belousov–Zhabotinsky (BZ) reaction.**
  - Observed (stirred solution): in the cerium-catalysed bromate/malonic-acid system, the Ce(IV)/Ce(III) ratio oscillates, so the solution alternates between yellow and colourless.
  - Observed (unstirred dishes with ferroin): spots grow into expanding rings and spirals. Shaking erases them and they re-form.
  - The waves continue until the reagents are consumed, so in a closed vessel the behaviour is transient.
  - Overall stoichiometry: 3 CH₂(CO₂H)₂ + 4 BrO₃⁻ → 4 Br⁻ + 9 CO₂ + 6 H₂O.
  - History: Belousov first saw the oscillation in 1951 and was rejected by two journals. He published in 1959 in a non-reviewed venue. Zhabotinsky took over the project in 1961, and the West learned of it at a 1968 Prague meeting (Winfree 1984, *J. Chem. Educ.*, doi:10.1021/ed061p661).
  - Added: classification as a far-from-equilibrium dissipative structure.
  - Source: [Wikipedia: BZ reaction](https://en.wikipedia.org/wiki/Belousov%E2%80%93Zhabotinsky_reaction).
- [MOD] **FKN mechanism and Oregonator.**
  - The Field–Kőrös–Noyes (FKN) mechanism has about 18 elementary steps and 21 species.
  - The Oregonator reduces it to three intermediate variables and reproduces limit-cycle oscillation. It is a model calibrated to the observed oscillation.
  - Sources: [Wikipedia: Oregonator](https://en.wikipedia.org/wiki/Oregonator); [Wikipedia: BZ reaction](https://en.wikipedia.org/wiki/Belousov%E2%80%93Zhabotinsky_reaction).
- [unverified] Sustained, non-decaying oscillation is normally obtained in continuously fed stirred-tank reactors (CSTRs), which hold the system at a fixed distance from equilibrium.

**Maximum entropy production (MEP)**
- [DEF] **Several principles, not one.**
  - Ziegler's principle applies in linear response.
  - Paltridge's climate principle is a "partial steady state" version.
  - Dewar's path-space MaxEnt derivations come in "linear-response" and "total steady state" variants.
  - A non-variational MEP is also used in some fluid-dynamics work.
  - Source: [Bruers 2007, arXiv:0705.3226](https://ar5iv.arxiv.org/html/0705.3226).
- [REC/MOD] **Evidence offered.**
  - Paltridge (1979, as cited) and Lorenz (2003) argue that planetary winds and currents arrange themselves to maximise entropy production. This rests on model fits to observed climate.
  - Qualitative examples include forests producing more entropy than deserts at the same latitude.
  - Source: [Lineweaver, "Cosmological and biological reproducibility: limits on the MEP principle"](https://www.mso.anu.edu.au/~charley/papers/mepp.pdf).
- [MOD] **Critiques of the derivations.**
  - Bruers: Dewar's 2003 derivation yields *minimum* entropy production in the linear regime. The main-text derivation of his second paper works only in linear response, and its appendix leaves points unresolved. Paltridge's principle is unrelated to Dewar's. Source: [Bruers](https://ar5iv.arxiv.org/html/0705.3226).
  - Grinstein & Linsker 2007 (*J. Phys. A*, doi:10.1088/1751-8113/40/31/N01): an error invalidates the far-from-equilibrium derivation, and the claimed link to self-organised criticality is unsupported. Source: [Zenodo record](https://zenodo.org/record/889780).
  - Paquette 2011 (*J. Phys. A* 44, 368001, doi:10.1088/1751-8113/44/36/368001): the 2003/2005 analysis rests on a physically unrealistic assumption. Source: [McMaster record](https://experts.mcmaster.ca/scholarly-works/1577788).
- [MOD] **Dewar's reframing (2009).**
  - MEP is not a physical principle. It is equivalent to Jaynes's MaxEnt inference applied to nonequilibrium systems.
  - Failed predictions therefore indict the physical assumptions fed in, not MEP itself.
  - He concedes the equivalence is not rigorously shown far from equilibrium.
  - Source: *Entropy* 11, 931–944, doi:10.3390/e11040931; [ANU record](https://researchportalplus.anu.edu.au/en/publications/maximum-entropy-production-as-an-inference-algorithm-that-transla/).
- [SIM] **Atmospheric-model counterexample.** Nicolis 1999 (*Q. J. R. Meteorol. Soc.* 125, 1859, doi:10.1002/qj.49712555718) found an atmospheric model's attractor to be neither a maximum- nor a minimum-dissipation regime. Cited in [Wikipedia: Non-equilibrium thermodynamics](https://en.wikipedia.org/wiki/Non-equilibrium_thermodynamics); not opened.
- [MOD] **Convection.** Attard 2012 (arXiv:1208.5105) argues heat convection does not obey extremal principles for the entropy-production rate. Same Wikipedia citation; not opened.
- [MOD] **Restricted defence (Lineweaver).**
  - MEP applies only to reproducible dissipative structures, such as planetary climates and stars.
  - Identifying the constraints is the central open problem.
  - Living systems may sit at transient local maxima. He proposes long-term bacterial evolution experiments as a test.
  - Source: [Lineweaver](https://www.mso.anu.edu.au/~charley/papers/mepp.pdf).
- [MOD, 2024 preprint, not peer reviewed] **Exactly solvable Rayleigh-gas model.**
  - Free relaxation lowers entropy production toward zero (MinEP-like). Forced relaxation to a source/sink steady state makes it maximal.
  - The authors read the two principles as covering different conditions.
  - The text has internal inconsistencies, and its equations are given only as images.
  - Source: [Tadjibaev & Tadjibaev, Preprints.org 202412.1156](https://www.preprints.org/manuscript/202412.1156/v1).

### Inferences
- MinEP and the MEP principles answer differently constrained questions. MinEP fixes some forces in a linear model, while MEP variants fix fluxes, partial constraints or information constraints. Much of the apparent contradiction comes from comparing different constraint sets, consistent with Bruers's taxonomy and the Tadjibaev reading.
- Reaction rates depend exponentially on affinity. The linear (MinEP) regime therefore holds only for affinities small compared with RT. Fuelled assemblies, oscillators and motors (sections 4–5) all run outside it, so MinEP has no predictive role for them.
- Candidate classes with membership criteria, in chemistry's own terms:
  - *Equilibrium state:* every elementary process is balanced by its reverse (detailed balance), net fluxes are zero, and entropy production is zero.
  - *Nonequilibrium steady state (NESS):* state variables are constant while net fluxes and entropy production are nonzero, sustained by exchange at the boundary.
  - *Dissipative structure:* a NESS or periodic state with spatial or temporal order that exists only above a drive threshold.
  - *Near-equilibrium (linear) regime:* fluxes are linear in forces, with constant, Onsager-symmetric coefficients.

### Gaps
- Not opened:
  - Kondepudi & Prigogine, *Modern Thermodynamics* (1998; 2nd ed. 2015)
  - Glansdorff & Prigogine (1971)
  - Keizer & Fox (1974)
  - Martyushev & Seleznev's *Physics Reports* MEP review (2006) [unverified]
  - Ziegler's and Paltridge's originals
- No 2023–2026 MinEP or MEP literature could be searched. A paper worth checking is Endres (2017, *Sci. Rep.*), "Entropy production selects nonequilibrium states in multistable systems" [unverified; the direction of its result was not checked].
- CSTR-sustained BZ oscillation is [unverified] here.

---

## 2. Chemical reaction network theory: deficiency theorems, complex balance, multistationarity, and the status of the Persistence and Global Attractor Conjectures

### Takeaway
CRNT proves results from network structure alone that hold for all positive rate constants: the deficiency-zero and deficiency-one theorems, the Horn–Jackson complex-balance results, and Boros's existence theorem. The Global Attractor Conjecture (GAC) is proved in two-dimensional, three-species, three-dimensional and single-linkage-class cases. A general proof was posted by Craciun in 2015, but the arXiv record shows no journal reference. In 2019 Craciun described toric differential inclusions as an approach to both conjectures. The Persistence Conjecture was open in general in every source seen. The 2026 standing of both could not be verified.

### Cited Findings

**Definitions**
- [DEF] **Network vocabulary.**
  - A reaction network is a triple of species, complexes and reactions. Complexes are non-negative integer combinations of species, and reactions form a directed graph on complexes with no self-loops.
  - Linkage classes are the connected components of that graph. The stoichiometric subspace S is the span of the reaction vectors, and a compatibility class is (c₀ + S) ∩ the non-negative orthant.
  - Weakly reversible: each connected component is strongly connected.
  - Persistent: every positive trajectory keeps each coordinate's liminf above zero.
  - Permanent: there is a compact set inside the orthant that every positive trajectory eventually enters.
  - Source: [Craciun, Nazarov & Pantea, arXiv:1010.3050](https://ar5iv.arxiv.org/html/1010.3050).
- [DEF] **Deficiency.** δ = n − ℓ − s (complexes minus linkage classes minus dim S). This is the standard definition; not displayed on pages opened [unverified].
- [DEF] **Complex-balanced systems.**
  - A system admitting a positive complex-balanced equilibrium. The formal definition, in which inflow equals outflow at every complex, was not displayed [unverified wording].
  - Mass-action complex-balanced systems were named "toric dynamical systems" by Craciun, Dickenstein, Shiu & Sturmfels.
  - The unique positive equilibrium in a compatibility class is called the Birch point.
  - Source: [Pantea, arXiv:1103.0603](https://ar5iv.arxiv.org/html/1103.0603).

**Theorems** (all [MOD], i.e. mathematics about mass-action model constructs)
- **Horn–Jackson (1972, *Arch. Rational Mech. Anal.* 47, 81).**
  - A complex-balanced system has exactly one positive equilibrium per positive compatibility class, and that equilibrium is complex-balanced.
  - It is locally asymptotically stable via a strict Lyapunov function of free-energy form. That function does not by itself give global stability.
  - Sources: [Pantea](https://ar5iv.arxiv.org/html/1103.0603); [Wikipedia: CRNT](https://en.wikipedia.org/wiki/Chemical_reaction_network_theory).
- **Deficiency-zero theorem.**
  - Weakly reversible, deficiency-zero mass-action systems are complex-balanced for every choice of positive rate constants (Feinberg; Horn). Source: [Pantea](https://ar5iv.arxiv.org/html/1103.0603).
  - Reference: Feinberg 1987, *Chem. Eng. Sci.* 42, 2229–2268, the paper titled for the deficiency-zero and deficiency-one theorems. Source: [Wikipedia: CRNT](https://en.wikipedia.org/wiki/Chemical_reaction_network_theory).
  - The companion clause, that a deficiency-zero network that is not weakly reversible has no positive steady state for any kinetics, is [unverified].
- **Deficiency-one theorem.**
  - Feinberg's 1995 deficiency-one theorem is cited as guaranteeing positive steady states for a class of deficiency-one networks. Boros (2013) treated the weakly reversible deficiency-one case.
  - Source: [Boros, arXiv:1710.04732](https://arxiv.org/pdf/1710.04732).
  - The exact conditions are [unverified]: each linkage class has deficiency ≤ 1, these sum to the network deficiency, and each linkage class has a single terminal strong linkage class.
- **Existence for all weakly reversible networks (Boros).**
  - Every weakly reversible mass-action system has a positive steady state in every positive compatibility class. The proof uses Brouwer's fixed point theorem.
  - Deng, Feinberg, Jones & Nachman had claimed this in a 2011 arXiv manuscript. Boros calls their finiteness claim unsupported, and notes that Nachman proved the single-linkage-class case in the early 1980s without publishing it.
  - Source: [Boros](https://arxiv.org/pdf/1710.04732). Journal publication [unverified].
- **Multistationarity.**
  - Catalytic "trigger" mechanisms with multiple steady states are cited (Slin'ko et al. 1976; Bykov et al. 1976). Source: [Wikipedia: CRNT](https://en.wikipedia.org/wiki/Chemical_reaction_network_theory).
  - Not checked here [unverified]: the deficiency-one algorithm, injectivity criteria for excluding multistationarity (Craciun & Feinberg, about 2005–06), and absolute concentration robustness (Shinar & Feinberg 2010, *Science*).
- **Contraction result (Gorban, Bykov & Yablonskii 1986).** In systems without interactions between components, the weighted L1 distance between solutions with equal conserved quantities decreases monotonically. Source: [Wikipedia: CRNT](https://en.wikipedia.org/wiki/Chemical_reaction_network_theory).

**Conjectures and status**
- **The GAC.**
  - For complex-balanced mass-action systems, the unique positive equilibrium in each compatibility class attracts every interior trajectory.
  - Horn stated it in its present form in 1974. It is often called the field's leading open problem.
  - Sources: [Pantea](https://ar5iv.arxiv.org/html/1103.0603); [Craciun, arXiv:1501.02860](https://arxiv.org/abs/1501.02860).
- **Proven special cases (prior, sources 2010–2016):**
  - two-dimensional compatibility classes (Anderson & Shiu; Siegel & Johnston);
  - a single linkage class (Anderson);
  - three species (Craciun, Nazarov & Pantea);
  - three-dimensional classes (Pantea, Theorem 6.3).
  - Sources: [Pantea](https://ar5iv.arxiv.org/html/1103.0603); [CNP](https://ar5iv.arxiv.org/html/1010.3050).
  - Craciun's 2015 text describes the three-dimensional case as previously proved and the four-dimensional case as previously unproved.
- **Claimed general proof (Craciun, arXiv:1501.02860).**
  - Versions: v1 dated 13 January 2015; v2 dated January 2016.
  - It introduces toric differential inclusions.
  - Theorem C: toric dynamical systems are persistent.
  - Theorem D: the GAC.
  - Corollaries: detailed-balanced systems, and weakly reversible deficiency-zero systems, have the global-attractor property.
  - A sequel proving the Persistence Conjecture is listed as "in preparation".
  - No journal reference was shown on the arXiv record viewed.
  - Sources: [arXiv abstract](https://arxiv.org/abs/1501.02860); [v1 record](https://arxiv.org/abs/1501.02860v1).
- **Craciun 2019 (arXiv:1901.02544).**
  - One version, 8 January 2019, with no journal reference shown.
  - Recasts the GAC and the Persistence Conjecture as statements about polynomial systems generated by Euclidean embedded graphs.
  - Says the toric-inclusion embedding "suggests an approach for the proof" of both, without claiming completion.
  - Source: [arXiv abstract](https://arxiv.org/abs/1901.02544).
- **The Persistence Conjecture.**
  - Every weakly reversible mass-action system is persistent. Feinberg's earlier remark stated a weaker form: no positive trajectory converges to a boundary point.
  - The Extended Persistence Conjecture of Craciun, Nazarov & Pantea is proved for two species.
  - Persistence is proved for two-dimensional classes with bounded trajectories (Pantea, Theorem 5.1).
  - Persistence implies the GAC.
  - Sources: [Pantea](https://ar5iv.arxiv.org/html/1103.0603); [CNP](https://ar5iv.arxiv.org/html/1010.3050).
  - The Permanence Conjecture was listed as open in 2018. Source: [Boros](https://arxiv.org/pdf/1710.04732).
- **Endotactic networks.** This class strictly contains the weakly reversible networks. For two species, endotactic networks give permanent systems even with time-varying rate constants within compact bounds. Source: [CNP](https://ar5iv.arxiv.org/html/1010.3050).

### Inferences
- Detailed-balanced systems form a subclass of complex-balanced ones; Craciun 2015 treats them as a corollary class. Complex balance keeps a free-energy-like Lyapunov function while allowing net circulation among complexes [inference; the circulation point is unverified as phrased]. It is therefore a candidate class of flux-carrying but equilibrium-like steady states, useful when classifying nonequilibrium steady states.
- CRNT offers two kinds of membership criterion:
  - structural, from the graph alone (deficiency, weak reversibility, linkage classes);
  - parametric, from rate constants satisfying the complex-balance conditions.
  - Deficiency zero plus weak reversibility makes complex-balance membership structural, holding for all rate constants.
- Cautious standing for 2026:
  - special cases: settled;
  - general GAC: a proof has been claimed (2015), but whether it was published or accepted is [unverified];
  - Persistence Conjecture: open in general (prior, 2019).

### Gaps
- Not verified:
  - whether Craciun's proof appeared in a peer-reviewed journal or was independently checked by 2026;
  - progress on persistence for endotactic or other classes after 2019;
  - Gopalkrishnan, Miller & Shiu's "geometric approach" to the GAC (title seen cited in Boros; not opened).
- Feinberg's monograph *Foundations of Chemical Reaction Network Theory* (Springer, 2019) [unverified] was not opened.
- Experimental counterparts, such as multistability and hysteresis in CSTRs, were not gathered.

---

## 3. Stochastic thermodynamics: fluctuation theorems, thermodynamic uncertainty relations, speed limits, proofreading, and the cost of accuracy and timekeeping

### Takeaway
Stochastic thermodynamics assigns work, heat and entropy production to single trajectories. The TUR was conjectured in 2015 and proved for Markov jump steady states in 2016. It prices relative precision ε at no less than 2k_BT/ε² of dissipation. It held in an optical-trap test, and it fails or is unproven outside its scope.

Proofreading and biochemical timekeeping trade free energy and speed for accuracy or coherence. Single-molecule motor measurements give the observed energy budgets. No synthetic (non-biological) chemical TUR test was verified in this session.

### Cited Findings

**Framework**
- [DEF] **Scope of the framework.**
  - The systems are small and driven: colloids in time-dependent optical traps, single biomolecules manipulated by optical tweezers or AFM tips, and quantum dots.
  - Work, heat and entropy production are defined per trajectory, and their distributions obey integral and detailed fluctuation theorems.
  - Review: Seifert 2012, *Rep. Prog. Phys.* 75, 126001.
  - Source: [Seifert colloquium notice, Vienna 2015](https://lehre4.rad.univie.ac.at/share/WWW_Exchange/SEKRETARIAT/Wpk%20PDF%20files/WS%202015/Seifert_WPK_7-Dec-2015.pdf).
- [MOD] **Fluctuation theorems.**
  - Crooks 1999 (*Phys. Rev. E* 60, 2721–2726) relates entropy-production fluctuations to the nonequilibrium work relation for free-energy differences. Reference entry seen in [Marsh](https://arxiv.org/pdf/2204.00416).
  - Gallavotti–Cohen 1995, Jarzynski 1997, Crooks 1998 and Tasaki 2000 are listed in [Timpanaro](https://ar5iv.labs.arxiv.org/html/2407.10390).
  - Jarzynski 1997, *Phys. Rev. Lett.* 78, 2690: details [unverified].
- [OBS, unverified] **Classic single-molecule tests.**
  - Liphardt et al. 2002 (*Science*): an RNA hairpin pulled by optical tweezers; the equilibrium free energy was recovered from irreversible pulls via the Jarzynski equality.
  - Collin et al. 2005 (*Nature*): the forward and reverse work distributions of an RNA three-way junction crossed at ΔG, as the Crooks theorem predicts.
  - Primary pages not opened.
- [OBS] **DNA hairpin protocols.** In an optical trap, protocols that slow down in the hopping regime dissipated less than constant-speed protocols. Source: [Brown & Sivak, arXiv:1909.09180](https://arxiv.org/pdf/1909.09180); journal [unverified: *Chem. Rev.* 2020].

**Thermodynamic uncertainty relation (TUR)**
- [MOD] **Original statement** (Barato & Seifert 2015, *PRL* 114, 158101; arXiv submitted 20 February 2015).
  - Biomolecular processes are modelled as Markov networks.
  - Reaching uncertainty ε in an output, such as molecules made or motor steps, costs at least 2k_BT/ε², independent of elapsed time.
  - Named applications: motors, pumps, transcription, translation and enzymes.
  - Source: [arXiv:1502.05944](https://arxiv.org/abs/1502.05944v2).
- [MOD] **Proof.** The general bound was proved by Gingrich et al. 2016 using large deviations. Sources: [Pietzonka, Ritort & Seifert](https://ar5iv.arxiv.org/html/1702.07699); [Brown & Sivak](https://arxiv.org/pdf/1909.09180). Author list and DOI (*PRL* 116, 120601) are [unverified].
- [MOD] **Unicyclic motor form.**
  - Ω·t·ε² = ω·coth(ω/2) ≥ 2k_BT.
  - Reaching 1% precision requires at least 2×10⁴ k_BT.
  - For N-state cycles the bound approaches a Fano factor of 1/N.
  - Biomolecular motors approach the TUR limit in several cases, and a towed cargo raises precision.
  - Source: [Brown & Sivak](https://arxiv.org/pdf/1909.09180).
- [REC] **Finite-time TUR check on experimental data.**
  - Observed (Dieterich et al. 2015 data): a colloidal bead in an optical trap whose centre jumps between ±λ₀ at Poisson times. Switching rates were about 2.88, 8.73 and 12.3 s⁻¹. Fluctuating work was computed from trap position and measured force.
  - Added: the finite-time TUR held at all times and rates. It was about twice as tight as the long-time form at short times (about 5.4 versus 12.0 k_BT at t ≈ 0.03 s, as reported).
  - The finite-time form is proved only for short times and linear response.
  - Source: [Pietzonka, Ritort & Seifert, arXiv:1702.07699](https://ar5iv.arxiv.org/html/1702.07699).
- [MOD] **Tilted periodic potential.**
  - Q = ⟨q⟩ε² ≥ 2k_BT. The bound is attained both near and far from equilibrium when the dissipated heat is Gaussian.
  - The cost peaks near the critical force.
  - Source: [Hyeon & Hwang, arXiv:1705.04027](https://ar5iv.arxiv.org/html/1705.04027).
- [MOD] **Scope limits.**
  - Transient (non-stationary) processes can fall below the steady-state bound (Ritort 2004; Funo et al. 2016). Source: [Pietzonka et al.](https://ar5iv.arxiv.org/html/1702.07699).
  - The classical form can be violated in quantum settings (Ptaszyński 2018). Source: [Timpanaro](https://ar5iv.labs.arxiv.org/html/2407.10390).
  - As of 2020 there was no proof for underdamped dynamics, and periodically or time-dependently driven cases were unresolved. Source: [ESPCI seminar 2020](https://espci.psl.eu/fr/agenda/2020/gulliver-seminar-udo-seifert-university-of).
  - 2024: a family of TUR-like bounds was derived that holds for any fluctuation theorem, including quantum and feedback cases. Source: [Timpanaro, arXiv:2407.10390](https://ar5iv.labs.arxiv.org/html/2407.10390).
- [MOD] **Uses.**
  - A lower bound on the cost of temporal precision (clocks).
  - A model-free upper bound on motor efficiency from measurable observables.
  - Inference of entropy production from measured currents.
  - Source: [ESPCI 2020](https://espci.psl.eu/fr/agenda/2020/gulliver-seminar-udo-seifert-university-of).
- [unverified] **Thermodynamic speed limits.**
  - Shiraishi, Funo & Saito 2018 (*PRL* 121, 070601) bound transition times by entropy production and dynamical activity.
  - Yoshimura & Ito 2021 extended speed limits and TURs to deterministic chemical reaction networks.

**Proofreading, accuracy, sensing and clocks**
- [MOD] **Error floors.**
  - Without driving, the error rate for a wrong substrate with penalty Δ is about e^(−βΔ).
  - Dissipative cyclic resampling, a single proofreading stage, lowers it to about e^(−2βΔ).
  - Lower error costs more free energy and more cycles, and slows copying.
  - Source: [Brown & Sivak](https://arxiv.org/pdf/1909.09180).
  - Originals [unverified]: Hopfield 1974, *PNAS* 71, 4135; Ninio 1975, *Biochimie* 57, 587.
- [REC] **Measured error rates.** DNA replication 10⁻¹⁰–10⁻⁸; transcription 10⁻⁵–10⁻⁴; translation 10⁻⁴–10⁻³. Source: [Brown & Sivak](https://arxiv.org/pdf/1909.09180).
- [REC/MOD] **Speed versus specificity.** DNA copying and translation lie near a speed–specificity Pareto frontier. In vivo they appear to favour speed once a threshold specificity is reached. Source: [Brown & Sivak](https://arxiv.org/pdf/1909.09180).
- [MOD] **Sensing.** Barato, Hartich & Seifert 2014 (*New J. Phys.* 16, 103024) analysed the thermodynamic cost of information acquisition in bacterial sensing. Source: [Seifert 2015 notice](https://lehre4.rad.univie.ac.at/share/WWW_Exchange/SEKRETARIAT/Wpk%20PDF%20files/WS%202015/Seifert_WPK_7-Dec-2015.pdf).
- [unverified] **Clocks.** Cao, Wang, Ouyang & Tu 2015 (*Nat. Phys.* 11, 772) gave the free-energy cost of accurate biochemical oscillations, applied to the KaiABC clock. Follow-up work treats the minimal cost of coherent oscillation.

**Motor energetics (observings)**
- [OBS] **Single-molecule measurements.**
  - F1-ATPase (magnetic trap or electrorotation) indicates near-100% efficiency. Mechanical and chemical reversibility has been demonstrated in F1, the full ATP synthase, and an isolated kinesin stage.
  - Kinesin-1: 8 nm steps; stall about 4 pN at 2 mM ATP; about 800 nm/s (about 100 steps/s); about 100 steps per run; randomness parameter 0.3–1.5.
  - Myosin V: 36 nm steps; stall 1.6 pN; run about 1,400 nm. Myosin XI moves at up to 7 µm/s.
  - Added: most of kinesin's input free energy is dissipated.
  - Source: [Brown & Sivak](https://arxiv.org/pdf/1909.09180).

### Inferences
- Rearranged, the TUR turns the mean and variance of any measured current into a lower bound on dissipation. "How far from equilibrium" thus becomes partly measurable without a full model. The bound is one-sided: a low inferred value does not show the system is near equilibrium.
- Proofreading and the TUR share one logic. Performance beyond equilibrium limits, whether accuracy below e^(−βΔ) or precision tighter than a given ε, has a minimum dissipation price. Both are statements about driven cycles (broken detailed balance) in Markov models.
- Candidate class *proofreading scheme*: a discrimination network containing at least one fuel-driven cycle that resamples substrate after an energy-consuming step. The observing criterion is an error rate below the equilibrium discrimination limit at measured fuel consumption.

### Gaps
- Not verified:
  - any synthetic-chemistry TUR test;
  - thermodynamic speed-limit papers;
  - experimental cost-of-proofreading measurements, such as in vitro tRNA synthetase or ribosome energetics;
  - molecular-clock cost papers;
  - all 2023–2026 developments (no search budget remained).

---

## 4. Driven and fuelled chemistry: transient assembly, dissipative self-assembly, active matter, chemical engines and ratchets, motors, clocks and computing

### Takeaway
"Fuel-driven" covers three different schemes:
- The fuel templates a downhill assembly whose lifetime follows fuel depletion.
- The building blocks themselves process the fuel.
- The building blocks process the fuel *and* kinetic asymmetry holds concentrations away from equilibrium, storing energy.

Synthetic small-molecule motors have shown net directional rotation, measured by chiral chromatography and NMR at the ensemble level. They are powered by carbodiimide (2022), Pd redox (2016, non-autonomous), and enzyme-gated redox (2025). The field explains this as information-ratchet kinetics, not a power stroke.

### Cited Findings

**Vocabulary** (Ragazzon & Prins 2018, *Nat. Nanotechnol.* 13, 882–889, doi:10.1038/s41565-018-0250-8)
- Sources: [UniPD record](https://www.research.unipd.it/handle/11577/3286551); [author manuscript](https://www.research.unipd.it/bitstream/11577/3286551/1/manuscript.pdf); volume and pages confirmed in [ESOR 2019 abstract](https://esor.chem.pmf.unizg.hr/Abstracts/PL6.pdf).
- [DEF] **Dissipative self-assembly.** Assembly coupled to fuel-to-waste conversion that the building blocks themselves mediate.
- [DEF] **Self-assembly under dissipative conditions.** Fuel-to-waste conversion is done by a separate agent, such as an enzyme, without the monomers or aggregates taking part. All consumed energy is dissipated and none is stored.
- [DEF] **Driven self-assembly.** Dissipative self-assembly that stores energy in a high-energy aggregate because fuel consumption is kinetically asymmetric.
- [DEF] **Energy partition.** Consumed energy (from fuel to waste) splits into stored energy, which holds concentrations away from equilibrium, and dissipated energy.
- [MOD] **Ratcheting constant K_r.**
  - In an equilibrium cycle, the product of equilibrium constants around the cycle equals 1 (microscopic reversibility).
  - In a fuelled cycle, the activation and deactivation constants are replaced by ratios of rate constants for the fuel and waste pathways, so the product K_r need not equal 1.
  - K_r depends only on the asymmetry of transition states (kinetic asymmetry), which is the information-ratchet mechanism.
  - Stored free energy is ΔG = −RT ln K_r. In their simulation, K_r ≈ 1.6×10¹⁰ corresponds to about 58 kJ/mol at 298 K.
- [MOD] **Design rules.**
  - Activation should happen mainly at the monomer level and deactivation mainly at the aggregate.
  - Equilibrium exchange steps must be slower than catalytic fuel conversion, or re-equilibration erases the storage.
- [DEF] **Proposed evidence criteria.**
  - Catastrophic collapse events.
  - Comparison of dissipative with non-dissipative conditions, using inhibitors or non-hydrolysable analogues.
  - Direct measurement of concentrations under continuous fuelling.

**Observed fuelled assemblies**
- [OBS] **ATP-templated vesicles** (Maiti et al. 2016, *Nat. Chem.* 8, 725–731; citation from [ESOR 2019 abstract](https://esor.chem.pmf.unizg.hr/Abstracts/PL6.pdf)).
  - Observed: ATP templates surfactant vesicles below the surfactant's critical aggregation concentration (about 100 µM). Potato apyrase hydrolyses ATP to AMP and phosphate, and the vesicles disassemble over time. A bulk-hydrolysis model fits the kinetics.
  - Added (Ragazzon & Prins): this is self-assembly under dissipative conditions. No energy is stored; the fuel sets the lifetime.
  - Source: [manuscript](https://www.research.unipd.it/bitstream/11577/3286551/1/manuscript.pdf).
- [OBS] **Methylation-fuelled fibres** (Boekhoven et al. 2010, *Angew. Chem.*).
  - Observed: the dicarboxylate gelator DBC is methylated by methyl iodide to a diester that forms fibres. Slower ester hydrolysis returns DBC, so fibres accumulate transiently.
  - Added: an example of dissipative self-assembly.
  - Source: [manuscript](https://www.research.unipd.it/bitstream/11577/3286551/1/manuscript.pdf).
- [OBS] **"Transient assembly of active materials fuelled by a chemical reaction"** (Boekhoven et al. 2015, *Science*).
  - Ragazzon & Prins cite its catastrophic collapse events as indirect evidence for an information ratchet, by analogy with microtubules.
  - Source: [manuscript](https://www.research.unipd.it/bitstream/11577/3286551/1/manuscript.pdf).
  - That the fuel was the carbodiimide EDC, converting carboxylates to transient anhydrides, and the specific lifetimes, are [unverified].
- [REC] **Microtubules.**
  - GTP-tubulin assembles. GTP hydrolysis is accelerated inside the lattice, and a GTP cap prevents disassembly.
  - The GDP lattice is estimated to store about 21 kJ/mol.
  - Source: [manuscript](https://www.research.unipd.it/bitstream/11577/3286551/1/manuscript.pdf).
- [OBS, not opened] **Steady states under continuous fuelling.** Sorrenti, Hermans et al. 2017 is cited as an example of measuring nonequilibrium steady states in supramolecular polymerisation under continuous fuel. Source: [manuscript](https://www.research.unipd.it/bitstream/11577/3286551/1/manuscript.pdf).
- [REC] **Fuel classes in a 2024 review.**
  - Carbodiimide-fuelled anhydride assemblies (Tena-Solsona et al. 2017, 2018; Kariyawasam & Hartley 2017).
  - ATP-fuelled assemblies (Maiti 2016; Pezzato & Prins 2015).
  - Redox, enzymatic, light and pH fuels.
  - Assemblies include gels, vesicles, micelles and nanoparticle aggregates.
  - Source: [Wang, Yuan & Hao 2024, *ChemPhysMater* 3, 1–23, doi:10.1016/j.chphma.2023.06.002](https://journal.hep.com.cn/chphma/EN/10.1016/j.chphma.2023.06.002).

**Molecular motors, engines and ratchets**
- [MOD] **Ratchet classes.**
  - Chemically driven motors work as information ratchets: the chemical step is gated by the mechanical state.
  - Externally modulated systems (pH, redox potential, electric field) work as energy ratchets, where the power stroke matters.
  - Light-driven motors do depend on power strokes. The authors attribute this to a symmetry difference between optical transitions and the microscopic reversibility of thermal steps.
  - Leigh's group built a chemically driven information ratchet, and synthetic pumps have been run by external redox cycling.
  - Source: [Astumian, Mukherjee & Warshel 2016, *ChemPhysChem* 17, 1719, doi:10.1002/cphc.201600184](https://pmc.ncbi.nlm.nih.gov/articles/5518708).
- [DEF] **Definitions and efficiency at viscous load.**
  - Power stroke: energy input directly causes a conformational stroke.
  - Brownian ratchet: thermal motion is rectified by the energy input.
  - "Stokes efficiency" applies under viscous load.
  - Source: [Chowdhury resource letter, arXiv:0807.2731](https://arxiv.org/pdf/0807.2731).
- [OBS] **Pd-redox rotary motor** (Collins et al. 2016, Feringa group, *Nat. Chem.* 8, 860–866, doi:10.1038/nchem.2543).
  - Observed: an organopalladium biaryl rotor completes a 360° unidirectional rotary cycle about a single-bond axle. It passes through Pd(II)/Pd(0) states in 180° half-turns and is driven by two simple chemical fuels.
  - Added: coupling metal-centred redox to stepwise conformational change can power directional motion.
  - Source: [Nature Chemistry](https://www.nature.com/articles/nchem.2543). Whether fuel delivery was sequential rather than autonomous is [unverified].
- [OBS, not opened] **Earlier Leigh machines.** Leigh-group chemically fuelled machines from 2016 (Wilson et al., *Nature*) and 2017 (Erbas-Cakmak et al.) are cited in [Ragazzon & Prins](https://www.research.unipd.it/bitstream/11577/3286551/1/manuscript.pdf).
- [OBS] **Autonomous fuelled rotation about a covalent single bond** (Borsley, Kreidt, Leigh & Roberts 2022, *Nature* 604, 80–85, doi:10.1038/s41586-022-04450-5).
  - Observed, system: motor 1a is 1-phenylpyrrole-2,2′-dicarboxylic acid, a 26-atom molecule with phenyl and pyrrole rings joined by an N–C bond.
  - Observed, chemistry: with a carbodiimide fuel, intramolecular anhydride formation and anhydride hydrolysis run continuously, and the motor catalyses carbodiimide hydration.
  - Observed, numbers: more than 97% of fuel molecules are consumed through the motor's engine cycle. Directional bias reaches 71:29 with chirality-matched fuel and hydrolysis-promoting additive, and reversing the chirality reverses the direction. Source: [IDEAS/RePEc abstract](https://ideas.repec.org/a/nat/nature/v604y2022i7904d10.1038_s41586-022-04450-5.html).
  - Rate: roughly one turn per 3 hours, with a directional error every 3–4 turns. Source: [ChemistryViews](https://www.chemistryviews.org/?p=29327).
  - Methods: diacid enantiomeric enrichment was measured by chiral HPLC (ChiralPak IF). The anhydride intermediate was followed by ¹H NMR (CD₃CN:D₂O 7:3, 600 MHz, 298 K). An (S)- or (R)-configured hydrolysis catalyst was used. Of the variants, only 1a completed 360° on the fuelling timescale. Source: [Ragazzon-lab journal-club analysis](https://ragazzonlab.isis.unistra.fr/wp-content/uploads/2022/05/Journal-club-12_05_2022-Daniel-Couto.pdf).
  - Added: both chemical steps are kinetically gated, giving net direction. The journal club frames this as a "dynamic kinetic double resolution"; the field frames it as an information ratchet driven by kinetic asymmetry.
  - Rotation is reconstructed from ensemble stereochemical outcomes, not watched in single molecules.
- [OBS] **Redox-powered C–C bond rotation under enzyme control** (Berreur et al. 2025, *Nature* 644, 96–101, doi:10.1038/s41586-025-09291-6).
  - Observed, system: an achiral biphenyl triol (3a), with two hydroxymethyl groups on one ring and an ortho-F on the other.
  - Observed, fuels and enzymes: air O₂ and ammonia borane. Alcohol dehydrogenase ADH 291 performs the enantioselective oxidation, and NADP is recycled by YcnD.
  - Observed, conditions: 10 mM 3a, pH 7 phosphate, 10% DMSO, 40 °C, 48 h.
  - Observed, rates: oxidation 5.59×10⁻⁴ mM s⁻¹ (HPLC); r_red/r_enant = 0.50.
  - Observed, barrier: Mosher-ester rotation barrier about 79 kJ/mol (¹⁹F EXSY, 40 °C).
  - Observed, selectivity and cycling: oxidation enantioselectivity 85.7–89.5% ee (deuterated isotopomers, ¹H NMR). Deuterium from H₃N·BD₃ was incorporated, consistent with repeated redox cycling. Pulsed fuel kept the system active for at least 96 h.
  - [SIM] A simulated population averages about 2.35 full rotations per molecule in 48 h.
  - Added: enantioselective oxidation followed by non-selective reduction, with the kinetic hierarchy r_enant > r_red > r_ox, yields net directional rotation.
  - The authors acknowledge a high background fuel-to-waste reaction and a low rotation frequency. Direction is inferred from measured selectivity and rates.
  - Source: [PMC full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC12328200).
- [MOD] **Kinetic asymmetry and the Curtin–Hammett principle.**
  - Esposito, Kreidt, Leigh, Penocchio & Roberts relate kinetic asymmetry, power strokes and the Curtin–Hammett principle in catalysis-driven Brownian ratchets. Only the title and authors were seen. Source: [ORBilu record](https://orbilu.uni.lu/handle/10993/53685); journal and year [unverified].
  - The same record lists Amano et al. 2022, an information-thermodynamics analysis of a synthetic motor (not opened).

**Autonomous oscillators and clocks, chemical computing, active matter**
- [OBS/MOD] **BZ oscillator and Oregonator:** see section 1.
- [unverified] **Other clocks and oscillators.**
  - Clock reactions such as the iodine clock give a single delayed switch, not oscillation.
  - The KaiABC protein oscillator has been reconstituted in vitro (Nakajima et al. 2005).
  - An oscillating network of organic reactions has been run in a CSTR (Semenov et al. 2016, *Nature*).
- [unverified] **Chemical computing.** Logic in excitable BZ media; DNA strand-displacement circuits (Qian & Winfree 2011).
- **Active matter.**
  - [OBS] Broken detailed balance in flagella and cilia: see B5.
  - [REC] Microtubule dynamic instability: see above.
  - Broader active-matter literature was not gathered.

### Inferences
- Membership criteria for the fuelled classes, in chemistry's own terms:
  - *Fuel-templated transient assembly:* the assembly needs fuel present; an external agent destroys the fuel; there is no storage (K_r is irrelevant).
  - *Dissipative self-assembly:* the building blocks take part in fuel conversion, and activation and deactivation are chemically distinct.
  - *Driven self-assembly:* K_r ≠ 1, and stationary concentrations differ from equilibrium values.
  - *Catalysis-driven motor (information ratchet):* the motor catalyses fuel-to-waste conversion, rates depend on mechanical state, and a net directional cycle is sustained by fuel. Direction is set by the chirality or kinetics of the gating steps, not by state energies.
- All of these share a reaction cycle whose forward and reverse paths are chemically different (fuel to waste). That breaks the rule that the product of constants around a cycle equals 1. This is broken detailed balance at the level of chemical kinetics.
- In synthetic motors the observing is an ensemble stereochemical quantity (er, ee, intermediate ratios). Rotation counts and per-molecule direction are reconstructions or simulations.

### Gaps
- Not opened:
  - Boekhoven 2015 primary data (fuel concentrations, lifetimes);
  - Leigh-group papers from 2016–17 and after 2022 (pumps, further motors);
  - *Nature Reviews Chemistry* reviews on dissipative assembly;
  - Astumian's later kinetic-asymmetry papers.
- Chemical computing and flow reactors were not covered from verified sources.

---

## 5. Life and flow: far-from-equilibrium chemistry, dynamic kinetic stability, dissipative adaptation, homeostasis versus steady state, metabolic flux, flow processing

### Takeaway
That living matter runs far from equilibrium is observed directly: as net probability flux in the shape space of flagella and cilia, and as the energy budgets of ATP-driven motors. Theories that make dissipation the organising cause of life remain contested claims built on models and simulations. These include England's dissipative adaptation and Michaelian's dissipation theory of the origin of life. Pross's dynamic kinetic stability, homeostasis, metabolic flux and flow-reactor practice could not be verified in this session.

### Cited Findings
- [OBS] **Mesoscopic broken detailed balance in cells** (Battle et al. 2016). Details under B5.
- [OBS/REC] **Molecular-machine energy budgets** (F1 near-100% efficient; kinesin dissipates most of its input). Source: [Brown & Sivak](https://arxiv.org/pdf/1909.09180).
- [REC] **The microtubule GTP cycle as driven self-assembly.** Source: [Ragazzon & Prins manuscript](https://www.research.unipd.it/bitstream/11577/3286551/1/manuscript.pdf).
- [MOD] **Background texts.**
  - Schrödinger, *What is Life?* (first published 1944).
  - Prigogine & Nicolis 1971, *Q. Rev. Biophys.* 4, 107–148, on biological order, structure and instabilities.
  - Reference entries seen in [Marsh](https://arxiv.org/pdf/2204.00416).
- [MOD/SIM] **England's programme.**
  - England 2013 (*J. Chem. Phys.* 139, 121923): when growth exceeds decay, self-replication has a positive lower bound on entropy production, ln(g/δ). Source: [Marsh](https://arxiv.org/abs/2204.00416).
  - England 2015 (*Nat. Nanotechnol.* 10, 919–923, doi:10.1038/NNANO.2015.250): "dissipative adaptation in driven self-assembly". Sources: [Wikipedia: Dissipative system](https://en.wikipedia.org/wiki/Dissipative_system); [Marsh](https://arxiv.org/pdf/2204.00416).
  - Perunov, Marsland & England 2016 (*Phys. Rev. X* 6, 021036), "statistical physics of adaptation". Source: [Wikipedia: Jeremy England](https://en.wikipedia.org/wiki/Jeremy_England).
  - [SIM] Kachman, Owen & England 2017 (*PRL* 119, 038001), self-organised resonance during search of a diverse chemical space. Source: [Marsh](https://arxiv.org/pdf/2204.00416).
  - Horowitz & England 2017 (*PNAS*): [unverified].
  - Popular framing: driven matter tends to arrange itself to absorb and dissipate energy more reliably ("dissipation-driven adaptation"). Source: [Wikipedia: Jeremy England](https://en.wikipedia.org/wiki/Jeremy_England).
  - A 2014-era student magazine described it as controversial and untested on biological systems. Source: [Yale Scientific](https://www.yalescientific.org/?p=7140).
- [MOD] **Critiques compiled by Marsh.**
  - England's relation favours work-absorbing trajectories over their own time-reverses. It does not favour them over other forward routes from the same start; Marsh credits this point to an anonymous referee.
  - In the Kachman–Owen–England toy chemistry, outcome states absorbed work *less* well than their predecessors.
  - Some authors consider the generalised second-law formulation unnecessary, since standard entropy-flow bookkeeping already handles open systems.
  - Toy-model simulations are not real chemistry.
  - Marsh nonetheless judges the far-from-equilibrium case for the origin of life to be fairly strong.
  - Source: [Marsh, arXiv:2204.00416](https://arxiv.org/abs/2204.00416); journal and date not stated.
- [SIM] **Selection by stored energy, not dissipation.**
  - Following England and Astumian, Ragazzon & Prins argue that the selected state need not be the most stable one.
  - In their simulation, the cycle with higher K_r dominated even though its aggregate was thermodynamically less stable. Storage capacity (kinetic asymmetry), not dissipation alone, decided.
  - Source: [manuscript](https://www.research.unipd.it/bitstream/11577/3286551/1/manuscript.pdf).
- [MOD] **Michaelian.**
  - "Thermodynamic dissipation theory for the origin of life" (2011, *Earth Syst. Dynam.* 2, 37–51, doi:10.5194/esd-2-37-2011).
  - UVC abiogenesis of adenine (2021, *Entropy* 23, 217).
  - Marsh summarises the argument as follows: nucleic acids had a large entropy-producing potential under early-Earth UV.
  - Source: [Marsh](https://arxiv.org/pdf/2204.00416).
- [MOD] **Lineweaver.** Life may track transient local entropy-production maxima, and whether biogenesis is reproducible is unknown. Source: [Lineweaver](https://www.mso.anu.edu.au/~charley/papers/mepp.pdf).
- [unverified] **Pross's dynamic kinetic stability (DKS).**
  - Replicating populations persist through continual turnover and replication rather than through thermodynamic stability.
  - Pross proposes this as a kinetic selection principle linking chemistry to biology (Pross 2011–2012; Pascal, Pross & Sutherland 2013, *Open Biol.*).
  - Lincoln & Joyce 2009 (*Science* 323, 1229), on self-sustained replication of an RNA enzyme, is a reference entry seen in [Marsh](https://arxiv.org/pdf/2204.00416). Its use as DKS evidence is [unverified].
- [unverified] **Homeostasis versus steady state.**
  - A nonequilibrium steady state is any time-invariant state under through-flux.
  - Homeostasis adds regulated return toward set points after perturbation through feedback, which is a control criterion.
  - von Bertalanffy's "Fließgleichgewicht" named the open-system steady state.
- [unverified] **Metabolic flux.** Fluxes are measured by ¹³C isotope labelling and modelled by flux balance analysis. Flux, not concentration, is the primary nonequilibrium variable.
- [unverified] **Continuous processing.**
  - CSTRs and plug-flow or micro-flow reactors run reactions at steady state, with gains in heat and mass transfer and in safety.
  - Review: Plutschack et al. 2017, *Chem. Rev.*

### Inferences
- "Life is far from equilibrium" rests on observings at molecular scale (motor energetics) and mesoscopic scale (probability flux). "Life arises because dissipation is selected or maximised" is an explaining claim, supported so far by bounds and simulations, and contested.
- The NESS/homeostasis split matches the classification task:
  - *NESS* means stationarity under flux.
  - *Homeostasis* additionally needs a measured restoring response to perturbation.
  - The two have different membership tests: time-invariance versus perturbation–recovery.

### Gaps
- Not verified:
  - Pross;
  - homeostasis definitions;
  - metabolic flux methods;
  - flow-chemistry practice;
  - Horowitz & England 2017;
  - published replies by England to critics;
  - any 2023–2026 experimental test of dissipative adaptation.

---

## 6. Open disputes stated as binaries

### Takeaway
Disputes about observings are settled in particular systems:
- broken detailed balance in flagella and cilia;
- autonomous directional rotation in two synthetic motors;
- power-stroke-like substeps in myosin V and F1.

Disputes about explanations remain open, or are dissolving into scope and definition splits:
- whether an extremum principle selects steady states;
- whether dissipation selects structures;
- whether a power stroke sets motor direction.

The CRNT conjectures are mathematical. The GAC has a claimed general proof whose 2026 standing was not verified.

### Cited Findings

#### B1. Does minimum entropy production select the stationary state? (split by scope)
- **Scope note.** As usually argued, the claim spans two scopes, so it is split into B1a and B1b.
- **B1a: linear scope.**
  - *Claim:* in a system with linear flux–force laws, constant Onsager-symmetric coefficients and some forces fixed by time-invariant boundaries, the stationary state minimises total entropy production among states compatible with the fixed forces.
  - *Negation:* under those same conditions, some stationary state does not minimise it.
  - *Evidence, for:* a theorem, extended microscopically at zero magnetic field ([Phys. Rev. 1957](https://dx.doi.org/10.1103/PhysRev.105.360)).
  - *Evidence, against:* none inside the assumptions. Outside them:
    - Fourier, Fick and resistor counterexamples, plus a 1D simulation showing entropy production rising [MOD/SIM] ([Su et al.](https://arxiv.org/pdf/2202.08001));
    - conflict with balance equations ([Bertola & Cafaro 2008](https://www.research.ed.ac.uk/en/publications/a-critical-analysis-of-the-minimum-entropy-production-theorem-and/)).
  - *Why hard:* the theorem is valid, but its assumptions seldom hold exactly. For heat flow, conductivity would have to scale as 1/T². Debate mixes "the theorem is true" with "real systems obey it".
  - *Standing 2026:* settled as a conditional theorem. It is also settled that common transport laws fall outside its scope (prior, sources 1957–2022).
  - *What would settle the residue:* agreed rules for posing the fixed-force constraints in continuum problems.
  - *Proponents:* Prigogine and textbook treatments, against Bertola & Cafaro and Su, Hua & Guo.
  - *Type:* explaining (the scope of a model result).
- **B1b: chemical systems far from equilibrium.**
  - *Claim:* for reaction systems driven at affinities not small compared with RT, the realised stationary state minimises entropy production.
  - *Negation:* for such systems, the realised state is in general not a minimum of entropy production.
  - *Evidence:*
    - Chemical linearity holds only near equilibrium ([Wikipedia: Prigogine's theorem](https://en.wikipedia.org/wiki/Prigogine%27s_theorem)).
    - Extensions failed, some giving opposite results, and stability can be lost through Hopf bifurcations, as in the Brusselator ([Wikipedia: Dissipative system](https://en.wikipedia.org/wiki/Dissipative_system)).
    - [OBS] The BZ oscillation is not stationary at all ([Wikipedia: BZ](https://en.wikipedia.org/wiki/Belousov%E2%80%93Zhabotinsky_reaction)).
  - *Standing:* settled against a general principle. This is prior consensus, and no current defender was found.
  - *Type:* explaining.

#### B2. Does maximum entropy production select among nonequilibrium steady states?
- **Claim:** for a driven system with more than one dynamically accessible steady state under fixed external constraints, the realised state is the one of maximal entropy production compatible with those constraints.
- **Negation:** for some such systems under the same constraints, the realised state is not the one of maximal entropy production.
- **Scope note.** "MEP" names at least three principles: Ziegler (linear response), Paltridge (partial steady state) and Dewar (total steady state, MaxEnt) ([Bruers](https://ar5iv.arxiv.org/html/0705.3226)). Each needs its own binary; this one targets the general far-from-equilibrium version.
- **Evidence for:** [REC] climate models tuned to MEP reproduce heat transport (Paltridge; Lorenz), plus qualitative ecological examples ([Lineweaver](https://www.mso.anu.edu.au/~charley/papers/mepp.pdf)).
- **Evidence against:**
  - [SIM] Nicolis 1999: an atmospheric attractor that is neither a maximum nor a minimum.
  - [MOD] Attard 2012: convection fails to obey extremal principles. Both via [Wikipedia: Non-equilibrium thermodynamics](https://en.wikipedia.org/wiki/Non-equilibrium_thermodynamics).
  - Derivation errors and unrealistic assumptions ([Grinstein & Linsker 2007](https://zenodo.org/record/889780); [Paquette 2011](https://experts.mcmaster.ca/scholarly-works/1577788)).
  - The proponent's own retreat to inference-only status ([Dewar 2009](https://researchportalplus.anu.edu.au/en/publications/maximum-entropy-production-as-an-inference-algorithm-that-transla/)).
- **Why hard:**
  - Which entropy production counts (total or partial), and which constraints are fixed, can be chosen after the fact.
  - Multistable systems depend on history.
  - Entropy production is seldom measured independently of the model under test.
  - Climate "tests" use parametrised models.
- **Standing 2026:** open as a heuristic. Not established as a general physical principle (prior: sources 2003–2012, plus a 2024 preprint; 2023–2026 status [unverified]).
- **What would settle it:**
  - A prediction made in advance, with stated constraints, of which branch a controlled multistable chemical system adopts (for example a bistable CSTR), with entropy production on both branches measured from heat or affinities.
  - Or a theorem or counterexample for a defined class of Markov networks.
- **Proponents:**
  - For: Ziegler; Paltridge; Dewar (now framed as inference); Martyushev & Seleznev [unverified]; Lineweaver (restricted scope).
  - Against: Grinstein & Linsker; Paquette; Nicolis; Attard. Bruers clarifies the conceptual distinctions.
- **Type:** explaining (which principle accounts for the realised state), resting on an observing criterion (is the realised state's entropy production maximal?).

#### B3. Does dissipation drive self-organisation or only permit it? (split by meaning)
- **Scope note.** "Drive" is used to mean a necessary condition, a selecting cause, or a monotone trend. These readings have different observing criteria, so the dispute is split into B3a and B3b.
- **B3a: necessity (observing).**
  - *Claim:* in fuelled transient assemblies, the assembled state persists only while fuel-to-waste conversion continues, and decays after fuel is exhausted.
  - *Negation:* the assembled state persists unchanged after fuel is exhausted.
  - *Evidence:*
    - [OBS] ATP-templated vesicles disassemble as apyrase depletes ATP; DBC fibres vanish as the methyl ester hydrolyses ([Ragazzon & Prins](https://www.research.unipd.it/bitstream/11577/3286551/1/manuscript.pdf)).
    - [OBS] BZ waves cease once reagents are consumed ([Wikipedia: BZ](https://en.wikipedia.org/wiki/Belousov%E2%80%93Zhabotinsky_reaction)).
  - *Standing:* settled for these systems.
  - *Caution:* the result fits both "drive" and "permit", so it does not decide B3b.
  - *Type:* observing.
- **B3b: selection (explaining).**
  - *Claim:* under a given drive, which of several accessible structures is reached and maintained is predicted by the work absorbed and dissipated along its formation history. More-dissipating structures are favoured.
  - *Negation:* under the same drive, which structure is reached and maintained is predicted by kinetic accessibility and kinetic asymmetry (barrier heights, K_r). Dissipation magnitude does not predict it, and less-dissipating alternatives can dominate.
  - *Evidence for:*
    - [MOD] England 2013 and 2015 irreversibility bounds; Perunov et al. 2016.
    - [SIM] Kachman–Owen–England 2017, self-organised resonance in a toy chemical space.
    - [MOD] Michaelian on the origin of life.
    - Sources: [Marsh](https://arxiv.org/pdf/2204.00416); [Wikipedia: Jeremy England](https://en.wikipedia.org/wiki/Jeremy_England).
  - *Evidence against:*
    - The referee point that England's comparison is forward against reverse, not against alternatives. Outcome states in the 2017 toy model absorbed less work than their predecessors ([Marsh](https://arxiv.org/abs/2204.00416)).
    - [SIM] A higher-K_r cycle dominates despite a less stable aggregate ([Ragazzon & Prins](https://www.research.unipd.it/bitstream/11577/3286551/1/manuscript.pdf)).
    - [MOD] Kinetic asymmetry as the determinant of chemically driven outcomes ([Astumian 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4302201)).
  - *Why hard:*
    - Dissipation and kinetic asymmetry co-vary in most models and experiments.
    - Dissipation per pathway is rarely measured.
    - "Favoured" can be relative to the reverse path or relative to alternatives.
    - Most evidence comes from toy simulations.
  - *Standing 2026:* open (prior, sources 2013–2022; no verified decisive test since).
  - *What would settle it:*
    - A chemical system with two competing fuelled assembly pathways in which dissipation rate and gating asymmetry can be tuned independently, for example a catalyst that changes fuel turnover without changing gating.
    - Fuel consumption or heat per pathway, and the product distribution, would both be measured, with predictions registered in advance.
  - *Proponents:* England and co-authors, and Michaelian, for. Ragazzon & Prins, and Astumian, for the kinetic-asymmetry account. Marsh is a reviewer with mixed conclusions.
  - *Type:* explaining.

#### B4. Do molecular motors require a power stroke? (split into four binaries)
- **Scope note.** The camps use different membership criteria for "power stroke":
  - Astumian: the free-energy *difference* between pre- and post-stroke states of a chemically driven motor ([Astumian 2015](https://pmc.ncbi.nlm.nih.gov/articles/PMC4302201)).
  - Hwang & Karplus: a *large, nearly irreversible downhill change over a distance comparable to the step* ([Hwang & Karplus 2019](https://biomed-hwanglab.engr.tamu.edu/papers/2019/hwang_pnas19.pdf)).
  - The dispute also mixes an explaining question (what sets direction), an observing question (is there such a step) and a model-performance question (speed). Hence four binaries.
- **B4a: what sets direction (explaining; chemically driven, microscopically reversible kinetics).**
  - *Claim:* the directionality, stopping force and maximal efficiency of a chemically driven motor depend on the free-energy differences between its mechanical states (the power stroke).
  - *Negation:* they depend only on kinetic asymmetry, meaning the relative barrier heights of the chemical steps in different mechanical states, and not on state-energy differences.
  - *Negation side (Astumian):*
    - [MOD] The step ratio depends on q = exp[(ΔE_R − ΔE_L)/k_BT], built from activation energies. Stopping force is F_stop = k_BT ln(q⁻¹)/[l − (a_R − a_L)].
    - [REC] Fits to kinesin back-stepping data: Nishiyama et al., q⁻¹ = 221 with 2.9 nm; Carter & Cross, q⁻¹ = 802 with 3.7 nm.
    - Light-driven and externally modulated motors are exempted; there the power stroke does matter.
    - Sources: [Astumian 2015, *Biophys. J.* 108, 291, doi:10.1016/j.bpj.2014.11.3459](https://pmc.ncbi.nlm.nih.gov/articles/PMC4302201); [Astumian, Mukherjee & Warshel 2016](https://pmc.ncbi.nlm.nih.gov/articles/5518708).
    - Earlier: a chemically reversible Brownian-motor model fitted kinesin force–velocity, 1 ATP per 8 nm, and randomness data ([Astumian & Derényi 1999, *Biophys. J.* 77, 993](https://pmc.ncbi.nlm.nih.gov/articles/1300390)).
  - *Claim side (Hwang & Karplus):*
    - The argument "may be valid" only if free energy is released through elastic relaxation.
    - Treating position as the sole reaction coordinate cannot explain force generation.
    - Microscopic reversibility need not apply to coarse conformational states that integrate many atomic degrees of freedom.
    - [MOD/SIM] Storing about 10 k_BT elastically needs only about 1.3° of bending or 2.3% strain, comparable to thermal fluctuations, so pure elastic power strokes are unlikely. Steric push is favoured instead.
    - Source: [Hwang & Karplus 2019, *PNAS* 116, 19777, doi:10.1073/pnas.1818589116](https://biomed-hwanglab.engr.tamu.edu/papers/2019/hwang_pnas19.pdf).
  - *Why hard:*
    - Both sides fit the same coarse single-molecule data.
    - Their "power stroke" criteria differ.
    - Whether microscopic reversibility applies at the conformational level is itself disputed.
    - Kinetic prefactors that set speed do depend on the power stroke, which blurs the line between speed and direction.
  - *Standing 2026:* open but narrowing into a definitional split.
    - Reviews treat the mechanisms as non-exclusive and stage-dependent ([Brown & Sivak](https://arxiv.org/pdf/1909.09180); [Hwang & Karplus](https://biomed-hwanglab.engr.tamu.edu/papers/2019/hwang_pnas19.pdf)).
    - Synthetic motors (B4d) show kinetic gating is *sufficient* for direction in some chemical systems. They do not show power strokes are irrelevant in proteins.
    - Prior; 2023–2026 status [unverified].
  - *What would settle it:* vary the free-energy drop of one conformational transition (by mutation, strain or synthetic design) while holding the barrier asymmetry of the gating steps fixed, and measure stall force and step ratio. Paired synthetic motors differing only in one state energy would serve.
  - *Proponents:*
    - Negation side: Astumian with Derényi, Bier, Mukherjee and Warshel. Leigh, Esposito, Penocchio and co-workers frame catalysis-driven motors through kinetic asymmetry ([ORBilu](https://orbilu.uni.lu/handle/10993/53685)).
    - Claim side: Hwang & Karplus.
  - *Type:* explaining.
- **B4b: is there a power-stroke step in specific protein motors? (observing)**
  - *Claim:* myosin V and F1-ATPase each show a fast, large, downhill conformational step that produces displacement or rotation.
  - *Negation:* their displacement arises only from diffusive search rectified by binding, with no such step.
  - *Evidence (reviewed by Hwang & Karplus):*
    - [OBS] Myosin V: direct evidence of a power stroke, followed by a constrained diffusive search.
    - [OBS] F1: ATP binding (about 10 kcal/mol) drives an 80–90° substep. Single-molecule acceleration and deceleration phases are incompatible with rotational diffusion.
    - [OBS] Kinesin-1: imaging, DNA tethers and gold-nanoparticle tracking show the moving head rarely moves forward before stepping. Load-dependent stepping and the absence of free diffusion imply active force generation; a freely diffusing head would step too slowly under 2 pN load.
    - Source: [Hwang & Karplus](https://biomed-hwanglab.engr.tamu.edu/papers/2019/hwang_pnas19.pdf).
  - *Standing:* largely settled that these motors combine power-stroke-like substeps with diffusive search. This is compatible with Astumian, who does not deny such steps exist, only their role in setting direction.
  - *Type:* observing.
- **B4c: performance (model).**
  - *Claim:* within a transition-state / Hill-diagram continuum from pure power stroke to pure Brownian ratchet, power-stroke motors give higher speed, power and constant-velocity efficiency than ratchet motors under all modelled conditions.
  - *Negation:* within the same model class, some conditions give ratchet performance equal to or above power-stroke performance.
  - *Evidence:* [MOD] the claim holds within the model. The advantage is very large for simple motors and becomes inconsequential for complex motors with extra kinetic barriers ([Wagoner & Dill 2016, *J. Phys. Chem. B* 120, 6327, doi:10.1021/acs.jpcb.6b02776](https://researchconnect.stonybrook.edu/en/publications/molecular-motors-power-strokes-outperform-brownian-ratchets/)).
  - *Standing:* settled within the model; external validity open.
  - *Note:* these observables (speed, power) differ from B4a's (direction, stall force), so this is not a direct contradiction of Astumian.
  - *Type:* explaining (model).
- **B4d: autonomous directional rotation without a designed power stroke (observing, synthetic).**
  - *Claim:* a small molecule with no designed power stroke can undergo autonomous, chemically fuelled, net directional 360° rotation about a covalent single bond.
  - *Negation:* no such molecule shows net directional rotation under autonomous fuelling.
  - *Evidence:*
    - [OBS] Borsley et al. 2022: 71:29 bias, more than 97% of fuel through the motor cycle, chiral HPLC and NMR ([IDEAS](https://ideas.repec.org/a/nat/nature/v604y2022i7904d10.1038_s41586-022-04450-5.html); [journal club](https://ragazzonlab.isis.unistra.fr/wp-content/uploads/2022/05/Journal-club-12_05_2022-Daniel-Couto.pdf)).
    - [OBS] Berreur et al. 2025, an independent group using different chemistry (redox, enzyme, C–C bond). Its directionality is inferred from 85.7–89.5% ee oxidation selectivity and the rate hierarchy ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12328200)).
    - The earlier Pd-redox 360° motor was fuel-driven but probably not autonomous ([Collins et al. 2016](https://www.nature.com/articles/nchem.2543); autonomy [unverified]).
  - *Standing 2026:* settled in the affirmative at ensemble level for two independent systems (2022, 2025). The result was reproduced across chemistries rather than replicated in the same system.
  - *Type:* observing, with an interpretive overlay (information ratchet).

#### B5. Is detailed balance broken in a given system, and how is that measured?
- **Claim:** for system S in a stationary state, a chosen coarse-grained configuration variable shows statistically significant nonzero net probability flux (cyclic current), so detailed balance is broken. S here is an isolated *Chlamydomonas reinhardtii* flagellum, or a primary cilium of an epithelial cell.
- **Negation:** for the same S, variable and conditions, net flux is zero within statistical error.
- **Observings:**
  - [OBS] Battle, Broedersz, Fakhri, Geyer, Howard, Schmidt & MacKintosh 2016 (*Science* 352, 604–607, doi:10.1126/science.aac8167).
  - Observed: flagellar shapes were tracked by microscopy and decomposed into bending modes of a free flexible rod. A coarse-grained phase space was built from the first three modes, and probability distributions and flux were mapped; flux loops were found.
  - Primary cilia also showed broken detailed balance, in *non-periodic* fluctuations. The subject heading suggests MDCK kidney epithelial cells, which the press release confirms as kidney cells.
  - A stochastic model showed that broken detailed balance can be quantified without periodic motion.
  - Sources: [Duke record](https://scholars.duke.edu/publication/1427814); [Schmidt-lab page](https://schmidtlab.phy.duke.edu/research-2/active-matter-nonequilibrium/); [NWO press release](https://archief.nwo-i.nl/en/news/2016/04/29/researchers-find-that-the-equilibrium-of-living-cells-is-unsteady/).
  - Added: the system is active and nonequilibrium at the mesoscopic scale. Before this, whether such breaking could be seen at cell scale had been "hotly debated" (NWO).
- **Other measurement routes:**
  - TUR-based inference of a lower bound on entropy production from measured currents ([ESPCI 2020](https://espci.psl.eu/fr/agenda/2020/gulliver-seminar-udo-seifert-university-of)).
  - Violation of the fluctuation–dissipation theorem, comparing active and passive microrheology (Mizuno et al. 2007) [unverified].
- **Why hard:**
  - The inference is asymmetric. Detected flux proves nonequilibrium, but absent flux does not prove equilibrium, because coarse-graining or a poor choice of variables can hide currents [inference].
  - Long stationary records are needed for significance.
  - Flux-based entropy estimates are lower bounds [unverified as stated in a source here].
- **Standing 2026:** settled for the flagellum and primary cilia (2016). The method is general, and other systems are decided case by case. Later replications or extensions were not verified.
- **What would settle a given case:**
  - Long stationary trajectories in at least two variables, with flux significance tested by resampling.
  - A perturbation control, such as removing the fuel, in which flux vanishes [the controls Battle used are unverified].
- **Proponents:** the Battle et al. team. No opposing camp was found; the earlier debate concerned detectability, not principle.
- **Type:** observing.

#### B6. Does a fuelled assembly store energy (driven) or only last as long as its fuel (templated)?
- **Claim:** in system X under continuous fuelling, the stationary concentration of the assembly differs from its equilibrium value at the same composition, so energy is stored (driven self-assembly).
- **Negation:** under the same fuelling, the stationary concentration equals the equilibrium value for the momentary composition. The fuel sets only the lifetime (self-assembly under dissipative conditions).
- **Observings:**
  - [OBS] ATP-templated vesicles (Maiti 2016) are classified by Ragazzon & Prins as the Negation case.
  - [OBS] Catastrophic collapse in Boekhoven 2015 is read as indirect evidence for the Claim.
  - [REC] The microtubule lattice stores about 21 kJ/mol.
  - Source: [Ragazzon & Prins](https://www.research.unipd.it/bitstream/11577/3286551/1/manuscript.pdf).
- **Why hard:**
  - The equilibrium reference needs a non-dissipative control, such as a non-hydrolysable analogue or an inhibitor.
  - Batch experiments never reach stationarity.
  - Activated species are scarce and short-lived.
- **Standing 2026:** open, system by system. The framework has been clear since 2018. Status after 2018 is [unverified].
- **What would settle it:** continuous fuelling, by flow or by fuel regeneration, to a stationary state; quantification of every species; and comparison with an equilibrium control ([Ragazzon & Prins](https://www.research.unipd.it/bitstream/11577/3286551/1/manuscript.pdf)).
- **Proponents:** the framework is from Ragazzon & Prins. The experimental programmes are by Boekhoven, Hermans, van Esch, Prins and others ([Wang et al. 2024](https://journal.hep.com.cn/chphma/EN/10.1016/j.chphma.2023.06.002)).
- **Type:** observing, per system.

#### B7. The Global Attractor Conjecture (mathematical)
- **Claim:** every complex-balanced mass-action system has, in each positive compatibility class, a positive equilibrium that attracts all positive trajectories.
- **Negation:** some complex-balanced mass-action system has a positive trajectory that does not converge to its class's equilibrium.
- **Results:**
  - Proved for two-dimensional classes, three species, three-dimensional classes, and single linkage classes ([Pantea](https://ar5iv.arxiv.org/html/1103.0603); [CNP](https://ar5iv.arxiv.org/html/1010.3050)).
  - A general proof was claimed by Craciun in 2015 ([arXiv:1501.02860](https://arxiv.org/abs/1501.02860)).
  - Craciun's 2019 abstract still speaks of "an approach" ([arXiv:1901.02544](https://arxiv.org/abs/1901.02544)).
- **Why hard:** Horn–Jackson guarantees only local stability. The difficulty is excluding limit points on the boundary of the orthant, which is the persistence problem.
- **Standing 2026:** narrowing. A proof was claimed in 2015; its publication and acceptance are [unverified].
- **What would settle it:** peer-reviewed publication and independent verification of the 2015 proof, possibly formalised; or a counterexample.
- **Proponents:**
  - Horn formulated the conjecture.
  - Craciun claims the general proof.
  - Anderson, Shiu, Nazarov, Pantea, Siegel & Johnston, and Gopalkrishnan, Miller & Shiu supplied partial results.
- **Type:** neither observing nor explaining. It is a mathematical claim about a model construct, with chemical meaning: complex-balanced chemistry would always relax to one state per set of conserved totals.

#### B8. The Persistence Conjecture (mathematical)
- **Claim:** every weakly reversible mass-action system is persistent; no species is driven to zero from positive initial conditions.
- **Negation:** some weakly reversible mass-action system has a positive trajectory along which some species' liminf is zero.
- **Results:**
  - Proved for two species, and for two-dimensional classes with bounded trajectories ([CNP](https://ar5iv.arxiv.org/html/1010.3050); [Pantea](https://ar5iv.arxiv.org/html/1103.0603)).
  - Claimed for complex-balanced (toric) systems in Craciun 2015, Theorem C.
  - The Permanence Conjecture was open in 2018 ([Boros](https://arxiv.org/pdf/1710.04732)).
- **Standing 2026:** open in general (prior, as of 2019 sources; later status [unverified]).
- **What would settle it:** a proof or a counterexample.
- **Type:** mathematical.

#### B9. Does the TUR hold universally? (split by scope)
- **B9a.**
  - *Claim:* every time-integrated current in a nonequilibrium steady state of a continuous-time Markov jump process with time-independent rates satisfies Var(J)·σ / ⟨J⟩² ≥ 2k_B, with Var and the mean taken over the same time window.
  - *Negation:* some such system violates it.
  - *Standing:* settled (proved by Gingrich et al. 2016, per [Pietzonka et al.](https://ar5iv.arxiv.org/html/1702.07699)).
  - *Type:* a mathematical result about a model.
- **B9b.**
  - *Claim:* the same bound holds for every physical system, including underdamped, periodically driven, transient and quantum ones.
  - *Negation:* some such systems violate it.
  - *Evidence:* quantum violations ([Timpanaro](https://ar5iv.labs.arxiv.org/html/2407.10390)); transient processes can fall below the bound ([Pietzonka et al.](https://ar5iv.arxiv.org/html/1702.07699)); no underdamped proof as of 2020 ([ESPCI](https://espci.psl.eu/fr/agenda/2020/gulliver-seminar-udo-seifert-university-of)).
  - *Standing:* settled in the negative for the unrestricted version. Scope-specific generalisations continue (2024).
  - [REC] A colloidal test satisfied the finite-time version.
  - *Proponents:* Barato, Seifert, Pietzonka, Ritort and Gingrich (bounds), with Ptaszyński on the violations.
  - *Type:* model plus observing. Experiments check whether real systems meet the model's assumptions.

### Inferences
- Several disputes persist because one word carries different membership criteria:
  - "power stroke": an energy difference between states, or a large near-irreversible step;
  - "drive": a necessary condition, or a selecting cause;
  - "MEP": at least three principles.
- Stating the criterion splits each into a definitional question plus a narrower empirical or mathematical one, as done in B1, B3, B4 and B9.
- Positive and negative results carry different weight. A positive observing settles a case: flux detected, or a directional bias measured. A negative one does not: coarse-graining hides flux, and ensemble measurements can hide per-molecule direction.
- In chemistry's own terms, nearly every driven system here contains a cycle whose forward and reverse legs are chemically different, with the product of constants around the cycle ≠ 1 (K_r ≠ 1). That is how chemistry represents being "kept changing by a flow". It holds across fuelled assemblies, motors, proofreading and broken detailed balance (synthesis across sections 3–4).

### Gaps
- The 2023–2026 standing of B2, B3b, B4a, B6, B7 and B8 could not be verified, because search and fetch budgets were exhausted.
- Specific leads to check:
  - publication status of Craciun's GAC proof;
  - post-2022 Leigh, Boekhoven and Prins papers on kinetic asymmetry and energy storage;
  - experimental TUR or entropy-inference studies on synthetic chemical systems;
  - replies by England to critics;
  - Pross's DKS literature;
  - Martyushev's MEP reviews;
  - thermodynamic speed limits for chemical reaction networks (Yoshimura & Ito) [unverified];
  - the cost of biochemical oscillators (Cao et al. 2015) [unverified].
