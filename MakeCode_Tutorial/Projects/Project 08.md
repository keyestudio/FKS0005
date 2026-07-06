### 4.2.8 Adivina el Número

#### 4.2.8.1 Resumen

![Img](./media/top1.png)

En este proyecto, jugamos un juego de adivinar números con una placa Micro:bit, una placa de control de gamepad y una pantalla OLED. Cuando se adivina el número correcto, la OLED muestra "¡Genial!"; si la suposición es demasiado alta o demasiado baja, muestra "¡Demasiado alto!" / "¡Demasiado bajo!" respectivamente, junto con el rango correspondiente de números posibles.

![Img](./media/bottom1.png)

#### 4.2.8.2 Conocimiento de Componentes

Este proyecto utiliza la misma pantalla OLED que el Proyecto 07. Consulte la sección 4.2.7.2 para conocer sus componentes.

#### 4.2.8.3 Piezas Requeridas

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Placa micro:bit V2** (suministrada por el usuario) ×1 | **Smart Gamepad micro:bit** (ensamblado) ×1 | **Pila AAA** (suministrada por el usuario) ×4 |
|![Img](./media/OLED.png)|![Img](./media/7008.png)||
| **Pantalla OLED** (suministrada por el usuario) ×1 | **Cable DuPont F-F** (suministrado por el usuario) x4 ||

#### 4.2.8.4 Diagrama de Cableado

![Img](./media/jiexian8.png)

**Después de cablear como se muestra arriba, inserte la micro:bit en la ranura de la placa de control del gamepad.**

| Pantalla OLED | Placa de control del gamepad micro:bit | Pin de la placa micro:bit |
| :--: | :--: | :--: |
| GND | GND | GND |
| VCC | 3V | 3V |
| SDA | SDA | P20 |
| SCL | SCL | P19 |

#### 4.2.8.5 Flujo del Código

![Img](./media/8001.png)

#### 4.2.8.6 Código de Prueba

⚠️ **Tenga en cuenta que aquí se incluye la librería OLED, por lo que necesitamos importar: https://github.com/keyestudio/pxt-environment-kit-master**.

**Código completo:**

![Img](./media/8002.png)

![Img](./media/line1.png)

**Breve explicación:**

① Inicialice el bit de la bandera de actualización de pantalla, establezca la variable de modo en 0 (0-preparación del juego, 1-juego en ejecución) e inicialice la visualización de la pantalla OLED.

![Img](./media/8003.png)

② Durante la preparación del juego, establezca el rango de adivinanza, el valor de adivinanza inicial, el valor objetivo y la adivinanza.

![Img](./media/8004.png)

③ Actualice el rango de valores y el valor de adivinanza en la OLED. Muestre las indicaciones correspondientes cuando cambie el bit de la bandera de estado del resultado: "¡Demasiado alto!" cuando state=1; "¡Demasiado bajo!" cuando state=2; y "¡Genial!" cuando state=3.

Y establezca el modo en preparación del juego y espere 1000 milisegundos (1s).

![Img](./media/8005.png)

④ Presione C y el valor de adivinanza temp+1; si el valor de adivinanza excede el máximo, establézcalo como el nuevo máximo.

Presione E y el valor de adivinanza temp-1; si el valor de adivinanza es menor que el mínimo, establézcalo como el nuevo mínimo.

![Img](./media/8006.png)

⑤ Presione D para comparar el valor de adivinanza con el valor objetivo. Si temp es mayor, registre el nuevo máximo max2 e ingrese al Estado 1; si temp es menor, registre el nuevo mínimo min2 e ingrese al Estado 2; si ambos valores son iguales, vaya al Estado 3.

Finalmente, actualice la pantalla con un retraso de 1000 milisegundos.

![Img](./media/8007.png)

#### 4.2.8.7 Resultado de la Prueba

![Img](./media/4top.png)

Después de grabar el código, inserte la placa micro:bit en la ranura del gamepad (**pilas instaladas**), y active el interruptor a “ON”.

Después de cargar el código, la OLED se inicializa y muestra el rango de valores de “num: 1 ~ 100” y la suposición inicial de 50. Puede presionar C para temp+1 (máx. de 100) o E para temp-1 (mín. de 1) para cambiar su valor de suposición en la OLED.

Presione D para enviar su valor, y temp se comparará con el valor objetivo aleatorio. Si temp>valor, muestre "¡Demasiado alto!" y asigne temp a max2; si temp<valor, muestre "¡Demasiado bajo!" y asígnelo a min2. Si tiene demasiada suerte y temp=valor, verá "¡Genial!" durante 1s.

Después de eso, el juego se reiniciará y se establecerá un nuevo valor objetivo. ¡Juguemos otra ronda!

![Img](./media/8000.gif)

⚠️ **El bloque de construcción en el Resultado de la Prueba no está incluido en este kit de producto.**

<span style="color: rgb(0, 209, 0);">**Consejo:** Si no hay respuesta en la placa, presione el botón de reinicio en la parte posterior de la placa micro:bit.</span>

![Img](./media/4bottom.png)
