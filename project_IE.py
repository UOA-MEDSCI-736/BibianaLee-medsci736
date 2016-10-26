"""Copyright (c) 2016 Sang Eun Lee
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""
#Python 2.7.12 
#pandas version : u'0.18.1

import pandas as pd
import os
import matplotlib.pyplot as pyplot
from scipy import stats  


##lists of lists contianing various values and labels##
lines = [] #will contain lines from main file after clean up
#list of inputs values 
time = []
aif = []
#list of output values
ktrans_val = []
difcoef_val = []
pixelen_val = []
pixelstd_val = []
aif = []

fileName = ""

# This prints the main menu, and prompts for a choice
def display_welcome_to_project_IE(): 
    print "Welcome to Project IE" #print what options you have
    print "your options are:"
    print " "
    print "1) One file"
    print "2) Quit"
    print " "

#This function asks the user for input and is where the navigation process begins
def ask_for_menu_input():
    user_input = raw_input ("Choose your option: ") #ask the user for an input 1, 2, 3
    print" " #blank line for screen aesthetics 
    expected_user_input = ['1','2'] #These are the expected outputs for the welcome menu
    proceed = check_the_user_input(expected_user_input, user_input) #checks user input
    go_to_chosen_pathway(proceed) #passes user input to function which pipes them to the right function

#This function was taken from Callum Chalmer(2016)- it checks the user input from a list of expected inputs and directs the end-user according to whether or not the input is valid or invalid
def check_the_user_input(expected_user_input, user_input): #takes user input and compares it to a set of expected inputs to ensure the programme runs correctly
    if user_input not in expected_user_input: #if the user_input is not in the list of expected outputs
        return 0 #a zero will be returned
    else: #if user enters an expected input
        return user_input #the user's will be returned 

##This function was added as the the append_values_to_lines function was looping over the data continuously
def run_once(f): #copied from http://stackoverflow.com/questions/4103773/efficient-way-of-having-a-function-only-execute-once-in-a-loop
    def wrapper(*args, **kwargs): #ensures that indicated loops (f) only run once
        if not wrapper.has_run:
            wrapper.has_run = True
            return f(*args, **kwargs)
    wrapper.has_run = False
    return wrapper

##This portion of code tidies and appends values to an empty list from the list of lists at the beginning of the script
def append_values_to_lines(file): #appends lines to lines list after tidying
    for line in file: #reads line by line
        if not line.strip().startswith("#") and not line.strip() == '': #strips anything starting with a # and blank line
            lines.append(line.rstrip().split(",")) #seperates values by the deliminter ','
       
action = run_once(append_values_to_lines) #make sure the append_values_to_lines funtion only runs once

def append_values_to_lists(lines):#append values to corresponding list

    for line in lines: #for every line in the list lines
        str1 = ''.join(line) #covert list to strings

        if str1.find("ktrans") != -1:# if 'ktrans'' is present in string
            ktrans_val.append(line) #append to the list labeled ktrans_val

        elif str1.find("difcoef") != -1: #if 'difcoef'is present in string 
            difcoef_val.append(line) #append to the list labeled difcoef_val

        elif str1.find("enhanc(t)") != -1: #if 'enhanc(t)' present in string 
            pixelen_val.append(line) #append to the list pixelen_val

        elif str1.find("time") != -1: #if 'time'' present in string
            time.append(line) #append to the list time

        elif str1.find("std") != -1: #if 'std' present in string
            pixelstd_val.append(line) #append to the list pixelstd_val

        elif str1.find("aif") != -1: #if 'aif' present in string
            aif.append(line) #append to the list aif
        
        else: 
            break
    ##DATAFRAMES##
    #These are the dataframes - this is how the code manages the data retrieved from the inputted file
    #Each list of labels and values is put through a dataframe in order to properly index it and manage it 

def pandas_aif_df(aif): #function to put aif values through a dataframe
    aif_df = pd.DataFrame((aif), #pass list aif into pandas
                        index = ['aif']) #label index
    aif_df.drop(aif_df[[0]], axis=1, inplace=True) #drop column
    aif_df = aif_df.apply(pd.to_numeric) # converting objects to floats
    aif_df = aif_df.apply(pd.to_numeric) # convert to float 
    return aif_df

def pandas_time_df(time):#function to put time values through a dataframe
    time_df = pd.DataFrame((time), #pass list time into pandas
                        index = ['time(seconds)']) #label index
    time_df.drop(time_df[[0]], axis=1, inplace=True) #drop column
    time_df = time_df.apply(pd.to_numeric) # convert to float 
    return time_df

def pandas_ktrans_df(ktrans_val):#function to put ktrans values through a dataframe
    ##Ktrans Dataframe## 
    ktrans_df = pd.DataFrame((ktrans_val), #pass the list ktrans_val through pandas 
                             columns = ['none', 'Mean','STD','Max','Min']) #label the columns 
    ktrans_df['none'] = ktrans_df['none'].str.split('_') #split the list in the column 'none' by the delimiter ","
    ktrans_df[['none','Ktrans','ID1','ID2']]= ktrans_df['none'].apply(pd.Series) # split the list in none into columns and label them
    ktrans_df = ktrans_df.drop('none', 1) #drop any columns labeled 'none'
    ktrans_df = ktrans_df.set_index(['Ktrans', 'ID1','ID2']) #multi index the new columns 
    ktrans_df = ktrans_df.apply(pd.to_numeric) # converting objects to floats
    return ktrans_df

def pandas_difcoef_df(difcoef_val):#function to put difcoef values through a dataframe
    ##Difcoef Dataframe## 
    difcoef_df = pd.DataFrame((difcoef_val), #pass the list difcoef_val through pandas 
                             columns = ['none', 'Mean','STD','Max','Min'])#label the columns
    difcoef_df['none'] = difcoef_df['none'].str.split('_') #split the list in the column 'none' by the delimiter ","
    difcoef_df[['none','Difcoef','ID1','ID2']]= difcoef_df['none'].apply(pd.Series) # split the list in none into columns and label them
    difcoef_df = difcoef_df.set_index(['Difcoef', 'ID1','ID2']) #drop any columns labeled 'none'
    difcoef_df = difcoef_df.drop('none', 1) #multi index the new columns 
    difcoef_df = difcoef_df.apply(pd.to_numeric) # converting objects to floats
    return difcoef_df

def pandas_pixel_enhancement_df(pixelen_val):#function to put pixel enhancement values through a dataframe
    ##Pixel Enchancement values Dataframe## 
    enhan_df = pd.DataFrame(pixelen_val) #pass the list pixelen_val through pandas
    enhan_df[0] = enhan_df[0].str.split('_') #split the list in the column 'none' by the delimiter ","
    enhan_df[['none','Pixel enhancement Ave','ID1','ID2']]= enhan_df[0].apply(pd.Series) # split the list in none into columns and label them
    enhan_df.drop(enhan_df.columns[[0]], axis=1, inplace=True) #drop column with the index 0 
    enhan_df = enhan_df.set_index(['Pixel enhancement Ave', 'ID1','ID2'])  #multi index the columns
    enhan_df = enhan_df.drop('none', 1) #drop any columns labeled 'none'
    enhan_df = enhan_df.apply(pd.to_numeric) # converting objects to floats
    return enhan_df

def pandas_pixel_enhancement_std(pixelstd_val):#function to put pixel enhancement standard dev values through a dataframe
    ##Pixel Enchancement standard dev Dataframe## 
    std_df = pd.DataFrame(pixelstd_val) #pass the list pixelstd_val through pandas
    std_df[0] = std_df[0].str.split('_') #split the list in the column 'none' by the delimiter ","
    std_df[['none', 'none','Pixel enhancement STD','ID1','ID2']]= std_df[0].apply(pd.Series) # split the list in none into columns and label them
    std_df.drop(std_df.columns[[0]], axis=1, inplace=True) #drop column with the index 0 
    std_df = std_df.set_index(['Pixel enhancement STD', 'ID1','ID2']) #multi index the columns
    std_df = std_df.drop('none', 1) #drop any columns labeled 'none'
    std_df = std_df.apply(pd.to_numeric) # converting objects to floats"""
    return std_df

