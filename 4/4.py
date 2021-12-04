import os
import sys
import pandas as pd

path = os.path.join(sys.path[0],"input.txt")
numbers = open(path).readlines()[0]
numbers = [x for x in numbers.replace("\n", "").split(",")]
lines = [list(x.replace("\n", "").split("\n")) for x in open(path).readlines()][1:]

# df = pd.DataFrame(lines)
# df = df[0].str.split(' ',expand=True)
#print(df)

#print(numbers)

# Create 2d array of input - Removes space before single digits
newlist = []
for x in lines:
    for y in x:
        newlist.append([z for z in y.split(" ") if z != ""])


# Either check for win depending on row number or split dfs and check each one
def check_for_win(df):
    # Win by row
    for index, row in df.iterrows():
        #print(row[index])
        xcount = 0
        for x in range(len(row)):
            #print(row[x])
            if row[x] == "X":
                xcount += 1
            else:
                break

            if xcount == 5:
                return True, index
                #return index # return index of row to determine which board won
            # print(row)
            # print(win)
    # Win by col
    for col in df:
        #print(df[col])
        xcount = 0
        i = 0
        for x in df[col]:
            if x == None:
                xcount = 0
            if x == "X":
                xcount +=1
            if xcount == 5:
                print(i)
                print(col)
                print(df[col])
                return True, i
            i += 1
            #print(x)

    return False, 0

def calc_sum(df, row):
    # split df and keep only winning board
    # start and end index of row in the winning board
    start = row - row % 6 + 1
    end = row - row % 6 + 5
    #print(start, end)
    sum = 0
    for x in range(start, end+1):
        for y in df.iloc[x]:
            if y != "X":
                sum += int(y)
    #print(sum)
    return sum

# Find and replace drawn numbers
df = pd.DataFrame(newlist)
for x in numbers:
    df = df.replace(x, "X")
    #print(df)
    win, row = check_for_win(df)
    if win:
        # break here
        winning_number = x
        #print(winning_number)
        sum = calc_sum(df, row)
        res = sum * int(x)
        print(f"Part 1: {res}")
        break
        # sum all unmarked numbers in the winning board and multiply by winning_number
        #(Determine board with row numbers, 1-5, 7-11, 13-17 etc)
#print(df)


