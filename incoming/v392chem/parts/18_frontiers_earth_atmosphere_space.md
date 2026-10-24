# Frontier binaries: geochemistry, atmospheric and ocean chemistry, cosmochemistry, astrochemistry (status at 23 October 2026)

## Key gathered points

- **Coverage.** 25 binaries plus further candidates. Sections 1–2 (remote detections; cometary and returned-sample chemistry) rest on sources fetched this session. **Sections 3–5 (atmospheric, Earth-system, cosmochemistry) could not be checked**: the shared search budget and hourly fetch limit ran out, so they come from prior knowledge, are marked [unverified], and are leads, not findings.
- **Venus phosphine: open, not retracted.** The 2020 claim (~20 ppb, 266.94 GHz, JCMT+ALMA) was weakened by re-processing (line not robust), a mesospheric-SO2 fit and a strict SOFIA limit. The discovery team reports a JCMT-Venus confirmation (2022–23, ~0.3 ppm near 55 km), preliminary and in conference proceedings. No independent refereed confirmation was found.
- **K2-18 b DMS: moving toward non-detection.** Four independent 2025 reanalyses (Schmidt et al., Luque et al., Taylor, Welbanks et al.) found no robust DMS. A five-NIRSpec-transit study co-authored by the claimant gives DMS below 3σ. A 2026 model-plus-lab study favours a sub-Neptune without DMS. The claimant keeps DMS as a candidate. A liquid-water surface is open, and models disagree on abiotic DMS.
- **Mars methane: open, sharper.** TGO's ≤0.05 ppbv limit (2019) against Curiosity TLS (background ~0.2–0.7 ppbv, spikes to ~21 ppbv). A 2025 reanalysis points to methane inside the rover and underestimated errors, and proposes a sealed-cell test.
- **Comet 67P D/H: reopened, then contested.** 2024: dust inflates local D/H, and well-mixed gas is near-terrestrial. 2026: more than 7,600 ROSINA measurements give (4.67 ± 0.59) × 10⁻⁴, about 3× VSMOW, with little variation.
- **Bennu organics.** 14 protein and 19 non-protein amino acids, all five nucleobases, racemic chiral amino acids, ¹⁵N enrichment, sodium-salt evaporites. An indigenous origin is strongly supported. The synthesis site (parent-body fluids or cold-cloud ices) is open.
- **Pattern.** Remote-detection disputes turn on a weak feature, its reduction, line-list completeness and statistical conventions. Independent instruments or in-situ sampling, not more modelling, will settle them. Elsewhere the contested quantity (pO2, fO2, aerosol pH, t₀) comes from a proxy or model, while the observing is a measured ratio.

Labels: **(obs)** observing; **(recon)** reconstruction; **(conv)** convention or definition; **(model)** model construct; **(sim)** simulation. "Field adds" marks interpretation.

## 1. Remote detections: did X occur?

### Takeaway
All three flagship detections (Venus PH3, K2-18 b DMS, Mars CH4) remain unconfirmed by independent methods. For K2-18 b the evidence has moved clearly against the claim. For Venus and Mars it is deadlocked between the discovery teams and their critics, and each needs an observation that removes the disputed processing step: in-situ sampling for Venus, a sealed-cell repeat for Mars.

### Cited findings: frontier binaries

#### B1. Phosphine in Venus's cloud deck (observing binary)
- **Claim:** Gas-phase PH3 is present in Venus's atmosphere at cloud-deck altitudes (~50–60 km) at ppb-or-greater abundance, detectable in millimetre absorption.
- **Negation:** At the same altitudes and detection threshold, no PH3 is present. The reported millimetre absorption comes from something else: mesospheric SO2 or a processing artefact.
- **Scope split:** Three accounts compete and they do not share one scope. In (i), the 2020 feature is cloud-level PH3 at ~20 ppb. In (ii), the feature is SO2 and/or a baseline artefact. In (iii), PH3 exists but varies with time or altitude, for example through daytime destruction, which would reconcile the detections with the non-detections. That gives two proper binaries:
  - **B1a:** the 266.94 GHz absorption in the discovery spectra is PH3, versus it is not.
  - **B1b:** PH3 at ≥ppb is present at cloud level in at least some epochs (JCMT-Venus 2022–23), versus it is absent in all epochs at levels the SOFIA and infrared limits exclude.
- **Observings, claim side:**
  - (obs) JCMT and ALMA spectra of the whole disc show absorption at 266.94 GHz (~1.1 mm), the PH3 J=1–0 frequency. This was read as ~20 ppb in the clouds. Source: Greaves et al., *Nat. Astron.* 5, 655 (online Sept 2020), https://doi.org/10.1038/s41550-020-1174-4. The DOI was seen in reference lists. The 20 ppb figure is as restated by Lincowski et al., https://arxiv.org/pdf/2101.09837. Observation years (JCMT 2017, ALMA 2019) [unverified].
  - (obs, reanalysis) The 1978 Pioneer Venus Large Probe mass-spectrometer data were reanalysed. They show gas-phase phosphorus, which was read as PH3 fragments. Source: Mogul et al. 2021, *GRL*, https://doi.org/10.1029/2020GL091327, as summarised in the detection team's review (Bains et al. 2024, https://frontiersin.org/journals/astronomy-and-space-sciences/articles/10.3389/fspas.2024.1372057/full). An alternative carrier, phosphoric acid or phosphorus oxides, was offered by Brinckerhoff et al. (LPSC 2021).
  - (obs, preliminary) The JCMT-Venus campaign used the new Ū'ū receiver in Feb 2022, Jul 2023 and Sep 2023, with ~200 h awarded and ~100 h used. It observed PH3, HDO and SO2 simultaneously. A preliminary result gives ~0.3 ppm PH3 near 55 km, including pressure-broadened line wings. The author calls the method experimental. Source: Clements 2024, Kavli-IAU Symp. 387 proceedings, arXiv:2409.13438, https://arxiv.org/html/2409.13438v1. This is not a refereed detection paper.
  - (obs, contested) A reanalysis of SOFIA far-infrared data is said to support PH3: Greaves et al. 2023, *GRL*, https://doi.org/10.1029/2023GL103539. Cordiner et al. 2023 dispute it, https://doi.org/10.1029/2023GL106136. Both are as summarised in Bains et al. 2024.
- **Observings, negation side:**
  - (obs, reanalysis) A re-processing of the ALMA data found the feature not statistically robust. High-order polynomial baselines can create spurious lines. Sources: Snellen et al. 2020, *A&A* 644, L2, https://doi.org/10.1051/0004-6361/202039717; Akins et al. 2021, https://doi.org/10.3847/2041-8213/abd56a (per Bains et al. 2024).
  - (sim on obs) Radiative-transfer Jacobians place the line core above ~80 km, where PH3 lasts less than 1 s. A nominal mesospheric SO2 profile fits the JCMT line without PH3: 30 ppb at 78 km rising to 400 ± 150 ppb at 100 km. That profile is consistent with cloud-top SO2 of 200–350 ppb measured within a month. Keeping 20 ppb of PH3 there would need ~3.7 × 10¹⁵ molecules cm⁻² s⁻¹, about 100 times Earth's photosynthetic O2 flux. The authors say cloud-level PH3 is not excluded, because the line is insensitive at cloud altitudes. Source: Lincowski et al. 2021, *ApJL* 908, L44, https://doi.org/10.3847/2041-8213/abde47 (arXiv text read). Villanueva et al. 2021 point the same way, https://doi.org/10.1038/s41550-021-01422-z.
  - (obs) SOFIA observations set a "strict upper limit": Cordiner et al. 2022, *GRL*, https://doi.org/10.1029/2022GL101055. The value, ~0.8 ppb at 75–110 km, is [unverified].
  - (obs) IRTF/TEXES infrared spectra set a cloud-top upper limit: Encrenaz et al. 2020, *A&A* 643, L5, https://doi.org/10.1051/0004-6361/202039559. The value is [unverified].
