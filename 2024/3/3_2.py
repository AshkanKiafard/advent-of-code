import sys
import re

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    meomory = file.read()

res = 0
enabled = True
for instr in re.findall( "mul\(\d+,\d+\)|do\(\)|don't\(\)", meomory):
    if "mul" in instr and enabled:
        nums = instr.replace("mul", "").replace("(", "").replace(")", "").split(",")
        res += int(nums[0])*int(nums[1])
    elif "do()" == instr:
        enabled = True
    elif "don't()" == instr:
        enabled = False

print(res)