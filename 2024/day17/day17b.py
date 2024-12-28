import time
from z3 import *
start_time = time.time()

# 00 2,4: B <- A % 8
# 02 1,2: B <- B ^ 2
# 04 7,5: C <- A // (2^B)
# 06 4,5: B <- B ^ C
# 08 1,3: B <- B ^ 3
# 10 5,5: output B % 8
# 12 0,3: A <- A // 8
# 14 3,0: reset (goto 00)

# while A != 0 {
#   B = A & 8
#   B = B ^ 2
#   C = A / (1 << B)
#   B = B ^ C
#   B = B ^ 3
#   A = A / (1 << 3)
#   OUT(B % 8)
# }

code = [2,4,1,2,7,5,4,5,1,3,5,5,0,3,3,0]
zs = z3.Solver()
aStart = z3.BitVec('a', 64)
a, b, c = aStart, 0, 0
for i, d in enumerate(code):
    b = a % 8           # bst 
    b ^= 2              # bxl 
    c = a >> b          # cdv 
    b ^= c              # bxc 
    b ^= 3              # bxl 
    a = a >> 3          # adv 
    zs.add(b % 8 == d)  # out 
    if i != len(code) - 1:
        zs.add(a != 0)  # jnz 
    else:
        zs.add(a == 0)

if zs.check() == z3.sat:
    model = zs.model()
    a_solution = model[aStart]
    print(f"{a_solution}")
else:
    print("No solution found.")

end_time = time.time()
print(f'Time took: {round((end_time - start_time) * 1000, 2)}ms')