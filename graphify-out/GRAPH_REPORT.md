# Graph Report - .graph-src  (2026-11-02)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 109 nodes · 217 edges · 9 communities (8 shown, 1 thin omitted)
- Extraction: 96% EXTRACTED · 4% INFERRED · 0% AMBIGUOUS · INFERRED: 8 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `bfce359d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- index.html.js
- buzz
- chTick
- go
- rnd
- kRender
- show
- esc
- sw.js

## God Nodes (most connected - your core abstractions)
1. `go()` - 11 edges
2. `rnd()` - 9 edges
3. `buzz()` - 8 edges
4. `impStart()` - 8 edges
5. `shuffle()` - 8 edges
6. `gsFinish()` - 7 edges
7. `gsStart()` - 7 edges
8. `kRender()` - 7 edges
9. `chTick()` - 6 edges
10. `impSetupRender()` - 6 edges

## Surprising Connections (you probably didn't know these)
- `chTick()` --calls--> `buzz()`  [EXTRACTED]
  index.html.js → index.html.js  _Bridges community 1 → community 2_
- `impSecret()` --calls--> `buzz()`  [EXTRACTED]
  index.html.js → index.html.js  _Bridges community 1 → community 7_
- `gsNext()` --calls--> `shuffle()`  [EXTRACTED]
  index.html.js → index.html.js  _Bridges community 1 → community 4_
- `gsStart()` --calls--> `go()`  [EXTRACTED]
  index.html.js → index.html.js  _Bridges community 1 → community 3_
- `kDraw()` --calls--> `kRender()`  [EXTRACTED]
  index.html.js → index.html.js  _Bridges community 1 → community 5_

## Import Cycles
- None detected.

## Communities (9 total, 1 thin omitted)

### Community 0 - "index.html.js"
Cohesion: 0.05
Nodes (28): bgObs, CATS, CH, CH_COLORS, cv, cx, FIN, G (+20 more)

### Community 1 - "buzz"
Cohesion: 0.21
Nodes (15): buzz(), fmtTime(), gsAnswer(), gsBegin(), gsCountdown(), gsFinish(), gsFS(), gsNext() (+7 more)

### Community 2 - "chTick"
Cohesion: 0.22
Nodes (11): chDraw(), chHint(), chLift(), chReset(), chResize(), chStart(), chStop(), chTick() (+3 more)

### Community 3 - "go"
Cohesion: 0.31
Nodes (10): go(), gsRender(), impCount(), impMaxImps(), impPickWord(), impSetupRender(), impStart(), impUsingNames() (+2 more)

### Community 4 - "rnd"
Cohesion: 0.29
Nodes (10): buildDeck(), chColor(), draw(), fill(), key(), nextCard(), pickCouple(), pickPlayer() (+2 more)

### Community 5 - "kRender"
Cohesion: 0.29
Nodes (8): cardFace(), faceSvg(), kEnter(), kNew(), kRender(), kSetDesc(), makeBubbles(), renderCrowns()

### Community 6 - "show"
Cohesion: 0.50
Nodes (5): advance(), fontSizeFor(), goBack(), show(), startGame()

### Community 7 - "esc"
Cohesion: 0.20
Nodes (11): couples(), esc(), heart(), impCover(), impHide(), impSecret(), impTalk(), ipShow() (+3 more)

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `go()` connect `go` to `index.html.js`, `buzz`, `chTick`, `kRender`, `show`?**
  _High betweenness centrality (0.004) - this node is a cross-community bridge._
- **Should `index.html.js` be split into smaller, more focused modules?**
  _Cohesion score 0.05405405405405406 - nodes in this community are weakly interconnected._
- **Why does `rnd()` connect `rnd` to `index.html.js`, `chTick`, `go`, `esc`?**
  _High betweenness centrality (0.002) - this node is a cross-community bridge._
- **Why does `shuffle()` connect `rnd` to `index.html.js`, `buzz`, `go`, `kRender`?**
  _High betweenness centrality (0.002) - this node is a cross-community bridge._