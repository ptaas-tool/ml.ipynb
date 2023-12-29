# PTaaS Model

![](https://img.shields.io/badge/Language-Python-blue)
![](https://img.shields.io/badge/Context-ML-blue)

Implementing a machine learning model in order to find the attacks
that can be performed during a penetration testing by using analysis result data
which consists of system vulnerabilities, bugs, and bad smells.

## Dateset

The project dataset is created with help of network and security engineers by analysing 3500
vulnerabilities and choosing the right attacks based on each state. Kinda like simulating 3500
penetration testing attack done by a human agent. Take a look into to our [dataset](https://github.com/ptaas-tool/dataset).

## Model

Our dataset is labelled and its linear, therefore, we are using supervised learning. Our algorithm is 
based on classification. Our two methods are:

- ```SVM```: accuracy 86%
- ```Nbias```: accuracy 92%
