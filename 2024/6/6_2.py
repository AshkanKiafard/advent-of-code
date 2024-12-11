import sys

if len(sys.argv) > 1:
    file_name = sys.argv[1]

    with open(file_name, 'r') as file:
        input = file.read()
else:
    input = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#..."""

def get_direction(d):
    match d:
        case Direction.UP:
            return (0, -1)
        case Direction.RIGHT:
            return (1, 0)
        case Direction.DOWN:
            return (0, 1)
        case Direction.LEFT:
            return (-1, 0)

def rotate_dir(d):
    match d:
        case Direction.UP:
            return Direction.RIGHT
        case Direction.RIGHT:
            return Direction.DOWN
        case Direction.DOWN:
            return Direction.LEFT
        case Direction.LEFT:
            return Direction.UP

class Direction:
    UP = "^"
    RIGHT = ">"
    LEFT = "<"
    DOWN = "v"

DIRECTIONS = [Direction.UP, Direction.RIGHT, Direction.LEFT, Direction.DOWN]

matrix = []
pos = (0,0)
for li, line in enumerate(input.splitlines()):
    line_list = []
    for ci, char in enumerate(line):
        if char in DIRECTIONS:
            pos = (ci,li)
        line_list.append(char)
    matrix.append(line_list)

in_map = True
dir_name = ""
direction = (0, 0)
count = 0
memory = []
while in_map:
    dir_name = matrix[pos[1]][pos[0]]
    memory.append((pos, dir_name))
    obstacle_ahead = False

    direction = get_direction(dir_name)

    if pos[1]+direction[1] < len(matrix):
        if pos[0]+direction[0] < len(matrix[pos[1]+direction[1]]):
                if matrix[pos[1]+direction[1]][pos[0]+direction[0]] == "#":
                    obstacle_ahead = True
                    dir_name = rotate_dir(dir_name)
        else:
            in_map = False
    else:
        in_map = False

    if not obstacle_ahead:
        rotated_dir = rotate_dir(dir_name)
        rotated_direction = get_direction(rotated_dir)
        if rotated_direction[0] == 0:
            for i in range(pos[1], (-1 if rotated_direction[1] == -1 else len(matrix)), rotated_direction[1]):
                if matrix[i][pos[0]] == "X":
                    if ((pos[0], i), rotated_dir) in memory:
                        print(pos, dir_name)
                        count += 1
                        break
        elif rotated_direction[1] == 0:
            for i in range(pos[0], (-1 if rotated_direction[0] == -1 else len(matrix[pos[1]])), rotated_direction[0]):
                if matrix[pos[1]][i] == "X":
                    if ((i, pos[1]), rotated_dir) in memory:
                        count += 1
                        print(pos, dir_name)
                        break

    direction = get_direction(dir_name)
    pos = (pos[0]+direction[0], pos[1]+direction[1])

    if pos[1] < len(matrix):
        if pos[0] < len(matrix[pos[1]]):
            matrix[pos[1]][pos[0]] = dir_name
        else:
            in_map = False
    else:
        in_map = False

    matrix[pos[1]-direction[1]][pos[0]-direction[0]] = "X"

print(count)