- **Field adds:** Going from a line to an abundance requires a model atmosphere: temperature, SO2 profile, line shape and continuum (model). Going from an abundance to "anomalous" requires a complete photochemical and kinetic network (model). The detection team argues that no known abiotic process yields the inferred PH3. They concede that part of the absorption appears to come from the mesosphere. There PH3 should be destroyed in under a second, so either the absorber is not PH3 or the photochemical models are badly incomplete (Bains et al. 2024). Two further items were seen only in an aggregator (https://orbitcodex.com/knowledge-base/phosphine-on-venus) and the primaries were not seen. One is a JWST detection of PH3 in the brown dwarf Wolf 1130C (Oct 2025), together with the observation that no single model fits PH3 across giant planets and brown dwarfs. The other is a 2025 PNAS review of reduced-phosphorus pathways, https://doi.org/10.1073/pnas.2507109122, which found none that matches.
- **Why hard:** The signal is one weak line at the noise floor, close to an SO2 transition. The interferometer filters out broad features and needs baseline fitting. Whole-disc single-dish spectra mix altitudes. Venus SO2 is highly variable. And appealing to time-variable PH3 can absorb any non-detection, so the claim risks becoming unfalsifiable.
- **Standing 2026:** Open. Nothing has been retracted. The proponents report confirmation, and the critics' reanalyses and upper limits still stand. No independent refereed confirmation was found through Oct 2026.
- **What would settle it:** In-situ cloud-level mass or laser spectrometry, such as the NASA DAVINCI probe; an aggregator gives its launch as "early 2030s", and its schedule and budget status for 2025–26 are [unverified]. Alternatively, an independent multi-line detection (other rotational lines, or infrared bands) by a group outside the discovery team, using public data, a method free of baseline fitting, and a simultaneous SO2 profile.
- **Main proponents:** Claim: J. Greaves, A. Richards, W. Bains, S. Seager, J. Petkowski, D. Clements, P. Rimmer. Negation or scepticism: I. Snellen; A. Lincowski and V. Meadows; G. Villanueva; M. Cordiner; T. Encrenaz.
- **Type:** Observing (did PH3 occur at cloud level?), with a nested explaining dispute over which molecule makes the line.

#### B2. Dimethyl sulfide (DMS, and DMDS) in K2-18 b's atmosphere (observing binary)
- **Claim:** JWST transmission spectra (0.6–12 µm) of the temperate sub-Neptune K2-18 b contain DMS and/or DMDS absorption at ≳ppmv abundance, above the detection threshold (Bayes-factor or ≳3σ preference).
- **Negation:** For the same spectra and wavelength range, under defensible reductions and a complete molecule set, no DMS or DMDS absorption can be distinguished. Any preference falls below threshold or is equally well explained by other molecules or by noise.
- **Observings, claim side:**
  - (obs + model retrieval) NIRISS/SOSS and NIRSpec G395H transits (JWST GO 2722) show CH4 at ~5σ, CO2 at ~3σ and a low-significance DMS signal. Source: Madhusudhan et al. 2023, *ApJ* 956, L13, as summarised by Luque et al., https://arxiv.org/html/2505.13407v1.
  - (obs + retrieval) One MIRI/LRS transit (~5–12 µm) shows DMS/DMDS features at ~3σ and >10 ppmv. The near-infrared data were not included in that analysis. Source: Madhusudhan et al. 2025, *ApJL* 983, L40. Summaries: Luque et al. (above); https://theanalyticalscientist.com/issues/2025/articles/apr/five-reasons-to-be-skeptical-about-life-on-k2-18b/.
  - (retrieval) A search over ~650 molecules kept DMS near the top of the candidates. Source: Pica-Ciamarra et al. 2025, arXiv:2505.10539, as reported at https://carlzimmer.com/new-studies-dismiss-signs-of-life-on-distant-planet/ (NYT, 23 May 2025).
  - (obs + retrieval, weak) Four new NIRSpec transits (GO 2372) plus archival data give DMS only ~2.7σ. CH3SH and N2O are marginal, and nothing exceeds 3σ. Source: Hu et al. 2025, arXiv:2507.12622, https://arxiv.org/html/2507.12622v1; the ~2.7σ figure is from https://www.astronomy.com/?p=165339. Madhusudhan is a co-author.
- **Observings, negation side:**
  - (reanalysis) Sixty data treatments and more than 250 retrievals of the NIRISS+NIRSpec data found no statistically significant or reliable CO2 or DMS. CH4 is retained at ~4σ (per Luque). The authors conclude that an oxygen-poor mini-Neptune suffices. Source: Schmidt et al. 2025, *AJ* 170, 298, https://doi.org/10.3847/1538-3881/ae019a (https://www.ipac.caltech.edu/publication/2025AJ....170..298S).
  - (reanalysis) A joint 0.6–12 µm analysis used three pipelines (exoTEDRF, Eureka!, SPARTA) plus the published JExoRES spectra, and two retrieval codes (PLATON, SCARLET). Adding DMS/DMDS changes ln Z by −0.3 to +2.8, below the Δln Z > 5 convention. Ethane fits equally well. The MIRI features would need an implausibly hot atmosphere. Rejecting a flat line at 3σ would take about 25 more MIRI transits. Source: Luque et al. 2025, *A&A* 700, A284 (27 Aug 2025), https://doi.org/10.1051/0004-6361/202555580.
  - (reanalysis) In the MIRI-only data, five of six tests favour a featureless spectrum, with ~2σ at the DMS positions. Source: Taylor 2025, arXiv:2504.15916, per The Analytical Scientist (above).
  - (reanalysis) Of 90 plausible molecules tested, 59 could explain the MIRI signal. Propyne is the strongest. Source: Welbanks et al. 2025, arXiv:2504.21788, per NYT/Zimmer.
  - (sim + lab) Coupled climate–photochemistry runs at eccentricity 0.2 used new laboratory infrared opacities for DMS and DMDS (HFML-FELIX) and ethane overtone bands. They support a sub-Neptune without DMS. Source: Tsai et al. 2026, arXiv:2603.19803, https://astrobiology.com/2026/03/24/three-outstanding-physical-questions-for-k2-18-b-and-other-temperate-sub-neptunes/.
- **Field adds:** The "σ" or Bayes-factor detection threshold is a convention (conv), and Luque et al. caution against converting Δln Z to σ. Retrievals are model constructs. Their outcome depends on the molecule list (leaving out ethane or propyne inflates DMS), on line-list completeness (DMS/DMDS lack line lists below 1 bar, and the hydrocarbon lists are incomplete), and on reduction choices near 7 and 10 µm (Luque et al.).
- **Why hard:** There is a single MIRI transit, low signal-to-noise, overlapping methyl-group bands (DMS, DMDS, ethane, propyne), missing opacity data, and Bayesian evidence that is sensitive to priors and to the model space.
- **Standing 2026:** Moving toward "not detected at the claimed significance". Nothing has been retracted. DMS remains a sub-3σ candidate in analyses that include the proponents. No independent confirmation was found.
- **What would settle it:** About 25 more MIRI transits (Luque et al.) plus NIRSpec coverage of the C–H region; complete laboratory line lists for DMS, DMDS, ethane and propyne at the relevant temperatures and pressures; and blind multi-team retrievals over a shared, open molecule set.
- **Main proponents:** Claim: N. Madhusudhan and the Cambridge group. Negation: R. Luque and J. Bean (Chicago); S. Schmidt and R. MacDonald; J. Taylor; L. Welbanks; S.-M. Tsai.
- **Type:** Observing.

#### B3. K2-18 b: liquid-water ocean under a thin H2 atmosphere, or a deep gas-rich envelope (explaining binary)
- **Claim:** K2-18 b's terminator composition is rich in CH4 and CO2 and poor in NH3, CO and H2O. That composition is explained by a thin H2-rich atmosphere over a liquid-water ocean (the "hycean" account).
- **Negation:** The same composition is explained by a deep, high-metallicity H2-rich envelope with no liquid-water surface, as in a gas-rich sub-Neptune, possibly over magma.
- **Shared observings:** (obs) CH4 and CO2 are robustly detected, and H2O, NH3 and CO are not, in 5 NIRSpec transits plus NIRISS and MIRI data (Hu et al. 2025, https://arxiv.org/html/2507.12622v1). (obs) In the NIRISS+NIRSpec data alone, CH4 is detected at ~4σ and CO2 is not significant (Schmidt et al. 2025, https://doi.org/10.3847/1538-3881/ae019a).
- **Claim side:** (model) Hu et al. conclude that the planet is water-rich. Either the envelope is at least 10% H2O by volume, or a thin atmosphere sits over liquid water. The missing water vapour implies a cold trap, and the NH3 and CO non-detections favour a small H2 atmosphere over a liquid reservoir. The authors concede that models containing those gases also fit, and they call the ocean question open. Madhusudhan said the data are slightly more consistent with a hycean world (https://www.astronomy.com/?p=165339).
- **Negation side:** (model) Schmidt et al.: an oxygen-poor mini-Neptune needs neither a liquid surface nor life. (sim + lab) Tsai et al. 2026 find no strong evidence for a water-rich interior and prefer a cloudy, high-metallicity sub-Neptune (https://astrobiology.com/2026/03/24/three-outstanding-physical-questions-for-k2-18-b-and-other-temperate-sub-neptunes/). (model) Wogan et al. 2024 (ApJ 963, L7), Shorttle et al. 2024 (ApJ 962, L8; magma-ocean alternative) and Huang et al. 2024 (ApJ 975, 146) challenged the hycean reading even using the 2023 abundances. All three are as summarised in Luque et al., https://arxiv.org/html/2505.13407v1.
- **Sub-binary B3b (explaining; simulation versus simulation):** Can DMS form without life at detectable levels in a K2-18 b-like H2-rich atmosphere? Hu et al. 2025 say yes: their photochemistry makes DMS and CH3SH in massive, metal-rich H2 envelopes, so DMS alone is not a biosignature. Tsai et al. 2026 say abiotic DMS is highly unlikely. That reading comes only from a secondary summary (https://www.emergentmind.com/papers/2603.19803) and needs checking against the full paper. The two model results conflict directly.
- **Field adds:** The mass and radius alone allow a water world, a mini-Neptune or a magma world, so interior inference is degenerate (model). "Hycean" is a model category (conv/model). Its original 2021 definition is [unverified]. Whether DMS counts as a biosignature depends on which category applies.
- **Why hard:** Transmission spectra sample only the ~mbar–bar terminator. The deep interior is inferred through quench chemistry. Clouds, the thermal structure and orbital eccentricity (~0.2) all shift the predictions.
- **Standing 2026:** Open. Independent studies lean against a hycean world. The study with the most data, co-authored by the claimant, still argues for a water-rich interior.
- **What would settle it:** ppm-level detections of, or limits on, NH3, CO and H2O; thermal constraints from eclipse or phase-curve data; laboratory kinetics for organosulfur formation in H2; and convergence among quench-chemistry models.
- **Main proponents:** Hycean: Madhusudhan. Water-rich (ocean open): Hu and Benneke. No ocean, gas-rich: Schmidt, MacDonald, Wogan, Shorttle, Tsai.
- **Type:** Explaining.

#### B4. Methane in Mars's near-surface air at Gale crater (observing binary, with an explaining tail)
- **Claim:** Near-surface Martian air at Gale crater contains CH4 at a background of a few tenths of a ppbv, with episodic spikes of ~5–21 ppbv, as measured by Curiosity's Tunable Laser Spectrometer (TLS) in the SAM suite.
- **Negation:** At Gale, under the same sampling, Martian air holds no CH4 at those levels. The reported TLS values come from methane inside the rover and/or from underestimated uncertainty.
- **Scope note:** The usual framing, "Curiosity versus TGO", compares different scales. Curiosity samples air 1 m above the ground, mostly at night. TGO measures the column above ~4–5 km in solar occultation at the terminator. So the two results do not contradict each other unless transport and lifetime models are added. The proper observing binary therefore asks whether the TLS values are Martian (B4). A separate explaining binary asks, if they are, what closes the gap: night-time containment plus fast removal, or a local point source (B4b).
- **Observings, claim side:**
  - (obs) TLS reported a seasonal background of ~0.2–0.7 ppbv and a spike of 5.78 ppbv in 2013. The Mars Express PFS team reported seeing that spike from orbit (https://skyandtelescope.org/astronomy-news/mars-methane-mystery-continues/, 2019). TLS measured 21 ppbv in June 2019, and the reading was back to ~1 ppbv days later (https://skyandtelescope.org/astronomy-news/curiosity-detects-big-whiff-of-methane-on-mars/).
  - (obs) Webster et al. 2021 (*A&A*, https://doi.org/10.1051/0004-6361/202040030): two daytime enriched runs bracketing a night run gave near-zero daytime methane, with the night value within the long-term average. The background mean is below 0.5 ppbv (https://earthsky.org/?p=364912; https://www.sciencealert.com/nasa-thinks-they-are-close-to-cracking-the-mars-methane-mystery).
- **Observings, negation side:**
  - (obs) TGO's ACS and NOMAD instruments (solar occultation) found no methane, with a 0.05 ppbv upper limit, or less than ~500 t in the whole atmosphere. Source: *Nature* 2019, https://doi.org/10.1038/s41586-019-1096-4, as reported at S&T, above. The attribution to Korablev et al. is [unverified]. Later limits are more than ten times below the lowest Curiosity detection (https://aeronomy.be/en/news/2025/methane-mars-mere-illusion). An aggregator gives ~0.02 ppbv [unverified in primary].
  - (obs reanalysis) Viscardy, Catling and Zahnle 2025 (*JGR Planets*, https://doi.org/10.1029/2024JE008441) report three things. The foreoptics chamber next to the sample cell holds at least 1,000 times more CH4 than the cell. Pressure rose during detections, which suggests gas exchange with an unknown reservoir. And in five published runs the three CH4 lines, fitted separately, mostly disagreed, with only one line showing methane; they put the chance of that pattern at ~1 in 1,000. Their proposal is two consecutive-night runs with the same sample sealed in the cell (aeronomy.be, above). An aggregator says the authors stopped short of calling the detections spurious (https://orbitcodex.com/knowledge-base/methane-on-mars).
  - (expert view, 2019) Rodin (MIPT) did not rule out an artefact from rover materials (https://www.newswise.com/articles/view/715160/?sc=sphn).
- **B4b observings and models:** (model) 1-D models with horizontally uniform methane cannot reconcile the datasets, because methane's photochemical lifetime of ~300 years is far longer than the mixing time. (sim) Inverse Lagrangian 3-D transport reconciles them with a point source in north-western Gale. That raises a "coincidence problem", since the source would sit right beside the rover, and it requires fast removal in the atmosphere rather than at the surface (DPS 2023, https://baas.aas.org/pub/2023n8i300p09). (model) Barometric pumping of subsurface gas can produce sub-diurnal swings: *JGR Planets* 2024, https://doi.org/10.1029/2023JE008043, seen only via the aggregator. The proposed removal agents, dust electrification and surface oxidants, are untested (EarthSky, above).
- **Field adds:** Converting enriched-run spectra into atmospheric mixing ratios requires assumptions about cell integrity and the enrichment factor. Every reading of the source as biological, serpentinisation or clathrate release is interpretation.
- **Why hard:** There is only one in-situ instrument, and it has a methane reservoir in its optical path. Orbiters cannot see below ~4 km or at night. Reconciliation requires a sink much faster than known gas-phase photochemistry.
- **Standing 2026:** Open. The 2025 reanalysis narrowed the question to the instrument. No published sealed-cell test was found.
- **What would settle it:** The sealed-cell repeat; an independent in-situ sensor; near-surface night-time remote sensing; and an isotopic signature (δ13C or D/H) of any methane.
- **Main proponents:** Martian origin: C. Webster and P. Mahaffy (TLS/SAM), J. Moores (containment), M. Giuranna (PFS). Doubt: S. Viscardy, D. Catling, K. Zahnle; the TGO instrument teams.
- **Type:** Observing (B4) and explaining (B4b).

### Inferences
- The three detections share one anatomy: (i) a weak feature, (ii) a reduction or calibration step that can create or erase it, (iii) a model-dependent step from feature to abundance, and (iv) a step from abundance to "anomalous, perhaps biogenic" that depends on how complete known chemistry is. Only (i)–(ii) are observing. Steps (iii)–(iv) are explaining. Most of the public dispute takes place at (iii)–(iv), while the decisive evidence sits at (i)–(ii).
- In both the Venus PH3 and Mars CH4 cases, proponents reconcile non-detections by appeal to temporal variation (diurnal or episodic). Such cycling claims can be tested only with measurements matched in time and altitude, which are seldom available.
- The K2-18 b sequence shows the field's correction method working within about a year. Public data allowed several independent pipelines and retrieval codes, plus open molecule lists. The Venus lessons paper (Clements 2024) argues for the same norms.

### Gaps
- I found no refereed 2025–26 JCMT-Venus abundance paper, no SOFIA limit value in a primary source, and no current DAVINCI schedule. The search budget ran out.
- I could not check whether new JWST transits of K2-18 b (MIRI or NIRSpec) were published in 2026.
- I found no 2025–26 Curiosity TLS response to Viscardy et al., and no TGO pptv-level limits in a primary source.

## 2. Interstellar, cometary and returned-sample chemistry

### Takeaway
The best-documented frontier here is the D/H of comet 67P's water. One dataset (Rosetta/ROSINA) gave two conflicting answers in 2024 and 2026, and that decides whether Jupiter-family comets could have supplied much of Earth's water. For Bennu, the organics being indigenous is close to settled. Where they were synthesised (inherited from the cold cloud or outer disk, or made on the parent body) is still being worked out. The question of whether complex organic molecules (COMs) form on grains or in the gas phase could not be checked this session.

### Cited findings: frontier binaries

#### B5. Bulk D/H of comet 67P's water: ~3× terrestrial or near-terrestrial (observing binary)
- **Claim:** Water from the nucleus of 67P/Churyumov–Gerasimenko has D/H ≈ 3× VSMOW (~5 × 10⁻⁴).
- **Negation:** For the same comet and quantity, D/H in the nucleus water is near-terrestrial (≈ VSMOW). The high values are a local artefact of dust-borne ice sublimating near the spacecraft.
- **Observings, claim side:**
  - (obs) Early ROSINA/DFMS mass spectra gave about 3× Earth's value: Altwegg et al. 2015, *Science* 347, 1261952. A later analysis of 150 spectra across mission phases gave (5.01 ± 0.41) × 10⁻⁴: Müller et al. 2022, *A&A* 662, A69. Both are as cited in Müller et al. 2026.
  - (obs) Müller et al. 2026 used more than 7,600 DFMS neutral-mode measurements over the whole mission. They give D/H = (4.67 ± 0.59) × 10⁻⁴, about 3× VSMOW (taken as 1.56 × 10⁻⁴). They also give ¹⁶O/¹⁷O = 1623 ± 206 (~40% ¹⁷O-enriched relative to terrestrial water) and ¹⁶O/¹⁸O = 377 ± 48 (~25% ¹⁸O-enriched). The ratios vary little with mission phase, latitude or distance. The authors explicitly dispute the variability that Mandt et al. report. Source: *A&A* 713, A120 (accepted 2 July 2026), https://doi.org/10.1051/0004-6361/202661244 (PDF read: https://www.aanda.org/10.1051/0004-6361/202661244/pdf).
- **Observings, negation side:**
  - (obs reanalysis) Mandt et al. 2024 reanalysed more than 4,000 water-isotope measurements from the whole mission (the abstract's figure; press releases say >16,000, a discrepancy not resolved here). They found that local D/H rises with dust near the spacecraft. In well-mixed gas farther from the nucleus, D/H is close to terrestrial, like other Jupiter-family comets. The mechanism they propose is that HDO preferentially adsorbs on dust grains (based on laboratory work). Source: *Sci. Adv.* 10, eadp2191 (Nov 2024), https://doi.org/10.1126/sciadv.adp2191 (abstract via https://boris-portal.unibe.ch/entities/publication/334aef0e-f140-4b69-a594-8fb8e3e13127; NASA summary https://ipb.gsfc.nasa.gov/600/public-nuggets/042125-nugget.pdf; release https://astrobiology.com/2024/12/09/nasa-led-team-links-comet-water-to-earths-oceans/). No numerical revised value was seen [unverified].
  - (obs, context) Lis et al. 2019 (*A&A* 625, L5) report that D/H falls as a comet's active fraction rises, with hyperactive comets near-terrestrial (as cited in Müller 2026). Values for comets 103P and 46P are [unverified].
- **Field adds:** "Bulk" D/H requires a model of coma sources: nucleus versus distributed sources on dust (model). VSMOW is a reference convention (conv). Reading D/H as evidence of interstellar inheritance is a model (Müller 2026 cite Cleeves et al. 2014, *Science* 345, 1590).
- **Why hard:** Rosetta sampled only the local coma at the spacecraft. HDO and H3¹⁶O⁺ share m/z 19, and Müller 2026 report hydronium forming inside the DFMS ion source. That ion-source chemistry is therefore a likely point of disagreement between the analyses; this is my inference.
- **Standing 2026:** Reopened in 2024 and contested in 2026 by the instrument team. Open.
- **What would settle it:** An independent reanalysis with shared raw data and code; joint modelling of dust and gas sources; and D/H for many more Jupiter-family comets measured remotely.
- **Main proponents:** High: K. Altwegg, M. Rubin, D. Müller (ROSINA, Bern). Near-terrestrial: K. Mandt (NASA GSFC/JHU-APL) and co-authors.
- **Type:** Observing (the value of a measured quantity).

#### B6. Origin of Earth's water (explaining; three accounts split into binaries)
- **Scope:** Three accounts compete: chondritic asteroids, comets, and nebular-gas ingassing. They are not mutually exclusive in a mass balance, so I split them.
  - **B6a:** Earth's exogenous water came mainly from chondritic (asteroidal) bodies, versus mainly from comets.
  - **B6b:** A measurable fraction of mantle hydrogen comes from solar-nebula H2 dissolved into a magma ocean, versus none.
  - **B6c:** The chondritic water came mainly from inner-system (enstatite-like, non-carbonaceous) material, versus mainly from outer-system (carbonaceous) material.
- **Observings:**
  - (obs) Seawater D/H is ≈1.56 × 10⁻⁴ (VSMOW; Müller 2026, above).
  - (obs) The 67P values are given in B5. Under the 2026 value, Müller et al. conclude that comets like 67P contributed little. Under the 2024 reanalysis, Mandt et al. say that possibility is reopened (sources in B5).
  - The following were not checked this session [unverified]: carbonaceous chondrite D/H close to terrestrial; near-terrestrial D/H for 103P/Hartley 2 (Hartogh et al. 2011, *Nature*); hydrogen in enstatite chondrites sufficient for several oceans (Piani et al. 2020, *Science*); low-δD deep-mantle hydrogen in Baffin Island lavas read as nebular (Hallis et al. 2015, *Science*); cometary xenon making up part of Earth's atmospheric Xe (Marty et al. 2017, *Science*); and Mo-isotope evidence that Earth accreted late carbonaceous material (Budde et al. 2019, *Nat. Astron.*).
- **Field adds:** Isotope end-member mass-balance models assume D/H is preserved through accretion, magma-ocean degassing, core formation and escape (model). The "late veneer" is a model construct.
- **Why hard:** Earth's bulk hydrogen budget, including any hydrogen in the core, is unknown. D/H fractionates during escape and degassing. And comet D/H spans a wide range even within one class.
- **Standing 2026:** Open. A chondritic majority is the common view [unverified]. The cometary share is re-contested (B5). The nebular share is open.
- **What would settle it:** A core hydrogen budget; D/H of undegassed deep-mantle samples; a cometary sample return; and noble-gas and N isotopes jointly with D/H.
- **Proponents:** Comets reopened: Mandt. Comets minor: Altwegg and Müller. Enstatite or inner-system: Piani [unverified]. Nebular component: Hallis [unverified].
- **Type:** Explaining.

#### B7. Bennu soluble organics are indigenous, not terrestrial contamination (observing binary)
- **Claim:** The amino acids, nucleobases and ammonia measured in OSIRIS-REx samples of Bennu are extraterrestrial, present in the asteroid before the samples were collected.
- **Negation:** For the same samples and analyses, the compounds are terrestrial contaminants introduced during return or curation.
- **Observings:** (obs) The samples contain 14 of the 20 protein amino acids plus 19 non-protein amino acids, and all five nucleobases of DNA and RNA. They hold ammonia, amines, formaldehyde, carboxylic acids, PAHs and N-heterocycles, and ~10,000 N-bearing species. Bennu is richer in C, N and NH3 than Ryugu and most meteorites. The chiral non-protein amino acids are racemic or nearly so. ¹⁵N enrichments are present. The samples were studied without uncontrolled exposure to Earth's biosphere. Source: Glavin, Dworkin et al. 2025, *Nat. Astron.* (29 Jan 2025), https://doi.org/10.1038/s41550-024-02472-9 (https://ntrs.nasa.gov/citations/20250001355; https://www.natureasia.com/ja-jp/nature/pr-highlights/15148).
- **Field adds:** Several observations together count as evidence of an abiotic, extraterrestrial origin: a racemic distribution, non-protein amino acids, and ¹⁵N enrichment (inference by convention of the field). The specific contamination-control protocols were not seen [unverified].
- **Sub-binary B7b (observing):** Do non-protein chiral amino acids in pristine returned asteroid samples carry an L-enantiomeric excess? For Bennu the answer is no: they are racemic or nearly so. The authors infer that life's L-preference may not come from biased molecules delivered by impacts (Glavin 2025, above; https://physicsworld.com/a/asteroid-bennu-contains-the-stuff-of-life-sample-analysis-reveals). L-excesses reported in Murchison (isovaline) are [unverified].
- **Related:** Ryugu yielded amino acids (Physics World mentions 23 amino-acid forms) and uracil (Oba et al. 2023, *Nat. Commun.*) [unverified primary]. No ribose was found in Bennu as of Feb 2025, and no complex polymers (Physics World, above).
- **Standing 2026:** Effectively settled as indigenous for Bennu. Nothing has been retracted.
- **What would settle the residue:** Compound-specific δ¹³C, δ¹⁵N and δD of individual amino acids and nucleobases.
- **Proponents:** Glavin, Dworkin and the OSIRIS-REx team. No organised opposition was found.
- **Type:** Observing.

#### B8. Where Bennu's N-rich organics were synthesised (explaining)
- **Claim:** Bennu's amino acids and N-heterocycles were mainly synthesised on the parent body, in low-temperature, ammonia-rich aqueous fluids.
- **Negation:** They were mainly synthesised before accretion, in cold molecular-cloud or outer-disk ices, and inherited intact.
- **Observings:** (obs) ¹⁵N enrichments in the ammonia and N-bearing soluble molecules point to formation in a cold molecular cloud or the outer disk. (obs) The relative abundances of amino acids and soluble organics point to low-temperature reactions, possibly in NH3-rich fluids. The parent body likely accreted ices where NH3 ice was stable. Source: Glavin 2025, https://ntrs.nasa.gov/citations/20250001355. (obs) An evaporite sequence of sodium phosphates, carbonates, sulfates, chlorides and fluorides, including halite and 11 salt minerals in total, records brine evaporation on the parent body. Source: McCoy et al. 2025, *Nature* 637, 1072–1077, https://doi.org/10.1038/s41586-024-08495-6 (https://www.sci.news/space/amino-acids-salts-asteroid-bennu-samples-13624.html). (interpretation, press) ²⁶Al heating kept pockets of water liquid, and brines may have templated organic reactions (Physics World, above).
- **Split:** As posed, the binary is too coarse. A proper version applies it per compound class. For precursors (NH3, HCN, H2CO), the evidence favours inheritance. For final products (amino acids), parent-body synthesis is favoured. A two-stage account is the likely convergence; this is my inference.
- **Standing 2026:** Narrowing.
- **What would settle it:** Isotopic signatures of individual molecules compared with laboratory products of ice irradiation and of aqueous Strecker-type synthesis.
- **Type:** Explaining.

#### B9. COMs in cold cores: grain-surface versus gas-phase formation (explaining) [unverified: not checked this session]
- **Claim:** The gas-phase COMs seen at ~10 K in prestellar cores (e.g., CH3OCHO, CH3OCH3, CH3CHO) form mainly on icy grain surfaces and are released by non-thermal desorption.
- **Negation:** In the same cores, they form mainly by gas-phase reactions of desorbed precursors such as CH3OH and radicals.
- **Observings (all [unverified]):** COMs detected in cold cores such as L1544 and B1-b (Bacmann et al. 2012; Cernicharo et al. 2012; Jiménez-Serra et al. 2016). JWST/MIRI ice features assigned to ethanol, acetaldehyde, methyl formate and possibly acetic acid toward the protostars IRAS 2A and IRAS 23385 (Rocha et al. 2024, *A&A*). Laboratory CO-ice hydrogenation at ~10 K yielding glycolaldehyde, ethylene glycol and glycerol (Fedoseev et al. 2015, 2017), and glycine without energetic processing (Ioppolo et al. 2021, *Nat. Astron.*).
- **Field adds:** Rate networks (gas-phase routes, Balucani et al. 2015; non-diffusive grain chemistry, Jin & Garrod 2020) are model constructs. The desorption efficiency at 10 K is the crux [unverified].
- **Why hard:** Ices are seen only in absorption toward background or embedded sources. Gas is seen in emission from different volumes. Desorption may fragment COMs.
- **Standing 2026:** Open for cold cores. Hot cores and corinos are broadly attributed to sublimated grain products [unverified].
- **What would settle it:** Ice and gas abundances in the same lines of sight (JWST + ALMA); D/¹³C fractionation links; laboratory yields for non-thermal desorption.
- **Type:** Explaining.

### Inferences
- B5 is a clean case where two teams read one archive differently. The disagreement lies in the observing step (source attribution in the coma), not in the theory.
- The Bennu results move origin-of-life chirality claims from "delivered excess" toward "excess generated on Earth", as the authors themselves say.

### Gaps
- Not checked: numerical Mandt 2024 values; Ryugu primary papers (Naraoka 2023; Oba 2023); any 2025–26 Bennu sugar or ribose reports; presolar-grain abundances in Bennu or Ryugu; all COM primary literature; enstatite-chondrite hydrogen papers from 2024–25.

## 3. Atmospheric chemistry open problems

### Takeaway
**Nothing in this section was checked in this session.** The search budget was spent before these topics were reached. Every item is [unverified] and is written from prior knowledge as leads for checking. References are given as author, year and journal only, with no DOIs, to avoid unverified identifiers. A shared feature: most of these "problems" are budget residuals, meaning a measured concentration or rate minus a modelled one. So the observing (the concentration) and the explaining (the missing term) separate cleanly.

### Cited findings: frontier binaries (all [unverified])

#### B10. Daytime HONO: is there an extra source, and what is it? [unverified]
- **B10a (observing, residual):** *Claim:* In sunlit boundary-layer air, HONO exceeds the photostationary state set by OH + NO formation and by photolysis and OH loss. This implies an extra source of roughly 0.1–several ppbv h⁻¹ in polluted air. *Negation:* Under the same conditions, once instrument interferences are removed, HONO matches the photostationary state within uncertainty.
- **B10b (explaining):** *Claim:* The extra daytime source is mainly photolysis of particulate nitrate (renoxification), enhanced 10 to more than 100 times relative to gas-phase HNO3. *Negation:* It is mainly ground-surface chemistry: photo-enhanced NO2 conversion on organic or humic surfaces, HNO3 photolysis on surfaces, and soil nitrite emission.
- **Observings:** Wet-chemical (LOPAP), CIMS and DOAS/IBBCEAS measurements in urban, forest and marine air. Proposed sources: photosensitised NO2 on humic films (Stemmler et al. 2006, *Nature*); soil nitrite (Su et al. 2011, *Science*); canopy HNO3 photolysis (Zhou et al. 2011, *Nat. Geosci.*); a gas-phase source inferred from Zeppelin profiles (Li et al. 2014, *Science*), challenged in a comment (Ye et al. 2015); aircraft evidence for nitrate photolysis over the remote ocean (Ye et al. 2016, *Nature*); field evidence at Cape Verde (Andersen et al. 2023, *Sci. Adv.*). Enhancement factors are disputed; for example, Romer et al. 2018 (*ES&T*) found smaller values.
- **Field adds:** The "missing source" is computed as measured HONO minus the photostationary state (reconstruction plus model).
- **Why hard:** HONO lives only ~10–20 min by day and has steep near-ground gradients. Instruments disagree, and the source term is a small difference between large terms.
- **Standing 2026:** B10a is narrowing toward "yes, a source exists" in most settings. B10b is open and probably depends on the environment.
- **Settle:** Flux and vertical-gradient measurements; ¹⁵N-labelled nitrate photolysis on real aerosol; intercomparisons that remove interferences.
- **Proponents:** Nitrate photolysis: C. Ye, X. Zhou, L. Carpenter group. Ground or soil: H. Su, U. Pöschl. Gas-phase: X. Li, F. Rohrer, A. Hofzumahaus.

#### B11. Winter-haze sulfate on the North China Plain [unverified]
- **B11b (explaining):** *Claim:* In winter haze (high humidity, high NH3), most rapidly forming particulate sulfate comes from S(IV) oxidised by dissolved NO2 in aerosol water at near-neutral pH (~5.4–6.2). Sources: Cheng et al. 2016, *Sci. Adv.*; Wang et al. 2016, *PNAS*. *Negation:* Under the same conditions, NO2 oxidation is minor. Other pathways dominate: Mn or Fe-catalysed O2 oxidation on aerosol surfaces (Wang et al. 2021, *Sci. Adv.*), H2O2 oxidation enhanced by ionic strength (Liu et al. 2020, *PNAS*), and others.
- **B11a (observing):** *Claim:* A substantial part (tens of percent) of the sulfate measured by ion chromatography in Beijing winter haze is actually hydroxymethanesulfonate (HMS) from HCHO + S(IV) (Moch et al. 2018, *GRL*; Song et al. 2019, *ACP*). *Negation:* HMS is a minor part. Ion chromatography sulfate is overwhelmingly real sulfate.
- **Observings:** Sulfate fractions rise in PM2.5 during haze, and models underpredict sulfate. Thermodynamic pH estimates of ~4.2–4.7 make the NO2 pathway minor (Liu et al. 2017, *GRL*; Song et al. 2018, *ACP*). Δ¹⁷O of sulfate has been used to apportion pathways.
- **Field adds:** Aerosol pH is not measured directly. It comes from thermodynamic models (ISORROPIA-II, E-AIM) using NH3/NH4⁺ partitioning, so the ranking of pathways rests on a model construct.
- **Why hard:** Rates depend on pH to the power of several units. Kinetics at high ionic strength are poorly known. Standard ion chromatography cannot separate HMS from sulfate.
- **Standing 2026:** Open. There is broad agreement that several pathways contribute.
- **Settle:** Direct particle pH measurement (Raman microspectroscopy, indicators); speciated S(IV) and HMS measurement; Δ¹⁷O and δ³⁴S calibrated per pathway; kinetics in concentrated solutions.
- **Proponents:** NO2: Y. Cheng, H. Su, U. Pöschl; G. Wang, R. Zhang. H2O2: T. Liu, J. Abbatt. Mn: W. Wang. HMS: D. Jacob, J. Moch, S. Song.

#### B12. Missing OH reactivity and excess OH in low-NO isoprene air [unverified]
- **B12a (observing, residual):** *Claim:* In forest air, measured total OH reactivity exceeds the sum of (measured species × rate constants) by a large fraction (often 30–70% or more). *Negation:* After correcting instrument artefacts, measured and summed reactivity agree within uncertainty.
- **Observings:** Total OH loss by LIF flow tube (Kovacs & Brune 2001). Comparative reactivity method (Sinha et al. 2008, *ACP*). A Michigan forest showed missing reactivity with a terpene-like temperature dependence (Di Carlo et al. 2004, *Science*). Large gaps in boreal and Amazon air (Sinha et al. 2010; Nölscher et al. 2016, *Nat. Commun.*). An instrument intercomparison at SAPHIR (Fuchs et al. 2017, *AMT*).
- **B12b (observing, then explaining):** *Claim:* OH measured in low-NO, isoprene-rich air exceeds standard models by factors of 2–10 (Lelieveld et al. 2008, *Nature*, Amazon; Hofzumahaus et al. 2009, *Science*, Pearl River Delta). *Negation:* The excess is largely an LIF interference, revealed by chemical-modulation inlets (Mao et al. 2012, *ACP*; Novelli et al. 2014). Isoprene peroxy-radical H-shift chemistry (Peeters et al. 2009; Crounse et al. 2011) explains part of the remainder.
- **Field adds:** "Missing reactivity" and "OH recycling" are a residual and a mechanism construct respectively.
- **Standing 2026:** Both are narrowing. Better speciation of oxygenated VOCs closes part of B12a. B12b is partly interference and partly mechanism.
- **Settle:** Full speciation (PTR-ToF, iodide-CIMS); blind instrument intercomparisons; chamber runs at ambient NO.
- **Proponents:** W. Brune, J. Williams, J. Lelieveld; A. Hofzumahaus, H. Fuchs; J. Peeters; J. Mao.

#### B13. New-particle formation in polluted megacities [unverified]
- **Scope split:** No single mechanism governs every regime. The proposed regimes are: coastal (iodine oxoacids: Sipilä et al. 2016, *Nature*; He et al. 2021, *Science*); boreal (H2SO4 + highly oxygenated molecules: Kirkby et al. 2016, *Nature*); upper troposphere (HNO3–H2SO4–NH3: Wang et al. 2020 and 2022, *Nature*); urban (H2SO4–amine). So the binary is posed for the urban regime only.
- **Claim:** In Chinese megacity boundary layers, despite high condensation sinks, the observed nucleation rates are quantitatively explained by H2SO4–dimethylamine clustering (Yao et al. 2018, *Science*, Shanghai; Cai et al. 2021, *ACP*, Beijing).
- **Negation:** Under the same conditions, H2SO4–dimethylamine cannot account for the observed rates. Organics, HNO3–NH3 or nucleation aloft followed by mixing down are required.
- **Observings:** Cluster composition from CI-APi-TOF. The CLOUD chamber found NH3 insufficient (Kirkby et al. 2011, *Nature*) and dimethylamine strongly enhancing (Almeida et al. 2013, *Nature*). Kulmala and co-workers framed the "urban NPF puzzle".
- **Why hard:** Sub-2 nm clusters sit near detection limits. Amines are present at pptv. Growth from 2 to 10 nm needs organic vapours. The vertical structure is unsampled.
- **Standing 2026:** For nucleation, narrowing in favour of H2SO4–amine, with organics needed for growth. How much upper-tropospheric nucleation matters globally is open.
- **Settle:** Co-located cluster, amine, H2SO4 and HOM measurements; vertical profiles; chamber-to-field rate tests.
- **Proponents:** M. Kulmala and V.-M. Kerminen; J. Kirkby (CLOUD); L. Wang (Fudan); J. Jiang (Tsinghua).
- **Type:** Explaining.

#### B14. Urban SOA: volatile chemical products versus mobile sources [unverified]
- **Claim:** In US and European cities, volatile chemical products (VCPs: solvents, coatings, personal-care products) rival or exceed motor vehicles as the main anthropogenic SOA-precursor class (McDonald et al. 2018, *Science*; Coggon et al. 2021, *PNAS*).
- **Negation:** In the same cities, mobile-source emissions, including intermediate-volatility organics (IVOCs), remain the dominant anthropogenic SOA precursors.
- **Background observings:** Mexico City SOA was underpredicted ~8× (Volkamer et al. 2006, *GRL*). Semi-volatile and intermediate-volatility organics were added (Robinson et al. 2007, *Science*). Chamber vapour-wall losses cause yields to be underestimated by up to ~4× (Zhang et al. 2014, *PNAS*). Autoxidation produces highly oxygenated molecules (Ehn et al. 2014, *Nature*).
- **Field adds:** Volatility-basis-set yields are a model construct. PMF factors from aerosol mass spectrometry are statistical reconstructions, and naming the factors is a convention.
- **Standing 2026:** Narrowing toward VCPs as a major source in US cities. Their share elsewhere is open.
- **Settle:** VCP-specific SOA tracers; eddy-covariance emission fluxes; revised inventories.
- **Proponents:** B. McDonald, J. de Gouw, M. Coggon, J. Gilman; A. Robinson, S. Pandis. No named opposing group was identified.
- **Type:** Explaining.

#### B15. Share of global methane removed by tropospheric Cl atoms [unverified]
- **Claim:** Cl atoms remove ~2–3% of tropospheric CH4 (Allan et al. 2007, *JGR*, from marine boundary-layer δ¹³C of CH4; Hossaini et al. 2016, *JGR*, model).
- **Negation:** Cl removes about 1% or less (Gromov et al. 2018, *PNAS*, from δ¹³C of CO; Wang et al. 2019, *ACP*, GEOS-Chem ~1%).
- **Observings:** ClNO2 found inland, which means N2O5 uptake on chloride yields Cl at dawn (Thornton et al. 2010, *Nature*). Arctic Cl2 at tens of pptv (Liao et al. 2014, *Nat. Geosci.*). Cl + CH4 has a large ¹³C kinetic isotope effect, which makes the isotope constraint possible.
- **Field adds:** Cl atoms (~10³–10⁴ cm⁻³) are never measured directly. They are inferred from precursors or hydrocarbon-ratio clocks, and the global budget is a model.
- **Standing 2026:** Open. Recent models cluster near ~1%.
- **Settle:** Precursor networks (Cl2, ClNO2, HOCl) across the marine boundary layer; joint δ¹³C-CH4 and δ¹³C-CO time series.
- **Proponents:** R. Hossaini, W. Allan; S. Gromov, C. Brenninkmeijer; X. Wang, D. Jacob.
- **Type:** Explaining, resting on reconstructions.

### Inferences
- In B10–B12 and B15 the observable is a concentration or a loss rate. The contested object is a residual defined against a model. A better model or a better instrument can make such a residual vanish without any new chemistry. Interference corrections have repeatedly shrunk the gaps (B12b), which suggests that "missing" terms should be stated together with the instrument that defines them.
- B11 depends on a quantity, aerosol pH, that no instrument currently reads directly in ambient particles. It is a model output treated as an input.

### Gaps
- No primary source in this section was opened. Developments in 2023–26 are unknown here: for example, whether there is now consensus on nitrate-photolysis enhancement factors, new CLOUD results, or new HMS speciation methods.

## 4. Ocean and Earth-system chemistry

### Takeaway
**Nothing in this section was checked in this session** (the search budget was exhausted). All items are [unverified] leads from prior knowledge. The project already holds entries on the causes and magnitude of the Great Oxidation Event (GOE), so here the GOE appears only as a sequencing question (B20). Nearly every binary in this section is a reconstruction from proxies. What is observed is an element ratio, an isotope ratio or a mineral fabric in a rock. The quantity in dispute (pO2, fO2, alkalinity) comes from a proxy calibration model.

### Cited findings: frontier binaries (all [unverified])

#### B16. "Whiffs" of O2 before the GOE (observing, via reconstruction) [unverified]
- **Claim:** Free O2 built up transiently in surface environments before the GOE. One example is the ~2.50 Ga Mount McRae Shale (Hamersley Basin, Western Australia), where it was enough to mobilise Mo and Re by oxidative weathering.
- **Negation:** In the same intervals, no free O2 built up in air or surface water. The enrichments and isotope shifts are post-depositional or non-oxidative.
- **Claim side:** Mo and Re enrichments in drill core ABDP-9 (Anbar et al. 2007, *Science*). Coeval Δ33S changes (Kaufman et al. 2007, *Science*). Tl and Mo isotopes suggesting oxygenated shelf waters (Ostrander et al. 2019, *Nat. Geosci.*). Mo isotopes in the 2.95 Ga Sinqeni Formation (Planavsky et al. 2014, *Nat. Geosci.*). Cr isotope fractionation in ~2.96 Ga palaeosols (Crowe et al. 2013, *Nature*).
- **Negation side:** Petrographic and synchrotron mapping places Mo and Re in late, post-depositional phases (Slotznick et al. 2018, *Sci. Adv.*). Heavy Cr in ~2.95 Ga iron formation is attributed to modern weathering (Albut et al. 2018, *GCA*).
- **Historically notable, rejected:** Steranes and 2-methylhopanes in 2.7 Ga Pilbara rocks were read as evidence of oxygenic life (Brocks et al. 1999, *Science*). They were later shown to be contamination (Rasmussen et al. 2008, *Nature*; French et al. 2015, *PNAS*).
- **Field adds:** Weathering and mobility models connect element enrichments to pO2 thresholds (model). The threshold for S-MIF preservation, pO2 < ~10⁻⁵ PAL, is photochemical (Pavlov & Kasting 2002) (model).
- **Why hard:** Metamorphism and fluid flow remobilise trace metals. Proxies have different thresholds and record water versus air. Cores are few.
- **Standing 2026:** Contested.
- **Settle:** Fresh cores with sample-by-sample petrography. Several proxies (Mo, Tl, Se, N, Cr) measured on the same aliquots. In-situ analysis of distinct mineral generations.
- **Proponents:** Pro-whiff: A. Anbar, T. Lyons, N. Planavsky, C. Ostrander. Sceptics: S. Slotznick, W. Fischer.

#### B17. Atmospheric O2 at ~1.4 Ga (observing, via reconstruction) [unverified]
- **Claim:** pO2 was below ~0.1–1% PAL, too low for animal-grade aerobic respiration. Evidence: unfractionated Cr isotopes (Planavsky et al. 2014, *Science*) and low productivity inferred from Δ17O in sulfate (Crockford et al. 2018, *Nature*).
- **Negation:** At ~1.4 Ga, pO2 was at least ~4% PAL. Evidence: trace-metal patterns in the Xiamaling Formation, North China (Zhang et al. 2016, *PNAS*), and fractionated Cr in Mesoproterozoic shales (Canfield et al. 2018, *Nat. Commun.*).
- **Scope:** pO2 probably varied through the 1.8–0.8 Ga interval, so a clean binary must be pinned to one time slice. Low averages and local peaks could both be true.
- **Context (prior state):** The euxinic "Canfield ocean" (Canfield 1998, *Nature*) was largely replaced by a picture of a ferruginous deep ocean with euxinic margins (Poulton et al. 2010, *Nat. Geosci.*; Planavsky et al. 2011, *Nature*).
- **Field adds:** The Cr proxy assumes that Cr(III) oxidation needs Mn oxides, and therefore a pO2 threshold (model).
- **Standing 2026:** Open.
- **Settle:** Independent proxies on the same well-dated sections, and quantitative proxy calibration.
- **Proponents:** Low: N. Planavsky, C. Reinhard, P. Crockford. Higher: D. Canfield, S. Zhang, X. Wang.

#### B18. "Dark oxygen" from abyssal polymetallic nodules (observing, with an explaining tail) [unverified; a DOI fetch failed, see Gaps]
- **Claim:** On the nodule-covered seafloor of the Clarion–Clipperton Zone (~4 km depth), O2 is produced in darkness without photosynthesis. In situ benthic-chamber incubations showed net O2 rising, and the authors proposed electrolysis of seawater driven by surface potentials measured on nodules (up to ~0.95 V reported). Source: Sweetman et al. 2024, *Nat. Geosci.*
- **Negation:** In the same chambers and conditions, there is no net O2 production. The rises are artefacts (for example, air trapped during deployment), and nodule potentials cannot drive sustained electrolysis. Rebuttal preprints appeared in 2024–25, some from authors linked to mining interests.
- **Why hard:** Few deployments. Water splitting needs ~1.23 V plus an overpotential and a current path. Earlier CCZ chamber work reported only O2 consumption.
- **Field adds:** "Electrolysis" is a proposed mechanism (model), not an observation.
- **Standing 2026:** Contested. I have no record of replication.
- **Settle:** Independent bubble-free replication; ¹⁸O-labelled water to trace the source of the O2; co-measurement of H2, since water splitting gives H2:O2 = 2:1 (my inference from stoichiometry); and current measurements.
- **Proponents:** A. Sweetman, F. Geiger. Critics: not identified here.
- **Relevance:** Seafloor redox geochemistry and nodule electrochemistry. Policy debates over deep-sea mining heighten the interest on both sides.

#### B19. Upper-mantle fO2 through time (observing, via reconstruction) [unverified]
- **Claim:** Upper-mantle fO2 has stayed within ~0.5 log units of today's value (~FMQ) since at least 3.5 Ga, and perhaps since the Hadean. Evidence: V/Sc in Archean basalts (Li & Lee 2004, *EPSL*; Canil 1997, *Nature*) and Ce anomalies in Hadean zircons (Trail et al. 2011, *Nature*).
- **Negation:** fO2 rose by roughly 1 log unit or more between ~3.5 and ~1.9 Ga. Evidence: V partitioning between olivine and melt in komatiites (Nicklas et al. 2019, *GCA*) and V/Sc in eclogite xenoliths (Aulbach & Stagno 2016, *Geology*).
- **Field adds:** The oxybarometers rest on partitioning calibrations plus assumptions about the source and the degree of melting (model). The link to the GOE runs through the oxidation state of volcanic gases, which is an explaining step (Kasting et al. 1993; Holland 2002).
- **Standing 2026:** Open.
- **Settle:** Measuring Fe³⁺/ΣFe directly by XANES on Archean melt inclusions, and cross-calibrating proxies.
- **Proponents:** Constant: C.-T. Lee, D. Canil. Oxidation: R. Nicklas, I. Puchtel, S. Aulbach.

#### B20. GOE as a sequence: one irreversible step or oscillation until ~2.22 Ga? (observing, plus convention) [unverified; cross-reference to the project's GOE entries]
- **Claim:** After S-MIF first disappeared (~2.43–2.33 Ga), atmospheric O2 fell back below the S-MIF threshold at least once. Permanent oxygenation came only around 2.22 Ga. Evidence: multiple S isotopes in Transvaal cores (Poulton et al. 2021, *Nature*) and asynchronous S-MIF loss in Western Australia (Philippot et al. 2018, *Nat. Commun.*).
- **Negation:** Once lost, S-MIF stayed lost. Later S-MIF is recycled from older sediments, a crustal memory effect (Reinhard, Planavsky & Lyons 2013, *Nature*). Onset ages: ~2.33 Ga (Luo et al. 2016, *Sci. Adv.*) and ~2.43 Ga (Gumsley et al. 2017, *PNAS*).
- **Field adds:** Defining the GOE by S-MIF loss, by permanent oxygenation or by redbeds is a convention (conv). The threshold is a model.
- **Standing 2026:** Narrowing toward a protracted, oscillatory transition, though still contested.
- **Settle:** In-situ multiple-S isotopes in individual pyrite generations; correlation across cratons; tighter geochronology.

#### B21. Reverse weathering as a major Precambrian alkalinity sink (explaining) [unverified]
- **Claim:** Before silica-secreting organisms, high dissolved silica allowed extensive authigenic clay formation (reverse weathering). This consumed alkalinity, kept pCO2 higher and kept seawater pH lower (Isson & Planavsky 2018, *Nature*). Support comes from Li isotopes rising through Earth history (Kalderon-Asael et al. 2021, *Nature*).
- **Negation:** Reverse weathering was a minor sink. As today, the Precambrian alkalinity balance was set mainly by silicate weathering against carbonate burial.
- **Field adds:** Box models of the carbon and silica cycles (model). Li-isotope fluxes need assumptions about fractionation factors (model).
- **Standing 2026:** Open.
- **Settle:** Independent proxies (K, Mg, Si isotopes) and authigenic-clay inventories in Precambrian sediments.
- **Type:** Explaining.

### Inferences
- In this section the "observing" is almost always a rock measurement: Mo concentration, δ53Cr, Δ33S, V/Sc. The atmospheric or mantle variable comes from a calibration model. A binary about pO2 is therefore really a binary about a proxy's transfer function. Disagreements often trace to that transfer function rather than to the data.
- B16 and B20 test the field's sequencing claims: whether events were prior, contemporaneous or repeated. Whether the transition was a single step or a cycle (B20) is exactly the kind of "changing and changing back" the framing project tracks.

### Gaps
- Not opened this session: Sweetman et al. 2024. A DOI fetch failed because the URL was not on the allowlist, so the DOI 10.1038/s41561-024-01480-8 is [unverified]. The rebuttals and any 2025–26 follow-up are also unchecked. So are recent whiff studies (2023–26), a 2026 mantle-redox synthesis, and new GOE geochronology.

## 5. Cosmochemistry

### Takeaway
**Nothing in this section was checked in this session** (the search budget was exhausted). All items are [unverified]. One clear pattern stands out. The observing halves are robust and replicated: radiometric ages and nucleosynthetic isotope anomalies measured with MC-ICPMS, TIMS or SIMS. The live disputes are about explaining: what the anomalies and ages mean, and which chronometer assumptions hold. The solar abundance problem and primordial lithium are cross-referenced only (Section 6).

### Cited findings: frontier binaries (all [unverified])

#### B22. Formation of most chondrules: nebular shocks or planetesimal collisions (explaining) [unverified]
- **Scope split:** CB-chondrite chondrules (Gujba, Isheyevo; ~4562.5 Ma) are widely accepted as products of an impact vapour plume (Krot et al. 2005, *Nature*). The binary therefore covers only the dominant population in ordinary and most carbonaceous chondrites.
- **Claim:** That population formed by flash heating of free-floating dust aggregates in nebular gas, by shock waves (Desch & Connolly 2002, *MAPS*; Morris & Desch 2010).
- **Negation:** That population formed as melt droplets or spray from collisions between planetesimals (impact jetting: Johnson et al. 2015, *Nature*; splashing of molten planetesimals: Asphaug et al. 2011, *EPSL*).
- **Observings:** Pb–Pb ages show chondrule formation spanning ~4567.3–4564.7 Ma, starting together with CAIs (Connelly et al. 2012, *Science*). Al–Mg gives ~1–3 Myr after CAIs (Villeneuve et al. 2009, *Science*). Na retained in chondrule olivine implies very high solid densities during formation (Alexander et al. 2008, *Science*). Chondrules and matrix show complementary compositions, including nucleosynthetic W isotopes (Hezel & Palme 2010, *EPSL*; Budde et al. 2016, *PNAS*), which points to one reservoir. Dusty olivine in Semarkona records a ~54 ± 21 µT field (Fu et al. 2014, *Science*). Cooling rates from textures are ~10–1000 K h⁻¹.
- **Field adds:** Complementarity is read as evidence against a planetary origin (inference). The Na constraint is read as dense clumps, which could fit either picture (model).
- **Why hard:** Chondrules record only end states. Several mechanisms may each have operated. The required energy, densities and cooling rates do not fit cleanly into either model.
- **Standing 2026:** Open. Many authors accept more than one mechanism.
- **Settle:** Chondrule-by-chondrule ages, isotopes and palaeomagnetism; whether chondrule and matrix complementarity holds after more replication.
- **Proponents:** Nebular: S. Desch, H. Connolly, D. Hezel, G. Budde. Collisional: B. Johnson, E. Asphaug, I. Sanders.

#### B23. Uniform 26Al and the Pb–Pb age of t₀ (observing, via reconstruction) [unverified]
- **Claim:** At t₀, 26Al/27Al was uniform (canonical ≈ 5.2 × 10⁻⁵) across the CAI and chondrule-forming regions and the parent bodies of achondrites. Al–Mg relative ages can therefore be mapped onto Pb–Pb ages. Desch et al. (2023, *Icarus*) applied this assumption to infer a t₀ older than the measured CAI Pb–Pb age, about 4568.4 Ma.
- **Negation:** 26Al was heterogeneous, lower in some reservoirs. Al–Mg and Pb–Pb ages of the same objects diverge, as in the angrite D'Orbigny (Larsen et al. 2011, *ApJL*; Schiller et al. 2015, *EPSL*), and CAI Pb–Pb ages (4567.30 ± 0.16 Ma; Connelly et al. 2012) stand as t₀.
- **Related observing:** Measured variation in 238U/235U in CAIs requires U-isotope-corrected Pb–Pb ages (Brennecka et al. 2010, *Science*). An earlier uncorrected CAI age of 4568.2 Ma (Bouvier & Wadhwa 2010, *Nat. Geosci.*) is a prior state.
- **Field adds:** Every relative chronometer assumes a uniform initial ratio (conv/model).
- **Standing 2026:** Open.
- **Settle:** Pb–Pb, Al–Mg, Hf–W and Mn–Cr ages measured on the same well-quenched objects, with reservoir-specific ²⁶Al proxies (Δ²⁶Mg*).
- **Proponents:** Homogeneous: S. Desch, N. Kita. Heterogeneous: M. Bizzarro, M. Schiller, K. Larsen.

#### B24. The NC–CC isotopic dichotomy: barrier or timing? (explaining) [unverified]
- **Settled observing (obs):** Bulk meteorites fall into two non-overlapping groups in nucleosynthetic anomalies (ε⁵⁴Cr, ε⁵⁰Ti, Δ¹⁷O, then Mo and W): non-carbonaceous (NC) and carbonaceous (CC) (Warren 2011, *EPSL*; Budde et al. 2016, *EPSL*). Hf–W model ages of iron meteorites show that both reservoirs coexisted from <1 Myr to ~3–4 Myr after CAIs (Kruijer et al. 2017, *PNAS*). Ryugu and Bennu samples belong with CC/CI. Earth is mostly NC-like, with a small CC fraction (Budde et al. 2019, *Nat. Astron.*).
- **B24a Claim:** The two reservoirs were kept apart spatially by the early growth of Jupiter's core, which opened a gap in the disk (Kruijer et al. 2017). **Negation:** The barrier was not Jupiter. It was a pressure bump or a structure at the snowline (Brasser & Mojzsis 2020, *Nat. Astron.*). Another version ties the split to inward drift of the water-ice line (Lichtenberg et al. 2021, *Science*).
- **B24b Claim:** The NC/CC difference is mainly spatial: two coexisting reservoirs. **Negation:** It is mainly temporal: the composition of material falling from the molecular cloud changed with time, and bodies record when they accreted (Nanne et al. 2019, *EPSL*; Burkhardt et al. 2019, *GCA*).
- **Field adds:** The barrier and the infall history are disk-evolution models. The "reservoir" category is a classification by bulk isotope signature: a candidate set whose membership criterion is the sign and size of ε⁵⁴Cr and ε⁵⁰Ti (conv).
- **Standing 2026:** The observing half is settled. B24a and B24b are open.
- **Settle:** Anomaly–age systematics for more NC and CC bodies; recognising the carrier phase for each anomaly; disk models that reproduce the isotopes quantitatively.
- **Proponents:** Jupiter barrier: T. Kleine, T. Kruijer, G. Budde. Pressure bump or snowline: R. Brasser, S. Mojzsis, T. Lichtenberg. Infall timing: C. Burkhardt, J. Nanne.

#### B25. Initial solar-system 60Fe/56Fe: high (~10⁻⁷–10⁻⁶) or low (~10⁻⁸) (observing, via reconstruction) [unverified]
- **Claim:** Initial 60Fe/56Fe was ~10⁻⁷–10⁻⁶, based on in-situ SIMS analysis of chondrule silicates and sulfides (Mishra & Goswami 2014, *GCA*; Mishra et al. 2016, *ApJL*). That level requires late supernova injection.
- **Negation:** Initial 60Fe/56Fe was ~1 × 10⁻⁸, about the galactic background, based on bulk MC-ICPMS of chondrules and differentiated meteorites (Tang & Dauphas 2012, *EPSL*; 2015, *ApJ*). Telus et al. (2012; 2018, *GCA*) showed that high SIMS ratios can arise from statistical bias at low counts and from Fe–Ni redistribution.
- **Field adds:** Inferences about supernova injection, or Wolf–Rayet winds supplying 26Al without 60Fe, are explaining models (model).
- **Standing 2026:** Narrowing toward the low value.
- **Settle:** Counting-statistics-robust SIMS checked against bulk analyses on the same objects.
- **Proponents:** High: R. Mishra, J. Goswami. Low: H. Tang, N. Dauphas, M. Telus.
- **Presolar-grain link:** Presolar SiC, graphite, oxides and silicates carry anomalies of up to orders of magnitude, matched to AGB stars, supernovae and novae (obs: NanoSIMS). An open explaining question is whether bulk anomalies such as ε⁵⁴Cr come from selective thermal processing of carriers like ⁵⁴Cr-rich nanospinels (Dauphas et al. 2010, *ApJ*; Qin et al. 2011, *GCA*) or from heterogeneous infall (B24b).

### Inferences
- In cosmochemistry the observing layer, meaning isotope ratios and their uncertainties, is comparatively secure. What is contested is the set of shared assumptions: uniform initial ratios, the identity of the carrier phase, disk architecture. Any rewrite should present ages as "measured ratio + assumed initial ratio + decay constant", with the assumption stated separately.

### Gaps
- No 2023–26 primary source was opened. I could not confirm the Desch et al. 2023 t₀ value, any new CAI age papers (2024–26), or Bennu and Ryugu presolar-grain abundances.

## 6. Further candidate binaries (one line each; all [unverified] unless a source is given)

### Takeaway
These are shorter or lower-priority candidates for later checking. The two project cross-references are flagged.

### Cited findings
- **Cross-reference only (project entry):** the solar abundance problem. Do lower photospheric C, N and O abundances (Asplund et al. 2021, *A&A*) conflict with helioseismology, compared with higher values (Magg et al. 2022, *A&A*)? [unverified]
- **Cross-reference only (project entry):** primordial lithium. Is the ⁷Li abundance on the Spite plateau about 3× below the BBN+CMB prediction because of stellar depletion, or because of new physics? [unverified]
- **2020–22 methane growth surge:** was it driven mainly by more microbial emissions (falling δ¹³C-CH4) or by less OH (explaining)? [unverified]
- **Carbonate compensation depth:** did the ~1 km deepening at the Eocene–Oligocene boundary (Pälike et al. 2012, *Nature*) come from carbonate shifting from shelf to basin, or from more weathering-supplied alkalinity (explaining)? [unverified]
- **Archean ocean temperature:** do high-δ¹⁸O cherts record hot oceans, or seawater whose δ¹⁸O changed (explaining via proxy convention)? [unverified]
- **Banded iron formations:** were they oxidised mainly by photoferrotrophs, or by abiotic UV photo-oxidation of Fe²⁺ (explaining)? [unverified]
- **Hadean water:** do Jack Hills zircon δ¹⁸O values (~4.4 Ga) require liquid water at the surface (reconstruction)? [unverified]
- **Interstellar aromatic infrared bands:** are they carried by free PAHs, given that specific PAHs have been identified by radio in TMC-1 (McGuire et al. 2021, *Science*)? [unverified]
- **Diffuse interstellar bands beyond C60⁺:** do the other bands have molecular carriers that can be identified (observing)? [unverified]
- **Mars organics:** do the decane-to-dodecane alkanes in Gale mudstone (Curiosity SAM, 2025) come from fatty-acid precursors (explaining)? [unverified]
- **Enceladus plume:** do phosphates and organics detected by Cassini CDA point to an ocean able to support prebiotic chemistry (explaining)? [unverified]
- **Lunar water:** in Chang'e-5 and Apollo samples, is it mainly from the solar wind or indigenous (explaining)? [unverified]
- **Earth–Moon isotopic identity:** does it come from a canonical giant impact followed by equilibration, from a synestia, or from an Earth-like impactor (explaining)? [unverified]
- **Phosphine on brown dwarfs and giant planets:** does a single chemical model fit PH3 across them? The JWST Wolf 1130C detection (Oct 2025) is per https://orbitcodex.com/knowledge-base/phosphine-on-venus (an aggregator; primary not seen).
- **Ocean deoxygenation since 1960:** is the ~2% global O2 loss robust, given sparse sampling (reconstruction)? [unverified]

### Inferences
- Most candidates are explaining binaries resting on one proxy convention. Each should be reformulated so that the observing (the measured ratio) appears separately from the proxy transfer function.

### Gaps
- The candidates were not checked against sources this session, because the search and fetch budgets were exhausted.





