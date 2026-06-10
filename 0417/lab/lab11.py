transposed = []
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("원래행렬=", matrix)
for i in range(len(matrix[0])):
    transposed_row= []
    for row in matrix: 
        transposed_row.append(row[i])  
    transposed.append(transposed_row)
    
print("전치행렬=", transposed)
