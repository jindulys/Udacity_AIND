#!/usr/bin/env python

import sys

from utils import *

# Step 1: Convert the grid string to dict representation.

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '123456789' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '123456789' if it is empty.
    """
    dict = {}
    for i in range(len(grid)):
        if grid[i] == '.':
            dict[boxes[i]] = '123456789'
        else:
            dict[boxes[i]] = grid[i]
    return dict

'''
Solutions:

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
    return dict(zip(boxes, grid))

'''

# Step 2: Elimination

#if its peers contains a single value, we can remove it

def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    valuesCopy = values
    
    # for k,v in values.items():
    #     if len(v) != 1:
    #         for p in peers[k]:
    #             if len(values[p]) == 1:
    #                 #print("Before%s, to replace%s",v, values[p])
    #                 v = v.replace(values[p],"")
    #                 #print("After%s, to replace%s",v, values[p])
    #         #print("Current %s, replaced %s"%(k, v))
    #         values[k] = v
    
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = valuesCopy[box]
        for peer in peers[box]:
            valuesCopy[peer] = valuesCopy[peer].replace(digit,'')

    return valuesCopy

# Step 3: Only choice

# Inside a unit, if a digit can only appear in one spot, assign that spot with that value.

def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here
    #unSolved = [k for k in values.keys() if len(values[k]) != 1]
    
    for unit in unitlist:
        for digit in '123456789':
            digitAppearance = [box for box in unit if digit in values[box]]
            if len(digitAppearance) == 1:
                values[digitAppearance[0]] = digit
    
    return values

'''
# Wrong solution.
def only_choice(values):
    """Finalize all values that are the only choice for a unit.

    Go through all the units, and whenever there is a unit with a value
    that only fits in one box, assign the value to this box.

    Input: Sudoku in dictionary form.
    Output: Resulting Sudoku in dictionary form after filling in only choices.
    """
    # TODO: Implement only choice strategy here
    #unSolved = [k for k in values.keys() if len(values[k]) != 1]
        
    #display(values)
    
    for unit in unitlist:
        toHandle = [u for u in unit if len(values[u]) != 1]
        for i in range(len(toHandle)):
            handleCopy = toHandle[:]
            current = toHandle[i]
            handleCopy.remove(current)
            currentSet = set(values[current])
            restString = ""
            for k in handleCopy:
                restString += values[k]
            othersSet = set(restString)
            d = currentSet.difference(othersSet)
            if len(d) == 1:
                for v in d:
                    values[current] = v
    
    return values
'''

'''

Constraint Propagation is all about using local constraints in a space to dramatically
reduce the search space. If we repeated try set an element and apply constraints we might
get an answer.

'''

# Stage 4: reduce puzzle

def reduce_puzzle(values):
	stalled = False
	while not stalled:
		solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
		eliminate(values)
		only_choice(values)
		solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
		stalled = solved_values_after == solved_values_before
		if len([box for box in values.keys() if len(values[box]) == 0]):
			return False
	return values

# Stage 5: Search

def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
    	return False
    solved_values = len([box for box in values.keys() if len(values[box]) == 1])
    if solved_values == 81:
    	# Note return values so it can be used.
    	return values

    def find_min_box(a, b):
    	if len(values[a])<len(values[b]):
    		return a
    	else:
    		return b
    
    # First time, I forgot to filter out those boxes whose len == 1. So I reached max recursion.
    candidateBox = reduce(find_min_box, filter(lambda x: len(values[x]) > 1, values.keys()))

    for digit in values[candidateBox]:
    	# Important: For python, dict needs to be copy otherwise you permanently change those value.
    	valuesCopy = values.copy()
    	valuesCopy[candidateBox] = digit
    	result = search(valuesCopy)
    	if result:
    		return result
    return False

'''
Solutions:

def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt
'''




if __name__ == '__main__':
	sudokuString = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
	harderSudoku = '4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......'
 	# Stage 1
 	display(grid_values(sudokuString))

 	print ""

 	# Stage 2
 	display(eliminate(grid_values(sudokuString)))

 	print ""

 	# Stage 3
 	display(only_choice(eliminate(grid_values(sudokuString))))

 	print ""

 	display(reduce_puzzle(grid_values(harderSudoku)))
 	display(search(grid_values(harderSudoku)))



