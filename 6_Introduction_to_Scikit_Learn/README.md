# Machine Learning Modelling Using Scikit-Learn

Scikit-learn is an open source machine learning library that supports supervised and unsupervised learning. It also provides various tools for model fitting, data preprocessing, model selection and evaluation, and many other utilities. You can find out more on the project's [Documentation](https://scikit-learn.org/stable/)

The bulk of the time and effort data scientists dedicate to building machine learning models are usually spent on cleaning the data (Extraction, Transformation and Loading operations, fixing missing values, feature engineering, handling categorical variables, etc.). It is also helpful to carry out exploratory data analysis (EDA) to better understand the dataset and identify promising tactics. Both processes would be shown in this practical.


We'd go through the step by step process of building a machine learning model using scikit-learn and the wine quality dataset. We would also look at some useful tips and tricks.


The visualization tools used are [Matplotlib](https://matplotlib.org/) and [Seaborn](https://seaborn.pydata.org/)


## Setup:
- If you haven't already, clone this repo. 
- As done for previous tasks, we'll use virtual environment to manage all our installations. If you already have a virtual environment created for a previous practical, you can simply activate the environment and install the libraries using
```
pip install matplotlib seaborn scikit-learn pandas
```
Otherwise, create a new virtual environment then 
```
pip install -r requirements.txt
```
- Go through the notebook to try your hands on the codes. 🔨🔨
- While doing that, you may realise that there are some details that weren't explored and that'll be awesome. So get at them! 🔨🔨

## Data
The dataset used in this practice is related to red variants of the Portuguese "Vinho Verde" wine.

Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).

This datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are many more normal wines than excellent or poor ones). 

Outlier detection algorithms could be used to detect the few excellent or poor wines. Also, we are not sure if all input variables are relevant. So it could be interesting to test feature selection methods.

Citation:
  P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. 
  Modeling wine preferences by data mining from physicochemical properties.
  In Decision Support Systems>, Elsevier, 47(4):547-553. ISSN: 0167-9236.

  Available at: [@Elsevier] http://dx.doi.org/10.1016/j.dss.2009.05.016
                [Pre-press](http://www3.dsi.uminho.pt/pcortezwinequality09pdf)
                [bib](http://www3.dsi.uminho.pt/pcortez/dss09.bib)


## Other Tools & Projects

| S/N | Tool | Awesome projects |
| --- | ---- | ---------------- |
| 1 | [IMBLEARN](https://imbalanced-learn.org/stable/)  |
| 2 | [NLTK](https://www.nltk.org/)  |
| 3 | [XGBOOST](https://xgboost.ai/) | 
| 4 | [CATBOOST](https://catboost.ai/) |
| 5 | [SPACY](https://spacy.io/) | 
| 6 | [SCIKIT-IMAGE](https://scikit-image.org/) |
| 7 | [RAPIDS](https://www.nvidia.com/en-us/deep-learning-ai/software/rapids/) |



## Project Ideas

- Check out the datasets available on the [UCI_Machine_Learning_Repository](https://archive.ics.uci.edu/ml/index.php) to get more exposure on data exploration and machine learning modeling.
- Pratice using different strategies and evaluates what works (Bearing in mind the "No free Lunch Theory").
