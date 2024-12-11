import sys

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    lists = file.read()

list1 = []
list2 = []
count = {}
for line in lists.split('\n'):
    nums = line.split(" ")
    num_1, num_2 = int(nums[0]), int(nums[3])
    list1.append(num_1)
    list2.append(num_2)
    if num_2 in count:
        count[num_2] += 1
    else:
        count[num_2] = 1

list1.sort()
list2.sort()

score = 0
for i in list1:
    if i in count:
        score += i*count[i]

print(score)