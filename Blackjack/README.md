# Proyecto: Blackjack

Este es un juego simple de Blackjack implementado en Python. El juego comienza preguntando al usuario si desea jugar una partida de Blackjack. Si el usuario responde afirmativamente, se inicia el juego.

## Funcionamiento

1. Al inicio del juego, tanto al usuario como a la computadora se les reparten dos cartas. Las cartas se eligen al azar de un mazo que contiene cartas del 2 al 10 y un 11, que representa al As.

2. Se muestra la primera carta de la computadora y las cartas del usuario junto con su puntuación actual.

3. Si el usuario o la computadora obtienen un Blackjack (un As y una carta de valor 10 en sus dos primeras cartas), el juego termina inmediatamente. Si el usuario obtiene un Blackjack, gana el juego. Si la computadora obtiene un Blackjack, el usuario pierde el juego.

4. Si no hay un Blackjack, el usuario tiene la opción de pedir otra carta ("hit") o pasar ("stand"). El usuario puede seguir pidiendo cartas hasta que decida pasar o hasta que su puntuación supere los 21 puntos, en cuyo caso pierde el juego.

5. Una vez que el usuario decide pasar, es el turno de la computadora. Si la puntuación de la computadora es menor a 17, la computadora seguirá pidiendo cartas hasta que su puntuación sea 17 o más.

6. Finalmente, se comparan las puntuaciones del usuario y de la computadora. Si la puntuación de la computadora es mayor que la del usuario y no supera los 21, el usuario pierde. Si la puntuación de la computadora supera los 21, el usuario gana. Si las puntuaciones son iguales, el juego termina en empate.

## Requisitos

- Python 3 o superior

## Cómo ejecutar

Para ejecutar el juego, usa el siguiente comando:

```sh
python blackjack.py