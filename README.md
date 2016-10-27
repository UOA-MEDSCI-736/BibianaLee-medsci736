# Project IE
Project IE is a python supported module which parses, stores and analyses cochlear MRI data from text files. This prototype currently allows the user to input one raw file at a time to be tidied and passed through [pandas](http://pandas.pydata.org/) DataFrame for easy data management. The resulting DataFrames also enable further processing in the form of a one-way ANOVA analysis or can alternatively output a graph which is then saved as an image (.png). 

Visualisation (graphing) was achieved using a plotting library called [matplotlib](http://matplotlib.org/) and the one-way ANOVA analysis was completed using the [SciPy library](https://www.scipy.org/)

## Project Description

This study looks to quantify spatial and temporal inflammation-induced changes in the capsular permeability and macrophage infiltration in guinea-pig cochlea using MRI. Modelling of such exchanges in blood and different inner ear (IE) compartments require the analysis of a substantial amount of data. 

These data have been extracted from a set of MRI which measures the propagation of a contrast agent injected into the IE. This project aims to investigate the parsing of this data and statistical analysis of these results. 

This project could provide reference data that can in future be used to quantitatively assess the treatment of ear disease in animal models and establish a platform from which such techniques can be transferred into clinical practice. 

##Contributors

1. Bibiana Lee
2. Kreshnik Pireva
3. Callum Chalmers

## Prerequisities

1. **Python**
   - Successful running of this programme will require Python 2.7.12
   - You can download Python 2.7.12 following [This link ](https://www.python.org/downloads/release/python-2712/)  
   - Alternatively, you may alter the script to fit your version of Python

2. **Operating System**
  - Ubuntu 16.04 LTS 


##Data File Requirements

 - Data Files must be text files (.txt)
 - Files should be labeled like this: **(no.of images)D(no.days after treatment or non-treatment)**
 - So the name should contain **a number** followed by a **D** then another **number**
 - For example: a file labeled **13D4** is an animal that has been imaged 13 times, 4 days after treatment 
 
 ###Labels 
 - The data file must contain the following labels. **This is a must**
 - The Ktrans and Diffusion coefficient labels must be followed by four numbers 
 - ID1 can be either 294 (Right ear) or 295 (Left ear) 
 - ID2 is the height of the cochlear anatomy and ranges from 0 - 7 
 
      ```
      ## INPUTS ##

      # arterial input function values
      aif:

      # time after fixed capture, in second
      time:
      
      ## OUTPUTS ##
      **k trans value, average value, std value, max and minimal values**
      local-cochlea-bm.ktrans_ID1_ID2:val_mean,val_std,val_max,val_min
      
      **Pixel enhancement average value along the time**
      local-cochlea-bm.enhan(t)_ID1_ID2:enhancement1,...
      
      **Pixel enhancement std value along the time**
      local-cochlea-bm.std_enh(t)_ID1_ID2:std_enhancement1,...
      
      **Diffusion coefficient, average value, std value, maximal and minimal values**
      local-cochlea-bm.difcoef_ID1_ID2:coef_mean,coef_std,coef_max,coef_min
      
      ```
   **Example Raw Data** 
   
   `aif,0,0.914,1.115,1.235,1.225,1.218,1.122,1.106,1.192,1.017,1.214`
   
   `time,0,120,220,320,420,520,620,820,920,1120,1220`
   
   `local-cochlea-bm.mha_ktrans_294_0,0.0123,0.0025,0.0326,0.00425`
   
   `local-cochlea-bm.mha_enhanc(t)_294_0,3.926,5.013,4.329,4.426,5.036,4.627,4.858,3.364,4.764,4.247`
   
   `local-cochlea-bm.mha_std_enh(t)_294_0,2.015,2.706,2.263,2.251,2.696,2.342,2.487,1.985,2.219,2.405`
   
   `local-cochlea-bm.mha_difcoef_294_0,0.0123,0.0025,0.0326,0.00425`
   
##Running the programme using the test data
###Loading project_IE.py
1) Download the test_Project_IE folder and transfer the project_IE.py
2) Open a command line terminal in the folder containing project_IE.py
 
3) Type in python project_IE.py in the command window 
4) Once this is complete you should be greeted with the first menu 

   ```
   Welcome to Project IE
   your options are:

   1) One file
   2) Quit

   Choose your option:
   ```
   **If you would like to exit the programme you can type `2` otherwise keep reading the instructions**
   
