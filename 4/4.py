import os
import sys
import pandas as pd

path = os.path.join(sys.path[0],"input.txt")
numbers = open(path).readlines()[0]
numbers = [x for x in numbers.replace("\n", "").split(",")]
lines = [list(x.replace("\n", "").split("\n")) for x in open(path).readlines()][1:]

# Create 2d array of input - Removes space before single digits
newlist = []
for x in lines:
    for y in x:
        newlist.append([z for z in y.split(" ") if z != ""])

def check_for_win(df):
    # Win by row
    for index, row in df.iterrows():
        xcount = 0
        for x in range(len(row)):
            if row[x] == "X":
                xcount += 1
            else:
                break

            if xcount == 5:
                return True, index
                # return index of row to determine which board won

    # Win by col
    for col in df:
        xcount = 0
        i = 0
        for x in df[col]:
            if x == None:
                xcount = 0
            if x == "X":
                xcount +=1
            if xcount == 5:
                return True, i
            i += 1

    return False, 0

def calc_sum(df, row):
    # start and end index of row in the winning board
    start = row - row % 6 + 1
    end = row - row % 6 + 5
    sum = 0
    for x in range(start, end+1):
        for y in df.iloc[x]:
            if y != "X":
                sum += int(y)
    return sum

def part1():
    # Find and replace drawn numbers with X
    df = pd.DataFrame(newlist)
    for x in numbers:
        df = df.replace(x, "X")
        win, row = check_for_win(df)
        if win:
            winning_number = x
            sum = calc_sum(df, row)
            res = sum * int(winning_number)
            return res


print(f"Part 1: {part1()}")


def part2():
    return 0
