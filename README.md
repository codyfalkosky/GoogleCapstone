<div align="center">
<img src="./images/google-logo-transparent.png" width=400px><img>
</div>

# Google Advanced Data Analytics: Capstone Project
***
    
[**Overview**](#1)
| [**Project**](#2)
| [**A Step Further**](#3)

<br><br>
<div id='1'></div>
    
## Capstone Project Scenario Overview: Working for Salifort Motors
***

### About the Company

Salifort Motors is a fictional French-based alternative energy vehicle manufacturer. Its global workforce of over 100,000 employees research, design, construct, validate, and distribute electric, solar, algae, and hydrogen-based vehicles. Salifort’s end-to-end vertical integration model has made it a global leader at the intersection of alternative energy and automobiles.        

### Your Business Case

As a data specialist working for Salifort Motors, you have received the results of a recent employee survey. The senior leadership team has tasked you with analyzing the data to come up with ideas for how to increase employee retention. To help with this, they would like you to design a model that predicts whether an employee will leave the company based on their  department, number of projects, average monthly hours, and any other data points you deem helpful. 

### The Value of your Deliverable

For this deliverable, you are asked to choose a method to approach this data challenge based on your prior course work. Select either a regression model or a tree-based machine learning model to predict whether an employee will leave the company. Both approaches are shown in the project exemplar, but only one is needed to complete your project.

The capstone project will provide you with valuable experience and data analysis examples that you can share with potential employers.

<br>
<div id='2'></div>

## Project
***
Two notebooks accomplish the project objective of building the best model to predict employees quitting.

### Data Exploration  
[Notebook](./1_Data_Exploration_Cleaning.ipynb)  
The dataset is a csv file of various features including `left`, whether or not the emplyee quit.  This notebook is a detailed exploration and subtle cleaning of the data.

### Modeling  
[Notebook](./2_Modeling.ipynb)  
A full run-through of the modeling process.  This notebook contains data scaling, train test split, testing multiple models & hyperparameters with BayesSearchCV, and finally, choosing the best model.  This is the end of the official capstone. However...

<br>
<div id='3'></div>

## A Step Further
***
### Data Analysis  
[Notebook](./3_Data_Analysis.ipynb)  
There is more than just a great model, there is understanding why!  This notebook exploits model insights with sharply values, delves into categorizing employee types with clustering, and explores other data insights.

### Solution Analysis  
[Notebook](./4_Solution_Analysis.ipynb)  
There is more than just knowing why, there is fixing it!  This notebook explores if the analyzed problems seem possible to fix and makes predictions using the model if such fixes could be implemented.

### Summary  
[Notebook](./0_Summary.ipynb)  
A simple executive stakeholder summary.  The simple what is wrong, and can we fix it?
