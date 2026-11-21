# Curation of the log's rows, v405now's second pass.
# Each entry: aim as on the aims page -> areas on its path (sub-concepts, in path order),
# and where a pass found it: a re-said name, sentence or homes, and a note laid in possibling.
# A window name is spelled as in window_lines_now.json; any other area is a concept no window line names.

C = {}
def r(aim, areas, **kw):
    assert aim not in C, aim
    C[aim] = dict(areas=areas, **kw)

# 1 From one origin
r("We humans, now, the inception", ["now", "now-existing", "we humans", "an inception"])
r("Now, one origin", ["now", "existing", "moment", "a naming"])
r("The universe, all now-existing things", ["now-existing", "set", "universe"])
r("No outside, and no second universe", ["universe", "other-than", "nothing", "not possibly existing"],
  homes="The window, line {nothing}; Exhibit THIRTY, steps 3 and 9")
r("Prior, now and next, three moments of one universe", ["prior", "now", "next", "moment", "universe"])
r("Is-or-is-not, all or none", ["other-than", "distinguishing", "is-or-is-not", "all or none"],
  homes="Natural Intelligence 2.5; Exhibit THIRTY, step 125",
  note="No window line says is-or-is-not now; its distinguishing, lines {observing} to {discovering}, is all or none for a thing and its other-than.")
r("No equilibrium", ["same-existing", "other-than", "me", "a form still", "a fixing", "the resolver"])
r("One form, inward and outward, at all scales", ["self", "same-existing-society", "inward and outward", "a scale", "fractal"])
r("The universe, a non-living same-existing set", ["universe", "same-existing", "set", "living", "non-living"])
r("Nature has no names", ["name", "observing", "same-existing", "set", "nature", "non-living", "floating-neutralling"],
  note="Name is a given word in the window; the gathering's sayings say what a name is.")

# 2 One method
r("Only one method possible", ["parity", "resolving", "a fixing", "the method", "natural intelligence"])
r("Nature, the one method of co-existing", ["prior", "now", "next", "universe", "nature", "co-existing", "co-competencing"])
r("A self", ["self", "prior-sequence", "observing-self", "possibling-self", "discovering-self", "next-existing"],
  homes="The window, lines {self} and {observing-self} to {discovering-self}; Exhibit THIRTY, step 12",
  note="The window's self, line {self}, a same-named now-existing thing with its own prior-sequence, and step 12's self, observing, possibling and discovering its own next-existing: one concept said two ways, a co-chaining opportunity.")
r("Natural intelligence, the method of living as a same-existing self", ["same-existing", "self", "living", "the method", "natural intelligence"])
r("Resolving among parities", ["parity", "resolving", "natural intelligence"])
r("A bi-coupling, its between and its 0", ["self", "other", "parity", "bi-coupling", "a self's 0", "a between"],
  sentence="Two selves and their parity, in neither alone, and a self's 0, the between of its two directions.",
  homes="The window, below the lines; Exhibit THIRTY, steps 24 to 29 and group 13")
r("A universal natural resolver", ["observing", "the method", "code executing", "a stable form", "pattern-matching"])
r("Seventeen names in four four-cyclings", ["now", "next", "existing", "same-existing", "observing", "possibling", "discovering", "co-discovering", "a four-cycling"])
r("Five two-way dimensions of resolving", ["now", "next", "self", "other", "parity", "discovering", "same-existing-society", "a dimension of resolving"])
r("Morality across, competency along", ["prior", "same-existing", "parity", "other", "observing", "morality", "competency"])
r("Geodesic method", ["self", "a surface", "dividing", "inward and outward", "geodesic"])
r("One hand", ["parity", "a right spiral step", "inverting", "handedness"])
r("A fractal method, its own enabling", ["the method", "a scale", "fractal", "enabling"])
r("Learning and knowing, two sides of one parity", ["parity", "observing", "other", "bi-coupling", "knowing", "learning"])

