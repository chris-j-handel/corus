# Frontiers of phase transitions, nucleation, crystallization, glass formation and self-assembly: frontier binaries (gathered 23 Oct 2026)

## Key gathered points

- **Source status (read first).** No source could be opened: the shared search budget was spent before my first query, and the proxy blocked doi.org and Crossref. All citations come from memory; every DOI is marked [unverified]. Standings after 2023 are least certain.
- **Labels:** [obs] observing · [recon] reconstruction from observings · [conv] convention or definition · [model] model construct · [sim] simulation.
- **There are 25 binaries (B1–B25). The most consequential are:**
  - prenucleation clusters in calcium carbonate (B1);
  - the Kauzmann entropy crisis (B10);
  - random first-order transition theory vs dynamic facilitation (B12);
  - condensates as true phase separation (B24);
  - crystal structure prediction (B7);
  - disappearing polymorphs (B8);
  - the triphenyl phosphite liquid–liquid transition (B15);
  - quasicrystal stabilisation (B21);
  - the onset of ice premelting (B19);
  - hard-sphere nucleation rates (B25).
- **Recurring pattern.** The two sides usually share the raw data: titration, scattering, cryo-TEM snapshots, extrapolated calorimetry. They split over one of two things:
  - a reference state or class criterion: cluster vs ion pair, liquid vs nanocrystal, "living", polymorph vs computed minimum, phase vs network, time crystal vs limit cycle;
  - an extrapolation beyond what can be measured: T_K, T0, the spinodal.
- **Settled:**
  - the hexatic phase in 2D melting, with a first-order liquid–hexatic step for hard disks (simulations 2011–2015, colloids 2017);
  - the fluid–liquid transition in phosphorus (2000, 2004);
  - entropy-driven freezing of hard spheres (1957, 1986);
  - amorphous carbonate precursors in sea urchins (2008) and corals (2017);
  - the existence of ultrastable vapour-deposited glasses (2007);
  - pathway complexity in supramolecular polymerisation (2012);
  - jamming as distinct from the glass transition for ideal spheres (2010–2017);
  - Ostwald's rule as a tendency, not a law.
- **Narrowing:**
  - multi-step nucleation of proteins, which depends on the system;
  - facilitation as how relaxation spreads near Tg (2022 simulations);
  - crystal structure prediction: generating structures is largely solved, ranking is contested after the 2024 blind test;
  - an amorphous precursor in zebrafish bone.
- **Open:**
  - cluster stability;
  - T_K and whether relaxation times diverge;
  - fragility;
  - the triphenyl phosphite and silicon transitions;
  - the onset of ice premelting (2024 AFM adds data);
  - quasicrystal stability (2025 DFT favours energy) [unverified];
  - condensates in cells;
  - the hard-sphere rate gap;
  - the mechanisms of disappearing polymorphs;
  - time crystals in NMR.
- **For the project.** Where an unstated membership criterion decides a dispute, the entry names it.

## Q1 Nucleation: classical vs non-classical pathways, prenucleation clusters (PNCs), oriented attachment, amorphous precursors, Ostwald's rule, spinodal assignments

### Takeaway
Since about 2008 the field has moved from one classical picture (one step, sharp interface, capillarity) to a menu of pathways. These include dense-liquid and amorphous intermediates and the attachment of particles. Amorphous precursors, mesoscopic protein clusters and oriented-attachment events are reproduced observings. How to explain them is contested, most sharply for calcium carbonate (CaCO3) PNCs. All Q1 references are [unverified].

### Cited Findings (frontier binaries)

**B1. CaCO3 PNCs: stable solute species or not**
- **Claim:** Dilute aqueous CaCO3 at room temperature and pH 9–10, under- or supersaturated, holds a population of multi-ion clusters about 1–2 nm across. They are thermodynamically favoured over free ions and ion pairs, have no phase interface, and lie on the nucleation pathway.
- **Negation:** In the same solutions, free ions, ion pairs and short-lived small complexes account for all speciation. Association beyond the ion pair is unfavourable, as classical solution chemistry expects.
- **Observings for:**
  - Gebauer, Völkel & Cölfen 2008, Science 322:1819, doi:10.1126/science.1164271.
    - A Ca-selective electrode tracked free calcium as CaCl2 was dosed into carbonate buffer at constant pH. Before nucleation, more Ca was bound than ion-pair constants predict [obs].
    - Analytical ultracentrifugation detected species a few nm across [obs]. Calling them "clusters" is [recon].
  - Pouget et al. 2009: cryo-TEM showed features 0.6–1 nm across before amorphous calcium carbonate (ACC) formed under a template [obs]. Their identity as PNCs is [recon]. doi:10.1126/science.1169434.
  - Demichelis et al. 2011: force-field MD found chain-like ionic polymers ("DOLLOPs") with favourable free energy [sim]. doi:10.1038/ncomms1604.
  - Avaro et al. 2023: in situ SAXS, doi:10.1021/acs.jpclett.3c00585 [details not recalled].
- **Observings against:**
  - Smeets et al. 2017: cryo-TEM, titration and simulation data fit classical nucleation of a dense amorphous phase plus ordinary ion association. doi:10.1073/pnas.1700342114.
  - Henzler et al. 2018: Ca K-edge X-ray absorption of supersaturated solutions, with ab initio and classical MD. The coordination fits hydrated ions and ion pairs, and no cluster population was detected [obs+sim]. doi:10.1126/sciadv.aao6283.
- **Why hard:**
  - The species are under 2 nm, dilute and fluxional.
  - Every method carries model assumptions: activity models, sizing of tiny species, cryo-TEM artefacts, and force fields where a few kJ/mol flips the verdict.
  - "Stable" needs a stated reference state, and classical theory also allows sub-critical clusters [conv].
- **Standing in 2026:** Open and polarised. Gebauer, Raiteri, Gale & Cölfen 2018 set out both views (doi:10.2475/09.2018.05). Work from 2024–2026 was not checked.
- **What would settle it:**
  - A model-independent in situ size distribution of solute species, from undersaturation to nucleation onset (quantitative SAXS/WAXS, diffusion NMR), with activities measured independently. The test is whether species of more than three ions follow ion-pair mass action.
  - Association free energies computed ab initio.
- **Proponents:**
  - Claim: D. Gebauer, H. Cölfen, M. Kellermeier. J. Gale and P. Raiteri supply simulations and take a middle position.
  - Negation: J. De Yoreo, N. Sommerdijk, P. Smeets, K. Henzler, C. Mundy, G. Schenter.
- **Type:** Both. The observing is whether a distinct population exists. The explaining is whether the association is favourable or classical. The class criterion at issue is what separates a "cluster species" from an ion pair or a sub-critical nucleus.

**B2. Protein crystal nucleation: inside dense precursors (two-step) or directly from solution**
- **Claim:** Globular proteins (lysozyme, glucose isomerase, ferritin) crystallising outside the metastable liquid–liquid region form crystalline nuclei inside pre-existing mesoscopic dense clusters.
- **Negation:** Under the same conditions, nuclei form directly from the dilute solution. The clusters are bystanders, or at most sites for heterogeneous nucleation.
- **Observings for:**
  - ten Wolde & Frenkel 1997: near a metastable critical point, nuclei formed inside dense droplets [sim]. doi:10.1126/science.277.5334.1975.
  - Vekilov group: dynamic light scattering, Brownian microscopy and AFM found clusters of 50–500 nm at tiny volume fraction. Their size did not depend on protein concentration [obs]. Calling them a "dense liquid" is [recon]. doi:10.1039/C0NR00628A.
  - Van Driessche et al. 2018: glucose isomerase nucleated in dense precursors, and additives set the polymorph. doi:10.1038/nature25971.
  - Houben et al. 2020: cryo-STEM tomography of ferritin showed order building up inside dense precursors [obs of snapshots]. The time order is [recon]. doi:10.1038/s41586-020-2104-4.
- **Observings against:** Sleutel et al. 2014 used molecular-resolution AFM to watch 2D nucleation on glucose isomerase crystal faces. It fitted classical expectations [obs]. Nat Commun 5:5598, doi:10.1038/ncomms6598.
- **Why hard:**
  - Nucleation is rare and involves only 10–100 molecules.
  - Snapshots carry no time order, and the electron dose in liquid-cell TEM can cause aggregation.
  - A dense liquid and an amorphous solid are hard to tell apart.
  - The two-step free-energy landscape [model] has several free parameters.
