from collections import namedtuple

Position = namedtuple("Position", "x y z")
Velocity = namedtuple("Velocity", "x y z")
# Moon = namedtuple("Moon", "name pos vel")

def input_to_position(s):
    x, y, z = s[1:-1].split(",")
    _, x = x.split("=")
    _, y = y.split("=")
    _, z = z.split("=")
    return Position(int(x), int(y), int(z))


def move(moon):
    new_pos = []
    for c in range(3):
        new_pos.append(moon[1][c] + moon[2][c])
    moon[1] = Position(new_pos[0], new_pos[1], new_pos[2])


def print_moons(step, moons):
    print "After step", step + 1
    for m in moons:
        print m
    print


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

for step in range(1000):
    for idx in range(len(moons)):
        for jdx in range(len(moons)):
            if idx < jdx:
                pos_i = moons[idx][1]
                pos_j = moons[jdx][1]

                vel_i = moons[idx][2]
                vel_j = moons[jdx][2]

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

                moons[idx][2] = Velocity(new_veli[0], new_veli[1], new_veli[2])
                moons[jdx][2] = Velocity(new_velj[0], new_velj[1], new_velj[2])

    for idx in range(len(moons)):
        m = moons[idx]
        move(m)

    # print_moons(step, moons)

total = 0
for m in moons:
    p = 0
    k = 0

    for i in range(3):
        p += abs(m[1][i])
        k += abs(m[2][i])

    total += p * k

print total
