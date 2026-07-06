### 4.2.7 Medidor de Temperatura y Humedad

#### 4.2.7.1 Resumen

![Img](./media/top1.png)

En este proyecto, construimos un sistema de monitoreo de temperatura y humedad con una placa Micro:bit, un gamepad, un sensor de temperatura y humedad XHT11 y una pantalla OLED. El sensor XHT11 mide la temperatura y humedad ambiente, mientras que la pantalla OLED actualiza las lecturas en tiempo real. La placa controladora del gamepad facilita la expansión del circuito y las conexiones estables, permitiendo que el sistema funcione como un termómetro simple.

![Img](./media/bottom1.png)

#### 4.2.7.2 Conocimiento de Componentes

![Img](./media/2top.png)

**Sensor de temperatura y humedad XHT11**

![Img](./media/XHT11.png)

El sensor de temperatura y humedad XHT11 emite señales digitales y emplea una adquisición y conversión de señal analógica especializada, técnicas avanzadas de detección de temperatura y humedad para garantizar una excelente estabilidad a largo plazo y alta fiabilidad.

Incorpora sensores resistivos de humedad y termistores de temperatura de alta precisión, integrados con un microcontrolador de 8 bits de alto rendimiento.

**Modo de comunicación XHT11:**

Emplea una comunicación simplificada de un solo bus. El bus único consta de una sola línea de datos, a través de la cual se realizan todos los intercambios de datos y operaciones de control dentro del sistema.

- Bit de datos de transmisión de un solo bus:

  - Formato de datos de un solo bus: Transmite 40 bits de datos a la vez, el bit más alto primero.

  - 8 bits de datos de humedad enteros + 8 bits de datos de humedad decimales + 8 bits de datos de temperatura enteros + 8 bits de datos de temperatura decimales + 8 bits de paridad.

    **Nota: La parte decimal de la humedad es 0**.

- Bit de paridad:
  
  - 8 bits de datos de humedad enteros + 8 bits de datos de humedad decimales + 8 bits de datos de temperatura enteros + 8 bits de datos de temperatura decimales
  
    El bit de paridad de 8 bits es los últimos 8 bits del resultado.

![Img](./media/7001.png)

Diagrama de secuencia de datos del sensor de temperatura y humedad XH11:

Después de que el host de usuario (MCU) envía una señal de inicio, el XHT11 cambia del modo de bajo consumo al modo de alta velocidad, y después de que esta señal finaliza, el XHT11 envía una señal de respuesta y 40 bits de datos, y activa una adquisición de señal.

La señal se envía como se muestra en la figura:

![Img](./media/7002.png)

⚠️ **Consejo:** Los datos de temperatura y humedad leídos por el host del sensor XHT11 son siempre los valores de la medición anterior. Si hay un intervalo largo entre dos mediciones, realice dos lecturas consecutivas; el valor de la segunda vez será el real.

**Diagrama esquemático:**

![Img](./media/cou73-2.png)

**Parámetros:**

- Voltaje de funcionamiento: DC 3V~5V
- Corriente de funcionamiento: (Máx.) 2.5mA
- Potencia máxima: 0.0125W
- Rango de temperatura: -25 ~ +60°C (±2℃)
- Rango de humedad: 5 ~ 95%RH (Precisión alrededor de 25C° es ±5%RH)
- Señal de salida: bus único bidireccional digital

**Pantalla OLED**

![Img](./media/A636.png)

OLED ofrece ventajas excepcionales como una rica reproducción de color, alto contraste y amplios ángulos de visión. Las imágenes en ella son claras y vívidas, con un negro particularmente sobresaliente. Cada píxel es autoemisivo sin necesidad de retroiluminación, lo que resulta en un consumo de energía relativamente bajo. La pantalla OLED de 0.9 pulgadas, con su tamaño compacto, alta resolución (128×64 píxeles) y bajo consumo de energía, es ideal para aplicaciones en sistemas embebidos y dispositivos portátiles.

⚠️ **Nota**: Para esta pantalla OLED, la interfaz SDA está conectada al pin P20 de la placa Micro:bit, mientras que la SCL está conectada al pin P19.

**Parámetros:**

- Voltaje de funcionamiento: DC 3V - 5V
- Corriente de funcionamiento: 30mA
- Interfaz: Pin con una separación de 2.54mm
- Modo de comunicación: comunicación I2C
- Chip de controlador interno: SSD1306
- Resolución: 128×64
- Ángulo de visión: Mayor de 150°

#### 4.2.7.3 Piezas Requeridas

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Placa micro:bit V2** (suministrada por el usuario) ×1 | **Smart Gamepad micro:bit** (ensamblado) ×1 | **Pila AAA** (suministrada por el usuario) ×4 |
|![Img](./media/XHT11.png)|![Img](./media/OLED.png)|![Img](./media/7008.png)|
|**Sensor de temperatura y humedad XHT11** (suministrado por el usuario)×1|**Pantalla OLED** (suministrada por el usuario)×1 |**Cable DuPont F-F**(suministrado por el usuario) x7|


#### 4.2.7.4 Diagrama de Cableado

![Img](./media/jiexian.png)

**Después de cablear como se muestra arriba, inserte la micro:bit en la ranura de la placa de control del gamepad.**

| Pantalla OLED | Placa de control del gamepad micro:bit | Pin de la placa micro:bit |
| :--: | :--: | :--: |
| GND | GND | GND |
| VCC | 3V | 3V |
| SDA | SDA | P20 |
| SCL | SCL | P19 |

| Sensor de temperatura y humedad XHT11 | Placa de control del gamepad micro:bit | Pin de la placa micro:bit |
| :--: | :--: | :--: |
| G | GND | GND |
| V | 3V | 3V |
| S | 12 | P12 |


#### 4.2.7.5 Flujo del Código

![Img](./media/7003.png)

#### 4.2.7.6 Código de Prueba
⚠️ **Tenga en cuenta que aquí se incluyen las librerías OLED y DHT11, por lo que necesitamos importar: https://github.com/keyestudio/pxt-environment-kit-master**.

**Código completo:**

![Img](./media/7004.png)

![Img](./media/line1.png)

**Breve explicación:**

① Inicialice los píxeles de la OLED y bórrelos, establezca la matriz de LED de 5×5 para que muestre ![Img](./media/1006.png), y defina los valores de temperatura y humedad en 0.

![Img](./media/7005.png)

② Asigne las lecturas correspondientes del sensor XHT11 a las variables de temperatura y humedad.

![Img](./media/7006.png)

③ La OLED muestra las lecturas del sensor XHT11.

![Img](./media/7007.png)

④ Retraso de 500ms (0.5s).

![Img](./media/cou28.png)

#### 4.2.7.7 Resultado de la Prueba

![Img](./media/4top.png)

Después de grabar el código, inserte la placa micro:bit en la ranura del gamepad (**pilas instaladas**), y active el interruptor a “ON”.

Después de cargar el código en la placa micro:bit, la OLED muestra la temperatura y humedad leídas por el sensor XHT11 en tiempo real.

![Img](./media/7000.gif)

<span style="color: rgb(0, 209, 0);">**Consejo:** Si no hay respuesta en la placa, presione el botón de reinicio en la parte posterior de la placa micro:bit.</span>

![Img](./media/4bottom.png)
