width = 10
heights = [69, 42, 68, 76, 40, 87, 14, 65, 76, 81]
count = 50

for i in range(count):
    heights.sort()
    heights[0] += 1
    heights[-1] -= 1
heights.sort()
print(heights[-1] - heights[0])