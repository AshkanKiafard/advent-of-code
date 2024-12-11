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
count = 1
while in_map:
    dir_name = matrix[pos[1]][pos[0]]
    direction = get_direction(dir_name)

    if pos[1]+direction[1] < len(matrix):
        if pos[0]+direction[0] < len(matrix[pos[1]+direction[1]]):
                if matrix[pos[1]+direction[1]][pos[0]+direction[0]] == "#":
                    dir_name = rotate_dir(dir_name)
        else:
            in_map = False
    else:
        in_map = False

    direction = get_direction(dir_name)
    pos = (pos[0]+direction[0], pos[1]+direction[1])

    if pos[1] < len(matrix):
        if pos[0] < len(matrix[pos[1]]):
            if matrix[pos[1]][pos[0]] == ".":
                count += 1
            matrix[pos[1]][pos[0]] = dir_name
        else:
            in_map = False
    else:
        in_map = False

    matrix[pos[1]-direction[1]][pos[0]-direction[0]] = "X"

print(count)