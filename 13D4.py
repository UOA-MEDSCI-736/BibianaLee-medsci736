
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np

with open("13D4") as file:
    lines = []
    for line in file:
        if not line.strip().startswith("#") and not line.strip() == '':
             lines.append(line.rstrip().split(","))
                
df = pd.DataFrame(lines)  
df[1] = pd.to_numeric(df[1]) #wtf <-look at lambda function from lec
df[2] = pd.to_numeric(df[2])
df[3] = pd.to_numeric(df[3])
df[4] = pd.to_numeric(df[4])
df[5] = pd.to_numeric(df[5])
df[6] = pd.to_numeric(df[6])
df[7] = pd.to_numeric(df[7])
df[8] = pd.to_numeric(df[8])
df[9] = pd.to_numeric(df[9])
df[10] = pd.to_numeric(df[10])
df[11] = pd.to_numeric(df[11])
df[12] = pd.to_numeric(df[12])
df[13] = pd.to_numeric(df[13])

ktrans = [df[2:10],df[18:26]] #getting Ktrans rows - probably not the best way to do this...
result = pd.concat(ktrans) #merging them
result = result.drop(result.columns[5:14], axis=1) # drop the nones 
result[0] = result[0].str.split('_') #split list in index0
result[['Remove','Ktrans','ID1','ID2']]= result[0].apply(pd.Series) #make list columns
result.drop(result.columns[[0]], axis=1, inplace=True) #drop the original one
df2= result.set_index(['Ktrans', 'ID1','ID2']) #multiindex it 
df2.columns = ['Mean','STD','Max','Min','what'] #columns be renames with the random thing i should get rid of
yo = df2.drop(df2.columns[[4]], axis=1, inplace=True) #random column removed 

difcoef = df[34:50] #getting difcoef rows - probably not the best way to do this...
result1 = difcoef.drop(difcoef.columns[5:14], axis=1) # drop the nones
result1[0] = result1[0].str.split('_') #split list in index0
result1[['Remove','Difcoef','ID1','ID2']]= result1[0].apply(pd.Series) #make list columns
result1.drop(result1.columns[[0]], axis=1, inplace=True) #drop the original one
df3= result1.set_index(['Difcoef', 'ID1','ID2']) #multiindex it 
df3.columns = ['Mean','STD','Max','Min','what'] #columns be renamed with the random thing i should get rid of
yo2 = df3.drop(df3.columns[[4]], axis=1, inplace=True) #random column removed 

enhan = [df[10:18],df[26:34]] #getting Ktrans rows - probably not the best way to do this...
result2 = pd.concat(enhan) #merging them
result2 = result2.drop(result2.columns[13], axis=1) # drop the nones 
result2[0] = result2[0].str.split('_') #split list in index0
result2[['Remove','Pixel enhancement Ave','ID1','ID2']]= result2[0].apply(pd.Series) #make list columns
result2.drop(result2.columns[[0]], axis=1, inplace=True) #drop the original one
df4 = result2.set_index(['Pixel enhancement Ave', 'ID1','ID2']) #multiindex it 
df4.columns = ['enhancement1', 'enhancement2','enhancement3','enhancement4','enhancement5', 'enhancement6', 'enhancement7', 'enhancement8', 'enhancement9', 'enhancement10', 'enhancement11', 'enhancementT','what']
yo3 = df4.drop(df4.columns[[12]], axis=1, inplace=True) #random column removed 

enhan1 = df[50:66]
result3 = enhan1.drop(enhan1.columns[13], axis=1) # drop the nones
result3[0] = result3[0].str.split('_') #split list in index0
df5 = result3[['remove','Remove','Pixel enhancement std','ID1','ID2']]= result3[0].apply(pd.Series) #make list columns
result3.drop(result3.columns[[0]], axis=1, inplace=True) #drop the original one
df5 = result3.set_index(['Pixel enhancement std', 'ID1','ID2']) #multiindex it 
df5.columns = ['enhancement1', 'enhancement2','enhancement3','enhancement4','enhancement5', 'enhancement6', 'enhancement7', 'enhancement8', 'enhancement9', 'enhancement10', 'enhancement11', 'enhancementT','what','what']
df5 = df5.drop(df5.columns[12:13], axis=1) 

print df2

print df3

print df4

print df5

#How to slice data: df#.loc['index1','index2','index3']['column']
df2.loc['ktrans','294','0':]['Mean'] 
# In[ ]:



