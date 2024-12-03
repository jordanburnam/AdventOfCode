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


input_file_path='2024/3/input/data'
input_file_path='2024/3/input/example'

logging.info(f"Reading file at '{input_file_path}'")

line_count=0


with open(input_file_path, 'r') as input_file:
    for line in input_file:
        line_count+=1

print(f"total_lines:{line_count}")
