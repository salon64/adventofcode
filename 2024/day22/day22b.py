from collections import defaultdict
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

best_price_sequences = set()
for ind, number in enumerate(secret_numbers):
    i = 0
    on0 = 0
    on1 = 0
    on2 = 0
    on3 = 3
    pc0 = pc1 = pc2 = pc3 = 0
    max_price = 0
    while i < 1999:
        number64 = number * 64
        number = number ^ number64 # mix
        number = number % 16777216 # prune

        number32 = number // 32
        number = number ^ number32 # mix 
        number = number % 16777216 # prune

        number2048 = number * 2048
        number = number ^ number2048 # mix 
        number = number % 16777216 # prune 


        price = number % 10 # last digit
        pc0 = on1 - on0
        pc1 = on2 - on1
        pc2 = on3 - on2
        pc3 = price - on3
        # print(f"{number}: {pc3}")
        on0 = on1
        on1 = on2
        on2 = on3
        on3 = price

        if i > 3:
            if price >= max_price:
                max_price = price
                best_price_sequences.add((pc0, pc1, pc2, pc3))
                # print((pc0, pc1, pc2, pc3))
        i+=1

print(f"len: {len(best_price_sequences)}")
sums = defaultdict(int)
max_sum = 0
for intsasd, sq in enumerate(best_price_sequences):
    print(intsasd)
    for ind, number in enumerate(secret_numbers):
        i = 0
        on0 = 0
        on1 = 0
        on2 = 0
        on3 = 3
        pc0 = pc1 = pc2 = pc3 = 0
        max_price = 0
        while i < 1999:
            number64 = number * 64
            number = number ^ number64 # mix
            number = number % 16777216 # prune

            number32 = number // 32
            number = number ^ number32 # mix 
            number = number % 16777216 # prune

            number2048 = number * 2048
            number = number ^ number2048 # mix 
            number = number % 16777216 # prune 


            price = number % 10 # last digit
            pc0 = on1 - on0
            pc1 = on2 - on1
            pc2 = on3 - on2
            pc3 = price - on3
            # print(f"{number}: {pc3}")
            on0 = on1
            on1 = on2
            on2 = on3
            on3 = price

            if i > 3:
                if (pc0, pc1, pc2, pc3) == sq:
                    sums[(pc0, pc1, pc2, pc3)] += price
                    max_sum = max(max_sum, sums[(pc0, pc1, pc2, pc3)])
                    break

            
            i+=1



# if (-2, 1, -1, 3) in best_price_sequences:
#     print("okay")
#     print(sums[(-2, 1, -1, 3)])



print(max_sum)
end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')

