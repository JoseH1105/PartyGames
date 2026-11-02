# Brindis: identidad y guía de estilo

Esta guía describe cómo se ve, cómo suena y cómo está hecha Brindis. Cualquier pantalla, juego o carta nueva tiene que respetarla. Los valores salen tal cual de `index.html`; si se cambia uno allá, se actualiza aquí.

---

## 1. Qué es Brindis

- **Producto:** web app (PWA instalable) de juegos para la fiesta y para tomar.
- **Cómo se juega:** un solo celular que pasa de mano en mano. Nada de cuentas, nada de servidor, funciona sin internet después de la primera carga.
- **Público:** grupos de amigos y parejas, hispanohablantes, con guiños a Costa Rica (categoría de palabras ticas en El impostor, Keylor Navas en Famosos).
- **Juegos actuales:** Retos, Kings Cup, Chooser, El impostor y Adivina quién soy.
- **Personalidad:** fiestera, cálida, directa y con humor. Nocturna (fondo oscuro) pero llena de color. Nunca corporativa, nunca infantil.
- **Mensaje fijo:** "Tomen con responsabilidad. Si toman, nadie maneja." aparece en el menú principal y no se quita.

---

## 2. Voz y tono

| Regla | Ejemplo real |
| --- | --- |
| Español neutro latino, tuteo (tú), plural con **ustedes** (nunca vosotros). | "Digan uno por turno." / "Descubran quién es." |
| Frases cortas e imperativas. La instrucción cabe en una línea. | "Responde o bebe", "Cumple o toma" |
| Siempre hay consecuencia en tragos con número. | "…o toma 2 tragos." / "Confiesa o toma 2." |
| Signos de apertura ¿ ¡ siempre. | "¿A qué jugamos?", "¡Adivinó!" |
| Puntos suspensivos con el carácter `…`, no `...`. | "Yo nunca he…" |
| Botones con verbo o acción concreta, sin "OK" ni "Aceptar". | "Empezar", "Repartir palabras", "Seguir jugando", "Barajar de nuevo" |
| Títulos de juego en español salvo nombres ya conocidos. | "Kings Cup", "Chooser" se quedan en inglés |
| Las cartas usan marcadores de jugador `{A}` y `{B}`, que se pintan resaltados. | "{A} y {B}: piedra, papel o tijera. Quien pierda toma 2." |
| Textos de UI en sentence case (solo mayúscula inicial). Las etiquetas pequeñas van en MAYÚSCULAS vía CSS, no escritas así. | `.eyebrow`, `.pill`, `.panel h2` |

Nada de emojis en la interfaz: los íconos son SVG propios.

---

## 3. Paleta de color

### 3.1 Tokens base (`:root` en `index.html`)

La app tiene **un único tema oscuro** (`color-scheme: dark`). No hay modo claro.

| Token | Hex | Uso |
| --- | --- | --- |
| `--bg` | `#15101d` | Fondo de la app, `theme_color` del manifest, fondo del ícono, lienzo del Chooser |
| `--surface` | `#211a2c` | Paneles (`.panel`), hojas modales |
| `--surface-2` | `#2b2239` | Chips, categorías, botones secundarios dentro de paneles |
| `--line` | `#3b3050` | Bordes de 1 px, separadores, estado vacío de barras |
| `--fg` | `#f7f0fb` | Texto principal (blanco lila) |
| `--muted` | `#a998bd` | Texto secundario, placeholders, etiquetas |
| `--accent` | `#ffb347` | **Color de marca** (ámbar cerveza). CTA principal, "dis" de Brindis, foco, coronas, toggles activos |
| `--accent-ink` | `#2a1606` | Texto sobre `--accent` |
| `--danger` | `#ff6b6b` | Acciones destructivas ("Terminar partida") |

Variantes del acento: `#f29a2e` (rayas del dorso de carta), `#c77d12` (borde de corona).

### 3.2 Rosas de apoyo (parejas y selección)

| Hex | Uso |
| --- | --- |
| `#ff5c96` | Corazón activo, chip seleccionado |
| `#ff8fb8` | Etiqueta de pareja, texto de pista rosa |
| `#3a1f35` | Fondo de chip seleccionado |

