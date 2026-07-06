## Solución de Problemas

### 5.3.1 Preguntas Frecuentes

#### 5.3.1.1 Problemas

Muchos usuarios nuevos han encontrado recientemente este problema: Cuando conectan la placa Micro:bit al ordenador mediante un cable Micro USB y hacen clic en “**Download**”, el código no se descarga y la placa no responde.

Si accidentalmente mantuvo presionado el botón de reinicio en la parte posterior de la placa Micro:bit en el momento en que copió el programa en ella, esto habría puesto la placa en modo de mantenimiento. O quizás debido a algunos errores propios, el firmware de la placa se ha perdido.

Como resultado, aparecerá una nueva unidad “**MAINTENANCE**” en su administrador de archivos, por lo que la micro:bit no aceptará su código de usuario.

La unidad MAINTENANCE se verá así, dependiendo de su ordenador:

![Img](./media/158.png)

#### 5.3.1.2 Soluciones

(1) Descargue el archivo <span style="color: rgb(255, 76, 65);">.hex</span> apropiado para su versión de micro:bit desde esta página a su ordenador.

Descargue [el último firmware de Micro:bit - archivo .hex 0255](https://www.microbit.org/get-started/user-guide/firmware/), que también proporcionamos en la carpeta.

(2) Arrastre y suelte el archivo .hex que descargó de esta página en la unidad **MAINTENANCE**. <span style="color: rgb(255, 76, 65);">Tenga en cuenta que el firmware varía según el modelo de la placa Micro:bit V2. Aquí está el Firmware para V2.20_V2.21.</span> Cuando la actualización se complete, la micro:bit se reiniciará, se expulsará del ordenador y reaparecerá en el modo de unidad **MICROBIT** normal.

![Img](./media/326.png)

![Img](./media/331.png)

#### 5.3.1.3 Evitar el Modo “MAINTENANCE”

(1) No presione el botón de reinicio en la parte posterior de la placa Micro:bit cuando esté conectada a un cable Micro USB.

Si se presiona el botón de reinicio al encender, la micro:bit entrará en modo de mantenimiento. (**<span style="color: rgb(255, 76, 65);">Errores comunes cometidos por principiantes</span>**)

![Img](./media/228.png)

(2) No la desconecte repentinamente durante la descarga del programa. O el firmware podría perderse, y la micro:bit entrará entonces en modo MAINTENANCE.

(3) Durante el experimento, un cableado incorrecto también provocará un cortocircuito, por lo que el firmware de la micro:bit podría perderse. Los principiantes deben prestar atención al operar.

#### 5.3.1.4 Descargar con WebUSB

¿Su micro:bit parece haber desarrollado un fallo con WebUSB (/ device/ usb/ webusb)? Intentemos averiguar la razón.

**Paso 1: Prueba con el cable micro USB**

Conecte la micro:bit a su ordenador con un cable micro USB. Debería aparecer como una unidad MICROBIT.

![Img](./media/321.png)

Si MICROBIT aparece como una unidad en Dispositivos y unidades, vaya al Paso 2.

Si no, intente: (a) otro cable; (b) otro puerto USB en su ordenador; (c) conectar la micro:bit a otro ordenador.

Algunos cables micro USB solo pueden ofrecer una conexión de alimentación y no transmiten datos, y algunos ordenadores pueden apagar sus puertos USB por alguna razón.

¿Todavía no puede ver la unidad MICROBIT? Hum, podría haber un problema con su placa micro:bit. Consulte el artículo sobre [solución de problemas](https://support.microbit.org/solution/articles/19000024000-fault-finding-with-a-micro-bit) con microbit.org o abra un [ticket de soporte](https://support.microbit.org/support/tickets/new) para notificar el problema a la Fundación Micro:bit. Y, omita todos los pasos siguientes.

**Paso 2: Comprobación de la versión de su firmware**

Para saber qué versión de firmware tiene en su micro:bit:

① Conéctela a un ordenador mediante el cable USB y abra la unidad **MICROBIT**.

![Img](./media/A8491.png)

② Abra el archivo **DETAILS.TXT**.

![Img](./media/0452.png)

③ Busque el número en la línea que comienza con “Interface/Bootloader Version”.

![Img](./media/501.png)

Si es 0234/0241/0243, necesita actualizar el firmware de su placa micro:bit V2. Vaya al Paso 3 para la actualización.

Si es 0249/0257 o superior, vaya al Paso 4.

**Paso 3: Cómo actualizar el firmware**

Si necesita actualizar el firmware para acceder a una nueva función o solucionar un problema, aquí le explicamos cómo hacerlo:

① Desconecte el cable USB y el paquete de baterías de la micro:bit.

② Mantenga presionado el botón de reinicio en la parte posterior de la micro:bit y conecte el cable USB a la micro:bit y a su ordenador. Debería ver una unidad aparecer en su administrador de archivos llamada **MAINTENANCE** (en lugar de MICROBIT) y el indicador LED amarillo en la parte posterior debería encenderse.

![Img](./media/551.png)

![Img](./media/AAC1.webp)

③ Descargue el [archivo .hex del firmware](https://microbit.org/guide/firmware/) apropiado para su versión de micro:bit. <span style="color: rgb(255, 76, 65);">Aquí está el Firmware para V2.20_V2.21.</span>

![Img](./media/0629.png)

④ Arrastre y suelte el firmware <span style="color: rgb(255, 76, 65);">.hex</span> en la unidad **MAINTENANCE**.

![Img](./media/331.png)

⑤ Espere a que el LED amarillo en la parte posterior del dispositivo deje de parpadear. Después de copiar, el LED se apagará y la micro:bit se reiniciará. MAINTENANCE volverá a ser MICROBIT.

⑥ Finalmente, compruebe el archivo <span style="color: rgb(255, 76, 65);">DETAILS.TXT</span> que se encuentra en la unidad **MICROBIT** y asegúrese de que tenga el mismo número de versión que el firmware .hex.

Para cualquier problema con la placa, el modo de mantenimiento y las actualizaciones de firmware, consulte la [Guía de Firmware](https://microbit.org/guide/firmware/).

**Paso 4: Comprobación de la versión de su navegador**

WebUSB es una función relativamente nueva que puede requerir que actualice su navegador. Compruebe si su navegador es: (a) compatible con Android, Chrome OS; (b) Microsoft Edge; (c) Chrome 65+ de Linux, macOS y Windows 10.

**Paso 5: Conexión de un dispositivo**

Abra Google Chrome / Microsoft Edge para ir al editor MakeCode, y haga clic en “**Connect Device**”. Para saber cómo emparejar un dispositivo, consulte [WebUSB (/ device/ usb/ webusb)](https://microbit.org/get-started/user-guide/web-usb/).

¡Disfrute de una descarga rápida!
