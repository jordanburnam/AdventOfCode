import os
import re
from collections import Counter
import logging 


logging.basicConfig(
    level=logging.INFO,  # Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),  # Log to a file
        logging.StreamHandler()          # Also log to console
    ]
)


input_file_path='2024/1/input/data.tsv'
# input_file_path='2024/1/input/example.tsv'

logging.info(f"Reading file at '{input_file_path}'")

# left and right lists
left_list=[]
right_list=[]

# Count the lines to check our work later
line_count=0

#opening file and reading line by line
with open(input_file_path, 'r') as input_file:
    for line in input_file:
        line_count+=1
        # Remove leading and trailing whitespace
        line = line.strip()

        # Split line on exactly three spaces
        split_line = re.split(r'\s{3}', line)
        
        # Ensure there are exactly two columns as that is a requirement for this to work
        if len(split_line) != 2:
            raise Exception(f"Expected line in file ot yeild 2 rows but instead got {len(split_line)} rows, line was '{line}'")

        # Convert to float and fail with details if not able to convert
        try:
            split_line = [float(value) for value in split_line]
        except Exception as e:
             raise Exception(f"Failed to convert values to float, {split_line[0]} and {split_line[1]}")

        left_list.append(split_line[0])
        right_list.append(split_line[1])

#Log some values to show what we found while parsing the file 
logging.info(f"total_lines_in_file:{line_count}|left_list_count:{len(left_list)}|right_list_count:{len(right_list)}")

# Do some sanity checking

#Verify the number of the left is the same as the total lines
if line_count != (len(left_list)):
    raise Exception(f"Expected totals to match, lines in file:{line_count}, left_list:{len(left_list)}")

#Verify the number of the right is the same as the total lines
if line_count != (len(right_list)):
    raise Exception(f"Expected totals to match, lines in file:{line_count}, right_list:{len(right_list)}")

#sort our lists so things line up
# left_list.sort()
# right_list.sort()


count_right_list_dict = Counter(right_list)
similarity_scores=[]
#this keeps track of things missing to ensure our totals add up later
missing_occurences_count=0
for left in left_list: 
    if left in count_right_list_dict.keys():
        num_occurences = count_right_list_dict[left]
        score = left * num_occurences
        similarity_scores.append(score)
        logging.debug(f"left:{left}|num_occurences:{num_occurences}|score:{score}")
    else:
        missing_occurences_count+=1
        logging.debug(f"missing_left:{left}|count_right_list_dict[left]:{count_right_list_dict[left]}")

if len(left_list) != (missing_occurences_count + len(similarity_scores)):
    raise Exception(f"Expected total from left_list: {len(left_list)} to equal the combind total of missing_occurences_count:{missing_occurences_count} and len(similarity_scores):{len(similarity_scores)}")

logging.info(f"missing_occurences_count:{missing_occurences_count}|similarity_scores_count:{len(similarity_scores)}")


#now lets calculate the total similarity
similarity_score = 0
for score in similarity_scores:
    similarity_score += score



print(f"Total Similarity: {similarity_score}")


