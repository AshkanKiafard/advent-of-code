import sys
import re

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    meomory = file.read()

res = 0
for instr in re.findall( r'mul\(\d+,\d+\)', meomory):
    nums = instr.replace("mul", "").replace("(", "").replace(")", "").split(",")
    res += int(nums[0])*int(nums[1])

print(res)