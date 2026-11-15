"""v402mgr: the health of Natural Intelligence's gathering file, its first part, the head. Each droplet read whole.
A droplet of an other living file goes to that file's gathering file. A repetition dissolves into the droplet having its value.
No droplet's words leave the set: each is in a gathering file after it, checked here."""
import sys, re
R = sys.argv[1]; GV = R + '/gathering-value/'
def rd(t): return open(GV + t + '.md', encoding='utf-8').read()
ni = rd('Natural_Intelligence').split('\n')
a = next(i for i, l in enumerate(ni) if l.startswith('## Head, the whole file'))
z = next(i for i, l in enumerate(ni) if l.startswith('## Opening'))
idx = [i for i in range(a + 1, z) if ni[i].startswith('- ')]
assert len(idx) == 42, len(idx)
D = {n + 1: ni[i] for n, i in enumerate(idx)}
assert D[2].startswith('- **An explaining** · The plan for this file') and D[42].startswith('- **An explaining** · Is-or-is-not is the one')
body = lambda d: d.split(' · ', 1)[1]
# 6 has 8 in it now; 9 is a repetition of 6. 13 has 11 in it now.
D6 = D[6] + ' ' + body(D[8])
assert 'goes on into Exhibit ONE and out of it unchanged' in D[6]            # what 9 repeats
last11 = "Each sentence of Natural Intelligence's own with a parity of the code, a 0 provided, or + and − as two changing directions is read beside these three, with its next improving."
assert last11 in D[11] and 'The code has nothing about parity' in D[13] and 'The 0 is not provided' in D[13] and '+ is the all-parity direction' in D[13]
D13 = D[13] + ' ' + last11
concern = ("- **Possible incohering** · Inhaling, exhaling, ingesting and exhausting, each by which of the seventeen names: a concern by its two sides, resolved by neither yet. "
           "One side, this part's two droplets before this one: co-possibling is a between's inhaling and possibling its exhaling; ingesting is with 17-next-existing, and exhausting with 9-next-co-discovering. "
           "Other side, the sentences of 13 November in this file's last part: 2-now-possibling is inhaling, 7-now-observing exhaling, 6-now-co-possibling ingesting and 3-now-co-observing exhausting.")
keep = [D[1], D[3], D[4], D[5], D6, D[7], D[10], D[12], D13, D[14], D[15], concern, D[42]]
to_method = [D[2]]
to_resolver = [D[n] for n in range(16, 42)]
ni[a + 1:z] = [''] + keep + ['']
open(GV + 'Natural_Intelligence.md', 'w', encoding='utf-8').write('\n'.join(ni))
lead = "- **An explaining** · The droplets after this one, to the next droplet of this kind or to this part's end, are from the head of Natural Intelligence's gathering file, placed here by the managing session v402mgr, 15 November, each as it was: "
gm = rd('Geodesic_Improving_Method').rstrip('\n') + '\n' + lead + "a plan of a session, a value of the method and of no sentence of Natural Intelligence.\n" + '\n'.join(to_method) + '\n'
open(GV + 'Geodesic_Improving_Method.md', 'w', encoding='utf-8').write(gm)
nr = rd('Natural_Resolver').rstrip('\n') + '\n' + lead + "each is of a form of Exhibit ONE Natural Resolver, a table, a spiral, a torus or its names, written inside Natural Intelligence.\n" + '\n'.join(to_resolver) + '\n'
open(GV + 'Natural_Resolver.md', 'w', encoding='utf-8').write(nr)
# no words leave the set
after = {'Natural_Intelligence': '\n'.join(ni), 'Geodesic_Improving_Method': gm, 'Natural_Resolver': nr}
lost = []
for n in range(1, 43):
    t = body(D[n])
    where = [k for k, v in after.items() if t in v]
    if not where:
        if n == 9: where = ['a repetition of the sixth droplet']
        elif n == 11: where = ['in the thirteenth droplet'] if all(x in D13 for x in ('The code has nothing about parity', 'The 0 is not provided', '+ is the all-parity direction', last11)) else []
    if not where: lost.append(n)
print('the head: 42 droplets before,', len(keep), 'after · to Exhibit ONE Natural Resolver', len(to_resolver), '· to the Geodesic Improving Method', len(to_method), '· dissolved into the droplet having its value: 3 · a concern added: 1')
print('a droplet with its words in no gathering file after it:', lost if lost else 'none')
