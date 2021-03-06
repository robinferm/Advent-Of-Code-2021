import os
import sys
import pandas as pd
import copy

path = os.path.join(sys.path[0],"input.txt")
numbers = open(path).readlines()[0]
numbers = [x for x in numbers.replace("\n", "").split(",")]
lines = [list(x.replace("\n", "").split("\n")) for x in open(path).readlines()][1:]

# Create 2d array of input - Removes space before single digits
newlist = []
for x in lines:
    for y in x:
        newlist.append([z for z in y.split(" ") if z != ""])

# Part 1

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
    start = row - row % 6 + 1 # Part 1
    end = row - row % 6 + 5 # Part 1
    sum = 0
    for x in range(start, end+1):
        # iloc returns the values row x
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



# Part 2

def row_win(df):
    for index, row in df.iterrows():
        xcount = 0
        for x in row:
            if x == "X":
                xcount += 1
            else:
                break

            if xcount == 5:
                return True

def col_win(df):
    for col in df:
        xcount = 0
        for x in df[col]:
            if x == None:
                xcount = 0
            if x == "X":
                xcount +=1
            if xcount == 5:
                return True



def mark_numbers(df):
    # Find and replace drawn numbers with X
    dfs = split(df)
    dfs_winners = {}
    v = 0
    for x in numbers:
        for i in range(len(dfs)):
            dfs[i] = dfs[i].replace(x, "X")
            # Check if row complete
            if row_win(dfs[i]):
                if i not in dfs_winners:
                    # Using dict to only get one result per dataframe
                    # order is used to know which board was solved last
                    # {key: [dataframe, order, number]}
                    dfs_winners[i] = [dfs[i], v, x]
                    v += 1

            # Check if col is complete
            elif col_win(dfs[i]):
                if i not in dfs_winners:
                    dfs_winners[i] = [dfs[i], v, x]
                    v += 1

    return dfs_winners


def split(df):
# Split dataframes into one per board and add to a list
    n = 1
    dfs = []
    totalboards = int(len(df) / 6)
    for _ in range(totalboards):
        dfs.append(pd.DataFrame(df.iloc[n:n+5]))
        n += 6
    return dfs

def sum(df):
    sum = 0
    for x in range(len(df)):
    # iloc returns the values row x
        for y in df.iloc[x]:
            if y != "X":
                sum += int(y)
    return sum
            
def part2():
    df = pd.DataFrame(newlist)
    winners = mark_numbers(df)

    for k,v in winners.items():
        # get last item
        if v[1] == len(winners)-1:
            num = v[2]
            dfsum = sum(v[0])
            return int(num) * int(dfsum)

    
print(f"Part 1: {part1()}")
print(f"Part 2: {part2()}")