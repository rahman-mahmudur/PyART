## This is a fork of the PyART real time API reccomendation tool used for undergraduate research. 

## Current modifications:
* Added ability to search Google for information about recommended apis using Python Requests and BeautifulSoup Web Scraper.
* Improved readability in terminal.
* Added least recommended APIs for caller based on probability score.
* Added Support Vector Machine, Naive Bayes, and Logistic Regression Classifier to compare performance and accuracy to Random Forest.
* Commented out Google searching feature to speed up testing, uncomment to readd feature

## Testing and ranking accuracy of different machine learning algorithms on accuracy of intra project reccomendation using average Top K scores:

More information on Top K scores and MRR calculation in paper: https://arxiv.org/pdf/2102.04706.pdf

## Testing method for intra project
* Testing covers intra project reccomendation accuracy (test files starting with a)
* Test projects saved in testdata folder
* Created separate folder for each project to tested for example flask_test and bs4_test
* Added files to generate machine learning models and generate test results for each type of algorithm, for example generateclf.py, generatesvm.py, aget_test_result.py, aget_test_result_svm.py
* K Score array for Top 1, Top 2, Top 3, Top 4, Top 5, Top 10, and MRR (more information in paper) of each reccomendation added together then divided by number of apis recommended for average Top K score

## Testing method for accross project
* Testing covers accross project reccomendation accuracy (test files starting with b)
* Only using allennlp folder and changing CURRENT_PROJ variable in bget_test_result.py (and other test files) for the sake of time saving
* Otherwaise similar process for intra project testing

## Test Results:

Could not test Bs4 and Httpbin due to missing files. 

Flask results:

Top K Averages for Random Forest: Top 1: 0.192 Top 2: 0.24 Top 3: 0.245 Top 4: 0.245 Top 5: 0.331 Top 10: 0.554 MRR: 0.266

Top K Averages for SVM: Top 1: 0.0 Top 2: 0.0 Top 3: 0.0 Top 4: 0.180 Top 5: 0.271 Top 10: 0.4 MRR: 0.102

Top K Averages for Naive Bayes: Top 1: 0.033Top 2: 0.083 Top 3: 0.271 Top 4: 0.271 Top 5: 0.271 Top 10: 0.299 MRR: 0.151

Top K Averages for Linear Regression: Top 1: 0.0 Top 2: 0.167 Top 3: 0.167 Top 4: 0.167 Top 5: 0.167 Top 10: 0.324 MRR: 0.115

Allennlp results:

Top K Averages for Random Forest: Top 1: 0.086 Top 2: 0.103 Top 3: 0.133 Top 4: 0.172 Top 5: 0.246 Top 10: 0.534 MRR: 0.169

Top K Averages for SVM: Top 1: 0.07 Top 2: 0.105 Top 3: 0.16 Top 4: 0.205 Top 5: 0.268 Top 10: 0.392 MRR: 0.153

Top K Averages for Naive Bayes: Top 1: 0.176 Top 2: 0.219 Top 3: 0.247 Top 4: 0.247 Top 5: 0.377 Top 10: 0.538 MRR: 0.262

Top K Averages for Linear Regression: Top 1: 0.112 Top 2: 0.160 Top 3: 0.225 Top 4: 0.258 Top 5: 0.27 Top 10: 0.456 MRR: 0.207

Cornice results:

Top K Averages for Random Forest: Top 1: 0.192 Top 2: 0.24 Top 3: 0.245 Top 4: 0.245 Top 5: 0.331 Top 10: 0.554 MRR: 0.266

Top K Averages for SVM: Top 1: 0.19 Top 2: 0.19 Top 3: 0.19 Top 4: 0.19 Top 5: 0.19 Top 10: 0.268 MRR: 0.205

Top K Averages for Naive Bayes: Top 1: 0.265 Top 2: 0.265 Top 3: 0.265 Top 4: 0.265 Top 5: 0.392 Top 10: 0.444 MRR: 0.309

Top K Averages for Linear Regression: Top 1: 0.203 Top 2: 0.203 Top 3: 0.203 Top 4: 0.203 Top 5: 0.203 Top 10: 0.203 MRR: 0.215



Gitsome results:

Top K Averages for Random Forest: Top 1: 0.022 Top 2: 0.1941 Top 3: 0.194 Top 4: 0.194 Top 5: 0.194 Top 10: 0.316 MRR: 0.133

