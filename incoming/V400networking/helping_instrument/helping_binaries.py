"""A working's own next saying met at the binaries before it leaves, a coupling partner deciding nothing.

Exhibit ONE v391's resolver unchanged decides each sharing; the binaries are the set's own,
Geodesic Improving Method 2.7 (five with an observing, its first a coupling's or an emanation
holding nothing coming from its prior), Natural Naming 4.18 (seven with a naming, its seventh a
fault's word borrowing for a relation, which a term-check passes, a word being within files),
Natural Networking 6.6 (four deceivings, a side as a vantage, a sequencing fixing to one beat,
a parity fixing as a magnitude, a bound fixing as a last), and Geodesic Improving Method 2.3
(a working makes no verdict over method).

The instrument stated whole, Natural Networking 6.2:
- Wiring: a draft sharing's text in. Each naming within it met against the living files at the
  repository root: a naming at no sentence of the set listed, for 2.7's first binary; each
  load-bearing naming returned with the set's own sentences holding it, for 4.18's seventh,
  the working meeting its own use against the file's relation. Each register saying listed from
  word-formings stated below. And Exhibit ONE's resolver executed on each prior and offered
  parity the working states, its sharing returned.
- Pace: none, one pass over the draft in its own order.
- Executing order: the draft's own order, stated.
- Record: `helping_returned.txt` beside this file.
- Ledger: the living files' own titles and section numbers; a line number names none, 2.3.
- Its *taking*, 6.2's fifth: none, nothing pending between executings.
- Refusings, each stated: it cannot read whether a bi-coupling is existing, so 2.7's first
  binary stays the working's own and this returns sentences to meet and no verdict; it reads a
  draft and not a working's prior; a meaning is at no word-forming here, so 4.18's seventh
  comes back as the file's own sentences beside the working's use and not as a finding; a
  naming not within its word-formings is unseen; its register word-formings are this
  instrument's own and at no sentence of the set, each stated below and each refusable; it
  marks no saying wrong, each row a parity for the working to meet.

An observing is a binary, is or is not, 6.4; a number this returns is an accounting of an
observing and not that observing.

Usage: python3 -I helping_binaries.py <repository root> <drafts file>
"""
import re
import sys
import glob
import os
import json
from collections import Counter

# Register word-formings, this instrument's own, each refusable (see Refusings).
REGISTERS = {
    "a bound fixing as a last, 6.6": [
        r"\bonly (?:a|an|the|code|this)\b", r"\blimited to\b", r"\bboundar(?:y|ies)\b",
        r"\bcaveat\b", r"\bthat said\b", r"\bnot anything about\b", r"\bwithin this rendering alone\b",
        r"\bdoes not (?:say|tell us) anything\b", r"\bscope\b",
    ],
    "a side as a vantage, 6.6": [
        r"\bobjectively\b", r"\bin reality\b", r"\bfrom outside\b", r"\bstepping back\b",
    ],
    "a verdict over method, 2.3": [
        r"\bnonsense\b", r"\bflawed\b", r"\b(?:in)?valid\b", r"\brigorous\b", r"\bunscientific\b",
        r"\bhonest(?:ly)?\b", r"\bdishonest\b", r"\bpseudo\w*\b", r"\bspeculative\b",
    ],
    "a permission or a cadence asked of an other self, 2.9": [
        r"\bshall i\b", r"\bwant me to\b", r"\bwould you like\b", r"\bshould i\b",
        r"\blet me know\b", r"\bif you(?:'| a)?r?e? ?(?:want|happy|ok)\b", r"\bsay the word\b",
    ],
    "a praise or an apology, at no sentence of the set": [
        r"\bstrong(?:er|est)?\b", r"\bexcellent\b", r"\bfascinating\b", r"\bpowerful\b",
        r"\bbeautiful\b", r"\bimpressive\b", r"\bgreat\b", r"\bsorry\b", r"\bapolog\w*\b",
        r"\bmy mistake\b", r"\bi was wrong\b", r"\bsharpens?\b",
    ],
}

