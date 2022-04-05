from sklearn.naive_bayes import GaussianNB
import pandas as pd
import joblib,os,sys
import time



proj_name="flask"
start=time.time()
data=pd.read_csv('traincsv/'+proj_name+'_data.csv')
label=pd.read_csv('traincsv/'+proj_name+'_label.csv')
lines=len(data)
trainnum=lines
train_data=data[:trainnum]
train_label=label[:trainnum]
labels=train_label.values.ravel()

clf = GaussianNB()
clf.fit(train_data,labels)
result=clf.score(train_data,labels)
joblib.dump(clf,'traincsv/'+proj_name+'_NaiveBayes.pkl')
print(result)
#sys.exit()
end=time.time()
print(end-start)