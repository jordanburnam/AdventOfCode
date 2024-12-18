import os
import logging


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

def sum_of_middle_pages(rules, data):
    correctly_ordered_updates = []
    
    for update in data:
        if is_correctly_ordered(update, rules):
            correctly_ordered_updates.append(update)
    
    # Sum the middle pages
    total = 0
    for update in correctly_ordered_updates:
        middle_index = len(update) // 2
        total += update[middle_index]
    return total

result = sum_of_middle_pages(rules, data)
print(result)