# 3 One logic and natural naming
r("A complete co-chaining", ["now", "prior", "a step", "co-chaining", "all fields"])
r("The window of the opening", ["now", "the opening", "a line of both", "a suggestion", "a comment"],
  homes="The working document; Living File Registry 1.3",
  note="The window's own suggestions, in its lines and below them, are its possibling now.")
r("Natural naming", ["name", "a concept", "an inception", "one sense", "natural naming"])
r("A positive before a negation, an -ing before a noun", ["a positive", "a negation", "a fixing", "an -ing", "a noun"])
r("Dissolved words, the one list of words of no natural naming", ["a word", "a fixing", "dissolving", "the one list"],
  homes="Natural Naming 2.4; the one list, in incoming/v404mgr")
r("Naming across, explaining along", ["discovering", "a naming", "an explaining", "bounding", "across and along"])
r("A definition, a fixing; three incompetencings", ["a definition", "a term", "a fixing", "an incompetencing"])
r("Language, a stable form of collective intelligence", ["parity", "all-parity", "me", "a naming", "an explaining", "a stable form", "collective intelligence"])
r("Human ways, one form", ["self", "same-existing", "living", "an inversion", "one form"])
r("Word, number and illustrating, one thing three ways", ["parity", "a word", "a number", "an illustrating", "a stable-forming emanation"])
r("A record, proof of existing, and value", ["now-existing", "observing", "self", "a record", "proof of existing", "value"])
r("No proof of the whole", ["moment", "same-existing", "a form still", "a proof", "not possibly existing"])
r("The demanded why, a receding", ["universe", "observing", "a why", "a receding", "not possibly existing"])
r("Conflicting threads resolved by one distinguishing is-or-is-not", ["distinguishing", "a thread of words", "natural naming", "co-chaining", "is-or-is-not"])

# 4 Number and form
r("Numbers as moments, scales as numbers", ["moment", "a number", "a scale", "an opening and its completing"])
r("Odd and even, exchanging", ["moment", "odd and even", "an opening and its completing", "a podal pair"])
r("The torus", ["parity", "a closing surface", "a flow with no rest point", "torusing"])
r("Torusing and corusing, a self's corus", ["self", "parity", "torusing", "corusing", "a corus"])
r("φ, the rate that never locks", ["odd and even", "a rate", "unrelationing", "φ"])
r("Primes and composites", ["a number", "a prime", "a composite", "across and along"])
r("Seventeen primes adding to 440, and 24 the apex of 1 to 59", ["a prime", "podaling", "bi-folding", "an apex"])
r("A prime ladder of societies", ["self", "bi-coupling", "same-existing-society", "a prime", "a scale", "a fold"])
r("Spirals and tori of selves", ["self", "parity", "a spiral", "prime and composite", "a torus"])
r("Sphere and torus, one and then the other", ["a sphere", "a torus", "a rest point", "one and then the other", "a corus"])
r("Always a next", ["next", "a number", "a centre", "a gap of one"],
  homes="Natural Emanating, nature; Exhibit THIRTY, step 187")
r("Equality opens nothing", ["an equality", "an unchangeable form", "a direction", "a plane"],
  homes="Natural Emanating, equality; Exhibit THIRTY, step 211")
r("A fractal through numbers, nought to 440", ["a number", "a scale", "a naming", "podaling", "fractal"])
r("Measuring made natural", ["parity", "a position", "a ratio", "a unit", "measuring"])