### 3.3 Colores de juego (tarjetas del menú, `--m`)

| Juego | Hex | Fondo en partida |
| --- | --- | --- |
| Retos | `#d93f7f` | Color de la categoría de la carta |
| Kings Cup | `#3654d6` | `--kbg`, inicia en `#3a2a55`, luego el color de la regla |
| Chooser | `#13987f` | `--bg` |
| El impostor | `#5b3fc4` | `--ibg: #4a33a8`; resultado `#9e1030` |
| Adivina quién soy | `#c96f12` | `--gbg: #c96f12` |

Un juego nuevo necesita un color propio, saturado, de luminosidad media (texto blanco legible encima) y distinto de los cinco anteriores.

### 3.4 Paleta de categorías (fondos de carta a pantalla completa)

Todos llevan texto blanco salvo Graciosos.

| Clave | Nombre | `bg` | `fg` |
| --- | --- | --- | --- |
| `suave` | Rompehielo | `#1d8a78` | `#ffffff` |
| `risas` | Graciosos | `#f2a93b` | `#2b1703` |
| `yonunca` | Yo nunca | `#3654d6` | `#ffffff` |
| `probable` | ¿Quién es más probable? | `#7a4bd8` | `#ffffff` |
| `verdad` | Verdad o trago | `#e2553f` | `#ffffff` |
| `retos` | Retos | `#0f7fb3` | `#ffffff` |
| `temas` | Temas | `#0e8a8a` | `#ffffff` |
| `prefieres` | ¿Qué prefieres? | `#c2611f` | `#ffffff` |
| `confesiones` | Confesiones | `#4b4fae` | `#ffffff` |
| `parejas` | Parejas | `#d93f7f` | `#ffffff` |
| `picante` | Atrevidos +18 | `#9e1030` | `#ffffff` |
| `regla` | Reglas | `#2f9a58` | `#ffffff` |
| (FIN) | Fin de la regla | `#3a3f4a` | `#ffffff` |

Kings Cup reutiliza la misma familia (`#1d8a78`, `#e2553f`, `#c7612a`, `#3654d6`, `#0f7fb3`, `#d93f7f`, `#7a4bd8`, `#2f9a58`, `#b8456b`, `#0e8a8a`, `#6a3fc2`, `#c0306a`, `#9e1030`; cuarto rey `#6e0a20`). Adivina quién soy también (`GQC`). **Para colores nuevos, elegir primero de esta familia** antes de inventar uno.

Regla de intensidad: el rojo vino `#9e1030` significa "lo más fuerte" (+18, rey, impostor descubierto, tiempo agotándose).

### 3.5 Colores vivos (Chooser y acentos de puntos)

`CH_COLORS`: `#ff5c96`, `#ffb347`, `#4fd1c5`, `#7a8bff`, `#b57bff`, `#ff6b4a`, `#5ad16b`, `#ffd93d`, `#3fb6ff`, `#ff8fd8`. Son más claros y neón; solo para elementos pequeños que brillan sobre `--bg` (dedos, puntos, pulsos), no para fondos grandes.

### 3.6 "Papel" (cartas físicas y tarjetas secretas)

| Hex | Uso |
| --- | --- |
| `#fffaf3` | Cara de naipe, tarjeta secreta, borde del dorso |
| `#221a2e` | Tinta sobre papel (palos negros, palabra secreta) |
| `#d6283f` | Palos rojos |
| `#6d5f80` | Etiqueta pequeña sobre papel |
| `#5b3fc4` / `#ece6fb` | Píldora de categoría sobre papel |
| `#ffd9b0` | Piel de las figuras J/Q/K |

### 3.7 Transparencias sobre fondos de color

Sobre pantallas de juego (fondo saturado) no se usan los tokens de superficie; se usa negro o blanco translúcido:

- Botones redondos, píldoras, chips: `rgba(0,0,0,.18)` – `rgba(0,0,0,.28)`
- Burbujas: `rgba(255,255,255,.14)`
- Botón fantasma: borde `rgba(255,255,255,.45)`
- Velo modal: `rgba(10,6,16,.6)` + `backdrop-filter: blur(4–6px)`
- Brillo de pantalla (`::before`): `radial-gradient(120% 70% at 50% 0%, rgba(255,255,255,.16), transparent 60%)` arriba y `radial-gradient(90% 60% at 50% 110%, rgba(0,0,0,.28–.3), transparent 70%)` abajo. Toda pantalla de juego nueva lo lleva.

