import copy

from collections import namedtuple
from fractions import gcd

Position = namedtuple("Position", "x y z")
Velocity = namedtuple("Velocity", "x y z")

X = 0
Y = 1
Z = 2

POS = 1
VEL = 2

x_states = set([])
y_states = set([])
z_states = set([])
states = [x_states, y_states, z_states]


def lcm(a, b, c):
    return (a * b * c) // gcd(gcd(a, b), c) // gcd(gcd(a, b), c)


def input_to_position(s):
    x, y, z = s[1:-1].split(",")
    _, x = x.split("=")
    _, y = y.split("=")
    _, z = z.split("=")
    return Position(int(x), int(y), int(z))


def move(moon):
    new_pos = []
    for c in range(3):
        new_pos.append(moon[POS][c] + moon[VEL][c])
    moon[POS] = Position(new_pos[X], new_pos[Y], new_pos[Z])


def print_moons(step, moons):
    print "After step", step + 1
    for m in moons:
        print m
    print


def moons_to_tuple(moons, coord):
    return tuple([(m[POS][coord], m[VEL][coord]) for m in moons])


def add_state(states, moons):
    for i in range(len(states)):
        states[i].add(moons_to_tuple(moons, i))


INPUT = """<x=-15, y=1, z=4>
<x=1, y=-10, z=-8>
<x=-5, y=4, z=9>
<x=4, y=6, z=-2>""".splitlines()

moons = []
moons.append(["Io", input_to_position(INPUT[0]), Velocity(0, 0, 0)])
moons.append(["Europa", input_to_position(INPUT[1]), Velocity(0, 0, 0)])
moons.append(["Ganymede", input_to_position(INPUT[2]), Velocity(0, 0, 0)])
moons.append(["Callisto", input_to_position(INPUT[3]), Velocity(0, 0, 0)])

print moons
add_state(states, moons)

step = 1
x_cycle = None
y_cycle = None
z_cycle = None
while x_cycle is None or y_cycle is None or z_cycle is None:
    for idx in range(len(moons)):
        for jdx in range(len(moons)):
            if idx < jdx:
                pos_i = moons[idx][POS]
                pos_j = moons[jdx][POS]

                vel_i = moons[idx][VEL]
                vel_j = moons[jdx][VEL]

                new_veli = []
                new_velj = []
                for coord in range(3):
                    if pos_i[coord] < pos_j[coord]:
                        ic = 1
                        jc = -1
                    elif pos_i[coord] > pos_j[coord]:
                        ic = -1
                        jc = 1
                    else:
                        ic = 0
                        jc = 0

                    new_veli.append(vel_i[coord] + ic)
                    new_velj.append(vel_j[coord] + jc)

                moons[idx][VEL] = Velocity(new_veli[X], new_veli[Y], new_veli[Z])
                moons[jdx][VEL] = Velocity(new_velj[X], new_velj[Y], new_velj[Z])

    for idx in range(len(moons)):
        m = moons[idx]
        move(m)

    # check for cycles
    # x
    if x_cycle is None and moons_to_tuple(moons, X) in states[X]:
        x_cycle = step
        print "x", x_cycle

    # y
    if y_cycle is None and moons_to_tuple(moons, Y) in states[Y]:
        y_cycle = step
        print "y", y_cycle

    # z
    if z_cycle is None and moons_to_tuple(moons, Z) in states[Z]:
        z_cycle = step
        print "z", z_cycle

    add_state(states, moons)

    # print x_cycle, y_cycle, z_cycle
    step += 1

print x_cycle, y_cycle, z_cycle
print lcm(x_cycle, y_cycle, z_cycle)

# total = 0
# for m in moons:
#     p = 0
#     k = 0

#     for i in range(3):
#         p += abs(m[1][i])
#         k += abs(m[2][i])

#     total += p * k

# print total
