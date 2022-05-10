# n, m = 5, 140
# weights = [90, 50, 70, 100, 60]

n, m = 10, 150
weights = [86, 95, 107, 67, 38, 49, 116, 22, 78, 53]

flags = [0] * n
weights.sort(reverse=True)
cnt = 0

for i in range(n):
    if flags[i] == 1:
        continue
    for j in range(n):
        if flags[j] == 1:
            continue

        if i == j:
            continue
        else:
            if weights[i] + weights[j] <= m:
               flags[i] = 1
               flags[j] = 1
               cnt += 1
               break
    else:
        flags[i] = 1
        cnt += 1

print(cnt)