---

## 4. Tipografía

Se sirven desde la carpeta `fonts/` del propio sitio (subconjunto latino en `.woff2`, licencia SIL OFL), así ningún dato de quien abre la app llega a terceros. El service worker las guarda para uso sin conexión. No vuelvan a enlazar Google Fonts ni otro CDN; si hace falta un carácter fuera del subconjunto latino, descarguen el subconjunto correspondiente a `fonts/`.

| Token | Familia | Pesos | Uso |
| --- | --- | --- | --- |
| `--display` | **Dela Gothic One** (respaldo: Arial Black, Impact) | 400 (única) | Logo, títulos de pantalla, texto de las cartas, nombres de juego, números grandes, botón principal `.go` |
| `--body` | **Figtree** (respaldo: system-ui) | 400, 500, 600, 700, 800 | Todo lo demás |

Reglas:

- La display **siempre con `font-weight:400`** (no tiene negrita; forzarla la deforma).
- Títulos display con `line-height` apretado: `.88`–`1.18`. Usar `text-wrap: balance` en textos centrados.
- Tamaños fluidos con `clamp()`: logo `clamp(3.2rem,16vw,5rem)`, título de pantalla `clamp(2.6rem,12vw,3.6rem)`, nombre grande `clamp(2.3rem,11vw,3.6rem)`.
- El texto de las cartas de Retos se ajusta solo con `fontSizeFor()`; no fijar tamaños a mano.
- Base del cuerpo: 16 px. Secundario `.8rem`–`.95rem`.
- **Etiquetas pequeñas (eyebrow):** Figtree 700–800, `.68rem`–`.82rem`, `text-transform: uppercase`, `letter-spacing: .12em`–`.18em`.
- Números que cambian (contadores, tiempo) con `font-variant-numeric: tabular-nums`.
- Patrón de logo/título: segunda parte de la palabra en `--accent` con `<span>` → "Brin**dis**", "Re**tos**", "El **impostor**", "Adivina quién **soy**".

---

## 5. Forma, espacio y componentes

### Radios
| Elemento | Radio |
| --- | --- |
| Píldoras, chips, toggles | `999px` |
| Tarjetas de juego del menú, modal centrado | `26px` |
| Hoja inferior | `24px 24px 0 0` |
| Paneles, botón `.go` | `18–20px` |
| Categorías, stepper | `16px` |
| Inputs, botones de hoja, segmentado | `14px` |
| Naipes | `7% / 5%` |

### Espaciado
- Margen lateral mínimo 16 px, siempre combinado con el área segura: `max(16px, env(safe-area-inset-left,0px))`.
- Columna de configuración: `max-width: 560px`, centrada, `gap: 22px` entre paneles.
- Dentro del panel: `padding: 18px`, `gap: 14px`.
- Botones táctiles de al menos 44 × 44 px (`.rbtn`).

### Componentes reutilizables (clases existentes, úsenlas antes de crear otras)

| Clase | Qué es |
| --- | --- |
| `.mode` | Tarjeta de juego del menú. Color por `--m`, entrada escalonada por `--d`, ilustración en `.art` |
| `.brand` / `.hero` | Encabezado con título display + vaso SVG |
| `.backlink` | Píldora "‹ Menú" para volver |
| `.panel` + `h2` | Bloque de configuración con etiqueta en mayúsculas y contador `<b>` |
| `.go` | CTA principal ámbar, fuente display, sombra ámbar |
| `.ghost` | Botón secundario transparente con borde blanco (sobre color) |
| `.dock` | Barra inferior fija con degradado y el `.go` |
| `.why` | Mensaje bajo el CTA que explica por qué está deshabilitado |
| `.cat` | Opción seleccionable con color `--c`, check y barra de intensidad `.heat` |
| `.chip` / `.chipsel` | Jugador / categoría seleccionable en forma de píldora |
| `.seg` | Selector segmentado (activo en `--accent`) |
| `.stepper` | − número + |
| `.tog` / `.tog.optrow` | Interruptor; estado en `aria-pressed` |
| `.top` / `.bottom` | Barras de pantalla de juego con `.rbtn` y `.pill` |
| `.sheet` / `.sheet.center` | Hoja inferior de pausa / diálogo de confirmación |
| `.ipview`, `.tapcue` | Vista "pasa el celular y toca" |
| `.secret` | Tarjeta de papel con información privada |

