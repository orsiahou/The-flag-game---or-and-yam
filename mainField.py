import pygame
import const

def start_matrix():
    row = []
    matrix = []
    for i in range(const.NUM_OF_ROWS):
        for j in range(const.NUM_OF_COLS):
            row.append(const.EMPTY_CELL)
        matrix.append(row)
    return matrix


def put_flag():
    for i in range(const.NUM_OF_ROWS - 3, const.NUM_OF_ROWS):
        for j in range(const.NUM_OF_COLS - 4, const.NUM_OF_COLS):
            const.matrix[i][j] = const.FLAG
#
# def put_trees(my_list):
#     for i in range(len(list)):
#         row = my_list[i][0]
#         col = my_list[i][1]
#         for j in range(row, row + 2):
#             const.matrix[row][col] = const.TREE


def put_boom(my_list):
    for i in range(len(my_list)):
        row = my_list[i][0]
        col = my_list[i][1]
        for j in range(col, col + 3):
            const.matrix[row][j] = const.BOOM

def solider_matrix():
    for i in range(4):
        for j in range(2):
            const.solider_matrix[i][j] == const.SOLIDER

def game_matrix(trees_list, boom_list):
    # put_trees(trees_list)
    put_boom(boom_list)
    put_flag()


def where_to_go():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_END:
                return const.RIGHT
            elif event.key == pygame.K_HOME:
                return const.LEFT
            elif event.key == pygame.K_UP:
                return const.UP
            elif event.key == pygame.K_DOWN:
                return const.DOWN


def want_to_show_boom():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                return True
    return False


def touch_flag():
    mini_list = []
    index_list = []
    for i in range(const.NUM_OF_ROWS):
        for j in range(const.NUM_OF_COLS):
            if const.matrix[i][j] != const.FLAG and (
                    const.matrix[i - 1][j] == const.FLAG or const.matrix[i][j + 1] == const.FLAG):
                mini_list.append(i)
                mini_list.append(j)
        index_list.append(mini_list.copy())
        mini_list.clear()
    return index_list

def touch_boom():
    mini_list = []
    index_list = []
    for i in range(const.NUM_OF_ROWS):
        for j in range(const.NUM_OF_COLS):
            if const.matrix[i][j] != const.BOOM and (
                    const.matrix[i - 1][j] == const.BOOM or const.matrix[i][j + 1] == const.BOOM):
                mini_list.append(i)
                mini_list.append(j)
        index_list.append(mini_list.copy())
        mini_list.clear()
    return index_list

#
# def touch_flag():
#     mini_list = []
#     index_list = []
#     for i in range(const.NUM_OF_ROWS):
#         for j in range(const.NUM_OF_COLS):
#             if const.matrix[i][j] != const.FLAG and (const.matrix[i-1][j] == const.FLAG or const.matrix[i][j+1] == const.FLAG):
#                 mini_list.append(i)
#                 mini_list.append(j)
#         index_list.append(mini_list.copy())
#         mini_list.clear()
#     return index_list
#
# def touch_boom():
#     mini_list = []
#     index_list = []
#     for i in range(const.NUM_OF_ROWS):
#         for j in range(const.NUM_OF_COLS):
#             if const.matrix[i][j] != const.BOOM and (const.matrix[i - 1][j] == const.BOOM or const.matrix[i][j + 1] == const.BOOM):
#                 mini_list.append(i)
#                 mini_list.append(j)
#         index_list.append(mini_list.copy())
#         mini_list.clear()
#     return index_list

