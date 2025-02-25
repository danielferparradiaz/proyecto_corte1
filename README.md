# Black Jack en Python

## Descripción
Este proyecto implementa una versión en Python del juego de Black Jack utilizando un mazo estándar de 52 cartas. La aplicación sigue las reglas clásicas del juego, con algunas modificaciones específicas para esta implementación.

## Reglas del Juego
- Al inicio del juego, las cartas se revuelven y se reparten entre dos jugadores.
- Se escoge aleatoriamente cuál de los dos jugadores hará el primer movimiento.
- En su turno, cada jugador puede elegir entre tomar una nueva carta o plantarse.
- Cada jugador comienza con 50 créditos y en cada partida solo puede apostar hasta 10 créditos.
- El jugador que logre acumular 100 créditos será el ganador.

## Requisitos
Para ejecutar este proyecto necesitas tener instalado:
- Python 3.x

## Instalación
1. Clona este repositorio en tu máquina local:
   ```sh
   git clone https://github.com/danielferparradiaz/proyecto_corte1.git
   ```
2. Accede al directorio del proyecto:
   ```sh
   cd proyecto_corte1
   ```
3. Ejecuta el script principal para jugar:
   ```sh
   python black_jack_game_RESOLVE.py 
   ```

## Funcionamiento
- El programa inicia automáticamente repartiendo cartas y seleccionando un jugador al azar para empezar.
- Durante el turno de un jugador, este puede pedir una nueva carta o plantarse.
- Si un jugador supera los 21 puntos, pierde la ronda y pierde los créditos apostados.
- El juego continúa hasta que un jugador alcance los 100 créditos.

## Personalización
Puedes modificar el código para:
- Ajustar la cantidad de créditos iniciales y la apuesta máxima.
- Implementar una interfaz gráfica para mejorar la experiencia del usuario.
- Agregar más jugadores o modos de juego.

## Contribución
Si deseas mejorar el proyecto, puedes hacer un fork del repositorio y enviar un pull request con tus cambios.

## Autor
Desarrollado por [Daniel Parra, Gabriela, Juan Pablo y Santiago]

