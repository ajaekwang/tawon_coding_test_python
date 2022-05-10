n = 5
time_table = list()
for i in range(5):
    s, e = map(int, input().split())
    time_table.append([s, e])

cnt = 0
for time in time_table:
    end_time = time[1]
    # end