Top K Averages for SVM: Top 1: 0.134 Top 2: 0.134 Top 3: 0.134 Top 4: 0.134 Top 5: 0.134 Top 10: 0.134 MRR: 0.141

Top K Averages for Naive Bayes: Top 1: 0.05 Top 2: 0.168 Top 3: 0.207 Top 4: 0.214  Top 5: 0.225 Top 10: 0.482 MRR: 0.17

Top K Averages for Linear Regression: Top 1: 0.061 Top 2: 0.189 Top 3: 0.189 Top 4: 0.189 Top 5: 0.290 Top 10: 0.505 MRR: 0.184

Pyspider results:

Top K Averages for Random Forest: Top 1: 0.12  Top 2: 0.12  Top 3: 0.167 Top 4: 0.167 Top 5: 0.174 Top 10: 0.291 MRR: 0.168

Top 1: 0.027 Top 2: 0.077 Top 3: 0.165 Top 4: 0.267 Top 5: 0.297 Top 10: 0.453 MRR: 0.14

Top K Averages for Naive Bayes: Top 1: 0.1 Top 2: 0.1 Top 3: 0.157 Top 4: 0.251 Top 5: 0.285 Top 10: 0.511 MRR: 0.19

Top K Averages for Linear Regression: Top 1: 0.14Top 2: 0.213 Top 3: 0.255 Top 4: 0.255 Top 5: 0.274 Top 10: 0.547 MRR: 0.24

Simplejson results:

Top K Averages for Random Forest: Top 1: 0.0 Top 2: 0.0 Top 3: 0.0 Top 4: 0.0 Top 5: 0.0 Top 10: 0.497 MRR: 0.093

Top K Averages for Random Forest: Top 1: 0.0 Top 2: 0.0 Top 3: 0.0 Top 4: 0.0 Top 5: 0.0 Top 10: 0.497 MRR: 0.093

Top K Averages for Naive Bayes: Top 1: 0.0 Top 2: 0.0 Top 3: 0.52 Top 4: 0.52 Top 5: 0.52 Top 10: 0.667 MRR: 0.193

Top K Averages for Linear Regression: Top 1: 0.0 Top 2: 0.0 Top 3: 0.0 Top 4: 0.0 Top 5: 0.0 Top 10: 0.52 MRR: 0.09



## Readme instructions for API reccomendation from original project:
Link to original project: https://github.com/PYART0/PyART-demo
## Description

PyART is a real-time API recommendation tool for Python, which includes two main functions:
* data-flow analysis for (incomplete or complete) Python code context,
* real-time API recommendation.


Compared to classical tools, it has two important particularities:
* it works on real-time recommendation scenario,
* it provides data-flow analysis and API recommendation for dynamic language.

## Installation


### Dependencies


PyART works on Ubuntu 18.04 OS and requires:

- Python (>= 3.6)
- pytype
- sklearn
- pandas
- joblib
- nltk

If you want to run the baseline tool Pysonar2 for PyART on data-flow analysis, you need to install:
- Java


### User installation

The experiments of PyART are performed on Linux (Ubuntu 18+). The operation system can be downloaded on https://ubuntu.com/download/desktop, or you can download *.iso file from http://mirrors.163.com/ubuntu-releases/18.04/ and install it on vmware tools. Since there is Python 3.6+ installed in original ubuntu 18+ os, you just need to install java environment. You can use the following command to easily install Java (the default JDK) on Ubuntu: 

`sudo apt-get update `

`sudo apt-get upgrade `

`sudo apt-get install default-jdk `

To verify the installation, by running the following command which will print the Java version: 

`java -version`

To install other library dependencies, you can use the following commands:

`sudo apt-get install libnss3 libfontconfig gconf-service libasound2 libatk1.0-0 libc6 libcairo2 libcups2 libdbus-1-3 libexpat1 libfontconfig1 libgcc1 libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libpangocairo-1.0-0 libstdc++6 libx11-6 libx11-xcb1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-certificates fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils wget` 

`python3 -m pip install --upgrade pip` 

`python3 -m pip install pytype sklearn pandas joblib nltk`

Since PyART also requires punkt package of nltk_data, you can run the following command:

~~~~~~~

Python3

>>> import nltk

>>> nltk.download('punkt')

~~~~~~~~

If the above method is not useful, then you can download nltk_data from https://github.com/nltk/nltk_data, and put it to any path in the following: 

