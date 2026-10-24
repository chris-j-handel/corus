# Order and structure classifications in chemistry: phases, crystals, symmetry, topology, soft order, defects (status to 23 October 2026)

*Item labels: **[observing]** = a measurement as made; **[reconstruction]** = reconstruction from observings (refined structure, fitted parameter, assigned group, database flag); **[convention]** = convention or definition (including mathematically derived counts); **[model]** = model construct, theory or interpretation; **[simulation]** = computed result. **[unverified]** = background knowledge not checked against a source in this session. "Prior" marks a superseded state. The session's web-search allowance ran out before sources on polymers, colloids, reticular nets, defect notation and stereodescriptors could be fetched. Those items sit in the Gaps sub-sections, flagged [unverified].*

## Key gathered points

- **Crystal** [convention]: since 23 March 2021 the IUCr gives two criteria it holds to be equivalent. Direct space: the atoms, ions or molecules form, on average, a long-range ordered arrangement. Reciprocal space: the diffraction pattern is essentially sharp, with Bragg peaks indexable by n ≥ 3 integers (n = 3 for periodic crystals). The 1992 wording was explicitly interim, and the 2021 text is also called interim. Mathematicians note that pure-point limit-periodic structures fall outside the finite-n clause.
- **Counts** [convention]: 7 crystal systems spanning space-group types 1–230; 32 crystallographic point groups; 14 Bravais lattices; 1651 magnetic space-group types (230 + 230 + 674 + 517); 122 magnetic point groups; 775 / 3,338 / 12,584 superspace groups for (3+1)/(3+2)/(3+3) dimensions. Spin space groups number ">100,000" (2024) or 183,498 in another enumeration; the total depends on the equivalence and supercell cut-off chosen.
- **Databases** [reconstruction]: on 1 Jan 2026 the CSD held 1,431,347 refined structures (1,274,034 distinct compounds). Of these, 29.1% carry a modelled-disorder flag and 3.2% a polymorph flag; 51.3% are monoclinic, 26.2% triclinic and 0.7% cubic. ICSD: more than 318,000 entries (August 2025, secondary source), with more than 16,000 added each year and computed models included. AFLOW prototype library: 1,783 prototypes (2024).
- **Mesophases** [convention]: the IUPAC 2001 classes are N, N*, SmA/SmC, Col (h/r/ob), BPI–III and TGB. The ferroelectric nematic N_F was first seen in 2017 and identified as ferroelectric in 2020; about 150 materials showed it by 2024.
- **Water**: X-ray-laser scattering in 2020 showed coexisting high- and low-density liquid peaks. A 2026 *Science* paper reports a critical divergence near 210 ± 8 K, so the liquid–liquid critical point has moved from simulation-backed to experimentally claimed. No independent reproduction was found.
- **Glass** [convention, proposed]: Zanotto and Mauro (2017) define glass as a non-equilibrium, non-crystalline state that relaxes toward its supercooled liquid. IUPAC has not ratified this.
- **New phases from one signature plus a model**:
  - superionic ice XVIII: an fcc oxygen lattice seen by nanosecond XRD at 100–400 GPa; proton mobility is inferred;
  - molecular BEC of NaCs (2024): bimodal fits give up to 60% condensate; self-bound droplets followed in 2026, supersolidity not shown;
  - quasicrystal stability (2025): DFT says enthalpy-stabilized; simulation only.
- **Topology** [convention + observing]: knots are named by crossing number. The tightest is 8₁₉ (192-atom loop, 2017); a 16-crossing single-strand knot came from the Chi group; an 18-crossing topologically chiral [6]catenane was reported in 2025. Which structure holds the record depends on the category.
- **Contested edges**: glass as a phase; water's critical point; light-driven classical "space-time crystals" (2025); RuO₂ altermagnetism; the N_X vs SmZA assignment; what stabilizes quasicrystals.

## 1. States and phases, and how phase transitions are classified

### Takeaway
No ratified IUPAC list of "states of matter" turned up. Chemistry defines states and phases one at a time by an order criterion (positional, orientational, polar, magnetic, conformational, dynamical). It admits a new member when a signature observable is paired with a model that names the order. The main moves in 2023–2026 were:
- an experimental claim for water's liquid–liquid critical point (2026);
- the first molecular BEC (2024) and its self-bound droplets (2026);
- consolidation of the ferroelectric nematic family;
- a classical "space-time crystal" claim in a nematic (2025).

### Cited Findings

