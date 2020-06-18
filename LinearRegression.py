# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler
import numpy as np
import matplotlib.pyplot as plt

spark=SparkSession.builder.getOrCreate()
df=spark.read.csv('D:\PY\ML\m_share.csv',header=True)
datas=df.select(df.view.cast('double'),df.like.cast('double'),df.danmaku.cast('double'),df.reply.cast('double'),df.share.cast('double'))

#datas=df.select(df.view.cast('double'),df.like.cast('double'),df.danmaku.cast('double'),df.reply.cast('double'),df.share.cast('double'))

(trainingdata,testdata)=datas.randomSplit([0.7,0.3])

assembler=VectorAssembler(inputCols=["view","like","danmaku","reply"],outputCol="features")
output=assembler.transform(trainingdata)
label_features=output.select("features","share").toDF('features','label')
label_features.show(truncate=False)

lr=LinearRegression(maxIter=10,regParam=0.3,elasticNetParam=0.8)
lrModel=lr.fit(label_features)
print("Coefficients: %s" % str(lrModel.coefficients))
print("Intercept: %s" % str(lrModel.intercept))

trainingSummary = lrModel.summary
print("numIterations: %d" % trainingSummary.totalIterations)
print("objectiveHistory: %s" % str(trainingSummary.objectiveHistory))

trainingSummary.residuals.show()
print("RMSE: %f" % trainingSummary.rootMeanSquaredError)
print("r2: %f" % trainingSummary.r2)

output1=assembler.transform(testdata)
test_features=output1.select("features","share").toDF('features','label')

result=lrModel.transform(label_features).collect()
reallist=[]
prelist=[]
ccc=0
for it in result:
    if ccc==50:
        break
    reallist.append(it['label'])
    prelist.append(it['prediction'])
    ccc+=1
print(reallist)
print(prelist)

fig=plt.figure(figsize=(10,6))
plt.ylim(0,10000)
ax=fig.add_subplot(1,1,1)
ax.set_title('Test')
ax.set_xlabel('number')
ax.set_ylabel('video_score')
ticks=ax.set_xticks(np.arange(50))
ax.scatter(np.arange(50),prelist,label='Pred_Value')
ax.scatter(np.arange(50),reallist,label='Label_Value')
ax.legend(loc='best')
plt.savefig('D:\PY\GraphX\handle\png\graph2.png',dpi=400,bbox_inches='tight')