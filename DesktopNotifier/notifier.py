#https://youtu.be/lslXD_VU_Do


import datetime
import time
from plyer import notification
import yfinance as yf
from financecode import data

msft=yf.Ticker("MSFT")
datainfo=msft.info
while True:
    notification.notify(
        title="To-Do List".format(datetime.date.today()),
        message="Current Price={cp} \nDay Low={dl} \nDay High={dh}".format(
            cp=datainfo['currentPrice'],
            dl=datainfo['dayLow'],
            dh=datainfo['dayHigh']
        ),
        app_icon = r"DesktopNotifier\red_bell_icon-icons.com_59499.ico",
        timeout=10
    )
    time.sleep(60*30)
