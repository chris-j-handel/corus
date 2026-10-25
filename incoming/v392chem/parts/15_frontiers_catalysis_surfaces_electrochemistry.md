# Frontiers of catalysis, surface chemistry and electrochemistry: frontier binaries (gathered to 23 October 2026)

*Provenance. Tool limits shaped this file. The shared web-search budget ran out at this researcher's first query. Publisher and DOI hosts (nature.com, doi.org, science.org, pubs.acs.org, Wiley) were not on the fetch allowlist, PubMed Central returned a browser check, and the hourly fetch cap was then reached. Sources actually read in this session are marked "seen" and given with their URL. Everything else comes from the researcher's prior knowledge and is marked [unverified]. DOIs given inside an [unverified] mark were typed from memory and must be checked before use. The 2024–2026 standings are the weakest part of the file. Item labels: [observing] = what an instrument recorded; [reconstruction] = a structure or quantity fitted from observings; [convention] = a definition or counting rule; [model] = a theoretical construct or mechanism; [simulation] = computed (DFT, MD, microkinetics). Anomalous underscreening belongs to the water-and-interfaces notes and is only cross-referenced here (B11).*

## Key gathered points

- **Coverage.** 25 frontier binaries (B1–B25) in six areas, plus one-line further candidates. Ranked most consequential and cleanest first: B21 dark oxygen (observing; contested) · B12 aqueous electrochemical N2→NH3 (observing; largely settled against the claims at reported rates) · B8 cations required for CO2 electroreduction (observing; narrowing to yes) · B16–B17 photosystem II O–O formation (narrowing after 2023) · B13–B15 nitrogenase (open) · B1 single atoms vs clusters (narrowing to "condition-dependent") · B20 plasmonic hot carriers vs heat (open) · B4–B6 scaling relations, dynamic catalysis, d-band reach (model-level; open) · B25 perovskite hysteresis (largely settled for ion migration).
- **Verified this session.** (1) Room-temperature XFEL crystallography of photosystem II (Bhowmick et al. 2023) shows the inserted oxygen Ox fading between about 500 and 1,200 µs after the third flash, with Mn1–Mn4 contracting only after about 1.2 ms. The authors favour O5–Ox coupling through a peroxide-like transient, but S4 itself was not seen and the coupling partner is unresolved at 2.0–2.16 Å. (2) Microsecond FTIR (Greife et al. 2023) places a deprotonation bottleneck before O–O formation and assigns the reactive state as an oxyl radical. (3) Nitrogenase E4(4H) carries two Fe–H–Fe hydrides and two S-bound protons, and N2 binding is coupled to H2 reductive elimination. Alternating vs distal remains unproven because no intermediates have been isolated in the native enzyme; computations favour one or the other depending on whether Mo or Fe is taken as the binding site. H2 evolution persists even at 50 atm N2. (4) Breaking the *OOH/*OH scaling relation is necessary but not sufficient for better OER/ORR catalysts.
- **Cross-cutting pattern.** Nearly every dispute sets the working state (catalyst or enzyme during turnover) against states that were prepared, trapped, imaged ex situ or computed. Operando methods narrow such disputes but rarely close them, because a small active minority can hide beside a spectator majority. Many mechanism labels (LH/ER, AEM/LOM, radical/nucleophilic, single atom) are model classes whose membership criteria are seldom stated as measurable tests.
- **What usually settles a binary.** Counting a candidate site that has a spectroscopic handle during reaction, normalised to turnover; isotope labelling with quantified backgrounds; replication across instruments and laboratories.
- **Main limit.** Only a few primary sources could be read. Most entries, and nearly all 2024–2026 standings, are [unverified], above all dark oxygen, plasmonic catalysis, Cu/ZnO, pMMO and hydrogenase.

## 1. Active-site identity: single atoms, alloys, interfaces, and the working vs the prepared catalyst

### Takeaway
The active-site binaries share one structure. A site class seen before or after reaction is asked to account for turnover measured during reaction. All three below are narrowing toward condition-dependent answers rather than a win for one side [unverified for 2024–2026].

### B1 · Isolated Pt atoms vs Pt clusters as the CO-oxidation turnover species on oxide supports
- **Claim:** On CeO2 (and similar reducible oxides) under low-temperature CO oxidation (CO + O2, roughly below 200 °C), isolated cationic Pt atoms are the dominant turnover sites.
- **Negation:** With the same support, pretreatment and conditions, Pt clusters or nanoparticles (including clusters formed by restructuring during reaction) carry the dominant turnover, and isolated atoms are spectators or precursors.
- **Scope note:** published claims differ in support (CeO2, FeOx, Al2O3, zeolite), pretreatment (oxidising or reducing) and temperature. The binary is only proper when all three are fixed, so the literature holds several binaries, not one.
- **Observings, claim side:**
  - [observing] Aberration-corrected HAADF-STEM showed isolated bright atoms, and EXAFS showed no Pt–Pt path, on a Pt1/FeOx catalyst that oxidised CO [unverified; Qiao et al., Nat. Chem. 2011; 10.1038/nchem.1095].
  - [observing] Pt trapped on CeO2 by 800 °C air treatment stayed atomically dispersed and active. Later steam treatment activated neighbouring lattice oxygen and raised low-temperature rates [unverified; Jones et al., Science 2016, 10.1126/science.aaf8800; Nie et al., Science 2017, 10.1126/science.aao2109].
- **Observings, negation side:**
  - [observing] In situ IR with STEM on Pt/zeolite and Pt/Al2O3: isolated Pt held CO strongly and did not oxidise it at low temperature, while activity followed Pt nanoparticles [unverified; Ding et al., Science 2015, 10.1126/science.aac6368].
  - [observing] In situ IR/XAS with STEM on Pt/CeO2: the local coordination of atomically dispersed Pt changed under reducing and reaction conditions, and reactivity tracked that change [unverified; DeRita et al., Nat. Mater. 2019, 10.1038/s41563-019-0349-9].
- **Field's explaining (kept apart):** [convention] "Single-atom catalyst" has a membership criterion: no metal–metal bonds, shown by isolated atoms in STEM and no M–M path in EXAFS. That criterion is usually tested before or after reaction, not during it. [simulation] DFT assigns the CO bands and barriers. The class framing as a bridge between homogeneous and heterogeneous catalysis appears in a 2018 review (seen as a reference on https://en.wikipedia.org/wiki/Heterogeneous_catalysis: Wang, Li, Zhang, Nat. Rev. Chem. 2018, doi 10.1038/s41570-018-0010-1).
- **Why hard:** a cluster minority of a few percent can dominate rate. CO bands on Pt1 and on small clusters overlap. Atoms and clusters interconvert reversibly with redox conditions (a cycle, so the state seen depends on when one looks). STEM rarely runs under reaction gas and temperature.
- **Standing in 2026:** narrowing toward "both can be active; which dominates depends on coordination, support and pretreatment" [unverified].
- **What would settle it:** site-selective counting during steady-state turnover (e.g., isotopic transient kinetics), on samples whose populations are verified operando at sub-percent sensitivity, repeated in more than one laboratory.
- **Main proponents:** claim — Tao Zhang, Jun Li, Abhaya Datye, Yong Wang. Negation or conditional — Peter Stair and co-workers (Ding), Phillip Christopher (DeRita) [unverified].
- **Observing or explaining:** explaining (which population accounts for turnover), resting on an observing (do isolated atoms persist under reaction?).

### B2 · Methanol synthesis on Cu/ZnO: Cu–Zn surface alloy vs Cu–ZnO interface
- **Claim:** In Cu/ZnO/Al2O3 under methanol-synthesis conditions (about 200–300 °C, 50–100 bar CO/CO2/H2), the rate-setting site is reduced Zn incorporated into Cu surface steps (a Cu–Zn surface alloy).
- **Negation:** Under the same conditions, the rate-setting site is the interface between Cu and oxidic Zn (a ZnO or ZnOx overlayer or perimeter), and reduced Zn in the Cu surface is not required.
- **Observings, claim side:** [observing] In industrial catalysts, activity correlated with Cu bulk defects and with Zn at Cu steps. The interpretation was supported by [simulation] DFT of Zn-decorated Cu(211) [unverified; Behrens et al., Science 2012, 10.1126/science.1219831]. [observing] Chemisorption-based titration of Zn coverage on the Cu surface: methanol activity rose with Zn surface coverage [unverified; Kuld et al., Science 2016, 10.1126/science.aaf2403].
- **Observings, negation side:** [observing] XPS and kinetics on Zn/Cu(111) and ZnO/Cu(111) model catalysts: under CO2 hydrogenation, surface Zn oxidised to ZnO, and the ZnO/Cu interface was the more active [unverified; Kattel et al., Science 2017, 10.1126/science.aal3573]. [observing] HRTEM of industrial catalysts showed a thin, graphite-like ZnO overlayer on Cu, attributed to a strong metal–support interaction [unverified; Lunkenbein et al., Angew. Chem. 2015]. Operando high-pressure XPS of a Zn/ZnO/Cu(211) model followed Zn speciation under reaction gas; its bearing on this binary could not be checked [unverified; Amann et al., Science 2022].
- **Field's explaining:** [model] an "active site" is treated as a fixed ensemble, although Zn speciation cycles with the CO/CO2/H2O ratio. [simulation] DFT microkinetics assigns formate or CO-hydrogenation routes to each site.
- **Why hard:** the Zn oxidation state depends on gas composition and reverses when it changes. There is a pressure gap between UHV models and 50-bar reactors. Alloy and interface can interconvert, and the active Zn is a small fraction of total Zn.
- **Standing in 2026:** open. A conditional resolution (alloy-type sites in CO-rich feeds, interface sites in CO2-rich feeds) has been proposed but not established [unverified].
- **What would settle it:** surface-sensitive Zn speciation at industrial pressure measured together with kinetics; feed-switching transients; site-selective poisoning; and model catalysts run at 20–50 bar.
- **Main proponents:** alloy — Malte Behrens, Robert Schlögl, Jens Nørskov, Felix Studt, Ib Chorkendorff. Interface — José Rodriguez, Ping Liu [unverified].
- **Observing or explaining:** explaining.

### B3 · Oxide-derived Cu in CO2 electroreduction: does Cu+ or subsurface oxygen persist at working potentials?
- **Claim:** In oxide-derived Cu held at CO2-reduction potentials (about −0.8 to −1.1 V vs RHE in bicarbonate), a measurable population of Cu+ or subsurface oxygen persists and raises C2+ selectivity.
- **Negation:** At the same potentials the electrode is metallic Cu within detection limits. The oxide precursor acts only through morphology: grain boundaries, roughness and local pH.
- **Observings, claim side:** [observing] Ambient-pressure X-ray spectroscopy indicated subsurface oxygen in oxide-derived Cu [unverified; Eilert et al., J. Phys. Chem. Lett. 2017]. Operando XAS on plasma-oxidised Cu reported Cu+ remaining during reaction [unverified; Mistry et al., Nat. Commun. 2016].
- **Observings, negation side:** [observing] In 18O-labelled oxide precursors, residual labelled oxygen after reduction was at percent level or below, so the oxide did not survive [unverified; Lum and Ager, Angew. Chem. 2018]. [simulation] DFT found subsurface oxygen unstable at these potentials [unverified; Garza, Bell, Head-Gordon, ACS Catal. 2018].
- **Field's explaining:** [model] mixed Cu+/Cu0 sites are said to favour CO dimerisation. Here the observing (is Cu+ there?) is cleaner than the explaining (does it matter?).
- **Why hard:** samples re-oxidise when the potential is released or air enters. XAS averages over the bulk. A surface species below 1% could still matter. Cu dissolves and redeposits through transient Cu+ during restructuring (cycling: oxidised ⇄ reduced).
- **Standing in 2026:** narrowing toward metallic Cu at steady state, with transient Cu+ during pulsed operation or restructuring; persistent-Cu+ claims continue [unverified].
- **What would settle it:** time-resolved, surface-sensitive operando probes (Cu–O Raman modes, grazing-incidence XAS) with stated detection limits, combined with 18O tracking through to the products.
- **Main proponents:** persistence — Anders Nilsson, Beatriz Roldan Cuenya, Ethan Crumlin. Metallic — Joel Ager, Alexis Bell, Martin Head-Gordon [unverified].
- **Observing or explaining:** observing first (does Cu+ persist?), then explaining.

### Inferences and gaps (area 1)
- [Inference] In each case, prepared and working states are linked by a reversible change with conditions, which makes "the active site" a time-dependent population rather than a fixed member of a set. The membership criterion therefore has to name the conditions under which it is applied.
- [Gap] No 2024–2026 primary source could be read for B1–B3. Nor could the operando-STEM and high-pressure XPS literature after 2022.

## 2. Scaling relations, the Sabatier volcano and the reach of the d-band model

### Takeaway
Scaling relations are well-documented regularities within classes of surfaces and intermediates. Whether they are limits or breakable depends on the class chosen. Dynamic catalysis tries to evade them by time modulation, and the d-band model ranks adsorption well for late transition metals with known exceptions.

### B4 · Linear scaling: a ceiling for static catalysts, or breakable?
- **Claim:** For multistep reactions whose intermediates bind through the same atom (*OH/*OOH in OER/ORR; *N/*NHx in NH3 synthesis), linear scaling between adsorption energies sets a best-case overpotential or rate that no static catalyst of that class can beat.
- **Negation:** Some static catalysts of the same reaction class exceed the scaling-bounded volcano peak under the same conditions, for example through a second binding motif, confinement, hydrogen-bond acceptors, dual sites or split functions.
- **Observings and constructs, claim side:**
  - [model/simulation] *OOH and *OH energies are tied: about 3.20 eV apart on most catalysts vs an ideal 2.46 eV. This is presented as the OER/ORR bottleneck — seen: Govindarajan, Garcia-Lastra, Meijer, Calle-Vallejo, Curr. Opin. Electrochem. 2018, https://dare.uva.nl/id/e22fe4be-d8ae-4d49-b249-f943677063c3 (doi 10.1016/j.coelec.2018.03.025).
  - [model] Scaling across transition-metal surfaces for hydrogen-containing adsorbates, and BEP relations for N2 dissociation, shrink catalyst design to one or two descriptors. Scaling also limits selectivity, as in C–H activation for methane to methanol — seen: https://en.wikipedia.org/wiki/Heterogeneous_catalysis (references seen there: Abild-Pedersen et al., PRL 2007, doi 10.1103/PhysRevLett.99.016105; Nørskov et al., PCCP 2008, doi 10.1039/B720021H; Nørskov et al., Nat. Mater. 2017, doi 10.1038/nmat4760).
  - [observing] The best measured OER overpotentials (NiFe in base, IrOx in acid) sit roughly 0.25–0.35 V above 1.23 V at 10 mA cm−2 [unverified].
- **Observings and constructs, negation side:** [observing] A LiH-mediated nitrogen-transfer route gave low-temperature ammonia synthesis and was framed as breaking scaling by splitting functions across two materials (seen as a reference title on the Wikipedia page above: Chen et al., Nat. Chem. 2017, doi 10.1038/nchem.2595). Plasma-enabled ammonia synthesis was also claimed to overcome scaling [unverified; Mehta et al., Nat. Catal. 2018, 10.1038/s41929-018-0045-1].
- **Field's explaining:** [model] Breaking *OOH/*OH scaling is necessary but not sufficient. The steps must also be balanced, and the authors propose an electrochemical-step symmetry index for that — seen: Govindarajan et al. 2018 (URL above). [Inference] If the 3.2 eV gap is split evenly between the two middle steps, each needs 1.6 eV, a minimum theoretical overpotential of about 0.37 V (computed here from the stated numbers).
- **Why hard:** what counts as "breaking" depends on the class and descriptor chosen, so membership in "obeys scaling" is set by convention. DFT errors (about 0.1–0.2 eV) are comparable to claimed breaks. Experiments measure currents, not intermediate energies. Mechanism switches (B7) evade scaling rather than break it.
- **Standing in 2026:** narrowing on the conceptual point that scaling relations are class regularities, not laws. Genuine breaks within one mechanism and site class remain rare and contested [unverified].
- **What would settle it:** experimentally measured intermediate binding energies (calorimetry, potential-dependent coverage spectroscopy) on a catalyst claimed to break scaling, together with activity above the class volcano computed for identical conditions.
- **Main proponents:** limit within class — Jens Nørskov, Jan Rossmeisl, Marc Koper. Breakable — Federico Calle-Vallejo, Ping Chen, William Schneider and Jason Hicks (plasma) [unverified except the seen authorships].
- **Observing or explaining:** explaining (model construct).

### B5 · Dynamic (oscillating) catalysis beyond the static Sabatier maximum
- **Claim:** Modulating a catalyst's binding energy periodically (by potential, strain, light or field) at frequencies matched to surface-reaction times yields a time-averaged turnover frequency above the best static catalyst whose binding energy lies within the oscillation range.
- **Negation:** Under the same conditions, measured enhancements do not exceed that static maximum once heating, mass transport and double-layer charging are excluded.
- **Observings and constructs, claim side:** [simulation] Microkinetic models predicted enhancements of orders of magnitude above the volcano peak at "resonant" frequencies [unverified; Ardagh, Abdelrahman, Dauenhauer, ACS Catal. 2019, 10.1021/acscatal.9b01606]. [observing] Pulsed-potential formic acid oxidation on Pt and pulsed-light studies on metal nanoparticles reported time-averaged rates above static ones [unverified].
- **Observings, negation side:** [observing] Reported dynamic enhancements are often comparable to the best static operating point, and capacitive charging currents complicate electrochemical cases. No demonstration in thermal catalysis at industrial conditions is known to this researcher [unverified].
- **Field's explaining:** [model] "Resonance" and the static Sabatier maximum are both model-defined: they assume scaling plus BEP and a single dominant pathway. A 2025 preprint argues that the standard turnover frequency from the energetic-span model collapses catalysis to one scalar and assumes a dominant pathway with no spatial or temporal variation, which is the assumption dynamic catalysis abandons — seen: Crespilho, "Toward a Unified Theory of Catalysis," https://arxiv.org/pdf/2505.01213.
- **Why hard:** binding-energy amplitudes of about 0.1–1 eV at Hz–MHz rates are hard to impose uniformly and to measure independently. The right static comparator must be measured on the same catalyst.
- **Standing in 2026:** open. The theory is robust within its models; experimental demonstrations are early [unverified].
- **What would settle it:** a modulated catalyst whose rate exceeds the best static rate measured across its whole oscillation range, with operando evidence that binding energy actually oscillates.
- **Main proponents:** claim — Paul Dauenhauer, Omar Abdelrahman. Sceptical voices not identified in this session [unverified].
- **Observing or explaining:** observing (does the rate exceed?), judged against a model criterion.

### B6 · Is the d-band centre a sufficient descriptor of chemisorption trends?
- **Claim:** For a given adsorbate, the d-band centre (first moment of the surface-projected d-band density of states) ranks adsorption energies correctly across transition metals, alloys and strained surfaces.
- **Negation:** Systematic classes within the same surfaces (filled-d noble metals, near-surface alloys, adsorbates with strong Pauli repulsion) are misranked by the d-band centre at the same level of theory, and further descriptors (width, upper edge, filling, sp coupling) are needed.
- **Observings, claim side:** [model] Gold's nobility explained by d-band position plus coupling strength [unverified; Hammer and Nørskov, Nature 1995, 10.1038/376238a0]. [observing] Activity of Pt-alloy ORR catalysts correlated with d-band shifts estimated from photoemission [unverified].
- **Observings, negation side:** [simulation] Exceptions in which adsorbate–d-state repulsion dominates [unverified; Xin and Linic, J. Chem. Phys. 2010, 10.1063/1.3437609]. The upper band edge has been proposed as a better descriptor for some metals and oxides [unverified].
- **Field's explaining:** [simulation] The d-band centre is itself computed. Its experimental proxy, valence photoemission, measures total rather than surface-projected states.
- **Why hard:** "sufficient" depends on the tolerance chosen. The model assumes metallic surfaces and fails by construction on oxides and isolated atoms.
- **Standing in 2026:** settled as a useful first-order descriptor for late transition metals with named exceptions. Open for oxides, single atoms and electrified interfaces [unverified].
- **What would settle it:** a benchmark of experimental adsorption energies (single-crystal calorimetry) for many metals and alloys against competing descriptors.
- **Main proponents:** Bjørk Hammer, Jens Nørskov (model). Suljo Linic, Hongliang Xin, Aleksandra Vojvodic (refinements) [unverified].
- **Observing or explaining:** explaining.

### Inferences and gaps (area 2)
- [Inference] B4–B6 are disputes about the scope of model constructs, not about observings. Each turns on how a set ("obeys scaling", "on the volcano", "d-band metal") is bounded.
- [Gap] No 2023–2026 review of scaling-relation breaking could be fetched; a 2025 Chem. Soc. Rev. article surfaced in an earlier session search but failed to load.

## 3. Electrocatalysis mechanisms

### Takeaway
Most electrocatalysis binaries turn on what sits in the first nanometre of the interface: lattice versus adsorbed oxygen, cations, and water structure. The cleanest observing binaries (B8 cation necessity, B12 nitrogen reduction) are settling. The explaining binaries (B9, B10, B11) remain open because double-layer structure is not directly measured.

### B7 · Oxygen evolution: does lattice oxygen enter the product?
- **Claim (scoped):** On a stated oxide (e.g., La1−xSrxCoO3−δ perovskites, amorphous IrOx, RuO2) in a stated electrolyte at OER potentials, part of the evolved O2 contains lattice oxygen (lattice oxygen mechanism, LOM), beyond what surface isotope exchange with water explains.
- **Negation:** On the same oxide under the same conditions, evolved O2 contains no lattice oxygen beyond the exchange background, and O–O forms through adsorbates (AEM: *OH → *O → *OOH → O2).
- **Split:** this is (a) an observing (is lattice oxygen in the product?) and (b) an explaining (does LOM carry a large share of turnover and explain the pH-dependent activity?). Only (a) is treated as the binary here.
- **Observings, claim side:** [observing] With 18O-labelled perovskites, on-line mass spectrometry detected labelled O2, and activity varied with pH on the RHE scale; this was read as LOM with decoupled proton–electron transfer [unverified; Grimaud et al., Nat. Chem. 2017, 10.1038/nchem.2695]. [observing] Lattice-oxygen release from amorphous IrOx tracked its dissolution [unverified; Kasian et al., Energy Environ. Sci. 2019]. A 2021 study reported evidence of a Mars–van Krevelen-type route on Ni-based OER catalysts (title only, seen in a search listing: https://pubs.kist.re.kr/handle/201004/116901 and https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8251801/; content not read; attribution to Strasser and co-workers [unverified]).
- **Observings, negation side:** [observing] Isotope-labelled electrochemical mass spectrometry on crystalline rutile IrO2 and RuO2 found lattice contributions at or below the percent level at moderate potentials [unverified; Chorkendorff, Stephens and co-workers, 2018–2022].
- **Field's explaining:** [model] AEM and LOM are pathway classes. pH dependence on the RHE scale is used as an LOM diagnostic, but cations and the double layer can also produce it (B9–B11). [simulation] The oxygen p-band centre has been proposed as a descriptor [unverified].
- **Why hard:** surface oxygen exchanges with water. Natural-abundance 34O2 sets a background. Dissolution and amorphisation create new surfaces during measurement, and lattice participation correlates with instability.
- **Standing in 2026:** narrowing. Lattice participation is accepted on some covalent or defective oxides, often tied to degradation, and is considered minor on crystalline rutiles [unverified].
- **What would settle it:** a quantitative 18O mass balance from catalyst label to product with depth-resolved accounting, measured alongside dissolution.
- **Main proponents:** LOM — Yang Shao-Horn, Alexis Grimaud, Peter Strasser, Alexie Kolpak. AEM-dominant — Jan Rossmeisl and Jens Nørskov (theory), Ib Chorkendorff and Ifan Stephens (measurement on rutiles) [unverified].
- **Observing or explaining:** observing for (a); explaining for (b).

### B8 · Are metal cations required for CO2 electroreduction on Cu, Au and Ag?
- **Claim:** In aqueous electrolyte at CO2-reduction potentials, CO2 reduction on Cu, Au and Ag needs metal cations at the interface. Without them, only hydrogen evolution occurs.
- **Negation:** Under the same conditions, CO2 reduction proceeds at measurable rates in electrolytes containing no metal cations.
- **Observings, claim side:** [observing] Voltammetry with on-line product detection (including scanning electrochemical microscopy) on Au, Ag and Cu: no CO in cation-free (proton-only) electrolyte, and CO appeared when metal cations were added [unverified; Monteiro et al., Nat. Catal. 2021, 10.1038/s41929-021-00655-5]. Cation-size effects on product distribution date to the 1990s [unverified; Murata and Hori 1991].
- **Observings, negation side:** [observing] Organic cations (tetraalkylammonium) also support CO2 reduction in some reports. The claim is therefore about non-proton cations generally, with metal cations as the tested case [unverified].
- **Field's explaining:** [model] A partially desolvated cation stabilises adsorbed *CO2− by short-range interaction. [simulation] Ab initio molecular dynamics and DFT support this (same paper).
- **Why hard:** a "cation-free" solution still holds H3O+. Trace alkali contamination at micromolar levels matters. The interfacial cation concentration is not measured directly.
- **Standing in 2026:** narrowing, and widely cited as established for metallic Cu/Au/Ag in water. The number of independent replications was not checked [unverified].
- **What would settle it:** independent replication with electrolytes verified by ICP-MS to sub-micromolar alkali, plus surface-enhanced IR detection of *CO2− appearing only when cations are present.
- **Main proponents:** claim — Marc Koper, Mariana Monteiro, Federico Dattila, Núria López. No organised opposing side identified [unverified].
- **Observing or explaining:** observing.

### B9 · How do cations promote CO2 reduction? Interfacial field or coordination vs buffering
- **Split:** three accounts compete: (i) the interfacial electric field set by cations at the outer Helmholtz plane; (ii) buffering of local pH by cation hydrolysis; (iii) short-range coordination of a partially desolvated cation to *CO2−. Accounts (i) and (iii) differ in range; (ii) is a different causal path. Two proper binaries follow: B9a, field-type (i or iii) vs buffering (ii); B9b, long-range field vs short-range coordination (listed with the further candidates).
- **Claim (B9a):** At fixed potential and bulk pH, the rise in CO and C2+ rates on Cu and Ag with cation size (Li+ < Na+ < K+ < Cs+) comes mainly from cation-induced field or coordination stabilising *CO2 and *CO–*CO coupling.
- **Negation (B9a):** It comes mainly from hydrolysis of larger hydrated cations buffering the interface, which lowers local pH and raises local CO2.
- **Observings:** [observing] On Cu and Ag, larger cations increased CO, C2H4 and ethanol rates but not H2 or CH4 rates [unverified; Resasco et al., JACS 2017, 10.1021/jacs.7b06765]. [observing + model] Cation-size trends on Ag and Cu were modelled with cation-hydrolysis buffering [unverified; Singh et al., JACS 2016, 10.1021/jacs.6b07612]. [simulation] A continuum double-layer model with DFT found cation size changes the field and that hydrolysis is too weak to buffer [unverified; Ringe et al., Energy Environ. Sci. 2019, 10.1039/C9EE01341E]. Monteiro et al. 2021 (B8).
- **Why hard:** field and local pH both change with cation identity. Local pH is hard to measure at operating currents. Models need unmeasured inputs (outer-Helmholtz-plane distance, local permittivity; see B11).
- **Standing in 2026:** narrowing toward field or coordination as the main cause, with buffering secondary. The range of action (B9b) is open [unverified].
- **What would settle it:** varying cation identity at operando-verified constant local pH; varying field at constant cation; vibrational Stark spectroscopy quantifying the field felt by the intermediate.
- **Main proponents:** field — Karen Chan, Alexis Bell, Stefan Ringe. Buffering — Meenesh Singh, Joel Ager, Alexis Bell (2016). Coordination — Marc Koper, Núria López [unverified].
- **Observing or explaining:** explaining.

### B10 · Why is hydrogen evolution on Pt slower in base than in acid? Hydrogen binding energy vs interfacial water
- **Split:** three accounts: pH-dependent hydrogen binding energy (HBE); interfacial-water reorganisation; promotion by adsorbed OH (bifunctional). The binary here is HBE vs interfacial water; adsorbed OH is listed with the further candidates.
- **Claim:** The roughly hundredfold lower HER/HOR rates on Pt in alkaline vs acidic electrolyte (on the RHE scale) are explained mainly by a pH-dependent strengthening of the Pt–H binding energy.
- **Negation:** Under the same conditions they are explained mainly by slower reorganisation of interfacial water (linked to how far the HER potential lies from the potential of zero free charge), not by a change in H binding.
- **Observings, claim side:** [observing] Rotating-disk HOR/HER exchange currents on Pt/C across buffered pH 0–13, with the hydrogen underpotential-deposition peak shifting about 10 mV per pH unit; activity correlated with the HBE derived from that peak [unverified; Sheng et al., Nat. Commun. 2015, 10.1038/ncomms6848].
- **Observings, negation side:** [observing] On Pt(111), with and without Ni(OH)2 decoration, laser-induced temperature jumps located the potential of maximum entropy (a proxy for the potential of zero free charge). HER rates correlated with its distance from the HER potential, read as an interfacial-water reorganisation barrier [unverified; Ledezma-Yanez et al., Nat. Energy 2017, 10.1038/nenergy.2017.31]. Ni(OH)2-decorated Pt sped up alkaline HER [unverified; Subbaraman et al., Science 2011, 10.1126/science.1211934].
- **Field's explaining:** [convention/model] "HBE from the UPD peak" assumes that underpotential-deposited H stands in for the HER intermediate. That is disputed: UPD H and on-top H may differ, and co-adsorbed cations or OH shift the UPD peaks.
- **Why hard:** pH co-varies with cation concentration, field and proton donor (H3O+ vs H2O). The potential of zero free charge on Pt is not measured directly.
- **Standing in 2026:** open. It is increasingly framed as a double-layer and proton-donor effect, with HBE contributing [unverified].
- **What would settle it:** decoupling pH from cation identity and concentration; measuring on-top Pt–H coverage (surface IR) versus pH; independent estimates of the potential of zero free charge.
- **Main proponents:** HBE — Yushan Yan, Jingguang Chen. Interfacial water — Marc Koper. Adsorbed OH — Nenad Markovic, Vojislav Stamenkovic [unverified].
- **Observing or explaining:** explaining.

### B11 · Does the Gouy–Chapman–Stern picture describe metal/aqueous double layers?
- **Claim:** For a metal electrode (Hg, Ag, Au or Pt single crystals) in dilute aqueous electrolyte without specific adsorption, the Gouy–Chapman–Stern model (a diffuse layer of point ions in series with a potential-independent compact layer) reproduces measured differential capacitance against potential and concentration.
- **Negation:** Under the same conditions, measured capacitance and interfacial structure deviate systematically from Gouy–Chapman–Stern in ways that require molecular features it lacks: water orientation and dielectric saturation, ion–surface attraction, and electron spill-out from the metal.
- **Observings, claim side:** [observing] Mercury capacitance curves with a diffuse-layer minimum near the potential of zero charge at low concentration were the classical support [unverified; Grahame, Chem. Rev. 1947, 10.1021/cr60130a002].
- **Observings, negation side:** [observing] Pt(111) in dilute perchlorate showed a Gouy–Chapman-like minimum, but fitting it needed extra ion–surface terms [unverified; Ojha, Doblhoff-Dier, Koper, PNAS 2022]. [observing] X-ray absorption showed potential-dependent changes in the hydrogen bonding of interfacial water on Au [unverified; Velasco-Velez et al., Science 2014, 10.1126/science.1259437]. [observing] Water confined to about 1 nm had a dielectric constant near 2, far below the bulk value of about 80, which challenges uniform-permittivity compact layers [unverified; Fumagalli et al., Science 2018, 10.1126/science.aat4191]. Concentrated-electrolyte and ionic-liquid deviations (overscreening, crowding) are covered by the water-and-interfaces notes [cross-reference; unverified here: Kornyshev, J. Phys. Chem. B 2007; Bazant, Storey, Kornyshev, PRL 2011].
- **Field's explaining:** [model] Gouy–Chapman–Stern treats the compact-layer capacitance as an adjustable constant. Modified Poisson–Boltzmann and [simulation] ab initio or classical MD add steric, dielectric and specific-interaction terms.
- **Why hard:** capacitance integrates over structure, so different models can fit the same curve. Clean single-crystal data are scarce. Simulations cannot yet reach realistic concentrations and timescales.
- **Standing in 2026:** settled that Gouy–Chapman–Stern works as a coarse description near the potential of zero charge at low concentration; open for a quantitative molecular model. This bears directly on B9 and B10 [unverified].
- **What would settle it:** capacitance, interfacial-water orientation (sum-frequency or surface IR) and ion profiles (X-ray reflectivity) measured on the same crystal across potential, compared with parameter-free simulation.
- **Main proponents:** classical — the Grahame tradition. Revisions — Alexei Kornyshev, Martin Bazant, Marc Koper, Wolfgang Schmickler [unverified].
- **Observing or explaining:** explaining (model adequacy).

### B12 · Aqueous electrochemical N2 reduction: real ammonia or contamination?
- **Claim:** Transition-metal and nanostructured electrocatalysts in aqueous electrolyte at ambient temperature and pressure reduce N2 to NH3 at the rates and Faradaic efficiencies reported in 2016–2020 (typically µg h−1 mg−1, a few percent FE).
- **Negation:** Under the same conditions, the NH3 detected comes from contaminants (NH3 and NOx in gas, electrolyte, membranes or catalyst nitrogen), and N2-derived NH3 confirmed quantitatively with 15N2 is below detection.
- **Observings:** [observing] A protocol with 15N2, gas cleaning and quantitative isotope analysis was applied to several reported systems. None gave N2-derived NH3 in aqueous electrolyte, while lithium-mediated reduction in organic electrolyte did [unverified; Andersen et al., Nature 2019, 10.1038/s41586-019-1260-x]. A systematic analysis of false positives followed [unverified; Choi et al., Nat. Commun. 2020]. Lithium-mediated systems later reported near-unit current efficiency and continuous flow [unverified; Du et al., Nature 2022; Fu et al., Science 2023].
- **Field's explaining:** [convention] "Confirmed" means 15N in product, full nitrogen balance and rate well above blanks. That criterion was adopted only after the false-positive wave.
- **Why hard:** NH3 is everywhere at ppb–ppm. Colorimetric assays suffer interference. 15N2 cylinders can carry 15NH3 or 15NOx impurities. Claimed rates sat near background.
- **Standing in 2026:** largely settled against the aqueous transition-metal claims at the reported rates; some retractions are known to this researcher but not checked. The lithium-mediated route is an active, accepted field [unverified].
- **What would settle it (remaining cases):** quantitative 15N2 runs with gas cleaning and full N balance in independent laboratories, at rates at least ten times above blanks.
- **Main proponents:** rigorous protocol — Ib Chorkendorff, Ifan Stephens, Jens Nørskov, Thomas Jaramillo, Douglas MacFarlane and Alexandr Simonov. Claims — many groups, 2016–2020 [unverified]. Historically notable as a rejected claim set; the reason is failed isotope controls.
- **Observing or explaining:** observing.

### Inferences and gaps (area 3)
- [Inference] B8–B11 form a chain: the cation question (B8, B9) and the pH question (B10) both reduce to double-layer structure (B11), which no instrument yet images at molecular resolution under reaction.
- [Gap] Post-2023 work on cation coordination (surface IR, Stark spectroscopy, acidic CO2 reduction with cations) could not be read.

## 4. Enzymatic and bioinorganic mechanisms

### Takeaway
2023 brought the strongest direct data for photosystem II: time-resolved XFEL structures and microsecond IR. Nitrogenase has firm spectroscopic data up to E4, and pathway inference beyond that point. pMMO and [FeFe]-hydrogenase are disputes about which observed states lie on the catalytic cycle.

### B13 · Nitrogenase: alternating vs distal hydrogenation of N2
- **Claim:** In Mo-nitrogenase, after N2 binds at E4, hydrogenation alternates between the two N atoms (diazene- then hydrazine-level species), so the first NH3 leaves only after N–N cleavage at the hydrazine level.
- **Negation:** Hydrogenation goes to the distal N first, releasing the first NH3 at an E5/E6-level stage and leaving a metal-bound nitride (the distal or Chatt/Schrock-type route).
- **Observings, alternating side:** [observing] Vanadium nitrogenase releases hydrazine as a product (seen as a reference on https://en.wikipedia.org/wiki/Nitrogenase: Dilworth and Eady, Biochem. J. 1991, doi 10.1042/bj2770465). [model] A teaching text lays out the alternating sequence: hydrazido at E5, hydrazine at E6, NH3 release with an amide left at E7 — seen: https://wisc.pb.unizin.org/nitrogencycle/?p=28. [observing] Iron model complexes reduce N2 catalytically (seen as reference: Anderson, Rittle, Peters, Nature 2013, doi 10.1038/nature12435).
- **Observings, distal side:** [observing] Single-Mo complexes reduce N2 through nitrido intermediates (seen as reference: Schrock, Acc. Chem. Res. 2005, doi 10.1021/ar0501121). [simulation] Mo-centred DFT analyses favour distal routes (seen as reference: Neese, Angew. Chem. 2005, doi 10.1002/anie.200502667; Hinnemann and Nørskov, Top. Catal., doi 10.1007/s11244-006-0002-0).
- **Status statement (seen):** neither pathway is proven, because no intermediates have been isolated in the native enzyme; computations support one or the other depending on whether Mo or Fe is taken as the binding site — https://en.wikipedia.org/wiki/Nitrogenase.
- **Field's explaining:** [convention] Lowe–Thorneley En labels count delivered electron–proton equivalents (E0–E8), not structures. [model] Pathway assignments map structures onto those counts.
- **Why hard:** intermediates past E4 are short-lived and trapped at low occupancy among mixtures. The binding site (Fe2/Fe6 face vs Mo) is not established. Hydrazine or diazene fed as substrates may enter the cycle differently from N2-derived species.
- **Standing in 2026:** open, leaning alternating among the main spectroscopy groups. A 2025 unified kinetic model exists (seen as reference title: Harris, Dean, Hoffman, Raugei, Seefeldt, ACS Catal. 2025, doi 10.1021/acscatal.5c05136); its pathway conclusions were not read.
- **What would settle it:** 15N-resolved spectroscopy (ENDOR, Mössbauer, NRVS) of an N2-derived E5–E7 intermediate trapped with N2 as substrate, plus single-turnover timing of the first NH3 release against electron count.
- **Main proponents:** alternating — Brian Hoffman, Lance Seefeldt, Dennis Dean. Distal — Richard Schrock (model chemistry) and Mo-centred computation [partly seen via references].
- **Observing or explaining:** explaining.

### B14 · Nitrogenase: is H2 release obligatorily coupled to N2 binding at E4 (the "Janus" mechanism)?
- **Claim:** Productive N2 binding requires E4(4H), and binding is coupled to reductive elimination of H2 from two bridging hydrides. At least one H2 per N2 is therefore obligatory (N2 + 8e− + 8H+ → 2NH3 + H2).
- **Negation:** N2 binding and activation do not require H2 reductive elimination. H2 formed during N2 reduction is a parallel side reaction (hydride protonation), so the minimum could be lower than one H2 per N2.
- **Observings, claim side:**
  - [observing] H2 evolution was not suppressed even at 50 atm N2 (seen as reference title: Simpson and Burris, Science 1984, doi 10.1126/science.6585956, on https://en.wikipedia.org/wiki/Nitrogenase).
  - [observing] In the α-V70I variant, whose bulky Ile side chain suppresses hydride protonation, E4(4H) accumulates. Its EPR/ENDOR signals match wild type and show two bridging hydrides (Fe2–H–Fe6, Fe3–H–Fe7) with protons on two sulfurs. In wild type at −50 °C, relaxation by hydride protonation took about 6 min from E4(4H) and about 330 min from E2(2H). The authors also propose a minor direct H2-elimination route to an E4(2H)* state — seen: Lukoyanov et al., Faraday Discuss. 2023, 243, 231–252, https://par.nsf.gov/servlets/purl/10439202 (doi 10.1039/d2fd00153e).
  - [model] E4 is the branch point, going forward to N2 fixation or back to E2/E0 with H2 loss — seen: https://wisc.pb.unizin.org/nitrogencycle/?p=28; ENDOR "electron inventory" of E4 (seen as reference: Doan et al., JACS 2011, doi 10.1021/ja205304t).
- **Observings and constructs, negation side:** [observing] E3 can also react with N2 (stated on the Wikipedia page, seen). [simulation] Alternative DFT mechanisms bind N2 at other states or form H2 independently of N2 [unverified; Ian Dance; Per Siegbahn].
- **Field's explaining:** [convention] The canonical 16 MgATP per N2 is itself model-dependent; the Wikipedia page cites a recent kinetic refinement raising the minimum to about 25 MgATP per N2 (seen; the attribution to Harris et al. 2025 is likely but [unverified]).
- **Why hard:** coupling is inferred from kinetics and cryogenic snapshots, not watched at turnover temperature. The N2 binding site is unknown.
- **Standing in 2026:** narrowing. It is widely accepted within the Hoffman–Seefeldt–Dean framework and contested by some computational alternatives [unverified beyond the seen sources].
- **What would settle it:** time-resolved detection of H2 release concurrent with N2 binding at E4 under turnover, with HD-formation kinetics (from D2 + N2) matching the model quantitatively.
- **Main proponents:** claim — Brian Hoffman, Lance Seefeldt, Dennis Dean, Simone Raugei (seen authorships). Negation — some computational groups [unverified].
- **Observing or explaining:** explaining.

### B15 · Nitrogenase: is the central carbide a spectator or a participant?
- **Claim:** The interstitial μ6-carbide of FeMo-co stays a structural and electronic spectator during catalysis: it is not protonated, exchanged or used as a substrate site.
- **Negation:** The carbide takes part chemically during turnover, through transient protonation or Fe–C bond lability that opens the cluster for substrate binding.
- **Observings:** [observing] The carbide was identified in 2011 by X-ray emission spectroscopy and high-resolution crystallography [unverified; Lancaster et al., Science 2011, 10.1126/science.1206445; Spatzal et al., Science 2011, 10.1126/science.1214025]. It is inserted by a radical-SAM enzyme, NifB [unverified; Wiig et al., Science 2012]. [observing] Belt sulfur S2B was displaced by CO or Se in crystal structures, showing that the cluster is labile around the carbide [unverified; Spatzal et al., Science 2014, 10.1126/science.1256679]. A 2018 structure assigned an N2-derived species at belt positions; this was contested [unverified; Sippel et al., Science 2018, 10.1126/science.aar2765]. No experiment known to this researcher shows carbide exchange or protonation during turnover [unverified].
- **Field's explaining:** [reconstruction] Atom identities at 1 Å-scale resolution come from electron density plus spectroscopy. [simulation] Protonated-carbide proposals depend on the DFT functional used.
- **Why hard:** the carbide is buried. Probing it needs 13C-labelled cofactor. Crystallisation can trap off-cycle states.
- **Standing in 2026:** open, leaning toward an electronically important spectator [unverified]. The nitrogenase sources seen this session did not discuss the carbide.
- **What would settle it:** 13C-carbide ENDOR or solid-state NMR under turnover, showing or excluding hyperfine changes expected from protonation or bond opening.
- **Main proponents:** Oliver Einsle, Douglas Rees, Serena DeBeer, Markus Ribbe and Yilin Hu, Ragnar Bjornsson (computation) [unverified].
- **Observing or explaining:** explaining, with an observing core (does the carbide environment change under turnover?).

### B16 · Photosystem II: which oxygens form the O–O bond?
- **Claim:** In the S3→[S4]→S0 transition at room temperature, O2 forms by coupling of the bridging oxo O5 with Ox (also called O6), the oxygen inserted between Mn1 and Ca during S2→S3.
- **Negation:** Under the same conditions, O2 forms without O5–Ox coupling, for example O5 with water W2 or W3 (Ox then replacing O5), or Ox with a terminal water.
- **Observings (seen):** Room-temperature serial femtosecond crystallography at LCLS and SACLA, with samples delivered by acoustic droplet ejection on a moving tape. S3 was prepared by two flashes and the third flash started the transition. Delays ran 50, 250, 500, 730, 1,200, 2,000 and 4,000 µs, plus a 200 ms S0 reference, at 2.00–2.16 Å resolution.
  - [observing] Ox density became asymmetric from about 250 µs, fell after 500 µs and reached noise level at 1,200–2,000 µs (below 20% occupancy at 2,000 µs). The abstract dates its loss to about 700 µs, parallel with reduction of the tyrosine YZ.
  - [observing] The Mn1–Mn4 distance stayed long until 1,200 µs, then contracted over about 3 ms, taken as the onset of O2 release.
  - [observing] D1-E65 rotated and a hydrogen-bond path formed in the Cl1 channel at about 250–500 µs, read as a first proton release; a second change at 1,200–4,000 µs was read as a second. Waters of the O1-channel "water wheel" had high B-factors.
  - Source: Bhowmick et al., Nature 2023, 617, 629–636, doi 10.1038/s41586-023-06038-z — seen: https://bergmann.physics.wisc.edu/wp-content/uploads/2023/06/pub226.pdf and https://impact.ornl.gov/en/publications/structural-evidence-for-intermediates-during-osub2sub-formation-i/
- **Field's explaining (seen, same paper):** [reconstruction] each time point was fitted as a multicomponent mixture (S3 still about 35% at 1,200 µs). [model] The authors favour O5–Ox coupling, based on proximity and lower O5 density at 1,200 µs, but do not exclude O5 + W2/W3 with Ox replacing O5. They find no clear support for routes excluding O5. They propose a transient, probably peroxide-like intermediate within a two-step, four-electron reduction. S4 and that intermediate were not directly observed, and better Ox placement needs higher resolution.
- **Earlier and later context:** Ox/O6 was first reported in S3 by XFEL work from the Suga/Shen and Kern/Yano/Yachandra teams [unverified; Suga et al., Science 2019, 10.1126/science.aaw4325; Kern et al., Nature 2018, 10.1038/s41586-018-0681-2]. A 2024 XFEL study of S1→S2→S3 [unverified; Li et al., Nature 2024].
- **Why hard:** short-lived states sit in mixed populations. Occupancy and disorder limit resolution even without radiation damage. S4 has never been trapped structurally. The protonation state of O5 is uncertain.
- **Standing in 2026:** narrowing to O5-involving coupling. The choice between O5–Ox and O5–water is open [unverified for post-2023 work].
- **What would settle it:** sub-1.8 Å time-resolved crystallography with purer S-state populations; substrate-water exchange kinetics with H2 18O (membrane-inlet mass spectrometry) assigning the slowly and rapidly exchanging substrates to O5 and Ox; time-resolved X-ray spectroscopy detecting a peroxide.
- **Main proponents:** O5–Ox — Junko Yano, Vittal Yachandra, Jan Kern, Johannes Messinger, Athina Zouni (seen authorships); Michihiro Suga and Jian-Ren Shen (O5–O6). Water as partner — Gary Brudvig, Vincent Pecoraro [unverified].
- **Observing or explaining:** observing/reconstruction (which atoms couple?).

### B17 · Photosystem II: radical (oxyl–oxo) coupling vs nucleophilic attack
- **Claim:** The O–O bond forms by radical coupling of a Mn-bound oxyl radical with an oxo bridge.
- **Negation:** It forms by nucleophilic attack of water or hydroxide (possibly Ca-bound) on an electrophilic Mn(V)=O or Mn(IV)-oxyl.
- **Observings:** [observing] Time-resolved microsecond FTIR with quantum chemistry found an early deprotonation (Asp61, or a Glu65/Glu312 pair) forming an electron–proton bottleneck before the final oxidation, and identified the reactive intermediate as an oxyl-radical state — seen: news summary of Greife et al., Nature 2023, doi 10.1038/s41586-023-06008-5, https://www.sfb1078.de/news/230504_Nature_Rana-Ali.html (paper itself not read). [observing] Bhowmick et al. note that the earlier oxyl/oxo proposal for S3 conflicts with X-ray emission data showing Mn rather than ligand oxidation in S2→S3; they did not test radical vs nucleophilic coupling for S3→S0 (seen, PDF above). [observing] Time-resolved X-ray absorption showed a lag of about 200 µs before O2 formation (an S4′-type state) [unverified; Haumann et al., Science 2005, 10.1126/science.1117827]. [observing] S3 EPR indicated all-Mn(IV) octahedral ions poised for O–O formation [unverified; Cox et al., Science 2014, 10.1126/science.1254698].
- **Field's explaining:** [simulation] DFT gives the lowest barrier for oxyl–oxo coupling [unverified; Siegbahn, Acc. Chem. Res. 2009, 10.1021/ar900117k]. [convention] "Radical coupling" and "nucleophilic attack" may be limiting labels on a continuum of Mn–O electronic structures.
- **Why hard:** the O–O step is fast compared with the steps before it. Mn(IV)-oxyl and Mn(V)-oxo overlap spectroscopically. Computed barriers depend on the functional.
- **Standing in 2026:** narrowing toward oxyl (radical) character in the reactive state; the coupling mode stays open [unverified for post-2023 work].
- **What would settle it:** time-resolved spectroscopy sensitive to ligand radicals (O K-edge or Kβ emission) at the timing of O–O formation; kinetic isotope effects; substrate-water exchange data.
- **Main proponents:** radical coupling — Per Siegbahn, Johannes Messinger, Holger Dau, Dimitrios Pantazis and Nicholas Cox. Nucleophilic attack — Gary Brudvig, Vincent Pecoraro [unverified].
- **Observing or explaining:** explaining.

### B18 · Particulate methane monooxygenase: CuD vs CuB as the active site
- **Split:** three accounts: the CuB site in PmoB (mono- or dicopper); the CuD site (with nearby CuC) in the membrane-bound PmoC; and a tricopper cluster. The binary here is CuD vs CuB; the tricopper proposal is listed with the further candidates.
- **Claim:** The methane-oxidising site of pMMO is CuD in PmoC, identified in lipid environments where activity is preserved.
- **Negation:** The methane-oxidising site is CuB in the soluble region of PmoB.
- **Observings, CuB side:** [reconstruction] A crystal structure of detergent-solubilised pMMO showed copper sites, including one modelled as dinuclear CuB [unverified; Lieberman and Rosenzweig, Nature 2005, 10.1038/nature03311]. [observing] Activity of soluble PmoB fragments was read as dicopper CuB being active [unverified; Balasubramanian et al., Nature 2010, 10.1038/nature08992]. EPR/ENDOR later found only mononuclear copper centres [unverified; Ross et al., Science 2019, 10.1126/science.aav2572].
- **Observings, CuD side:** [observing] Cryo-EM of pMMO in lipid nanodiscs restored activity and revealed the CuD site [unverified; Koo et al., Science 2022]. [observing] Cryo-EM and ENDOR with the product analogue 2,2,2-trifluoroethanol placed it near CuD [unverified; Tucci et al., Nat. Catal. 2023, 10.1038/s41929-023-01051-x].
- **Why hard:** activity is lost on solubilisation, copper occupancy is partial, and for decades no robust in vitro activity existed. Assignments depend on reconstitution conditions.
- **Standing in 2026:** narrowing toward CuD. The tricopper proposal is still argued by its originators [unverified for 2024–2026].
- **What would settle it:** in vivo mutagenesis of CuD vs CuB ligands with activity assays; spectroscopic capture of a Cu–oxygen intermediate at CuD under turnover.
- **Main proponents:** CuD — Amy Rosenzweig, Brian Hoffman. CuB (earlier view) — Rosenzweig 2010. Tricopper — Sunney Chan [unverified].
- **Observing or explaining:** explaining, with an observing core (where do substrate and product bind?).

### B19 · [FeFe]-hydrogenase: only CO-bridged intermediates on the cycle?
- **Claim:** During H2 turnover the H-cluster passes only through states that keep the bridging CO between the two Fe of the [2Fe] subcluster.
- **Negation:** The catalytic cycle includes states in which the bridging CO has become terminal and a bridging hydride sits between the Fe atoms.
- **Observings:** [observing] FTIR spectroelectrochemistry and nuclear resonance vibrational spectroscopy identify states including a terminal-hydride state; states with a bridging hydride and no bridging CO appear under some pH, variant or redox conditions [unverified]. The argument that catalysis uses CO-bridged intermediates exclusively has been made from spectroscopy plus computation [unverified; Birrell, Lubitz, DeBeer, Cramer and co-workers, JACS 2020]; the opposing kinetic-spectroscopic case comes from the Haumann, Stripp and Happe groups [unverified].
- **Why hard:** states interconvert with pH and potential. Assignments rest on CO/CN band positions. Cryogenic, steady-state and room-temperature data differ.
- **Standing in 2026:** open [unverified].
- **What would settle it:** time-resolved IR during turnover (potential or light jumps) correlating state populations with H2 production on the same timescale.
- **Main proponents:** CO-bridged only — James Birrell, Wolfgang Lubitz, Edward Reijerse. Alternative states — Michael Haumann, Sven Stripp, Thomas Happe [unverified].
- **Observing or explaining:** explaining (which observed states are on-cycle).

### Inferences and gaps (area 4)
- [Inference] The enzyme binaries are disputes about sequencing: which of several observed states come prior, now and next within a cycle (Kok S0–S4; Lowe–Thorneley E0–E8). The counting conventions (S-states, E-states) are firmer than the structures attached to them. The Kok scheme's period-four oscillation is a model fit to flash yields, and its signals are not always uniquely assignable — seen: Shinkarev, Photosynth. Res. 1996, https://link.springer.com/article/10.1007/BF00029473 (doi 10.1007/BF00029473).
- [Gap] Could not read post-2023 nitrogenase cryo-EM under turnover, 2024–2026 pMMO work, or hydrogenase primary papers.

## 5. Surface reaction dynamics and contested observings

### Takeaway
One dispute here is about whether something happened at all (dark oxygen). The other two are about which account explains an agreed rise in rate (plasmonic catalysis; Langmuir–Hinshelwood vs Eley–Rideal under plasma).

### B20 · Plasmonic photocatalysis: hot carriers vs photothermal heating
- **Claim:** In the Cu–Ru antenna–reactor NH3-decomposition system and similar plasmonic catalysts under visible light, a substantial part of the light-induced rate increase comes from non-thermal hot-carrier processes, beyond what the measured temperature rise explains.
- **Negation:** In the same systems, the rate increase is fully explained by photothermal heating, including temperature gradients the experiments did not measure.
- **Observings, claim side:** [observing] Rates were measured against light intensity and wavelength, with catalyst temperature from a thermal camera and thermocouples. The apparent activation energy fell with intensity, read as hot-carrier action [unverified; Zhou et al., Science 2018, 10.1126/science.aat6967]. Earlier claims: superlinear intensity dependence and isotope effects on Ag [unverified; Christopher, Xin, Linic, Nat. Chem. 2011, 10.1038/nchem.1032]; H2 dissociation on Au [unverified; Mukherjee et al., Nano Lett. 2013].
- **Observings, negation side:** [observing + model] A technical comment argued that thermal gradients, thermocouple placement and Arrhenius sensitivity can account for the data without hot carriers [unverified; Sivan, Baraban, Un, Dubi, Science 2019, 10.1126/science.aaw9367]; the original authors replied [unverified]. Methodological guides list experiments to separate the two [unverified; Baffou et al., Light Sci. Appl. 2020, 10.1038/s41377-020-00345-0].
- **Field's explaining:** [model] "Hot carriers" are electrons or holes outside the thermal distribution that transfer into adsorbate states. The usual diagnostics (non-Arrhenius intensity dependence, wavelength dependence, kinetic isotope effects) each have thermal alternatives.
- **Why hard:** the temperature at the active nanoparticle is not measured directly, and the exponential Arrhenius dependence magnifies small temperature errors. Both processes can coexist in varying shares. Illumination geometries differ between studies.
- **Standing in 2026:** open, moving toward case-by-case quantification with better thermometry [unverified].
- **What would settle it:** in situ nanoscale thermometry (anti-Stokes/Stokes Raman, luminescence) on the working particles; dark controls matched in temperature and gradient; quantum yields resolved by wavelength at constant absorbed power.
- **Main proponents:** hot carriers — Naomi Halas, Peter Nordlander, Suljo Linic, Phillip Christopher. Photothermal — Yonatan Sivan, Yonatan Dubi; Guillaume Baffou (methodology) [unverified].
- **Observing or explaining:** explaining.

### B21 · Dark oxygen production by seafloor polymetallic nodules
- **Claim:** In situ benthic-chamber incubations on polymetallic-nodule fields of the Clarion–Clipperton Zone (about 4,000 m depth) record net O2 production in darkness. Its origin is abiotic and linked to the nodules; the proposed mechanism is seawater electrolysis driven by potential differences on nodule surfaces.
- **Negation:** The recorded O2 rises are methodological artefacts (for example oxygen carried down with the lander, such as trapped air or oxygenated water, or optode drift), and no nodule-linked net O2 production occurs.
- **Observings, claim side:** [observing] Autonomous lander chamber incubations with O2 sensors over about two days showed O2 increases in many chambers. Ex situ measurements found surface potentials of up to about 0.95 V on nodules, and ship-based nodule incubations were run [unverified; Sweetman et al., Nat. Geosci. 2024, 10.1038/s41561-024-01480-8 (DOI typed from memory; fetch blocked)].
- **Observings, negation side:** [observing + model] Critics argued that the chamber method can introduce O2, and that the measured voltages are below the 1.23 V thermodynamic minimum for water splitting plus overpotential [unverified]. Some critics were affiliated with the deep-sea mining industry, which had partly funded the original fieldwork [unverified].
- **Field's explaining:** [model] "Geobattery" electrolysis is the authors' interpretation, separate from the O2 time series. A 2:1 H2 co-product would be expected and was not reported as measured [unverified].
- **Why hard:** abyssal in situ work is rare and costly. Chamber deployment can introduce gases. Biological and abiotic sources must be separated. Electrochemistry at 4 km (about 400 bar, 1–2 °C) is poorly characterised.
- **Standing as of 23 October 2026:** could not be checked in this session. By this researcher's prior knowledge the 2024 paper had not been retracted, and critiques were circulating or submitted as formal comments in 2024–2025. Treat as open and contested [unverified].
- **What would settle it:** independent replication with redesigned, gas-free chambers carrying several independent O2 sensors; isotopically labelled water (H2 18O) to trace the oxygen source; nodule-free and inert-mimic controls; measurement of any H2 co-production.
- **Main proponents:** claim — Andrew Sweetman, Franz Geiger. Critiques — deep-sea scientists including mining-industry-affiliated authors; names not checked [unverified].
- **Observing or explaining:** observing (did net O2 production occur?).

### B22 · Langmuir–Hinshelwood vs Eley–Rideal in plasma-assisted ammonia synthesis
- **Background (seen):** [convention] Langmuir–Hinshelwood (LH): both reactants adsorb and react on the surface. Eley–Rideal (ER): an adsorbed species reacts directly with one arriving from the fluid. Most heterogeneously catalysed reactions are said to follow LH — https://en.wikipedia.org/wiki/Heterogeneous_catalysis. [observing] In model systems, ER and "hot-atom" pathways are established by molecular beams; for example, gas-phase H atoms abstracting adsorbed H or D on Cu(111) give products with high translational energy [unverified; Rettner, PRL 1992; Rettner and Auerbach, Science 1994].
- **Claim:** In dielectric-barrier-discharge plasma ammonia synthesis over metal catalysts near ambient temperature, a substantial fraction of NH3 forms through ER steps between gas-phase radicals (N, H, NHx) and adsorbed species.
- **Negation:** Under the same conditions, NH3 forms mainly through LH steps among adsorbed species, the plasma acting chiefly by vibrationally exciting N2 to ease its dissociative adsorption.
- **Observings:** [observing] Plasma-catalytic NH3 rates across metals shifted the volcano toward weaker binders, read through vibrational excitation (an LH-type surface route) [unverified; Mehta et al., Nat. Catal. 2018, 10.1038/s41929-018-0045-1]. [simulation] Microkinetic plasma models give radical ER steps a significant share [unverified; Bogaerts group].
- **Why hard:** plasmas hold radicals, ions and excited molecules at once. Surface coverages under plasma are not measured. ER and hot-atom routes are hard to tell apart outside beam experiments.
- **Standing in 2026:** open [unverified].
- **What would settle it:** in situ surface IR under plasma at controlled radical densities; isotopic labelling separating gas-phase N atoms from surface N; product energy distributions.
- **Main proponents:** vibrational/LH — William Schneider, Jason Hicks. Radical/ER — Annemie Bogaerts [unverified].
- **Observing or explaining:** explaining.

### Inferences and gaps (area 5)
- [Inference] B21 is the only binary in this file where the observing itself, not its explaining, is contested. Its standing depends on replication rather than on modelling.
- [Gap] The 2025–2026 history of B21 (formal comments, replies, new expeditions) and of B20 could not be checked, and both need verification before the report is written.

## 6. Batteries and energy chemistry

### Takeaway
The battery and photovoltaic binaries are about buried interfaces seen through indirect signals. Ion migration for perovskite hysteresis is the closest to settled; dendrite initiation and SEI phase identity are narrowing with operando imaging and cryo-EM.

### B23 · Lithium penetration in ceramic electrolytes: mechanical cracking first, or nucleation by electronic conduction?
- **Claim:** In Li-metal cells with ceramic electrolytes (Li6PS5Cl, LLZO) at practical current densities, dendrite initiation starts with cracks at the anode/electrolyte interface. Cracks open by spallation as Li fills surface defects, propagate ahead of the Li, and Li then fills them.
- **Negation:** Initiation occurs when Li nucleates inside the electrolyte (at grain boundaries or pores) because of its finite electronic conductivity; isolated deposits then connect into a short without needing cracks from the interface.
- **Observings, claim side:** [observing] Operando X-ray tomography and microscopy: dendrites initiated as subsurface spallation cracks at the interface, and crack propagation ran ahead of Li filling [unverified; Ning et al., Nature 2023, 10.1038/s41586-023-05970-4]. Voids formed on stripping were linked to dendrites on plating [unverified; Kasemchainan et al., Nat. Mater. 2019, 10.1038/s41563-019-0438-9]. Metal penetration was described as crack-driven [unverified; Porz et al., Adv. Energy Mater. 2017].
- **Observings, negation side:** [observing] Time-resolved neutron depth profiling found Li deposition inside LLZO and Li3PS4, attributed to electronic conductivity [unverified; Han et al., Nat. Energy 2019, 10.1038/s41560-018-0312-z].
- **Field's explaining:** [model] Mechanical-stability criteria (shear-modulus arguments) [unverified; Monroe and Newman, J. Electrochem. Soc. 2005] vs electronic-leakage models.
- **Why hard:** the interfaces are buried. Tomography resolution is coarser than nucleation length scales. Both routes may operate, depending on electronic conductivity, microstructure, stack pressure and current.
- **Standing in 2026:** narrowing toward mechanical initiation at interfacial defects in sulfide and garnet electrolytes at room temperature, with electronic leakage important in some materials [unverified].
- **What would settle it:** nanoscale operando imaging co-registered with electronic-conductivity measurements on the same samples; electrolytes with engineered electronic conductivity at fixed mechanical properties.
- **Main proponents:** mechanical — Peter Bruce, Yet-Ming Chiang, Jeff Sakamoto. Electronic — Chunsheng Wang (Han et al.) [unverified].
- **Observing or explaining:** explaining.

### B24 · Is LiH a significant phase in the solid–electrolyte interphase on lithium metal?
- **Claim:** The SEI on Li metal in common carbonate (and some ether) electrolytes contains LiH as a significant crystalline or nanocrystalline phase.
- **Negation:** Signals assigned to LiH come from misassignment (LiF has almost the same rocksalt lattice spacing) or from beam damage, and LiH is absent or negligible.
- **Observings:** [observing] Cryo-STEM with spectroscopy mapped dendrites and SEI and assigned LiH-containing phases [unverified; Zachman et al., Nature 2018, 10.1038/s41586-018-0397-3]. Synchrotron diffraction and pair-distribution analysis with titration identified both LiH and nanocrystalline LiF and warned that their similar lattice constants cause misassignment in electron microscopy [unverified; Shadike et al., Nat. Nanotechnol. 2021]. Cryo-EM resolved SEI nanostructure (mosaic and multilayer motifs) [unverified; Li et al., Science 2017, 10.1126/science.aam6014]. SEI swelling in electrolyte was captured by cryo-EM [unverified; Zhang et al., Science 2022].
- **Field's explaining:** [model] Peled's interphase concept and later mosaic picture [unverified; Peled, J. Electrochem. Soc. 1979, 10.1149/1.2128859]. [convention] Phase identity is assigned from d-spacings, which here are nearly degenerate.
- **Why hard:** near-identical d-spacings; beam and air sensitivity; small quantities; reaction during sample washing.
- **Standing in 2026:** narrowing toward LiH being present in some electrolytes; its functional role is open [unverified].
- **What would settle it:** combined cryo-EM with Li K-edge fine structure distinguishing hydride from fluoride; titration gas analysis (H2 or HD from LiH); 1H and 7Li solid-state NMR on the same samples.
- **Main proponents:** LiH present — Lena Kourkoutis, Lynden Archer, Xiao-Qing Yang and Enyuan Hu (Shadike), Betar Gallant. Sceptics not identified [unverified].
- **Observing or explaining:** observing.

### B25 · Perovskite solar-cell hysteresis: ion migration vs ferroelectric polarisation
- **Claim:** Current–voltage hysteresis in metal-halide perovskite cells (dependent on scan rate and direction, seconds-scale, sensitive to preconditioning) comes from mobile ionic defects, chiefly iodide vacancies, redistributing and modulating interfacial recombination.
- **Negation:** It comes from switching of ferroelectric polarisation in the perovskite absorber (e.g., MAPbI3).
- **Observings, claim side:** [observing] Hysteresis depended on scan rate, direction and preconditioning by light or bias [unverified; Snaith et al., J. Phys. Chem. Lett. 2014, 10.1021/jz500113x; Unger et al., Energy Environ. Sci. 2014]. [simulation + observing] A calculated iodide-vacancy migration barrier of about 0.6 eV agreed with kinetic data [unverified; Eames et al., Nat. Commun. 2015, 10.1038/ncomms8497]. [simulation] Drift–diffusion models with slow ions reproduced hysteresis [unverified; Richardson et al., Energy Environ. Sci. 2016]. [observing] Transient photovoltage showed ion migration even in cells with little hysteresis, implicating interfacial recombination [unverified; Calado et al., Nat. Commun. 2016, 10.1038/ncomms13831].
- **Observings, negation side:** [model] Molecular ferroelectric contributions were proposed [unverified; Frost, Butler, Walsh, APL Mater. 2014]. [observing] Tetragonal MAPbI3 was reported to be ferroelectric [unverified; Rakita et al., PNAS 2017, 10.1073/pnas.1702429114]. Striped domains seen by piezoresponse force microscopy were later attributed to ferroelasticity with chemical segregation [unverified; Liu et al., Nat. Mater. 2018].
- **Field's explaining:** [convention] "Ferroelectric" requires switchable remanent polarisation shown by leakage-free P–E loops. Piezoresponse signals can come from electrochemical strain, which is ionic, so the membership test itself is contested.
- **Why hard:** ions and polarisation both produce slow, capacitor-like responses, and probes of ferroelectricity are confounded by ion motion.
- **Standing in 2026:** largely settled that ion migration with interfacial recombination causes hysteresis. Whether MAPbI3 is ferroelectric remains contested but is treated as secondary [unverified].
- **What would settle the residue:** suppressing ion migration (composition, passivation, temperature) while monitoring polarisation, to show hysteresis disappears with polarisation unchanged; definitive switching measurements on leakage-free samples.
- **Main proponents:** ions — Aron Walsh, Piers Barnes, Brian O'Regan, Saiful Islam, Henry Snaith. Ferroelectricity in MAPbI3 — Yevgeny Rakita, David Cahen, Leeor Kronik; Alexander Colsmann (domains) [unverified].
- **Observing or explaining:** explaining.

### Inferences and gaps (area 6)
- [Inference] B23 and B24 repeat area 1's pattern: the state seen after disassembly or cryo-fixation is asked to stand for the working interface.
- [Gap] No battery or perovskite source could be read this session; all entries need checking.

## Further candidates (one line each; all [unverified])
- Fe–N–C ORR catalysts: FeN4 single sites (the Mössbauer D1/D2 assignments) vs Fe clusters as the working species.
- NiFe oxyhydroxide OER: Fe as the turnover site vs Ni as the site with Fe as modifier (Friebel et al., JACS 2015; Trotochaud et al., JACS 2014).
- Cu-SSZ-13 NH3-SCR: mobile Cu–ammine pairs forming transient dimers as the O2-activation site (Paolucci et al., Science 2017) vs static framework Cu.
- Au/TiO2 CO oxidation: Au–TiO2 perimeter vs small bilayer Au clusters as the active site.
- Hydrogen spillover across non-reducible supports at catalytically relevant rates vs only on reducible supports (Karim et al., Nature 2017).
- Alkaline HER: adsorbed OH promotes the Volmer step (bifunctional) vs OH plays no part.
- B9b: cation action on *CO2− through long-range field vs short-range coordination.
- Liquid-electrolyte Li dendrites: transport limitation (Sand's time) vs SEI or mechanical initiation below the limiting current (Bai et al., Energy Environ. Sci. 2016).
- LiF-rich SEI: causally beneficial vs a correlate of other solvation-structure changes.
- pMMO: tricopper cluster (Chan) vs mononuclear CuD.
- Nitrogenase crystal structures with an N2-derived species at belt-sulfur sites: genuine intermediate vs crystallographic misassignment.
- Water–gas shift on Cu or Pt: redox (surface O) vs associative (carboxyl or formate) mechanism.
- Strong metal–support interaction: the encapsulating oxide layer as a participant vs a blocker.
- CO2 reduction C–C coupling: *CO–*CO dimerisation vs *CO–*CHO coupling as the selectivity-setting step.
- Electrochemical restructuring of single-site Cu–N–C catalysts into clusters during CO2 reduction: reversible cluster formation as the active state vs intact single sites.

## Verification ledger and overall gaps
- **Read in this session (content seen):** Bhowmick et al. 2023 (PDF and abstract pages); news summary of Greife et al. 2023; Lukoyanov et al. 2023; Hickey 2022 teaching chapter; Wikipedia "Nitrogenase" (mechanism text and reference list); Wikipedia "Heterogeneous catalysis" (Sabatier, scaling, LH/ER text and reference list); Govindarajan et al. 2018 (abstract); Shinkarev 1996 (abstract); Crespilho 2025 preprint. References "seen as reference" were read only as entries in those lists.
- **Titles only:** the 2021 Ni-based OER Mars–van Krevelen paper (search listing).
- **Everything else [unverified]:** including every DOI inside an [unverified] mark (typed from memory), all proponent lists not drawn from seen author lines, and every 2024–2026 standing except those quoted from seen sources.
- **Highest-priority checks for the report writer:** B21 dark oxygen 2025–2026 (formal comments, replies, replications, retraction status); B20 plasmonic (post-2019 thermometry studies); B2 Cu/ZnO (2022–2026 operando work); B18 pMMO and B19 hydrogenase (2024–2026); B12 retraction tally; B13–B15 nitrogenase cryo-EM under turnover.
- **Why the gaps exist:** search budget exhausted; allowlist blocked publisher and DOI hosts; PubMed Central browser check; hourly fetch cap.
