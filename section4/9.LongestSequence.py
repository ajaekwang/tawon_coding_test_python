from collections import deque

n = 10
sequence = [3, 2, 10, 1, 5, 4, 7, 8, 9, 6]

# n = 5
# sequence = [2, 4, 5, 1, 3]

sequence = deque(sequence)
temp = -1
result = ''
for i in range(len(sequence)):
    if i == 0:
        if sequence[0] < sequence[-1]:
            result += 'L'
            temp = sequence.popleft()
        else:
            result += 'R'
            temp = sequence.pop()
    else:
        if sequence[0] < sequence[-1]:
            if sequence[0] > temp:
                result += 'L'
                temp = sequence.popleft()
            elif sequence[-1] > temp:
                result += 'R'
                temp = sequence.pop()
            else:
                break
        else:
            if sequence[-1] > temp:
                result += 'R'
                temp = sequence.pop()
            elif sequence[0] > temp:
                result += 'L'
                temp = sequence.popleft()
            else:
                break
print(len(result))
print(result)
