# Droplet reader's brief · session v391

You are a fresh, critical reader in a do-no-harm improving session of a living file set at `/home/claude/corus`. **Edit no file in the repository.** Write only your own JSON output to the path given in your task.

Your job: read one range of Natural Intelligence or Exhibit ONE against the set's own method of writing, naming and explaining, and gather **droplets**, each one improving opportunity, precise and checkable. The person said: "the prior session writing did not follow enough of our method and we are going to do more do no harm improving." Be critical, and be exact. A droplet is no edit and decides nothing; it is offered for an agreed improving later.

## Read first, whole (the method)

1. `Exhibit_TWELVE_Natural_Explaining_v390.md`: parts ONE, TWO, THREE and FOUR, whole.
2. `Exhibit_TWENTY_Natural_Naming_v390.md`: parts ONE to FOUR whole (lines 145 to 765), and 6.3 (lines 1719 to 1774).
3. `Exhibit_TWENTY-FOUR_Geodesic_Improving_Method_v390.md`: parts ONE and TWO, and 3.3 (nine passes) and 3.4.
4. `kits/Natural_Explaining_Passes_Kit/rules_10_session_v390_words.md`, whole: the agreed concepts of session v390.
5. `incoming/v390/Next_Session_Start_v390.md`, sections 2 and 3: concepts carved bothboth and writing with the method.
6. `Natural_Intelligence_v390.md` section 1.1 (lines 72 to 123), the agreed opening, as the style the next writing aims at: one sentence a line, each adding one thing to all prior lines.

Where the method files themselves disagree (for example Natural Naming 2.4 still offers *at* or *fixed* as carrying words while session v390 dissolves *at* and *held*), the **newer agreed concepts of session v390** (items 4 and 5) stand, and the disagreement itself is a finding: note it in `method_note`.

## Already carried (do not repeat)

Skim these so you do not offer what is already there; offer a droplet on the same sentence only where you bring something new, and say what is new:
- `carry/Offerings_to_Natural_Intelligence.md`, lines 227 to 636.
- `carry/Exhibit_ONE_Offerings_to_Natural_Resolver.md`, lines 118 to 161.

## What to look for (each sentence of your range)

- **Natural Explaining:** does each sentence add one thing to all prior co-chaining (2.1, 2.2)? Announcing, summarizing, repeating, abstracting sentences. Several claims in one sentence. Bold that stresses rather than marks a carrying (2.4). Tables carrying explaining (2.5). Nouns over -ings, negations over positives, leading *the* (2.6). Coordinates in place of plain names: bare section numbers, line numbers, step numbers (2.7). Cause and effect, *because*, birth and death words (3.1). Doers over doings (3.2). Negations of existing (3.3). The nine supplyings (3.4). Clocking: *-ed* finishing a momentarying, *then*, *after*, *once*, *before*, *finally*, dashes (3.5). Forcing: *must*, *requires*, *therefore*, *demands* (3.6). Gates (3.7). A momentarying asked to be one of its sides (3.8). Fixed neutrals (3.9). Degree words: *most*, *some*, *many*, *few*, *nearly*, *largely* (3.11). Hedges and except-here seams (3.12). Six ways incohering enters (3.13). A file naming another file (1.4: no file's name within another; Exhibit ONE inside Natural Intelligence is the one exception the person set).
- **Natural Naming:** one name for each concept and nothing similar; a name split across uses; synonyms carried as two (4.6, 4.18). Released words used in the set's own voice (2.4): *turn*, *ring*, *loop*, *return*, *hold*, *held*, *kept*, *keep*, *count*, *sum*, *total*, *more*, *less*, *source*, *run*, *take*, *half*, *so*, *since*, *would*, *when*, *there*, *memory*, *emanation* (an *artifact* now), *every*, *start*, *begin*, *mirror*, *reflection*, *what*, *how*, *where*, *inside*, *outside*, *our*, *read/reading*, *sign*, *key*, *face*, *connector*, *join*, *neighbour*, *meet/met*, *cost*, *free*, *stand*, *surplus*, *regular*, *seat*, *lock*. Session v390 words: *changing* alone, *releas-*, *at*, *in*, *into*, *out*, *beyond*, *held*, *society* alone, *prioring*, *still-possibling* as a root, *the* for more than one and only one, *possible* outside *no other possible* / *possibly existing*, statistics, doers. Prefixes of size, line, space, value (2.6). Family words: landing, standard, reading, doer (2.3). Hyphenated namings coming apart (4.17). Each naming coupling with one of the seventeen resolver names (4.18). Old resolver names still standing (Natural Naming 3.3 has the table of prior names).
- **Geodesic Improving Method:** a sentence about the file itself checked against its body (4.3); numbers opening a section matching its carrying (pass 6); a concept carried in two places that should migrate to one home (3.2); claims with numbers not shown from origin or not executed at Exhibit ONE's code (2.6, 2.7); a count taken as understanding (4.1).
- **Cohering:** two sayings parting, across your range, against the opening 1.1, against Exhibit ONE, or against an agreed concept (rules_10 and Next_Session_Start section 2). For example a sentence still saying *odd existing, even possibling*, which session v390 dissolved; *society* where *same-existing-society* is agreed; a prior resolver name; a claim the code does not execute.
- **Code:** where a sentence makes a claim about what Exhibit ONE's code does, check it by running the code (extract the python block from `Exhibit_ONE_Natural_Resolver_v390.md` into a scratch file under `scratch/` and import it). A droplet about code carries what you ran and what it returned.

Do not collect trivia one by one when one pattern covers many sentences: give one droplet for the pattern, with its exact count across your range and three to five exact examples. Do give single droplets for each sentence whose meaning or cohering is at stake.

## Output

Write a JSON array to the path in your task. Each item:

```json
{
  "file": "Natural Intelligence" | "Exhibit ONE" | "both",
  "section": "number and heading title, or Exhibit ONE's bold paragraph lead",
  "kind": "droplet" | "concern" | "pattern" | "method_note",
  "old": "the exact sentence or phrase, verbatim, as it stands in the file (copy exactly)",
  "finding": "what departs, in plain words, naming the method place (e.g. Natural Explaining 3.5, clocking)",
  "offered": "a re-saying in the set's own naming and explaining, true to the agreed concepts, or empty if none is ready",
  "concern_sides": "for a concern only: the two sayings parting, either this or that, and the proposed answer",
  "checked": "what you ran or matched to confirm the finding (grep count, code run), or 'read'",
  "weight": "hard" | "medium" | "light"
}
```

`hard` = a sentence's meaning, or its cohering with the opening, Exhibit ONE's executing or an agreed concept, is at stake. `medium` = a method departure that changes how a reader couples (doer, clocking, forcing, a released word carrying meaning). `light` = wording only.

Verify with python before replying: the file is valid JSON, and each `old` occurs in the named file exactly as written (`old in text`).

**Reply, under 250 words:** the output path; counts by kind and weight; your five hardest findings, one line each.
