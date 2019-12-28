import copy
import itertools

from intcode import execute, execute_until_output

INPUT = [int(t) for t in open("day07.input").read().split(",")]

# INPUT = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

m = 0
for phases in itertools.permutations(range(5)):
	input_signal = 0
	for amp in range(5):
		outputs = execute(INPUT, [phases[amp], input_signal])
		input_signal = outputs[0]

	if outputs[0] > m:
		m = outputs[0]

print m

print
print "part 2"
m = 0

for phases in itertools.permutations(range(5, 10)):
	memory_a = copy.copy(INPUT)
	memory_b = copy.copy(INPUT)
	memory_c = copy.copy(INPUT)
	memory_d = copy.copy(INPUT)
	memory_e = copy.copy(INPUT)
	pc_a = 0
	pc_b = 0
	pc_c = 0
	pc_d = 0
	pc_e = 0
	output_a, memory_a, pc_a = execute_until_output("A", memory_a, pc_a, [phases[0], 0])
	output_b, memory_b, pc_b = execute_until_output("B", memory_b, pc_b, [phases[1], output_a])
	output_c, memory_c, pc_c = execute_until_output("C", memory_c, pc_c, [phases[2], output_b])
	output_d, memory_d, pc_d = execute_until_output("D", memory_d, pc_d, [phases[3], output_c])
	output_e, memory_e, pc_e = execute_until_output("E", memory_e, pc_e, [phases[4], output_d])

	outputs = [output_a, output_b, output_c, output_d, output_e]
	last_e = 0
	while (all([output is not None for output in outputs])):
		output_a, memory_a, pc_a = execute_until_output("A", memory_a, pc_a, [output_e])
		output_b, memory_b, pc_b = execute_until_output("B", memory_b, pc_b, [output_a])
		output_c, memory_c, pc_c = execute_until_output("C", memory_c, pc_c, [output_b])
		output_d, memory_d, pc_d = execute_until_output("D", memory_d, pc_d, [output_c])
		output_e, memory_e, pc_e = execute_until_output("E", memory_e, pc_e, [output_d])

		if output_e is not None:
			last_e = output_e

		outputs = [output_a, output_b, output_c, output_d, output_e]

	if last_e > m:
		m = last_e

print
print m
