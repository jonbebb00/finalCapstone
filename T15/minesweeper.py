
# Define a function named 'minesweep' which takes in one parameter 'minefield'
def minesweep(minefield):
    # Iterate through each row of the minefield
    for current_row, row in enumerate(minefield, start=0):
        # Iterate through each column in the current row
        for current_col, col in enumerate(row, start=0):
            # If the current cell is a mine (#), skip to the next iteration of the loop
            if col == "#":
                continue
            # If the current cell is empty (-), count the number of adjacent mines and assign it to the current cell
            elif col == "-":
                count = 0
                check_list = []
                # Iterate through all adjacent cells to the current cell
                for current_r, r in enumerate(minefield, start=0):
                    for current_c, c in enumerate(r, start=0):
                        # If the adjacent cell is within 1 row and 1 column of the current cell, and not the current cell itself, add it to the 'check_list'
                        if (
                            abs(current_row - current_r) <= 1
                            and abs(current_col - current_c) <= 1
                            and (abs(current_col - current_c) + abs(current_row - current_r) != 0)
                        ):
                            check_list.append(c)
                        else:
                            continue
                # Iterate through the 'check_list' to count the number of adjacent mines
                for check in check_list:
                    if check == "#":
                        count += 1
                    else:
                        continue
                # Assign the 'count' as a string to the current cell in the minefield
                minefield[current_row][current_col] = str(count)
            # If the current cell is neither a mine nor an empty cell, assign a question mark (?) to the current cell
            else:
                minefield[current_row][current_col] = "?"

        # Print the current row after all the columns have been processed
        print(row)

# Create a sample minefield
minefield = [["#", "-", "-", "-"], ["-", "-", "-", "#"], ["#", "-", "#", "#"], ["-", "#", "-", "-"], ["-", "-", "-", "-"]]

# Call the 'minesweep' function on the sample minefield
minesweep(minefield)