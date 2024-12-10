import time
start_time = time.time()
with open('2024/day9/day_9_input.txt', 'r') as file:
    data = file.read().strip()

# data = list('2333133121414131402')
line = []

def printList():
    string = ""
    ind = 0
    res = 0
    for thing in line:
        for i in range(0,thing[1]):
            string += thing[0]
            ind+=1
            if thing[0] != '.':
                res+= ind*int(thing[0])
    print(string)
    return



for i, char in enumerate(data):
    if char == '0':
            continue
    if i % 2 == 0:
        ind = str(int(i/2)) # ind
        line += [[ind, int(char)][:]] # ind, amount
    else: 
        line += [['.', int(char)][:]] # char, amount

left = 0
right = len(line)-1

while left < right:
    if line[right][0] == '.':
        right -= 1

    else:
        left_tmp = 0
        while left_tmp < right:
            if line[left_tmp][0] == '.': # if left is '.'
                if line[left_tmp][1] >= line[right][1]: # can contain
                    dotts = line[right][1]
                    line[left_tmp][1] = line[left_tmp][1] - line[right][1] # updates legth of '.'
                    line.insert(left_tmp, line.pop(right)) # pops right char to the left of '.'
                    line.insert(right+1, ['.', dotts]) # inserts '.' at pos right
                    right+=1
                    # printList()

                    if line[left_tmp+1][1] == 0: # pops '.' out if its legth is 0
                        line.pop(left_tmp+1)
                        right-=1
                    break
                else: # can not contain
                    left_tmp += 1
            else:
                left_tmp += 1
        right-=1


# print(line)
ind = 0
res = 0
for thing in line:
    for i in range(0,thing[1]):
        if thing[0] != '.':
            res+= ind*int(thing[0])
        ind+=1

print(res)

end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
