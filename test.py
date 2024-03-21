def lower_values_below_zeros_2d(arr):
    rows = len(arr)
    cols = len(arr[0])
    result = [[0] * cols for _ in range(rows)]

    for j in range(cols):
        row_ptr = rows - 1
        for i in range(rows - 1, -1, -1):
            if arr[i][j] != 0:
                result[row_ptr][j] = arr[i][j]
                row_ptr -= 1
    return result

arr_2d = [
    [4, 3, 3, 1],
    [4, 5, 0, 0],
    [3, 0, 3, 2],
    [6, 2, 6, 5]]

for i in range(len(arr_2d)):
    print(arr_2d[i])

result_2d = lower_values_below_zeros_2d(arr_2d)
print()

for i in range(len(result_2d)):
    print(result_2d[i])
