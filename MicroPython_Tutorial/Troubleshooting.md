## トラブルシューティング
### 5.3.1 USBドライバーのインストール (オプション)

**Micro:bitはドライバーのインストールは不要です。ただし、コンピューターがメインボードを認識しない場合は、ドライバーをインストールできます。**


#### 5.3.1.1 USBドライバーのダウンロード

[USBドライバー](./USB_driver.7z)をダウンロードするには、ここをクリックしてください。

#### 5.3.1.2 USBドライバーのインストール

⚠️ ここではWindowsでのドライバーのインストール方法を説明します。これはMacOSユーザーの参考になります。

1\. micro:bitメインボードをUSBケーブルでコンピューターに接続します。

![Img](./media/A800.png)

2\. ドライバーファイルを見つけてクリックし、**Install**をクリックします。

![Img](./media/A323.png)

![Img](./media/A327.png)

3\. 「**Install**」をクリックし、「**Next**」をクリックします。

![Img](./media/A347.png)

4\. 「**Install**」をクリックし、「**Finish**」をクリックします。

![Img](./media/A408.png)

![Img](./media/A349.png)

5\. 「**Computer**」→「**Properties**」→「**Device manager**」をクリックすると、次のように表示されます:

![Img](./media/A427.png)

### 5.3.2 FAQ
Microbitがプログラムをダウンロードできず、MAINTENANCEと表示される問題の解決策。

#### 5.3.2.1 問題

多くの新規ユーザーが最近この問題に遭遇しています: Micro:bitボードをMicro USBケーブルでコンピューターに接続し、「**Download**」をクリックすると、コードがダウンロードされず、ボードが応答しません。

プログラムをコピーする際に誤ってMicro:bitボードの背面にあるリセットボタンを押し続けていた場合、ボードはメンテナンスモードに入ります。または、何らかの誤りにより、ボード上のファームウェアが失われた可能性があります。

その結果、ファイルマネージャーに新しい「**MAINTENANCE**」ドライブが表示され、micro:bitはユーザーコードを受け付けなくなります。

MAINTENANCEドライブは、コンピューターによって次のように表示されます:

![Img](./media/158.png)

 #### 5.3.2.2 解決策

(1) このページからmicro:bitのバージョンに適した<span style="color: rgb(255, 76, 65);">.hex</span>ファイルをコンピューターにダウンロードします。

