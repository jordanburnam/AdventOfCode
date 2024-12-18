import os
import re


input_file_path='2024/1/input/data.tsv'
# input_file_path='2024/1/input/example.tsv'

#left and right lists
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
# Do some sanity checking

#Verify the number of the left is the same as the total lines
if line_count != (len(left_list)):
    raise Exception(f"Expected totals to match, lines in file:{line_count}, left_list:{len(left_list)}")

#Verify the number of the right is the same as the total lines
if line_count != (len(right_list)):
    raise Exception(f"Expected totals to match, lines in file:{line_count}, right_list:{len(right_list)}")

#sort our lists so things line up
left_list.sort()
right_list.sort()

distances=[]
#now lets loop and calculate the distances
for left, right in zip(left_list, right_list):
    distnace = abs(left - right)
    distances.append(distnace)

# now calculate the total distance
# I know I could of saved a loop by doing it in one but I want to be explicit about what I am doing and why!
total_distance = 0
for distance in distances: 
    total_distance += distance


print(f"Total Distnace: {total_distance}")


