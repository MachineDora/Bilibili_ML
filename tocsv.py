# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
import pymongo

client=pymongo.MongoClient(host='127.0.0.1',port=27017)
db=client.bilibili
v=db.MLlib_share

data=pd.DataFrame(list(v.find()))
data.head()

data.to_csv('D:\PY\ML\m_share.csv',encoding='utf-8')


