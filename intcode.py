import copy

POS = 0
IMM = 1
REL = 2


def calculate_addr(param, mode, base):
    offset = param
    if mode == REL:
        offset += base
    return offset


def read_param(memory, param, mode, base):
    if mode == IMM:
        return param
    else:
        return memory[calculate_addr(param, mode, base)]


def execute(program, input_values):
    memory = copy.copy(program)
    cur_input_index = 0
    rel_base = 0
    outputs = []

    pc = 0
    while (memory[pc] != 99):
        v = str(memory[pc])
        opcode = int(v[-2:])

        opmode_1 = POS
        opmode_2 = POS
        opmode_3 = POS

        if len(v) > 2:
            opmode_1 = int(v[-3])
        if len(v) > 3:
            opmode_2 = int(v[-4])
        if len(v) > 4:
            opmode_3 = int(v[-5])

        param1 = memory[pc+1]

        if opcode == 3:
            if opmode_1 == IMM:
                print "error, input instruction opmode IMM"
            op1 = calculate_addr(param1, opmode_1, rel_base)
        else:
            op1 = read_param(memory, param1, opmode_1, rel_base)

        if opcode == 1 or opcode == 2 or opcode == 5 or opcode == 6 or opcode == 7 or opcode == 8:
            param2 = memory[pc+2]
            op2 = read_param(memory, param2, opmode_2, rel_base)

        if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
            # Third operand is the destination operand, always in position/relative mode.
            if opmode_3 == IMM:
                print "error, destination operand specified IMM"

            param3 = memory[pc+3]
            dest = calculate_addr(param3, opmode_3, rel_base)

        # Instructions
        if opcode == 1:
            memory[dest] = op1 + op2
            pc += 4

        elif opcode == 2:
            memory[dest] = op1 * op2
            pc += 4

        elif opcode == 3:
            # input
            memory[op1] = input_values[cur_input_index]
            print "[", pc, "]", "<-", input_values[cur_input_index]
            cur_input_index += 1
            pc += 2

        elif opcode == 4:
            # output
            output = op1
            print "[", pc, "]", output, "->"
            outputs.append(output)
            pc += 2

        elif opcode == 5:
            # jump-if-true
            if op1 != 0:
                pc = op2
            else:
                pc += 3

        elif opcode == 6:
            # jump-if-false
            if op1 == 0:
                pc = op2
            else:
                pc += 3

        elif opcode == 7:
            if op1 < op2:
                memory[dest] = 1
            else:
                memory[dest] = 0
            pc += 4

        elif opcode == 8:
            if op1 == op2:
                memory[dest] = 1
            else:
                memory[dest] = 0
            pc += 4

        elif opcode == 9:
            rel_base += op1
            pc += 2

        else:
            print "invalid opcode", opcode
            break

    print "halt"
    return outputs


def execute_until_output(name, program, starting_pc, input_values):
    memory = copy.copy(program)
    cur_input_index = 0
    outputs = []

    print name

    pc = starting_pc
    while (memory[pc] != 99):
        v = str(memory[pc])
        opcode = int(v[-2:])

        imm_1 = False
        imm_2 = False
        imm_3 = False

        if len(v) > 2:
            imm_1 = v[-3] == "1"
        if len(v) > 3:
            imm_2 = v[-4] == "1"
        if len(v) > 4:
            imm_3 = v[-5] == "1"

        param1 = memory[pc+1]
        if imm_1 or opcode == 3:
            # "input" always take a position parameter.
            op1 = param1
        else:
            op1 = memory[param1]

        if opcode == 1 or opcode == 2 or opcode == 5 or opcode == 6 or opcode == 7 or opcode == 8:
            param2 = memory[pc+2]
            op2 = read_param(memory, param2, imm_2)

        if opcode == 1 or opcode == 2 or opcode == 7 or opcode == 8:
            # Third operand is the destination operand, always in position mode.
            dest = memory[pc+3]

        # Instructions
        if opcode == 1:
            memory[dest] = op1 + op2
            pc += 4

        elif opcode == 2:
            memory[dest] = op1 * op2
            pc += 4

        elif opcode == 3:
            # input
            memory[op1] = input_values[cur_input_index]
            print "[", pc, "]", "<-", input_values[cur_input_index]
            cur_input_index += 1
            pc += 2

        elif opcode == 4:
            # output
            output = op1
            print "[", pc, "]", output, "->"
            return output, memory, pc + 2

        elif opcode == 5:
            # jump-if-true
            if op1 != 0:
                pc = op2
            else:
                pc += 3

        elif opcode == 6:
            # jump-if-false
            if op1 == 0:
                pc = op2
            else:
                pc += 3

        elif opcode == 7:
            if op1 < op2:
                memory[dest] = 1
            else:
                memory[dest] = 0
            pc += 4

        elif opcode == 8:
            if op1 == op2:
                memory[dest] = 1
            else:
                memory[dest] = 0
            pc += 4

        else:
            print "invalid opcode", opcode
            break

    # print "halt"
    return None, memory, pc
