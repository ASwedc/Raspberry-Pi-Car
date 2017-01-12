# Raspberry-Pi-Car
樹梅派的初次使用安裝
===================
1.在樹梅派上安裝作業系統，我們使用Raspbian當我們的作業系統。

下載網址:

https://www.raspberrypi.org/downloads/raspbian/

2.更新作業系統，並設定以下動作:

改變區域(Change Locale)Zh_TW.UTF-8 UTF-8

改變時區(Change Timezone) ，設定為亞洲台北(Asia / Taipei )。 

改變鍵盤配置(Change Keyboard Layout)，設定為English US 鍵盤。

改變Wi-Fi 國家(Change Wi-Fi Country) ，設定為TW Taiwan 。

3.分別把4顆直流馬達、電池和樹梅派電源接到L298N驅動模組

接腳位置

![接腳圖](https://pic.pimg.tw/magicjackting/1462987943-3402620679.png)

5V、GND等特殊功能的線路只能接對應功能的接腳

左右兩邊的GND跟IN1~8都須接上

若電池沒電可暫時先將L298N的5V接腳接到樹梅派的5V接腳上

把樹梅派接上插頭透過GPIO供電給馬達使用

5.把Github上的程式碼和資料夾放置同一個目錄底下。

6.安裝Flask

Flask資料庫 

http://flask.pocoo.org/docs/0.12/

安裝指令
```
   $ sudo pip install Flask
```
6.接著使用command並切換到放置程式的目錄底下執行app.py

7.接著使用可以連上和樹梅派同一個區網的電腦或手機，在瀏覽器上輸入樹梅派的IP位址並加上port5000(:5000)，就可以開啟操控車子的使用者介面了。

===================
Flask影像串流的部分參考自

https://github.com/miguelgrinberg/flask-video-streaming
