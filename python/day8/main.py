import math

f = open("input.txt")
lines = f.readlines()

# Left/right instructions
instructions: str = lines[0][:-1]

# Map
network_map: dict = {}
for line in lines[2:]:
    key, value = line.split(" = ")
    network_map[key] = value[1:-2].split(", ")

# Part 1
instruction_index: int = 0
steps: int = 0
current_node = "AAA"

while current_node != "ZZZ":
    if instructions[instruction_index] == "L":
        current_node = network_map[current_node][0]
    else:
        current_node = network_map[current_node][1]
    
    steps += 1
    instruction_index += 1

    if instruction_index >= len(instructions):
        instruction_index = 0

print("Steps: ", steps)

# The following two functions are from https://www.geeksforgeeks.org/program-to-find-lcm-of-two-numbers/
# Recursive function to return gcd of a and b 
def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
# Function to return LCM of two numbers 
def lcm(a,b): 
    return (a // gcd(a,b))* b 

# Part 2
instruction_index: int = 0
steps: int = 0
current_nodes = [x for x in network_map.keys() if x[-1] == 'A']
periods = [0 for _ in current_nodes]

periods2 = [[] for _ in current_nodes]

while any([x == 0 for x in periods]):
    steps += 1
    for i, node in enumerate(current_nodes):
        if periods[i] > 0:
            continue
        if instructions[instruction_index] == "L":
            current_nodes[i] = network_map[node][0]
        else:
            current_nodes[i] = network_map[node][1]
        
        if current_nodes[i][-1] == 'Z':
            periods2[i].append(steps)
            periods[i] = steps

    instruction_index += 1

    if instruction_index >= len(instructions):
        instruction_index = 0

print("Steps: ", math.lcm(*periods))
