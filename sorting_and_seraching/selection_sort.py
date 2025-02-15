import sys
from load import load_numbers

numbers = load_numbers(sys.argv[1])

def selection_sort(values):
    sorted_list = []

    for i in range(len(values)):
        idx_to_move = index_of_min(values)
        sorted_list.append(values.pop(idx_to_move))
        
    return sorted_list

def index_of_min(values):
    min_index = 0

    for i in range(1,len(values)):
        if values[i] < values[min_index]:
            min_index = i

    return min_index

