# The podaling journey and the equilibria clusters

Returned by `scripts/journey.py`. The resolving step is Equilibria Definitions v363 §3.1, F(P, Q) = (−Q, P), from the existing prior (+, −). Arrivals 0 to 9 are prior 0–3, now 4–7 and next 8–9.

## The two journeys

| arrival | spot | sign pair | relation | odd origin | even origin |
|---:|---|---|---|---|---|
| 0 | centre | +- | oppose | bi | co |
| 1 | bottom | ++ | agree | co | bi |
| 2 | upper right | -+ | oppose | bi | co |
| 3 | left | -- | agree | co | bi |
| 4 | lower right | +- | oppose | bi | co |
| 5 | top | ++ | agree | co | bi |
| 6 | lower left | -+ | oppose | bi | co |
| 7 | right | -- | agree | co | bi |
| 8 | upper left | +- | oppose | bi | co |
| 9 | centre | ++ | agree | co | bi |

## Each cluster as a fixed rule

| cluster | the rule at the arrival | odd origin | even origin |
|---|---|---|---|
| 1. State–flow–state equilibria | a state along, a flow across: along carries agreeing signs, across carries opposing signs | lives to 9 | blocked at 1 |
| 2. Flow–state–flow equilibria | a flow along, a state across: along carries opposing signs, across carries agreeing signs | blocked at 1 | lives to 9 |
| 3. All-changing equilibria with an unchanged distinction | both signs change at every arrival while the distinction between them is held | blocked at 1 | blocked at 1 |
| 4. Returning equilibria sufficient for the whole continuing | a station met again carries what it carried before: the return is the whole | blocked at 9 | blocked at 9 |
| 5. Same-form equilibria identified with immediate-next | the next arrival carries the same sign pair as now | blocked at 1 | blocked at 1 |
| 6. Equilibria as a relation conserved through changing | the signs change while their relation, agreeing or opposing, is conserved | blocked at 1 | blocked at 1 |
| 7. Equilibria without required relational changing | one sign is retained while the other changes | blocked at 2 | blocked at 2 |
| 8. Equilibria as unchanged membership during changing | the positive membership is never emptied | blocked at 3 | blocked at 3 |

## Every fixed condition at what one arrival carries

Eight carryings (along or across, four sign pairs), so 256 conditions. Lives through both journeys: 1, the condition admitting all eight, which adds nothing. Lives through the odd journey only: 15. The even only: 15. Neither: 225. Every blocked journey is blocked by arrival 4.

| run length | distinct runs met, odd | even |
|---:|---:|---:|
| 1 | 4 | 4 |
| 2 | 4 | 4 |
| 3 | 4 | 4 |
| 4 | 4 | 4 |
| 5 | 4 | 4 |
| 6 | 4 | 4 |
| 7 | 4 | 4 |
| 8 | 3 | 3 |
| 9 | 2 | 2 |
