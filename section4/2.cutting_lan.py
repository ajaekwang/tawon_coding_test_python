def cut_count(data, mid):
    cnt = 0
    for d in data:
        cnt += d // mid
    return cnt

n, m = 4, 11
data = [802, 743, 457, 539]
start_idx = 1
end_idx = max(data)

while start_idx <= end_idx:
    mid = (start_idx + end_idx) // 2
    count = cut_count(data, mid)
    if count >= m:
        print(mid)
        start_idx = mid + 1
    else:
        end_idx = mid - 1
