array = []
for i in range(0, 9):
    array.append(list(map(int, input().split())))

maxValue = array[0][0]
row = 1
column = 1
for i in range(0, 9):
    for j in range(0, 9):
        if array[i][j] > maxValue:
            maxValue = array[i][j]
            row = i+1
            column = j+1
print(maxValue)
print(row,column)