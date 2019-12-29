import math

from collections import namedtuple
from fractions import gcd as calculate_gcd

Position = namedtuple("Position", "row col")

MAP = []

for line in open("day10.input"):
	MAP.append(line.strip())

# print MAP
# MAP = """.#..#
# .....
# #####
# ....#
# ...##
# """.splitlines()

# MAP = """.#....#####...#..
# ##...##.#####..##
# ##...#...#.#####.
# ..#.....#...###..
# ..#.#.....#....##
# """.splitlines()

# MAP = """.#..##.###...#######
# ##.############..##.
# .#.######.########.#
# .###.#######.####.#.
# #####.##.#.##.###.##
# ..#####..#.#########
# ####################
# #.####....###.#.#.##
# ##.#################
# #####.##.###..####..
# ..######..##.#######
# ####.##.####...##..#
# .#####..#.######.###
# ##...#.##########...
# #.##########.#######
# .####.#.###.###.#.##
# ....##.##.###..#####
# .#.#.###########.###
# #.#.#.#####.####.###
# ###.##.####.##.#..##
# """.splitlines()

W = len(MAP[0])
H = len(MAP)

DETECTED = [["." for _ in range(W)] for _ in range(H)]

def print_map(m):
	for line in m:
		print " ".join(line)

print H, W
print_map(MAP)
print
# print_map(DETECTED)

def slopes(pos, m, w, h):
	res = set([(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, -1), (-1, -1), (1, 1)])
	for x in range(1, w):
		for y in range(1, h):
			if x != y:
				gcd = calculate_gcd(x, y)
				new_x = x // gcd
				new_y = y // gcd
				res.add((new_x, new_y))
				res.add((-new_x, new_y))
				res.add((new_x, -new_y))
				res.add((-new_x, -new_y))

	return res

def get_detected(pos, m, w, h):
	detected = set()
	slopes_seen = set()
	for slope in slopes(pos, m, w, h):
		for step in range(1, max(w, h)):
			new_row = pos.row + step * slope[1]
			new_col = pos.col + step * slope[0]
			if new_row >= 0 and new_row < h and new_col >= 0 and new_col < w:
				# print slope, "step ", step
				# print new_row, new_col
				if m[new_row][new_col] == "#":
					# print "can see from pos %d %d at pos %d %d" % (pos.col, pos.row, new_col, new_row)
					detected.add((new_col, new_row))
					break # next slope

	return detected


max_num_detected = 0
best_pos = None
for col in range(W):
	for row in range(H):
		if MAP[row][col] == "#":
			# print row, col
			n = len(get_detected(Position(row, col), MAP, W, H))
			# print
			DETECTED[row][col] = str(n)
			if n > max_num_detected:
				max_num_detected = n
				best_pos = Position(row, col)

# print_map(MAP)
print max_num_detected
print_map(DETECTED)
print best_pos

detected = get_detected(best_pos, MAP, W, H)
# print detected

def angle(d, origin):
	if d[0] < origin.col:
		# To the left of the vertical line.
		if d[1] < origin.row:
			# In the top-left quadrant.
			y = origin.row - d[1]
			x = origin.col - d[0]
			phi = 2 * math.pi - math.atan(float(x)/y)
			# print d, phi

		elif d[1] == origin.row:
			phi = (3/2) * math.pi
			# print d, phi

		elif d[1] > origin.row:
			# In the bottom-left quadrant.
			y = d[1] - origin.row
			x = origin.col - d[0]
			phi = math.pi + math.atan(float(x)/y)
			# print d, phi

	elif d[0] == origin.col:
		if d[1] < origin.row:
			phi = 0.0
			# print d, phi
		elif d[1] > origin.row:
			phi = math.pi
		else:
			print "error"

	elif d[0] > origin.col:
		if d[1] < origin.row:
			# In the top-right quadrant.
			y = origin.row - d[1]
			x = d[0] - origin.col
			phi = math.atan(float(x)/y)
			# print d, phi

		elif d[1] == origin.row:
			phi = math.pi / 2
			# print d, phi

		elif d[1] > origin.row:
			# In the bottom-right quadrant.
			y = d[1] - origin.row
			x = d[0] - origin.col
			phi = math.pi - math.atan(float(x)/y)
			# print d, phi

	return phi

print sorted(detected, key=lambda d: angle(d, best_pos))
print sorted(detected, key=lambda d: angle(d, best_pos))[199]
