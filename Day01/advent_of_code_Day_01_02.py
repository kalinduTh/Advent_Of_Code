from collections import Counter

left = []
right = []
total = 0

with open ('input.txt', 'r') as input_numbers:
    for line in input_numbers:
        parts = line.split()

        if len(parts) == 2:
            left.append(int(parts[0]))
            right.append(int(parts[1]))
    

right_count = Counter(right)

for i in left:
    total += right_count.get(i, 0) * i

print(total)