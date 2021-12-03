import os
import sys
import pandas as pd

lines = [list(x.replace("\n", "")) for x in open(os.path.join(sys.path[0],"input.txt")).readlines()]


df = pd.DataFrame(lines)

counts = df.apply(pd.value_counts)

zeros = counts.values[0]
ones = counts.values[1]
gamma = ""
epsilon = ""
for x in range(len(zeros)):
    if zeros[x] > ones[x]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

res_gamma = int(gamma, 2)
res_epsilon = int(epsilon, 2)

print(f"Part 1: {res_gamma * res_epsilon}")


