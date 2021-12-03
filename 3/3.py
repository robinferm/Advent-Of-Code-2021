import os
import sys
import pandas as pd
import numpy as np

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
print(res_gamma)
print(res_epsilon)
print(f"Part 1: {res_gamma * res_epsilon}")
print(gamma)

# Part 2

def calc_oxygen(gamma, oxygen, i):
    if len(oxygen) == 1:
        return oxygen

    # col in input - match index in gamma
    zerocount = len(oxygen[df[i].str.match('0')])
    onecount = len(oxygen[df[i].str.match('1')])
    if zerocount == onecount:
        oxygen = oxygen[df[i].str.match('1')]
    elif zerocount > onecount:
        oxygen = oxygen[df[i].str.match('0')]
    else:
        oxygen = oxygen[df[i].str.match('1')]

    return calc_oxygen(gamma, oxygen, i+1)

test = calc_oxygen(gamma, df, 0)

asd = test.to_numpy()
asd = np.concatenate(asd)
stringasd = ""
for x in asd:
    stringasd += str(x)
print(stringasd)
print(int(stringasd, 2))
print(f"Oxygen: {test.to_numpy()}")
print(f"Gamma: {gamma}")

#################################

def calc_c02(gamma, co2, i):
    if len(co2) == 1:
        return co2
    #region test
    # if len(co2) == 2:
    #     # Filtrera en sista gång, om det är olika kommer endast den som mathcar gamma kvarstå
    #     # test2 = co2[df[i].str.match(gamma[i])]
    #     test2 = co2[df[i].str.contains(gamma[i])==False]
    #     # print("##")
    #     # print(test2)
    #     # print("##")
    #     # Om det är en 0a och en 1a i de två sista, dvs lika många, då ska 1an väljas
    #     if len(test2) == 1:
    #         #return co2[~df[i].str.match('1')]
    #         return co2[df[i].str.contains('1')==False]
    #     return test2
    #endregion
    # col in input - match index in gamma

    zerocount = len(co2[df[i].str.match('0')])
    onecount = len(co2[df[i].str.match('1')])

    if zerocount == onecount:
        co2 = co2[df[i].str.match('0')]
    elif zerocount > onecount:
        co2 = co2[df[i].str.match('1')]
    else:
        co2 = co2[df[i].str.match('0')]

    return calc_c02(gamma, co2, i+1)

test = calc_c02(gamma, df, 0)
print(test)
print(f"CO2: {test.values}")
print(f"Gamma: {gamma}")



asd = test.to_numpy()
asd = np.concatenate(asd)
stringasd2 = ""
for x in asd:
    stringasd2 += str(x)
print(stringasd2)
print(int(stringasd2, 2))


print(f"Part 2: {int(stringasd, 2) * int(stringasd2, 2)}")