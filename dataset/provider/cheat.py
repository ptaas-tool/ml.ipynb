import glob
import os
import sys
import json
import random


# find the number of file
list_of_files = glob.glob('./backup/*.json')
if len(list_of_files) == 0:
    list_of_files.append("/backup/data.000.json")

latest_file = max(list_of_files, key=os.path.basename)
number = int(latest_file.split('/')[2].split('.')[1])

ATTACKS_PATH = "./docs/attacks.txt"
OUTPUT_PATH = f"./backup/data.{number+1:03d}.json"
BATCHES = int(sys.argv[1])
MAX_RAND = int(sys.argv[2])


vulnerabilities = []
attacks = []

with open(ATTACKS_PATH, 'r', encoding='UTF-8') as file:
    while line := file.readline():
        attacks.append(line.rstrip())
        
with open("./provider/cheat.txt") as file:
    for line in file:
        line = line.rstrip()
        parts = line.split("->")
        
        atmp = []
        
        tmp = parts[1].split(",")
        for item in tmp:
            atmp.append(attacks[int(item)])
        
        vulnerabilities.append((parts[0].rstrip(), atmp))

if __name__ == "__main__":
    outputs = []
    print(f'Output file is "{OUTPUT_PATH}"\n\n')
    
    for _ in range(0, BATCHES):
        v_tmp = random.randint(1, MAX_RAND)
        v_list = random.sample(vulnerabilities, k=v_tmp)
        
        a_tmp = []
        
        for item in v_list:
            a_tmp = a_tmp + item[1]
        
        a_tmp = list(dict.fromkeys(a_tmp))
        
        outputs.append({
                'vulnerabilities': [x[0] for x in v_list],
                'attacks': a_tmp
            })

    # save output
    with open(OUTPUT_PATH, 'w') as file:
        file.write(json.dumps(outputs, indent=4))
