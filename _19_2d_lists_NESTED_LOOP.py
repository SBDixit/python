# 2d LISTS OR ARRAY IS SIMPLIY LOOKS LIKE A MATRIX :

Number_grid = [          #======>>>>>>> its sub-array elements  index    column  row 
    [1,2,3],             #                                        0        0      0
    [4,5,6],             #                                        1        1      1
    [7,8,9],             #                                        2        2      2     
    [0]                  #                                        3        _      3
] 
#print(Number_grid[index][COLUMN])
print(Number_grid[0][2])
print("     ")

for row in Number_grid:
    for col in row:
        print(col)
     #   print(row)