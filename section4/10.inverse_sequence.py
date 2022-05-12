# n = 8
# inverse_sequence = [5, 3, 4, 0, 2, 1, 1, 0]

n = 30
inverse_sequence = [24, 0, 21, 5, 20, 10, 19, 1, 8, 20, 16, 0, 13, 9, 5, 8, 11, 8, 3, 6, 1, 7, 5, 6, 2, 4, 2, 0, 1, 0]
result = [0] * n

for i in range(n):
    count = 0
    for j in range(n):
        if result[j] == 0:
            count += 1
            if count > inverse_sequence[i]:
                result[j] = i+1
                break

print(result)

