left = []
right = []

with open('input.txt', 'r') as input_numbers:
    for line in input_numbers:
        parts = line.split()

        if len(parts) == 2:
            left.append(int(parts[0]))
            right.append(int(parts[1]))

left.sort()
right.sort()

len = len(left)
sum = 0

for i in range (len):
    
    sum += abs(left[i] - right[i])

print(sum)