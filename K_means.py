# -*- coding:utf-8 -*-
from pyspark.mllib.clustering import KMeans, KMeansModel
from numpy import array
from math import sqrt
from pyspark import SparkContext
from pyspark.ml.linalg import Vectors
from pyspark.sql import Row

def f(x):
    rel = {}
    rel['features'] = Vectors.dense(float(x[0]),float(x[1]),float(x[2]),float(x[3]),float(x[4]),float(x[5]))
    return rel

sc = SparkContext("local", "pythonkmeans")

data=sc.textFile('D:\PY\GraphX\handle\k.txt')

parsedData = data.map(lambda line: array([float(x) for x in line.split(' ')]))

clusters = KMeans.train(parsedData, k=10, maxIterations=10,
                            runs=10, initializationMode="random")

def error(point):
        center = clusters.centers[clusters.predict(point)]
        return sqrt(sum([x ** 2 for x in (point - center)]))

WSSSE = parsedData.map(lambda point: error(point)).reduce(lambda x, y: x + y)

print("Within Set Sum of Squared Error = " + str(WSSSE))


def sort(point):
        return clusters.predict(point)

clusters_result = parsedData.map(sort)
# Save and load model
# $example off$

cu=open('D:\PY\GraphX\handle\k_title.txt','a',encoding='utf-8')
title=open('D:\PY\GraphX\handle\Title.txt','r',encoding='utf-8')
tlist=title.read().split('\n')

count=0

for i in clusters_result.collect():
    print(count)
    temp=[]
    temp.append(i)
    temp.append(tlist[count])
    count=count+1
    cu.write(str(temp))
    cu.write('\n')
sc.stop()

