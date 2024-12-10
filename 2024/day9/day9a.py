import time
start_time = time.time()

with open('2024/day9/day_9_input.txt', 'r') as file:
    data = file.read().strip()


line = []
# data = list('2333133121414131402')
for i, char in enumerate(data):
    if i % 2 == 0:
        ind = str(int(i/2))
        tmp = int(char)*[ind]
        line.extend(tmp[:])
    else: 
        
        tmp = int(char)*['.']
        line.extend(tmp[:])

left = 1
left_right = left
right = len(line)-1
right_left = right

while left < right:
    if line[left] != '.':
        left += 1
        left_right += 1
        continue
    if line[right] == '.':
        right -= 1
        right_left -= 1
        continue
    
    while line[right_left] != '.' and line[right_left] == line[right]:
        right_left -= 1

    # check if it can fit 
    tmp_left = left
    tmp_Left_right = left_right 
    while tmp_Left_right < right_left:
        if line[tmp_Left_right] == '.':
            tmp_Left_right += 1
        else:
            if tmp_Left_right - tmp_left >= right - right_left:
                break
            else:
                tmp_Left_right += 1
                tmp_left = tmp_Left_right
    else:
        right = right_left
        continue


    while line[left_right] == '.':
        left_right += 1
    
    if left_right-left >= right-right_left:
        while right_left < right:
            line[left], line[right] = line[right], line[left]
            left+=1
            right-=1            
        
        print(f"{right_left} to {right}")
        left = 0
        left_right = 0
    else:
        left_right += 1
        left = left_right
    



# print(line)
res = 0
for i, char in enumerate(line):
    if char == '.':
        continue
    res += i * int(char)

print(res)
print("done")







end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')
