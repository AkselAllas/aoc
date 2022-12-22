import pandas as pd
input=pd.read_csv('5/input', sep="\t", header=None)[0].tolist() 

new_data = input
maps_list = ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']
maps = {}

i=0
j=0
new_map={}
seeds = str(new_data[:1]).split(': ')[1][:-2].split(" ")
for line in new_data[1:]:
    if ((i <= len(maps_list)-1) and line == maps_list[i]+' map:'):
            j=0
            new_map={}
    else:
        new_map[j] = line
        maps[maps_list[i-1]] = new_map
    j+=1
    if ((i <= len(maps_list)-1) and line == maps_list[i]+' map:'):
        i+=1

for map, lines in maps.items():
    new_map_value = {} 
    k=0
    for line_nr, line in lines.items():
        dest, source, range_value = line.split(" ")
        new_map_value[k]=[int(source), int(dest), int(range_value)]
        k+=1
    maps[map] = new_map_value

def get_next_val(num: int, map):
    for key, value in map.items():
        if (num <= value[0]+value[2] and num >= value[0]):
            return(num + value[1] - value[0])
    return(num)
    
locations = set()
#for seed in seeds:
#    next_val = int(seed)
#    for map_name, map in maps.items():
#       next_val = get_next_val(next_val, map)
#    locations.add(next_val)

#print(min(locations))

#Step 2

#def check_if_seeds_stay_unchanged_from_maps(start, addition, maps):
#    for map_name, map in maps.items():
#        for key, value in map.items():
#            if (start < value[0]+value[2] and start >= value[0]):
#                return(False)
#            if (start+addition < value[0]+value[2] and start+addition >= value[0]):
#                return(False)


seeds_range = []
i=0
m=0
for l, seed in enumerate(seeds):
    from_seed = seeds[i]
    to_seed = seeds[i+1]
    for j in range(int(from_seed), int(from_seed)+int(to_seed)):
        seeds_range.append(j)
        m+=1
    i+=2
    print(i)

    if(i > len(seeds)/2):
       break
print(len(seeds_range))

min_location = 99999999999
i=0
for seed in seeds_range:
    i+=1
    if(i % 1000000 == 0):
        print(i)
    next_val = seed
    for map_name, map in maps.items():
       next_val = get_next_val(next_val, map)
    if(next_val < min_location):
        min_location=next_val

print(min_location)