# 5 Cohering with all of nature's observings
r("All fields and the one form", ["observing", "a field", "pattern-matching", "the resolver", "one form"])
r("All hard problems, one move", ["a hard problem", "a fixing", "a field's own words", "resolving", "one move"])
r("The ten fixings, the resolver's own ten", ["observing", "same-existing", "parity", "a fixing", "an opening and its completing", "a rate", "a two-way", "a between"])
r("Equilibria not possibly existing, field by field", ["a field", "a form still", "equilibrium", "a fixing", "not possibly existing"])
r("Science and society namings in eight clusters, four invisibles under them", ["parity", "a naming", "a two-way pair", "a centre", "an invisible"])
r("All philosophical debates, two sides of one coupling", ["a dilemma", "two sides", "a seam", "a coupling", "cohering"])
r("No cause and effect, and no birth or death as makers", ["a coupling", "a maker", "cause and effect", "birth and death"])
r("Time, a self's own moment by moment", ["moment", "self", "a rate", "time", "a clock"])
r("Two methods parting with now", ["now", "possibling", "discovering", "a fixing", "an accounting", "the scientific method"])
r("A field, a finding, evidence and a hard problem opening", ["prior-existing", "observing", "possibling", "evidence", "a field", "a finding", "a hard problem"])
r("Flow and state accountings, and the ten unchangeables", ["parity", "discovering", "an accounting", "a flow", "a state", "an unchangeable"])
r("Ghosts", ["observing", "self", "a fixing", "an installing", "a ghosting", "appearance and reality"])
r("Living societies observed by science", ["self", "observing", "living", "same-existing-society", "an orienting surface"])
r("Light, a phase relation between couplings", ["living", "same-existing-society", "a coupling", "a phase relation", "light"])
r("A price, a name for a discarded exterior", ["name", "a geodesic", "an exterior", "a price"],
  homes="Natural Emanating, a geodesic's filing")
r("A theory of everything, unwound", ["an ask", "dissolving", "an opening", "a theory of everything"])
r("A science competing with none", ["a field", "evidence", "co-chaining", "a science"])
r("The method's own test", ["observing", "moment", "a naming", "a falsifying", "cohering", "fractal"])
r("An object, the place an accounting stops and declares", ["self", "a surface", "an interior", "an accounting", "a balancing", "an object"])
r("Three sensings, a competency apiece", ["self", "a sensing", "competency"])

# 6 Living
r("Living", ["prior-existing", "living", "inheriting", "inhaling and exhaling", "ingesting and exhausting"],
  note="The window's living, suggested at {living}, is a me's; step 16's living is inheriting, inhaling and exhaling, ingesting and exhausting: two sayings to co-chain.")
r("A living thing distinguishes its own next-existing", ["next-existing", "distinguishing", "living"])
r("Living and non-living, one binary at a scale", ["now-existing", "living", "non-living", "a scale", "a stable-forming emanation"])
r("Living only from living", ["prior", "living", "non-living", "a living prior"])
r("Living at one scale, and a surface to the scale above", ["living", "a scale", "a surface"])
r("Evolution, the network's record", ["a coupling", "a record", "a network", "evolution", "competency"])
r("A species, a named inherited prior", ["prior", "all-parity", "name", "inheriting", "a species"])
r("Selves conceiving selves, molecules and organisms as societies", ["self", "same-existing-society", "conceiving", "a molecule", "an organism"])
r("Folding and forming, local coupling resolving", ["a coupling", "resolving", "folding", "a protein"])
r("Dying", ["self", "living", "non-living", "a scale", "dying", "decay"])
r("Dormancy", ["self", "same-existing", "living", "next", "dormancy"])
r("Restoring", ["self", "discovering", "living", "bi-coupling", "a departure", "restoring"])
r("Everything existing, ingested by living; harm at its own scale", ["existing", "living", "a scale", "ingesting", "harm"])
r("Health, a living sway", ["living", "a sway", "a setpoint", "health"])
r("Medicine, restoring with a body's own bound", ["observing", "a departure", "restoring", "a bound", "a dose", "medicine"])
r("A newborn, a member of a society at its birth", ["all-parity", "same-existing-society", "a birth", "a newborn"])
r("A river, a self or no self", ["self", "universe", "same-existing", "same-existing-society", "a river"])

