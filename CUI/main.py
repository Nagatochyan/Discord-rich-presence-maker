from pypresence import Presence
import time
content=input("内容：")
subcontent=input("細かい説明:")
timeornot=input("プレイ時間を追加しますか？(y/n):")

def notimenobutton():
    rpc=Presence("1072099016302673951")
    rpc.connect()
    rpc.update(state=content,details=subcontent)

def notimehavebutton(buttonnamae,buttonurll):
    rpc=Presence("1072099016302673951")
    rpc.connect()
    rpc.update(state=content,details=subcontent,buttons=[{"label": buttonnamae, "url": buttonurll}])

def havetimenobutton():
    rpc=Presence("1072099016302673951")
    rpc.connect()
    rpc.update(state=content,details=subcontent,start=time.time())

def havetimehavebutton(buttonnamae,buttonurll):
    rpc=Presence("1072099016302673951")
    rpc.connect()
    rpc.update(state=content,details=subcontent,start=time.time(),buttons=[{"label": buttonnamae, "url": buttonurll}])

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
        notimenobutton()
