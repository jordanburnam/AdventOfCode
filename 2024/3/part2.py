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
# input_file_path='2024/3/input/example'

logging.info(f"Reading file at '{input_file_path}'")

line_count=0

input_string = ""
with open(input_file_path, 'r') as input_file:
    for line in input_file:
        line_count+=1
        input_string += line

pattern = r"mul\((\d+),(\d+)\)|don't\(\)|do\(\)"
pattern = r"mul\((\d+),\1\)|don't\(\)|do\(\)"
pattern = r'mul\((?P<x>(?:[-+]?\d+(?:\.\d+)?(?:[eE][-+]?\d+)?|do\(\)|don\'t\(\))),(?P=x)\)'
pattern = r'mul\(((?:\d+|do\(\)|don\'t\(\))),\1\)'
pattern = r"mul\(\s*(?P<x>(?:-?\d+|do\(\)|don't\(\)))\s*,\s*(?P=x)\s*\)"

do_pattern = r"do\(\)"
dont_pattern = r"don't\(\)"
mul_pattern = r"mul\((\d+),(\d+)\)"

do_matches = re.finditer(do_pattern, input_string)
dont_matches = re.finditer(dont_pattern, input_string)
mul_matches = re.finditer(mul_pattern, input_string)
all_matches = {}

do_matches_count = 0
for match in do_matches:
    do_matches_count += 1
    matched_text = match.group(0)
    start_index = match.start()
    end_index = match.end()
    all_matches[start_index] = matched_text
logging.info(f"Found {do_matches_count} 'do()' match(es)")
      
dont_matches_count = 0
for match in dont_matches:
    dont_matches_count += 1
    matched_text = match.group(0)
    start_index = match.start()
    end_index = match.end()
    all_matches[start_index] = matched_text
    logging.debug(f"{matched_text}|{start_index}")
logging.info(f"Found {dont_matches_count} 'don't()' match(es)")

mul_matches_count = 0
for match in mul_matches:
    mul_matches_count += 1
    matched_text = f"{match.group(1)},{match.group(2)}"
    start_index = match.start()
    end_index = match.end()
    all_matches[start_index] = matched_text
    logging.debug(f"{matched_text}|{start_index}")
logging.info(f"Found {mul_matches_count} 'mul(x,y)' match(es)")

all_matches_sorted = dict(sorted(all_matches.items()))
logging.info(f"Sorted all match(es)")


do_something = True
total=0
for key,value in all_matches_sorted.items():
    if value == "don't()":
        do_something = False
        logging.debug(f"Turned off Do!")
    elif value == "do()":
        do_something = True
        logging.debug(f"Turned on Do!")
    else: 
        if do_something:
            logging.debug(f"do something was true so adding {value}")
            numbers = list(map(int, value.split(',')))
            product = numbers[0] * numbers[1]
            prev_total = total
            total += product
            logging.debug(f"Prev total: {prev_total} and after product of {product} is now {total}")

        else: 
            logging.debug(f"do somethingw as false so skipping {value}")

logging.info(f"Compeleted, total is {total}")