### 4.2.4 Reproductor de Música

#### 4.2.4.1 Resumen

![Img](./media/top1.png)

Aquí construimos un reproductor de música que genera sonido a través del zumbador incorporado en la placa micro:bit (no reproduce música vocal). Cuenta con una biblioteca de 20 pistas cortas y admite la reproducción secuencial y aleatoria.

En el modo secuencial, al presionar el botón C (Canción anterior) o E (Canción siguiente) se cambian las pistas según una secuencia preestablecida hasta llegar al final de la lista; mientras que en el modo aleatorio, cada pulsación selecciona una pista al azar entre los 20 sonidos con las luces de colores parpadeando, y cuando una canción termina, se detiene inmediatamente.

Mientras tanto, la matriz de LED de la micro:bit muestra el modo de reproducción actual en tiempo real.

![Img](./media/bottom1.png)

#### 4.2.4.2 Piezas Requeridas

| ![Img](./media/microbitV2.png)| ![Img](./media/shoubin.png) |![Img](./media/dianchi.png) |
| :--: | :--: | :--: |
| **Placa micro:bit V2** (suministrada por el usuario) ×1 | **Smart Gamepad micro:bit** (ensamblado) ×1 | **Pila AAA** (suministrada por el usuario) ×4 |

#### 4.2.4.3 Flujo del Código

![Img](./media/4001.png)

#### 4.2.4.4 Código de Prueba

**Código completo:**

![Img](./media/4002.png)

![Img](./media/line1.png)

**Breve explicación:**

① Inicialice la matriz de LED y el volumen del sonido, conecte el pin RGB a P8 y establezca el número de RGB en 4.

![Img](./media/4003.png)

② Inicialice el array de melodías a 20 y añada sus pistas detalladas, y establezca su volumen inicial.

![Img](./media/4004.png)

③ Determine si se presiona el botón D o F. Presione D para '0-reproducción secuencial', F para '1-reproducción aleatoria'.

![Img](./media/4005.png)

④ En modo secuencial, presione C para reproducir la canción anterior, E para saltar a la siguiente canción.

![Img](./media/4006.png)

Dado que solo hay 20 pistas en el array, solo se puede reproducir música del N.º 0-19. Por lo tanto, agregamos una condición if para evitar desbordamientos y subdesbordamientos del array.

![Img](./media/4007.png)

Sin embargo, en modo aleatorio, presione C/E para mezclar todas estas 20 canciones.

![Img](./media/4008.png)

⑤ Determine si la canción anterior es inconsistente con la actual. Si es así, detenga la actual primero y luego reproduzca esa.

![Img](./media/4009.png)

⑥ Compruebe si el modo es '0-reproducción secuencial', mostrando '![Img](./media/4010.png)', o '1-reproducción aleatoria', mostrando '![Img](./media/4011.png)', con un retardo de 100ms.

![Img](./media/4012.png)

⑦ Haga que las luces RGB respiren en segundo plano.

![Img](./media/4013.png)

⑧ Presione A para subir el volumen (+10); presione B para bajarlo (-10). El volumen del zumbador de la micro:bit se decide por el voltaje de salida del pin interno conectado. Podemos controlar el volumen convirtiendo valores digitales 0~255 en analógicos a través de DAC.

![Img](./media/4014.png)

#### 4.2.4.5 Resultado de la Prueba

![Img](./media/4top.png)

Después de grabar el código, inserte la placa micro:bit en la ranura del gamepad (**pilas instaladas**), y active el interruptor a “ON”.

Después de encender, está en modo secuencial por defecto, y reproducirá la canción en el N.º “0”. Cuando termine, puede presionar C para la última canción o E para la siguiente.

Presione F para cambiar al modo aleatorio. Y puede presionar D para volver al secuencial. En el modo F, se reproducirá una pista aleatoria de estas 20 si presiona C/E. Después de terminar, se detiene.

Las luces RGB siempre están respirando desde el momento de encender. Mientras tanto, la matriz de LED de la micro:bit muestra “![Img](./media/4010.png)” en modo secuencial y “![Img](./media/4011.png)” en modo aleatorio.

Para el volumen, presione A para subir y B para bajar.

![Img](./media/4015.gif)

<span style="color: rgb(0, 209, 0);">**Consejo:** Si no hay respuesta en la placa, presione el botón de reinicio en la parte posterior de la placa micro:bit.</span>

![Img](./media/4bottom.png)
