def count(xi, mid):
    cnt = 1
    s = xi[0]
    for i in range(1, len(xi)):
        if xi[i] - s >= mid:
            cnt += 1
            s = xi[i]

    return cnt

n, c = 5, 3
xi = [1, 2, 4, 8, 9]

xi.sort()
start = xi[0]
end = xi[-1]
result = -1

while start <= end:
    mid = (start + end) // 2
    if c <= count(xi, mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)