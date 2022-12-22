import pandas as pd
input=pd.read_csv('3/input', sep="\t", header=None)[0].tolist() 

new_data = input[0:3]

#Step 1
def get_coords_to_check(line_nr, row_nr, max_line_nr): 
    if (line_nr != 0 and line_nr != max_line_nr):
        return [(line_nr-1, row_nr-1), (line_nr-1, row_nr), (line_nr-1, row_nr+1), (line_nr, row_nr-1), (line_nr, row_nr+1), (line_nr+1, row_nr-1), (line_nr+1, row_nr), (line_nr+1, row_nr+1)]
    elif (line_nr == max_line_nr):
        return [(line_nr-1, row_nr-1), (line_nr-1, row_nr), (line_nr-1, row_nr+1), (line_nr, row_nr-1), (line_nr, row_nr+1)]
    else:
        return [(line_nr, row_nr-1), (line_nr, row_nr+1), (line_nr+1, row_nr-1), (line_nr+1, row_nr), (line_nr+1, row_nr+1)]

def get_number_from_coords(coords, data, list_of_checked_coords: set):
    sum_value=0
    numbers_found = {} 
    if(coords in list_of_checked_coords):
        return 0
    list_of_checked_coords.add(coords)
    char = data[coords[0]][coords[1]]
    if (char in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")):
        numbers_found[coords[1]] = char
        add_numbers_from_left((coords[0], coords[1]-1), data, list_of_checked_coords, numbers_found)
        add_numbers_from_right((coords[0], coords[1]+1), data, list_of_checked_coords, numbers_found)
    sorted_numbers_found = dict(sorted(numbers_found.items()))
    idx = 0
    length = len(sorted_numbers_found)
    for key, value in sorted_numbers_found.items():
        power_to_raise_to = length-idx-1
        number = int(value)
        add = number * pow(10, power_to_raise_to)
        sum_value = sum_value + add
        idx += 1
    return sum_value

def add_numbers_from_left(coords, data, list_of_checked_coords: set, numbers_found: dict):
    if(coords in list_of_checked_coords):
        return
    list_of_checked_coords.add(coords)
    char = data[coords[0]][coords[1]]
    if (char in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")):
        numbers_found[coords[1]] = char
        add_numbers_from_left((coords[0], coords[1]-1), data, list_of_checked_coords, numbers_found)
        add_numbers_from_right((coords[0], coords[1]+1), data, list_of_checked_coords, numbers_found)
    else:
        return
        
def add_numbers_from_right(coords, data, list_of_checked_coords: set, numbers_found: dict):
    if(coords in list_of_checked_coords):
        return
    if(coords[0] >= len(data)):
        return
    if(coords[1] >= len(data[0])):
        return
    list_of_checked_coords.add(coords)
    char = data[coords[0]][coords[1]]
    if (char in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")):
        numbers_found[coords[1]] = char
        add_numbers_from_right((coords[0], coords[1]+1), data, list_of_checked_coords, numbers_found)
    else:
        return

sum_value=0
data = input 
for line_nr, line in enumerate(data):
    for row_nr, char in enumerate(line):
        if (char not in (".", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0")):
            coords_to_check = get_coords_to_check(line_nr, row_nr, len(data))
            list_of_checked_coords = set()
            for coords in coords_to_check:
                sum_value += get_number_from_coords(coords, data, list_of_checked_coords)
print(sum_value)

#Step 2

sum_value=0
data = input 
for line_nr, line in enumerate(data):
    for row_nr, char in enumerate(line):
        if (char == "*"):
            coords_to_check = get_coords_to_check(line_nr, row_nr, len(data))
            list_of_checked_coords = set()
            numbers_found = set()
            for coords in coords_to_check:
                number = get_number_from_coords(coords, data, list_of_checked_coords)
                if (number != 0):
                    numbers_found.add(number)
            if (len(numbers_found) == 2):
                dot_product = 1
                for value in numbers_found:
                    dot_product *= value 
                sum_value += dot_product
print(sum_value)