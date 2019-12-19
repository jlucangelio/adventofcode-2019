from intcode import execute

INPUT = [int(t) for t in open("day05.input").read().split(",")]

execute(INPUT, 1)
execute(INPUT, 5)
