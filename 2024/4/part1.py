import os
import logging

input_file_path='2024/4/input/data'
# input_file_path='2024/4/input/example'

# Lets parse the code into a two dimensional array
word_search = []

with open(input_file_path, 'r') as input_file:
    row_length = None  # Variable to store the length of the first row
    for line_number, line in enumerate(input_file, start=1):
        row = line.strip()
        cols = list(row)
        
        # Check if the current row length matches the previous rows
        if row_length is None:
            row_length = len(cols)  # Set the row length from the first row
        elif len(cols) != row_length:
            raise ValueError(
                f"Inconsistent row length detected on line {line_number}: "
                f"expected {row_length}, but got {len(cols)}"
            )
        
        word_search.append(cols)

word = "XMAS"
rows, cols = len(word_search), len(word_search[0])
directions = [
    (0, 1),   # Right
    (0, -1),  # Left
    (1, 0),   # Down
    (-1, 0),  # Up
    (1, 1),   # Down-Right
    (1, -1),  # Down-Left
    (-1, 1),  # Up-Right
    (-1, -1)  # Up-Left
]

def is_valid(x, y):
    return 0 <= x < rows and 0 <= y < cols

def search_from(x, y, direction):
    dx, dy = direction
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if not is_valid(nx, ny) or word_search[nx][ny] != word[i]:
            return False
    return True

matches = []

for r in range(rows):
    for c in range(cols):
        if word_search[r][c] == word[0]:  # Only start search if the first letter matches
            for direction in directions:
                if search_from(r, c, direction):
                    matches.append(((r, c), direction))


# Print results
print(f"Word '{word}' found {len(matches)} times.")




# for cols in word_search:
#     print(cols)


