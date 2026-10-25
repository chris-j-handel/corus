# How chemistry partitions itself and decides chemical identity and kinds

*Gathering file 01, compiled 23 October 2026.*

**Tags (one per catalogue item):**
- [OBS] observing
- [REC] reconstruction from observings
- [CONV] convention or definition
- [MODEL] model construct
- [SIM] simulation

**Criterion kinds:**
- MP: measured property
- DC: declared convention
- TD: theory-derived

**Notes on reading:**
- [unverified] marks background knowledge not re-checked in this session.
- Bullets under "Inferences" are the compiler's analysis, not the field's claims.
- For institutional [CONV] items nothing is measured; the tag records that the item is a declaration.

**Session limits:** The shared web-search allowance ran out part-way through. Several sources failed or were blocked: nobelprize.org, the PubChem statistics page, PMC, the InChI Trust and several publisher DOI pages. Items that depend on these are flagged, not dropped.

## Key gathered points

- **Official partitions are declared conventions that do not coincide.**
  - IUPAC: 8 divisions (Physical/Biophysical, Inorganic, Organic/Biomolecular, Polymer, Analytical, Environment, Human Health, Nomenclature/Structure Representation).
  - ACS: 32 technical divisions (2024–2026).
  - CAS: every abstract in exactly one of 80 sections (5 groups), plus cross-references.
  - RSC: 72 interest groups and 8 subject communities (2026).
- **Registries count by their own identity rules.**
  - PubChem (12 Sep 2024): 118.6 million compounds, 322.4 million substances.
  - CAS Registry: over 290 million substances (undated 2026 page).
  - ChEBI: over 195,000 entries, with roles kept apart from structural classes; relaunched as ChEBI 2.0 on 20 Oct 2025.
  - ClassyFire's ChemOnt: 4,825 SMARTS-defined categories, up to 11 levels, unchanged since 2016.
- **IUPAC's identity terms depend on context and timescale.**
  - A molecular entity is distinguished by constitution or isotopes, at the precision the purpose needs.
  - A chemical species shares accessible energy levels within the experiment's duration, so conformers can be one species or two.
- **"Element" has two IUPAC senses:** a kind of atom fixed by proton number, and a pure substance of such atoms.
  - This mirrors Paneth's 1931 basic/simple-substance distinction; Scerri argues the Gold Book loses the abstract sense.
  - The SEP (revised March 2026) credits a 1923 IUPAC decision tying table positions to atomic number; Needham's isotope objection stands.
- **IUPAC names secondary bonds by periodic group:** hydrogen (2011), halogen (2013), chalcogen (2019), pnictogen (PAC 2024).
  - Tetrel bond: only an authors' proposal (CrystEngComm 2023); no IUPAC recommendation on IUPAC's lists on 23 Oct 2026.
  - "σ-hole" and "π-hole" have no IUPAC definitions.
- **Bond and mechanism classes are idealizations and inferences.**
  - Ionic, covalent and metallic are poles of a continuum, cut by conventional electronegativity thresholds (~1.7).
  - Mechanism classes are model constructs inferred by elimination; reaction types are book-keeping reconstructions.
- **Nobel Prize in Chemistry:** 2026 (7 Oct) to Kagan and Soai, for non-linear effects and autocatalysis in asymmetric synthesis; 2025 to Kitagawa, Robson and Yaghi, for MOFs.
- **Unverified this session** (search budget exhausted, sites blocked): acid–base scheme dates, metalloid surveys, the Herzfeld criterion, mechanism notations, MeSH, chemical-space estimates, InChI's tautomer policy, exact 2026 PubChem and CAS counts.

## 1. Which subdisciplines chemistry recognizes, and how official bodies divide it

### Takeaway
Official partitions are declared conventions (DC). Each rests on a different principle: subject, compound class, phenomenon, method, industry or profession. They do not map one-to-one onto each other. IUPAC has 8 divisions, the ACS 32 technical divisions, CAS 80 sections in 5 groups, and the RSC 72 interest groups and 8 communities. Only CAS forces exclusive membership: one section per abstract, with cross-references for overlap.

### Cited Findings

**IUPAC** (scope: international standards for the whole discipline)