- **Standing in 2026:** Narrowing toward pluralism that depends on conditions. Multi-step pathways are common in proteins. How general they are, and what the precursor is, remain open.
- **What would settle it:**
  - Low-dose in situ tracking of single clusters and crystal births together.
  - Nucleation rate against cluster number density: the two-step picture predicts proportionality.
- **Proponents:** Claim: P. Vekilov, P. R. ten Wolde, D. Frenkel, A. Van Driessche. Classical sufficiency in specific cases: M. Sleutel.
- **Type:** An observing (where do nuclei form?) inside an explaining (which landscape?).

**B3. Oriented attachment (OA): alignment before or after contact**
- **Claim:** In ferrihydrite or ZnO nanocrystals undergoing OA in water, particles align their lattices before touching, guided by direction-specific forces across gaps of about 1 nm.
- **Negation:** In the same systems, alignment happens only at or after contact, as touching particles rotate. No orientation-specific force acts beyond the last solvent layer.
- **Observings:**
  - Penn & Banfield 1998: HRTEM of coarsened anatase showed interfaces with continuous lattices and dislocations [obs]. OA as the mechanism is [recon]. doi:10.1126/science.281.5379.969.
  - Li et al. 2012: liquid-cell TEM of ferrihydrite. Particles rotated and touched briefly until their lattices matched, then jumped into contact from under 1 nm [obs]. Direction-specific Coulomb forces are the [model]. doi:10.1126/science.1219643.
  - Zhang et al. 2017: AFM forces between ZnO surfaces depend on orientation [obs]. doi:10.1038/s41467-017-00844-8.
  - Review: De Yoreo et al. 2015, doi:10.1126/science.aaa6760.
- **Why hard:**
  - The gaps are a few nm.
  - Beam radiolysis and charging alter the forces.
  - 2D projections hide rotation out of the image plane.
  - Double-layer theory fails below 1 nm.
- **Standing in 2026:**
  - OA as an event is settled (1998–2012).
  - Before vs after contact depends on the system and is open as a general account.
  - How much OA contributes to natural mineral growth is a separate open observing.
- **What would settle it:** Low-dose 3D liquid-cell imaging at millisecond resolution, with orientation-resolved force–distance curves measured in the same solution.
- **Proponents:** Before contact: J. De Yoreo, J. Banfield, K. Rosso, D. Li. After contact: no organised camp [unverified].
- **Type:** Explaining.

**B4. Amorphous calcium phosphate (ACP) as the first mineral of bone formed in vivo**
- **Claim:** In vertebrate bone formed in vivo, mineral is first deposited as ACP, which then becomes apatite.
- **Negation:** In the same tissue, apatite forms directly, possibly via octacalcium phosphate. ACP is absent or minor, and reported ACP is an artefact of preparation or of the beam.
- **Observings:**
  - Mahamid et al. 2008: cryo-SEM, electron diffraction and FTIR of zebrafish fin rays found abundant ACP in new bone [obs]. doi:10.1073/pnas.0803354105.
  - Grynpas & Omelon 2007 argued that later X-ray work did not confirm the 1960s claims of ACP in bone, and that apatite crystals 2–5 nm across can look amorphous [recon]. doi:10.1016/j.bone.2007.04.173.
  - Settled anchors:
    - ACC precedes calcite in sea-urchin spicules (Politi et al. 2008, doi:10.1073/pnas.0806604105).
    - Coral skeletons form from ACC particles (Mass et al. 2017, doi:10.1073/pnas.1707890114).
- **Why hard:**
  - "Amorphous" means no order at the probe's coherence length, so the label depends on the method [conv].
  - ACP converts within minutes to hours.
  - Drying and staining can destroy ACP or create it.
- **Standing in 2026:** Narrowing toward the claim for fin rays studied by cryo-methods. Open for mammalian lamellar bone.
- **What would settle it:** A cryo-preserved in vivo time series at the mineralisation front (cryo-EELS, 4D-STEM, XANES), with pulse-chase labelling.
- **Proponents:**
  - Claim: S. Weiner, L. Addadi, J. Mahamid, N. Sommerdijk.
  - Negation: M. Grynpas, S. Omelon; historically M. Glimcher.
- **Type:** Observing.

**B5. Ostwald's step rule: law or tendency**
- **Claim (law):** A system leaving an unstable state first forms the phase closest in free energy to the parent, then steps down through progressively more stable phases.
- **Negation (tendency):** The first phase is whichever nucleates and grows fastest. It is often metastable, but not systematically, and the stable phase often forms directly.
- **Observings:**
  - Ostwald 1897: metastable forms often appear first. doi:10.1515/zpch-1897-2233.
  - Calorimetry shows an energy staircase: ACC above vaterite, above aragonite, above calcite [obs] (Radha et al. 2010, doi:10.1073/pnas.1009959107).
  - Nielsen et al. 2014: liquid-cell TEM showed calcite, vaterite and aragonite forming both directly and via ACC, in one experiment [obs]. doi:10.1126/science.1254051.
  - McHale et al. 1997: γ-Al2O3 is more stable than α-Al2O3 at high surface area [obs]. This gives a size-dependent basis for the steps [model]. doi:10.1126/science.277.5327.788.
- **Why hard:**
  - The rule is imprecise: which phase, and "closest" in what sense?
  - The interfacial energies of nuclei are unknown.
  - Additives and surfaces reorder outcomes.
  - Reported cases are a selected sample.
- **Standing in 2026:** Settled as a heuristic, usually explained by the lower interfacial energy of less stable phases. A theory that predicts which phase forms is open.
- **What would settle it:** Measure the interfacial free energies and nucleation rates of the competing phases in one system, and use them to predict the outcome in advance.
- **Proponents:** Size-dependent thermodynamics: A. Navrotsky. Kinetic and multiple-pathway view: J. Threlfall, J. De Yoreo [unverified attribution].
- **Type:** Explaining: the status of a generalisation. The sequence in any one system is a reproducible observing.

**B6. Dense liquid from supersaturated CaCO3: spinodal or nucleation**
- **Claim:** At high supersaturation, CaCO3 solutions, and polymer-induced liquid-precursor systems, separate into a solute-rich liquid by spinodal decomposition, with no barrier. The liquid then dehydrates to ACC.
- **Negation:** Under the same conditions, the dense phase forms by nucleation and growth over a finite, possibly small, barrier.
- **Observings:**
  - Faatz, Gröhn & Wegner 2004: light scattering read as liquid–liquid demixing [obs+recon]. Adv Mater 16:996.
  - Bewernitz et al. 2012: diffusion NMR found slow, liquid-like species [obs]. doi:10.1039/C2FD20080E.
  - Wallace et al. 2013: MD plus an analytical model proposed a liquid–liquid binodal [sim+model]. doi:10.1126/science.1230915.
  - Smeets et al. 2015: liquid-cell TEM showed ACC nucleating through ion binding in a polymer matrix [obs]. doi:10.1038/nmat4193.
- **Why hard:**
  - The spinodal signature is a structure-factor peak at a fixed wavevector that first grows and then coarsens. Dehydration within milliseconds to seconds masks it.
  - Electron beams promote precipitation.
  - MD verdicts depend on the force field.
  - A sharp spinodal exists only in mean-field theory [model].
- **Standing in 2026:** Open. Several methods support a transient, hydrated, liquid-like phase; how it forms is unresolved.
- **What would settle it:** Stopped-flow, time-resolved SAXS/USAXS across a range of supersaturations, distinguishing growth at a fixed wavevector from isolated droplets, with the composition of the dense phase measured.
- **Proponents:**
  - Spinodal or binodal: D. Gebauer, H. Cölfen, L. Gower, G. Wegner (historical), with MD by P. Raiteri and J. Gale.
  - Nucleation: P. Smeets, N. Sommerdijk.
  - J. De Yoreo co-authored both the 2013 and the 2017 papers.
- **Type:** Explaining, with an observing core: is there a liquid at all?

### Inferences
- "Classical vs non-classical" bundles three questions:
  - Which intermediates are present?
  - What is the free-energy landscape?
  - Does the capillarity approximation hold?
