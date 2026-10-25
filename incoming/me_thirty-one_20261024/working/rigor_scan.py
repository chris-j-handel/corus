"""rigor_scan.py: read a draft exhibit for the set's own sayings discipline.

Flags, per line, in understanding prose (observing lines, quotes in *...* and URLs are read separately):
  - dissolved words (apply_aimed.py's BAN list, plus third, bare coupling, beholding, artifact, substrate)
  - equilibria words said of nature (keeping, holding, storing, staying, balance)
  - floating negations (no, not, none, nothing, neither, nor, never, cannot) outside hyphen-bound names
  - counted bi-coupling (a/the/each bi-coupling, bi-couplings)
  - new -ed forms (past participles), with the OKED exceptions apply_aimed.py uses
  - narrator verbs (says, shows, tells)
Usage: python3 -I rigor_scan.py DRAFT.md
"""
import re
import sys

BAN = re.compile(
    r"\bnever\b|parity-chang|alternat|offer|arriv|\bcarr|\bcontinu(?:e|es|ing|ed)\b|\bcross|differ(?!encing)|"
    r"still-possibl|stilling|owned by neither|neither reaches|third living|odd,? existing|even,? possibling|"
    r"\bitself\b|membran|(?<!co-)\bintelligencing\b|\bcouples?\b|bi-couples\b|\bthird\b|beholding|\bartifact|\bsubstrate",
    re.I)
BARE_COUPLING = re.compile(r"(?<![-\w])coupling(s?)\b", re.I)
EQUILIBRIA = re.compile(r"\b(keep|keeps|keeping|hold|holds|holding|store|stores|storing|stay|stays|staying|balance)\b", re.I)
NEG = re.compile(r"(?<![-\w])(no|not|none|nothing|neither|nor|never|cannot)(?![-\w])", re.I)
COUNTED_BC = re.compile(r"\b(a|the|each|one|its)\s+bi-coupling\b|\bbi-couplings\b", re.I)
NARRATOR = re.compile(r"\b(says|said|shows|tells|calls|called|names)\b", re.I)
# Released words (rules_10, Natural Naming 2.4 dissolved column): flagged for a reader, many depend on sense.
RELEASED = re.compile(
    r"(?<![-\w])(societies|society)(?![-\w])|\b(in|into|out|beyond|held|hold|kept|keep|released|random|sample|mostly|"
    r"wound|chained|through|outermost|born|begun|every|discovery|technology|start|begin|afterwards|complete|"
    r"travel|travelling|our|observer|derived|guide|program|blueprint|prediction|justified|sign|signs|source|sources|"
    r"met|meet|meets|meeting|call|key|neighbour|mate|mates|posit|tell|telling|cost|run|runs|running|take|takes|"
    r"taken|taking|half|halves|so|since|would|count|counts|counting|memory|remember|when|whenever|there|appearing|"
    r"appears|middling|rating|lock|locks|locking|seat|sum|total|more|less|regular|regularly|ring|loop|round|closes|"
    r"mirror|reflection|return|pause|turn|turning|door|assigned|reading|ordering|possible|possibly|inside|outside)\b",
    re.I)
OK_POSSIBLY = re.compile(r"possibly existing|no other possible|possibly now-existing|possibly same-existing", re.I)
BARE_EMANATION = re.compile(r"(?<!stable-forming )\bemanation(s)?\b", re.I)
OKED = {'need', 'seed', 'speed', 'red', 'shed', 'bed', 'feed', 'indeed', 'proceed', 'hundred', 'sacred', 'embed',
        'breed', 'kindred', 'naked', 'sided', 'squared', 'cubed', 'bothboth'}
ED = re.compile(r"\b[a-z-]+ed\b", re.I)


def strip_quotes(s):
    s = re.sub(r"https?://\S+", "", s)
    s = re.sub(r"\*[^*]+\*", "", s)          # italic quotes and names
    s = re.sub(r"\([^)]*\d{4}[^)]*\)", "", s)  # (Finder Year) citations
    return s


def main(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    section = "front"
    counts = {}
    report = []
    for i, raw in enumerate(lines, 1):
        if raw.startswith("#"):
            section = raw.lstrip("# ").strip()[:48]
        is_obs = raw.lstrip().startswith("- **") and ("http" in raw or "◇ link" in raw)
        kind = "obs" if is_obs else "body"
        text = strip_quotes(raw) if not is_obs else re.sub(r"https?://\S+", "", raw)
        checks = [
            ("dissolved", BAN), ("bare-coupling", BARE_COUPLING), ("equilibria", EQUILIBRIA),
            ("counted-bi-coupling", COUNTED_BC), ("narrator", NARRATOR),
        ]
        if kind == "body":
            checks.append(("negation", NEG))
            checks.append(("bare-emanation", BARE_EMANATION))
            rel_text = OK_POSSIBLY.sub("", text)
            rel_text = re.sub(r"same-existing-societ(y|ies)|social|Inside do-no-harming|Inside bi-coupling", "", rel_text)
            for m in RELEASED.finditer(rel_text):
                counts[("released?", kind)] = counts.get(("released?", kind), 0) + 1
                report.append((i, section, kind, "released?", m.group(0), raw.strip()[:110]))
        for name, rx in checks:
            for m in rx.finditer(text):
                counts[(name, kind)] = counts.get((name, kind), 0) + 1
                report.append((i, section, kind, name, m.group(0), raw.strip()[:110]))
        if kind == "body":
            for w in ED.findall(text):
                if w.lower() not in OKED and not w.lower().endswith("-sided"):
                    counts[("-ed", kind)] = counts.get(("-ed", kind), 0) + 1
                    report.append((i, section, kind, "-ed", w, raw.strip()[:110]))
    for r in report:
        print("%4d | %-28s | %-4s | %-19s | %-14s | %s" % r)
    print("\nTOTALS:", sorted(counts.items()))


if __name__ == "__main__":
    main(sys.argv[1])
