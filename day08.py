digits = [int(d) for d in open("day08.input").read()]

#print digits
print len(digits) / (25*6)

w = 25
h = 6

layer_len = w * h
nlayers = len(digits) / layer_len
print nlayers

#image = [[[None for _ in range(w)] for _ in range(h)] for _ in range(nlayers)]
#print image

counts = {}
counts[0] = {}
counts[1] = {}
counts[2] = {}

min_layer = 0
min_count = len(digits) + 1

for layer in range(nlayers):
	counts[0][layer] = 0
	counts[1][layer] = 0
	counts[2][layer] = 0

for i, d in enumerate(digits):
	layer = i // (w * h)
	#print "i is " , i, " layer is ", layer
	counts[d][layer] += 1

for layer in range(nlayers):
	if counts[0][layer] < min_count:
		min_layer = layer
		min_count = counts[0][layer]

print min_layer
print counts[1][min_layer] * counts[2][min_layer]

image = [[None for _ in range(w)] for _ in range(h)]

for col in range(w):
	for row in range(h):
		last = 2
		for layer in range(nlayers):
			cur = digits[layer * layer_len + row * w + col]
			if last == 2:
				last = cur

		if last == 0:
			image[row][col] = " "
		elif last == 1:
			image[row][col] = "#"

for row in range(h):
	for col in range(w):
		print image[row][col],
	print
