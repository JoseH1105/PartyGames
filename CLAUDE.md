# Brindis (PartyGames)

Web app de juegos para la fiesta. Toda la app está en `index.html` (HTML + CSS + JS); `sw.js` es el service worker. Sin build ni dependencias.

## Antes de cambiar algo

1. **Lee el grafo** para ubicar el código y medir el impacto:
   - `graphify-out/GRAPH_REPORT.md`: resumen, nodos centrales y comunidades.
   - Consultas: `python -m graphify query "pregunta" --graph graphify-out/graph.json`,
     `python -m graphify affected "go()" --graph graphify-out/graph.json`,
     `python -m graphify explain "kRender()" --graph graphify-out/graph.json`.
   - El grafo se arma sobre `.graph-src/index.html.js`, una copia del JS con los **mismos números de línea que `index.html`**.
2. **Sigue `docs/IDENTIDAD.md`** para colores, tipografía, tono y componentes.

## Después de cambiar código

```bash
python tools/build-graph.py
```

(Usa `--full` para reconstruirlo desde cero). Requiere `pip install graphifyy`.
Si publicas, sube `CACHE` en `sw.js`.

## Mapa del código (comunidades del grafo)

| Sección en `index.html` | Líneas aprox. | Comunidad | Contenido |
| --- | --- | --- | --- |
| CONTENT | 662–1360 | 0 | Datos: `CATS`, `POOL`, `MORE`, `SUBS`, `PRESETS` (cartas de Retos) |
| STATE | 1361–1384 | 0 | `players`, `selected`, `save()`/`load()` |
| SETUP UI | 1385–1480 | 8 | `renderPlayers()`, `renderCats()`, parejas, `validate()` |
| DECK & PICKING | 1481–1561 | 4 | `buildDeck()`, `nextCard()`, `pickPlayer()`, `shuffle()`, `rnd()` |
| GAME UI | 1562–1649 | 6 | `show()`, `advance()`, `goBack()`, `fontSizeFor()`, `makeBubbles()`, `buzz()` |
| NAVIGATION | 1650–1665 | 3 | `SCREENS`, `go()` (nodo central) |
| KINGS CUP | 1666–1790 | 5 | `KR`, `cardFace()`, `faceSvg()`, `kDraw()`, `kRender()` |
| CHOOSER | 1791–1914 | 2 | Canvas multitouch: `chStart()`, `chTick()`, `chDraw()` |
| EL IMPOSTOR | 1915–2028 | 3, 7 | `IW` (palabras), `IMP`, `impStart()`, `impSecret()` |
| ADIVINA QUIÉN SOY | 2029–2141 | 1 | `GQ`, `G`, `gsStart()`, `gsTick()`, `gsFinish()` |
| sw.js | — | 9 | Caché offline |

Los números de comunidad pueden cambiar al regenerar el grafo; las secciones de `index.html` (`/* ===== X ===== */`) son la referencia estable.