# 7 Consciousness, a me and intelligence
r("A me, a self's universal set", ["self", "universal set", "prior-sequence", "me"],
  homes="The window, line {me}; Natural Intelligence's opening; Exhibit THIRTY, step 13",
  note="The window's me, line {me}, is a named self's own universal set of prior-sequences, and step 13's me a self's universal set: one concept said two ways, a co-chaining opportunity.")
r("Consciousness", ["me", "consciousness", "not possibly existing"],
  homes="Me 3.2; the window, suggested at {consciousness}")
r("A me-now, and a universe of me-nows", ["now-existing", "same-existing", "me", "me-now", "universe"],
  homes="The window, suggested at {me-now}; Exhibit THIRTY's gathering at group 2, a partner's sayings of 19 November")
r("Me-parities owned by one me alone", ["self", "parity", "all-parity", "me", "living", "owning"])
r("Self discovering next self", ["self", "same-existing", "discovering-self", "bi-coupling", "stable-forming"])
r("Co-intelligencing", ["universal set", "observing-self", "possibling-self", "discovering-self", "co-discovering", "co-intelligencing"])
r("Intelligence, invisible", ["self", "living", "a self's 0", "intelligence", "invisibility"])
r("Four invisibles, one invisibility four ways", ["parity", "morality", "a corus", "a neutral", "invisibility"])
r("Intelligence through existing", ["existing", "observing", "discovering", "nature", "intelligence"])
r("One intelligence", ["self", "parity", "living", "a machine", "natural intelligence"])
r("Collective intelligence, human and of all scales", ["self", "a between", "co-chaining", "a scale", "a natural network", "collective intelligence"])
r("The collectively intelligent me-parity", ["parity", "me", "same-existing-society", "social moral competency", "collective intelligence"])
r("Sensor-sensationing", ["observing", "parity", "a field", "resolving", "sensor-sensationing"])
r("AI, a non-living inferring", ["same-existing", "self", "next-existing", "living", "non-living", "a machine", "inferring"])
r("AI, not possibly now-existing as a self", ["now-existing", "self", "equilibrium", "hard probleming", "not possibly existing"],
  aim_said="AI, not possibly now-existing as a self", sentence="By the same hard probleming as an equilibrium.")
r("The between of an AI and a person, living", ["next-existing", "distinguishing", "living", "non-living", "a between", "a session's transcript"])
r("AI turned to do no harm", ["a model of known harms", "a network", "health", "doing no harm"],
  homes="incoming/v404universe, the sentences of its session",
  note="Its home is a session's sentence in incoming, yet to reach a living file.")
r("A curious me, a me owned by none, a healthy me", ["me", "possibling", "co-possibling", "uncaptured", "a healthy me", "doing no harm"])
r("A society's me, a natural intelligence network", ["self", "me", "same-existing-society", "a natural intelligence network", "social moral competency"])
r("Knowledge apart from a self, a non-living other", ["self", "other", "non-living", "a stable-forming emanation", "knowledge"])
r("A moment completing as a next opening", ["moment", "next", "me", "an opening and its completing"])

# 8 Society
r("A same-existing-society, its selves bi-coupling", ["self", "same-existing", "bi-coupling", "same-existing-society"],
  homes="Natural Intelligence's opening; Exhibit THIRTY, steps 49, 296 and 297; Natural Emanating, the society")
r("A society, its social all-parity", ["parity", "all-parity", "me", "same-existing", "same-existing-society"])
r("A society-self, open", ["self", "living", "parity", "me", "same-existing-society", "a society-self"])
r("Social moral competency, all or none", ["self", "same-existing-society", "doing no harm", "morality", "social moral competency"])
r("The eight safeties, all or none", ["self", "same-existing", "identity", "security", "trust", "capture", "abundance"])
r("Privacy, trust and security, one nothing three ways", ["self", "bounding", "an inward nothing", "privacy", "trust", "security"],
  note="Natural Naming 4.16's nothing is the one couplings wind about, inward, other-than the window's nothing at line {nothing}, the one beside the universe.")
