import pandas as pd
input=pd.read_csv('input', sep="\t", header=None)[0].tolist() 

#step 1
#a = sum((digits := [int(i) for i in line if i.isdigit()])[0] * 10 + digits[-1] for line in input)
#print(a)

mappings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
new_data = [[x if (x := "".join([str(idx) for idx, val in enumerate(mappings, 1) if line[i:].startswith(val)])) else line[i] for i in range(len(line))] for line in input]
sum = sum((digits := [int(i) for i in line if i.isdigit()])[0] * 10 + digits[-1] for line in new_data)
print(sum)