#### Intermediate (mesomorphic) order: IUPAC definitions
- **Mesomorphic state** [convention].
  - Criterion: order between a perfect 3D crystal and an isotropic liquid, gas or amorphous solid.
  - IUPAC files conformationally disordered (condis) crystals and plastic crystals here alongside liquid crystals, so "intermediate order" covers more than liquid crystals.
  - Sources: [IUPAC 2001, *Pure Appl. Chem.* 73, 845–895](https://stats.iupac.org/publications/pac/2001/pdf/7305x0845.pdf) (DOI 10.1351/pac200173050845 per the [IUPAC landing page](https://publications.iupac.org/pac/73/5/0845/index.html)); [IUPAC 2002, *Pure Appl. Chem.* 74, 493–509](https://stats.iupac.org/publications/pac/2002/pdf/7403x0493.pdf)
- **Liquid-crystal state** [convention]. Criterion: "long-range orientational order and either partial positional order or complete positional disorder." A **mesophase** is a phase existing over a definite range of temperature, pressure or concentration within the mesomorphic state. — [IUPAC 2001](https://stats.iupac.org/publications/pac/2001/pdf/7305x0845.pdf)
- **Mesophase classes** [convention] (source for all: [IUPAC 2001](https://stats.iupac.org/publications/pac/2001/pdf/7305x0845.pdf)):
  - nematic N: no long-range positional order of molecular centres; average alignment along a director **n**;
  - chiral nematic N*: the director rotates about one axis with pitch P; IUPAC prefers this name to "cholesteric";
  - smectic Sm: layers with a defined spacing. SmA has long axes roughly normal to the layers, SmC is tilted, SmC* is chiral;
  - columnar Col: discs stack into columns on a 2D lattice, with three lattice subtypes (Colh, Colr, Colob);
  - blue phases BPI and BPII: a 3D helical director with defects on a cubic lattice, with lattice constants near visible wavelengths; BPIII is amorphous. Blue phases occur between N* and the isotropic liquid in short-pitch materials;
  - twist-grain-boundary phases TGBA* and TGBC*: smectics held twisted by arrays of screw or edge dislocations.
  - Observed vs added: smectic layer spacing and the cubic blue-phase lattice are measurable periodicities [observing]. The director field, the helicoidal superstructure and the defect arrangements are [model] constructs inferred from optical textures and scattering.
  - IUPAC grouped its terms into five sections: general states, mesophase types, optical textures and defects, physical (electro- and magneto-optical) characteristics, and LC polymers. Class vocabulary is therefore tied to characterization methods. — [IUPAC landing page](https://publications.iupac.org/pac/73/5/0845/index.html)
- **Thermotropic vs lyotropic** [convention]. Thermotropic mesophases form when a solid is heated or an isotropic liquid is cooled. Lyotropic ones form when an amphiphilic mesogen is dissolved at a suitable concentration; their order is carried by micelles or aggregates rather than by single molecules. Mesogens are **calamitic** (rod or lath) or **discotic** (disc or sheet). — [IUPAC 2001](https://stats.iupac.org/publications/pac/2001/pdf/7305x0845.pdf)
- **Polymer liquid crystals** [convention]: main-chain (mesogenic units only in the backbone) vs side-chain (mesogenic units only in side groups). — [IUPAC 2002](https://stats.iupac.org/publications/pac/2002/pdf/7403x0493.pdf)

#### Ferroelectric nematic (N_F): a nematic subclass added 2017–2020
- **Origins.** [model, prior] Born proposed a polar fluid in 1916. [observing] In 2017 two independent groups found extra nematic phases in RM230, RM734 and DIO and first reported them as multiple nematic phases. — [Cruickshank 2024, *ChemPlusChem*, DOI 10.1002/cplu.202300726](https://rgu-repository.worktribe.com/OutputFile/2294153)
- **Chen et al. 2020** (*PNAS* 117, 14021–14031):
  - [observing] Planar cells of RM734 imaged by depolarized transmission microscopy showed domains of opposite polarization.
  - [observing] Applied fields reversed the polarization by domain-wall motion, with hysteresis.
  - [observing] Integrating the reversal current gave P ≈ 6 µC/cm² at low temperature, the largest the authors knew for a fluid. Polar Fréedericksz thresholds gave a consistent independent value.
  - [simulation] Atomistic MD (384 molecules, APPLE&P force field) showed head-to-tail polar correlations and a matching polarization.
  - [model] The authors judged the data inconsistent with the earlier "splay nematic" assignment, so that reading is superseded (2020).
  - Source: [Chen et al., DOI 10.1073/pnas.2002290117](https://par.nsf.gov/servlets/purl/10312373)
- **State of the family by 2024** [reconstruction] (sources: [Cruickshank 2024](https://rgu-repository.worktribe.com/OutputFile/2294153); [GDCh abstract](https://gdch.de/my/article/the-emergence-of-a-polar-nematic-phase-a-chemists-insight-into-the-ferroelectric-nematic-phase-cplu)):
  - About 150 compounds show N_F, mostly built on three archetypes (RM734, DIO, UUQU-4N). Design heuristics: short terminal chains and lateral fluorines.
  - Identification signature: D–E hysteresis, a strong dielectric relaxation mode and banded textures.
  - Related phases: N_X (also labelled SmZA; antiferroelectric domains; argued to be nematic rather than smectic), SmA_F, a second polar nematic N′_F, the chiral helielectric N_F* (micron pitch) and SmX_F.
  - Open questions: reported permittivity magnitudes are disputed; a large longitudinal dipole is necessary but not sufficient; no simple design rule exists.

#### Glass and gel
- **Glass** [convention, proposed 2017]. Zanotto and Mauro (*J. Non-Cryst. Solids* 471, 490; DOI 10.1016/j.jnoncrysol.2017.05.019) define glass as a non-equilibrium, non-crystalline condensed state that:
  - shows a glass transition;
  - has a structure like its parent supercooled liquid and relaxes spontaneously toward it;
  - would crystallize in the infinite-time limit.

  They give a lay version and an expert version. They reject "solid" and "isotropic" as defining features, since some glasses are anisotropic. Mauro calls glass neither truly solid nor truly liquid, describing it as a hybrid phase. — [Chemistry World](https://www.chemistryworld.com/news/glass-should-be-redefined-as-a-liquid/3008199.article); [ACerS](https://ceramics.org/ceramic-tech-today/new-definition-of-glass-describes-non-equilibrium-state-of-matter-ending-in-crystallization)
  - Observed vs added: the glass transition and slow relaxation are measured [observing]. "Ultimate fate is crystallization" is an infinite-time extrapolation [model].
  - Old church panes are not systematically thicker at the bottom [observing]. Viscosity estimates put room-temperature flow of window glass far beyond observable times, and the uneven thickness comes from manufacture [model]. — [RSC Education](https://edu.rsc.org/analysis/do-you-really-know-what-glass-is/3008331.article)
- **Gel** [convention]. The IUPAC 2007 recommendations (Alemán et al., *Pure Appl. Chem.* 79, 1801) define 150 terms for sols, gels, networks and inorganic–organic hybrids, grouped under precursors, gels, solids and processes. A **polymer gel** is a gel whose network component is a polymer. — [Gold Book source listing](https://mail.goldbook.iupac.org/sources/view/144); [polymer gel entry](https://old.goldbook.iupac.org/plain/PT07187-plain.html); [Kent record, DOI 10.1351/pac200779101801](https://kar.kent.ac.uk/2161/). The page range is 1801–1827 in the Kent record and 1801–1829 in an IUPAC listing.

#### Superionic phases
- **Ice XVIII** [observing + model]: Millot et al., *Nature* 2019, DOI 10.1038/s41586-019-1114-6. Sources: [Physics World](https://physicsworld.com/a/new-superionic-ice-phase-could-shed-more-light-on-icy-giant-cores/); [LLNL](https://www.llnl.gov/news/giant-lasers-crystallize-water-shockwaves-revealing-atomic-structure-superionic-ice).
  - Method: a ~30 µm water layer between diamond disks was shocked by six Omega laser beams to 100–400 GPa and roughly 2,000–3,000 K. Sixteen more beams struck an iron foil to make an X-ray flash for nanosecond diffraction.
  - Observed: Bragg peaks from a crystalline oxygen sublattice forming within about 3–5 ns. The lattice is fcc above ~250 GPa near 2,000 K and bcc at lower pressure (probably ice X). The measured compressibility agrees with prediction.
  - Not observed: the proton diffusion that defines "superionic". That rests on theory (predicted ionic conductivity above 100 S/cm) and on 2018 shock experiments (*Nat. Phys.*, DOI 10.1038/s41567-017-0017-4).
  - Membership criterion as practised: one sublattice is crystalline (seen by diffraction) and another is liquid-like (inferred from transport or simulation).

#### Quasicrystals as thermodynamic phases
- [simulation] Baek, Gavini, Sun et al., *Nature Physics*, 13 June 2025 (DOI 10.1038/s41567-025-02925-6, taken from the article link).
  - Method: DFT energies of nanoparticles cut from Sc–Zn and Yb–Cd quasicrystals at several sizes, extrapolated to bulk, using a GPU algorithm said to be up to 100× faster.
  - Conclusion: both are enthalpy-stabilized (low bond energy) rather than entropy-stabilized.
  - Limits: only two systems, and the bulk value is an extrapolation.
  - Source: [U-Michigan](https://news.engin.umich.edu/2025/06/first-quantum-mechanical-model-of-quasicrystals-reveals-why-they-exist/)

#### Bose–Einstein condensates of molecules
- **Bigagli et al., *Nature* 631, 289–293 (2024)**, DOI 10.1038/s41586-024-07492-z. Sources: [NSF PAR copy](https://par.nsf.gov/servlets/purl/10617790); [Physics Today](https://physicstoday.aip.org/news/a-bose-einstein-condensate-of-dipolar-molecules).
  - [observing] About 30,000 NaCs molecules, assembled from laser-cooled atoms, were evaporated from 700(50) nK to 6(2) nK. Microwave shielding cut two-body loss by about 200×, and a second field suppressed three-body loss. Absorption images were taken after 17 ms time-of-flight.
  - [reconstruction] Bimodal (Thomas–Fermi + Gaussian) fits give condensate fractions up to 60(10)%. Condensation begins near phase-space density 1 with more than 2,000 molecules. Nearly pure condensates hold about 200 molecules, with a lifetime of 1.8(1) s, and expand with an inverted aspect ratio.
  - [model] Peak density comes from a Thomas–Fermi formula that ignores dipolar terms; scattering lengths come from coupled-channel calculations.
- [simulation] Finite-temperature extended Gross–Pitaevskii modelling (2025) reproduces the coldest measured condensate fraction and the expanded density profile. — [arXiv 2502.08339 (DOI 10.1103/9sbg-6qqw)](https://arxiv.org/abs/2502.08339v1)
- [observing] **2026 follow-up** (Zhang et al., *Nature*, DOI 10.1038/s41586-026-10245-9): two-field microwave dressing tuned the dipolar interactions. Past a threshold the condensates shrank into self-bound droplets about 100× denser and formed droplet arrays. Supersolid behaviour is proposed, not shown. Press dates are 18 March and 1 April 2026. — [Columbia Quantum Initiative](https://quantum.columbia.edu/news/columbia-physicists-observe-ultracold-molecular-droplets); [Columbia Physics](https://www.physics.columbia.edu/news/groundbreaking-research-bose-einstein-condensates-organize-self-bound-droplets)

#### Polymorphism and polyamorphism
- [reconstruction] The CSD flags 45,729 entries (3.2%) as polymorphic structures on 1 Jan 2026 (prior: 43,022 on 1 Jan 2025). — [CSD 2026](https://www.ccdc.cam.ac.uk/media/CSD-Entries-Summary-Statistics-2026.pdf); [CSD 2025](https://www.ccdc.cam.ac.uk/media/CSD-Entries-Summary-Statistics-2025.pdf)
- **Water's two liquids: status by year**
  - **2018** [observing; contested; prior]. In water plus hydrazinium trifluoroacetate, cooling to about −80 °C released heat and gave a more viscous liquid that reverted on warming. Infrared spectra suggested more ordered hydrogen bonding in the low-density form. A. Soper objected that mixtures often show such transitions and that IR does not fix structure uniquely. — [Physics World 2018](https://physicsworld.com/a/evidence-mounts-for-liquid-liquid-transition-in-supercooled-water/)
  - **2020** [observing + reconstruction + model]. Kim et al. (*Science* 370, 978–982; DOI 10.1126/science.abb9385). Sources: [paper PDF](https://www.eng.uc.edu/~beaucag/Classes/AdvancedMaterialsThermodynamics/Homework/Homework%202024/Homework%201%202024/Experimental%20Evidence%20for%20LDA%20HDA%20transition%20science.abb9385.pdf); [DESY record](https://bib-pubdb1.desy.de/record/452657/export/hm?ln=en).
    - Method: high-density amorphous ice was heated isochorically with ~100 fs infrared pulses (about 115 K to 205 ± 10 K; estimated 2.5–3.5 kbar). Decompression was followed with <50 fs, 9.7 keV X-ray-laser pulses at delays of 8.4 ns to 1 ms.
    - Observed: a high-density-liquid peak at q ≈ 2.15 Å⁻¹ coexisting with a growing low-density-liquid peak at q ≈ 1.7 Å⁻¹ (two peaks, not one shifting peak). Small-angle fluctuations peaked at 50–100 ns, and ice formed more than an order of magnitude later.
    - Model: a first-order HDL→LDL transition, implying a critical point at positive pressure.
    - Caveats: temperatures come partly from ST2 simulations with a 25 K offset; the critical point was not located; the stated timescales are not fully consistent between abstract and text.
  - **2023** [observing]. Liquid–liquid phase separation was reached by ultrafast heating of low-density amorphous ice (*Nat. Commun.* 14, 442; DOI 10.1038/s41467-023-36091-1). — [Poole publication list](https://people.stfx.ca/ppoole/)
  - **2025** [simulation]. Simulations confine the transition's temperature–pressure window to an experimentally reachable range (*Nat. Phys.*, 3 Feb 2025; DOI 10.1038/s41567-024-02761-0). Separate simulations treat nanodroplets (*PRL* 134, 138001; DOI 10.1103/PhysRevLett.134.138001). — [U Crete note](https://www.physics.uoc.gr/node/4461); [Poole list](https://people.stfx.ca/ppoole/)
  - **June 2025** [model]. P. Poole called the transition "firmly established" in realistic simulations, with a critical point near 210 K and 100 MPa. He said experiment had not yet demonstrated it because ice forms too fast. — [Indico abstract](https://indico.global/event/442/contributions/124772)
  - **November 2025** [observing]. Experimental evidence was reported for a fragile-to-strong dynamic transition in bulk supercooled water near 233 K (*Nat. Phys.*, DOI 10.1038/s41567-025-03112-3). — [U Crete note](https://www.physics.uoc.gr/en/node/4867)
  - **2026** [observing + model]. You et al. (*Science* 391, 1387; DOI 10.1126/science.aec0018). Sources: [Météo-France record](https://bibliotheque.meteo.fr/pub/DOC00061486-experimental-evidence-liquid-liquid-critical-point.html); [Poole list](https://people.stfx.ca/ppoole/).
    - Method: both high- and low-density amorphous ice were heated with ultrafast infrared pulses, with pump fluence varied to land on either side of the predicted critical point. X-ray scattering probed the liquids before crystallization.
    - Observed: a crossover from discontinuous to continuous behaviour, broad slow structural change, a steep heat-capacity rise and enhanced density fluctuations, with a critical divergence at 210 ± 8 K.
    - Interpretation: a direct probe of the region near a liquid–liquid critical point.
    - Status: claimed; no independent reproduction found.

#### Phases ordered in time
- [model] Wilczek proposed time crystals in 2012; his ground-state version later proved impossible. — [Hiroshima U](https://www.hiroshima-u.ac.jp/node/93018)
- [observing, as reported] Discrete (Floquet) time crystals have been shown in nuclear spins, trapped ions, cold atoms and superconducting qubits. — [Quantum Insider](https://thequantuminsider.com/2025/09/10/time-crystals-break-out-of-the-quantum-lab/)
- [observing + model] **Zhao and Smalyukh**, "Space-time crystals from particle-like topological solitons", *Nature Materials* 2025 (DOI 10.1038/s41563-025-02344-1). Hiroshima U dates publication 4 Sept 2025; Physics World reported it in mid-September. Sources: [Physics World](https://physicsworld.com/a/space-time-crystal-emerges-in-a-liquid-crystal/); [Hiroshima U](https://www.hiroshima-u.ac.jp/node/93018); [Quantum Insider](https://thequantuminsider.com/2025/09/10/time-crystals-break-out-of-the-quantum-lab/).
  - Setup: a nematic between dye-coated glass plates under steady polarized blue light.
  - Observed: microscopy shows particle-like solitons (localized twists of the director) ordering periodically in space and time. Patterns persist for hours, with periods of milliseconds to seconds, in one spatial dimension plus time.
  - Model: a light–dye–liquid-crystal feedback loop. Simulations with spring-like coupling between solitons recover the order within a few cycles after a defect is introduced.
  - Caveat: the system is classical, continuously driven and dissipative.

#### Magnetic order classified by spin symmetry
- [convention + observing] Spin-group symmetry separates collinear magnets into ferromagnets, conventional antiferromagnets and altermagnets. Altermagnets have zero net moment but spin-split bands, and their opposite-spin sublattices are related by a rotation rather than by translation or inversion.
  - Observed: spin-split bands in MnTe and CrSb by photoemission, including room-temperature order, and XMCD-PEEM images of MnTe domains and domain walls.
  - Sources: [Jungwirth et al. 2025](https://arxiv.org/pdf/2411.00717); [Jungwirth et al. Sept 2025](https://arxiv.org/pdf/2506.22860)

### Inferences
- Membership criteria fall into three families:
  - (a) symmetry or order-parameter criteria: crystal, N vs Sm, ferro- vs altermagnet;
  - (b) dynamical criteria: glass relaxation, superionic sublattice mobility, condensation;
  - (c) equilibrium status: phase vs non-equilibrium state.

  Glass is hard to place because it fails the crystalline test under (a) and is defined mainly by (b) and (c).
- New phases enter the catalogue as one signature observable plus a model that names the order. Disputes concentrate on the model step. Examples:
  - Bragg peaks of an oxygen sublattice → "superionic";
  - a bimodal time-of-flight profile → "condensate";
  - a hysteretic switching current → "ferroelectric nematic";
  - two coexisting scattering peaks → "two liquids".
- Several classes are defined by paired states that interconvert reversibly: ±P domains in N_F, HDL ⇄ LDL, and the 2018 solution transition that reverted on warming. Reversibility is itself reported as an observable (hysteresis loops, reversal on reheating).
- IUPAC's own wording separates a "state" (a broad kind of order: mesomorphic) from a "phase" (a region bounded in T, p or concentration within it: mesophase). Zanotto and Mauro use "state" for glass, yet Mauro informally calls it a hybrid phase. The vocabulary is not used consistently.

### Gaps
- No IUPAC or IUPAP enumerated list of "states of matter" was found; textbook lists differ.
- [unverified] **Plasma:** an ionized gas with collective electromagnetic behaviour (Debye screening). Ionization is gradual, so plasma is not a phase in the sense of a sharp transition.
- [unverified] **Supercritical fluid:** above the critical temperature and pressure there is no liquid–gas coexistence. Whether a "Widom line" or "Frenkel line" divides liquid-like from gas-like regimes is debated.
- [unverified] **Ehrenfest (1933):** the order of a transition is the order of the lowest discontinuous derivative of the Gibbs energy. λ-transitions (diverging heat capacity) fit poorly. Modern usage keeps only first-order (latent heat, coexistence, metastability) vs continuous.
- [unverified] **Landau (1937):** an order parameter that is zero in the symmetric phase and nonzero below the transition. Transitions are classed by the symmetry broken, and group–subgroup relations constrain which transitions can be continuous.
- [unverified] **Universality classes:** critical exponents depend on dimensionality and order-parameter symmetry, not on chemistry. Examples: 3D Ising for the liquid–gas and binary-mixture critical points; XY for superfluid helium; Heisenberg for isotropic magnets.
- [unverified] **Kosterlitz–Thouless (1972–73):** a 2D transition by vortex–antivortex unbinding without conventional long-range order. Together with topological phases of matter it was cited in the 2016 Nobel Prize in Physics (Thouless, Haldane, Kosterlitz). The nobelprize.org page could not be fetched.
- [unverified] **Topological phases:** distinguished by topological invariants (e.g., Chern number, Z₂) rather than local order parameters. They are observed as quantized transport or protected surface states.
- [unverified] Superfluid ⁴He (1938); atomic BECs (1995; Nobel 2001).
- [unverified] **Plastic crystals** (e.g., C₆₀ above ~260 K, adamantane, SF₆) and **rotator phases** of n-alkanes: positional order with orientational disorder.
- [unverified] **Polytypism:** polymorphism by stacking sequence (SiC, ZnS; Ramsdell symbols 2H, 4H, 6H, 3C). The IUCr dictionary entry could not be fetched.
- [unverified] Ambient-pressure superionic conductors such as α-AgI (disordered Ag⁺ in a bcc I⁻ lattice).

## 2. Crystallographic classification and counts

### Takeaway
Crystallographic classes are mathematically derived conventions (230; 1651; 775 / 3,338 / 12,584; more than 10⁵ spin groups) applied to reconstructions from diffraction. The definition of "crystal" moved from periodicity to diffraction in 1992, gained a direct-space form again in 2021, and is still officially interim. Database counts as of 1 January 2026 are firm for the CSD (1,431,347) but only secondary for the ICSD (more than 318,000 in August 2025).

### Cited Findings

#### What counts as a crystal
- [convention] **IUCr Online Dictionary** (edited 23 March 2021). Source: [IUCr ODC: Crystal](https://dictionary.iucr.org/Crystal).
  - Direct-space criterion: a solid whose atoms, ions and/or molecules form, on average, a long-range ordered arrangement.
  - Reciprocal-space criterion: the solid has "essentially a sharp diffraction pattern". Most intensity lies in Bragg peaks, and diffuse scattering is always present. Peak positions are H = Σhᵢaᵢ* with n ≥ 3 integer indices; n = 3 gives conventional crystals.
  - The two criteria are stated to be theoretically equivalent.
- [convention; history] Source: [IUCr Newsletter 29(2)](https://www.iucr.org/news/newsletter/volume-29/number-2/change-to-the-definition-of-crystal-in-the-iucr-online-dictionary-of-crystallography).
  - **1992:** the definition was first published in the terms of reference of the Commission on Aperiodic Crystals (*Acta Cryst.* A48, 928; DOI 10.1107/S0108767392008328) and was always meant to be interim.
  - **2009:** the Commission on Aperiodic Crystals revised it.
  - **2021:** the IUCr Commission on Crystallographic Nomenclature added the direct-space text. C. P. Brock drafted it with M. Glazer, with changes suggested by M. Senechal. The vote closed 17 March 2021 with 39 votes (72% of those eligible), all in favour. The motive was teachability, and the new text is also called interim.
- [convention] **Aperiodic crystals.** Source: [IUCr ODC: Aperiodic crystal](https://dictionary.iucr.org/Aperiodic_crystal).
  - The 1992 text spoke of an "essentially discrete diffraction diagram". A crystal is aperiodic when 3D lattice periodicity is absent, or too weak to describe the atomic correlations.
  - Narrower usage: the sharp peaks form a Fourier module of finite rank larger than the space dimension.
  - Four overlapping classes: incommensurately modulated structures, incommensurate composite crystals, quasicrystals and incommensurate magnetic structures.
  - Amorphous solids are excluded because they lack sharp peaks.
- [model; mathematics] **Grimm 2015** (*Acta Cryst.* B71, 258–274; DOI 10.1107/S2052520615008409). Sources: [Grimm 2015](https://journals.iucr.org/b/issues/2015/03/00/dq5011); [arXiv text](https://ar5iv.arxiv.org/html/1506.05276).
  - "Order" has no agreed precise meaning and no satisfactory measure. Entropy is crude, because every deterministic structure scores zero.
  - Diffraction sees only two-point correlations. A diffraction measure splits into pure-point (Bragg), singular-continuous and absolutely-continuous parts. Finite samples always have an absolutely continuous part, so the split is strict only for idealised infinite systems.
  - The finite-n clause excludes limit-periodic structures such as period-doubling, which are pure point. The 1991 draft lacked this clause.
  - Quasicrystals are modelled as cut-and-project ("model") sets: decagonal, octagonal and dodecagonal ones from 4D lattices, icosahedral ones from 6D.
  - Thue–Morse diffraction is purely singular continuous. The deterministic Rudin–Shapiro sequence has the same flat diffraction as a random coin-toss chain. They are homometric, so diffraction cannot always tell order from randomness, and the inverse problem is non-unique.
  - The IUCr definition is a working one that will probably need revision.

#### Symmetry hierarchy and counts
- [convention] **Seven crystal systems** and their space-group number ranges: triclinic 1–2, monoclinic 3–15, orthorhombic 16–74, tetragonal 75–142, trigonal 143–167, hexagonal 168–194, cubic 195–230. That gives 230 space-group types. — [CSD crystal-system statistics 2026](https://www.ccdc.cam.ac.uk/media/CSD-Crystal-System-Statistics-2026.pdf)
- [convention] **Point groups, lattices and frieze groups** (source: [Wikipedia: Magnetic space group](https://en.wikipedia.org/wiki/Magnetic_space_group)):
  - 32 crystallographic point groups. With time reversal there are 122 magnetic point groups: 32 ordinary + 32 grey + 58 black-white.
  - 14 Bravais lattices. There are 50 magnetic Bravais lattices: 14 ordinary + 14 grey + 22 black-white.
  - 7 frieze groups, which become 24 with colour reversal.
- [convention] **1651 magnetic space-group types.** Sources: [MathWorld](https://mathworld.wolfram.com/MagneticSpaceGroup.html); [BYU ISO-MAG](https://iso.byu.edu/magneticspacegroupshelp.php).
  - 230 type I: no time reversal.
  - 230 type II: grey groups; every operation appears with and without time reversal; describe paramagnets.
  - 674 type III: time reversal attached to half the point operations.
  - 517 type IV: time reversal attached to half the translations.
  - Formally they are subgroups of E(3) × {1, 1′}, and each has a BNS number. BNS and OG symbols coincide for types I–III and differ for type IV.
  - History: Heesch introduced antisymmetry in 1929–30. Zamorzaev derived the 1651 groups in his 1953 thesis. The BNS (1957) and OG (1965) notations followed, and Shubnikov and Belov published *Colored Symmetry* in 1964. — [Wikipedia](https://en.wikipedia.org/wiki/Magnetic_space_group)
  - Later tabulations: Litvin (2001; *Acta Cryst.* A57, 729–730; DOI 10.1107/S0108767301006547) relisted all 1651 OG symbols because later changes to ITA coordinate triplets had caused misreadings. Litvin's *Magnetic Group Tables* (IUCr; dated 2013 or 2014 depending on source; DOI 10.1107/9780955360220001). A 2023 algorithm identifies the magnetic space group from a magnetic structure (DOI 10.1107/S2053273323005016). — [Penn State record](https://pure.psu.edu/en/publications/magnetic-space-group-types/); [MathWorld](https://mathworld.wolfram.com/MagneticSpaceGroup.html)
  - Type labels vary: a 2025 preprint splits the black-white groups into "3a" (674) and "3b" (517) instead of III and IV. — [Ma et al. 2025](https://web3.arxiv.org/pdf/2507.03842)
- [convention, 2024–2025] **Spin space groups** (spin rotations decoupled from spatial operations):
  - Chen et al. (*PRX* 14, 031038, 2024; DOI 10.1103/PhysRevX.14.031038) enumerated more than 100,000, starting from the 230 space groups and translation subgroups up to order 8. They argue that magnetic space groups miss effects such as altermagnetic splitting, and they released an identification program. — [DOAJ](https://doaj.org/article/3f7fd92d7cf44d12b042a16ce6b5b70a)
  - Jiang et al. (arXiv 2307.10371, September 2024 version) list 157,289 non-coplanar, 24,788 coplanar non-collinear and 1,421 collinear spin space groups (sum 183,498, my addition); 8,505 have no supercell. Spin point groups: 598 non-coplanar (Litvin 1977), 252 coplanar, 90 collinear. — [arXiv PDF](https://arxiv.org/pdf/2307.10371)
  - A 2025 preprint says only that "more than 10000" have been enumerated. — [Ma et al. 2025](https://web3.arxiv.org/pdf/2507.03842)
- [convention] **Collinear classes by spin symmetry:**
  - Spin Laue groups: 11 ferromagnetic, 11 antiferromagnetic and 10 altermagnetic (4 d-wave, 4 g-wave, 2 i-wave). — [Jungwirth et al. 2024](https://arxiv.org/pdf/2409.10034)
  - 122 collinear spin point groups (37 altermagnetic, 32 ferromagnetic, 53 antiferromagnetic) and 1,421 collinear spin space groups (422 / 230 / 769). — [Jungwirth et al. 2025](https://arxiv.org/pdf/2411.00717)
- [convention] **Superspace groups** for modulated crystals:
  - (3+1)D: 775 groups in 24 Bravais classes; (3+2)D: 3,338 in 83; (3+3)D: 12,584 in 215. — [BYU SSG](https://iso.byu.edu/ssghelp.php)
  - The 2011 tables (*Acta Cryst.* A67, 45–55; DOI 10.1107/S0108767310042297) corrected omissions and duplicates in earlier tables, which are therefore prior.
  - A 2013 algorithm (*Acta Cryst.* A69, 75–90; DOI 10.1107/S0108767312041657) decides whether two settings describe the same group.
  - Sources: [Bayreuth 2011](https://eref.uni-bayreuth.de/17441); [Bayreuth 2013](https://eref.uni-bayreuth.de/6716)

#### Structure types and prototypes
- [convention] **Strukturbericht designations** (e.g., A11 α-Ga, A14 I₂, A17 black P) stopped being minted early in the post-WWII period and do not scale to large databases. — [AFLOW Part 4](https://arxiv.org/pdf/2401.06875)
- [convention] **Pearson symbol** = lattice type + number of atoms in the conventional cell (e.g., oP12). AFLOW labels add stoichiometry, space-group number and Wyckoff letters (β-SeO₂ → A2B_oP12_26_abc_ab). — [AFLOW Part 4](https://arxiv.org/pdf/2401.06875)
- [reconstruction] **AFLOW Library of Crystallographic Prototypes:** grew from 298 to 1,100 to 1,783 prototypes (Part 4, February 2024; 683 added). Of these, 1,632 link to ICSD or CCDC entries and 151 are hypothetical, predicted or obsolete. — [AFLOW Part 4](https://arxiv.org/pdf/2401.06875)

#### Structure databases (2025–2026)
- **CSD summary** [reconstruction], release of 1 Jan 2026 (source: [CSD 2026 summary](https://www.ccdc.cam.ac.uk/media/CSD-Entries-Summary-Statistics-2026.pdf)):

  | Measure | Count (share) |
  |---|---|
  | Entries | 1,431,347 |
  | Distinct compounds | 1,274,034 |
  | Organic | 655,284 (45.8%) |
  | Transition metal present | 653,119 (45.6%) |
  | Main-group metal present | 151,224 (10.6%) |
  | 3D coordinates present | 94.5% |
  | Neutron studies | 2,732 (0.2%) |
  | Powder studies | 10,408 (0.7%) |
  | Non-room-temperature | 57.1% |
  | Absolute configuration determined | 58,768 (4.1%) |
  | Disorder present | 417,195 (29.1%) |
  | Polymorphic | 45,729 (3.2%) |
  | R < 0.05 / R < 0.03 | 55.7% / 12.6% |

  Prior (1 Jan 2025): 1,362,809 entries. — [CSD 2025](https://www.ccdc.cam.ac.uk/media/CSD-Entries-Summary-Statistics-2025.pdf)
- **CSD by crystal system** (1,428,579 entries with a defined space group): triclinic 26.2%, monoclinic 51.3%, orthorhombic 16.9%, tetragonal 2.2%, trigonal 2.0%, hexagonal 0.6%, cubic 0.7%. — [CSD 2026 crystal systems](https://www.ccdc.cam.ac.uk/media/CSD-Crystal-System-Statistics-2026.pdf)
- **CSD growth by publication year:** 64,116 (2020), 60,934 (2021), 60,952 (2022), 60,892 (2023), 61,927 (2024), 58,600 (2025, incomplete); 4,045 for 1923–1964 combined. — [CSD 2026 by year](https://www.ccdc.cam.ac.uk/media/CSD-Publication-Year-Statistics-2026.pdf)
- **CSD history and scope:** begun in 1965 by Olga Kennard; the one-millionth entry was added on 8 June 2019; scope is compounds that generally contain C and H (organic, metal-organic, organometallic). — [Wikipedia: CSD](https://en.wikipedia.org/wiki/Cambridge_Structural_Database). The CCDC statistics landing page still said "over 1.25 million" when fetched, which is stale. — [CCDC stats](https://ccdc.cam.ac.uk/CCDCStats/)
- **ICSD** [reconstruction]:
  - Founded 1978 (Bergerhoff and Brown); now produced by FIZ Karlsruhe with NIST. It aims to hold all inorganic structures published since 1913, including elements, minerals, metals and intermetallics. It held over 318,000 entries as of August 2025, a figure flagged "citation needed". — [Wikipedia: ICSD](https://en.wikipedia.org/wiki/Inorganic_Crystal_Structure_Database)
  - FIZ (February 2025): more than 16,000 new entries a year; theoretically calculated structure models are included; mineral names were standardized. — [FIZ release](https://www.fiz-karlsruhe.de/sites/default/files/FIZ/Dokumente/FIZnews/FIZnews-ICSD-Manual-202502-en.pdf)
  - Prior: the NIST edition listed 212,673 entries (last updated October 2019). — [NIST ICSD](https://icsd.nist.gov/history.html)
- [reconstruction, 2026] **Quality of early ICSD entries.** Gross and Reeves-McLaren (*Acta Cryst.* B82, 462–470; DOI 10.1107/S2052520626007079) examined 697 ICSD records from 1929 or earlier. None has an R factor. NaCl-type (Fm-3m) makes up 43.8% of pre-1925 entries. A global instability index above 0.20 v.u. occurs in 21.5% of pre-1925 and 42.6% of 1925–29 entries. — [paper PDF](https://journals.iucr.org/b/issues/2026/05/00/yh5050/yh5050.pdf)

### Inferences
- The well-known counts are counts of equivalence classes ("types"), and they depend on the equivalence chosen. In the 2024–25 spin-group literature, totals differ by an order of magnitude with the supercell cut-off and convention. Two groups also report different collinear spin point group counts (90 vs 122).
- The classes are occupied very unevenly: in the CSD, triclinic plus monoclinic make up 77.5% and hexagonal plus cubic only 1.3%. That skew is an observation about how molecules pack, not a property of the classes.
- The CSD flags expose the layers of a structure determination:
  - observed intensities, which become
  - refined coordinates (94.5% of entries have 3D coordinates),
  - disorder models (29.1%),
  - quality metrics (R factor),
  - and finally classifications (space group, polymorph flag).
- Net CSD growth from January 2025 to January 2026 (68,538 entries) exceeds the roughly 60,000 structures published per year, which suggests older literature is being back-filled. This is an inference.
- If the ICSD had about 318,000 entries in August 2025 and grows by more than 16,000 a year, a late-2026 total of roughly 335,000 would follow. This is an extrapolation, not a reported number.

### Gaps
- [unverified] 6 crystal families and 7 lattice systems (the hexagonal family splits into trigonal and hexagonal systems; rhombohedral lattice); 17 plane groups; 80 layer groups; 75 rod groups; 219 affine space-group types (the 230 count 11 enantiomorphic pairs separately); 65 Sohncke groups; 4,783 space-group types in 4D (4,894 counting enantiomorphs); 528 magnetic layer groups. The IUCr dictionary page on crystal families could not be fetched.
- [unverified] **Close packing:** hcp (ABAB…) and ccp/fcc (ABCABC…), packing fraction ≈ 0.74; polytypes are alternative stacking sequences.
- [unverified] **Frank–Kasper (tetrahedrally close-packed) phases:** only tetrahedral interstices, with coordination polyhedra CN12, 14, 15 and 16. Families include A15 (Cr₃Si), σ, μ and the Laves phases C14 (MgZn₂), C15 (MgCu₂) and C36 (MgNi₂); the Laves phases form the most populous intermetallic family. Frank–Kasper phases also occur in soft matter (block copolymers, dendrimers, micelles).
- [unverified] **Zintl phases:** electropositive metals donate electrons to an electronegative main-group polyanion, which then obeys valence (octet) rules (the Zintl–Klemm concept). Examples: NaTl, CaSi₂, K₄Ge₉ clusters.
- Not found: an official ICSD entry count for 2026; the number of ICSD structure types; the size of the CSD MOF subset.

## 3. Molecular symmetry

### Takeaway
This session checked the crystallographic, magnetic and spin point-group counts, the CSD statistic on absolute configuration, and how molecular chirality carries into liquid-crystal classes. The standard material on molecular point groups, character tables, g/u labels and selection rules appears in Gaps as [unverified] background.

### Cited Findings
- [convention] The 32 crystallographic point groups are the finite groups compatible with 3D lattice translations. Magnetic point groups (122) add time reversal. Spin point groups add independent spin rotations: 598 / 252 / 90 in one count, 122 collinear in another. — [Wikipedia](https://en.wikipedia.org/wiki/Magnetic_space_group); [Jiang et al.](https://arxiv.org/pdf/2307.10371); [Jungwirth et al. 2025](https://arxiv.org/pdf/2411.00717)
- [convention] Symmetries that 3D lattices forbid (5-, 8-, 10- and 12-fold axes; icosahedral) are realized in quasicrystals by projection from 4D or 6D lattices. — [Grimm 2015](https://journals.iucr.org/b/issues/2015/03/00/dq5011)
- [model] A 2025 preprint proposes "multicolor groups" that extend colour (time-reversal-type) symmetry to molecules and solids. — [Ma et al. 2025](https://web3.arxiv.org/pdf/2507.03842)
- [reconstruction] In the CSD, absolute configuration is determined for 58,768 entries (4.1%) as of January 2026. — [CSD 2026](https://www.ccdc.cam.ac.uk/media/CSD-Entries-Summary-Statistics-2026.pdf)
- [convention] Molecular chirality carries into phase classification: N*, SmC*, N_F*, TGB* and the blue phases are the chiral counterparts of achiral mesophases. — [IUPAC 2001](https://stats.iupac.org/publications/pac/2001/pdf/7305x0845.pdf); [Cruickshank 2024](https://rgu-repository.worktribe.com/OutputFile/2294153)
- [convention] Altermagnet classes are distinguished by which real-space operation relates the opposite-spin sublattices: a proper or improper rotation, never inversion. — [Jungwirth et al. 2024](https://arxiv.org/pdf/2409.10034)

### Inferences
- Molecular point groups form an unbounded set, since any n-fold axis is allowed; the lattice caps crystallographic point groups at 32. Quasicrystals escape the cap by moving to a higher-dimensional lattice.
- Assigning a symmetry class always refers to an idealized model geometry, not to an instantaneous structure.
- Absolute configuration (which mirror form is present) is observed far less often than relative structure: only 4.1% of CSD entries.

### Gaps
- [unverified] **Point-group families:** C₁, Cₛ, Cᵢ, Cₙ, Cₙᵥ, Cₙₕ, Dₙ, Dₙₕ, Dₙd, S₂ₙ, T, T_d, T_h, O, O_h, I, I_h, C∞ᵥ, D∞ₕ. Schoenflies symbols are used for molecules and Hermann–Mauguin symbols for crystals.
- [unverified] **Character tables** list irreducible representations. Mulliken labels:
  - A and B: symmetric and antisymmetric to the principal rotation;
  - E and T: two- and three-fold degenerate;
  - subscripts 1/2 and primes refine these;
  - g/u (gerade/ungerade): even/odd under inversion, occurring only in centrosymmetric groups.
- [unverified] **Chirality criterion:** a molecule is chiral if and only if it has no improper rotation Sₙ (including σ = S₁ and i = S₂). The chiral point groups are C₁, Cₙ, Dₙ, T, O and I. The IUPAC Gold Book entry could not be fetched.
- [unverified] **Selection rules:**
  - IR-active fundamentals transform like x, y or z; Raman-active ones like quadratic forms;
  - centrosymmetric molecules obey mutual exclusion;
  - the Laporte rule allows electric-dipole transitions only g ↔ u;
  - a molecule has 3N−6 vibrational modes (3N−5 if linear).

  Observed: band positions, intensities and depolarization ratios. Added by models: assignments and normal coordinates.
- [unverified] Crystal-site symmetry (Wyckoff positions), Z′ > 1 and pseudo-symmetry. Sohncke groups host enantiopure crystals, and the Flack parameter from anomalous scattering is the observable behind absolute configuration.

## 4. Stereochemistry and molecular topology

### Takeaway
Molecular topology borrows mathematics' knot tables (Alexander–Briggs crossing number). Stereodescriptors (CIP) and chirality subclasses are separate conventions and were not checked this session. Synthesized knots are a tiny sample of the mathematical set. Record claims depend on the category:
- tightest knot: 8₁₉ (2017);
- most crossings in a single-stranded knot: 16 (Chi group);
- most crossings in a multi-ring catenane: 18 (2025).

### Cited Findings
- [convention] **Definitions.** A molecular knot is a self-entangled macrocycle whose essential (non-nugatory) crossings cannot be removed without breaking the covalent backbone. "Link" is the mathematical name for a catenane. A rotaxane is topologically trivial but held together mechanically. — [Ashbridge et al. 2022, *Chem. Soc. Rev.*](https://pubs.rsc.org/en/content/articlehtml/2022/cs/d2cs00323f) (DOI 10.1039/D2CS00323F inferred from the URL)
- [convention] **Notation.** Alexander–Briggs labels give the crossing number with an index (3₁ trefoil, 4₁ figure-eight). Links add the number of components as a superscript: 2²₁ Hopf, 4²₁ Solomon, 6³₂ Borromean, 6²₁ Star of David. The backbone crossing ratio (BCR, backbone atoms per crossing) measures tightness. — [Ashbridge et al.](https://pubs.rsc.org/en/content/articlehtml/2022/cs/d2cs00323f)
- [observing + reconstruction] **Selected synthesized knots and links** (source: [Ashbridge et al.](https://pubs.rsc.org/en/content/articlehtml/2022/cs/d2cs00323f)):
  - prime knots: 3₁ (Sauvage 1989; later Hunter 2001, Vögtle, and an all-benzene trefoil by Itami 2019); 4₁ (Sanders 2014); 5₁ pentafoil (2012, imine-linked Fe(II)); 5₂ (Leigh, *Nature* 2020); 7₄ (Leigh, *Nat. Chem.* 2021); 8₁₉ (Leigh 2017, plus a cage-derived 8₁₉ from the Nitschke group);
  - composite knots: 3₁#3₁ granny and square knots; 3₁#3₁#3₁ (9 crossings); a 12-crossing triskelion (Leigh, *Science* 2022);
  - links: Solomon link (Sauvage 1994); imine-based Borromean rings; a Star of David catenane made by metathesis;
  - metalla-knots: Ag(I) (Hosseini 2008); Rh/Ir (Jin group); Ru 8₁₈ (Chi group, 2018); Ag 7₁ and 8₂₁ (Fujita group);
  - 6₁ (stevedore) was still an untargeted goal in 2022;
  - BCR values: 8₁₉ = 24; 3₁ = 25–32; 4₁ = 28; 5₂ = 29; 7₄ = 37; triskelion = 32.
- [observing] **8₁₉ knot** (Danon et al., *Science* 355, 159–162, 2017; DOI 10.1126/science.aal1619): a 192-atom loop about 20 nm long, braided around Fe ions with a central chloride; structure by X-ray. It holds a Guinness record as the tightest knot. — [Manchester](https://www.manchester.ac.uk/about/news/manchester-scientists-tie-the-tightest-knot-ever-achieved/); [Technology Networks](https://www.technologynetworks.com/tn/news/scientists-produce-molecular-knot-with-eight-crossings-279486); [Chemistry World](https://chemistryworld.com/news/chemists-tie-molecular-knot-with-record-number-of-crossings-/3009015.article)
- [observing + model] **7₄ "endless" knot** (*Nat. Chem.* 13, 117–122, online 14 December 2020; DOI 10.1038/s41557-020-00594-x). Source: [Springer](https://link.springer.com/article/10.1038/s41557-020-00594-x).
  - A 258-atom loop was closed by alkene metathesis on a Zn(II)/Fe(II) 3×3 grid templated by BF₄⁻.
  - The grid was solved by X-ray (CCDC 2022144); the end groups of the closed loop were modelled with the MMFF force field on that geometry.
  - Ring closure gave three products together: an unknot, a Solomon link and the 7₄ knot.
- [observing] **16-crossing single-stranded knot** from K.-W. Chi's group (Ulsan). Eight arene and eight bent ligands self-assemble by coordination, characterized by X-ray and NMR. It is reported as the highest crossing count for a single-stranded molecular knot, and the article frames it as only the fifth knot type made. The fetched page does not give the journal (Wiley) or the date. — [Chemistry World](https://chemistryworld.com/news/chemists-tie-molecular-knot-with-record-number-of-crossings-/3009015.article)
- [observing, 2025] **18-crossing [6]catenane** (18⁶₁): a topologically chiral catenane with four topologically chiral stereogenic units, made by stereoselective self-assembly. Cui Zheng and Jin Guoxin, *Angew. Chem. Int. Ed.* 2025, Outside Front Cover; DOI 10.1002/anie.202515400 per the article link. — [Henan Normal U](https://www.htu.edu.cn/english/2025/1111/c21799a361240/page.htm)
- [convention + observing] **Topological chirality.** The over/under sense of each crossing is a stereochemical element, so most knots are chiral. This shows up as Cotton effects stronger than those of unknotted isomers, weakening for looser knots (BCR above about 30). — [Ashbridge et al.](https://pubs.rsc.org/en/content/articlehtml/2022/cs/d2cs00323f)
- [observing → reconstruction] **How topology is established** (source: [Ashbridge et al.](https://pubs.rsc.org/en/content/articlehtml/2022/cs/d2cs00323f)):
  - X-ray crystallography, which once corrected a catenane assignment to a trefoil;
  - NMR: DOSY diffusion changes and diastereotopic splitting;
  - ion-mobility MS drift times;
  - tandem-MS fragmentation energy (tighter knots fragment more easily);
  - CD spectroscopy;
  - HPLC and GPC separation of topological isomers.
- [convention] Scale: mathematics knows billions of prime knots, and chemists have made only a few. — [Leigh lecture, 2022](https://ias.tau.ac.il/node/3497)
- [planned] A 2019–2022 DFG fellowship aimed at a 12-crossing trefoil-of-trefoils by Vernier templating with lanthanides; the page reports no result. — [DFG GEPRIS](https://gepris.dfg.de/gepris/projekt/428837130)

### Inferences
- Topological classes have exact membership criteria (knot invariants), but assigning a class to a molecule is a reconstruction. A crystal structure is mapped onto a knot diagram; for the 7₄ knot, a precursor's crystal structure plus force-field ring closure stood in for that.
- Three record categories run in parallel: tightness (BCR), crossings in a single strand, and crossings in a multi-component link. A claim of the "most complex knot" needs its category stated. No 2023–2026 report of a single-stranded knot with more than 16 crossings appeared in the fetched sources.
- Topological chirality is a third layer of chirality beside the geometric (point-group) kind. It survives any continuous deformation, so conformational change cannot remove it.

### Gaps
- [unverified] **CIP sequence rules** (Cahn–Ingold–Prelog 1956/1966; Prelog–Helmchen 1982; IUPAC 2013 recommendations P-9) assign R/S, E/Z, P/M, Rₐ/Sₐ, Rₚ/Sₚ and Δ/Λ; pseudoasymmetric centres take r/s.
- [unverified] **Chirality classes:**
  - central (a stereocentre);
  - axial (biaryls, allenes);
  - planar (paracyclophanes, ferrocenes);
  - helical (helicenes);
  - inherent (curvature in an otherwise achiral structure, e.g., calixarenes, fullerenes).
- [unverified] **Atropisomers:** stereoisomers from hindered rotation about a single bond. Ōki's working criterion is isolability with a half-life of at least 1000 s at a stated temperature (about 93 kJ/mol at 300 K). Medicinal chemists use classes 1–3 by half-life at 37 °C. The Gold Book entry could not be fetched.
- [unverified] **Meso compounds:** achiral members of a stereoisomer set that have stereocentres and an internal improper symmetry element.
- [unverified] **Mechanical stereochemistry:** mechanically planar chiral rotaxanes and catenanes (Goldup and others); topological chirality as distinct from Euclidean chirality.
- Not found: a 2023–2026 review with updated knot records; the primary journal and year of the 16-crossing knot.

## 5. Assembled and soft order

### Takeaway
IUPAC supplies definitions for gels (150 terms, 2007) and for lyotropic and polymer liquid crystals (2001–2002). The search allowance ran out before sources could be fetched for:
- colloids and supramolecular classes;
- polymer architecture, tacticity, copolymer classes and sequence-defined polymers;
- RCSR nets and MOF/COF counts.

Those catalogues are listed in Gaps as [unverified] background.

### Cited Findings
- [convention] **Gel and network terminology:** 150 IUPAC terms (2007) covering precursors, gels, solids and processes for sols, gels, networks and inorganic–organic hybrids. A polymer gel is defined by its polymer network component. — [Gold Book source](https://mail.goldbook.iupac.org/sources/view/144); [Kent record](https://kar.kent.ac.uk/2161/); [polymer gel](https://old.goldbook.iupac.org/plain/PT07187-plain.html)
- [convention] **Lyotropic mesophases** are assembled order: the ordering units are micelles or amphiphile aggregates, not single molecules. — [IUPAC 2001](https://stats.iupac.org/publications/pac/2001/pdf/7305x0845.pdf)
- [convention] **Polymer liquid crystals** are classified by where the mesogens sit: main chain or side chain. — [IUPAC 2002](https://stats.iupac.org/publications/pac/2002/pdf/7403x0493.pdf)
- [observing + model] **Self-assembly and templating** produce topologically complex assemblies:
  - metal ions plus anions (BF₄⁻, Cl⁻) act as templates (7₄, 8₁₉);
  - 16 components assemble into the 16-crossing knot;
  - the [6]catenane forms by stereoselective self-assembly.

  Sources: [Springer 7₄](https://link.springer.com/article/10.1038/s41557-020-00594-x); [Chemistry World](https://chemistryworld.com/news/chemists-tie-molecular-knot-with-record-number-of-crossings-/3009015.article); [Henan Normal U](https://www.htu.edu.cn/english/2025/1111/c21799a361240/page.htm)
- [observing + simulation] Topological solitons in a nematic behave as particle-like units that organize into lattices in space and time under light. — [Physics World](https://physicsworld.com/a/space-time-crystal-emerges-in-a-liquid-crystal/)
- [reconstruction] 45.6% of CSD entries contain a transition metal. That set includes coordination polymers and MOFs; the size of the MOF subset was not found. — [CSD 2026](https://www.ccdc.cam.ac.uk/media/CSD-Entries-Summary-Statistics-2026.pdf)

### Inferences
- In soft and assembled matter the unit that carries the order is often not a molecule: it may be a micelle, a mesogenic segment, a soliton or a metal–ligand vertex. A membership criterion therefore has to name the unit as well as the kind of order.

### Gaps
- [unverified] **Colloids:** IUPAC's "colloidal" means dispersed units with at least one dimension of roughly 1 nm–1 µm. Classes:
  - by phases: sol, emulsion, foam, aerosol, solid foam, suspension;
  - by affinity: lyophilic vs lyophobic;
  - association colloids (micelles).

  Gels, xerogels and aerogels are networks, the last two dried.
- [unverified] **Supramolecular classes:** host–guest systems (crown ethers, cryptands, cyclodextrins, calixarenes, cucurbiturils, cages); self-assembled metallo-cages; mechanically interlocked molecules; supramolecular polymers. Related Nobel Prizes: 1987 (Cram, Lehn, Pedersen) and 2016 (Sauvage, Stoddart, Feringa).
- [unverified] **Polymer architecture:** linear; branched (short or long chain; star, comb, brush); hyperbranched; dendrimer (perfectly branched, numbered by generation); cyclic; network (crosslinked thermosets and elastomers).
- [unverified] **Tacticity:** isotactic, syndiotactic, atactic. The observable behind the class is the ¹³C NMR dyad/triad/pentad fractions (mm, mr, rr).
- [unverified] **Copolymer classes** (IUPAC source-based nomenclature connectives): statistical (-stat-), random (-ran-), alternating (-alt-), periodic (-per-), block (-block-), graft (-graft-), plus gradient (tapered) copolymers. Block copolymers adopt morphologies such as spheres, cylinders, gyroid and lamellae, and Frank–Kasper σ or A15 phases.
- [unverified] **Sequence-defined polymers:** monomer order is specified unit by unit (solid-phase or iterative synthesis) and read by tandem MS. "Sequence-controlled" is the broader class (Lutz et al., *Science* 2013).
- [unverified] **Reticular chemistry:**
  - the RCSR gives nets lower-case three-letter symbols (dia, pcu, sql, hcb, srs, nbo, fcu, pts, tbo, …) and lists a few thousand nets;
  - more than 100,000 MOFs in the CSD MOF subset; COFs in the low thousands;
  - the 2025 Nobel Prize in Chemistry went to Kitagawa, Robson and Yaghi for MOFs (the press release could not be fetched this session).

## 6. Defects and disorder

### Takeaway
Disorder enters chemistry's classifications at three levels:
- the definition of a crystal, where diffuse scattering is always present;
- refinement practice, where 29.1% of CSD entries carry modelled disorder;
- phase definitions in which defects are constitutive: TGB, blue phases, domain-structured ferroics.

The standard defect taxonomy, Kröger–Vink notation, correlated disorder and high-entropy phases were not checked this session.

### Cited Findings
- [convention] The crystal definition builds in imperfection: diffuse scattering always accompanies the Bragg peaks, and order is judged by where most of the intensity lies. — [IUCr ODC](https://dictionary.iucr.org/Crystal)
- [model; mathematics] Diffraction is a two-point statistic. Its split into Bragg, singular-continuous and diffuse parts is exact only for infinite idealizations. Deterministic and random structures can be homometric (Rudin–Shapiro vs a coin-toss chain), so "disorder" cannot always be read off a pattern. — [Grimm 2015](https://journals.iucr.org/b/issues/2015/03/00/dq5011)
- [reconstruction] Modelled disorder is common: 417,195 CSD entries (29.1%) carry a disorder flag (prior: 390,109 in January 2025), and 57.1% of determinations were made away from room temperature. — [CSD 2026](https://www.ccdc.cam.ac.uk/media/CSD-Entries-Summary-Statistics-2026.pdf); [CSD 2025](https://www.ccdc.cam.ac.uk/media/CSD-Entries-Summary-Statistics-2025.pdf)
- [convention] Defects can define a phase: TGB phases are smectics held twisted by arrays of screw or edge dislocations, and blue phases have defect lines arranged on a cubic lattice. — [IUPAC 2001](https://stats.iupac.org/publications/pac/2001/pdf/7305x0845.pdf)
- [observing] Domain walls act as functional defects: N_F polarization reverses by domain-wall motion, and MnTe altermagnetic domains and walls have been imaged by XMCD-PEEM. — [Chen et al.](https://par.nsf.gov/servlets/purl/10312373); [Jungwirth et al. Sept 2025](https://arxiv.org/pdf/2506.22860)
- [observing + simulation] Topological solitons (localized director twists) behave as particle-like defects; simulated lattices of them heal within a few cycles after a defect is inserted. — [Quantum Insider](https://thequantuminsider.com/2025/09/10/time-crystals-break-out-of-the-quantum-lab/)
- [reconstruction, 2026] Historic database models can carry undetected strain. Early ICSD structures have no R factors, many have high global instability indices, and 29.3% of the early set carries bond-valence parameter coverage flags. — [Gross and Reeves-McLaren 2026](https://journals.iucr.org/b/issues/2026/05/00/yh5050/yh5050.pdf)

### Inferences
- "Disorder" has three working meanings that need not coincide:
  - a physical deviation from an ideal lattice;
  - a refinement choice (split sites, partial occupancies) that the CSD flags;
  - a mathematical class of diffraction measure.

### Gaps
- [unverified] **Defect classes by dimension:**
  - 0D point defects: vacancy, interstitial, substitutional or antisite; Schottky and Frenkel pairs; colour centres;
  - 1D line defects: edge, screw and mixed dislocations, characterized by the Burgers vector;
  - 2D planar defects: grain and twin boundaries, stacking faults, antiphase boundaries, surfaces;
  - 3D volume defects: voids, precipitates.
- [unverified] **Kröger–Vink notation (1956):** M_S^C is species M on site S with charge C relative to the perfect lattice (• positive, ′ negative, × neutral); for example V_O^•• is an oxygen vacancy. It is used to write defect reactions balanced in mass, sites and charge.
- [unverified] **Correlated disorder:** deviations with short-range correlations that give structured diffuse scattering (Keen and Goodwin, *Nature* 2015). Examples: ice rules, spin ice, vacancy networks in Prussian blue analogues, relaxor ferroelectrics. It is analysed by 3D-ΔPDF and reverse Monte Carlo (both models).
- [unverified] **High-entropy phases:** high-entropy alloys (Cantor; Yeh, 2004) with five or more principal elements on one lattice; entropy-stabilized oxides (Rost et al., *Nat. Commun.* 2015, (MgCoNiCuZn)O). It is debated whether configurational entropy actually stabilizes most "high-entropy" materials.
- Not found: a current IUPAC defect-terminology document.

## 7. Where classifications of order are contested

### Takeaway
The live disputes of 2023–2026 are mostly about the model step that turns an observation into a class:
- whether water's second liquid ends in a critical point (claimed experimentally in 2026);
- whether glass is a state or a phase;
- whether driven classical patterns count as time crystals;
- what stabilizes quasicrystals;
- whether particular materials (RuO₂, N_X compounds) belong to newly defined classes.

The definition of "crystal" itself is officially interim.

### Cited Findings
- **What is a crystal** [convention; open]. The 1992 definition was interim, revised in 2009, extended in 2021, and the 2021 text is still described as interim. Grimm argues the finite-n clause wrongly excludes pure-point limit-periodic order and calls the definition a working one. — [IUCr Newsletter](https://www.iucr.org/news/newsletter/volume-29/number-2/change-to-the-definition-of-crystal-in-the-iucr-online-dictionary-of-crystallography); [Grimm 2015](https://journals.iucr.org/b/issues/2015/03/00/dq5011)
- **Glass: solid, liquid, state or phase** [convention; open]. The 2017 Zanotto–Mauro definition treats glass as a non-equilibrium state destined to crystallize, while their commentary also calls it a hybrid phase. No organized rebuttal appeared in the fetched sources. The medieval-window "flow" argument is a myth (prior popular belief). — [Chemistry World](https://www.chemistryworld.com/news/glass-should-be-redefined-as-a-liquid/3008199.article); [ACerS](https://ceramics.org/ceramic-tech-today/new-definition-of-glass-describes-non-equilibrium-state-of-matter-ending-in-crystallization); [RSC Education](https://edu.rsc.org/analysis/do-you-really-know-what-glass-is/3008331.article)
- **Liquid–liquid transition and critical point in water** [observing + model; advanced 2020; claimed 2026]. Status ran from contested mixture evidence (2018), through XFEL two-peak coexistence (2020) and simulation constraints (2025), to the critical-divergence claim at 210 ± 8 K (2026). A separate fragile-to-strong transition at about 233 K (November 2025) bears on the dynamics. Open: independent reproduction, and whether ultrafast-heated amorphous ice samples equilibrated liquid. — see Section 1 sources: [Kim 2020](https://bib-pubdb1.desy.de/record/452657/export/hm?ln=en); [You 2026](https://bibliotheque.meteo.fr/pub/DOC00061486-experimental-evidence-liquid-liquid-critical-point.html); [Poole 2025](https://indico.global/event/442/contributions/124772)
- **Time crystals in chemical and soft systems** [definitional; open]. The 2025 nematic "space-time crystal" is classical, continuously light-driven and dissipative. Wilczek's original equilibrium version was later shown to be impossible. Admitting the nematic case requires the broader non-equilibrium sense used for driven discrete time crystals. — [Hiroshima U](https://www.hiroshima-u.ac.jp/node/93018); [Physics World](https://physicsworld.com/a/space-time-crystal-emerges-in-a-liquid-crystal/)
- **What stabilizes quasicrystals** [simulation vs an entropy-stabilization view]. The 2025 DFT result (enthalpy-stabilized) covers two alloys and rests on extrapolation; experimental thermodynamic confirmation was not found. — [U-Michigan](https://news.engin.umich.edu/2025/06/first-quantum-mechanical-model-of-quasicrystals-reveals-why-they-exist/)
- **Assignments within the ferroelectric nematic family** [model; open]. Whether N_X is a nematic or a smectic (SmZA) is debated, permittivity magnitudes are disputed, and some phase assignments have been revised. — [Cruickshank 2024](https://rgu-repository.worktribe.com/OutputFile/2294153)
- **Altermagnetism in RuO₂** [contested]. The experimental signatures of magnetic order are called "a matter of debate", possibly because order is fragile with respect to stoichiometry or strain. MnTe and CrSb are treated as established. — [Jungwirth et al. Sept 2025](https://arxiv.org/pdf/2506.22860)
- **How many spin groups** [convention; unsettled]. Reported figures: ">100,000" (*PRX* 2024), 183,498 (summed from Jiang et al.), and "more than 10000" (2025 preprint). Collinear spin point groups are counted as 90 or 122. — [DOAJ](https://doaj.org/article/3f7fd92d7cf44d12b042a16ce6b5b70a); [Jiang et al.](https://arxiv.org/pdf/2307.10371); [Ma et al.](https://web3.arxiv.org/pdf/2507.03842); [Jungwirth et al. 2025](https://arxiv.org/pdf/2411.00717)
- **Superionic ice** [observing + model]. The crystalline half (fcc oxygen) is observed; the liquid-like proton half is inferred. — [Physics World](https://physicsworld.com/a/new-superionic-ice-phase-could-shed-more-light-on-icy-giant-cores/)
- **Molecular droplets and supersolids** [open]. Droplet arrays were observed in 2026, but supersolidity (a superfluid with crystal order) is not yet shown. — [Columbia Quantum Initiative](https://quantum.columbia.edu/news/columbia-physicists-observe-ultracold-molecular-droplets)
- **Knot records** [convention]. "Tightest" (8₁₉), "most crossings in a single strand" (16) and "most crossings in a link" (18, a [6]catenane) are different categories. — [Chemistry World](https://chemistryworld.com/news/chemists-tie-molecular-knot-with-record-number-of-crossings-/3009015.article); [Henan Normal U](https://www.htu.edu.cn/english/2025/1111/c21799a361240/page.htm)
- **Earlier reinterpretations** [prior]. The "splay nematic" assignment for RM734 gave way to the ferroelectric nematic (2020). The earlier superspace-group tables were superseded by the 2011 corrected enumeration. — [Chen et al.](https://par.nsf.gov/servlets/purl/10312373); [Bayreuth 2011](https://eref.uni-bayreuth.de/17441)

### Inferences
- Most contested items share a structure: the observation is accepted (two scattering peaks; a periodic soliton pattern; spin-split bands in some samples; slow relaxation of glass), and the dispute is over which class it licenses. The disagreement sits in the model or definition step, not in the measurement.
- Definitions written as "interim" or "working" (crystal 1992/2021; glass 2017) are common at the edges, where newly observed systems (aperiodic crystals, polar fluids, driven patterns) test the old membership criteria.

### Gaps
- [unverified; historically notable, rejected] **Polywater** (1960s): a claimed polymeric phase of water, rejected around 1973 as contamination by silica, salts and organics.
- [unverified; historically notable, rejected] **Pauling's multiple-twinning explanation** of icosahedral diffraction (1985 onward), abandoned after high-resolution imaging and the discovery of stable quasicrystals.
- [unverified] Other claimed liquid–liquid transitions: phosphorus (Katayama et al., *Nature* 2000); the contested "glacial phase" of triphenyl phosphite.
- [unverified] The Kauzmann paradox and the hypothetical ideal glass transition (thermodynamic) vs purely kinetic accounts of the glass transition.
- [unverified] Earlier NMR-based "time crystal" claims in molecular solids (2017–2018) and the view that classical oscillating reactions (e.g., Belousov–Zhabotinsky) are not time crystals in the strict sense.
- Not found: any IUPAC position on whether glass, plasma or supercritical fluid count as "phases"; independent replication of the 2026 water critical-point claim; any 2026 retraction in these areas.
