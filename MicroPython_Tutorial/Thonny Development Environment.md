## 5.1 Entorno de Desarrollo Thonny

**Antes de programar, debe realizar algunas preparaciones importantes.**

### 5.1.1 Instalar Thonny

Thonny es una plataforma de software gratuita y de código abierto con un tamaño pequeño, una interfaz sencilla, un funcionamiento simple y funciones ricas. Es un IDE Python adecuado para principiantes. En este tutorial, utilizaremos este IDE para desarrollar un ESP32. Thonny es compatible con múltiples sistemas operativos, incluidos Windows, Mac OS y Linux.

**1. Descargar Thonny**

(1) Ingrese al sitio web: [https://thonny.org](https://thonny.org) para descargar la última versión de Thonny. Otras versiones pueden no ser compatibles con las funciones de microbit.
(2) Librería de código abierto de Thonny: [https://github.com/thonny/thonny](https://github.com/thonny/thonny).

Descargue la versión correspondiente a su sistema operativo.

| SO | Descarga |
| :-- | :-- |
| MAC OS： | https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.pkg|
| Windows： | https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.exe|

| SO | Método | Comando |
| :-- |---------|--------------|
| Linux | Paquete binario | `bash <(wget -O - https://thonny.org/installer-for-linux)` |
| | Con pip | `pip3 install thonny` |
| | Paquetes de distribución | Debian/Ubuntu：`sudo apt install thonny`<br>Fedora：`sudo dnf install thonny` |

![Img](./media/t001.png)

**2. Sistema Windows**

A. El icono de Thonny descargado es el siguiente:

![Img](./media/t002.png)

B. Haga doble clic en “thonny-4.1.7.exe” y seleccione el modo de instalación. Aquí elegimos “Install for all users”.

![Img](./media/t003.png)

C. También puede seguir seleccionando “Next” para finalizar la instalación.

![Img](./media/t004.png)

![Img](./media/t005.png)


D. Si desea cambiar la ruta de instalación de Thonny, simplemente haga clic en “Browse...” para seleccionar una nueva ruta. Si no, simplemente siga haciendo clic en “Next”.

![Img](./media/t006.png)

![Img](./media/t007.png)

E. Marque “Create desktop icon”, verá Thonny en su escritorio.

![Img](./media/t008.png)

F. “Install”.

![Img](./media/t009.png)

G. Espere un momento, pero no haga clic en “Cancel”.

![Img](./media/t010.png)

H. Cuando vea la interfaz de éxito, haga clic en “Finish”.

![Img](./media/t011.png)

I. Puede ver el icono en su escritorio si marca “Create desktop icon”:

![Img](./media/t011.png)

### 5.1.2 Configuración Básica de Thonny

A. Haga doble clic en Thonny, elija el idioma y la configuración inicial y haga clic en “Let’s go!”.

![Img](./media/t013.png)

![Img](./media/t014.png)

![Img](./media/t015.png)

B. Haga clic en “**View**”→“**File**” y “**Shell**”.

![Img](./media/t016.png)

![Img](./media/t017.png)

![Img](./media/t018.png)

### 5.1.3 Grabar Firmware Micropython (Importante)

Para ejecutar un programa Python en la placa Micro:bit, primero debemos grabar el firmware en ella.

**Grabar el firmware Micropython:**

Conecte la Micro:bit a su PC con un cable USB.

![Img](./media/A800.png)

Asegúrese de que el controlador se haya instalado correctamente y que el puerto COM se pueda identificar correctamente. Abra “**Device Manager**” y expanda “**Ports**”.

![Img](./media/t019.png)

El número de puerto COM puede variar según los ordenadores.

Abra Thonny, haga clic en “**run**” y “**Configure interpreter...**”

![Img](./media/t020.png)

Seleccione “Micropython (BBC micro:bit)” y “mbeb Serial Port @ COM16” en su intérprete, y haga clic en “Install or update firmware”.

![Img](./media/t021.png)

Y verá lo siguiente. Establezca “Target volume” en “MICROBIT”, “MicroPython family” en “nRF52”, “variant” en “BBC micro:bit v2 (original simplifiled API)”, “version” en “2.1.2”, y luego “Install”.

Si el firmware no se instala, presione el botón de reinicio en la Micro:bit y haga clic en “Install”.

![Img](./media/t022.png)

Después de eso, haga clic en “Close” y “OK”.

![Img](./media/t023.png)

Cierre todas las ventanas y vaya a la página principal y haga clic en el icono “STOP”:

![Img](./media/t024.png)

### 5.1.4 Cargar Código

**Ejecutar el código de prueba (en línea)**

La Micro:bit ejecuta el código en línea cuando necesita conectarse al ordenador. Los usuarios pueden programar y depurar programas con Thonny.

Abra Thonny y haga clic en "**Open**".

![Img](./media/t025.png)

Cuando aparezca una nueva ventana, abra ".\MicroPython_Resource\Codes\Heart beat", seleccione “heartbeat&ZeroWidthSpace;.py”, y haga clic en “Run current script” (si hay errores, haga clic en ![Img](./media/t027.png) primero y luego en “Run current script”), y podrá ver un corazón latiendo en la Micro:bit.

![Img](./media/t026.png)

Nota: Al ejecutarlo en línea, si presiona el botón de reinicio, el código no se ejecutará de nuevo. Si desea que se ejecute después de reiniciarlo, consulte las instrucciones de ejecución sin conexión a continuación.

**Ejecutar el código de prueba (sin conexión)**

Después de reiniciar Micro:bit, ejecute primero el archivo main.py en el directorio raíz.

Por lo tanto, el nombre del archivo que cargamos en la Micro:bit debe cambiarse a main.py si queremos que ejecute el código después de reiniciar. Luego, cargue el archivo, presione el botón de reinicio y el código seguirá ejecutándose.

Aquí tomamos heartbeat.py como ejemplo. Seleccione **heartbeat&ZeroWidthSpace;.py** para "**rename**" a main.py, y haga clic en "**OK**". Ahora puede elegir “**Upload to micro:bit**”.

![Img](./media/t028.png)

![Img](./media/t029.png)

![Img](./media/t030.png)

Presione el botón de reinicio y podrá ver el corazón latiendo en la Micro:bit.

Si desea ejecutar otro código (no librerías), primero debe cambiar su nombre a main&ZeroWidthSpace;.py antes de cargarlo.

En cuanto a las librerías, haga clic derecho para “Upload to micro:bit” directamente (a veces la carga puede fallar debido al tamaño demasiado grande de la librería. Por lo tanto, debe simplificarla o eliminar las que no se utilicen).

### 5.1.5 Otras Operaciones Comunes

**Eliminar archivo en Micro:bit**

En “micro:bit”, seleccione “main&ZeroWidthSpace;.py” para “Delete”, y se eliminará.

![Img](./media/t031.png)

El mismo procedimiento se aplica al eliminar otros archivos.
