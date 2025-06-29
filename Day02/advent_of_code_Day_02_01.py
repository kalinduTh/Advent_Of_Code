
f = open('input.txt', 'r')
content = f.read()
f.close()


def add_to_arr(content):

    data_arr = []

    data = content.strip().split("\n")
    for line in data:
        row = line.split()
        data_arr.append(row)

    return data_arr
    
arr = add_to_arr(content)

def is_safe(arr):

    count = 0

    for row in arr:

        if len(row) != len(set(row)):
            continue
        
        try:
            nums = list(map(int, row))
        except ValueError:
            nums = row
        
        is_increasing = all(i < j for i, j in zip(nums, nums[1:]))
        is_decreasing = all(i > j for i, j in zip(nums, nums[1:]))

        if not (is_increasing or is_decreasing):
            continue

        differences_valid = all(1 <= abs(j - i) <= 3 for i, j in zip(nums, nums[1:]))

        if differences_valid:
            count += 1
        
    return count
            
c = is_safe(arr)

print(c)

is_safe(arr)
#def is_safe():



    