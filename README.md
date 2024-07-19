<div align="center">
<img src="./images/google-logo-transparent.png" width=400px><img>
</div>

# Google Advanced Data Analytics: Capstone Project
***
    
[**Overview**](#1)
| [**Project**](#2)
| [**A Step Further**](#2)

<br><br>
<div id='1'></div>
    
## Capstone project scenario overview: Working for Salifort Motors
***

### About the company

Salifort Motors is a fictional French-based alternative energy vehicle manufacturer. Its global workforce of over 100,000 employees research, design, construct, validate, and distribute electric, solar, algae, and hydrogen-based vehicles. Salifort’s end-to-end vertical integration model has made it a global leader at the intersection of alternative energy and automobiles.        

### Your business case

As a data specialist working for Salifort Motors, you have received the results of a recent employee survey. The senior leadership team has tasked you with analyzing the data to come up with ideas for how to increase employee retention. To help with this, they would like you to design a model that predicts whether an employee will leave the company based on their  department, number of projects, average monthly hours, and any other data points you deem helpful. 

### The value of your deliverable

For this deliverable, you are asked to choose a method to approach this data challenge based on your prior course work. Select either a regression model or a tree-based machine learning model to predict whether an employee will leave the company. Both approaches are shown in the project exemplar, but only one is needed to complete your project.

The capstone project will provide you with valuable experience and data analysis examples that you can share with potential employers.

<br>
<div id='2'></div>

## Project
***
Two notebooks accomplishing the project objective of building the best model to predict employees quitting.

### Data Exploration  
[Notebook](./1_Data_Exploration_Cleaning.ipynb)  
The dataset is a csv file of various features including `left`, whether or not the emplyee quit.  This notebook is a detailed exploration and subtle cleaning of the data.

### Modeling  
[Notebook](./2_Modeling.ipynb)  
A full runthough of the modeling process.  This notebook contains: data scaling, train test split, testing multiple models & hyperparameters with BayesSearchCV and finally chossing the best model.  This is the end of the offical capstone. However...

<br>
<div id='3'></div>

## A Step Farther
***
### Data Analysis  
[Notebook](./3_Data_Analysis.ipynb)  
There is more than just a great model, there is understanding why!  This notebook exploits model insights with shaply values, delves into categorising employees types with clustering, and exploring other data insights.

### Solution Analysis  
[Notebook](./4_Solution_Analysis.ipynb)  
There is more than just knowing why, there is fixing it!  This notebook explores if the analyised problems seems possible to fix and makes predictions using the model if such fixes could be implemented.

### Summary  
[Notebook](./0_Summary.ipynb)  
A simple executive stakeholder summary.  The simple what is wrong and can we fix it.
