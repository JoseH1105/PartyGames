# Graph Report - .graph-src  (2026-11-02)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 106 nodes · 214 edges · 10 communities (9 shown, 1 thin omitted)
- Extraction: 97% EXTRACTED · 3% INFERRED · 0% AMBIGUOUS · INFERRED: 7 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1db6c9aa`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- Community 0
- Community 1
- Community 2
- Community 3
- Community 4
- Community 5
- Community 6
- Community 7
- Community 8
- Community 9

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

## Communities (10 total, 1 thin omitted)

### Community 0 - "Community 0"
Cohesion: 0.06
Nodes (26): CATS, CH, CH_COLORS, cv, cx, FIN, G, GQ (+18 more)

### Community 1 - "Community 1"
Cohesion: 0.21
Nodes (15): buzz(), fmtTime(), gsAnswer(), gsBegin(), gsCountdown(), gsFinish(), gsFS(), gsNext() (+7 more)

### Community 2 - "Community 2"
Cohesion: 0.22
Nodes (11): chDraw(), chHint(), chLift(), chReset(), chResize(), chStart(), chStop(), chTick() (+3 more)

### Community 3 - "Community 3"
Cohesion: 0.31
Nodes (10): go(), gsRender(), impCount(), impMaxImps(), impPickWord(), impSetupRender(), impStart(), impUsingNames() (+2 more)

### Community 4 - "Community 4"
Cohesion: 0.33
Nodes (9): chColor(), draw(), fill(), key(), nextCard(), pickCouple(), pickPlayer(), rnd() (+1 more)

### Community 5 - "Community 5"
Cohesion: 0.29
Nodes (8): cardFace(), faceSvg(), kEnter(), kNew(), kRender(), kSetDesc(), makeBubbles(), renderCrowns()

### Community 6 - "Community 6"
Cohesion: 0.40
Nodes (6): advance(), buildDeck(), fontSizeFor(), goBack(), show(), startGame()

### Community 7 - "Community 7"
Cohesion: 0.40
Nodes (6): esc(), impCover(), impHide(), impSecret(), impTalk(), ipShow()

### Community 8 - "Community 8"
Cohesion: 0.40
Nodes (5): couples(), heart(), renderCats(), renderPlayers(), validate()

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `go()` connect `Community 3` to `Community 0`, `Community 1`, `Community 2`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.004) - this node is a cross-community bridge._
- **Should `Community 0` be split into smaller, more focused modules?**
  _Cohesion score 0.058823529411764705 - nodes in this community are weakly interconnected._
- **Why does `rnd()` connect `Community 4` to `Community 0`, `Community 2`, `Community 3`, `Community 7`?**
  _High betweenness centrality (0.002) - this node is a cross-community bridge._
- **Why does `shuffle()` connect `Community 4` to `Community 0`, `Community 1`, `Community 3`, `Community 5`, `Community 6`?**
  _High betweenness centrality (0.002) - this node is a cross-community bridge._