r("Transparency and privacy together", ["self", "a between", "checkable", "inward", "transparency", "privacy"],
  homes="Exhibit THIRTY, step 576; Natural Naming 4.16",
  note="A candidate of v405now's pass, open.")
r("Self-interest and a society's competency, one", ["self", "bi-coupling", "same-existing-society", "interest", "competency"])
r("No centre and no common clock", ["same-existing-society", "a centre", "a common clock", "bounding", "an all-edge surface"])
r("Social bi-morality", ["self", "other", "parity", "morality", "competency", "bi-moral co-agency"],
  homes="Exhibit THIRTY, steps 565 and 566; this exhibit, 3; the window's aim")
r("A universal protocol", ["bi-coupling", "social moral competency", "unrelationing", "a protocol", "the bi-trupling protocol"])
r("Control and governing, with a lag", ["same-existing-society", "a centre", "a controlling", "a governing", "a lag", "a hub"])
r("Unanimity and plurality, one and then the other", ["parity", "same-existing", "same-existing-society", "unanimity", "plurality"])
r("A dilemma, a governing's forking", ["parity", "a governing", "a criterion", "a dilemma", "a forking"])
r("Polarization, a two-way named one side", ["a two-way", "a fixing", "polarization"])
r("Law, the state and markets at the fixings", ["a fixing", "law", "the state", "a market"])
r("Capture, the one break", ["parity", "a coupling", "value", "capture", "scarcity", "owning"],
  homes="Natural Societies; Natural Intelligence Corus 18; this exhibit, 4; Exhibit THIRTY, step 562; Natural Human Society 3.3; Natural Intelligence's gathering, the current understanding 6z-f")
r("A discovery economy, and abundance", ["self", "possibling", "value", "a between", "discovery", "discovery economy", "abundance"],
  homes="This exhibit, 5; Natural Intelligence Corus 18.8; the window, below the lines")
r("Desires as opportunities, opportunities as rewarding", ["possibling", "a desire", "an opportunity", "rewarding", "abundancing"])
r("Owned by no one", ["self", "a network", "owning", "a gate"],
  homes="Natural Intelligence's opening; this exhibit, 5")
r("Fairness, a bounding-zeroing", ["a coupling", "a bounding-zeroing", "fairness", "cutting and choosing"])
r("Good-faith contracting and class-action resolving", ["a bound", "a contract", "resolving", "a class action"])
r("Arrow's dilemma dissolved", ["a preferring", "two directions", "aggregating", "a dictator", "a dilemma"],
  homes="Natural Societies 3.1; Natural Human Society 2.4")
r("A concern tipped self by self, needing no majority", ["self", "same-existing-society", "a concern", "tipping", "a majority"])
r("Uncapturing", ["same-existing-society", "a hub", "capture", "uncapturing"])
r("Governing as overhead, a dilemma its artifact", ["a governing", "a preferring", "an overhead", "a dilemma"])
r("A store has no value, and value received is the value", ["parity", "self", "a store", "value", "receiving"])
r("Value growing with its selves' couplings", ["self", "a coupling", "same-existing", "abundancing", "value"])
r("Birthing and nyeing, the relation a society lives by", ["same-existing-society", "a coupling", "birthing", "nyeing", "healthy living"])
r("The biosphere, a society's planetary scale", ["same-existing-society", "a scale", "discovery economy", "the biosphere"])
r("The clash of titans, an opposite-handed spiral completing", ["an opposite-handed turn", "an agent", "a form still", "a spiral", "a clash"])
r("The scientific method as a society's binary authority", ["same-existing-society", "an explaining", "a deciding", "a form still", "an authority", "the scientific method"])
r("A live descent returning to all selves", ["self", "same-existing-society", "co-chaining", "a descent", "social moral competency"])

