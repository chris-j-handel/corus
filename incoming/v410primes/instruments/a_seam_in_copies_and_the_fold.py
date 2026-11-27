# A seam wound as a stem: the next seam is the seam round, by the next opener in turns.
# A rank is the copies of one place of the seam, one copy a turn. A breaking test of five sentences, seam to next seam.
seam, unc = 2, [1]
for r in (3, 5, 7, 11, 13):
    nxt = seam * r
    ranks = {u: [u + t * seam for t in range(r)] for u in unc}
    crossed = {u: [c for c in cs if c % r == 0] for u, cs in ranks.items()}
    one_a_rank = all(len(v) == 1 for v in crossed.values())
    # the opener's crossings in all ranks of the stem, uncrossed or not: one a rank
    all_ranks = all(sum(1 for t in range(r) if (pl + t * seam) % r == 0) == 1 for pl in range(1, seam + 1))
    # the crossed copies of a podal pair of places are a podal pair about the next seam's middle
    podal_crossed = all(crossed[u][0] + crossed[seam - u][0] == nxt for u in unc)
    leaves = sorted(c for cs in ranks.values() for c in cs if c % r)
    fold = all((nxt - n) in set(leaves) for n in leaves)
    # the turn of the opener's crossing in a rank: all turns but the middle turn? the turns met
    turns = sorted((crossed[u][0] - u) // seam + 1 for u in unc)
    mid = (r + 1) // 2
    print(f"opener {r}: stem {seam} round, {r} turns, to {nxt}. ranks of leaves {len(unc)}; one crossing a rank of leaves: {one_a_rank}; one crossing in all {seam} ranks: {all_ranks}; "
          f"crossed copies of a podal pair podal: {podal_crossed}; leaves {len(leaves)} fold about {nxt//2}: {fold}; a crossing of a leaf at the middle turn {mid}: {mid in turns}")
    if r == 5:
        print("   ranks:", ranks, "; crossed:", crossed, "; leaves:", leaves)
    seam, unc = nxt, leaves
