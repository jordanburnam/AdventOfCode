import os
import logging
import re


logging.basicConfig(
    level=logging.INFO,  # Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler()          # Also log to console
    ]
)


input_file_path='2024/3/input/data'
input_file_path='2024/3/input/example'

logging.info(f"Reading file at '{input_file_path}'")

line_count=0

input_string = ""
with open(input_file_path, 'r') as input_file:
    for line in input_file:
        line_count+=1
        input_string += line

pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, input_string)

calculated_total = 0
for match in matches:
    if len(match) != 2:
        raise Exception(f"Oh shoot, I am dead .... goodbye cruel world")
    product = int(match[0]) * int(match[1])
    calculated_total += product
        
print(f"calculated_total:{calculated_total}")