###Loading dummy data 
1. Type `1`
 - If you enter an invalid number a message will appear saying 
   
   `The number you have entered is invalid please choose either option 1 or 2 `
   
2. Type in `10D4`
   - Your DataFrames should print now this should be followed by a message that reads: 

   ```
   Your graph has been plotted and saved
   
   You may choose another option now
   
   ```
3. The secondary  menu should greet you now
   ```
   What would you like to do now?
 
   1) visualisation
   2) one-way ANOVA
   3) Quit
   
   Choose your option: 
   ```

###Visualisation 
1. Type `1` for a visualization
2. A graph should automatically save in your folder called `Your Graph`
3. A new message will appear 
   ```
   Your graph has been plotted and saved.
   
   You may choose another option now.
   ```
4. Once this is complete you will be greeted by the secondary menu again 

### one-way ANOVA 
1. Type `2` for a one-way ANOVA
2. A message should appear saying: 
   `One-way ANOVA followed by your P value` 
3. An interpretation of your p-value should this output 
      - If it is significant (p-value <0.05)
      
      ```
      The differences between some of the means are statistically significant
     
      Your analysis is complete.

      You may choose another option now.
      ```
      - If it is not significant (p-value >0.05)
      
      ```
      The differences between the means are not statistically significant
     
      Your analysis is complete.

      You may choose another option now.
      ```
 
   **Once complete you can now exit the programme by typing `3`**
   
## Expected Output for Dummy Data

### DataFrames 
- The expected output for the dummy data should look like this for the Ktrans DataFrame 
- A seperate text filed called `10D4_expected_output.txt` can be found in the test folder to compare your results 

   ```
   ---------------------------------------------------
   Your Ktrans DataFrame
   ---------------------------------------------------
                     Mean      STD     Max      Min
   Ktrans ID1 ID2                                  
   ktrans 294 0    0.0123  0.00250  0.0326  0.00425
              1    0.0115  0.00450  0.0224  0.00354
              2    0.0121  0.00740  0.0422  0.00228
              3    0.0098  0.00470  0.0253  0.00177
              4    0.0187  0.00520  0.0309  0.00326
              5    0.0121  0.00290  0.0468  0.00292
              6    0.0073  0.00320  0.0103  0.00865
              7    0.0041  0.00250  0.0276  0.00342
          295 0    0.0123  0.00125  0.0326  0.00425
              1    0.0118  0.00664  0.0133  0.00242
              2    0.5411  0.00896  0.0505  0.00601
              3    0.8471  0.00843  0.0554  0.00808
              4    0.0676  0.01116  0.0939  0.00162
              5    0.0199  0.00763  0.0045  0.00496
              6    0.0131  0.00923  0.0889  0.00411
              7    0.0024  0.00616  0.0385  0.00315
   ```

### Graph 
The expected graph output can be found in the test folder and is called `Your_Graph_10D4.png`

###one-way ANOVA 
- The expected output for the dummy data should look like this: 

   ```
   ___________________________________________________

   One-way ANOVA P = 0.562677075784



   The differences between the means are not statistically significant 


   Your analysis is complete.
   ___________________________________________________

   You may choose another option now.
   ```
   
##Limitations 
   - The analysis and graph produced are for demonstrative purposes only. **This is a prototype**.
   - This prototype only checks for `#` and `empty spaces` as the MRI data text files not contain any other intrusive characters. Other characters such as a `@` may not detected by the software while parsing. It is therefore advised that the user **manually checks the file first if they are using their own data**.
   - The graph output is labeled "Your Graph" and will need to be manually re-named 
   - Once a file is in the programme it will be parsed and analyzed and it must run its course before you can quit and load another separate file 
   - This prototype is specifically for MRI text datafiles produced by an ongoing study so the labels must be present in the raw data or else the code will not work 
   
