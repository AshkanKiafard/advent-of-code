import sys

file_name = sys.argv[1]
with open(file_name, 'r') as file:
    reports = file.read()

def can_connect(cur, prev, inc):
    if inc is None:
        inc = cur > prev
    return (cur - prev) in range(1, 4) if inc else (prev - cur) in range(1, 4)

safes_count = 0
for report in reports.split('\n'):
    lvls = [int(x) for x in report.split(' ')]
    metadata = {lvl_index : [1, None] for lvl_index in range(len(lvls))}
    all_max = 0
    for index, lvl in enumerate(lvls):
        max_len = 0
        last_inc = None
        for i in range(index-1, max(-1, index-3), -1):
            prev_lvl = lvls[i]
            prev_lvl_data = metadata[i]
            if can_connect(lvl, prev_lvl, prev_lvl_data[1]):
                if prev_lvl_data[0] > max_len:
                    max_len = prev_lvl_data[0]
                    last_inc = lvl > prev_lvl
                else:
                    if prev_lvl_data[0] == max_len and last_inc != (lvl > prev_lvl):
                        if index < len(lvls)-1:
                            nxt_lvl = lvls[index+1]
                            if can_connect(nxt_lvl, lvl, lvl > prev_lvl):
                                max_len = prev_lvl_data[0]
                                last_inc = lvl > prev_lvl
            elif prev_lvl_data[1] is not None and can_connect(lvl, prev_lvl, not prev_lvl_data[1]):
                if 1 > max_len:
                    max_len = 1
                    last_inc = lvl > prev_lvl
        metadata[index][0] = 1 + max_len
        metadata[index][1] = last_inc
        all_max = max(all_max,  1 + max_len)
    if all_max >= len(lvls) - 1:
        safes_count += 1
print(safes_count)