"""Copyright (c) 2016 Sang Eun Lee
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE."""
#Python 2.7.12 
#pandas version : u'0.18.1
#matplotlib 1.5.3 
#SciPy 0.18.1

import pandas as pd 
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


# This prints the main menu, and prompts for a choice
def display_welcome_to_project_IE(): 
    print "Welcome to Project IE" #print what options you have
    print "your options are:"
    print " "
    print "1) One file" #process one file 
    print "2) Quit" #quit the programme 
    print " "
  

#This function asks the user for input and is where the navigation process begins
#Code pathway modelled from Callum Chalmer (2016) MIT license
#    Title: ePygenetics
#    Author: Callum Chalmer
#    Date: 2016
#    Code version: 1
#    Availability:https://github.com/UOA-MEDSCI-736/CallumChalmers29-crispy-disco

def ask_for_menu_input():
    user_input = raw_input ("Choose your option: ") #asks the user for an input -> they can choose between 1 or 2 
    print" " #blank line for screen aesthetics 
    expected_user_input = ['1','2'] #These are the expected inputs for the welcome menu
    proceed = check_the_user_input(expected_user_input, user_input) # Function which checks the user_input, it ensures that the values are valid
    go_to_chosen_pathway(proceed) #
    
def check_the_user_input(expected_user_input, user_input): #takes user input and compares it to a set of expected inputs to ensure the programme runs correctly
    if user_input not in expected_user_input: #if the user_input is not in the list of expected inputs 
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
########################################################
# NEED TO REMOVE '#' FROM 'return lines' WHEN TESTING #
#######################################################

##This portion of code tidies and appends values to an empty list from the list of lists at the beginning of the script
def append_values_to_lines(file): #appends lines to lines list after tidying
    for line in file: #reads line by line
        if not line.strip().startswith("#") and not line.strip() == '': #strips anything starting with a # and blank line
            lines.append(line.rstrip().split(",")) #seperates values by the deliminter ','
            #return lines

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
action = run_once(append_values_to_lines(lines)) #make sure the append_values_to_lines funtion only runs once
 
    ##DATAFRAMES##
    #These are the dataframes - this is how the code manages the data retrieved from the input file
    #Each list of labels and values is put through a dataframe in order to properly index it and manage it 

def pandas_aif_df(aif): #function to put aif values through a dataframe
    aif_df = pd.DataFrame((aif), #pass list aif into pandas
                        index = ['aif']) #label index
    aif_df.drop(aif_df[[0]], axis=1, inplace=True) #drop column
    aif_df = aif_df.apply(pd.to_numeric) # converting objects to floats
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

