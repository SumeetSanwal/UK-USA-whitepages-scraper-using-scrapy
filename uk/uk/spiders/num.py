import pandas as pd
df=pd.read_csv("num.csv")
a=df.iloc[:,0]
lt=[]
for x in a:
    if not "\n" in x:
        lt.append(x)

df2=pd.DataFrame(lt)
df2.to_csv(r"numbers.csv",sep=',',index=None,header=None)