##Matplot Graph##
#This is the portion of code where data from the pandas frame are sliced and then used as x or y inputs
 ##This portion of the code was modelled after Callum Chalmer(2016)'s code and processes the user input after it has been checked  
def go_to_chosen_pathway(user_input): #directs the user to the relevant function based on their input  
    
    if user_input == 0: #if user input invalid
        print "You have entered an invalid number, please enter either a '1' or '2'"
        ask_for_menu_input() #asks user to re-enter an input
    
    elif user_input == "1": # If the user wants to process just one file 
        file = open(raw_input("Enter Filename: "),'r') #ask user for file name
        fileName = file
        append_values_to_lines(file) #function which cleans up and appends values to list called lines
        append_values_to_lists(lines) #function which appends values to lists
        print(pandas_ktrans_df(ktrans_val) )#call function for ktrans dataframe
        print(pandas_difcoef_df(difcoef_val)) #call function for difcoef dataframe
        print(pandas_pixel_enhancement_df(pixelen_val)) #call pixel enhancement ave dataframe
        print(pandas_pixel_enhancement_std(pixelstd_val)) #call pixel_enhancement standard dev dataframe
        print "Your dataframes have been printed" #once done print this message
        secondary_menu() #call secondary menu which will give the user 4 options

    elif user_input == "2": #quit menu
       quit()

