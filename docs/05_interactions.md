# 05 – Interactions and linked views

Specify exactly what selection means and how views respond.

| Interaction | Source view | Selection meaning | Affected views | Expected response |
|---|---|---|---|---|
| Brush | Scatterplot | Records inside brushed region | Map and other charts | Highlight/filter matches |
| Select category | Fuel chart | Records in chosen category | Map, scatterplot, timeline | Update consistently |
| Select region | Map | Plants in selected region | Other views | Update/highlight |
| Select time range | Timeline | Plants commissioned in range | Other views | Update/highlight |

Replace examples with the final design.

## Selection semantics
- Are filters combined with AND, OR, or another rule?
- Does a new selection replace or add to an existing selection?
- Is the behaviour filtering or highlighting?
- How are selections cleared?
- How are missing values and empty results represented?

## Shared interaction state
_TBD: Describe how views share selection/filter state._

## Edge cases
_TBD: Overlapping points, empty selection, missing values, records not shown in a view._
