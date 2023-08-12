# Automated Penetration Testing Model

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

## Output

Now the model response should be something like this. We give vulnerabilities of a host to the model and
it should return us the attacks that we can perform on this host.