- One sample can follow several pathways at once (Nielsen 2014), so proper binaries are specific to a system and its conditions.
- Class criteria to state:
  - "cluster species": free energy below a dissociated reference, at stated activities;
  - "phase": an interface plus bulk properties;
  - "amorphous": no order at the probe's coherence length;
  - "spinodal": local instability of the homogeneous state.

### Gaps
- No source from 2023–2026 could be opened. Unknown as a result:
  - whether B1–B6 shifted, for example through ML-potential or cryo-EM speciation studies;
  - what recent reviews by De Yoreo, Gebauer or Vekilov conclude.
- The Avaro et al. 2023 result is not recalled in detail.

## Q2 Polymorphism: crystal structure prediction (CSP), disappearing and late-appearing polymorphs, thermodynamic vs kinetic control

### Takeaway
- CSP now routinely generates the observed structures of small rigid molecules.
- Ranking improved over the 6th (2016) and 7th (2024) blind tests. It is still disputed for flexible, multicomponent and Z′>1 targets.
- Disappearing polymorphs are conventionally blamed on seeding, which is rarely proved in any given case.
- Whether the observed form reflects thermodynamic or kinetic control varies from case to case.
- All Q2 references are [unverified].

### Cited Findings (frontier binaries)

**B7. Is CSP reliable?**
- **Claim:** For small, rigid to moderately flexible organic molecules, current best CSP ranks the observed polymorph among the top few computed structures for a large majority of blind targets.
- **Negation:** For the same classes of target under blind conditions, the observed form falls outside the top few, or is not generated at all, often enough that CSP cannot be relied on.
- **Scope:** "Reliable" needs a stated threshold: top-1, top-10, or generated at all [conv].
- **Observings:**
  - Cambridge Crystallographic Data Centre blind tests have run since 1999. Early success was low (Lommerse et al. 2000, Acta Cryst B 56:697).
  - 4th test: a dispersion-corrected DFT approach ranked all four targets first (Neumann, Leusen & Kendrick 2008, doi:10.1002/anie.200704247).
  - 6th test (25 groups; five targets, including a salt hydrate and a large flexible molecule): every structure was generated by at least one group, but ranking was uneven. Reilly et al. 2016, doi:10.1107/S2052520616007447.
  - 7th test (seven targets, including flexible drug-like and multicomponent systems): Hunnisett et al. 2024, doi:10.1107/S2052520624007492 (generation) and doi:10.1107/S2052520624008679 (ranking). Success rates not recalled.
- **Why hard:**
  - Polymorph energy gaps are a few kJ/mol, comparable to the error of DFT (Nyman & Day 2015, doi:10.1039/C5CE00045A).
  - Entropy and kinetics decide what actually forms.
  - The search space grows with flexibility and Z′.
  - Computed landscapes contain more minima than there are known forms. Finite-temperature MD merges many of them (Francia et al. 2020, doi:10.1021/acs.cgd.0c00918).
- **Standing in 2026:** Narrowing. Generation is largely solved for small molecules; ranking for drug-like targets is contested. Claims from 2025 of large-scale commercial validation were not checked.
- **What would settle it:** A prospective blind set of more than 50 targets, with:
  - a pre-registered criterion, for example top-3 by free energy at 300 K;
  - exhaustive experimental screens, so that a "miss" cannot be an undiscovered form.
- **Proponents:**
  - Optimistic: M. Neumann, G. Day, A. Tkatchenko, G. Beran, industrial groups.
  - Cautious, kinetics first: J. Bernstein, A. Cruz-Cabeza. S. L. Price takes a measured view [unverified characterisations].
- **Type:** Observing (the track record), feeding an explaining: is thermodynamic ranking enough?

**B8. Disappearing polymorphs: always seeding?**
- **Claim:** Every documented disappearing polymorph is caused by seeds or heteronucleants of the new form, including degradation products and airborne microcrystals. A disappearing polymorph is a once-reproducible form that can no longer be made after a new form appears.
- **Negation:** At least one case occurred without any seed or heteronucleant of the new form. Candidate routes are an impurity change that inhibits the old form, a process change, or stochastic primary nucleation.
- **Observings:**
  - Dunitz & Bernstein 1995 compiled cases and attributed them to seeding. They noted that lost forms can usually be recovered. doi:10.1021/ar00052a005.
  - **Ritonavir.** Bauer et al. 2001, doi:10.1023/A:1011052932607.
    - It was marketed in 1996 as Form I, in semisolid capsules.
    - In 1998 a much less soluble Form II, with a different molecular conformation, appeared. Capsules failed dissolution and were withdrawn.
    - A degradation product was implicated as a possible heteronucleant.
  - **Rotigotine (Neupro patch).**
    - A new form crystallised in patches around 2007–2008, leading to a US recall (Rietveld & Céolin 2015, doi:10.1002/jps.24626).
    - A later CSP found that form low on the computed landscape (Mortazavi et al. 2019, doi:10.1038/s42004-019-0171-y).
  - Further cases and recoveries: Bučar, Lancaster & Bernstein 2015, doi:10.1002/anie.201410356.
- **Why hard:**
  - Seeds can be sub-micron, and contamination is rarely recorded.
  - Proving that no seeds were present is nearly impossible.
  - Whether a structurally related impurity counts as "seeding" is a matter of definition [conv].
- **Standing in 2026:** Open as a universal claim. Seeding is the default explanation, and recoveries of lost forms support it. No case has been shown to be seed-free.
- **What would settle it:** Controlled studies in seed-free facilities, comparing deliberate trace seeding with impurity changes alone, with airborne particles monitored.
- **Proponents:** Seeding: J. Dunitz, J. Bernstein. Impurity and process roles: industrial process chemists [unverified].
- **Type:** Explaining, with an observing core: were seeds present?

**B9. Is the first-obtained form usually the thermodynamically stable one?**
- **Claim:** Across polymorphic organic compounds crystallised under ordinary solution conditions, the first form obtained is usually the stable one under those conditions.
- **Negation:** Under the same conditions, the first form is metastable at least as often, i.e. under kinetic control.
- **Observings:**
  - For ritonavir and rotigotine, more stable forms appeared years into manufacture [obs].
  - ROY has more than ten polymorphs, several of them metastable yet easily obtained (Yu 2010, doi:10.1021/ar100040r).
  - New forms of ROY were obtained by heteronucleation (Lévesque, Maris & Wuest 2020, doi:10.1021/jacs.0c04434).
  - Cruz-Cabeza, Reutzel-Edens & Bernstein 2015 gave statistics on how often polymorphism occurs and on energy gaps, doi:10.1039/C5CS00227C [numbers not recalled].
- **Why hard:**
  - "First obtained" depends on the screening protocol.
  - The stability order can change with temperature (enantiotropy).
  - Databases record outcomes, not attempts.
- **Standing in 2026:** Open as a population claim. I found no checked statistic.
- **What would settle it:** A curated database of complete screens, recording the order of appearance and the stability at the crystallisation temperature as determined by slurry experiments.
- **Proponents:** No organised camps. Kinetic emphasis: Bernstein, Cruz-Cabeza, Threlfall. Landscape emphasis: Price, Day [unverified].
- **Type:** Observing (statistical).

### Inferences
- "Polymorphs of compound X" conventionally means experimentally isolated crystal structures of one composition. Solvates and hydrates are excluded as "pseudopolymorphs" [conv]. A computed minimum is a candidate member, not a member.
- Ritonavir and rotigotine show that the membership list grows over time. "Disappearance" changes which members can be produced, not which members exist.

### Gaps
- Not checked:
  - success rates in the 7th blind test;
  - ritonavir Form III, reported around 2022;
  - the commercial CSP validations of 2025;
  - statistics on whether first-appearing forms are stable.

## Q3 Glass: thermodynamic vs kinetic transition, fragility, ultrastable glasses, liquid–liquid transitions (LLTs), jamming

### Takeaway
The project already holds a glass-transition entry, so this section adds only what goes beyond it:
- swap Monte Carlo (from 2017);
- vapour-deposited glasses and ancient amber, which reach states below the glass transition (Tg);
- simulations from 2022 that favour facilitation;
- the LLT cases.

