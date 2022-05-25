def dfs(l, sum_):
    if l == k:
        if sum_ in target:
            check[sum_] = 1
    else:
        dfs(l+1, sum_)
        dfs(l+1, sum_ + chu[l])
        dfs(l + 1, sum_ - chu[l])


if __name__ == '__main__':
    # k = 3
    # chu = [1, 5, 7]
    # k = 8
    # chu = [1,2,4,8,16,32,64,128]
    k=10
    chu = [1152, 835, 1351, 21351, 21353, 5533, 8359, 10350, 101, 108]
    target = range(0, sum(chu)+1)
    check = [0] * (sum(chu) +1)
    dfs(0, 0)
    print(sum(chu) - sum(check[1:]))
