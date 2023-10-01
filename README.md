# PTaaS Model

![](https://img.shields.io/badge/Language-Python-blue)
![](https://img.shields.io/badge/Context-ML-blue)

Implementing a machine learning model in order to find the attacks
that can be performed during a penetration testing by using analysis result data
which consists of system vulnerabilities, bugs, and bad smells.

## Dateset

The project dataset is created with help of network and security engineers by analysing 2500
vulnerabilities and choosing the right attacks based on each state. Kinda like simulating 2500
penetration testing attack done by a human agent. Take a look into to our [dataset](./dataset/README.md).

### input

First we give a set of available attacks that we can perform in our testing process:

```txt
sql-injection
ddos
dos
rbac
```

We have some sample data from our users real penetration testing results. This data is our
model dataset which we are going to work on.

```json
[
  {
    "vulnerabilities": [
      "sql raw input",
      "multi source access",
      "hardcode password"
    ],
    "attacks": [
      "sql-injection"
    ]
  }
]
```

### output

Now the model response should be something like this. We give vulnerabilities of a host to the model and
it should return us the attacks that we can perform on this host.

```json
[
  "sql-injection",
  "xss",
]
```