The core binaries remain open. The phosphorus LLT is settled; the triphenyl phosphite (TPP) and silicon LLTs are not. Jamming of ideal spheres is distinct from the glass transition.

### Cited Findings (frontier binaries)

**B10. Kauzmann entropy crisis: is there an ideal glass transition at finite temperature?**
- **Claim:** For fragile molecular glass-formers, the equilibrium configurational entropy reaches zero at a finite temperature T_K > 0. An ideal-glass transition lies there; experiments avoid it only for kinetic reasons.
- **Negation:** For the same liquids, the equilibrium configurational entropy stays positive at every T > 0. There is no thermodynamic transition at finite temperature.
- **Observings for:**
  - Kauzmann 1948 measured the excess entropy of liquid over crystal above Tg by calorimetry [obs]. Extrapolated, it reaches zero below Tg [recon]. doi:10.1021/cr60135a002.
  - T_K lies near the VFT divergence temperature T0. This is a correlation between two extrapolations.
  - Kinetic and thermodynamic fragility correlate [obs] (Martinez & Angell 2001, doi:10.1038/35070517).
  - Swap Monte Carlo equilibrates model liquids below the analogue of the experimental Tg [sim] (Ninarello et al. 2017, doi:10.1103/PhysRevX.7.021039). There, configurational entropy keeps falling, consistent with a T_K in 3D, but does not reach it [sim] (Berthier et al. 2017, doi:10.1073/pnas.1706860114).
- **Observings against:**
  - Stillinger 1988 argued that localised excitations keep the entropy positive [model]. doi:10.1063/1.454295.
  - In 2D swap simulations, configurational entropy extrapolates to zero only at T = 0 [sim] (Berthier et al. 2019, doi:10.1038/s41467-019-09512-3).
- **Why hard:**
  - T_K lies far below any temperature at which a liquid can be equilibrated.
  - Splitting entropy into configurational and vibrational parts depends on the model, and has no unique definition in finite dimensions [conv] (Berthier, Ozawa & Scalliet 2019, doi:10.1063/1.5091961).
- **Standing in 2026:** Open in 3D. Simulations weigh against a finite T_K in 2D (2019).
- **What would settle it:** Equilibrium configurational-entropy data in 3D that either reach the extrapolated T_K or level off before it, cross-checked against a growing point-to-set length.
- **Proponents:**
  - Claim: P. Wolynes, V. Lubchenko, G. Parisi, F. Zamponi; historically C. A. Angell.
  - Negation: F. Stillinger, D. Chandler, J. P. Garrahan, J. Dyre, G. McKenna.
  - L. Berthier's group reports results bearing on both sides.
- **Type:** Explaining, resting on an extrapolated observing. Refs [unverified].

**B11. Does the structural relaxation time diverge at finite temperature?**
- **Claim:** At equilibrium, the structural relaxation time τα (or the viscosity) diverges at a finite T0 > 0, as the VFT form implies.
- **Negation:** τα stays finite at every T > 0. Candidate forms include MYEGA, a parabolic law, or an Arrhenius crossover below Tg.
- **Observings:**
  - Hecksher et al. 2008: dielectric α-relaxation data for 42 liquids fit forms without a divergence as well as, or better than, VFT [obs+analysis]. doi:10.1038/nphys1050.
  - Mauro et al. 2009: viscosities of hundreds of oxide liquids fit MYEGA [obs+model]. doi:10.1073/pnas.0911705106.
  - Zhao, Simon & McKenna 2013: 20-million-year-old amber relaxes far faster than VFT extrapolation predicts [obs]. doi:10.1038/ncomms2809.
- **Why hard:**
  - Equilibrium data stop at τ ≈ 100–1000 s.
  - The candidate forms differ mainly below Tg, where samples are out of equilibrium.
  - Fictive temperatures are inferred, not measured [recon].
- **Standing in 2026:** Open. Accessible data lean toward no divergence, but none reach the decisive range.
- **What would settle it:** Equilibrium τα measured far below conventional Tg, in states shown to be equilibrium liquid (see B14).
- **Proponents:**
  - Divergence: the VFT tradition, RFOT.
  - Negation: J. Dyre, T. Hecksher, N. B. Olsen, J. P. Garrahan, J. Mauro, G. McKenna.
- **Type:** Observing. Refs [unverified].

**B12. Random first-order transition theory (RFOT) vs dynamic facilitation near Tg**
- **Claim:** Near Tg, relaxation proceeds by cooperative rearrangement of regions that grow as configurational entropy falls. Thermodynamics drives it (RFOT).
- **Negation:** Over the same range, relaxation proceeds mainly by facilitation: rare localised excitations relax and trigger their neighbours. No growing thermodynamic length is needed.
- **Scope:** Other accounts exist: hybrids, frustration-limited domains (G. Tarjus), elastic "shoving" models (J. Dyre), and mode-coupling theory at higher temperatures. The proper binary asks which mechanism dominates the relaxation observed near Tg.
- **Observings:**
  - Theory [model]: Kirkpatrick, Thirumalai & Wolynes 1989, doi:10.1103/PhysRevA.40.1045; Chandler & Garrahan 2010, doi:10.1146/annurev.physchem.040808.090405.
  - Berthier et al. 2005 estimated χ4 in experimental liquids. The number of dynamically correlated molecules grows on cooling [obs+recon]. doi:10.1126/science.1120714.
  - Albert et al. 2016: in glycerol and propylene carbonate, the fifth-order dielectric susceptibility grows faster than the third-order one. They read this as compact amorphous order [obs; reading model]. doi:10.1126/science.aaf3182.
  - Scalliet, Guiselin & Berthier 2022 simulated swap-equilibrated models out to about 30 ms of physical time. Relaxation began at sparse sites and spread by facilitation [sim]. doi:10.1103/PhysRevX.12.041028.
  - Guiselin et al. 2022 traced the dielectric "excess wing" to rare local relaxations [sim]. doi:10.1038/s41567-022-01508-z.
- **Why hard:**
  - Both theories reproduce super-Arrhenius dynamics and dynamic heterogeneity.
  - The quantities that would discriminate between them, the point-to-set length and the density of excitations, cannot be measured directly in molecular liquids.
- **Standing in 2026:** Open, narrowing. Since 2022, simulations at experimental timescales favour facilitation as the way relaxation spreads. Whether thermodynamics sets the rate of the elementary events is still open.
- **What would settle it:** Spatially resolved experiments that correlate local static order with local relaxation events over several decades of τ.
- **Proponents:**
  - RFOT: P. Wolynes, V. Lubchenko, G. Biroli, J.-P. Bouchaud, A. Cavagna.
  - Facilitation: J. P. Garrahan, T. Speck; supported by the 2022 Berthier-group simulations.
- **Type:** Explaining. Refs [unverified].

**B13. What sets fragility: configurational thermodynamics or elastic and vibrational properties?**
- **Claim:** Kinetic fragility, measured by the steepness index m at Tg, is set by how fast configurational entropy falls on cooling. This follows Adam–Gibbs (doi:10.1063/1.1696442) and RFOT.
- **Negation:** m is set by mechanical or vibrational quantities, such as the temperature dependence of the high-frequency shear modulus or the vibrational properties of the glass. The correlation with thermodynamics is secondary.
- **Observings:**
  - m correlates with thermodynamic fragility [obs] (Martinez & Angell 2001), but not for polymers [obs] (Huang & McKenna 2001, doi:10.1063/1.1348029).
  - m correlates with the temperature dependence of the nonergodicity factor measured by inelastic X-ray scattering [obs] (Scopigno et al. 2003, doi:10.1126/science.1089446).
  - m correlates with the Poisson ratio [obs] (Novikov & Sokolov 2004, doi:10.1038/nature02573). Each correlation has exceptions.
  - The strong–fragile classification is Angell 1995 [conv+obs], doi:10.1126/science.267.5206.1924. The shoving model is Dyre 2006, Rev Mod Phys 78:953 [model].
- **Why hard:**
  - Every link is a correlation among quantities that vary together, and each has exceptions.
  - m itself depends on the convention used to define Tg (100 s) [conv].
