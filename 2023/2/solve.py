import pandas as pd
import math
data=pd.read_csv('2/input', sep="\t", header=None)[0].tolist() 

new_data = data[45:46]

thresholds = {"red": 12, "green": 13, "blue": 14}
valid_game_sum = 0

#step 1
for line in data:
   game_nr, cubes_in_all_games = line.split(": ")
   cubes_in_game = cubes_in_all_games.split("; ")
   should_break = False
   for game in cubes_in_game:
      if(should_break):
         break
      cubes = game.split(", ")
      for cube in cubes:
         nr, color = cube.split(" ")
         if (int(nr) > thresholds[color]):
           should_break = True
           break
   if(not should_break):
      valid_game_sum += int(game_nr.split(" ")[1])

print(valid_game_sum)

#step 2 
valid_max_value_power_sum = 0
for line in data:
   game_nr, cubes_in_all_games = line.split(": ")
   cubes_in_game = cubes_in_all_games.split("; ")
   should_break = False
   max_values = {"red": 0, "green": 0, "blue": 0}
   for game in cubes_in_game:
      if(should_break):
         break
      cubes = game.split(", ")
      for cube in cubes:
         nr, color = cube.split(" ")
         if (int(nr) > max_values[color]):
            max_values[color] = int(nr)
   if(not should_break):
      power = 1
      for key in max_values:
         power *= max_values[key]
      valid_max_value_power_sum += power
      
print(valid_max_value_power_sum)

print(sum(math.prod([max(map(lambda s: s.get(color, 0), [{k: int(v) for v, k in map(str.split, _set.split(", "))} for _set in line.split(": ")[1].split("; ")])) for color in ("red", "green", "blue")]) for line in new_data))
