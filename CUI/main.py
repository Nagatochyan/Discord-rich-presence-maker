from pypresence import Presence
import time
import os
os.system("discord rich presence maker")
clear = lambda: os.system('cls')
clear()
content=input("内容：")
subcontent=input("細かい説明:")
timeornot=input("プレイ時間を追加しますか？(y/n):")

def notimenobutton():
    try:
        rpc=Presence("1072099016302673951")
        rpc.connect()
        rpc.update(state=content,details=subcontent)
    except Exception as e:
        print("discordを起動してください。")

def notimehavebutton(buttonnamae,buttonurll):
    try:
        rpc=Presence("1072099016302673951")
        rpc.connect()
        rpc.update(state=content,details=subcontent,buttons=[{"label": buttonnamae, "url": buttonurll}])
    except Exception as e:
        print("discordを起動してください。")

def havetimenobutton():
    try:
        rpc=Presence("1072099016302673951")
        rpc.connect()
        rpc.update(state=content,details=subcontent,start=time.time())
    except Exception as e:
        print("discordを起動してください。")

def havetimehavebutton(buttonnamae,buttonurll):
    try:
        rpc=Presence("1072099016302673951")
        rpc.connect()
        rpc.update(state=content,details=subcontent,start=time.time(),buttons=[{"label": buttonnamae, "url": buttonurll}])
    except Exception as e:
        print("discordを起動してください。")

if timeornot=="y":
    addbutton=input("ボタンを追加しますか？(y/n):")
    if addbutton=="y":
        buttonname=input("ボタンの名前:")
        buttonurl=input("ボタンを押したらアクセスするURL:")
        print("ステータスの表示に成功しました！")
        while True:
            havetimehavebutton(buttonnamae=buttonname,buttonurll=buttonurl)
    else:
        print("ステータスの表示に成功しました！")
        while True:
            havetimenobutton()

else:
    addbutton=input("ボタンを追加しますか？(y/n):")
    if addbutton=="y":
        buttonname=input("ボタンの名前:")
        buttonurl=input("ボタンを押したらアクセスするURL:")
        print("ステータスの表示に成功しました！")
        while True:
            notimehavebutton(buttonnamae=buttonname,buttonurll=buttonurl)
    else:
        print("ステータスの表示に成功しました！")
        while True:
            notimenobutton()