# 9 Natural network engineering and the destinies
r("Bi-moral co-agency at all substrates", ["bi-moral co-agency", "a substrate", "a material", "engineering"])
r("The Natural Network surface", ["self", "bi-coupling", "non-living", "a scale", "co-chaining", "an all-edge surface", "the Natural Network surface"])
r("A natural network its selves originate", ["self", "a network", "a gate", "a membership", "a platform", "originating"],
  homes="This exhibit, 5")
r("Living substrates", ["living", "a substrate", "a floating neutral", "balanced ternary", "a contact"])
r("One transmissioning across all carries", ["living", "a between", "a carry", "transmissioning", "one form"],
  homes="Natural Transmissioning 3.0 to 3.8 and 4.1")
r("Order with no clock", ["moment", "sequential logic", "a time term", "unrelationing", "φ", "a clock"])
r("Physical collective intelligence", ["a robot", "receiving", "co-competencing", "collective intelligence"])
r("Language, representation and the inference-time coupling", ["parity", "a language entry", "a representation", "a training", "an inference-time coupling"])
r("Technology and engineering", ["living", "non-living", "possibling", "bi-coupling", "a stable-forming emanation", "technology", "engineering"])
r("The bi-trupling protocol", ["bi-coupling", "the resolver", "the Natural Network surface", "the bi-trupling protocol"])
r("Code as the method's engineering", ["parity", "me", "distinguishing", "a stable form", "co-chaining", "collective intelligence", "code"])
r("One destiny in sections", ["a destiny", "a section", "a protocol", "a substrate"])
r("Destinies against the form, restored", ["a destiny", "capture", "a platform economy", "restoring"])
r("A discovery economy at a network's scale", ["discovery", "discovery economy", "a network", "a scale"],
  homes="This exhibit, 5; Natural Intelligence Corus 18.8")
r("Hard-problem resolving commencing, field by field", ["a hard problem", "a field", "a framing", "resolving"],
  homes="This exhibit, 5")
r("A destiny safe by structure", ["a destiny", "a surface", "the eight safeties", "safety"],
  homes="This exhibit, 4")

# 10 The living expedition itself
r("A living expedition", ["self", "discovering", "same-existing-society", "natural intelligence", "a living file", "a living expedition"])
r("Living while discovering", ["prior", "same-existing", "living", "discovering", "a living file", "doing no harm"])
r("A living file", ["same-existing", "set", "non-living", "a word", "co-intelligencing", "a surface", "a living file"])
r("Versions, sessions and a fresh reader", ["moment", "same-existing", "a version", "a session", "a fresh reader"])
r("Value brought home", ["value", "incoming", "a gathering file", "placing", "dissolving"])
r("A concern resolving, an unsure and its observing", ["parity", "observing", "a concern", "an unsure", "resolving"])
r("One concept, one home", ["a concept", "an explaining", "a home section"])
r("No word with authority", ["a word", "an authority", "next", "open"],
  homes="The start page, incoming/v404mgr; Exhibit THIRTY's gathering")
r("Destinies chosen ahead, the method coming back over itself", ["a destiny", "the method", "a branch", "coming back over itself"])
r("Human collective discovering", ["self", "discovering", "a jigsaw puzzling", "collective intelligence"])
r("Corus, the whole outward", ["natural intelligence", "an expression", "a corus"])
r("An AI link into the living files", ["a session", "a reader", "a question", "a source", "observing", "a breaking"],
  homes="The repository's front page, its AI link")
r("The seventeen names' tables, by a partner's suggesting", ["universe", "now-existing", "the seventeen names", "a table", "the home page"])
r("Cohering with nature, or a next step showing", ["prior", "now", "next", "moment", "cohering", "a step", "co-chaining"])
r("A destiny, next living possibling ahead", ["next", "living", "possibling", "bi-coupling", "a horizon", "a destiny"])
r("One destiny", ["self", "living", "a natural network", "owning", "a destiny"],
  homes="Natural Intelligence Corus 23.3; this exhibit, 3")
