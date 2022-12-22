import pandas as pd
data=pd.read_csv('input', sep="\t", header=None)[0].tolist() 

new_input = [line for line in data]
print(new_input)

