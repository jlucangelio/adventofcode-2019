from collections import defaultdict

from intcode import execute

MEMORY = defaultdict(int)

INPUT = open("day09.input").read().strip().split(",")
# INPUT = [1102,34915192,34915192,7,4,7,99,0]
# INPUT = [104,1125899906842624,99]
# INPUT = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
# INPUT = [1101,0,42,1985,109,2000,109,19,204,-34,99]

for idx, val in enumerate(INPUT):
    MEMORY[idx] = int(val)

print execute(MEMORY, [1])
print execute(MEMORY, [2])