- **Standing in 2026:** Open.
- **What would settle it:** Tune configurational entropy and shear-modulus softening independently (by pressure, mixtures or simulation) and see which one tracks m.
- **Proponents:**
  - Thermodynamic: C. A. Angell (historical), R. Richert, P. Wolynes.
  - Elastic: J. Dyre, T. Hecksher.
  - Vibrational: T. Scopigno, G. Ruocco, V. Novikov, A. Sokolov.
- **Type:** Explaining. Refs [unverified].

**B14. Are ultrastable vapour-deposited glasses equivalent to the equilibrium liquid at low fictive temperature?**
- **Claim:** Glasses vapour-deposited onto substrates at about 0.8–0.85 Tg (indomethacin, TNB, ethylbenzene) occupy the same states as the equilibrium supercooled liquid at a fictive temperature far below Tg. They can therefore stand in for equilibrium below Tg.
- **Negation:** These glasses are structurally distinct from that liquid, so they cannot stand in for it. They have anisotropic packing and molecular orientation, and on heating they transform by a propagating front.
- **Observings:**
  - Swallen et al. 2007: compared with glass cooled from the liquid, the deposits had a higher calorimetric onset temperature, lower enthalpy and higher density [obs]. The low fictive temperatures are [recon]. doi:10.1126/science.1135795.
  - Singh, Ediger & de Pablo 2013 reproduced ultrastability in simulated deposition [sim]. doi:10.1038/nmat3521.
  - Pérez-Castañeda et al. 2014 found tunnelling two-level systems suppressed in the low-temperature heat capacity [obs]. doi:10.1073/pnas.1405545111.
  - Dalal et al. 2015: molecular orientation depends on substrate temperature, so many deposits are anisotropic [obs]. doi:10.1073/pnas.1421042112.
  - Reviews: Ediger 2017, doi:10.1063/1.5006265; Rodríguez-Tinoco et al. 2022, doi:10.1007/s40766-022-00029-y.
- **Why hard:**
  - Fictive temperature is defined as the point where a property meets the extrapolated liquid line [conv], and different properties can disagree.
  - Anisotropy varies with the molecule and the deposition rate.
- **Standing in 2026:** Narrowing. That ultrastable glasses exist has been settled since 2007. Equivalence holds for some properties in near-isotropic deposits, not for all.
- **What would settle it:** One isotropic sample whose density, enthalpy, modulus and relaxation time all give the same fictive temperature, on the extrapolated equilibrium lines.
- **Proponents:** M. Ediger, J. de Pablo, J. Rodríguez-Viejo, M. A. Ramos. The same groups raise the caution about anisotropy.
- **Type:** Observing, plus a convention for what counts as equivalent. Refs [unverified].

**B15. TPP: LLT or frustrated nanocrystallisation?**
- **Claim:** Supercooled TPP annealed at about 213–230 K (Tg ≈ 176 K, Tm ≈ 297 K) transforms by a first-order transition into a second non-crystalline phase, the "glacial" phase or liquid 2.
- **Negation:** Under the same conditions, the glacial phase is nanocrystallites or defective crystal in leftover liquid.
- **Observings:**
  - Tanaka, Kurita & Mataki 2004 used phase-contrast microscopy. They saw droplet-like growth at higher annealing temperatures and interconnected, spinodal-like patterns at lower ones [obs]. Reading this as an LLT is [recon]. doi:10.1103/PhysRevLett.92.025701.
  - Hédoux, Guinet, Descamps and co-workers used X-ray diffraction and Raman. They saw broadened Bragg-type features and read them as nanocrystals [obs+recon] [refs unverified].
  - Walton et al. 2020 (Wynne group) report that the local order of each liquid resembles a different crystal polymorph. doi:10.1021/jacs.0c01712 [details unverified].
  - Review: Tanaka 2020, doi:10.1063/5.0021045.
- **Why hard:**
  - Crystallisation competes with the transition.
  - Crystallites a few nm across sit near the coherence limit of diffraction.
  - Liquid 2 may itself partly crystallise.
- **Standing in 2026:** Open and contested. There are similar disputes over n-butanol and D-mannitol [unverified].
- **What would settle it:** Pair-distribution or 4D-STEM data showing no crystalline order at 1–2 nm in phase 2, together with reversion to liquid 1 without a melting endotherm.
- **Proponents:**
  - LLT: H. Tanaka, R. Kurita, K. Wynne.
  - Nanocrystals: A. Hédoux, Y. Guinet, M. Descamps.
- **Type:** Observing: is phase 2 a liquid? Refs [unverified].

**B16. Silicon: first-order LLT in deeply supercooled liquid at ambient pressure**
- **Claim:** Liquid Si supercooled to about 1060 K at about 0 GPa transforms by a first-order transition from a dense metallic liquid to a low-density, tetrahedral, semiconducting liquid.
- **Negation:** Under the same conditions, real Si changes only continuously before it crystallises or vitrifies.
- **Settled anchor (phosphorus):**
  - Katayama et al. 2000 used X-ray diffraction in a large-volume press at about 1 GPa and 1050 °C. They saw an abrupt change from a molecular P4 liquid to a polymeric liquid [obs]. doi:10.1038/35003143.
  - Coexistence of the two liquids was imaged in 2004 (Science 306:848).
  - The low-density phase lies above the liquid–gas critical point, so "fluid–liquid" is the exact term (Monaco et al. 2003, doi:10.1103/PhysRevLett.90.255701).
- **Observings:**
  - Sastry & Angell 2003 found a first-order LLT in Stillinger–Weber Si [sim]. doi:10.1038/nmat994.
  - Vasisht, Saw & Sastry 2011 placed a liquid–liquid critical point at negative pressure [sim]. doi:10.1038/nphys1993.
  - Beye et al. 2010 used femtosecond X-ray emission on laser-melted, undercooled Si and saw a change in the valence electronic structure [obs]. Reading this as an LLT is [recon]. doi:10.1073/pnas.1006499107.
  - Amorphous Si shows a pressure-induced change between low- and high-density forms [obs] (McMillan et al. 2005, doi:10.1038/nmat1458).
- **Why hard:**
  - At 1060 K, Si crystallises within nanoseconds.
  - Simulation verdicts depend on the interatomic potential.
  - The experiments are transient.
- **Standing in 2026:** Open.
- **What would settle it:** Ultrafast X-ray diffraction of hyperquenched films showing a bimodal density with hysteresis, plus agreement among machine-learning potentials with first-principles accuracy.
- **Proponents:** Claim: S. Sastry, C. A. Angell, P. McMillan. Sceptics not identified [unverified].
- **Type:** Observing. Refs [unverified].

