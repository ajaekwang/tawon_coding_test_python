def dfs(l, sum_, time):
    global res
    if l == n:  # 부분집합 완성
        if time > m:
            return

        if sum_ > res:
            res = sum_

    else:
        dfs(l + 1, sum_ + pv[l], time + pt[l])
        dfs(l + 1, sum_, time)


if __name__ == '__main__':
    n, m = 5, 20
    values = [[10, 5], [25, 12], [15, 8], [6, 3], [7, 4]]
    pv = list()
    pt = list()

    for i in range(n):
        pv.append(values[i][0])
        pt.append(values[i][1])

    res = -2147000000
    dfs(0, 0, 0)

print(res)
