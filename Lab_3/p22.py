matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Original matrix:")
for row in matrix:
    print(row)

print("\nTransposed matrix:")
transposed_matrix = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
for row in transposed_matrix:
    print(row)