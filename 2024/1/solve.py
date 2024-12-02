import pandas as pd
data=pd.read_csv('input', sep="\t", header=None)[0].tolist() 

col1 = []
col2 = []
for line_nr, line in enumerate(data):
  line_arr = line.split()
  col1.append(int(line_arr[0]))
  col2.append(int(line_arr[1]))

sorted_col1 = sorted(col1)
sorted_col2 = sorted(col2)


sum = 0
for i, el in enumerate(sorted_col1):
  sum += abs(sorted_col1[i] - sorted_col2[i])

print(sum)

# Part 2
new_sum = 0
for i, num in enumerate(col1):
  new_sum += num * col2.count(num)

print(new_sum)