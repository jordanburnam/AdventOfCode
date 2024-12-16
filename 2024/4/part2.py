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





def count_x_mas_patterns(grid):
    """
    Counts how many times the special "X-MAS" pattern appears.
    The pattern is a 3x3 block where both diagonals form either "MAS" or "SAM" and the center is 'A'.
    The diagonals are:
      Top-left to bottom-right: (0,0), (1,1), (2,2)
      Top-right to bottom-left: (0,2), (1,1), (2,0)
    
    Valid diagonal strings: "MAS" or "SAM"
    
    We must have both diagonals forming one of these valid strings and share the same center 'A'.
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    valid_diagonals = {"MAS", "SAM"}
    count = 0
    
    for r in range(rows - 2):
        for c in range(cols - 2):
            # Extract the diagonals
            d1 = grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2]  # top-left to bottom-right
            d2 = grid[r][c+2] + grid[r+1][c+1] + grid[r+2][c]  # top-right to bottom-left
            
            if d1[1] == 'A' and d2[1] == 'A':  # center must be 'A'
                # Check if both diagonals are valid
                if d1 in valid_diagonals and d2 in valid_diagonals:
                    count += 1
                    
    return count



    
# Count how many times the X-MAS pattern appears (Part Two)
part2_count = count_x_mas_patterns(word_search)
print("Part Two count (X-MAS patterns):", part2_count)

