import pandas as pd
from elasticsearch import Elasticsearch
es = Elasticsearch("http://localhost:9200")
df=pd.read_csv("E:/people-500000.csv").dropna()
fard=df.iloc[1:500000:2,::]
a= pd.DataFrame(fard)
zoj=df.iloc[0:500000:2,::]
b=pd.DataFrame(zoj)
in_phone=pd.merge(a, b, on='Phone', how='inner')
m=str(len(in_phone['Phone'].unique()))
es.index(index='emtehan', document={'soal':'1' , 'javab':m})
print(m)
n=str(len(df['Job Title'].unique()))
es.index(index='emtehan', document={'soal':'2' , 'javab':n})
print(n)
v=df['Date of birth'].value_counts()
print(v)
c=df['First Name'].value_counts()
print(c)
female = df[df['Sex']=='Female']
x=str(len(female['Job Title'].unique()))
es.index(index='emtehan', document={'soal':'5' , 'javab':x})
print(x)
male =df[df['Sex']=='Male']
z=str(len(male['Job Title'].unique()))
es.index(index='emtehan', document={'soal':'5' , 'javab':z})
print(z)


