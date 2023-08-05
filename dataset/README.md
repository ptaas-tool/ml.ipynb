# Dataset

This dataset contains a list of vulnerabilities and attacks sets. We gathered a list
of possible layer 7 attacks on APIs and then we selected which attacks can be performed
based on the given vulnerabilities.

You can get this dataset in multiple versions in ```backup``` directory.
These files are our
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

## contribute

In order to add new data into our dataset, run the following python script and fill the inputs:

```shell
python3 main.py 100 # this is the number of batches that you want to import
```