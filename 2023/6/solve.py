import pandas as pd
import re
input=pd.read_csv('6/input', sep="\t", header=None)[0].tolist() 

new_data = input

#time = []
#distance = []
#for i, line in enumerate(new_data):
#    no_double_space_line = re.sub(r'\s+', ' ', line)
#    if(i == 0):
#        time_list = no_double_space_line.split(": ")[1].split(" ")
#    else:
#        distance_list = no_double_space_line.split(": ")[1].split(" ")
#
#def calc_distance(wait, time):
#    return((time-wait)*wait) 
#results = {}
#for i, time_str in enumerate(time_list):
#    results[i] = 0
#    distance = int(distance_list[i])
#    time=int(time_str)
#    print(distance, time)
#    for j in range(time):
#       if (calc_distance(j, time) > distance):
#          results[i] += 1
#
#dot_product = 1
#for key, value in results.items():
#    dot_product = dot_product*value
#print(dot_product)

#Part 2
for i, line in enumerate(new_data):
    no_double_space_line = re.sub(r'\s+', '', line)
    if(i == 0):
        time_str = no_double_space_line.split(":")[1]
    else:
        distance_str = no_double_space_line.split(":")[1]

def calc_distance(wait, time):
    return((time-wait)*wait) 
distance = int(distance_str)
time=int(time_str)
results=0
for j in range(time):
   if (calc_distance(j, time) > distance):
      results += 1

print(results)