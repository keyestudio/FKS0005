## 4.1.1 MakeCodeについて

⚠️ **以下の手順はWindowsオペレーティングシステムで操作されています。他のオペレーティングシステムを使用している場合は、参考にしてください。ここではGoogle Chrome / Microsoft Edgeで説明されています。**

**MakeCodeプログラミング環境:**

[MakeCodeエディターのオンライン版](https://makecode.microbit.org/#editor)を開きます。

MakeCodeのメインインターフェース:

![Img](./media/A637.png)

コード編集エリアには「**on start**」と「**forever**」のブロックがあります。「on start」は電源投入時またはリセット時にコードが一度だけ実行されることを意味し、「forever」はコードが繰り返し実行されることを意味します。

「**JS JavaScript**」をクリックするとJavaScriptコードが表示されます:

![Img](./media/A754.png)

または「**Python**」をクリックしてPythonコードに切り替えます:

![Img](./media/A814.png)

**言語設定:**

![Img](./media/Animation-3.gif)

手順:

ステップ1: 設定ボタン ![Img](./media/A806.png) をクリックします。

![Img](./media/A301.png)

ステップ2: 「Language」をクリックします。

![Img](./media/A302.png)

ステップ3: 希望する言語を選択します。ここでは「English」に設定します。

![Img](./media/A303.png)

## 4.1.2 Makecode拡張ライブラリ

### 4.1.2.1 ライブラリの追加

⚠️ **各プロジェクトのコードファイル（.hex）を提供していますので、MakeCodeエディターに直接ロードできます。または、必要に応じてコードブロックを自分で構築することもできます。手動で構築する場合はライブラリが必要であることに注意してください。**

⚠️ **<span style="color: rgb(255, 76, 65);">注:</span>** リンクを検索ボックスにコピーして貼り付けます: `https://github.com/keyestudio2019/pxt-creative-inventors-kit-master.git`。

![Img](./media/Animation-4.gif)

手順:

1\. ![Img](./media/A806.png) をクリックして「**Extensions**」を選択します。

![Img](./media/A842.png)

または、**Advanced**ブロックの上にある「**Extensions**」をクリックします。

![Img](./media/A900.png)

2\. キーワードを検索するか、GitHubリンクを貼り付けます。

![Img](./media/A909.png)

3\. ここでは、URL: `https://github.com/keyestudio2019/KEYES-Smart-Gamepad-master.git` を検索ボックスに入力し、![Img](./media/A3257.png) をクリックして「**Smart-Gamepad**」の拡張機能をロードします。

![Img](./media/A306.png)

4\. ロード中:

![Img](./media/A3316.png)

5\. ロード完了:

![Img](./media/A335.png)

### 4.1.2.2 ライブラリの更新/削除

⚠️ **通常、ライブラリは不要な場合を除き、削除する必要はありません。**

![Img](./media/Animation-4.gif)

手順:

1\. 「**JavaScript**」をクリックしてテキストコードに切り替えます。

![Img](./media/A724.png)

2\. 「**Explorer**」をクリックします。

![Img](./media/A749.png)

3\. 「**Smart-Gamepad**」を見つけて、ゴミ箱 ![Img](./media/A813.png) をクリックして削除します。

![Img](./media/A824.png)

4\. 「**Remove it**」をクリックします。

![Img](./media/A727.png)

## 4.1.3 MakeCodeプログラム

### 4.1.3.1 MakeCodeでのプログラムのインポート

プロジェクト「**heartbeat**」を例にとります。

![Img](./media/Animation-2.gif)

手順:

1\. micro USBケーブルを使用して、micro:bitボードをコンピューターに接続します。

![Img](./media/A800.png)

micro:bitの電源がオンになると、背面にある赤いLEDインジケーターが点灯します。

micro:bitボードには、micro USBを介してコンピューターと通信する際に点滅する黄色のLEDインジケーターがあります。

Finder(Mac) / デバイスとドライブ(Windows)を開くと、「MICROBIT」という名前のUSBドライブが表示されます。ただし、これは一般的なディスクではありません！

![Img](./media/A849.png)

2\. 「**Import**」をクリックします:

![Img](./media/A956.png)

3\. そして「**Import File...**」を選択します。

![Img](./media/A042.png)

4\. 「**Choose File**」をクリックして、必要なファイルを開きます。

![Img](./media/A06.png)

5\. ここでは「**heartbeat.hex**」を選択します。

![Img](./media/A28.png)

6\. 「**Go ahead √**」をクリックします。

![Img](./media/A149.png)

または、hexファイルをMakecodeのメインインターフェースに直接ドラッグすることもできます:

![Img](./media/A202.png)

7\. インポート済み:

![Img](./media/A217.png)

### 4.1.3.2 コードのダウンロード (WebUSB)

**Google Chrome/Microsoft Edge**のようなブラウザでは、WebUSBによりオンラインウェブページを介してmicro USBハードウェアデバイスに直接アクセスできます。「Connect Device」をクリックしてデバイスをペアリングします。その後、「**Download**」をクリックしてコードをmicro:bitボードにロードします。

![Img](./media/Animation.gif)

手順:

#### 4.1.3.2.1 デバイスのペアリング

1\. micro USBケーブルを使用して、micro:bitボードをコンピューターに接続します。

![Img](./media/A951.png)

2\. 「**Download**」の横にある3つの点「**...**」をクリックし、「**Connect device**」を選択します。

![Img](./media/A028.png)

3\. 「**Next**」をクリックします。

![Img](./media/A046.png)

4\. 「**Pair**」をクリックします。

![Img](./media/A104.png)

5\. 「**Device**」に接続し、「**Connect**」をクリックします。

![Img](./media/A127.png)

6\. 「**Done**」をクリックすると接続されます。

![Img](./media/A144.png)

#### 4.1.3.2.2 コードのダウンロード

接続後、「**Download**」をクリックするとコードがmicro:bitボードにダウンロードされ、![Img](./media/A212.png) が ![Img](./media/A220.png) に変わります。

![Img](./media/A232.png)

⚠️ **ヒント**

インターフェースにペアリングするデバイスがない場合は、[device-webusb-troubleshoot](https://makecode.microbit.org/device/usb/webusb/troubleshoot)を参照してください。

micro:bitファームウェアの更新が必要な場合は、[how-to-update-the-firmware](https://microbit.org/guide/firmware/)を参照してください。

### 4.1.3.3 コードのダウンロード (WebUSBなし)

1\. micro USBケーブルを使用して、micro:bitボードをコンピューターに接続します。

![Img](./media/A800.png)

micro:bitの電源がオンになると、背面にある赤いLEDインジケーターが点灯します。

micro:bitボードには、micro USBを介してコンピューターと通信する際に点滅する黄色のLEDインジケーターがあります。

Finder(Mac) / デバイスとドライブ(Windows)を開くと、「MICROBIT」という名前のUSBドライブが表示されます。ただし、これは一般的なディスクではありません！

![Img](./media/A849.png)

2\. ブラウザの場合、次のようにコードをmicro:bitボードにロードします:

![Img](./media/Animations-1.gif)

手順:

① 「**Download**」ボタンをクリックすると、「**.hex**」ファイルがダウンロードされます。これはmicro:bitボードで読み取ることができます。その後、ボードにコピーして貼り付けます。

Windowsの場合、「**Send to→MICROBIT**」で「**.hex**」をmicro:bitボードにロードできます。このプロセス中、ボードの背面にある黄色のインジケーターが点滅します。ロードが完了すると、インジケーターは点灯したままになります。

![Img](./media/A319.png)

![Img](./media/A449.png)

または、直接「**.hex**」ファイルをMICROBITにドラッグすることもできます:

![Img](./media/A341.png)

![Img](./media/A345.png)

② その後、micro USBケーブルでmicro:bitボードをコンピューターに接続して電源をオンにすると、オンボードの5 x 5 LEDマトリックスが ![Img](./media/A903.png) と ![Img](./media/A910.png) を繰り返し表示するのを確認できます。

![Img](./media/A22.png)



⚠️ プログラミング中、MICROBITディスクは自動的に排出されて戻り、コピーした**.hex**ファイルは表示されません。これは、micro:bitボードが最新のアップロードされたプログラムのみを受信して実行し、保存しないためです。

