## 4.1.1 Acerca de MakeCode

⚠️ **Los siguientes pasos se realizan en el sistema operativo Windows. Si utiliza otro sistema operativo, puede tomarlos como referencia. Aquí se demuestran en Google Chrome / Microsoft Edge.**

**Entorno de Programación MakeCode:**

Abra la [versión en línea del editor MakeCode](https://makecode.microbit.org/#editor).

Interfaz principal de MakeCode:

![Img](./media/A637.png)

Hay bloques “**on start**” y “**forever**” en el área de edición de código. Cuando se conecta la alimentación o se reinicia, “on start” significa que el código en el bloque solo se ejecuta una vez, mientras que “forever” implica que el código se ejecuta cíclicamente.

Haga clic en “**JS JavaScript**” para ver el código JavaScript:

![Img](./media/A754.png)

O haga clic en “**Python**” para cambiar al código Python:

![Img](./media/A814.png)

**Configuración de idioma:**

![Img](./media/Animation-3.gif)

Pasos:

Paso 1: Haga clic en el botón de configuración ![Img](./media/A806.png).

![Img](./media/A301.png)

Paso 2: Haga clic en “Language”.

![Img](./media/A302.png)

Paso 3: Seleccione el idioma que desee. Aquí lo configuramos en “English”.

![Img](./media/A303.png)

## 4.1.2 Librería de Extensiones Makecode

### 4.1.2.1 Añadir Librería

⚠️ **Proporcionamos archivos de código (.hex) para cada proyecto, por lo que puede cargarlos directamente en el editor MakeCode. O si lo desea, también puede construir bloques de código usted mismo. Tenga en cuenta que se requieren librerías al construirlos manualmente.**

⚠️ **<span style="color: rgb(255, 76, 65);">Nota:</span>** Copie y pegue el enlace en el cuadro de búsqueda: `https://github.com/keyestudio2019/pxt-creative-inventors-kit-master.git`.

![Img](./media/Animation-4.gif)

Pasos:

1\. Haga clic en ![Img](./media/A806.png) para seleccionar “**Extensions**”.

![Img](./media/A842.png)

O haga clic en “**Extensions**” encima de los bloques **Advanced**.

![Img](./media/A900.png)

2\. Busque palabras clave o pegue el enlace de GitHub.

![Img](./media/A909.png)

3\. Aquí introducimos la URL: `https://github.com/keyestudio2019/KEYES-Smart-Gamepad-master.git` en el cuadro de búsqueda y hacemos clic en ![Img](./media/A3257.png), y cargamos la extensión de “**Smart-Gamepad**”.

![Img](./media/A306.png)

4\. Cargando:

![Img](./media/A3316.png)

5\. Cargado:

![Img](./media/A335.png)

### 4.1.2.2 Actualizar/Eliminar Librería

⚠️ **Generalmente, no es necesario eliminar librerías, a menos que no sean requeridas.**

![Img](./media/Animation-4.gif)

Pasos:

1\. Haga clic en “**JavaScript**” para cambiar a códigos de texto.

![Img](./media/A724.png)

2\. Haga clic en “**Explorer**”.

![Img](./media/A749.png)

3\. Busque el “**Smart-Gamepad**” y haga clic en el icono de la papelera ![Img](./media/A813.png) para eliminarlo.

![Img](./media/A824.png)

4\. “**Remove it**”.

![Img](./media/A727.png)

## 4.1.3 Programa MakeCode

### 4.1.3.1 Importar Programa en MakeCode

Tomamos el proyecto “**heartbeat**” como ejemplo.

![Img](./media/Animation-2.gif)

Pasos:

1\. Conecte la placa micro:bit a su ordenador mediante un cable micro USB.

![Img](./media/A800.png)

Cuando la micro:bit se enciende, el indicador LED rojo en su parte posterior se iluminará.

En la placa micro:bit, hay un indicador LED amarillo que parpadeará cuando la placa se comunique con su ordenador a través de micro USB.

Abra Finder (Mac) / Dispositivos y unidades (Windows), y podrá ver una unidad USB llamada "MICROBIT". ¡Pero tenga en cuenta que no es un disco común!

![Img](./media/A849.png)

2\. Haga clic en “**Import**”:

![Img](./media/A956.png)

3\. Y seleccione “**Import File...**”.

![Img](./media/A042.png)

4\. “**Choose File**” para abrir el archivo que necesita.

![Img](./media/A06.png)

5\. Aquí elegimos “**heartbeat.hex**”.

![Img](./media/A28.png)

6\. “**Go ahead √**”.

![Img](./media/A149.png)

O puede arrastrar directamente el archivo hex a la interfaz principal de Makecode:

![Img](./media/A202.png)

7\. Importado:

![Img](./media/A217.png)

### 4.1.3.2 Descargar Código (WebUSB)

Para navegadores como **Google Chrome/Microsoft Edge**, su WebUSB permite el acceso directo al dispositivo de hardware micro USB a través de una página web en línea. Haga clic en “Connect Device” para emparejar el dispositivo. Después de eso, haga clic en “**Download**” para cargar el código en la placa micro:bit.

![Img](./media/Animation.gif)

Pasos:

#### 4.1.3.2.1 Emparejar dispositivo

1\. Conecte la placa micro:bit a su ordenador mediante un cable micro USB.

![Img](./media/A951.png)

2\. Haga clic en los tres puntos “**...**” detrás de “**Download**” y seleccione “**Connect device**”.

![Img](./media/A028.png)

3\. “**Next**”.

![Img](./media/A046.png)

4\. “**Pair**”.

![Img](./media/A104.png)

5\. Conéctese a un “**Device**” y “**Connect**”.

![Img](./media/A127.png)

6\. “**Done**” y conectado.

![Img](./media/A144.png)

#### 4.1.3.2.2 Descargar código

Después de conectar, haga clic en “**Download**” y el código se descargará en la placa micro:bit, y ![Img](./media/A212.png) se convierte en ![Img](./media/A220.png).

![Img](./media/A232.png)

⚠️ **Consejos**

Si no hay ningún dispositivo para emparejar en la interfaz, consulte la [solución de problemas de WebUSB del dispositivo](https://makecode.microbit.org/device/usb/webusb/troubleshoot).

Si el firmware de la micro:bit requiere una actualización, consulte [cómo actualizar el firmware](https://microbit.org/guide/firmware/).

### 4.1.3.3 Descargar Código (sin WebUSB)

1\. Conecte la placa micro:bit a su ordenador mediante un cable micro USB.

![Img](./media/A800.png)

Cuando la micro:bit se enciende, el indicador LED rojo en su parte posterior se iluminará.

En la placa micro:bit, hay un indicador LED amarillo que parpadeará cuando la placa se comunique con su ordenador a través de micro USB.

Abra Finder (Mac) / Dispositivos y unidades (Windows), y podrá ver una unidad USB llamada "MICROBIT". ¡Pero tenga en cuenta que no es un disco común!

![Img](./media/A849.png)

2\. Para los navegadores, cargue el código en la placa micro:bit de la siguiente manera:

![Img](./media/Animations-1.gif)

Pasos:

① Haga clic en el botón “**Download**” y se descargará un archivo “**.hex**”, que puede ser leído por la placa micro:bit. Después de eso, cópielo y péguelo en la placa.

Para Windows, puede “**Send to→MICROBIT**” y cargar el “**.hex**” en la placa micro:bit. Durante este proceso, el indicador amarillo en la parte posterior de la placa parpadeará. Cuando termine de cargarse, el indicador permanecerá encendido.

![Img](./media/A319.png)

![Img](./media/A449.png)

O puede arrastrar directamente el archivo “**.hex**” a la MICROBIT:

![Img](./media/A341.png)

![Img](./media/A345.png)

② Después de eso, conecte la placa micro:bit al ordenador mediante un cable micro USB y enciéndala, y podrá ver la matriz de LED de 5x5 a bordo mostrando repetidamente ![Img](./media/A903.png) y ![Img](./media/A910.png).

![Img](./media/A22.png)



⚠️ Durante cada programación, el disco MICROBIT se expulsará y volverá automáticamente, y los archivos **.hex** que haya copiado en él no se mostrarán. Esto se debe a que la placa micro:bit solo recibe y ejecuta el último programa cargado en lugar de almacenarlos.