### Iconografía
- SVG en línea, trazo `stroke-width: 2.4–2.6`, `stroke-linecap/linejoin: round`, `currentColor`.
- Palos de baraja como `<symbol>` (`#s-h`, `#s-d`, `#s-s`, `#s-c`) reutilizados con `<use>`.
- **El vaso** (vidrio blanco, líquido `#ffb347`, espuma blanca, burbujas) es el símbolo de la marca: ícono de la app, encabezados y dorso de carta ("B" sobre rayas ámbar).

---

## 6. Movimiento

- Entradas con rebote suave: `cubic-bezier(.2,.9,.25,1.2)` (cartas), `cubic-bezier(.2,.9,.3,1.3)` (pop, modales).
- Duraciones: 0.12–0.2 s para presión/hover, 0.25–0.5 s para entradas, 0.75 s para el reparto de naipes.
- Al presionar: `transform: scale(.97–.98)`.
- Detalles vivos en bucle: burbujas que suben, coronas, puntos que pulsan (`dpulse`), naipes que flotan.
- Cambio de color de fondo entre cartas con `transition: background .35s`.
- Respeta `prefers-reduced-motion`: ya hay una regla global que apaga animaciones; no la quiten.
- Vibración corta con `buzz()` en momentos clave (elección, adivinanza, fin de tiempo).

---

## 7. Patrones de pantalla

1. **Menú (`#home`)**: hero con logo y vaso, "¿A qué jugamos?", grilla de `.mode` (1 columna en celular; desde 760 px, 3 arriba + 2 abajo en una grilla de 6).
2. **Configuración** (`#setup`, `#imp`, `#guess`): `.backlink`, `.brand`, paneles apilados y `.dock` con el CTA.
3. **Juego** (`#game`, `#kings`, `#impplay`, `#guessplay`): pantalla completa del color del juego o la carta, brillo radial, `.top` con volver/píldora/menú, área central que se toca para avanzar, `.bottom` con controles.
4. **Pausa y salida**: hoja inferior "Pausa" y, si se pierde progreso, diálogo centrado "¿Volver al menú?".

Siempre: solo vertical (`orientation: portrait`), áreas seguras respetadas, se pide `requestWake()` para que la pantalla no se apague durante el juego.

---

## 8. Reglas técnicas que afectan el estilo

- Todo vive en `index.html` (CSS en `<style>`, JS en `<script>`), más las fuentes en `fonts/`. No se agregan frameworks, CDNs, analítica ni llamadas a servidores: la app no envía datos fuera del celular.
- Nuevas pantallas: agregar su `id` a `SCREENS` y su lógica de entrada/salida en `go()`.
- Configuración guardada en `localStorage` con prefijo `brindis.` (`brindis.v1`, `brindis.imp`, `brindis.guess`, `brindis.kdesc`), siempre dentro de `try/catch`.
- Cada cambio publicado: subir `CACHE` en `sw.js` (`brindis-v1` → `brindis-v2`…).
- Accesibilidad: `aria-label` en botones de solo ícono, `aria-pressed` en toggles, `aria-live` en zonas que cambian, foco visible con contorno `--accent` de 3 px.

---

## 9. Lista de verificación para una mejora

- [ ] Colores tomados de esta guía (tokens o familia de categorías).
- [ ] Títulos en Dela Gothic One 400, resto en Figtree.
- [ ] Textos en español latino, tuteo, con consecuencia en tragos y signos ¿ ¡.
- [ ] Reutiliza componentes existentes (`.panel`, `.go`, `.seg`, `.tog`, `.sheet`…).
- [ ] Funciona a 375 px de ancho con áreas seguras.
- [ ] Animaciones con las curvas de arriba y apagadas con reduced-motion.
- [ ] `CACHE` subido en `sw.js`.
- [ ] Grafo regenerado (`python tools/build-graph.py`).
