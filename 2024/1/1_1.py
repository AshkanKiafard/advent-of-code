import sys

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    lists = file.read()

list1 = []
list2 = []
for line in lists.split('\n'):
    nums = line.split(" ")
    num_1, num_2 = int(nums[0]), int(nums[3])
    list1.append(num_1)
    list2.append(num_2)

list1.sort()
list2.sort()

dis = 0
for i in range(len(list1)):
    dis += list1[i] - list2[i] if list1[i] >= list2[i] else list2[i] - list1[i]

print(dis)