
# coding: utf-8
import pandas as pd
import glob

# This prints the main menu, and prompts for a choice
def menu(): 
#print what options you have
    print "Welcome"
    print "your options are:"
    print " "
    print "1) One file"
    print "2) Multiple files"
    print "3) Quit"
    print " "
    return raw_input ("Choose your option: ")

def visulisation_menu():
    print "Would you like a visualisation?"
    print " "
    print "1) Yes"
    print "2) No"
    print " "
    return raw_input ("Choose your option: ")

    loop = 1
    choice = 0
    while loop == 1:
        choice = process_one_file_menu()
        if choice == 1:
            pass
        elif choice == 2:
            loop = 0
        else:
            print "whut"

   
    ktrans_val = []
    time = []
    aif = []
    difcoef_val = []
    pixelen_val = []
    pixelstd_val = []
    aif = []
    lines = []

def run_once(f):
        def wrapper(*args, **kwargs):
            if not wrapper.has_run:
                wrapper.has_run = True
                return f(*args, **kwargs)
        wrapper.has_run = False
        return wrapper

action = run_once(append_values_to_lines)

def append_values_to_lines(file):
        for line in file:
            if not line.strip().startswith("#") and not line.strip() == '':
                lines.append(line.rstrip().split(","))
           

def append_values_to_lists(lines):
        for line in lines:
            str1 = ''.join(line)

            if str1.find("ktrans") != -1:
                ktrans_val.append(line)

            elif str1.find("difcoef") != -1:
                difcoef_val.append(line)

            elif str1.find("enhanc(t)") != -1:
                pixelen_val.append(line)

            elif str1.find("time") != -1:
                time.append(line)

            elif str1.find("std") != -1:
                pixelstd_val.append(line)

            elif str1.find("aif") != -1:
                aif.append(line)
            
def pandas_aif_df(aif):
        aif_df = pd.DataFrame((aif), #pass list aif into pandas
                            index = ['aif']) #label index
        aif_df.drop(aif_df[[0]], axis=1, inplace=True) #drop column
        aif_df = aif_df.apply(pd.to_numeric) # converting objects to floats
        print aif_df
        
def pandas_time_df(time):
        time_df = pd.DataFrame((time), #pass list time into pandas
                            index = ['time (seconds)']) #label index
        time_df.drop(time_df[[0]], axis=1, inplace=True) #drop column
        print time_df


def pandas_ktrans_df(ktrans_val):
        ##Ktrans Dataframe## 
        ktrans_df = pd.DataFrame((ktrans_val), #pass the list ktrans_val through pandas 
                                 columns = ['none', 'Mean','STD','Max','Min']) #label the columns 
        ktrans_df['none'] = ktrans_df['none'].str.split('_') #split the list in the column 'none' by the delimiter ","
        ktrans_df[['none','Ktrans','ID1','ID2']]= ktrans_df['none'].apply(pd.Series) # split the list in none into columns and label them
        ktrans_df = ktrans_df.drop('none', 1) #drop any columns labeled 'none'
        ktrans_df = ktrans_df.set_index(['Ktrans', 'ID1','ID2']) #multi index the new columns 
        ktrans_df = ktrans_df.apply(pd.to_numeric) # converting objects to floats
        print ktrans_df

def pandas_difcoef_df(difcoef_val):
        ##Difcoef Dataframe## 
        difcoef_df = pd.DataFrame((difcoef_val), #pass the list difcoef_val through pandas 
                                 columns = ['none', 'Mean','STD','Max','Min'])#label the columns
        difcoef_df['none'] = difcoef_df['none'].str.split('_') #split the list in the column 'none' by the delimiter ","
        difcoef_df[['none','Difcoef','ID1','ID2']]= difcoef_df['none'].apply(pd.Series) # split the list in none into columns and label them
        difcoef_df = difcoef_df.set_index(['Difcoef', 'ID1','ID2']) #drop any columns labeled 'none'
        difcoef_df = difcoef_df.drop('none', 1) #multi index the new columns 
        difcoef_df = difcoef_df.apply(pd.to_numeric) # converting objects to floats
        print difcoef_df

def pandas_pixel_enhancement_df(pixelen_val):
        ##Pixel Enchancement values Dataframe## 
        enhan_df = pd.DataFrame(pixelen_val) #pass the list pixelen_val through pandas
        enhan_df[0] = enhan_df[0].str.split('_') #split the list in the column 'none' by the delimiter ","
        enhan_df[['none','Pixel enhancement Ave','ID1','ID2']]= enhan_df[0].apply(pd.Series) # split the list in none into columns and label them
        enhan_df.drop(enhan_df.columns[[0]], axis=1, inplace=True) #drop column with the index 0 
        enhan_df = enhan_df.set_index(['Pixel enhancement Ave', 'ID1','ID2'])  #multi index the columns
        enhan_df = enhan_df.drop('none', 1) #drop any columns labeled 'none'
        enhan_df = enhan_df.apply(pd.to_numeric) # converting objects to floats
        print enhan_df
    
def pandas_pixel_enhancement_std(pixelstd_val):
        ##Pixel Enchancement standard dev Dataframe## 
        std_df = pd.DataFrame(pixelstd_val) #pass the list pixelstd_val through pandas
        std_df[0] = std_df[0].str.split('_') #split the list in the column 'none' by the delimiter ","
        std_df[['none', 'none','Pixel enhancement STD','ID1','ID2']]= std_df[0].apply(pd.Series) # split the list in none into columns and label them
        std_df.drop(std_df.columns[[0]], axis=1, inplace=True) #drop column with the index 0 
        std_df = std_df.set_index(['Pixel enhancement STD', 'ID1','ID2']) #multi index the columns
        std_df = std_df.drop('none', 1) #drop any columns labeled 'none'
        std_df = std_df.apply(pd.to_numeric) # converting objects to floats"""
        print std_df


def mapping (): 
     print "What would you like graphed"
        print "your options are:"
        print " "
        print "1) Pixel enchancement Ave"
        print "2) Pixel enhancement STD"
        print "3) Quit"
        print " "
        return raw_input ("Choose your option: ")

def visualisation (): 
    
        pyplot.plot(x_data, y_data)
        pyplot.show()
        time_df = x_data

loop = 1
choice = 0
while loop == 1:
    choice = menu()
    if choice == 1:
        file = open(raw_input("Enter Filename: "),'r')
        append_values_to_lines(file)
        append_values_to_lists(lines)
        pandas_ktrans_df(ktrans_val)
        pandas_difcoef_df(difcoef_val)
        pandas_pixel_enhancement_df(pixelen_val)        
        pandas_pixel_enhancement_std(pixelstd_val)
        print "Your Dataframes have been printed"
        mapping()
    elif choice == 2:
        pass
    
    elif choice == 3:
        print "----END----"
        loop = 0
