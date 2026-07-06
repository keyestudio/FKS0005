### 4.2.9 Coche Robot Mecanum 4WD Controlado por Gamepad Micro:bit

#### 4.2.9.1 Resumen

![Img](./media/top1.png)
En este proyecto, controlamos un Coche Robot Mecanum 4WD mediante una placa de control de gamepad y una placa Micro:bit. El joystick permite que el coche avance, retroceda, gire a la izquierda y a la derecha; el botón C mueve el coche lateralmente a la izquierda, el D lateralmente a la derecha, el E acelera y la tecla F desacelera (con un rango de velocidad de 20 a 95). Cuando no se realiza ninguna operación, el coche permanece estacionario.

![Img](./media/bottom1.png)

#### 4.2.9.2 Piezas Requeridas

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Placa micro:bit V2** (suministrada por el usuario) ×1 | **Smart Gamepad micro:bit** (ensamblado) ×1 | **Pila AAA** (suministrada por el usuario) ×4 |
| ![Img](./media/che.png) | ![Img](./media/18650.png) ||
| **Kit KS4034** (suministrado por el usuario) ×1 | **Pila 18650** (suministrada por el usuario) ×2 ||

Para obtener información detallada sobre el Coche Robot Mecanum 4WD**(KS4034)**, visite [aquí](https://docs.keyestudio.com/projects/KS4034/en/latest/).
#### 4.2.9.3 Diagrama de Cableado

Consulte las instrucciones de cableado en la documentación del KS4034 para conectar el Coche Robot Mecanum 4WD y el gamepad mediante comunicación por radio. No se requiere cableado físico entre ambos; ambos dispositivos se comunican de forma inalámbrica.

#### 4.2.9.4 Flujo del Código
⚠️ **Tenga en cuenta que la siguiente librería debe importarse al programar los códigos del coche: https://github.com/keyestudio2019/mecanum_robot_v2**.

**Flujo de código del gamepad:**

![Img](./media/9001.png)

**Flujo de código del coche:**

![Img](./media/9002.png)

#### 4.2.9.5 Código de Prueba

**Código completo del gamepad:**

![Img](./media/9003.png)

![Img](./media/line1.png)

**Breve explicación:**

① Inicialice el grupo de radio en 1 con una fuerza de transmisión de señal de 7; muestre un icono de corazón y establezca las variables SEND_INTERCAL en 100 y BTN_DEBOUNCE_TIME en 20.

![Img](./media/9004.png)

② Establezca la variable currentCmd (variable de contenido de instrucción) en el carácter '0' y asigne los valores de los ejes X e Y del joystick a las variables rockerX y rockerY, respectivamente.

![Img](./media/9005.png)

③ Compruebe si el joystick o el botón tienen una operación correspondiente. Si ocurre una operación, establezca la variable currentCmd (variable de contenido de instrucción) en el carácter correspondiente (R/U/L/D/A/B/Z/X); de lo contrario, déjela sin cambios.

![Img](./media/9006.png)

④ Compruebe si currentCmd (variable de contenido de instrucción) difiere de lastCmd (almacena el contenido de la instrucción anterior). Si es así, envíe currentCmd, establezca lastCmd en currentCmd y espere un retraso especificado.

![Img](./media/9007.png)

**Código completo del coche:**

![Img](./media/9008.png)

![Img](./media/line1.png)

**Breve explicación:**

① Inicialice el grupo de radio en 1 con una fuerza de transmisión de señal de 7; muestre un icono de corazón y establezca las variables SPEED en 50, MIN_SPEED en 20 y MAX_speed en 95.

![Img](./media/9009.png)

② Reciba el valor de comando enviado por la radio y almacene el comando en la variable item.

![Img](./media/9010.png)

③ Basándose en los comandos de caracteres (U/L/D/R/A/B) recibidos por item, llame a las funciones correspondientes para controlar el coche para que avance, retroceda, gire a la izquierda, a la derecha, y se desplace a la izquierda y a la derecha.

![Img](./media/9011.png)

④ Basándose en el comando de carácter (Z/X) recibido por item, el coche se acelera o desacelera en consecuencia.

Durante la aceleración, la velocidad se establece en el mínimo de SPEED+5 y MAX_speed (para evitar exceder MAX_speed); durante la desaceleración, la velocidad se establece en el máximo de SPEED-5 y MIN_speed (para evitar caer por debajo de MIN_speed).

![Img](./media/9012.png)

⑤ Aquí se definen seis funciones de control de movimiento del vehículo:

- car_back controla los cuatro motores para que giren en sentido inverso para retroceder;
- car_forward controla los cuatro motores para que giren hacia adelante para avanzar;
- car_left logra el giro a la izquierda del coche configurando los motores del lado izquierdo hacia atrás y los motores del lado derecho hacia adelante;
- car_right logra el giro a la derecha configurando los motores del lado derecho hacia atrás y los motores del lado izquierdo hacia adelante;
- car_left_move y car_right_move permiten el desplazamiento lateral izquierdo y derecho mediante la rotación coordinada de los motores diagonales.

Todas las funciones toman la variable SPEED como parámetro de velocidad del motor.

![Img](./media/9013.png)

#### 4.2.9.6 Resultado de la Prueba

![Img](./media/4top.png)

Después de grabar el código, inserte la placa micro:bit en la ranura del gamepad (**pilas instaladas**), y active el interruptor a “ON”.

Cargando estos códigos en dos placas Micro:bit del gamepad y del coche respectivamente, y asegúrese de que las baterías tengan suficiente carga. Inserte la Micro:bit correspondiente en el gamepad y el coche y active los interruptores de ambos a "ON".

Ahora puede controlar el coche con el gamepad: empuje el joystick hacia arriba y el coche avanzará, empújelo hacia abajo para retroceder, a la izquierda lo girará a la izquierda y a la derecha lo girará a la derecha. También podemos controlar la aceleración (presione el botón E) / desaceleración (presione el botón F) del coche, el desplazamiento lateral izquierdo (C) y el desplazamiento lateral derecho (D). Tenga en cuenta que el rango de velocidad es de 20 a 95.

![Img](./media/9000.gif)

<span style="color: rgb(0, 209, 0);">**Consejo:** Si no hay respuesta en la placa, presione el botón de reinicio en la parte posterior de la placa micro:bit.</span>

![Img](./media/4bottom.png)
