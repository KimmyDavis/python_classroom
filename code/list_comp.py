"""
list comprehensions
"""

my_simple_list = [i ** 2 for i in range(100)]

test_list = list(range(11))
# doing a map
map_comp = [i ** 2 + 5 * i + 3 for i in test_list]
# doing a filter
filter_comp = [i for i in test_list if i % 2 == 0]
# filter and map
filter_map_comp = [i + 3/i for i in test_list if i and (i % 2 == 0)] # only on even numbers except for zero

# matrices
M1 = [
      [1, 2, 3], 
      [4, 5, 6], 
      [7, 8, 9]
    ]
M2 = [[i] * 3 for i in range(2, 5)]
# picking out a column
col2 = [row[1] for row in M1]
# picking out a diagonal
diag_maj = [M1[i][i] for i in range(len(M1))]
# combinign the two
flat_mat_prod = [M1[i][j] * M2[i][j] for i in range(3) for j in range(3)]
nested_mat_prod = [[M1[i][j] * M2[i][j] for j in range(3)] for i in range(3)]

print(nested_mat_prod)