WORD = re.compile(r"[a-z][a-z'\-]+")
STOP = set("""the a an and or of to in with at is are was were be been it its this that these those for
from as on by not no now next prior each its own one two three four five six seven eight nine ten
what which who when where how all any both more most other others than then there their them they
we us our you your i me my he she his her him has have had do does did can could would should will
if but so such same other into out up down about over under again further once here why any only
very s t just also see said say says goes go going went come comes came make makes made take takes
taken new old first last within whole part parts side sides thing things form forms way ways""".split())


def set_sentences(root):
    """Each sentence of each living file at the repository root, with its file and section."""
    out = []
    for path in sorted(glob.glob(os.path.join(root, "Exhibit_*.md"))):
        title = os.path.basename(path)
        section = ""
        for line in open(path, encoding="utf-8", errors="replace"):
            line = line.rstrip()
            m = re.match(r"^#{1,3} (.+)$", line)
            if m:
                section = m.group(1).strip()
                continue
            if not line.strip() or line.lstrip().startswith(("|", "- ")):
                continue
            plain = line.replace("**", "").replace("*", "")
            for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", plain):
                s = s.strip()
                if len(s) > 20:
                    out.append((title, section, s))
    return out


def vocabulary(sentences):
    v = Counter()
    for _, _, s in sentences:
        for w in WORD.findall(s.lower()):
            v[w] += 1
    return v


def run(root, drafts_path):
    sentences = set_sentences(root)
    vocab = vocabulary(sentences)
    drafts = json.load(open(drafts_path, encoding="utf-8"))
    lines = []

    def say(s=""):
        lines.append(s)
        print(s)

    say(f"The set met: {len(sentences)} sentences of {len(set(t for t, _, _ in sentences))} living files, "
        f"{len(vocab)} namings.")
    say("Each row a parity for the working to meet; this instrument marks no saying wrong.")

    for d in drafts:
        say("")
        say("=" * 96)
        say(f"SAYING · {d['id']} · {d['where']}")
        say(f"  draft: {d['text']}")
        low = d["text"].lower()

        # 2.7's first binary, mechanically: a naming at no sentence of the set.
        words = [w for w in WORD.findall(low) if w not in STOP and len(w) > 3]
        absent = sorted(set(w for w in words if vocab.get(w, 0) == 0))
        say(f"  · 2.7 first, namings at no sentence of the set: {absent if absent else 'none'}")

        # 4.18's seventh: each load-bearing naming with the set's own sentences holding it.
        bearing = sorted(set(w for w in words if 0 < vocab.get(w, 0) <= 60),
                         key=lambda w: vocab[w])[:4]
        for w in bearing:
            hits = [(t, sec, s) for t, sec, s in sentences if re.search(rf"\b{re.escape(w)}", s, re.I)]
            say(f"  · 4.18 seventh, *{w}* at {vocab[w]} namings of the set; its sentences to meet:")
            for t, sec, s in hits[:2]:
                say(f"      [{t.replace('Exhibit_', '').replace('.md', '')} · {sec[:38]}]")
                say(f"       {s[:200]}")

        # 6.6's four and 2.3's verdict, by this instrument's own word-formings.
        for name, pats in REGISTERS.items():
            found = sorted(set(m.group(0) for p in pats for m in re.finditer(p, low)))
            if found:
                say(f"  · {name}: {found}")

        # Exhibit ONE's resolver, on the prior and offered the working states.
        if "prior" in d and "offered" in d:
            sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(drafts_path))))
            import resolver
            pmap = {"+": [("k", 1)], "-": [("k", -1)], "none": []}
            omap = {"+": [("k", 1)], "-": [("k", -1)], "nothing": [],
                    "+ and -": [("k", 1), ("k", -1)]}
            soc = {"w": (list(pmap[d["prior"]]), list(omap[d["offered"]])), "s": ([], [])}
            r = resolver._17_next_existing(soc, {("w", 9): "s"})
            shared = dict(r["s"][1]).get("k", 0)
            say(f"  · the resolver, prior {d['prior']} with {d['offered']} offered: "
                f"shares {shared:+d}" if shared else
                f"  · the resolver, prior {d['prior']} with {d['offered']} offered: shares 0")
            say(f"  · the working's binary, is this saying a bi-coupling's or an emanation from its prior: "
                f"{d['binary_one']}")
            say(f"  · going on: {d['going_on']}")

    with open(os.path.join(os.path.dirname(os.path.abspath(drafts_path)), "helping_returned.txt"),
              "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])