##Chosen path way loop ##
def go_to_chosen_pathway(user_input): #directs the user to the relevant function based on their input  
    
    if user_input == 0: #if user input invalid
        print "You have entered an invalid number, please enter either a '1' or '2'"
        ask_for_menu_input() #asks user to re-enter an input
    
    elif user_input == "1": # If the user wants to process just one file 
        try: # this is how the script handles a bad file - if the file is not in the same folder as the script it will not run and display the "except:" error message
            file = open(raw_input("Enter Filename: "),'r') #ask user for file name
            append_values_to_lines(file) #function which cleans up and appends values to list called lines
            append_values_to_lists(lines) #function which appends values to lists
            print "" #blank line for aesthetics
            print "---------------------------------------------------" # line to indicate a new DataFrame
            print "Your Ktrans DataFrame"
            print "---------------------------------------------------" # line to indicate a new DataFrame
            print(pandas_ktrans_df(ktrans_val) )#call function for ktrans dataframe
            print "" #blank line for aesthetics
            print "---------------------------------------------------"# line to indicate a new DataFrame
            print "Your dicoef DataFrame"
            print "---------------------------------------------------"# line to indicate a new DataFrame
            print(pandas_difcoef_df(difcoef_val)) #call function for difcoef dataframe
            print "" #blank line for aesthetics
            print "---------------------------------------------------"# line to indicate a new DataFrame
            print "Your Pixel Enchancement Averages DataFrame"
            print "---------------------------------------------------"# line to indicate a new DataFrame
            print(pandas_pixel_enhancement_df(pixelen_val)) #call pixel enhancement ave dataframe
            print "" #blank line for aesthetics
            print "---------------------------------------------------"# line to indicate a new DataFrame
            print "Your Pixel Enhancement SD DataFrame"
            print "---------------------------------------------------"# line to indicate a new DataFrame
            print(pandas_pixel_enhancement_std(pixelstd_val)) #call pixel_enhancement standard dev dataframe
            print "" #blank line for aesthetics
            print "---------------------------------------------------"# line to indicate a new DataFrame
            print "Your dataframes have been printed" #once done print this message
            print "---------------------------------------------------"# line to indicate a new DataFrame
            print "You may choose another option now"
            print "" #blank line for aesthetics
            secondary_menu() #call secondary menu which will give the user 3 options

        except IOError: #if an error occurs due to an unreadable file, the script will print the following message
            print "" #blank line for aesthetics
            print ""#blank line for aesthetics
            print "*****" # a line to bring attention to the message 
            print ""#blank line for aesthetics
            print "COULD NOT READ FILE"
            print "Please check again or read the README"
            print "Remember the script and the file have to be in SAME FOLDER"
            print ""#blank line for aesthetics
            print "******"  # a line to bring attention to the message 
            print""#blank line for aesthetics
            print "You may choose again or you may quit"
            print "" #blank line for aesthetics
            display_welcome_to_project_IE() #takes you back to the main menu where you can choose to input a valid file or exit the programme
            ask_for_menu_input() #where the input goes 
        

    elif user_input == "2": #quit menu
       quit()


##SECONDARY MENU##
#This section of the code is where the secondary menu starts 
#It prompts the user for for 1 of 3 options 

def display_secondary_menu(): #prints the written portion of the secondary menu
    print "What would you like to do now?"#prints the four options options 
    print " " #blank line for aesthetics
    print "1) visualisation"
    print "2) one-way ANOVA"
    print "3) Quit"
    print " "
#again these pathways are very similar to the main menu ones they simply take an input and compare it against an expected input list. If the user inputted value is present in the list then the scrip will call another function and then move into a loop 
def ask_for_secondary_menu_input(): 
    secondary_user_input = raw_input ("Choose your option: ") #ask the user for an input 1, 2, 3
    print" " #blank line for screen aesthetics 
    expected_user_input_secondary = ['1','2','3'] #These are the expected outputs for the welcome menu
    proceed = check_the_user_input_secondarymenu(expected_user_input_secondary, secondary_user_input) #checks user input
    go_to_chosen_pathway_secondarymenu(proceed) #passes user input to function which pipes them to the right function

def check_the_user_input_secondarymenu(expected_user_input_secondary, secondary_user_input): #takes user input and compares it to a set of expected inputs to ensure the programme runs correctly
    if secondary_user_input not in expected_user_input_secondary: #if the user_input is not in the list of expected inputs
        return 0 #a zero will be returned
    else: #if user enters an expected input
        return secondary_user_input #the user's will be returned 
    
def go_to_chosen_pathway_secondarymenu(secondary_user_input): #directs the user to the relevant function based on their input  
    if secondary_user_input == 0: #if user input invalid
        print "The number you have entered is invalid please choose either option 1, 2 or 3" #prints this message to say you entered a invalid number
        secondary_menu() #takes you back to the secondary menu

    elif secondary_user_input == "1": # If the user wants to process just one file 
        plot_enhancement_df_vs_time() #calls function to plot graph enhancement df vs time 
        print "Your graph has been plotted and saved."
        print ""
        print "You may choose another option now"
        print ""
        secondary_menu() #takes you back to the secondary menu again

    elif secondary_user_input == "2": #this will put some of the data through a ANOVA analysis for demonstrative purposes 
        one_way_anova_enhan_aves(pandas_pixel_enhancement_df(pixelen_val)) # take you to 
        secondary_menu() #will call the secondary menu once this is done so that the user can do something else 

    else:
        quit() #quit the programme 

