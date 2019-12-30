from collections import defaultdict

from intcode import execute_until_output

BLACK = 0
WHITE = 1

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

INPUT = open("day11.input").read().strip().split(",")

memory = defaultdict(int)
for idx, t in enumerate(INPUT):
    memory[idx] = int(t)

hull = defaultdict(int)
pos = (0, 0)
# hull[pos] = BLACK
hull[pos] = WHITE
direction = UP

pc = 0
rel_base = 0
halt = False
painted = set([])
while True:
    output_paint, memory, pc, rel_base = execute_until_output("hull", memory, pc, [hull[pos]], rel_base)
    if output_paint is None:
        break

    hull[pos] = output_paint
    painted.add(pos)

    output_dir, memory, pc, rel_base = execute_until_output("hull", memory, pc, [], rel_base)
    if output_dir is None:
        break

    offset = 0
    if output_dir == 0:
        # turn counterclockwise
        offset = -1
    elif output_dir == 1:
        # turn clockwise
        offset = 1
    else:
        print "error"

    direction = DIRECTIONS[(DIRECTIONS.index(direction) + offset) % len(DIRECTIONS)]
    pos = (pos[0] + direction[0], pos[1] + direction[1])

print len(painted)

e = painted.pop()
min_x = e[0]
min_y = e[1]
max_x = e[0]
max_y = e[1]
painted.add(e)
for p in painted:
    min_x = min(p[0], min_x)
    min_y = min(p[1], min_y)
    max_x = max(p[0], max_x)
    max_y = max(p[1], max_y)

print min_x, max_x
print min_y, max_y

for j in range(max_y+1):
    for i in range(max_x+1):
        if hull[(i, j)] == 1:
            print "#",
        else:
            print ".",
    print

