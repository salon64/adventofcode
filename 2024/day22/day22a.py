import copy
from itertools import permutations
import re
import time
import heapq
start_time = time.time()
with open('2024/day22/day_22_input.txt', 'r') as file: # day_22_input.txt
    data = file.read().strip().splitlines()

secret_numbers = [int(line) for line in data]
# print(secret_numbers)


result = 0
for ind, number in enumerate(secret_numbers):
    i = 0
    while i < 2000:
        number64 = number * 64
        number = number ^ number64 # mix
        number = number % 16777216 # prune

        number32 = number // 32
        number = number ^ number32 # mix 
        number = number % 16777216 # prune

        number2048 = number * 2048
        number = number ^ number2048 # mix 
        number = number % 16777216 # prune 
        i+=1
    # print(number)
    result += number


print(result)
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')

