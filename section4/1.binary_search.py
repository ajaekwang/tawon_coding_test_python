n, m = 8, 32
target = 32
data = [23, 87, 65, 12, 57, 32, 99, 81]

data.sort()
start_idx = 0
end_idx = len(data) - 1

while start_idx <= end_idx:
    mid = (start_idx + end_idx) // 2
    print(target, mid, data[mid])
    if target == data[mid]:
        print(mid+1)
        break
    elif data[mid] > target:
        end_idx = mid - 1
    else:
        start_idx = mid + 1
