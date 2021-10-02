import math

import pandas as pd
df = pd.read_csv("products.csv",encoding = "ISO-8859-1", engine='python')
slicing = math.ceil(len(df)/200)
max = 0
for i in range(slicing):
    print(i)
    max = (i+1)*200
    newdf = df.loc[i*200:max,:]
    newdf.to_excel("products_{}.xlsx".format(i),columns=df.columns)