- [CONV] **Eight numbered divisions.**
  - I Physical and Biophysical Chemistry
  - II Inorganic Chemistry
  - III Organic and Biomolecular Chemistry
  - IV Polymer
  - V Analytical Chemistry
  - VI Chemistry and the Environment
  - VII Chemistry and Human Health
  - VIII Chemical Nomenclature and Structure Representation

  Membership criterion: projects and recommendations are allocated to a division by subject (DC). Divisions draft nomenclature, symbols, units, terminology and conventions for their field.

  Sources: [IUPAC divisions list (2007 page)](https://list.iupac.org/divisions/index.html); [IUPAC overview deck, 2021](https://syrte.obspm.fr/cofusi/presU&C2021/Pres2021_Chimie-IUPAC.pdf). IUPAC's live site still says it has eight divisions (page modified 14 Oct 2024): [IUPAC divisions](https://iupac.org/who-we-are/divisions/).
- [CONV] **Names get re-declared.** IUPAC's 2004 handbook gave Divisions I–VIII the body codes 100–800. It called Division IV the "Macromolecular Division"; by 2007 it was "Polymer". — [IUPAC coding of bodies, 2004](https://media.iupac.org/general/handbook/coding_bodies.html)
- [CONV] **Internal structure re-cut in 2001.** Until December 2001, Division I worked through a Subcommittee on Plasma Chemistry and seven commissions:
  - I.1 symbols, terminology and units
  - I.2 thermodynamics
  - I.3 electrochemistry
  - I.4 chemical kinetics
  - I.5 molecular structure and spectroscopy
  - I.6 colloid and surface chemistry including catalysis
  - I.7 biophysical chemistry

  — [Division I page (2008)](https://moureu.iupac.org/divisions/I)
- [CONV] **Division I's remit** covers critically evaluated physicochemical data, terminology, symbols, units, standards and reference materials. An Interdivisional Subcommittee on Materials Chemistry is shared by the physical/biophysical, inorganic and polymer divisions, so materials chemistry is institutionally a cross-division set. — [Division I scope](https://trs.goldbook.iupac.org/divisions/view/1)
- [CONV] **Division VIII** maintains and develops standard systems for designating chemical structures. These include both conventional names and computer-based identifiers, and the division has an advisory subcommittee of about 40 people. This is the division that owns name-based and identifier-based identity criteria. — [Division VIII page (2008)](https://list.iupac.org/divisions/VIII/index.html)
- [CONV] **Standing committees listed in 2021:**
  - Committee on Chemical Research Applied to World Needs (CHEMRAWN)
  - Chemistry and Industry (COCI)
  - Chemistry Education (CCE)
  - Publications and Cheminformatics Data Standards (CPCDS)
  - Green Chemistry for Sustainable Development (ICGCSD)
  - Terminology, Nomenclature and Symbols (ICTNS)

  The same 2021 deck mentions IUPAC's centenary, celebrated at the 2019 Paris congress (implying a 1919 founding). — [IUPAC overview, 2021](https://syrte.obspm.fr/cofusi/presU&C2021/Pres2021_Chimie-IUPAC.pdf)

  The 2004 handbook also lists an IUBMB–IUPAC Joint Commission on Biochemical Nomenclature, so biochemical names are a shared jurisdiction. — [IUPAC coding, 2004](https://media.iupac.org/general/handbook/coding_bodies.html)
- [CONV] **IUPAC declares subfields by recommendation.** "Definition of materials chemistry" is on IUPAC's recently-published list. It appeared in the same 2024 Chemistry International issue as the pnictogen-bond notice. I did not retrieve the wording of the definition [unverified]. — [IUPAC recently published](https://iupac.org/recommendations/recently-published/); [Chemistry International 2024](https://www.degruyterbrill.com/document/doi/10.1515/ci-2024-0317/html)
- [CONV] **Definitional work open on 23 Oct 2026:**
  - "Comprehensive definition of valence as a quantity" (comments due 30 Nov 2026).
  - Structure-based nomenclature for irregular linear, star, comb and brush polymers with non-identical repeating units (comments due 31 Dec 2026).

  Already published (titles seen, texts not retrieved): a comprehensive definition of oxidation state; a basic classification of polymerization reactions; terminology for chain polymerization; names and symbols for elements 113, 115, 117 and 118; how to name new elements. — [IUPAC under public review](https://iupac.org/recommendations/under-review-by-the-public/); [IUPAC recently published](https://iupac.org/recommendations/recently-published/)

**ACS** (scope: US-based society; membership by voluntary affiliation)

- [CONV] **32 technical divisions** in the February 2024 governance directory:

  | Division | Code | Division | Code |
  |---|---|---|---|
  | Agricultural & Food | AGFD | Agrochemicals | AGRO |
  | Analytical | ANYL | Biochemical Technology | BIOT |
  | Biological Chemistry | BIOL | Business Development & Management | BMGT |
  | Carbohydrate Chemistry & Chemical Glycobiology | CARB | Catalysis Science & Technology | CATL |
  | Cellulose & Renewable Materials | CELL | Chemical Education | CHED |
  | Chemical Health & Safety | CHAS | Chemical Information | CINF |
  | Chemical Toxicology | TOXI | Chemistry & the Law | CHAL |
  | Colloid & Surface | COLL | Computers in Chemistry | COMP |
  | Energy & Fuels | ENFL | Environmental | ENVR |
  | Fluorine | FLUO | Geochemistry | GEOC |
  | History | HIST | Industrial & Engineering | I&EC |
  | Inorganic | INOR | Medicinal | MEDI |
  | Nuclear Chemistry & Technology | NUCL | Organic | ORGN |
  | Physical | PHYS | Polymer | POLY |
  | Polymeric Materials: Science & Engineering | PMSE | Professional Relations | PROF |
  | Rubber | RUBB | Small Chemical Businesses | SCHB |

  Criterion: members enrol themselves in divisions chartered by ACS governance (DC). — [ACS Governance Directory, Feb 2024](https://www.acs.org:443/content/dam/acsorg/about/governance/governance-directory.pdf)
- [OBS] **The count is stable at 32; the labels drift.**
  - An ACS Axial post (9 Dec 2016) states 32, and a division web page (©2026) lists 32.
  - The 2026 page names BIOL "Biochemistry and Chemical Biology" and codes Inorganic as "DIC". The 2024 directory has "Biological Chemistry" and "INOR".

  — [ACS Axial 2016](https://axial.acs.org/multidisciplinary/chemists-acs-technical-divisions); [BIOL division page, ©2026](https://www.divbiolchem.org/resources-fixme/project-three-sng7y-fk9b7)

**CAS** (scope: worldwide chemistry-related literature; membership assigned by indexers)

- [CONV] **80 sections in five groups:**
  - Biochemistry (BIO/SC): sections 1–20
  - Organic (ORG/SC): 21–34
  - Macromolecular (MAC/SC): 35–46
  - Applied (APP/SC): 47–64
  - Physical, Inorganic and Analytical (PIA/SC): 65–80

  Each abstract appears in only one section, chosen by the novelty of the substance or process reported. Cross-references are added where other sections are relevant. — [CAS: The sections of CA](https://www.cas.org/support/documentation/references/ca-sections); [CAS lesson](https://www.cas.org/training/lesson/sections-ca)
- [CONV] **The sections mix partition principles.**
  - By compound class:
    - 23 Aliphatic; 24 Alicyclic; 25 Benzene and condensed benzenoids.
    - Heterocycles split by heteroatom count: 27 one, 28 more than one.
    - 29 Organometallic and Organometalloidal; 30 Terpenes; 31 Alkaloids; 32 Steroids; 33 Carbohydrates; 34 Amino acids, peptides, proteins.
  - By phenomenon: 70 Nuclear Phenomena; 76 Electric; 77 Magnetic.
  - By method: 9 Biochemical Methods; 79 Inorganic Analytical; 80 Organic Analytical.
  - By industry or material: 40 Textiles; 57 Ceramics; 58 Cement.

  Mechanisms are split along the organic/inorganic line: 22 Physical Organic Chemistry versus 67 Catalysis, Reaction Kinetics and Inorganic Reaction Mechanisms. — [CAS sections](https://www.cas.org/support/documentation/references/ca-sections)
- [OBS] **Section sizes in 2010.** The mean was 11,869 papers per section, ranging from 73,273 (section 1, Pharmacology) to 240 (section 32, Steroids). An earlier study by Braam and Bruil found the assigned section matched the authors' own preference for about 80% of papers. — [Bornmann, Marx & Barth 2013](https://arxiv.org/pdf/1307.7498)
- [CONV] **Sections are revised over time.** CAS's Subject Coverage Manual keeps a table of changes. The Biochemistry and Organic groups once appeared in odd-numbered weeks and the other groups in even weeks. — [Stanford CINF workshop, 1998](https://web.stanford.edu/group/swain/cinf/workshop98aug/casects.html)

**RSC** (scope: UK-based society; voluntary membership)

- [CONV] **72 interest groups** are stated; the list itself has 74 entries because of near-duplicates. Examples: Astrochemistry; Electrochemistry; Theoretical Chemistry; Environmental Chemistry; Toxicology; Water Science Forum; Management; Marketing.
- [CONV] **8 subject communities:** Analytical Science; Chemistry Biology Interface; Dalton; Education; Environment, Sustainability and Energy; Faraday Community for Physical Chemistry; Materials Chemistry; Organic Chemistry. — [RSC community and networking (2026 page)](https://www.rsc.org/membership/benefits/community-and-networking?e=1)

**The traditional five and the modern proliferation**

- [CONV] **The "traditional five":** analytical, biochemistry, inorganic, organic and physical chemistry. They are codified in the ACS Committee on Professional Training guidelines for approved bachelor's degrees [unverified]. In the sources seen, the CAS groups and the RSC communities (Analytical, Dalton, Faraday, Organic, Chemistry Biology Interface) roughly reproduce the five, and add macromolecular/materials and applied or industrial chemistry.
- [CONV] **Newer or specialist fields with an institutional home** in the sources seen:
  - nuclear: ACS NUCL; CAS sections 70–71
  - theoretical and quantum: RSC Theoretical Chemistry Group; ACS COMP and PHYS
  - astrochemistry: RSC group
  - geochemistry: ACS GEOC; CAS 53
  - green chemistry: IUPAC ICGCSD
  - materials chemistry: IUPAC definition and interdivisional subcommittee; RSC community
  - environmental: IUPAC Division VI; ACS ENVR; RSC ESE community
  - chemical biology: RSC CBI; ACS BIOL
  - cheminformatics: ACS CINF; IUPAC CPCDS
- [OBS] **Observed absence.** Systems chemistry, origins-of-life (prebiotic) chemistry and mechanochemistry are not divisions in any of the ACS 32, the IUPAC 8, the CAS 80 or the RSC 8 communities. The RSC interest-group list was only partly captured.
  - Their standing as named research fields with dedicated journals and meetings was not checked in this session [unverified].
  - IUPAC's 2019 "Top Ten Emerging Technologies in Chemistry" reportedly included reactive extrusion, a mechanochemical method [unverified].

**Nobel Prize in Chemistry**

- [OBS] **2026:** Henri Kagan and Kenso Soai, "for the discovery of non-linear effects and autocatalysis in asymmetric organic synthesis". Announced 7 October 2026. — [Khaleej Times](https://www.khaleejtimes.com/world/henri-kagan-kenso-soai-win-2026-nobel-chemistry-prize)

  Prize sum 12 million SEK. Committee chair Heiner Linke framed the award around chirality. — [ThePrint](https://theprint.in/world/kagan-and-soai-win-2026-nobel-chemistry-prize/3064245/)
- [OBS] **2025:** Susumu Kitagawa, Richard Robson and Omar Yaghi, for metal–organic frameworks. — [Prothom Alo](https://en.prothomalo.com/international/zmdis3c41t)
- [OBS] **Running totals [unverified].** Through 2023 the Nobel Foundation counted 115 chemistry prizes to 194 laureates. Adding 3 laureates (2024), 3 (2025) and 2 (2026) gives 118 prizes and 202 laureate awards, with Sanger counted twice. This is arithmetic on an unverified base; nobelprize.org failed to load.
- [REC] **Subject distribution: not obtained.** No field-by-field tally was found. Commentators often note that many recent prizes went to biochemical or biological work, e.g. genome editing (2020) and protein design and structure prediction (2024) [unverified].

### Inferences
- **No single official partition of chemistry exists.** Each body uses its own membership rule, and every one of these rules is a DC (none is an MP or TD):
  - IUPAC assigns projects by subject.
  - ACS and RSC rely on self-enrolment.
  - CAS indexers assign abstracts by novelty.
- **The principles are mixed even within one scheme.**
  - ACS has an element-defined division (Fluorine), material and industry divisions (Rubber, Cellulose), and profession divisions (Law, History).
  - CAS runs compound-class, phenomenon, method and industry sections side by side.

  The sets therefore overlap by design, not by error.
- **CAS's membership pattern is primary plus secondary.** One section per abstract, plus cross-references, is the closest institutional analogue to a partition with declared overlaps. The spread of section sizes (240 to 73,273 papers in 2010) shows the sets are not like-sized units.
- **The 2025 and 2026 prizes straddle partitions.**
  - MOFs sit across inorganic, organic and materials chemistry.
  - Kagan and Soai's work joins organic synthesis to kinetics and autocatalysis, and to the questions of chirality that also matter to origins-of-life chemistry (this link is my inference).

### Gaps
- An official 2026 IUPAC committee list after its 2024 site update.
- The full RSC list of interest groups.
- An official Nobel subject breakdown and running totals.
- The date CAS adopted the 80-section scheme.
- Whether the count or names of ACS divisions changed in 2025–26 beyond the label drift noted above.
- Primary sources on systems chemistry, origins-of-life chemistry and mechanochemistry as institutionalized fields.

## 2. Ontologies and databases: how substances are clustered and counted

### Takeaway
Ontologies and registries are conventions applied to records. Their counts are observings of the registries, not of nature.
- PubChem (12 Sep 2024): 118.6 million compounds and 322.4 million substances.
- CAS: over 290 million substances.
- ChEBI: over 195,000 entries; relaunched as ChEBI 2.0 in October 2025.
- ClassyFire/ChemOnt: 4,825 rule-defined categories, frozen since 2016.

ChEBI separates structural classes from roles, which are never superclasses of structures.

### Cited Findings

**ChEBI** (scope: small molecular entities of biological interest)

- [CONV] **Scope and distinctness rule.**
  - Covers atoms, molecules, ions, ion pairs, radicals, complexes and conformers. It also covers groups (parts of entities), substances and classes of entities.
  - Macromolecules encoded directly by the genome are generally excluded: nucleic acids, proteins, and peptides cleaved from proteins.
  - Two structures are distinct entries when they differ in constitution or isotopic composition (DC). This mirrors IUPAC's molecular entity.
  - Names follow IUPAC and NC-IUBMB.

  — [ChEBI About](https://ebi.ac.uk/chebi/about)
- [OBS] **Size.** More than 195,000 entries. — [ChEBI About](https://ebi.ac.uk/chebi/about)

  A benchmark built from release v237 had 1,364 grouping classes over 177,875 structures; its authors describe ChEBI as almost 200,000 structures. — [Mungall et al. 2025](https://arxiv.org/pdf/2505.18470)
- [CONV] **Two classification axes.** Structural classes and roles are kept apart. Roles classify structures non-structurally and are never superclasses of structures (DC). — [Mungall et al. 2025](https://arxiv.org/pdf/2505.18470)

  The top-level split into chemical entity, role (biological role, chemical role, application) and subatomic particle was not re-checked this session [unverified]. It is the standard ChEBI layout, introduced with the resource in Degtyarenko et al. 2008, NAR 36:D344–350, doi:10.1093/nar/gkm791 (citation seen on [Wikipedia: ChEBI](https://en.wikipedia.org/wiki/ChEBI)).
- [CONV] **Identity-adjacent relations [unverified].** ChEBI links related entities with named relations: is_conjugate_acid_of / is_conjugate_base_of, is_tautomer_of, is_enantiomer_of, has_functional_parent, has_parent_hydride, has_role. It also keeps the major microspecies at pH 7.3 as a separate entity. ChEBI thus models "same substance?" questions (protonation state, tautomer, enantiomer) as linked separate entities rather than merging them.
- [CONV] **ChEBI 2.0, launched 20 Oct 2025.**
  - Rebuilt infrastructure: PostgreSQL, Elasticsearch, RDKit structure handling.
  - REST APIs replace SOAP.
  - New downloads (ontology, TSV, SDF, JSON, PostgreSQL dump) with standardized prefixes, including CHEMROF and RO.
  - ChEBI IDs unchanged.

  — [EMBL-EBI news](https://www.ebi.ac.uk/about/news/updates-from-data-resources/chebi-2-0-launches/)

  Paper: Malik et al., "ChEBI: re-engineered for a sustainable future", NAR 54(D1): D1768–1778, doi:10.1093/nar/gkaf1271 (online 2025, issue 2026). — [Wikipedia: ChEBI](https://en.wikipedia.org/wiki/ChEBI); [marineinfo record](https://marineinfo.org/doc/publication/436265)

**ClassyFire / ChemOnt** (scope: any structure given as SMILES or InChI; fully automated)

- [CONV] **ChemOnt: 4,825 categories** defined by curated SMARTS patterns and arranged in a hierarchy.
  - More than 9,000 patterns are combined with Boolean and programmatic logic, and the pattern set is not public.
  - The taxonomy is static and has not been updated since 2016.
  - Membership criterion: presence or absence of substructural features (a DC applied by algorithm).

  — [Mungall et al. 2025](https://arxiv.org/pdf/2505.18470)

  Original paper: Djoumbou Feunang et al., J Cheminform 2016, doi:10.1186/s13321-016-0174-y (URL seen; full text not retrieved). — [J Cheminform](https://jcheminf.biomedcentral.com/articles/10.1186/s13321-016-0174-y)
- [CONV] **Levels.** Kingdom, Superclass, Class, Subclass, then parent levels 1–7: up to 11 levels. — [LaPratt et al., ASCCT 2024 poster](https://ntp.niehs.nih.gov/sites/default/files/2024-11/LaPratt_ASCCT2024_poster.pdf)

  Example output (classyfireR, classification version 2.1) for a methylhistidine: Organic compounds › Organic acids and derivatives › Carboxylic acids and derivatives › Amino acids, peptides, and analogues › Amino acids and derivatives › Alpha amino acids and derivatives › Histidine and derivatives. — [classyfireR vignette](https://wilsontom.r-universe.dev/classyfireR/doc/Getting-Started.html)

  That there are exactly two kingdoms (organic, inorganic) is [unverified]. The vignette shows an "Organic compounds" kingdom, and the poster counts inorganics separately.
- [OBS] **Application to Tox21.**
  - Of 9,329 Tox21 chemicals, 8,583 received a classification; 106 of these were inorganic.
  - Most frequent superclasses: Benzenoids (2,744) and Organoheterocyclic compounds (1,959).
  - The poster gives both 4,285 and 4,825 as the number of unique classes. 4,825 matches Mungall et al.

  — [LaPratt et al. poster](https://ntp.niehs.nih.gov/sites/default/files/2024-11/LaPratt_ASCCT2024_poster.pdf)
- [MODEL] **Critique of rule-based classification.**
  - SMARTS alone cannot express most classes.
  - OWL-DL is too weak for higher-order relations, and ChEBI does not use DL reasoning.
  - Manual curation is slow and can be incomplete or inconsistent.

  The authors propose using generative AI to synthesize executable classification programs for ChEBI classes. — [Mungall et al. 2025](https://arxiv.org/pdf/2505.18470)

**MeSH chemicals branch** [unverified; no MeSH page was checked]

- [CONV] MeSH tree D ("Chemicals and Drugs") divides in three ways:
  - by structure: Inorganic Chemicals, Organic Chemicals, Heterocyclic Compounds, Polycyclic Compounds, Macromolecular Substances;
  - by biochemical family: Carbohydrates, Lipids, Amino Acids/Peptides/Proteins, Nucleic Acids, plus "Complex Mixtures";
  - by function: D27 "Chemical Actions and Uses".

  D27 parallels ChEBI's role axis (comparison is mine).

**PubChem** (scope: open aggregator of depositor records)

- [OBS] **Counts as of 12 Sep 2024** (PubChem 2025 update, Table 1):

  | Record type | Count |
  |---|---|
  | Substances | 322,395,335 |
  | Compounds | 118,596,691 |
  | BioAssays | 1,671,325 |
  | Bioactivities | 295,360,133 |
  | Proteins | 248,298 |
  | Genes | 113,242 |
  | Pathways | 241,163 |
  | Cell lines | 2,007 |
  | Taxonomy | 107,617 |
  | Literature | 41,558,769 |
  | Patents | 50,836,952 |
  | Data classifications | 73 |
  | Data sources | 1,006 |

  — [OUP Table 1](https://academic.oup.com/view-large/499326936). The paper was published 18 Nov 2024 (PMID 39558165). — [abstract mirror](https://tagteam.harvard.edu/hub_feeds/4353/feed_items/14031227/about)
- [CONV] **Substance vs compound.** A substance is a depositor's record and may be a mixture, extract, complex or uncharacterized material. A compound is a unique, characterized structure derived from substances. So substances outnumber compounds by rule. — [Wikipedia: PubChem](https://en.wikipedia.org/wiki/PubChem), citing Kim et al., NAR 2021, which also gives the earlier counts: 111 million compounds and 293 million substances (Nov 2020).
- [OBS] **2026 figure, secondary only.** A library guide (updated 16 Oct 2026) gives more than 122 million compounds from more than 300 million substance records; the figure itself is undated. — [UCSD LibGuide](https://ucsd.libguides.com/organic-chemistry-projects/information). An official 2026 PubChem count was not obtained.
- [CONV] How PubChem standardizes tautomers, salts (via parent compounds), stereo and isotopes into one compound record was not checked [unverified].

**CAS Registry** (scope: substances disclosed in literature and patents; proprietary)

- [OBS] **Over 290 million unique substances**, with thousands added daily.
  - Coverage: literature from 1957 to the present, plus substances back to the early 1900s.
  - Includes polymers, elements, isotopes, proteins, nucleic acids and UVCBs (substances of unknown or variable composition).
  - CAS Common Chemistry, the open subset, holds nearly 500,000.
  - The page gives no as-of date.

  — [CAS REGISTRY](https://www.cas.org/cas-data/cas-registry)
- [CONV] **Assignment practice**, as summarized by a regulatory consultancy (updated 5 Aug 2026; secondary source):
  - Well-defined compounds need stereochemistry where applicable.
  - Polymers are characterized by monomers or reactants, mechanism, a representative structure and molecular weight.
  - UVCBs are characterized by reactants, reaction scheme and representative composition.
  - Ordinary formulated mixtures are generally handled through their components.
  - Broad categories, undefined trade products, finished formulations and organisms may be unsuitable.

  — [REACH24H CAS RN FAQ](https://en.reach24h.com/news/insights/chemical/cas-registry-number-faq)
- [CONV] CAS gives separate registry numbers to salts versus parents, hydrates, labelled isotopologues, and individual stereoisomers versus racemates [unverified this session].

**Chemical space** [unverified]

- [SIM/MODEL] Often-cited estimates:
  - about 10^60 small drug-like molecules (Bohacek, McMartin & Guida 1996);
  - the enumerated GDB-17 set of about 166.4 billion molecules with up to 17 heavy atoms (Ruddigkeit et al. 2012).

  Neither was checked this session. Both are enumerations or estimates under declared valence and stability rules, not observings.

### Inferences
- **Registered chemistry is a tiny sample of possible chemistry.** About 10^8 registered substances (OBS) set against about 10^11 enumerated and an estimated 10^60 possible structures (the latter unverified). "Known chemistry" is a sample defined by what was reported and registered.
- **Identity rules do a lot of merging.** PubChem's ratio of substances to compounds (about 2.7) measures it: the same structure deposited by many sources collapses into one compound.
- **"What kind is X?" has at least two independent answers.** ChEBI and MeSH carry a function-based axis (role; actions and uses) that is orthogonal to structure. CAS sections and ClassyFire are structure- or subject-based.
- **Ontology membership is fixed by curation or algorithm (DC), not by measurement.** ClassyFire's rule set has been frozen since 2016, and ChEBI's hierarchy is curated without automated reasoning.

### Gaps
- Exact 2026 counts for PubChem, the CAS Registry and ChEBI 3-star entries.
- Unchecked because the relevant pages failed or were not reached:
  - PubChem's standardization policy for tautomers and salts;
  - CAS's precise registry-number rules;
  - MeSH chemical-tree numbers;
  - ChEBI's top-level branch definitions as stated in the 2026 paper.

## 3. What counts as one substance or one species

### Takeaway
IUPAC grades identity at three levels:
- **molecular entity:** single units told apart by constitution or isotopes, at a precision set by purpose;
- **chemical species:** populations that are identical on the experiment's timescale;
- **substance:** bulk matter of constant composition.

"Element" has two senses: a kind of atom and a simple substance. Many standard distinctions are conventions keyed to timescale, conditions or regulatory purpose: isomer vs conformer, tautomer, polymorph, salt vs cocrystal, polymer as mixture, Berthollide.

### Cited Findings

**Molecular entity, chemical species, substance (IUPAC)**

- [CONV] **Molecular entity.** IUPAC's generic term for any single unit that can be told apart from others by constitution or isotopic make-up: an atom, molecule, ion, ion pair, radical, radical ion, complex, conformer and so on. "Chemical species" is the term for collections of such units.
  - The precision needed depends on the purpose. "Hydrogen molecule" is enough for some uses. Others require the electronic state, vibrational state or nuclear spin.
  - Source: PAC 1994, 66, 1077, p. 1142.
  - Criterion kind: a DC whose application rests on MP (differences that can be resolved).

  — [Gold Book: molecular entity, doi:10.1351/goldbook.M03986](https://goldbook.iupac.org/M03986.html)

  The Gold Book reached a 5th edition in 2025, as cited on [Wikipedia: ChEBI](https://en.wikipedia.org/wiki/ChEBI).
- [CONV] **Chemical species.** A population of chemically identical molecular entities that all have access to the same molecular energy levels within the time the experiment takes.
  - It also covers non-isolable units in solids, such as graphite or NaCl.
  - Conformers that interconvert slowly enough to give separate NMR spectra are separate species. In a slow reaction, the same conformers behave as one species.
  - Sources: PAC 1994, 66, 1077, p. 1096; PAC 1996, 68, 2193, p. 2202.
  - Criterion kind: a DC with an explicit dial for observing timescale.

  — [Gold Book: chemical species, doi:10.1351/goldbook.CT01038](https://goldbook.iupac.org/terms/view/CT01038)
- [CONV] **Substance.** Matter of constant composition and characteristic properties; either an element or a compound. The source records several places where the rule bends:
  - CAS indexes some alloys of uncertain composition as substances.
  - Non-stoichiometric compounds break the constant-composition rule.
  - Polymers are usually mixtures of molecules with different molar masses, specified by precursor, reaction or molar-mass distribution.
  - Law (e.g. EU REACH) can treat process-defined mixtures as substances.
  - Geology calls uniform inorganic solids minerals and their aggregates rocks.

  — [Wikipedia: Chemical substance](https://en.wikipedia.org/wiki/Chemical_substance). The Gold Book's own "chemical substance" entry was not retrieved [unverified].
- [CONV] **Compound.** A substance whose molecules or formula units contain atoms of more than one element held by chemical bonds. Classes by bonding type:
  - molecular (covalent);
  - ionic (salts);
  - intermetallic (ordered metal–metal phases with metallic bonding);
  - coordination complexes (coordinate covalent bonds to a central atom).

  — [Wikipedia: Chemical compound](https://en.wikipedia.org/wiki/Chemical_compound)

**The element: two senses (Paneth)**

- [CONV] **IUPAC's two senses.**
  1. A kind of atom: all atoms that share one proton count (atomic number).
  2. A pure substance made only of atoms with that proton count, sometimes called an "elementary substance".

  In practice "chemical element" covers both. Source: Red Book, 3rd ed., p. 35. Criterion kind: sense 1 is MP/TD (nuclear charge); sense 2 is MP (composition). — [Gold Book: chemical element, doi:10.1351/goldbook.C01022](https://goldbook.iupac.org/terms/view/C01022)
- [CONV/MODEL] **Paneth's 1931 lecture** (English translation 2003) argues that the element has a dual meaning, basic substance versus simple substance, as do other chemical concepts. Published in Foundations of Chemistry 5(2): 113–145. — [PhilArchive record](https://dc2.philarchive.org/rec/PANTES)
- [MODEL] **Scerri's reading of Paneth.**
  - The simple substance is the isolable, observable form, such as grey metallic sodium or green chlorine gas.
  - The basic substance is the unobservable bearer of properties that persists in compounds. It was characterized by atomic weight in Mendeleev's time and later by atomic number.
  - The periodic system classifies basic substances. That is why the halogens group together although their simple substances differ greatly.
  - On isotopes, Paneth and Hevesy showed that isotopes of one element are chemically almost identical, which supports one element per atomic number. Fajans opposed.

  — [Scerri 2005, HYLE 11(2):127–145](https://hyle.org/journal/issues/11-2/scerri.htm)
- [CONV] **Scerri's critique of the Gold Book.** He argues that the second sense mostly restates the first and misses Paneth's abstract sense. On his account, the abstract element is what reactions preserve (atomic number), and "carbon" covers all isotopes and allotropes. He gives no final wording, and cites Scerri & Ghibaudi (eds), *What is a Chemical Element?* (2020). — [Scerri, PhilSci-Archive](https://philsci-archive.pitt.edu/26821/1/What%20is%20an%20element%20for%20CI.docx)

  Earlier, Scerri noted that Mendeleev's own term was "simple body", and traced the concept to Lavoisier. — [Scerri, Chem. Int. 27(3), 2005](https://publications.iupac.org/ci/2005/2703/ud2_scerri.html)
- [REC → CONV] **History of the criterion.**
  - Lavoisier counted as elements whatever analysis could not yet decompose: an operational, revisable criterion. He suspected the "earths" were compounds.
  - Soddy named isotopes in 1913.
  - Delegates to the 1923 IUPAC meeting tied periodic-table positions to atomic number.
  - Chadwick's discovery of the neutron (1932) explained why atomic weight varies at fixed atomic number.
  - Needham (2008) objects that isotopes differ in chemically salient ways, such as reaction rates. Hendry (2006) replies that the table, and IUPAC, classify by atomic number.

  — [SEP: Philosophy of Chemistry (rev. 11 Mar 2026)](https://plato.stanford.edu/ENTRIES/chemistry)
- [MODEL] **Atomic number does two jobs.** It suffices to identify an element and it explains electronic structure and chemical behaviour. Because of isotopic variation, members of an element kind are not intrinsically identical, though they share nuclear charge. — [SEP: Natural Kinds (rev. 28 Jan 2022)](https://plato.stanford.edu/entries/natural-kinds)
- [CONV] **New elements.** Two IUPAC documents set the conventions for discovery claims and naming: the IUPAC/IUPAP provisional report "On the discovery of new elements" and "How to Name New Chemical Elements" (titles seen; content not retrieved). — [IUPAC recently published](https://iupac.org/recommendations/recently-published/)

**Compound vs mixture; Daltonides vs Berthollides**

- [REC/MODEL] **Proust vs Berthollet.** Proust's law of constant proportions (early 1800s) answered Berthollet's claim that composition can vary.
  - Berthollet was partly vindicated in the early 20th century by Berthollides such as wüstite: nominally FeO, but with less iron than the formula implies.
  - Berthollide compositions vary with temperature and pressure, and their stability is explained by minimizing Gibbs energy.
  - In thermodynamics, solutions and compounds differ by degree.

  — [SEP: Philosophy of Chemistry](https://plato.stanford.edu/ENTRIES/chemistry)
- [OBS/CONV] **Non-stoichiometric compounds** are a disputed marginal case. Palladium hydride PdHx has 0.02 < x < 0.58, and many silicate minerals vary in composition through substitution or defects. — [Wikipedia: Chemical compound](https://en.wikipedia.org/wiki/Chemical_compound). That "Daltonide" and "Berthollide" are Kurnakov's terms (c. 1912–14) is [unverified].

**Isotopologues and isotopomers**

- [CONV] **One element, distinct entities.** IUPAC's molecular-entity criterion and ChEBI's distinctness rule both separate isotopically distinct units. Isotopologues (differing in isotopic composition) are therefore different molecular entities and different ChEBI entries, yet the same element under IUPAC's sense 1. — [Gold Book M03986](https://goldbook.iupac.org/M03986.html); [ChEBI About](https://ebi.ac.uk/chebi/about); [Gold Book C01022](https://goldbook.iupac.org/terms/view/C01022)

  Formal Gold Book definitions were not retrieved [unverified]: isotopologue = differs in isotopic composition; isotopomer = same isotopes in different positions.

**Isomers, conformers, tautomers, resonance**

- [REC] **History of isomerism and structure.**
  - Berzelius coined "isomer" (1832) for substances with the same composition and different properties, e.g. ethanol and dimethyl ether (C2H6O).
  - Kekulé (1858) argued carbon is tetravalent. Crum Brown (1864) introduced graphic formulas, and Frankland the word "bond".
  - Van 't Hoff and Le Bel (1874) inferred tetrahedral carbon from optical isomerism. Van 't Hoff's argument worked by ruling out square-planar geometry.

  — [SEP: Philosophy of Chemistry](https://plato.stanford.edu/ENTRIES/chemistry). The SEP Natural Kinds entry dates the discovery of isomerism to Wöhler (1827). — [SEP: Natural Kinds](https://plato.stanford.edu/entries/natural-kinds)
- [CONV] **Stereoisomers** differ neither in constitution nor in isotopic make-up, yet they are distinct substances. Their terminology comes from IUPAC's "Basic terminology of stereochemistry" (PAC 1996, 68, 2193), which the species entry cites. — [Gold Book CT01038](https://goldbook.iupac.org/terms/view/CT01038)
- [CONV, timescale] **Conformers** are one species or two, depending on interconversion rate relative to the observation (see the species entry above). Atropisomers are conventionally distinguishable when their interconversion half-life is at least about 1000 s at the stated temperature (Ōki's criterion) [unverified].
- [CONV] **Tautomers** interconvert readily, so a pure tautomer usually cannot be isolated. This is a simplification: some tautomers can be isolated. — [Wikipedia: Chemical substance](https://en.wikipedia.org/wiki/Chemical_substance)
  - Identifier policies [unverified; the InChI Trust pages were blocked]:
    - Standard InChI deliberately merges some prototropic (mobile-H) tautomers but not keto–enol pairs.
    - A non-standard fixed-H layer keeps the drawn tautomer.
    - SMILES encodes the drawn tautomer, so canonical SMILES is not tautomer-invariant.
  - IUPAC's digital standards are InChI, RInChI (reactions) and MInChI (mixtures). An "IUPAC SMILES+ Specification" is under development. — [IUPAC digital standards](https://iupac.org/what-we-do/digital-standards/)
- [CONV] **Resonance structures** are alternative drawings of one entity. They are neither isomers nor interconverting species, so the classification concerns representation, not substance. The Gold Book wording was not checked [unverified].

**Solid forms: polymorphs, hydrates, solvates, salts, cocrystals**

- [CONV] The species concept extends to non-isolable units in solids such as graphite and NaCl. — [Gold Book CT01038](https://goldbook.iupac.org/terms/view/CT01038)

  Allotropy (e.g. of tin and of carbon) cuts across the element and substance hierarchies. — [SEP: Natural Kinds](https://plato.stanford.edu/entries/natural-kinds)
- [CONV] **Regulatory identity of solid forms [all unverified].**
  - US FDA guidance (2018) treats pharmaceutical cocrystals like polymorphs of the active ingredient, not as new active ingredients. Salts are treated as different chemical forms.
  - Polymorphs are one compound with different crystal packing, told apart by X-ray powder diffraction (XRPD) and thermal analysis.
  - Hydrates and solvates contain solvent in stoichiometric or non-stoichiometric amounts.
  - The salt/cocrystal boundary is usually drawn by whether a proton has transferred, with a ΔpKa rule of thumb: about 3 or more suggests a salt, below 0 a cocrystal.

**Polymers and dispersity**

- [CONV] **Polymer identity** is specified by source (monomer or precursor), structure (constitutional repeating units) or molar-mass distribution. — [Wikipedia: Chemical substance](https://en.wikipedia.org/wiki/Chemical_substance)
  - CAS-style identity uses monomers, mechanism, a representative structure and molecular weight. — [REACH24H](https://en.reach24h.com/news/insights/chemical/cas-registry-number-faq)
  - IUPAC conventions include source-based nomenclature, preferred names for constitutional units and notation for tactic polymers. Structure-based names for irregular, star, comb and brush polymers are under review until 31 Dec 2026. — [IUPAC recently published](https://iupac.org/recommendations/recently-published/); [IUPAC under review](https://iupac.org/recommendations/under-review-by-the-public/)
- [OBS → CONV] **Dispersity** Đ = Mw/Mn, measured by size-exclusion chromatography (SEC/GPC), replaced "polydispersity index" in IUPAC usage around 2009 [unverified].

**Timescale-dependent species (fluxional molecules)**

- [CONV] The species definition makes identity depend on the timescale of the measurement. — [Gold Book CT01038](https://goldbook.iupac.org/terms/view/CT01038)
- [OBS → MODEL] **Standard examples [unverified].**
  - Bullvalene (C10H10) rearranges among 10!/3 = 1,209,600 degenerate valence-tautomeric arrangements, and shows one averaged ¹H NMR signal at high temperature.
  - PF5's axial and equatorial fluorines are averaged on the NMR timescale by Berry pseudorotation.
  - What is observed: NMR line shapes that change with temperature (coalescence).
  - What the model adds: a mechanism (pseudorotation, Cope rearrangement) and an energy barrier.

### Inferences
- **IUPAC builds identity in tiers, each with its own membership rule.**
  - Entity: by constitution or isotopes (a DC grounded in MP).
  - Species: by shared accessible energy levels within the experiment's timescale (a DC with a dial).
  - Substance: by constant bulk composition and properties (MP).

  One object can be one at a tier and many at another. Isotopologues are one element but distinct entities. Conformers are one compound but possibly distinct species.
- **Rules point in different directions at the same items.**
  - The element merges isotopes, while ChEBI and the molecular entity separate them.
  - PubChem merges depositor records.
  - ChEBI keeps conjugate acids, conjugate bases and tautomers as separate linked entities (detail unverified).
- **There is a seam in the definitions.** The Gold Book lists conformers as molecular entities, although its stated criterion names only constitution and isotopes. Stereochemical and conformational identity are therefore supplied by other recommendations.
- **"One substance" becomes a declared convention** for polymers, Berthollides, UVCBs and alloys. Identity there rests on a process, a distribution or a composition range, not a fixed composition.

### Gaps
- Gold Book entries not retrieved: chemical substance, isotopologue, isotopomer, tautomerism, resonance, polymorph, cocrystal.
- InChI Trust tautomer FAQ and InChI 1.07 release notes.
- FDA cocrystal guidance.
- IUPAC dispersity recommendation.
- Kurnakov's original terminology.

## 4. How reactions and mechanisms are classified

### Takeaway
Three kinds of classification are layered here:
- **Reaction types** (addition, substitution, elimination, rearrangement, redox) are book-keeping classes reconstructed from the observed change between reactants and products.
- **Mechanism classes** (SN1/SN2, A/D/I, inner/outer sphere) are model constructs inferred from rate laws, stereochemistry, isotope labels and trapping experiments.
- **Named reactions and reaction ontologies** are conventions.

The IUPAC sources and the philosophy-of-mechanism material were verified this session. Most specific notation histories are flagged [unverified].

### Cited Findings

- [CONV] **IUPAC's controlling vocabulary** for mechanism and reactivity is the *Glossary of Physical Organic Chemistry* (IUPAC Recommendations 2021): Pure Appl. Chem. 94(4): 353–534 (2022), doi:10.1515/pac-2018-1010; corresponding author C. L. Perrin. Keywords: mechanism, reactivity, structure. Its treatment of specific notations was not checked. — [IUPAC](https://iupac.org/recommendation/glossary-of-physical-organic-chemistry/)
- [MODEL] **Thick vs thin mechanisms.**
  - A thick mechanism is a continuous account of nuclear and electronic motion. A thin mechanism is a discrete sequence of steps and intermediates.
  - Practice and textbooks use thin mechanisms, which serve to identify rate-determining steps and intermediate structures.
  - Mechanisms are confirmed mainly by eliminative induction: candidates that conflict with experiment are ruled out.
  - The open risk is unconceived alternatives, since no algorithm generates every candidate.
  - Examples: Okabe and McNesby's isotope-labelling study of ethane photolysis; van 't Hoff's elimination of planar carbon.
  - Corey's retrosynthetic analysis is offered as an example of a logic of discovery.

  — [SEP: Philosophy of Chemistry](https://plato.stanford.edu/ENTRIES/chemistry)
- [CONV] **Reaction identifiers.** RInChI encodes a reaction as the structures of its reactants, products and agents (paper doi:10.1186/s13321-018-0277-8, linked from IUPAC; content not retrieved). MInChI does the same for mixtures. — [IUPAC digital standards](https://iupac.org/what-we-do/digital-standards/)
- [CONV] **Polymerization classes.** IUPAC has published "Basic Classification and Definitions of Polymerization Reactions" and "Terminology for Chain Polymerization" (titles seen; texts not retrieved). — [IUPAC recently published](https://iupac.org/recommendations/recently-published/)
- [CONV] **CAS splits the mechanism literature** along the organic/inorganic line: section 22 versus section 67. — [CAS sections](https://www.cas.org/support/documentation/references/ca-sections)
- [OBS] **The 2026 Nobel subjects are autocatalysis and non-linear effects in asymmetric synthesis.** — [Khaleej Times](https://www.khaleejtimes.com/world/henri-kagan-kenso-soai-win-2026-nobel-chemistry-prize)

  Background [unverified]:
  - Kagan's non-linear effect (reported 1986): the product's enantiomeric excess (ee) is not proportional to the catalyst's ee.
  - Soai's asymmetric autocatalysis (1995): a chiral pyrimidyl alkanol product catalyzes its own formation and amplifies ee.
  - What is observed: product ee against catalyst ee, measured by chiral HPLC or GC.
  - What the models add: kinetic models of aggregation and autocatalytic feedback.

**Background catalogue** [all unverified this session; included because the report needs the full list]

- [REC/CONV] **Overall reaction types**, classified by the bonds made and broken:
  - addition; elimination; substitution; rearrangement;
  - redox: a change in oxidation state, itself an IUPAC convention (the comprehensive definition of oxidation state is a title verified on the [IUPAC list](https://iupac.org/recommendations/recently-published/));
  - acid–base: proton transfer or electron-pair transfer, depending on the acid–base definition used (see §5);
  - pericyclic: concerted, with a cyclic transition state. Subclasses are cycloaddition, electrocyclic, sigmatropic, cheletropic and group-transfer/ene. Whether a reaction is "allowed" follows from Woodward–Hoffmann orbital-symmetry rules (1965–69), a theory-derived criterion;
  - radical vs polar: homolytic vs heterolytic bond cleavage, which is inferred, not seen.
- [MODEL] **Hughes–Ingold labels** (1930s): SN1, SN2, E1, E2, plus E1cB. The number gives the molecularity of the rate-determining step.
  - What is observed: the order of the rate law, the stereochemical outcome (inversion vs racemization), rearrangements, solvent and leaving-group effects, kinetic isotope effects.
  - The label itself is inferred.
  - The same overall substitution can be classed SN1 or SN2 depending on substrate and solvent. Ion-pair continua (Winstein) blur the line.
- [CONV] **IUPAC Guthrie–Jencks notation** (Guthrie, PAC 61, 23–56, 1989). Mechanisms are written as strings of elementary association (A) and dissociation (D) steps, with subscripts marking nucleophilic or electrophilic roles. SN2 becomes ANDN; SN1 becomes DN + AN.
- [MODEL] **Langford–Gray scheme (1965)** for ligand substitution at coordination complexes.
  - Stoichiometric mechanism: associative (A, an intermediate of higher coordination number); dissociative (D, lower coordination number); or interchange (I, no detectable intermediate).
  - Intimate mechanism: splits I into Ia and Id according to sensitivity to the entering ligand.
  - What is observed: dependence on the entering group, activation volumes, detectable intermediates.
- [MODEL] **Taube's inner-sphere vs outer-sphere electron transfer.**
  - What is observed: ligand transfer into the product. In the classic Co(III)–Cl/Cr(II) experiment, the chloride ends up on chromium.
  - What the model adds: a bridged transition state, and Marcus theory for the outer-sphere case. Nobel 1983.
- [MODEL] **Organometallic elementary steps:** ligand substitution; oxidative addition and reductive elimination (oxidation state and coordination number change by ±2); migratory insertion and deinsertion; β-hydride elimination; transmetalation; σ-bond metathesis; nucleophilic attack on coordinated ligands. The classification rests on electron-counting conventions (ionic vs covalent counting).
- [CONV] **Polymerization classes.**
  - Chain vs step growth is a kinetic criterion: chain growth adds monomer only to active chain ends; step growth joins any two species.
  - This cross-cuts Carothers's older scheme of addition vs condensation, which is based on composition.
  - Living polymerization (Szwarc, 1956) has no irreversible termination or transfer.
  - IUPAC prefers "reversible-deactivation radical polymerization" to "controlled/living radical polymerization".
- [CONV] **Catalysis classes:** homogeneous vs heterogeneous (by phase); enzymatic (EC numbers classify enzymes by the reaction catalyzed); organocatalysis; photocatalysis and electrocatalysis; autocatalysis.
- [CONV] **Named-reaction catalogues and ontologies.**
  - RXNO is the RSC name-reaction ontology, with MOP covering molecular processes.
  - NameRxn assigns reactions to named types and classes by rule.
  - Hierarchical reaction classes used in pharmaceutical chemistry include heteroatom alkylation/arylation, acylation, C–C bond formation, protection/deprotection, reduction, oxidation and functional-group interconversion.

### Inferences
- **Three layers with three criterion kinds.**
  - Reaction type is REC: a book-keeping comparison of observed reactants and products (MP plus DC).
  - Mechanism class is MODEL: inferred by eliminative induction, and revisable when new alternatives are conceived (TD).
  - Named reactions and ontology classes are CONV: eponyms and rule sets.
- **Membership can be conditional.** One reaction type can fall into different mechanism classes as solvent or substrate changes. Chain/step and addition/condensation are two partitions of the same polymerizations that disagree about some members (examples unverified).

### Gaps
- No primary source was retrieved for:
  - Hughes–Ingold, Guthrie–Jencks, Langford–Gray, Taube or Woodward–Hoffmann;
  - RXNO and NameRxn counts;
  - the EC classification;
  - the text of IUPAC's polymerization classification.

  The search allowance was exhausted and these pages were blocked.

## 5. Bonds and interactions; acids and bases; metals and non-metals

### Takeaway
The primary bond classes (ionic, covalent, metallic, dative) are idealized limits on a continuum, separated by conventional electronegativity cutoffs. IUPAC names secondary interactions after the periodic group of the electrophilic atom: hydrogen 2011, halogen 2013, chalcogen 2019, pnictogen 2024. The tetrel bond has only an authors' proposal. Acid–base and metal/metalloid classes are plural, nested definitions, and membership depends both on the definition chosen and on conditions. Their sources could not be re-verified here.

### Cited Findings

**Primary bond classes**

- [CONV/MODEL] **Strong and weak bonds.**
  - Strong: covalent (shared electrons); coordinate covalent, where one atom supplies both electrons (e.g. F3B←NH3); ionic (electrostatic attraction between ions); metallic (delocalized electrons, which explain conductivity and lustre).
  - Weak: dipole–dipole forces, London dispersion, hydrogen bonds, halogen bonds.
  - Electronegativity-difference bands: roughly 0–0.3 nonpolar; 0.3–1.7 polar covalent; above 1.7 likely ionic. There is no precise cutoff.
  - The types shade into one another, and pure ionic bonding is an unrealistic limit.
  - The three-centre two-electron bond is noted as a covalent variant.
  - Criterion kind: TD (an electronegativity scale) applied with a DC cutoff.

  — [Wikipedia: Chemical bond](https://en.wikipedia.org/wiki/Chemical_bond)
- [REC/MODEL] **History.** Lewis (1916, 1923) and Kossel (1916). Lewis contrasted ionic compounds (radially symmetric electrostatic bonding in lattices) with covalent compounds (bonds directed between atomic centres). Frankland coined "bond". — [SEP: Philosophy of Chemistry](https://plato.stanford.edu/ENTRIES/chemistry)
- [MODEL] **What a bond is.**
  - Structural conception: bonds are localized, directional parts of molecules (Hendry 2008).
  - Energetic conception: bonding is real, but bonds as discrete objects are not (Weisberg).
  - Challenges: electron indistinguishability and delocalization (Mulliken); weakly bonded molecules in which bonding and stabilization come apart (Berson).
  - Bader's bond paths offer a criterion based on electron density. Critics note that they yield implausible "bonds", such as 60 bond paths from C60 to an encapsulated argon atom.
  - Valence-bond, molecular-orbital and semi-empirical models overlap in part and conflict in part.

  — [SEP: Philosophy of Chemistry](https://plato.stanford.edu/ENTRIES/chemistry)
- [CONV] **Further classes [unverified].**
  - σ/π/δ/φ, classified by nodal symmetry about the bond axis. δ bonds were identified in [Re2Cl8]²⁻ (Cotton, 1964); φ bonding was proposed computationally for U2 (2005).
  - Multicentre bonding, e.g. B2H6 with two 3c–2e B–H–B bridges.
  - The van Arkel–Ketelaar triangle (1940s) places binary compounds among ionic, covalent and metallic vertices, plotting mean electronegativity against electronegativity difference.

**Secondary (noncovalent) bonds: IUPAC definitions**

- [CONV] **Earlier IUPAC definitions:**
  - Hydrogen bond (2011): Arunan et al., PAC 83, 1637–1641, doi:10.1351/pac-rec-10-01-02. Companion report: PAC 83, 1619, doi:10.1351/pac-rep-10-01-01.
  - Halogen bond (2013): Desiraju et al., PAC 85, 1711–1713, doi:10.1351/pac-rec-12-05-10.
  - Chalcogen bond (2019): Aakeröy et al., PAC 91, 1889–1892, doi:10.1515/pac-2018-0713.

  Citations as given in the pnictogen recommendation. — [JYX PDF](https://jyx.jyu.fi/bitstreams/303681ef-6489-4fc8-808a-c3c508589908/download); also [Varadwaj et al. tetrel proposal](https://arxiv.org/pdf/2210.10649)
- [CONV] **Pnictogen bond.** "Definition of the pnictogen bond (IUPAC Recommendations 2023)" by Resnati, Bryce, Desiraju, Frontera, Krossing, Legon, Metrangolo, Nicotra, Rissanen, Scheiner and Terraneo: PAC 96(1): 135–145 (2024), doi:10.1515/pac-2020-1002. — [Chemistry International 2024](https://www.degruyterbrill.com/document/doi/10.1515/ci-2024-0317/html); [JYX record](https://jyx.jyu.fi/jyx/Record/jyx_123456789_93263)

  The provisional version was posted 15 Feb 2023, with comments due 30 Jun 2023. — [IUPAC provisional page](https://iupac.org/definition-of-the-pnictogen-bond/)

  Contents of the recommendation (a DC grounded in MP and TD):
  - **Membership criterion:** an attractive interaction between an electron-poor (electrophilic) region on a group-15 atom and an electron-rich (nucleophilic) region in the same or another entity. The term applies only when separation, energy or other measured or calculated properties differ from those of a comparable covalent or ionic bond.
  - **Observable indicators:**
    - Pn···A distance shorter than the sum of the van der Waals radii but longer than the sum of the covalent radii;
    - approach roughly opposite an R–Pn bond, or perpendicular to a planar unit;
    - lengthening of the R–Pn bond on the opposite side;
    - IR and Raman shifts in both partners; UV–vis changes;
    - changes in NMR shifts and in quadrupolar and spin–spin couplings;
    - little distortion of the donor (large distortion signals coordination instead).
  - **Model and computed indicators:** a QTAIM bond path and critical point; trends in strength with the electronegativity of Pn and the electron-withdrawing power of R.
  - **Context:** the three group-defined recommendations (halogen, chalcogen, pnictogen) were drafted in parallel for consistent terminology. "σ-hole" and "π-hole" have no formal IUPAC definitions and are treated as umbrella terms.

  — [JYX PDF of the recommendation](https://jyx.jyu.fi/bitstreams/303681ef-6489-4fc8-808a-c3c508589908/download)
- [CONV] **Tetrel bond (group 14): no IUPAC recommendation in the sources seen.**
  - Varadwaj, Varadwaj, Marques and Yamashita proposed a definition in CrystEngComm 2023, doi:10.1039/D2CE01621D. It is presented as the authors' own proposal, following the IUPAC pattern. It prefers "tetrel bond" to "carbon bond" for uniformity, and excludes cases where the tetrel atom acts as nucleophile. — [arXiv v6](https://www.arxiv.org/pdf/2210.10649v6)
  - Chemistry World (c. 2024) reported tetrel proposals expected for community review in 2025, with final publication possibly years away. Carbon's central place makes tetrel the hardest case. — [Chemistry World](https://chemistryworld.com/news/beyond-hydrogen-bonding-new-definitions-for-secondary-bonding-interactions-to-end-confusion/4020237.article)
  - On 23 Oct 2026, IUPAC's public-review list holds only the valence and irregular-polymer items. Its recently-published list shows the pnictogen and chalcogen definitions but no tetrel definition. — [IUPAC under review](https://iupac.org/recommendations/under-review-by-the-public/); [IUPAC recently published](https://iupac.org/recommendations/recently-published/)
  - Status: not adopted, as far as these pages show.
- [OBS vs SIM] **A worked tetrel-bond assignment** (Bhattacharya & Banerjee, PCCP 26: 21538–21547, 2024, doi:10.1039/D4CP01949K).
  - Observed: in matrix-isolation IR in solid argon, formic acid's C=O, C–O and O–H bands shift when it complexes with SiCl4.
  - Simulated: a σ-hole on a face of SiCl4; a QTAIM critical point between Si and O; NBO hyperconjugation.
  - Assignment: tetrel bond. By contrast, CCl4 with formic acid had been assigned a halogen bond. Bond-class membership thus depends on the central atom and is decided partly by computation.

  — [RSC](https://pubs.rsc.org/en/Content/ArticleLanding/2024/CP/D4CP01949K)
- [REC] **Identification practice** in a pnictogen-bond perspective paper:
  - searches of the Cambridge Structural Database (CSD) and the Inorganic Crystal Structure Database (ICSD);
  - contacts compared with van der Waals radii, which are uncertain by about ±0.2 Å;
  - IR, Raman and NMR shifts.

  The more criteria a contact meets, the more reliable the identification. — [Varadwaj et al., arXiv 2210.02823](https://arxiv.org/pdf/2210.02823)
- [MODEL] **Debate over the group-named bonds.**
  - They are seen as one phenomenon: an electron-poor region on an otherwise electron-rich atom, named after the electrophilic atom.
  - Supporters (Scheiner) say separate names help analyse each case.
  - Some chemists resist the idea that two electronegative atoms can attract, and such contacts are often misfiled as hydrogen bonds.
  - The hydrogen-bond definition was contested over C–H···O contacts and blue-shifted bands, and went through more than 20 referees.
  - The pnictogen definition took about six years.

  — [Chemistry World](https://chemistryworld.com/news/beyond-hydrogen-bonding-new-definitions-for-secondary-bonding-interactions-to-end-confusion/4020237.article)

**Acids and bases** [unverified this session; the sources I tried were blocked]

- [CONV/TD] **Arrhenius (1880s):** acids give H+ (H3O+) in water and bases give OH−. Scope: aqueous solution.
- [CONV/TD] **Brønsted–Lowry (1923):** an acid is a proton donor and a base a proton acceptor. Defines conjugate pairs; independent of solvent.
- [CONV/TD] **Lewis (1923):** an acid is an electron-pair acceptor and a base an electron-pair donor. Includes BF3 and metal ions. Every Brønsted base is a Lewis base; in a Brønsted transfer, H+ itself is the Lewis acid.
- [CONV] **Solvent-system definition** (Franklin; Cady & Elsey, 1920s): acids raise the concentration of the solvent's characteristic cation.
- [CONV] **Lux (1939)–Flood (1947):** a base donates oxide ion and an acid accepts it. Scope: oxide melts, glasses, geochemistry.
- [CONV] **Usanovich (1939):** any species that gives up cations or accepts anions or electrons is an acid. This absorbs redox chemistry, and is criticized as too broad to be useful.
- [MODEL] **Pearson's HSAB (1963)** sorts Lewis acids and bases into hard and soft.
- **Nesting:** for bases, roughly Arrhenius ⊂ Brønsted ⊂ Lewis ⊂ Usanovich. Lux–Flood is a special case of Lewis, with O²⁻ as the carrier of the donated pair.
- **Observing vs explaining:** what is observed is pH or conductivity change, titration curves, spectroscopic evidence of adducts and calorimetric enthalpies. Each definition adds a choice of which transferred entity is "essential".

**Metals, non-metals, metalloids** [unverified this session]

- [MP] **Physical criterion.** A metal's electrical conductivity falls as temperature rises, and its band structure has no gap at the Fermi level. Semiconductors and insulators have band gaps, and their conductivity rises with temperature.
- [TD] **Herzfeld criterion (1927):** an element is predicted to be metallic when its molar refraction approaches or exceeds its molar volume (a polarizability "catastrophe").
- [MODEL] **Mott's criterion** for a metal–insulator transition, set by carrier density.
- **Membership changes with conditions.** Pressure makes iodine and xenon metallic; claims of metallic hydrogen remain contested.
- [CONV] **Metalloids have no IUPAC-fixed list.**
  - The commonly cited six are B, Si, Ge, As, Sb and Te.
  - Surveys of published lists (Vernon 2013, J. Chem. Educ., analysing 194 lists) find C, Al, Se, Po and At included often but inconsistently.
  - The criteria used vary: electronegativity, ionization energy, semiconducting band structure, amphoteric oxides, packing efficiency.

### Inferences
- **Bond classes split into observed indicators and model attributions.** Observed: distances and angles from diffraction, vibrational and NMR shifts. Attributed by model or simulation: σ-holes, bond paths, attractive energies. IUPAC's definitions require both, so membership is a hybrid of measurement and model.
- **The periodic table's group partition is imported into the interaction taxonomy** by naming bonds after the electrophilic atom's group. Carbon is where this import strains: it is the archetypal covalent atom and also a possible tetrel-bond site that attracts nucleophiles.
- **Acid–base and metal/non-metal classes depend on conditions and on definitions.** Conditions: solvent, melt, pressure. Definitions: the nested schemes. One substance can be an acid in one scheme and not in another (specifics unverified).

### Gaps
- No verified primary source this session for:
  - the originators and dates of the acid–base schemes;
  - the Herzfeld criterion;
  - metalloid surveys, and IUPAC's position on "metalloid";
  - the first reports of δ and φ bonds;
  - the van Arkel–Ketelaar triangle.

## 6. Overlaps, conflicts, and dependence on conditions or observing timescale; natural vs conventional

### Takeaway
Most conflicts have one of two sources:
- different identity rules applied to the same matter (isotopes, tautomers, salts, polymers);
- criteria parameterized by timescale or conditions (species, Berthollides, metallization).

Philosophers dispute whether chemical kinds are natural (microstructural essentialism) or partly conventional or plural (Needham, van Brakel, Khalidi, Tobin, Dupré). The 2026 SEP revision leaves both positions open.

### Cited Findings

- [CONV, timescale] **Species identity varies with experimental timescale**, e.g. conformers on the NMR timescale versus in a slow reaction. — [Gold Book CT01038](https://goldbook.iupac.org/terms/view/CT01038)

  Conflict: ChEBI's scope lists conformers as entities ([ChEBI About](https://ebi.ac.uk/chebi/about)), while registries typically merge conformers into one compound (unverified for PubChem and CAS).
- [CONV, conditions] **Berthollide composition varies with temperature and pressure.** Stability is governed by Gibbs energy, and thermodynamics makes "compound vs solution" a matter of degree. — [SEP: Philosophy of Chemistry](https://plato.stanford.edu/ENTRIES/chemistry)
- [CONV conflict] **Isotopes.** They are one element (IUPAC sense 1) but distinct molecular entities (Gold Book, ChEBI).
  - Needham: isotopes' different reaction rates make them different substances.
  - Hendry: thermodynamic criteria cut finer than chemistry needs.

  — [SEP: Philosophy of Chemistry](https://plato.stanford.edu/ENTRIES/chemistry)
- [MODEL debate] **Water and microessentialism.**
  - "Water is H2O" (Kripke, Putnam) is challenged on the ground that H2O is a compositional formula. Liquid water contains self-ionization products and hydrogen-bonded clusters, and van Brakel calls water non-molecular.
  - Needham notes that macroscopic criteria, such as the triple point, define purity standards.
  - Hendry treats H2O molecules as constituents of water and notes that H3O+ and OH− are always present.
  - Pluralist positions: Chang, Bursten, Havstad.

  — [SEP: Philosophy of Chemistry](https://plato.stanford.edu/ENTRIES/chemistry); [SEP: Natural Kinds](https://plato.stanford.edu/entries/natural-kinds)
- [MODEL debate] **Hierarchy vs cross-cutting kinds.**
  - Chemical kinds are often taken as the paradigm natural kinds.
  - Khalidi and Tobin argue the hierarchy requirement fails, citing allotropy (tin, carbon) and functional groups: benzyl alcohol is both an alcohol and an aromatic compound.
  - Slater favours pluralism for macromolecules; Tahko defends monism for biochemical kinds.
  - Dupré's "promiscuous realism" allows many equally objective, cross-cutting classifications.
  - Conventionalists point to how idealized laboratory chemistry is.

  — [SEP: Natural Kinds](https://plato.stanford.edu/entries/natural-kinds)
- [MODEL debate] **The status of molecular structure.**
  - Woolley and Primas argue that quantum mechanics does not yield molecular shape without the Born–Oppenheimer separation.
  - Mátyus et al. (2011) recovered the expected electron density of H2 without it.
  - Hendry treats structure as a possibly emergent "unexplained explainer".
  - Schwarz argues the obstacles to deriving chemistry from quantum mechanics are only computational.

  — [SEP: Philosophy of Chemistry](https://plato.stanford.edu/ENTRIES/chemistry)
- [CONV conflict] **Organic vs inorganic is drawn differently in each system.**
  - CAS puts organometallics (section 29) in the Organic group and inorganic reactions (78) in the PIA group, and splits analytical chemistry into inorganic (79) and organic (80). — [CAS sections](https://www.cas.org/support/documentation/references/ca-sections)
  - IUPAC separates Divisions II and III.
  - ClassyFire splits at its top level, the kingdom. — [classyfireR vignette](https://wilsontom.r-universe.dev/classyfireR/doc/Getting-Started.html)
  - MOFs (Nobel 2025) and organometallics straddle the line. — [Prothom Alo](https://en.prothomalo.com/international/zmdis3c41t)
- [CONV conflict] **Shared jurisdictions.**
  - Biochemical nomenclature is joint IUBMB–IUPAC work. — [IUPAC coding](https://media.iupac.org/general/handbook/coding_bodies.html)
  - ChEBI follows both IUPAC and NC-IUBMB. — [ChEBI About](https://ebi.ac.uk/chebi/about)
  - Materials chemistry is interdivisional within IUPAC. — [Division I page](https://trs.goldbook.iupac.org/divisions/view/1)
- [CONV conflict] **Database identity rules diverge.**
  - PubChem: substance records versus standardized compounds. — [Wikipedia: PubChem](https://en.wikipedia.org/wiki/PubChem)
  - CAS: case-by-case identity review of polymers, UVCBs and mixtures. — [REACH24H](https://en.reach24h.com/news/insights/chemical/cas-registry-number-faq)
  - ChEBI: the constitution/isotope rule. — [ChEBI About](https://ebi.ac.uk/chebi/about)
  - Under manual curation, ontology classes can end up incomplete or inconsistent. — [Mungall et al. 2025](https://arxiv.org/pdf/2505.18470)
- [CONV conflict] **Disputed bond-class boundaries:**
  - C–H···O contacts and blue-shifted hydrogen bonds;
  - σ-hole contacts misclassified as hydrogen bonds;
  - "carbon bond" versus "tetrel bond";
  - the same partner (formic acid) assigned a tetrel bond with SiCl4 but a halogen bond with CCl4.

  — [Chemistry World](https://chemistryworld.com/news/beyond-hydrogen-bonding-new-definitions-for-secondary-bonding-interactions-to-end-confusion/4020237.article); [arXiv 2210.10649v6](https://www.arxiv.org/pdf/2210.10649v6); [PCCP 2024](https://pubs.rsc.org/en/Content/ArticleLanding/2024/CP/D4CP01949K)
- [REC] **Seifert (2023), *Chemistry's Metaphysics*** (Cambridge Elements), argues that the metaphysics of science needs chemistry's cases on natural kinds, realism, reduction, laws and causation. — [Cambridge](https://www.cambridge.org/core/books/chemistrys-metaphysics/2F8BB8139645B18C6690E759B88B8CF7)

### Inferences
- **Condition- and timescale-dependence are written into IUPAC's own definitions**, not merely raised by critics. The species definition carries an explicit observing-timescale clause, and the precision of a molecular entity depends on purpose. Many classifications are therefore relational: membership is fixed relative to a probe (the NMR timescale), to conditions (temperature, pressure, solvent) or to a purpose.
- **"One at coarse grain, many at fine grain" recurs:** element vs isotope, compound vs conformer, compound vs polymorph, polymer vs chain-length distribution. Different institutions stop at different grains, and this is the source of most conflicts in this survey.
- **"Natural vs conventional" is not settled.**
  - Strongest naturalist anchor: atomic number for elements (MP/TD).
  - Strongest conventionalist cases: metalloid lists, electronegativity cutoffs, the choice of acid–base scheme, institutional divisions, and ontologies' curated rules.

### Gaps
- 2023–2026 retractions or reopenings of disputes over chemical kinds, e.g. the status of metallic hydrogen or of contested superconducting hydrides.
- IUPAC's formal positions on metalloids and on acid–base definitions.
- Any 2023–2026 IUPAC project to redefine "chemical element".
- Whether a reasoning-based (OWL) reclassification of ChEBI has been deployed since ChEBI 2.0.
