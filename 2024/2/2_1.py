import sys

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    reports = file.read()

safes_count = 0
for report in reports.split('\n'):
    safe = True
    lvls = [int(x) for x in report.split(' ')]
    increasing = int(lvls[0]) <= int(lvls[1])
    for i, lvl in enumerate(lvls):
        if i > 0:
            diff = lvl - int(lvls[i-1]) if increasing else int(lvls[i-1]) - lvl
            if not diff in range(1, 4):
                safe = False
                break
    if safe:
        safes_count += 1

print(safes_count)