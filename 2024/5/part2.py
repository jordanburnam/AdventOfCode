import os
import logging
from collections import deque, defaultdict

logging.basicConfig(
    level=logging.INFO,  # Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler()          # Also log to console
    ]
)


input_rule_file_path='2024/5/input/rules'
input_data_file_path='2024/5/input/data'

# input_rule_file_path='2024/5/input/example/rules'
# input_data_file_path='2024/5/input/example/data'




line_rule_count = 0
rules = []
with open(input_rule_file_path, 'r') as input_rule_file:
    for line in input_rule_file:
        line_rule_count += 1
        row = line.strip()
        cols = row.split('|')
        numbers = [int(col) for col in cols]
        if len(cols) != 2:
            raise Exception(f"Line {line_rule_count + 1} had {len(cols)} but expected two: {line}")
        rules.append(numbers)

line_data_count = 0
data = []
with open(input_data_file_path, 'r') as input_data_file:
    for line in input_data_file:
        line_data_count += 1
        row = line.strip()
        cols = row.split(',')
        numbers = [int(col) for col in cols]
        data.append(numbers)




def is_correctly_ordered(update, rules):
    # RULES STRUCTURE LOOKS LIKE THIS: 
    # [[47, 53], [97, 13], [97, 61]]

    # UPDATE STRUCTURE LOOKS LIKE THIS:
    # [75, 47, 61, 53, 29]
    # [97, 61, 53, 29, 13]


    # Create a mapping of page to its index in the update
    index_map = {page: i for i, page in enumerate(update)}
    # INDEX MAP STRUCTURE LOOKS LIKE THIS: 
    # {'75': 0, '47': 1, '61': 2, '53': 3, '29': 4}
    # {'97': 0, '61': 1, '53': 2, '29': 3, '13': 4}

    # Check all applicable rules
    for X, Y in rules:

        if X in index_map and Y in index_map:
            # X must appear before Y
            if index_map[X] >= index_map[Y]:
                return False
    return True

def topological_sort(pages, rules):
    #PAGES STRUCTURE:
    # [75, 97, 47, 61, 53]
    # [61, 13, 29]
    # [97, 13, 75, 29, 47]

    # RULES STRUCTURE LOOKS LIKE THIS: 
    # [[47, 53], [97, 13], [97, 61]]
 
    
    pages_set = set(pages)
    # PAGES_SET STRUCTURE: 
    # {97, 75, 47, 53, 61}
    # {13, 29, 61}
    # {97, 75, 13, 47, 29}


    adj_list = defaultdict(list)
    # Starts out empty
    # ADJ_LIST STRUCTURE BEFORE:
    # defaultdict(List(_empty), {})
    # defaultdict(List(_empty), {})
    # defaultdict(List(_empty), {}) 

    in_degree = {p: 0 for p in pages}
    # IN_DEGREE STRUCTURE BEFORE:
    # {75: 0, 97: 0, 47: 0, 61: 0, 53: 0}
    # {61: 0, 13: 0, 29: 0}
    # {97: 0, 13: 0, 75: 0, 29: 0, 47: 0}


    # Build graph based on applicable rules
    for X, Y in rules:
        if X in pages_set and Y in pages_set:
            # X -> Y
            adj_list[X].append(Y)
            in_degree[Y] += 1

    # ADJ_LIST STRUCTURE AFTER:
    # defaultdict(<class 'list'>, {47: [53, 61], 97: [61, 47, 53, 75], 75: [53, 47, 61], 61: [53]})
    # defaultdict(<class 'list'>, {61: [13, 29], 29: [13]})
    # defaultdict(<class 'list'>, {97: [13, 47, 29, 75], 75: [29, 47, 13], 29: [13], 47: [13, 29]})
  
    # IN_DEGREE STRUCTURE AFTER:
    # {75: 1, 97: 0, 47: 2, 61: 3, 53: 4}
    # {61: 0, 13: 2, 29: 1}
    # {97: 0, 13: 4, 75: 1, 29: 3, 47: 2}



    # Perform topological sort (Kahn's algorithm)
    queue = deque([p for p in pages if in_degree[p] == 0])
    # QUEUE STRUCTURE: 
    # deque([97])
    # deque([61])
    # deque([97])

    sorted_pages = []
    while queue:
        node = queue.popleft()
        sorted_pages.append(node)
        for neigh in adj_list[node]:
            in_degree[neigh] -= 1
            if in_degree[neigh] == 0:
                queue.append(neigh)

    # If we got a full ordering, return it
    # (We assume no cycles because the problem implies a valid ordering is possible.)
    if len(sorted_pages) == len(pages):
        return sorted_pages
    else:
        # If there's a cycle or something unexpected, return None or raise an error
        raise Exception(f"OMG, SOMETHING BE WRONG! [INSERT DESCRIPTIVE ERROR MESSAGE HERE]")

def sum_of_incorrect_middle_pages(rules, data):
    incorrect_updates = [upd for upd in data if not is_correctly_ordered(upd, rules)]
    
    total = 0
    for upd in incorrect_updates:
        # Sort this update according to the rules
        correct_order = topological_sort(upd, rules)
        if correct_order is not None:
            # Find the middle page
            middle_index = len(correct_order) // 2
            total += correct_order[middle_index]
    return total

result = sum_of_incorrect_middle_pages(rules, data)
print(result)  