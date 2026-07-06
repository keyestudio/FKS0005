### 4.2.5 Evitar Ladrillos

#### 4.2.5.1 Resumen

![Img](./media/top1.png)

En este proyecto, jugamos un juego de evitar ladrillos donde los jugadores usan un gamepad Micro:bit para mover su indicador LED a izquierda y derecha mientras evaden ladrillos que caen desde arriba. Hay tres estados: a) un icono dinámico al inicio, b) acciones de evasión en tiempo real durante el juego, y c) una puntuación final después de las colisiones.

Los jugadores ganan 1 punto después de cada evasión (cuando el ladrillo llega al fondo), y el juego termina cuando colisionan con un ladrillo; la puntuación final se muestra con un efecto de desplazamiento.

El juego se puede iniciar o reiniciar presionando A+B. Este mecanismo de juego sencillo combina la capacidad de respuesta en tiempo real con la anticipación estratégica.

![Img](./media/bottom1.png)

#### 4.2.5.2 Piezas Requeridas

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Placa micro:bit V2** (suministrada por el usuario) ×1 | **Smart Gamepad micro:bit** (ensamblado) ×1 | **Pila AAA** (suministrada por el usuario) ×4 |

#### 4.2.5.3 Flujo del Código

![Img](./media/5001.png)

#### 4.2.5.4 Código de Prueba

⚠️ **Tenga en cuenta que el umbral inicial 300 en el código se puede modificar según sus necesidades. Cuanto mayor sea el valor, más lento caerá el ladrillo.**

**Código completo:**

![Img](./media/5002.png)

![Img](./media/line1.png)

**Breve explicación:**

① Inicialice las variables relacionadas, incluyendo la columna inicial del jugador, la fila y la velocidad del ladrillo, y establezca la posición del jugador en la columna inicial.

Llame a una función on_start.

![Img](./media/5003.png)

② En cuanto a esta función, hace que el ladrillo aparezca en una columna aleatoria de 0~4 al comienzo del juego.

![Img](./media/5004.png)

③ Determine si “A+B está presionado y el juego no ha comenzado”. Si es así y el inicio está marcado como un estado inicial, marque el estado de inicio primero y confirme nuevamente si los botones aún están presionados después de un breve retraso. De lo contrario, cancele la marca de inicio.

![Img](./media/5005.png)

④ La siguiente función reinicia el juego a su estado inicial. Establece el estado en “jugando” (game_state=1) y coloca al jugador en la posición inicial. Y el ladrillo aparecerá en una columna aleatoria (0~4) y en la fila 0, y las puntuaciones se pondrán a cero. Por último, la pulsación de A/B se marca como no activada, y la matriz se borra.

![Img](./media/5006.png)

⑤ Cuando el estado del juego es **0-estado inicial** (no jugando después de encender), el icono mostrado parpadeará.

![Img](./media/5007.png)

⑥ Cuando está en **2-fin del juego**, la puntuación se controlará según el recuento de parpadeos (flash_count). Si el recuento < 3, repite “mostrar puntuación → breve retraso → borrar pantalla → breve retraso → recuento + 1”; cuando el recuento llega a 3, siempre muestra la puntuación y extiende el retraso.

![Img](./media/5008.png)

⑦ En el estado **1-jugando**, cuando presiona C sin activar la marca de presión y la columna del jugador > 0, la columna del jugador -1 y marca el botón C como activado (con retraso para anti-jitter); presiona E sin activar y cuando la columna del jugador < 4, y la columna +1 con E activado (retraso); si no se realiza ninguna acción, la marca de activación de los botones correspondientes se restablece.

![Img](./media/5009.png)

⑧ Calcule la diferencia entre el tiempo actual y el último tiempo de movimiento del ladrillo. Si esta diferencia excede el umbral de velocidad del ladrillo, actualice el tiempo de movimiento del ladrillo y la fila del ladrillo +1. Si la fila > 4 (alcanzando el límite), reinicie el ladrillo a una columna aleatoria con su fila = cero, y puntuación +1.

Invoque las funciones de detección de colisiones y renderizado de gráficos del juego para dejar caer ladrillos, reiniciar después de alcanzar el límite, acumular puntuación y actualizar el estado del juego en tiempo real.

Invoque las funciones de detección de colisiones y renderizado de gráficos del juego para lograr el avance automático de ladrillos, el reinicio de límites, la acumulación de puntuación y las actualizaciones del estado del juego en tiempo real.

![Img](./media/5010.png)

⑨ Determine si el juego ha terminado: primero comprueba si “la columna del ladrillo coincide con la del jugador” y “si la fila del ladrillo coincide con la del jugador”. Si se cumplen ambas condiciones (es decir, los ladrillos se superponen con el jugador), establezca el juego en estado 2 (fin del juego), borre la pantalla y reinicie el contador de parpadeos.

“Fin del juego al colisionar.”

![Img](./media/5011.png)

⑩ Renderice los elementos visuales del juego: primero borra la pantalla y luego traza puntos con un brillo de 255 (Jugador) en la fila fija del jugador y en las posiciones de la columna actual; si el juego se inicia (game_state=1), traza puntos con un brillo de 85 (ladrillo) en la fila y columna del ladrillo. Así podemos distinguir los ladrillos del jugador según su brillo.

![Img](./media/5012.png)

#### 4.2.5.5 Resultado de la Prueba

![Img](./media/4top.png)

Después de grabar el código, inserte la placa micro:bit en la ranura del gamepad (**pilas instaladas**), y active el interruptor a “ON”.

Está en **0-estado inicial** después de encender y la matriz parpadea dos iconos cuadrados.

Presione A y B (durante al menos 1 segundo) para iniciar el juego (en estado **1-jugando**), y un ladrillo caerá en una columna aleatoria. Ahora puede moverse a izquierda/derecha presionando C/E. Cada vez que evite un ladrillo, puntuación +1.

Fin del juego al colisionar (**2-fin del juego**), y la puntuación final se mostrará en la matriz. Si desea jugar una ronda más, presione A y B nuevamente. Apague para salir del juego (cambie el interruptor DIP a “OFF”).

![Img](./media/5000.gif)

<span style="color: rgb(0, 209, 0);">**Consejo:** Si no hay respuesta en la placa, presione el botón de reinicio en la parte posterior de la placa micro:bit.</span>

![Img](./media/4bottom.png)
