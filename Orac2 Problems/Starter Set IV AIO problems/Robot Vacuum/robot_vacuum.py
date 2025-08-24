import sys

K = int(sys.stdin.readline())
instructions = sys.stdin.readline().strip()
instruction_frequency = {"N": 0, "S": 0, "E": 0, "W": 0}
for instruction in instructions:
    instruction_frequency[instruction] += 1
steps_needed = abs(instruction_frequency["N"] - instruction_frequency["S"]) + abs(instruction_frequency["E"] - instruction_frequency["W"])
print(steps_needed)