[最新のMicro:bitファームウェア -0255 .hexファイル](https://www.microbit.org/get-started/user-guide/firmware/)をダウンロードしてください。これはフォルダーにも提供されています。

(2) このページからダウンロードした.hexファイルを**MAINTENANCE**ドライブにドラッグアンドドロップします。<span style="color: rgb(255, 76, 65);">注: ファームウェアはMicro:bit V2ボードのモデルによって異なります。ここではV2.20_V2.21用のファームウェアです。</span>アップグレードが完了すると、micro:bitはリセットされ、コンピューターから排出され、通常の**MICROBIT**ドライブモードで再表示されます。

![Img](./media/326.png)

![Img](./media/331.png)

#### 5.3.2.3 「MAINTENANCE」モードを避ける

(1) Micro USBケーブルが接続されているときに、Micro:bitボードの背面にあるリセットボタンを押さないでください。

電源投入時にリセットボタンが押されると、micro:bitはメンテナンスモードに入ります。（**<span style="color: rgb(255, 76, 65);">初心者が犯しやすい間違い</span>**）

![Img](./media/228.png)

(2) プログラムのダウンロード中に突然抜き差ししないでください。ファームウェアが失われ、micro:bitがMAINTENANCEモードに入る可能性があります。

(3) 実験中に配線ミスがあると、短絡が発生し、micro:bitファームウェアが失われる可能性があります。初心者は操作時に注意を払う必要があります。

#### 5.3.2.4 WebUSBでのダウンロード

WebUSB（/ device/ usb/ webusb）でmicro:bitに障害が発生したようです。原因を突き止めましょう。

**ステップ1: micro USBケーブルでのテスト**

micro USBケーブルでmicro:bitをコンピューターに接続します。MICROBITドライブとして表示されるはずです。

![Img](./media/321.png)

デバイスとドライブの下にMICROBITがドライブとして表示される場合は、ステップ2に進みます。

そうでない場合は、(a)別のケーブル、(b)コンピューターの別のUSBポート、(c)micro:bitを別のコンピューターに接続してみてください。

一部のmicro USBケーブルは電源接続のみを提供し、実際にはデータを送信しない場合があります。また、一部のコンピューターは、何らかの理由でUSBポートの電源を落とす場合があります。

それでもMICROBITドライブが見えませんか？うーん、micro:bitボードに問題があるかもしれません。[トラブルシューティング](https://support.microbit.org/solution/articles/19000024000-fault-finding-with-a-micro-bit)の記事を参照するか、[サポートチケット](https://support.microbit.org/support/tickets/new)を開いてMicro:bit Foundationに問題を通知してください。そして、以下のすべての手順をスキップしてください。

**ステップ2: ファームウェアバージョンの確認**

micro:bitにインストールされているファームウェアのバージョンを確認するには:

① USBケーブルを使用してコンピューターに接続し、**MICROBIT**ドライブを開きます。

![Img](./media/A8491.png)

② **DETAILS.TXT**ファイルを開きます。

![Img](./media/0452.png)

③ 「Interface/Bootloader Version」で始まる行の番号を探します。

![Img](./media/501.png)

0234/0241/0243の場合は、micro:bit V2ボードのファームウェアを更新する必要があります。更新についてはステップ3に進みます。

0249/0257以降の場合は、ステップ4に進みます。

**ステップ3: ファームウェアの更新方法**

新機能にアクセスしたり、問題をトラブルシューティングしたりするためにファームウェアを更新する必要がある場合は、次の手順を実行します:

① USBケーブルとバッテリーパックをmicro:bitから切断します。

② micro:bitの背面にあるリセットボタンを押し続け、USBケーブルをmicro:bitとコンピューターに接続します。ファイルマネージャーに**MAINTENANCE**（MICROBITではなく）というドライブが表示され、背面にある黄色のLEDインジケーターが点灯するはずです。

![Img](./media/551.png)

![Img](./media/AAC1.webp)

③ micro:bitのバージョンに適した[ファームウェア.hexファイル](https://microbit.org/guide/firmware/)をダウンロードします。<span style="color: rgb(255, 76, 65);">ここではV2.20_V2.21用のファームウェアです。</span>

![Img](./media/0629.png)

④ <span style="color: rgb(255, 76, 65);">.hex</span>ファームウェアを**MAINTENANCE**ドライブにドラッグアンドドロップします。

![Img](./media/331.png)

⑤ デバイスの背面にある黄色のLEDが点滅を停止するまで待ちます。コピー後、LEDは消灯し、micro:bitはリセットされます。MAINTENANCEはMICROBITに戻ります。

⑥ 最後に、**MICROBIT**ドライブにある<span style="color: rgb(255, 76, 65);">DETAILS.TXT</span>ファイルを確認し、.hexファームウェアと同じバージョン番号であることを確認します。

ボード、メンテナンスモード、ファームウェアの更新に関する問題については、[ファームウェアガイド](https://microbit.org/guide/firmware/)を参照してください。

**ステップ4: ブラウザバージョンの確認**

WebUSBは比較的新しい機能であり、ブラウザを更新する必要がある場合があります。ブラウザが次のいずれかと互換性があるか確認してください: (a) Android、Chrome OS; (b) Microsoft Edge; (c) Linux、macOS、Windows 10のChrome 65+。

**ステップ5: デバイスの接続**

Google Chrome / Microsoft Edgeを開いてMakeCodeエディターに移動し、「**Connect Device**」をクリックします。デバイスのペアリング方法については、[WebUSB（/ device/ usb/ webusb）](https://microbit.org/get-started/user-guide/web-usb/)を参照してください。

迅速なダウンロードをお楽しみください！


