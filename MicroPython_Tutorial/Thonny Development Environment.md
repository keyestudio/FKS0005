## 5.1.1 Thonny IDEのインストール

⚠️ **以下の手順はWindowsオペレーティングシステムで操作されています。他のオペレーティングシステムを使用している場合は、参考にしてください。**

Thonnyは、初心者向けのPython IDEです。MicroPythonをmicro:bitボードにロードするのに役立ちます。

[Thonny IDE](https://thonny.org/)をダウンロードするには、ここをクリックしてください。

![Img](./media/A637.png)

**手順:**

1\. ダウンロードしたファイル「**thonny-4.0.2.exe**」をダブルクリックします。

![Img](./media/B001.png)

2\. 「**Install for all users (recommended)**」を選択し、「**Next**」をクリックします。

![Img](./media/B002.png)

3\. 「**I accept the agreement**」を選択し、「**Next**」をクリックします。

![Img](./media/B003.png)

4\. インストールパスを選択し、「**Next**」をクリックします。

![Img](./media/B004.png)

5\. 「**Next**」をクリックします。

![Img](./media/B005.png)

6\. 「**Install**」をクリックします。

![Img](./media/B006.png)

7\. インストール中:

![Img](./media/B007.png)

8\. 「**Finish**」をクリックします。

![Img](./media/B008.png)

## 5.1.2 Thonny IDEでのMicroPythonの書き込み

### 5.1.2.1 MicroPythonファームウェアの書き込み

⚠️ **MicroPythonでプログラミングする前に、MicroPythonファームウェアをmicro:bitボードに書き込む必要があります。**

**手順:**

1\. micro USBケーブルを使用して、micro:bitボードをコンピューターに接続します。

![Img](./media/A800.png)

micro:bitの電源がオンになると、背面にある赤いLEDインジケーターが点灯します。

micro:bitボードには、micro USBを介してコンピューターと通信する際に点滅する黄色のLEDインジケーターがあります。

Finder(Mac) / デバイスとドライブ(Windows)を開くと、「MICROBIT」という名前のUSBドライブが表示されます。ただし、これは一般的なディスクではありません！

![Img](./media/A849.png)

2\. Thonny IDEを開き、「**Tools**」→「**Options...**」をクリックします。

![Img](./media/B009.png)

3\. 「**Interpreter**」タブをクリックし、「**MicroPython (micro:bit)**」を選択します。

![Img](./media/B010.png)

4\. 「**Install or update firmware**」をクリックします。

![Img](./media/B011.png)

5\. 「**Port**」でmicro:bitボードのポートを選択し、「**Install**」をクリックします。

![Img](./media/B012.png)

6\. インストール中:

![Img](./media/B013.png)

7\. 「**Close**」をクリックします。

![Img](./media/B014.png)

8\. 「**OK**」をクリックします。

![Img](./media/B015.png)

### 5.1.2.2 MicroPythonコードの書き込み

**手順:**

1\. micro USBケーブルを使用して、micro:bitボードをコンピューターに接続します。

![Img](./media/A800.png)

micro:bitの電源がオンになると、背面にある赤いLEDインジケーターが点灯します。

micro:bitボードには、micro USBを介してコンピューターと通信する際に点滅する黄色のLEDインジケーターがあります。

Finder(Mac) / デバイスとドライブ(Windows)を開くと、「MICROBIT」という名前のUSBドライブが表示されます。ただし、これは一般的なディスクではありません！

![Img](./media/A849.png)

2\. Thonny IDEを開き、「**File**」→「**Open...**」をクリックします。

![Img](./media/B016.png)

3\. MicroPythonコードを選択し、「**Open**」をクリックします。

![Img](./media/B017.png)

4\. コードを開いた後、「**Run**」をクリックし、「**Run current script**」を選択します。

![Img](./media/B018.png)

5\. 「**MicroPython device**」を選択します。

![Img](./media/B019.png)

6\. コードがmicro:bitボードに書き込まれます。

![Img](./media/B020.png)

7\. 書き込み後、micro:bitボードのLEDマトリックスに「Hello World!」が表示されます。

![Img](./media/B021.png)

## 5.1.3 Thonny IDEでのMicroPythonライブラリの追加

### 5.1.3.1 ライブラリの追加

⚠️ **各プロジェクトのコードファイル（.py）を提供していますので、Thonny IDEに直接ロードできます。または、必要に応じてコードブロックを自分で構築することもできます。手動で構築する場合はライブラリが必要であることに注意してください。**

**手順:**

1\. micro USBケーブルを使用して、micro:bitボードをコンピューターに接続します。

![Img](./media/A800.png)

micro:bitの電源がオンになると、背面にある赤いLEDインジケーターが点灯します。

micro:bitボードには、micro USBを介してコンピューターと通信する際に点滅する黄色のLEDインジケーターがあります。

Finder(Mac) / デバイスとドライブ(Windows)を開くと、「MICROBIT」という名前のUSBドライブが表示されます。ただし、これは一般的なディスクではありません！

![Img](./media/A849.png)

2\. Thonny IDEを開き、「**Tools**」→「**Manage packages...**」をクリックします。

![Img](./media/B022.png)

3\. 「**Install from local file**」をクリックします。

![Img](./media/B023.png)

4\. 「**Browse...**」をクリックします。

![Img](./media/B024.png)

5\. ライブラリファイルを選択し、「**Open**」をクリックします。

![Img](./media/B025.png)

6\. 「**Install**」をクリックします。

![Img](./media/B026.png)

7\. インストール中:

![Img](./media/B027.png)

8\. 「**Close**」をクリックします。

![Img](./media/B028.png)

### 5.1.3.2 ライブラリの削除

**手順:**

1\. micro USBケーブルを使用して、micro:bitボードをコンピューターに接続します。

![Img](./media/A800.png)

micro:bitの電源がオンになると、背面にある赤いLEDインジケーターが点灯します。

micro:bitボードには、micro USBを介してコンピューターと通信する際に点滅する黄色のLEDインジケーターがあります。

Finder(Mac) / デバイスとドライブ(Windows)を開くと、「MICROBIT」という名前のUSBドライブが表示されます。ただし、これは一般的なディスクではありません！

![Img](./media/A849.png)

2\. Thonny IDEを開き、「**Tools**」→「**Manage packages...**」をクリックします。

![Img](./media/B022.png)

3\. 削除したいライブラリを選択し、「**Uninstall**」をクリックします。

![Img](./media/B029.png)

4\. 「**Yes**」をクリックします。

![Img](./media/B030.png)

5\. 「**Close**」をクリックします。

![Img](./media/B031.png)
