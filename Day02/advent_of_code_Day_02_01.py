
f = open('input.txt', 'r')
content = f.read()
f.close()

def add_to_arr(content):

    data_arr = []

    data = content.strip().split("\n")
    for line in data:
        row = line.split()
        data_arr.append(row)
    
    print(data_arr[100])

add_to_arr(content)


    