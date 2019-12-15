count_part1 = 0
count_part2 = 0
for i in range(387638, 919123 + 1):
	si = str(i)
	adjacent_same = False
	n_adjacents = 0
	increasing = True
	three_or_more = False
	twos = set()
	threes = set()

	for j in range(len(si)-1):
		if si[j] == si[j+1]:
			adjacent_same = True
			twos.add(si[j])
		if int(si[j]) > int(si[j+1]):
			increasing = False

		if j < len(si) - 2:
			if si[j] == si[j+1] and si[j+1] == si[j+2]:
				three_or_more = True
				threes.add(si[j])

	if adjacent_same and increasing:
		count_part1 += 1

	if adjacent_same and increasing and len(twos - threes) > 0:
		count_part2 += 1

print count_part1, count_part2
