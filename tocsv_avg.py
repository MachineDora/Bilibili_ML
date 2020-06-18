# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import pymongo

client=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=client.bilibili
v=db.MLlib
vv=db.MLlib_toshare

list=v.find()

allview=0
alllike=0
alldanmaku=0
allreply=0
allfavorite=0
allcoin=0
allshare=0

count=0

for i in list:
    allview=allview+i['view']
    alllike =alllike+i['like']
    alldanmaku = alldanmaku+i['danmaku']
    allreply = allreply+i['reply']
    allfavorite = allfavorite+i['favorite']
    allcoin = allcoin+i['coin']
    allshare = allshare+i['share']
    count=count+1

view_avg=allview/count
like_avg=alllike/count
danmaku_avg=alldanmaku/count
reply_avg=allreply/count
favorite_avg=allfavorite/count
coin_avg=allcoin/count
share_avg=allshare/count

listt=v.find()

for i in listt:
    s={
        'view':i['view']*share_avg/view_avg,
        'like':i['like']*share_avg/like_avg,
        'danmaku':i['danmaku']*share_avg/danmaku_avg,
        'reply':i['reply']*share_avg/reply_avg,
        'share':i['share']*10
    }
    vv.insert(s)