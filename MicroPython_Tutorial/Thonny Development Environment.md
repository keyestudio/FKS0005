## 5.1 Thonny 開発環境

**プログラミングの前に、いくつかの重要な準備をする必要があります。**

### 5.1.1 Thonny のインストール

Thonny は、サイズが小さく、インターフェースがシンプルで、操作が簡単で、機能が豊富な無料のオープンソースソフトウェアプラットフォームです。初心者向けの Python IDE です。このチュートリアルでは、この IDE を使用して ESP32 を開発します。Thonny は、Windows、Mac OS、Linux など、複数のオペレーティングシステムをサポートしています。

**1. Thonny のダウンロード**

(1) ウェブサイト: [https://thonny.org](https://thonny.org) にアクセスして、最新バージョンの Thonny をダウンロードしてください。他のバージョンは microbit の機能と互換性がない場合があります。
(2) Thonny のオープンソースコードライブラリ: [https://github.com/thonny/thonny](https://github.com/thonny/thonny)。

お使いのオペレーティングシステムに合ったものをダウンロードしてください。

| OS | ダウンロード |
| :-- | :-- |
| MAC OS： | https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.pkg|
| Windows： | https://github.com/thonny/thonny/releases/download/v4.1.7/thonny-4.1.7.exe|

| OS | 方法 | コマンド |
| :-- |---------|--------------|
| Linux | バイナリバンドル | `bash <(wget -O - https://thonny.org/installer-for-linux)` |
| | `pip` で | `pip3 install thonny` |
| | ディストリビューションパッケージ | Debian/Ubuntu：`sudo apt install thonny`<br>Fedora：`sudo dnf install thonny` |

![Img](./media/t001.png)

**2. Windows システム**

A.ダウンロードした Thonny のアイコンは次のとおりです。

![Img](./media/t002.png)

B.「thonny-4.1.7.exe」をダブルクリックし、インストールモードを選択します。ここでは「Install for all users」を選択します。

![Img](./media/t003.png)

C.「Next」を選択し続けることでインストールを完了できます。

![Img](./media/t004.png)

![Img](./media/t005.png)


D.Thonny のインストール先を変更したい場合は、「Browse...」をクリックして新しいパスを選択します。変更しない場合は、「Next」をクリックし続けます。

![Img](./media/t006.png)

![Img](./media/t007.png)

E.「Create desktop icon」にチェックを入れると、デスクトップに Thonny が表示されます。

![Img](./media/t008.png)

F.「Install」。

![Img](./media/t009.png)

G.しばらく待ちますが、「Cancel」はクリックしないでください。

![Img](./media/t010.png)

H.成功画面が表示されたら、「Finish」をクリックします。

![Img](./media/t011.png)

I.「Create desktop icon」にチェックを入れた場合、デスクトップにアイコンが表示されます。

![Img](./media/t011.png)                    

### 5.1.2 Thonny の基本設定

A.Thonny をダブルクリックし、言語と初期設定を選択して「Let’s go!」をクリックします。

![Img](./media/t013.png)

![Img](./media/t014.png)

![Img](./media/t015.png)

B.「**View**」→「**File**」と「**Shell**」をクリックします。

![Img](./media/t016.png)

![Img](./media/t017.png)

![Img](./media/t018.png)

### 5.1.3 MicroPython ファームウェアの書き込み (重要)

Micro:bit ボードで Python プログラムを実行するには、まずファームウェアを書き込む必要があります。

**MicroPython ファームウェアの書き込み:**

Micro:bit を USB ケーブルで PC に接続します。

![Img](./media/A800.png)

ドライバーが正常にインストールされ、COM ポートが正しく認識されていることを確認します。「**Device Manager**」を開き、「**Ports**」を展開します。

![Img](./media/t019.png)

COM ポート番号はコンピューターによって異なる場合があります。

Thonny を開き、「**run**」をクリックし、「**Configure interpreter...**」をクリックします。

![Img](./media/t020.png)

インタープリターで「Micropython (BBC micro:bit)」と「mbeb Serial Port @ COM16」を選択し、「Install or update firmware」をクリックします。

![Img](./media/t021.png)

すると、次のように表示されます。「Target volume」を「MICROBIT」、「MicroPython family」を「nRF52」、「variant」を「BBC micro:bit v2 (original simplifiled API)」、「version」を「2.1.2」に設定し、「Install」をクリックします。

ファームウェアのインストールに失敗した場合は、Micro:bit のリセットボタンを押し、「Install」をクリックします。

![Img](./media/t022.png)

その後、「Close」と「OK」をクリックします。

![Img](./media/t023.png)

すべてのウィンドウを閉じ、メインページに戻り、「STOP」アイコンをクリックします。

![Img](./media/t024.png)

### 5.1.4 コードのアップロード

**テストコードの実行 (オンライン)**

Micro:bit は、コンピューターに接続する必要があるときにオンラインでコードを実行します。ユーザーは Thonny を使用してプログラムをプログラミングおよびデバッグできます。

Thonny を開き、「**Open**」をクリックします。

![Img](./media/t025.png)

新しいウィンドウがポップアップしたら、「.\MicroPython_Resource\Codes\Heart beat」を開き、「heartbeat&ZeroWidthSpace;.py」を選択し、「Run current script」をクリックします (エラーが報告された場合は、まず ![Img](./media/t027.png) をクリックしてから「Run current script」をクリックします)。すると、Micro:bit でハートが点滅しているのが見えます。

![Img](./media/t026.png)

注: オンラインで実行しているときにリセットボタンを押しても、コードは再度実行されません。リセット後に実行したい場合は、以下のオフライン実行手順を参照してください。

**テストコードの実行 (オフライン)**

Micro:bit をリセットした後、まずルートディレクトリにある main.py ファイルを実行します。

したがって、リセット後にコードを実行したい場合は、Micro:bit にアップロードするファイル名を main.py に変更する必要があります。その後、ファイルをアップロードし、リセットボタンを押すと、コードが引き続き実行されます。

ここでは heartbeat.py を例にとります。**heartbeat&ZeroWidthSpace;.py** を選択して main.py に「**rename**」し、「**OK**」をクリックします。これで「**Upload to micro:bit**」を選択できます。

![Img](./media/t028.png)

![Img](./media/t029.png)

![Img](./media/t030.png)

リセットボタンを押すと、Micro:bit でハートが点滅しているのが見えます。

他のコード (ライブラリではない) を実行したい場合は、アップロードする前にまずその名前を main&ZeroWidthSpace;.py に変更する必要があります。

ライブラリについては、右クリックして直接「Upload to micro:bit」します (ライブラリのサイズが大きすぎるため、アップロードが失敗する場合があります。その場合は、簡素化するか、不要なものを削除する必要があります)。

### 5.1.5 その他の一般的な操作

**Micro:bit のファイルを削除**

「micro:bit」で「main&ZeroWidthSpace;.py」を選択して「Delete」すると、削除されます。

![Img](./media/t031.png)

他のファイルを削除する場合も同じ手順です。
