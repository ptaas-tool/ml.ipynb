# const variables
VULNERABILITIES_PATH = "./docs/vulnerabilities.txt"
ATTACKS_PATH = "./docs/attacks.txt"


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
