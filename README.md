# Project IE
Project IE is a python supported module which parses, stores and analyses cochlear MRI data from text files. This prototype currently allows the user to input one raw file at a time to be tidied and passed through [pandas](http://pandas.pydata.org/) DataFrame for easy data management. The resulting DataFrames also enable further processing in the form of a one-way ANOVA analysis or can alternatively output a graph which is then saved as an image (.png). 

Visualisation (graphing) was achieved using a plotting library called [matplotlib](http://matplotlib.org/) and the one-way ANOVA analysis was completed using the [SciPy library](https://www.scipy.org/)

## Project Description

This study looks to quantify spatial and temporal inflammation-induced changes in the capsular permeability and macrophage infiltration in guinea-pig cochlea using MRI. Modelling of such exchanges in blood and different inner ear (IE) compartments require the analysis of a substantial amount of data. 

These data have been extracted from a set of MRI which measures the propagation of a contrast agent injected into the IE. This project aims to investigate the parsing of this data and statistical analysis of these results. 

This project could provide reference data that can in future be used to quantitatively assess the treatment of ear disease in animal models and establish a platform from which such techniques can be transferred into clinical practice. 


### Prerequisities

1. **Python**
   - Successful running of this programme will require Python 2.7.12
   - You can download Python 2.7.12 following [This link ](https://www.python.org/downloads/release/python-2712/)
   - Alternatively, you may alter the script to fit your version of Python

2. **Operating System**
  - Ubuntu 16.04 LTS 


3. **Data File Requirements**
 - Data Files must be text files (.txt)
 - Files should be labeled like this: **(no.of images)D(no.days after treatment or non-treatment)**
 - So the name should contain **a number** followed by a **D** then another **number**
 - For example: a file labeled **13D4** is an animal that has been imaged 13 times, 4 days after treatment 

## Running the Software 


## License

This project is licensed under the MIT License - see the [LICENSE.txt](https://github.com/BibianaLee/BibianaLee-medsci736/blob/master/LICENCE.txt) file for details

