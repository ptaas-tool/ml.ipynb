# PTaaS Model

![](https://img.shields.io/badge/Language-Python-blue)
![](https://img.shields.io/badge/Context-ML-blue)

Implementing a machine learning model in order to find the attacks
that can be performed during a penetration testing by using analysis result data
which consists of system vulnerabilities, bugs, and bad smells.

## Problem

Our goal is to create a classifier in order to classify real world penetration testing attacks
base on a list of vulnerabilities. In order to classify our inputs, we need a dataset to train
and test our models.

### dateset

The project dataset is created with help of network and security engineers by analysing 3500
vulnerabilities and choosing the right attacks based on each state. Kinda like simulating 3500
penetration testing attack done by a human agent. Take a look into to our [dataset](https://github.com/ptaas-tool/dataset).

## Execute

In order to execute the model to see its results use the following command:

```sh
jupyter nbconvert --execute ./notebook/analysis_data.ipynb
```

## Model

Our dataset is labelled and its linear, therefore, we are using supervised learning. Our algorithm is 
based on classification. Our two methods are:

- ```SVM```: accuracy 86%
- ```Naive Bayes```: accuracy 92%

The reason we select ```Nbayes``` is that its simple and we can train our model as fast as possible. Not to mention that
penetration testing attacks and vulnerabilities are a lot, therefore we need a model that does not get biased easily.
We used ```SVM``` in order to validate the ```Nbayes``` outputs.
