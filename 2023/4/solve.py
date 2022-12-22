import pandas as pd
input=pd.read_csv('4/input', sep="\t", header=None)[0].tolist() 

new_data = input

sum_of_points = 0
for line in new_data:
    no_double_space_line = line.replace("  ", " ")
    card, rest_of_line = no_double_space_line.split(": ")
    winning_numbers, card_numbers = map(lambda string: string.split(" ") , rest_of_line.split(" | "))

    winning_numbers_set = set(winning_numbers)
    numbers_found = 0
    for number in card_numbers:
        if (number in winning_numbers_set):
            numbers_found += 1
    if (numbers_found == 1):
        sum_of_points += 1
    elif (numbers_found > 0):
        sum_of_points += 2**(numbers_found-1)

print(sum_of_points)

#Step 2
def parse_card(line_nr):
    global new_data 
    global cards_seen
    line = new_data[line_nr]
    cards_seen += 1
    no_double_space_line = line.replace("  ", " ")
    card, rest_of_line = no_double_space_line.split(": ")
    card_nr = card.split(" ")[1]
    winning_numbers, card_numbers = map(lambda string: string.split(" ") , rest_of_line.split(" | "))

    winning_numbers_set = set(winning_numbers)
    numbers_found = 0
    for number in card_numbers:
        if (number in winning_numbers_set):
            numbers_found += 1
    for value in range(1,numbers_found+1):
        if (line_nr+value not in card_copies_to_parse):
            card_copies_to_parse[line_nr+value] = 1
        else:
            card_copies_to_parse[line_nr+value] = card_copies_to_parse[line_nr+value]+1
    
    
    
        
cards_seen = 0
card_copies_to_parse = {}

for line_nr in range(len(new_data)):
    parse_card(line_nr)

while (len(card_copies_to_parse) != 0):
    for card_nr, nr_copies_to_parse in card_copies_to_parse.copy().items():
        for i in range(nr_copies_to_parse):
            parse_card(card_nr)
            if(card_copies_to_parse[card_nr] == 1):
                card_copies_to_parse.pop(card_nr)
            else:
                card_copies_to_parse[card_nr] = card_copies_to_parse[card_nr]-1

print(cards_seen)
