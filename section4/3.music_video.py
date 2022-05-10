def count(data, dvd_size):
    cnt = 0
    dvd = 0
    for d in data:
        if dvd_size >= dvd+d:
            dvd += d
        else:
            dvd = d
            cnt += 1
    return cnt + 1


n, m = 9, 3
data = range(1, 10)

start_idx = 1
end_index = sum(data)
result = -1
while start_idx <= end_index:
    dvd_size = (start_idx + end_index) // 2
    if m >= count(data, dvd_size):
        end_index = dvd_size - 1
        result = dvd_size
    else:
        start_idx = dvd_size + 1

print(result)