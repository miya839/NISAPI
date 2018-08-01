#!/usr/bin/python
#-*- coding: utf-8 -*- 

import requests
import json

class NIS():
    def __init__(self, URL, Address):
        self.url = URL
        self.address = Address 

    def heartbeat(self):
        #NISが稼働しているかどうかを要求する．
        print (requests.get(self.url + "/heartbeat").json())
    
    def status(self,URL):
        #NISの状態を決定する
        print (requests.get(self.url + "/status").json())

class Account():
    def __init__(self, URL, Address):
        self.url = URL
        self.address = Address 

    def generate(self):
        #新しいアカウントデータを生成する．
        print (requests.get(self.url + "/account/generate"))

    def account(self):
        #アドレスからアカウントのデータを要求する
        #vestedBalance:　ハーベスティング(マイニング)を行うために必要な既得残高 ハーベストにはこの値が10,000以上必要
        #Balance: 残高
        #Importnce: 重要度　上げることでハーベスティングする確率が上がる．Xemを使用すると上がる．
        zaif_ticker = requests.get("https://api.zaif.jp/api/1/ticker/xem_jpy").json()
        account = requests.get(self.url + "/account/get?address=" + self.address).json()["account"]
        balance = account["balance"]
        # print (account)
        print ("balance: {} XEM".format(float(balance) / 1000000.0))
        print ("balance: {0} YEN (zaif {1})".format(float(balance) / 1000000.0 * zaif_ticker["vwap"],zaif_ticker["vwap"]))

    def forward(self):
        res = requests.get(URL + "/account/get/forwarded?address=" + address).json()
        print (res)

    def publicKey(self, publicKey):
        #publicKeyからアカウントデータを要求する
        res = requests.get(URL + "/account/get/forwarded/from-public-key?address=" + publicKey).json()
        print (res)

    def status(self):
        res = requests.get(self.url + "/account/status?address=" + self.address).json()
        print (res)


if __name__ == '__main__':
    URL = "http://go.nem.ninja:7890"
    address = "NDOZFGZTFYVSKHGCSPZEFKM2WFQSXM66M5MCHYNP"
    myAccount = Account(URL, address)
    myAccount.status()
    # heartbeat(URL)
    # account(URL, address)
    # status(URL)
    # forward(URL,address)



