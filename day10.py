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

def num_detected(pos, m, w, h):
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

	# print sorted(detected)
	return len(detected)


max_num_detected = 0
best_pos = None
for col in range(W):
	for row in range(H):
		if MAP[row][col] == "#":
			# print row, col
			n = num_detected(Position(row, col), MAP, W, H)
			# print
			DETECTED[row][col] = str(n)
			if n > max_num_detected:
				max_num_detected = n
				best_pos = Position(row, col)

# print_map(MAP)
print max_num_detected
print_map(DETECTED)
