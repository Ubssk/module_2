def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

#Пример результата выполнения функции:
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print("Результат 1: ", result1)
print("Результат 2: ", result2)
print("Результат 3: ", result3)