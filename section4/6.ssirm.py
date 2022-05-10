n = 5
people = [[172, 67], [183, 65], [180, 70], [170, 72], [181, 60]]

cnt = 0
for i, body1 in enumerate(people):
    for j, body2 in enumerate(people):
        if i == j:
            continue
        else:
            if body1[0] < body2[0] and body1[1] < body2[1]:
                cnt += 1
                break
print(n - cnt)
