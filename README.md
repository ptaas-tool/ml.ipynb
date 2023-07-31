# Penetration Testing Model

Implementing a machine learning model in order to find the attacks
that can be performed during a penetration testing by using analysis result data
which consists of system vulnerabilities, bugs, and bad smells.

## Input Data

First we give a set of available attacks that we can perform in our testing process.

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
    'host': '127.0.0.1',
    'vulnerabilities': [
      'sql raw input',
      'multi source access',
      'hardcode password'
    ],
    'attacks': [
      'sql-injection'
    ]
  }
]
```
