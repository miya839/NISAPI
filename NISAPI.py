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
        print(requests.get(self.url + "/heartbeat").json())
    
    def status(self,URL):
        #NISの状態を決定する
        print(requests.get(self.url + "/status").json())

class Account():
    def __init__(self, URL, Address):
        self.url = URL
        self.address = Address 

    def generate(self):
        #新しいアカウントデータを生成する．
        print(requests.get(self.url + "/account/generate"))

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
        print(res)

    def publicKey(self, publicKey):
        #publicKeyからアカウントデータを要求する
        res = requests.get(URL + "/account/get/forwarded/from-public-key?address=" + publicKey).json()
        print(res)

    def status(self):
        res = requests.get(self.url + "/account/status?address=" + self.address).json()
        print(res)

    def receiveTransaction(self, hash = None, id = None):
        path = self.url + "/account/transfers/incoming?address=" + self.address
        if(hash):
            path = path + "&hash=" + hash
        if(id):
            path = path + "&id=" + id
        res = requests.get(path).json()
        print(res)

    def sendTransaction(self, hash = None, id = None):
        path = self.url + "/account/transfers/outgoing?address=" + self.address
        if(hash):
            path = path + "&hash=" + hash
        if(id):
            path = path + "&id=" + id
        res = requests.get(path).json()
        print(res)

    def unconfirmedTransaction(self):
        res = requests.get(self.url + "/account/unconfirmedTransactions?address=" + self.address).json()
        print(res)
    
    def harvest(self):
        res = requests.get(self.url + "/account/harvests?address=" + self.address).json()
        print(res)

    def importance(self, hash = None):
        res = requests.get(self.url + "/account/importances").json()
        print(res)

    def namespace(self, parent = None, id = None, pageSize = None):
        path = self.url + "/account/transfers/namespace/page?address=" + self.address
        if(parent):
            path = path + "&parent=" + parent
        if(id):
            path = path + "&id=" + id
        if(pageSize):
            path = path + "&pageSize=" + pageSize
        res = requests.get(path).json()
        print(res)

    def mosaicDefinition(self, parent = None, id = None):
        path = self.url + "/account/mosaic/definition/page?address=" + self.address
        if(parent):
            path = path + "&parent=" + parent
        if(id):
            path = path + "&id=" + id
        res = requests.get(path).json()
        print(res)

    def mosaic(self):
        res = requests.get(self.url + "/account/mosaic/owned?address=" + self.address).json()
        print (res)
        
    def unlock(self, privateKey):
        requests.post(self.url + "/account/unlock?privateKey=" + private_key)

    def lock(self, privateKey):
        requests.post(self.url + "/account/lock?privateKey=" + private_key)
    
    def unlockedInfo(self):
        requests.post(self.url + "/account/unlock/info")
    
    def accountHistorical(self, startHeight, endHeight, increment = 1):
        path = self.url + "/account/historical/get?address=" + self.address
        if(startHeight):
            path = path + "&startHeight=" + str(startHeight)
        if(endHeight):
            path = path + "&endHeight=" + str(endHeight)
        if(increment):
            path = path + "&increment=" + str(increment)
        res = requests.get(path).json()
        print(res)    

if __name__ == '__main__':
    URL = "http://go.nem.ninja:7890"
    address = "NDOZFGZTFYVSKHGCSPZEFKM2WFQSXM66M5MCHYNP"
    myAccount = Account(URL, address)
    myAccount.mosaic()
    



