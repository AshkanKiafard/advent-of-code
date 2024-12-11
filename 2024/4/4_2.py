import sys
from ctypes import c_char

H = "H"
V = "V"
DR = "DR"
DL = "DL"

file_name = sys.argv[1]

with open(file_name, 'r') as file:
    input_puzzle = file.read()

def word_search(puzzle, word):
    lines = puzzle.split("\n")
    matrix = [[[] for _ in line] for line in lines]
    for l_index, line in enumerate(lines):
        for c_index, char in enumerate(line):
            char_data = matrix[l_index][c_index]
            if c_index < len(line) - 1:
                right_char = line[c_index + 1]
                if word.find(right_char) == word.find(char) + 1 and (char == word[0] or [word.find(char), H] in char_data):
                    matrix[l_index][c_index + 1].append([word.find(right_char), H])
            if l_index < len(lines) - 1:
                bottom_char = lines[l_index + 1][c_index]
                if word.find(bottom_char) == word.find(char) + 1 and (char == word[0] or [word.find(char), V] in char_data):
                    matrix[l_index + 1][c_index].append([word.find(bottom_char), V])
                if c_index < len(lines[l_index + 1]) - 1:
                    diag_right_char = lines[l_index + 1][c_index + 1]
                    if word.find(diag_right_char) == word.find(char) + 1 and (char == word[0] or [word.find(char), DR] in char_data):
                        matrix[l_index + 1][c_index + 1].append([word.find(diag_right_char), DR])
                        if char == "A":
                            matrix[l_index][c_index].append(DR)
                if c_index > 0:
                    diag_left_char = lines[l_index + 1][c_index - 1]
                    if word.find(diag_left_char) == word.find(char) + 1 and (char == word[0] or [word.find(char), DL] in char_data):
                        matrix[l_index + 1][c_index - 1].append([word.find(diag_left_char), DL])
                        if char == "A":
                            matrix[l_index][c_index].append(DL)
    return matrix

matrix1 = word_search(input_puzzle, "SAM")
matrix2 = word_search(input_puzzle, "MAS")

count = 0
for il, line in enumerate(matrix1):
    for ic, char_data in enumerate(line):
        all_data = char_data + matrix2[il][ic]
        if DR in all_data and DL in all_data:
            count += 1

print(count)
