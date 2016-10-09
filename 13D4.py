
# coding: utf-8

# In[13]:

#Python 2.7.12 
#pandas version : u'0.18.1

##This script contains the main parse code for the file 13D4## 
#This script extracts lines and passes them through pandas for statistical analysis

import pandas as pd
import numpy as np


lines = [] #open a new list called "lines"

with open("13D4") as file: #open 13D4 and name it file 
    for line in file: #for every line in files 
        if not line.strip().startswith("#") and not line.strip() == '': #take out lines starting with '#' and any blank lines
             lines.append(line.rstrip().split(",")) #split the lines at the delimiter ',' and append the lines to the list 'lines' 

                
##Lists for Inputs##
time = []
aif = []
                
##Lists for Ouputs##                
ktrans_val = []
difcoef_val = []
pixelen_val = []
pixelstd_val = []

##extracting lines ##
for line in lines: # for lines in the list lines
    str1 = ''.join(line) #make the lines strings
    
##extracting Inputs##
    if str1.find("aif") != -1: #if the string has the word 'aif' extract it 
        aif.append(line) #append it to the corresponding list
        
    elif str1.find("time") != -1:#if the string has the word 'time' extract it 
        time.append(line) #append it to the corresponding list
        
##extracting Outputs## 
    elif str1.find("ktrans") != -1: #if the string has the word 'ktrans' extract it 
            ktrans_val.append(line)  #append it to the corresponding list - ktrans_val
    
    elif str1.find("difcoef") != -1: #if the string has the word 'difcoef' extract it 
        difcoef_val.append(line)  #append it to the corresponding list  - difcoef_val
        
    elif str1.find("enhanc(t)") != -1:#if the string has the word 'enhanc(t)' extract it 
        pixelen_val.append(line) #append it to the corresponding list - piexelen_val
    
 
    elif str1.find("std") != -1:#if the string has the word 'stf' extract it 
        pixelstd_val.append(line)  #append it to the corresponding list - pixelstd_val



# In[9]:

##passing the lists through a pandas dataframe for visualisation and analysis##

##INPUTS##
#aif 
aif_df = pd.DataFrame((aif), #pass list aif into pandas
                    index = ['aif']) #label index
aif_df.drop(aif_df[[0]], axis=1, inplace=True) #drop column

#Time
time_df = pd.DataFrame((time), #pass list time into pandas
                    index = ['time (seconds)']) #label index
time_df.drop(time_df[[0]], axis=1, inplace=True) #drop column


##OUTPUTS## 

##Ktrans Dataframe## 
ktrans_df = pd.DataFrame((ktrans_val), #pass the list ktrans_val through pandas 
                         columns = ['none', 'Mean','STD','Max','Min']) #label the columns 
ktrans_df['none'] = ktrans_df['none'].str.split('_') #split the list in the column 'none' by the delimiter ","
ktrans_df[['none','Ktrans','ID1','ID2']]= ktrans_df['none'].apply(pd.Series) # split the list in none into columns and label them
ktrans_df = ktrans_df.drop('none', 1) #drop any columns labeled 'none'
ktrans_df = ktrans_df.set_index(['Ktrans', 'ID1','ID2']) #multi index the new columns 

##Difcoef Dataframe## 
difcoef_df = pd.DataFrame((difcoef_val), #pass the list difcoef_val through pandas 
                         columns = ['none', 'Mean','STD','Max','Min'])#label the columns
difcoef_df['none'] = difcoef_df['none'].str.split('_') #split the list in the column 'none' by the delimiter ","
difcoef_df[['none','Difcoef','ID1','ID2']]= difcoef_df['none'].apply(pd.Series) # split the list in none into columns and label them
difcoef_df = difcoef_df.set_index(['Difcoef', 'ID1','ID2']) #drop any columns labeled 'none'
difcoef_df = difcoef_df.drop('none', 1) #multi index the new columns 

##Pixel Enchancement values Dataframe## 
ehan_df = pd.DataFrame(pixelen_val) #pass the list pixelen_val through pandas
ehan_df[0] = ehan_df[0].str.split('_') #split the list in the column 'none' by the delimiter ","
ehan_df[['none','Pixel enhancement Ave','ID1','ID2']]= ehan_df[0].apply(pd.Series) # split the list in none into columns and label them
ehan_df.drop(ehan_df.columns[[0]], axis=1, inplace=True) #drop column with the index 0 
ehan_df = ehan_df.set_index(['Pixel enhancement Ave', 'ID1','ID2'])  #multi index the columns
ehan_df = ehan_df.drop('none', 1) #drop any columns labeled 'none'

##Pixel Enchancement standard dev Dataframe## 
std_df = pd.DataFrame(pixelstd_val) #pass the list pixelstd_val through pandas
std_df[0] = std_df[0].str.split('_') #split the list in the column 'none' by the delimiter ","
std_df[['none', 'none','Pixel enhancement STD','ID1','ID2']]= std_df[0].apply(pd.Series) # split the list in none into columns and label them
std_df.drop(std_df.columns[[0]], axis=1, inplace=True) #drop column with the index 0 
std_df = std_df.set_index(['Pixel enhancement STD', 'ID1','ID2']) #multi index the columns
std_df = std_df.drop('none', 1) #drop any columns labeled 'none'


# In[11]:

##Extacting specific values from pandas dataframe##
#dataframe name.loc[multi index names][column name or index] e.g. 
ktrans_df.loc['ktrans','294','0':]['Mean'] #extracting specific values from the dataframes




