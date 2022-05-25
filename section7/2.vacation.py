def dfs(l, price):
    global res
    if l == n:
        if res < price:
            res = price

    else:
        if l + t[l] <= n:
            dfs(l+t[l], price + p[l])
        dfs(l+1, price)


if __name__ == '__main__':
    # n = 7
    # values = [[4, 20], [2, 10], [3, 15], [3, 20], [2, 30], [2, 20], [1, 10]]
    n = 10
    values = [[3, 30], [2, 20], [1, 10], [2, 20], [3, 30], [5, 50], [2, 20], [3, 30],
              [4, 40], [1, 10]]
    t = list()
    p = list()
    for i in range(n):
        t.append(values[i][0])
        p.append(values[i][1])
    # t.insert(0, 0)
    # p.insert(0, 0)
    res = -2147000000
    dfs(0, 0)

    print(res)