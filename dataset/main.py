import random
import json
import glob
import os
import sys



# find the number of file
list_of_files = glob.glob('./backup/*')
latest_file = max(list_of_files, key=os.path.getctime)
number = int(latest_file.split('/')[2].split('.')[1])


# const variables
VULNERABILITIES_PATH = "./docs/vulnerabilities.txt"
ATTACKS_PATH = "./docs/attacks.txt"
OUTPUT_PATH = f"./backup/data.{number+1:03d}.json"
BATCHS = int(sys.argv[1])


# base lists
vulnerabilities = []
attacks = []


# read input documents
with open(VULNERABILITIES_PATH, 'r', encoding='UTF-8') as file:
    while line := file.readline():
        vulnerabilities.append(line.rstrip())

with open(ATTACKS_PATH, 'r', encoding='UTF-8') as file:
    while line := file.readline():
        attacks.append(line.rstrip())

print(f'[INFO] loaded {len(attacks)} attacks, {len(vulnerabilities)} vulnerabilities into system.')

# generate output data list
outputs = []

# creating 100 attacks
for i in range(0, BATCHS):
    # get random vulnerabilities
    vtmp = random.randint(1, 10)
    vlist = random.sample(vulnerabilities, k=vtmp)
    
    print()
    print(f'batch {i+1} outof {BATCHS}')
    print("=======")
    
    for item in vlist:
        print(item, end=" | ")
       
    print() 
    print("=======")
    print()
    
    # select attacks
    for index, item in enumerate(attacks):
        print(f'[{index}] {item}', end=", ")
    
    print()
    print()
    selected = input('> select attacks: ').split(',')
    
    # generate output
    outputs.append({
        'vulnerabilities': vlist,
        'attacks': [attacks[int(j)] for j in selected]
    })
    
    print()
    
# save output
with open(OUTPUT_PATH, 'w') as file:
    file.write(json.dumps(outputs, indent=4))
