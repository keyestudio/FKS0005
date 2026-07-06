### 4.2.1 Indicador de Dirección

#### 4.2.1.1 Resumen

![Img](./media/top1.png)

Al mover el joystick, la matriz de puntos muestra flechas en la dirección correspondiente en tiempo real: izquierda, derecha, arriba, abajo, lo que le proporciona una clara referencia de dirección.

![Img](./media/bottom1.png)

#### 4.2.1.2 Conocimiento de Componentes

![Img](./media/2top.png)

**Matriz de puntos de Micro:bit:**

![Img](./media/1001.png)

La matriz de puntos LED de la placa micro:bit consta de un total de 25 diodos emisores de luz, un grupo de 5, correspondientes a los ejes X e Y, formando una matriz de 5×5. Cada uno se coloca en la intersección de la fila (X) y la columna (Y). Podemos controlar uno o algunos de ellos estableciendo los puntos de coordenadas.

**Joystick:**

| ![Img](./media/1002.png)| ![Img](./media/1003.png) |
| :--: | :--: |
| Producto real | Diagrama esquemático |

La estructura interna de este joystick está compuesta por dos resistencias ajustables (potenciómetros) con un valor de resistencia de 10KΩ cada una.

Detecta las direcciones (y la amplitud) del empuje a través del pin analógico ADC del microcontrolador para emitir las señales eléctricas analógicas de la dimensión correspondiente. Durante la lectura real de la señal, cuando los valores analógicos de los ejes X e Y del joystick se detectan dentro del rango de 450~600, se puede determinar que el joystick está en un estado neutro (estacionario) sin movimiento activo.

![Img](./media/2bottom.png)

#### 4.2.1.3 Piezas Requeridas

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png)|
| :--: | :--: | :--: |
| **Placa micro:bit V2** (suministrada por el usuario) ×1 | **Smart Gamepad micro:bit** (ensamblado) ×1 |**Pila AAA** (suministrada por el usuario) ×4 |


#### 4.2.1.4 Flujo del Código

![Img](./media/1008.png)

#### 4.2.1.5 Código de Prueba

⚠️ **Tenga en cuenta que los siguientes códigos incluyen las librerías Makecode del Gamepad (la forma de añadir librerías se mencionó anteriormente). La sensibilidad del joystick se puede ajustar según sus necesidades.**

**Código completo:**

![Img](./media/1004.png)


![Img](./media/line1.png)

**Breve explicación:**

① Inicialice la matriz LED para que muestre ![Img](./media/1006.png).


![Img](./media/1005.png)


② Lea los valores de los ejes X e Y para determinar la dirección del movimiento. Si se detecta, la matriz muestra la flecha correspondiente. Si no, muestra ![Img](./media/1006.png).

![Img](./media/1007.png)


#### 4.2.1.6 Resultado de la Prueba

![Img](./media/4top.png)

Después de grabar el código, inserte la placa micro:bit en la ranura del gamepad (**pilas instaladas**), y active el interruptor a “ON”.

Cuando mueva el joystick del gamepad, podrá ver las flechas correspondientes en la matriz. Si suelta el dedo para que vuelva al centro, aparecerá un icono de casa en la matriz.

![Img](./media/1009.gif)

<span style="color: rgb(0, 209, 0);">**Consejo:** Si no hay respuesta en la placa, presione el botón de reinicio en la parte posterior de la placa micro:bit.</span>

![Img](./media/4bottom.png)