**B17. Jamming vs the glass transition (frictionless spheres)**
- **Claim:** For frictionless spheres, the jamming point J (zero temperature and stress, volume fraction φ_J ≈ 0.64) is the glass transition approached along another axis of a single phase diagram [model] (Liu & Nagel 1998, doi:10.1038/23819).
- **Negation:** Jamming is a distinct transition. It occurs inside the glass, over a range of densities (the "J-line"), above the onset of dynamical arrest at about 0.58.
- **Observings:**
  - Critical scaling at J [sim] (O'Hern et al. 2003, doi:10.1103/PhysRevE.68.011306).
  - Mean-field theory [model] (Parisi & Zamponi 2010, doi:10.1103/RevModPhys.82.789).
  - Glass rheology and jamming rheology separated [sim] (Ikeda, Berthier & Sollich 2012, doi:10.1103/PhysRevLett.109.018301).
  - Review: Charbonneau et al. 2017, doi:10.1146/annurev-conmatphys-031016-025334.
- **Standing in 2026:** The negation is settled for ideal spheres in simulation and theory (2010–2017). How real emulsions, foams and grains map onto it is open.
- **Type:** Explaining. Refs [unverified].

### Inferences
- The glass binaries fall into three kinds:
  - observings beyond lab timescales (B10, B11);
  - explanations among quantities that vary together (B12, B13);
  - class-membership questions: is the deposit equivalent to the liquid (B14), and is phase 2 a liquid (B15)?
- Vapour deposition, ancient amber and swap Monte Carlo are the routes below Tg opened since 2007. Most recent shifts in standing rest on them.
- "LLT" needs a stated criterion: two non-crystalline phases of the same composition, separated by a first-order line with observed coexistence. Phosphorus meets it, with the fluid–liquid nuance. TPP and Si have not been shown to.

### Gaps
- Not checked: work since 2023 on facilitation vs RFOT, new equivalence tests for ultrastable glasses, and recent TPP and Si data.
- The project's existing glass entry was not visible to me, so some overlap may remain.

## Q4 Melting and order: Lindemann vs Born, premelting, 2D melting, quasicrystal stability, time crystals

### Takeaway
- **Ordinary melting** begins at surfaces and defects, at the thermodynamic melting point Tm. The Lindemann and Born criteria bear only on melting inside a superheated crystal, and there the evidence points to local nucleation.
- **2D melting** in two steps, through a hexatic phase, is settled.
- **Open:** when ice premelting begins, and what stabilises quasicrystals.
- **Time crystals in chemical systems** are largely a question of definition.
- All Q4 references are [unverified].

### Cited Findings (frontier binaries)

**B18. Melting inside a superheated crystal: elastic (Born) instability or homogeneous nucleation of liquid**
- **Claim:** A superheated crystal with no free surfaces or grain boundaries melts when an elastic stability condition fails, for example when a shear modulus reaches zero.
- **Negation:** The same crystal melts by thermally activated homogeneous nucleation of liquid before any elastic limit is reached.
- **Observings:**
  - Criteria [model]:
    - Lindemann 1910: vibration amplitude reaches about a tenth of the atomic spacing.
    - Born 1939: shear rigidity vanishes (doi:10.1063/1.1750497).
    - Tallon 1989: a hierarchy of stability limits (doi:10.1038/342658a0).
  - Real crystals melt at Tm with almost no superheating, because their surfaces melt first [obs].
  - Alsayed et al. 2005, microgel colloids: premelting began at grain boundaries and dislocations [obs]. doi:10.1126/science.1112399.
  - Wang et al. 2012, superheated colloidal crystals: liquid nucleated inside the crystal, preceded by defect-rich regions with large vibration amplitude [obs]. doi:10.1126/science.1224763.
  - Mo et al. 2018, MeV ultrafast electron diffraction of laser-heated gold films: melting switched from heterogeneous to homogeneous as the energy density rose [obs]. doi:10.1126/science.aar2058.
- **Why hard:**
  - The nucleation barrier vanishes near the stability limit, so the two mechanisms can coincide.
  - Colloids are only analogues of atomic crystals.
  - Ultrafast experiments are far from equilibrium.
- **Standing in 2026:**
  - Settled: at Tm, melting starts at surfaces and defects.
  - Narrowing: superheated crystals melt by local nucleation, with the elastic limit as an upper bound.
  - The Lindemann ratio survives as an empirical correlation [conv], not as a mechanism.
- **What would settle it:** Atom-resolved time series showing whether the measured local shear modulus vanishes before or after the first liquid nuclei appear.
- **Proponents:**
  - Elastic: M. Born, F. Lindemann (historical), J. Tallon.
  - Nucleation: K. Lu, A. Yodh, Y. Han [unverified attribution].
- **Type:** Explaining.

**B19. When does the ice surface premelt?**
- **Claim:** The basal surface of ice Ih in equilibrium with its vapour carries a disordered quasi-liquid layer (QLL) from tens of kelvin or more below 0 °C.
- **Negation:** The same surface stays crystalline, apart from reconstruction and point defects, until a few kelvin below 0 °C. There, liquid first appears as droplets or patches.
- **Observings:**
  - Frenken & van der Veen 1985 established surface melting as a phenomenon on Pb(110), using ion shadowing and blocking [obs]. doi:10.1103/PhysRevLett.54.134.
  - On ice, different methods (X-ray, sum-frequency, ellipsometry, AFM, optics) put the onset at temperatures spanning a very wide range below 0 °C (review: Slater & Michaelides 2019, doi:10.1038/s41570-019-0080-8).
  - Sazaki et al. 2012 used laser confocal differential-interference microscopy. QLL appeared as droplets and thin layers only above about −2 °C [obs]. doi:10.1073/pnas.1116685109.
  - Murata et al. 2016 linked QLL formation to vapour supersaturation and read it as incomplete wetting [obs+model]. doi:10.1073/pnas.1608888113.
  - Sánchez et al. 2017 used sum-frequency spectroscopy. The top bilayers disordered one at a time, far below 0 °C [obs]. doi:10.1073/pnas.1612893114.
  - Hong et al. 2024 used non-contact AFM with a functionalised tip on ice films in ultra-high vacuum. They saw mixed hexagonal–cubic stacking, with disorder appearing near 120 K [obs]. Calling this the onset of premelting is [recon]. doi:10.1038/s41586-024-07427-8.
- **Why hard:**
  - Each method uses its own order parameter.
  - "Disordered" is not the same as "liquid-like" [conv].
  - Results depend on contamination and on vapour supersaturation.
  - Films grown in vacuum are not bulk crystals in contact with vapour.
- **Standing in 2026:** Open. The 2024 AFM work adds a new low-temperature observing.
- **What would settle it:** One single-crystal basal surface under controlled vapour pressure, measured by at least two methods at once (structure and diffusion) from about 120 K to 273 K, with an agreed criterion for "liquid-like".
- **Proponents:**
  - Early, continuous onset: J. G. Dash and J. Wettlaufer (theory), A. Michaelides, Y. Jiang, M. Bonn.
  - Late, patchy onset: G. Sazaki, Y. Furukawa, K. Murata.
- **Type:** Observing.

**B20. 2D melting: is there a hexatic phase, and is the liquid–hexatic step first-order?**
- **Scope:** Three accounts compete:
  - KTHNY: two continuous steps;
  - a single first-order step;
  - a mixed scenario: first-order liquid–hexatic, then continuous hexatic–solid.
- They split into two binaries:
  - **B20a:** Do hard disks and dipolar colloids pass through a hexatic phase, or melt directly?
  - **B20b:** For hard disks, is the liquid–hexatic step first-order or continuous?
- **Observings:**
  - KTHNY theory [model]: Kosterlitz & Thouless 1973, doi:10.1088/0022-3719/6/7/010; Halperin & Nelson 1978, doi:10.1103/PhysRevLett.41.121; Young 1979, doi:10.1103/PhysRevB.19.1855.
  - Before 2011, simulations conflicted [prior] (Strandburg 1988, doi:10.1103/RevModPhys.60.161).
  - Zahn, Lenke & Maret 1999, video microscopy of superparamagnetic colloids with tunable dipolar repulsion: an intermediate hexatic regime, consistent with KTHNY [obs]. doi:10.1103/PhysRevLett.82.2721.
  - Bernard & Krauth 2011, event-chain Monte Carlo on about 10^6 hard disks: a loop in the pressure curve, i.e. first-order liquid–hexatic coexistence [sim]. doi:10.1103/PhysRevLett.107.155704.
  - Engel et al. 2013 confirmed this with three algorithms [sim]. doi:10.1103/PhysRevE.87.042134.
  - Kapfer & Krauth 2015: softer disks melt continuously, as in KTHNY [sim]. doi:10.1103/PhysRevLett.114.035702.
  - Thorneywork et al. 2017, monolayers of hard-sphere colloids: consistent with the mixed scenario [obs]. doi:10.1103/PhysRevLett.118.158001.
- **Why hard (prior):**
  - Finite-size effects and slow equilibration misled simulations before 2011.
  - The order of the transition depends on the interaction.
- **Standing in 2026:**
  - B20a is settled (experiment 1999–2017, simulation 2011–2015).
  - B20b is settled for hard disks (simulation 2011–2013, colloids 2017).
  - The view, held from the 1980s to the 2000s, that all 2D melting follows KTHNY is negated [prior].
- **Proponents:**
  - Simulation: W. Krauth, M. Engel, S. Kapfer.
  - Experiment: G. Maret, P. Keim.
  - KTHNY theory: J. M. Kosterlitz, D. Thouless, B. Halperin, D. Nelson, A. P. Young.
- **Type:** Observing: the phase sequence.

**B21. Quasicrystal stability: energy or entropy**
- **Claim:** Stable icosahedral quasicrystals such as i-YbCd5.7 and i-ScZn7.33 are enthalpy ground states, stable as T → 0.
- **Negation:** The same phases are stable only at finite temperature, through tiling (phason) entropy. At low temperature a periodic approximant or a phase mixture has lower free energy.
- **Observings:**
  - Shechtman et al. 1984: icosahedral diffraction from rapidly quenched Al–Mn, a metastable phase [obs]. doi:10.1103/PhysRevLett.53.1951.
  - Tsai et al. 2000: a stable binary Cd–Yb quasicrystal [obs]. doi:10.1038/35046202.
  - Widom, Strandburg & Swendsen 1987: the random-tiling model, in which entropy stabilises the phase [model/sim]. doi:10.1103/PhysRevLett.58.706.
  - Mihalkovič et al. 2002: a structure predicted from total energies [sim]. doi:10.1103/PhysRevB.65.104205.
  - A 2025 Nature Physics study ran DFT on nanoparticles of increasing size and extrapolated to the bulk. It found both phases studied to be enthalpy-stabilised [sim]. doi:10.1038/s41567-025-02925-6. Authors recalled as W. Baek, S. Das, S. Tan, V. Gavini and W. Sun (University of Michigan) [authors, DOI and details unverified].
  - Natural quasicrystals bear on formation under shock, not on stability at T = 0 [obs]: Khatyrka meteorite (Bindi et al. 2009, doi:10.1126/science.1170827); trinitite (Bindi et al. 2021, doi:10.1073/pnas.2101350118).
- **Why hard:**
  - DFT needs a periodic cell, and quasicrystals have none.
  - Quasicrystals and approximants differ by only meV per atom.
  - Phason entropy estimates depend on the model.
  - Phasons freeze at low temperature, so equilibrium there is out of reach.
- **Standing in 2026:** Open and probably system-dependent. The 2025 work adds weight to energy stabilisation for Tsai-type phases [unverified].
- **What would settle it:** Free-energy calculations that include phason entropy, checked against long-anneal transformations between quasicrystals and approximants.
- **Proponents:**
  - Entropy: C. Henley, K. Strandburg, M. Widom (early).
  - Energy: M. Mihalkovič, M. Widom (later), the 2025 DFT team.
- **Type:** Explaining.

**B22. Discrete time-crystalline order of nuclear spins in molecular systems**
- **Claim:** Periodically driven nuclear spins in molecular systems show discrete time-crystalline order stabilised by their interactions. The systems are 31P in ammonium dihydrogen phosphate, and star-shaped molecules in solution NMR. The order shows as a period-doubled response that is robust to pulse errors and outlasts single-spin dephasing.
- **Negation:** In the same experiments, single- or few-spin dynamics plus finite-time (prethermal) effects explain the response. There is no time-crystalline phase.
- **Observings:**
  - Theory [model]:
    - Wilczek 2012 proposed time crystals (doi:10.1103/PhysRevLett.109.160401).
    - Watanabe & Oshikawa 2015 gave a no-go theorem for equilibrium time crystals (doi:10.1103/PhysRevLett.114.251603).
    - Else, Bauer & Nayak 2016 introduced Floquet (periodically driven) time crystals (doi:10.1103/PhysRevLett.117.090402).
  - Physics platforms [obs]: trapped ions (Zhang et al. 2017, doi:10.1038/nature21413); NV centres in diamond (Choi et al. 2017, doi:10.1038/nature21426).
  - Molecular NMR [obs]: Rovny, Blum & Barrett 2018, doi:10.1103/PhysRevLett.120.180603; Pal et al. 2018, doi:10.1103/PhysRevLett.120.180602.
  - Belousov–Zhabotinsky oscillations are driven and open [obs]. Calling them "time crystals" rather than limit cycles is a convention [conv].
- **Why hard:**
  - The class criterion itself is disputed [conv]: equilibrium, Floquet or dissipative? Protected by many-body localisation, or only prethermal?
  - Clean NMR crystals lack the disorder that protection would need.
- **Standing in 2026:**
  - Equilibrium time crystals are excluded by the 2015 theorem, within its assumptions.
  - Whether the NMR results show a phase or only its signatures is open.
  - Whether chemical oscillators count is a matter of definition.
- **What would settle it:** Show that the lifetime of the subharmonic response scales with spin–spin coupling (for example by isotopic dilution), and that its phase stays rigid across a range of pulse errors.
- **Proponents:** Claim: S. Barrett, J. Rovny, T. S. Mahesh. Theorists stress prethermal limits [unverified attribution].
- **Type:** Explaining: classifying an observed response.

### Inferences
- In Q4 the decisive disagreements are about criteria:
  - what counts as "liquid-like";
  - whether "stable" means as T → 0 or at finite temperature;
  - what counts as a "time crystal".
- These are the places where the project must state its membership criteria.

### Gaps
- Not checked:
  - follow-ups since 2024 to the ice AFM work;
  - independent checks of the 2025 quasicrystal study;
  - recent claims of time crystals in chemical systems.

## Q5 Assembly and condensates: pathway complexity, living crystallisation-driven self-assembly, LLPS vs percolation, hard-sphere crystallisation

### Takeaway
- **Supramolecular assembly.** Pathway complexity and seeded "living" growth are reproduced observings (2007–2015). How common they are, and where "living" behaviour stops, are open.
- **Condensates.** Liquid–liquid phase separation (LLPS) is settled for purified proteins and for synthetic coacervates in vitro. Whether particular condensates in cells are phase-separated liquids is contested, and the answer depends on the criterion used.
- **Hard spheres.** Entropy-driven freezing is settled. Measured and simulated nucleation rates still disagree.
- All Q5 references are [unverified].

### Cited Findings (frontier binaries)

**B23. Kinetic control in supramolecular assembly**
- **B23a.**
  - Claim: supramolecular polymers made by common protocols (cooling, mixing solvents) reach equilibrium, so the structures reported do not depend on preparation history.
  - Negation: under the same protocols they are often kinetically trapped, so the structures do depend on history.
- **B23b.**
  - Claim: in seeded supramolecular polymerisation and living crystallisation-driven self-assembly (CDSA), growth happens only at existing ends, with no termination and no spontaneous nucleation. Length is then set by the ratio of monomer to seed.
  - Negation: under the same conditions, spontaneous nucleation, inactive ends or fragmentation also contribute.
- **Observings:**
  - Korevaar et al. 2012 followed a chiral π-conjugated monomer in methylcyclohexane by CD spectroscopy [obs]. doi:10.1038/nature10720.
    - A kinetically favoured aggregate of one helicity formed first.
    - It converted to the thermodynamic aggregate of opposite helicity, with outcomes depending on cooling rate.
    - The two-pathway account is [model].
  - Ogi et al. 2014: porphyrin monomers kept dormant by intramolecular hydrogen bonds grew only from added seeds [obs]. doi:10.1038/nchem.1849.
  - Kang et al. 2015: chain-growth supramolecular polymerisation of corannulenes [obs]. doi:10.1126/science.aaa4249.
  - Living CDSA:
    - Wang et al. 2007 grew poly(ferrocenyldimethylsilane) block-copolymer cylinders from seeds, with lengths measured by TEM [obs]. doi:10.1126/science.1141382.
    - Gilroy et al. 2010: length scaled linearly with the unimer-to-seed ratio, with low dispersity [obs]. doi:10.1038/nchem.664.
  - Review: Wehner & Würthner 2020, doi:10.1038/s41570-019-0153-8.
- **Why hard:**
  - Kinetic traps cannot be seen in end-state measurements.
  - Equilibration can take longer than any experiment.
  - "Living" is a criterion borrowed from polymer chemistry and applied operationally [conv].
- **Standing in 2026:**
  - Pathway complexity is settled as a phenomenon (2012, many reproductions). How common it is (B23a) is open.
  - Living growth within stated windows is settled operationally. Its mechanism and limits (B23b) are open.
- **What would settle it:**
  - B23a: routine path-independence tests (different rates; reaching the same state from both directions) and a literature audit.
  - B23b: kinetics that resolve addition of single unimers from addition of aggregates.
- **Proponents:** E. W. Meijer, T. de Greef, F. Würthner, S. Sugiyasu, M. Takeuchi, T. Aida, K. Kim; I. Manners (d. 2021), M. Winnik, R. O'Reilly [unverified attribution].
- **Type:** Observing, plus the convention of what "living" means.

**B24. Biomolecular condensates: true phase separation?**
- **B24a (observing).**
  - Claim: in living cells, a given condensate (nucleoli, stress granules) forms above a threshold scaffold concentration. Above it, extra scaffold goes into the dense phase while the dilute-phase concentration stays fixed.
  - Negation: in the same cells, the dilute-phase concentration keeps rising, with no sharp threshold.
- **B24b (explaining).**
  - Claim: these condensates form by a density transition: phase separation, often coupled to percolation.
  - Negation: they form without a density transition, by percolation or gelation alone, by clustering on scaffolds such as chromatin, or by active assembly.
- **Observings:**
  - Brangwynne et al. 2009: P granules in C. elegans fuse, drip and recover after photobleaching [obs]. doi:10.1126/science.1172046.
  - Li et al. 2012: purified multivalent signalling proteins form droplets above a sharp threshold in vitro [obs]. doi:10.1038/nature10879.
  - Riback et al. 2020: the dilute-phase concentration of NPM1 is not fixed in nucleoli. Their account is multicomponent interactions [obs+model]. doi:10.1038/s41586-020-2256-2.
  - Klosin et al. 2020: concentration buffering consistent with phase separation [obs]. doi:10.1126/science.aav6691.
  - McSwiggen et al. 2019 (eLife): herpesvirus replication compartments in infected cells concentrate proteins without LLPS signatures [obs]. doi:10.7554/eLife.47098. The same group's 2019 review sets out diagnostic caveats: doi:10.1101/gad.331520.119.
  - Kar et al. 2022: in vitro, phase-separating RNA-binding proteins form heterogeneous clusters below saturation [obs]. doi:10.1073/pnas.2202222119.
  - Material-state change over time:
    - Patel et al. 2015: FUS droplets turn from liquid to solid. doi:10.1016/j.cell.2015.07.047.
    - Jawerth et al. 2020: condensates age as Maxwell fluids. doi:10.1126/science.aaw4951.
  - Frameworks and critique: Banani et al. 2017, doi:10.1038/nrm.2017.7; Mittag & Pappu 2022, doi:10.1016/j.molcel.2022.05.018; Musacchio 2022 (critique), doi:10.15252/embj.2021109952.
  - Synthetic coacervates have measured binodals and are accepted as LLPS [obs] (Spruijt et al. 2010, doi:10.1021/ma101031t).
- **Why hard:**
  - Cells are multicomponent and active. True multicomponent phase separation need not show a fixed saturation concentration [model], so B24a does not decide B24b.
  - Imaging cannot resolve whether there is an interface.
  - Overexpression and fixation create artefacts.
- **Standing in 2026:**
  - Phase separation in vitro is settled.
  - B24a depends on the system: both buffering and its absence have been observed.
  - B24b is open and narrowing. "Condensate" is now a neutral term, and several tests are required for each case.
- **What would settle it:** For each condensate in cells, measure the dense- and dilute-phase concentrations while varying total concentration and composition. Add interfacial tension, and compare with multicomponent phase diagrams.
- **Proponents:**
  - Phase separation: A. Hyman, C. Brangwynne, F. Jülicher, M. Rosen, R. Pappu, T. Mittag, S. Alberti.
  - Sceptical or pluralist: A. Musacchio, D. McSwiggen, X. Darzacq, R. Tjian [unverified attribution].
- **Type:** B24a is an observing; B24b is an explaining.

**B25. Hard-sphere crystallisation: do experimental and simulated nucleation rates agree?**
- **Settled anchor:**
  - Hard spheres have no attractions, yet simulations show a fluid–solid transition [sim] (Wood & Jacobson 1957, doi:10.1063/1.1743956; Alder & Wainwright 1957, doi:10.1063/1.1743957).
  - Coexistence lies at volume fractions φ ≈ 0.494 and 0.545 (Hoover & Ree 1968, doi:10.1063/1.1670641).
  - In sterically stabilised PMMA colloids, crystals form in that window and glass forms above about 0.58 [obs] (Pusey & van Megen 1986, doi:10.1038/320340a0).
  - Fcc is more stable than hcp by only about 0.001 kT per particle [sim] (Bolhuis et al. 1997, doi:10.1038/40779).
  - Caveats on how φ is calibrated and how soft the particles are: Royall, Poon & Weeks 2013, doi:10.1039/C2SM26245B.
- **Claim:** For colloids that match hard spheres within stated tolerances, measured nucleation rates at φ ≈ 0.50–0.53 agree with rare-event simulation within about two orders of magnitude.
- **Negation:** At the same φ, measured and simulated rates differ by many orders of magnitude.
- **Observings:**
  - Auer & Frenkel 2001: rates from umbrella sampling fall far below rates from light scattering at low supersaturation [sim vs obs]. doi:10.1038/35059035.
  - Filion et al. 2010: three simulation methods agree with each other, and the gap remains [sim]. doi:10.1063/1.3506838.
  - Gasser et al. 2001: confocal microscopy puts the critical nucleus at about 100 particles [obs]. doi:10.1126/science.1058457.
  - Royall et al. 2024 (review) list the gap as unresolved. doi:10.1103/RevModPhys.96.045003.
- **Why hard:** The candidate causes are many, and each is its own binary:
  - calibration of φ;
  - polydispersity and softness;
  - sedimentation;
  - hydrodynamics;
  - nucleation at walls;
  - extrapolation in the simulations.
- **Standing in 2026:** Open [post-2024 unverified].
- **What would settle it:** Density-matched experiments in microgravity with absolute φ calibration, compared with simulations that use the measured size distribution and softness.
- **Proponents:**
  - Simulation: D. Frenkel, M. Dijkstra, L. Filion.
  - Experiment and critique: P. Pusey, W. Poon, E. Weeks, C. P. Royall, T. Palberg [unverified attribution].
- **Type:** The rates are an observing; their causes are an explaining.

### Inferences
- The class "phase" is under strain:
  - in vitro coacervates meet the textbook criterion of coexisting phases with a binodal;
  - condensates in cells may not, and theory says multicomponent phase separation need not show single-component signatures.
- The project should keep apart two things:
  - the observing criterion: threshold, buffering, interface;
  - the model class: phase separation, percolation, active assembly.

### Gaps
- Not checked:
  - condensate work from 2023–2026, such as phase diagrams measured in cells;
  - recent CDSA kinetics;
  - any resolution since 2024 of the hard-sphere rate gap.

## Further candidates (one line each; all refs unverified)
- **Water's liquid–liquid critical point.** Simulations: Palmer et al. 2014, doi:10.1038/nature13405; Debenedetti et al. 2020, doi:10.1126/science.abb9796. Experiments: Kim et al. 2017, doi:10.1126/science.aap8269; Kim et al. 2020, doi:10.1126/science.abb9385; Kringle et al. 2020, doi:10.1126/science.abb7542. Debated, and best treated in a water file.
- **Polymer crystallisation.** Is there a mesomorphic precursor (Strobl, doi:10.1007/s101890070030), or is classical secondary nucleation (Hoffman–Lauritzen) enough?
- **Complex coacervation.** Is it driven by counterion-release entropy or by electrostatic correlation (Voorn–Overbeek)?
- **Supercooled liquids.** Does medium-range crystal-like order control crystal nucleation? Russo & Tanaka 2012, doi:10.1038/srep00505.
- **Viedma ripening.** Does chiral symmetry breaking come from attrition-enhanced Ostwald ripening or from cluster incorporation? Viedma 2005, doi:10.1103/PhysRevLett.94.065504.
- **Frank–Kasper σ phase in block copolymers.** Is it stabilised by energy or by entropy? Lee, Bluemle & Bates 2010, doi:10.1126/science.1195552.
- **Liquid condensates and amyloid.** Are condensates obligatory intermediates on the way to amyloid? Patel et al. 2015.
- **Mpemba effect** (historically notable). Claims that hot water freezes faster fail to reproduce under control: Burridge & Linden 2016, doi:10.1038/srep37665. Markovian colloidal analogues exist: Kumar & Bechhoefer 2020, doi:10.1038/s41586-020-2560-x.
- **Polywater** (rejected; 1966–1973). The anomalous water condensed in capillaries was traced to contamination by silica and organic matter.
