import glob
import json


# global addresses
BACKUPS = "./backup/*"
VULNERABILITIES_PATH = "./docs/vulnerabilities.txt"
ATTACKS_PATH = "./docs/attacks.txt"

# stat variables
v = 0
a = 0
b = 0
f = 0

# read files
with open(VULNERABILITIES_PATH, 'r') as file:
    v = sum(1 for _ in file)
    

with open(ATTACKS_PATH, 'r') as file:
    a = sum(1 for _ in file)


for inputFile in glob.glob(BACKUPS):
    jfile = open(inputFile)
    data = json.loads(jfile.read())
    b = b + len(data)
    f = f + 1
    jfile.close()


print(f'Attacks = {a}, Vulnerabilities = {v}, Dataset size = {b}, Dataset files = {f}')
