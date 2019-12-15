orbits = {}
orbiting = {}

for line in open("day06.input"):
	center, satellite = line.strip().split(")")
	if center not in orbits:
		orbits[center] = []
	orbits[center].append(satellite)

	orbiting[satellite] = center

# print orbits

def distance_sum(center, orbits, dist):
	res = 0

	if center not in orbits:
		return dist

	for satellite in orbits[center]:
		res += distance_sum(satellite, orbits, dist + 1)

	return dist + res

print distance_sum("COM", orbits, 0)

def path_to(who, orbiting):
	path = []
	parent = orbiting[who]
	path.append(parent)
	while parent in orbiting:
		parent = orbiting[parent]
		path.append(parent)

	return path


path_to_san = path_to("SAN", orbiting)
path_to_you = path_to("YOU", orbiting)

print path_to_san
print path_to_you

i = 1

while path_to_san[-i] == path_to_you[-i]:
	i += 1

print len(path_to_san) + len(path_to_you) - i - i + 2
