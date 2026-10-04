# The resolver's cells, for working by hand

Repository /home/claude/corus (branch working/v380L). READ ONLY: do not edit, commit or push anything in the repository. NEVER execute the resolver or any python from the repository, and do not write a simulation of it: the standing direction is that the resolver is followed by hand, cell by cell, and a law is derived by reasoning, each step a consequence of the cells. Tables written by hand (on paper, in your notes) for small cases are the checking. Python may be used only for plain arithmetic on integers you already derived (a gcd, a list of primes), never to step selves through momentaries.

The resolver is the python block at lines 10 to 60 of `Exhibit_ONE_Natural_Resolver_v380R.md`. Read it. For one sharing, its cells are:

- A self carries a parity c, + or −. Its offerings at a momentary are what the selves coupled to it shared or released at the momentary before. An offering of 0 is passed over (surfaces none). Offerings all of one parity surface that parity; + and − together surface 0; none surfaces none.
- If the surfacing is the self's own parity c: a changing that is not. The self shares 0 and carries c on.
- At each other surfacing (the other parity, 0, or none): a changing. The self carries −c next and shares −c (its next parity).
- So what a self shares at a momentary is 0 if it carried on, and its next parity if it inverted.
- 17 gives each self's one changing on to each self it is coupled to: along (9) and across (6, 10), each where coupled; it arrives as that self's offering at the next momentary.
- At the first momentary nothing has been shared yet: none surfaces at each self, and each self inverts.

Structures (Exhibit ONE's tables near lines 610 to 665; read their column heads for the openings):
- A spiral of n selves: each releases along to the next, the last to the first. One offering at each self from its prior self.
- A torus of p along by q across: self (i, j) receives the changing of (i − 1, j) along and of (i, j − 1) across, indices taken round p and round q. Opening: one self carries −, the selves alternate along and across, and with an odd number the last and the first are alike.
- Two spirals crossed: two spirals, and self 1 of each also shares across to self 1 of the other, both ways.

The Co-Chaining Logic Registry is `Exhibit_THIRTY_Co-Chaining_Logic_Registry_v380L.md`; read a step with `grep -n -A2 -E "^(233|243|630|631|646|647|648|649|650|651)\. " <file>`.
