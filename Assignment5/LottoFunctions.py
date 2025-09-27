#1a. one- dimentional lists

#1 create "generate_row function" in Python using the random.sample function, which conveniently generates unique random numbers.
# Then sort the list before returning it.

import random

def generate_row (max_value: int, row_length: int) -> list[int]:#Generates a sorted list of unique random numbers. row can be replaced with lottery_numbers/numbers to be clearer
    row = random.sample(range(1,max_value+1),row_length)        # random.sample never picks the same number twice. Generate unique random numbers. range(start,stop,(step)). random.sample(population, k), population: a sequence (like a list, range, or tuple) to pick numbers from. k: how many unique elements you want to select.
    row.sort()         #sort list
    return row       #In Python, if a function doesn’t explicitly return a value, it returns None by default.

# range(1, max_value + 1) generates all possible numbers from 1 to max_value
# then random.sample picks *row_length unique numbers from that range
# row.sort() ensures the output list is sorted, changes the original list row so that its elements are in ascending order (smallest to largest). modifies the list itself and returns None

#Testing
print(generate_row(max_value=52, row_length=8))
print(generate_row(max_value=5, row_length=5))


#2 create a function that returns number of matching numbers, counts how many numbers in played_row are also in correct_row.
def check_row(correct_row: list[int], played_row: list[int]) -> int:            #correct_row: list[int] means the first input argument (correct_row) should be a list of integers. played_row: list[int] means the second input argument (played_row) should also be a list of integers. -> int → this indicates the function will return an integer, specifically the count of matching numbers.
    # The simplest and most efficient way is to use Python sets, which allow easy intersection.
    # Convert both lists to sets and find intersection
    correct_row = set(correct_row)
    played_set = set (played_row)

    matches = len(correct_row & played_set)     # Number of matches is the size of the intersection. "&" is the set intersection operator in Python. It returns a new set that contains only the elements that exist in both sets
    return matches

correct_row = [2, 5, 12, 13, 14, 23, 59]
played_row = [1, 5, 12, 15, 23]
print(check_row(correct_row, played_row))