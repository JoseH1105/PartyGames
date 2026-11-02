# Brindis

Juegos para la fiesta en una sola página web:

- **Retos**: verdad o trago, yo nunca, ¿qué prefieres?, confesiones, temas, retos para parejas y más (más de 600 cartas).
- **Kings Cup**: baraja de 52 cartas con la regla de cada una.
- **Chooser**: todos ponen un dedo y la app escoge a alguien.
- **El impostor**: todos tienen la misma palabra menos uno.
- **Adivina quién soy**: un personaje en la frente y los demás dan pistas.

## Jugar

https://joseh1105.github.io/PartyGames/

En el celular, abre el enlace y usa **Agregar a pantalla de inicio** (Safari) o **Instalar app** (Chrome). Después funciona sin conexión.

## Archivos

- `index.html`: toda la app (HTML, CSS y JS).
- `manifest.webmanifest` e `icons/`: para instalarla como app.
- `sw.js`: guarda la app para usarla sin internet.

Si cambias `index.html` y quieres que los teléfonos que ya la instalaron la actualicen, sube también el número de `CACHE` en `sw.js` (por ejemplo `brindis-v2`).