##SECONDARY MENU##
#This section of the code is where the secondary menu starts 
#It prompts the user for for 1 of 4 options 

def display_secondary_menu(): #prints the written portion of the secondary menu
    print "What would you like to do now?"#prints the four options options 
    print " " #blank line for aesthetics
    print "1) visualisation"
    print "2) one-way ANOVA"
    print "3) Back to the main menu"
    print "4) Quit"
    print " "
    
def ask_for_secondary_menu_input():
    secondary_user_input = raw_input ("Choose your option: ") #ask the user for an input 1, 2, 3
    print" " #blank line for screen aesthetics 
    expected_user_input_secondary = ['1','2','3','4'] #These are the expected outputs for the welcome menu
    proceed = check_the_user_input_secondarymenu(expected_user_input_secondary, secondary_user_input) #checks user input
    go_to_chosen_pathway_secondarymenu(proceed) #passes user input to function which pipes them to the right function

def check_the_user_input_secondarymenu(expected_user_input_secondary, secondary_user_input): #takes user input and compares it to a set of expected inputs to ensure the programme runs correctly
    if secondary_user_input not in expected_user_input_secondary: #if the user_input is not in the list of expected outputs
        return 0 #a zero will be returned
    else: #if user enters an expected input
        return secondary_user_input #the user's will be returned 
    
def go_to_chosen_pathway_secondarymenu(secondary_user_input): #directs the user to the relevant function based on their input  
    if secondary_user_input == 0: #if user input invalid
        secondary_menu()

    elif secondary_user_input == "1": # If the user wants to process just one file 
        plot_enhancement_df_vs_time()
        secondary_menu()

    elif secondary_user_input == "2": #If the user wants to process multiple files
        one_way_anova_enhan_aves(pandas_pixel_enhancement_df(pixelen_val))
        secondary_menu()

    elif secondary_user_input == "3": #If the user wants to process multiple files  
        menu()
    else:
        quit()

def secondary_menu ():
    display_secondary_menu()
    ask_for_secondary_menu_input()

def setting_y_values(pixelEnhanceDf, timedf):
    max_column_no = len(timedf.columns) - 1
    y_data = pixelEnhanceDf.loc['enhanc(t)','294', '0'][0:max_column_no]
    return y_data

def setting_x_values(timeDf):
    max_column_no = len(timeDf.columns) - 1
    x_data = timeDf.loc['time(seconds)',1:max_column_no]
    return x_data

def plot_enhancement_df_vs_time():
    x_data = setting_x_values(pandas_time_df(time))
    y_data = setting_y_values(pandas_pixel_enhancement_df(pixelen_val), pandas_time_df(time))
    pyplot.style.use('ggplot')
    pyplot.title('Pixel Enhancement Average vs. Time (Seconds)')
    pyplot.xlabel('Time (Seconds)')
    pyplot.ylabel('Pixel Enchancement Average')
    pyplot.axvline(x=0, color='blue')
    pyplot.plot(x_data, y_data)
    pyplot.savefig(fileName)

def one_way_anova_enhan_aves(pixelEnhanceDf):
    height0 = pixelEnhanceDf.loc['enhanc(t)','294','0']
    height1 = pixelEnhanceDf.loc['enhanc(t)','294','1']
    height2 = pixelEnhanceDf.loc['enhanc(t)','294','2']      
    f_val, p_val = stats.f_oneway(height0, height1, height2)   
    print "One-way ANOVA P =", p_val    

def menu():
    display_welcome_to_project_IE() #prints the welcome message 
    ask_for_menu_input() #asks for user input and then processes it 

menu()# runs the programm
