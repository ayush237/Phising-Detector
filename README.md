# Phishing-Website-Detector

## Contents 
- Overview
- Demo
- Project Motivation
- Data
- Project Structure
- Installation
- Running Project
- Model Selection
- Model Accuracy and Project reports
- Project Deployment
- Feature Request
- Tech Stack Used 
- About
- Credits
  
## Overview 
As over time, we have started to depend more on online services, cyber threats have been increasing with a faster rate. There are various websites which involves the usage of sensitive data of users like Online Banking, E-commerce or Social Networking, these websites are used everyday by millions of users and this opens a door for a **Phishing attack**.
  A website similar to the legit website is made and there is a high chance for a users to get fooled by it and enter their valuable info and credentials.
In this project, i have built a phishing website detection system with Machine Learning which is trained on multiple model and achieving an accuracy of 98%. It analysis the data over various aspects and classifies a website into **3 main categories** :
1. Legitimate
2. Suspecious
3. Phishing


## Demo 
Demo for this project : 

## Motivation and Aim
I am highly fascinated by the performance of data analysis and data science which is producing smart strategies in almost every domain and sector, be it industry , education, medical field or securtiy. We are able to take a much more efficient decision by inculcating many different forms of A.I in our systems.
Secondly, i got motivated to work on this project because currently it is the fastest time when from small scaled bussiness to large MNCs , every one is shifting their services online to the web. So it has become more vunerable to different cyber attacks, hence a system is needed for many companies to incorporate with their own systems, to take care of phishing attacks on their customers. 

The aim of this project is the efficiently reduce the cyber threats and specificely phishing, so that people may be more safe while using their sensitive information oer the web. This project is built on a full fledged , ene to end **industry based approach**. So it is not only useful to common man , but more of use to a company who provides online serices to their customers to incorporate with their systems , spread awareness and safety. 

## Project Structure

This project is class based model built on the top of **OOPs concepts** along with end to end **Exception/Error handeling** and **application logging** and stored in a **SQLite Database**
This project is mostly structured with Classes which are all at the same level. Each class is made into a different python file with it's member functions and each of the file is stored in a different directory.

So for every class , their goes a respective python file , in a respective directory/folder. 

i.e  **any class** --> **respective directory** --> **.py file**

Following is the **Directory Tree** of the project : 

![project structure](PhishingStructure.png)


## Working Flow 

**Note** : At every step, the following sequence is always followed :
1. an object of the class "Application logging" is created.
2. A repective file object is created in trainingLogs directory
3. Each step of execution is logged in the file, if there is an error, the exception is displayed, otherwise the step is marked as successfull

---

The project work flow is divided into 3 main parts : 

**1. Training :** 
  
  a. Data validation
  
  b. Data transformation
  
  c. DataBase operations
  
  d. Data preprocessing
  
  e. Data clustering
  
  f. Model selection and tuning
  
  ---
  
**2. Prediction :**
  
  a. Data validation
  
  b. Data transformation
  
  c. DataBase operations
  
  d. Data preprocessing
  
  e. Data clustering
  
  f. prediction
  
  ---
    
**3. Deployment on Heroku**



## Data : 

The data set used for training has **30 features** and **11056 rows.**

check the data ![here](https://github.com/ayush237/Phising-Detector/blob/master/phising.csv)

The data entry for each fature has been incoded between 3 values **[-1,0,1]** as per their values

Also, the data is first validated using the schema file , check ![here](https://github.com/ayush237/Phising-Detector/blob/master/schema_training.json) for the features list of data along with their decided structure/naming-convenction 

## Installation : 

Following are the steps to install the project in a **Windows system** : 
 
 1. Create a virtual environment 
 
 >  **using anaconda distribution** : `conda create -n name-of-your-environment`
 >  **using pip** : `py -m venv env`

 2. Install the packages : 
 
 > `pip install -r requirements.txt`
 
Following are the steps to install the project in a **MacOS/Linux system** :

1. Create a virtual environment 

> `python3 -m pip install --user virtualenv`

2. Install the packagea :

> `python -m pip install -r requirements.txt`


**Note** : I don't specifically know about this issue related to matplotlib, but if you face something like that, kindly check it here : ![https://stackoverflow.com/questions/41457612/how-to-use-requirements-txt-to-install-all-dependencies-in-a-python-project](https://stackoverflow.com/questions/41457612/how-to-use-requirements-txt-to-install-all-dependencies-in-a-python-project)




 




























