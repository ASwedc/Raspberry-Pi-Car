# Raspberry-Pi-Car
需要安裝Flask才能使用

Flask資料庫 

http://flask.pocoo.org/docs/0.12/

安裝指令
```
   $ sudo pip install Flask
```
===================
程式的執行方式打開command視窗
先將目錄移動到程式下載的位置

之後輸入指令
```
   $ sudo python app.py
```
===================
Flask影像串流的部分參考自

https://github.com/miguelgrinberg/flask-video-streaming
===================
GPIO接腳位置

![GPIO](https://pic.pimg.tw/magicjackting/1462987943-3402620679.png)

5V、GND等特殊功能的線路只能接對應功能的接腳

若電池沒電可將L298N的5V接腳接到樹梅派的5V上

讓樹梅派供電給馬達使用