def secondary_menu ():
    display_secondary_menu() #will display the secondary menu message 
    ask_for_secondary_menu_input() #ask the user for input - one of three options - graphing, ANOVA or quit 

def setting_y_values(pixelEnhanceDf, timedf): #getting y value for the plotting 
    max_column_no = len(timedf.columns) - 1 #this is to ensure that all values are of the same length - again because this is for demonstrative purposes this practice is permissable if the user wishese to actually do something they must edit it 
    y_data = pixelEnhanceDf.loc['enhanc(t)','294', '0'][0:max_column_no] #assign the values to the variable y_dat 
    return y_data #return this <- not tested for as the DataFames make it hard 

def setting_x_values(timeDf): #getting x value for plotting 
    max_column_no = len(timeDf.columns) - 1 #ensure that there are the same no. of values in both dataframes 
    x_data = timeDf.loc['time(seconds)',1:max_column_no] #assigns values to variable 
    return x_data #return x_data when complete 
#Using matplot to graph pixel enhancement ave vs time 
#using the ggplot style 
def plot_enhancement_df_vs_time():#funtion to plot 
    
    x_data = setting_x_values(pandas_time_df(time)) #calling function for setting x 
    y_data = setting_y_values(pandas_pixel_enhancement_df(pixelen_val), pandas_time_df(time)) #calling funtion for setting y 
    pyplot.style.use('ggplot') #plot style <- this can be edited to a different style
    pyplot.title('Pixel Enhancement Average vs. Time (Seconds)') #adding title of graph
    pyplot.xlabel('Time (Seconds)') #adding x label 
    pyplot.ylabel('Pixel Enchancement Average') #adding y label
    pyplot.axvline(x=0, color='blue') #color of line
    pyplot.plot(x_data, y_data) #calling the x and y values 
    pyplot.savefig("Your_Graph") #save as an image in folder

def one_way_anova_enhan_aves(pixelEnhanceDf): #this function collects and assigns the values to a variable after slicing from the Dataframe
    height0 = pixelEnhanceDf.loc['enhanc(t)','294','0']#height 0 of the GP cochlear 
    height1 = pixelEnhanceDf.loc['enhanc(t)','294','1']#height 1 of the GP cochlear 
    height2 = pixelEnhanceDf.loc['enhanc(t)','294','2']#height 2 of the GP cochlear    
    f_val, p_val = stats.f_oneway(height0, height1, height2)   
    print "___________________________________________________" #This is how the ANOVA is shown on command line as an output 
    print "ANOVA"
    print "___________________________________________________"
    print ""
    print "One-way ANOVA P =", p_val    #it will print the pvalue here 
    print ""
    if p_val < 0.05: #this will interpret the pvalue and print a message saying that it is significant and then follow this up with a final feedback so that the user knows that the code has ended 
        print ""
        print ""
        print "The differences between some of the means are statistically significant"
        print ""
        print ""
        print "Your analysis is complete."
        print "___________________________________________________"
        print ""
        print "You may choose another option now."
        print ""
        print ""
    else: #if it is not significant it will print that it is not and then follow this up with a message saying that the analysis is complete so that the user knows the script has ended 
        print ""
        print ""
        print "The differences between the means are not statistically significant "
        print ""
        print ""
        print "Your analysis is complete."
        print "___________________________________________________"
        print ""
        print "You may choose another option now."
        print ""
        print ""
def menu():
    display_welcome_to_project_IE() #prints the welcome message 
    ask_for_menu_input() #asks for user input and then processes it 
### NEED TO #MENU() OR REMOVE IT WHEN TESTING###
menu()# runs the programm 
