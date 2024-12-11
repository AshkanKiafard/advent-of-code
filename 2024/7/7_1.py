import sys

if len(sys.argv) > 1:
    file_name = sys.argv[1]

    with open(file_name, 'r') as file:
        input = file.read()
else:
    input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""


lines = input.splitlines()
res = 0
for line in lines:
    sep = line.find(":")
    test = int(line[:sep])
    ops = [int(x) for x in line[sep+1:].split()]
    possibilities = [ops[0]]
    for i, op in enumerate(ops):
        if i > 0:
            new_nums = []
            while len(possibilities) > 0:
                ps = possibilities.pop()
                temp1 = op * ps
                if temp1 <= test:
                    new_nums.append(temp1)

                temp2 = op + ps
                if temp2 <= test:
                    new_nums.append(temp2)

            possibilities += new_nums

    if test in possibilities:
        res += test

print(res)