~~~~~~~~~~~
-'/[your '~' path]/' #such as /root/ or ~ 
- '/usr/' 
- '/usr/share/' 
- '/usr/lib/' 
- '/usr/share/' 
- '/usr/local/share/' 
- '/usr/lib/' 
- '/usr/local/lib/' 
~~~~~~~~~~~~~

and unzip punkt.zip in nltk_data/packages/tokenizers/:

`cd nltk_data/packages/tokenizers/` 

`unzip punkt.zip` 

and then run 

`cd ..` 

`cp -r tokenizers/ ../`

## Evaluation of API Reccomendation (Task 2)


**To run training process of intra-project recommendation in Task2, use the following command:**

`cd PyART-demo/PyART`

`python3 aget_train_kfold.py`

The result of the command, which is set of feature vectors and labels, is output to *.csv files in `traincsv/` dictionary. The input of the command is stored in `testdata/`.

The excerpts of the console output of PyART for the training of `flask` project are like the following:

![FIG3](https://github.com/PYART0/PyART-demo/blob/main/Figures/FIG3.png)

in which the first line shows the current file, the second line shows a line of code which contains the recommendation point, the third line represents the information of the recommendtion point in the form of `[file name]#[line number]#[caller]:[inferred type]#expected API`.

Then use the following command to generate RF model:

`python3 generateclf.py`

The model is stored as *.pkl in traincsv/ dictionary.

The excerpts of the console output of PyART for generating model are as follows:

![FIG4](https://github.com/PYART0/PyART-demo/blob/main/Figures/FIG4.png)

To reproduce training for your own project:

Store your project in `testdata/`, change the `CURRENT_PROJ` in `aget_train_kfold.py` in line 1329, and change the `proj_name` variable in `generateclf.py` in line 6.


**To run testing process of intra-project recommendation in Task2, use the following command:**

`python3 aget_test_result.py`

The recommendation results are printed in real time, you can use `python3 aget_test_result.py > output/FILENAME` to store results, in which `FILENAME` denotes your output file.

The excerpts of the console output of PyART for testing are like the following:

![IMAGE](https://github.com/PYART0/PyART-demo/blob/main/Figures/FIG55.png)

in which the first line shows the line of code which contains recommendation point, the second line represents the information of the recommendtion point in the form of `[file name]#[line number]#[caller]:[inferred type]#expected API`, the 'Recommend List' shows the Top-10 recommendaiton results of PyART, the 'Ranks:[2,1]' shows all the ranks that the expected API is at in the list (without OOV), the 'Ranks:[100,2,1]' shows all the ranks that the expected API is at in the list (including OOV), the top-k and mrr give accuraies.


To reproduce testing for your own project:

Store your project in `testdata/`, change the `CURRENT_PROJ` in `aget_test_result.py` in line 1463.


**To run training process of across-project recommendation in Task2, use the following command:**

`python3 get_train_kfold.py`

The result of the command, which is set of feature vectors and labels, is output to *.csv files in traincsv-1/ dictionary. The input of the command is stored in traindata/. Since the training data for across-project is large, we only put a single project in traindata/, you can get our all training projects from Github with TrainDataList.txt.
Then use the following command to generate RF model:

`python3 ac_generateclf.py`

The model is stored as total.pkl in traincsv-1/ dictionary.

**To run testing process of across-project recommendation in Task2, use the following command:**

`python3 bget_test_result.py`

The recommendation results are printed in real time, you can use `python3 bget_test_result.py > FILENAME` to store results.

To reproduce testing for your own project:

Store your project in `testdata/`, change the `CURRENT_PROJ` in `bget_test_result.py` in line 1463.

The excerpts of the console output of PyART for across-project recommendation is similar to intra-project reocmmendation.

![FIG6](https://github.com/PYART0/PyART-demo/blob/main/Figures/FIG6.png)

**Other information in PyART:**

The testJson/ dictionary stores *.json files that collect def information of the target project. Of course, the json file can be obtained directly by Regular Expression Extraction. In our demo, we extract it with understand tool. If you want to use understand, you should download understand for linux and use the following commands:

vim ~/.bashrc

export PATH="$PATH:/[path]/understand/scitools/bin/linux64"

export STIHOME="/[path]/understand/scitools"

export LD_LIBRARY_PATH="/[path]/understand/scitools/bin/linux64"

[This is not necessary if you do not use understand]
