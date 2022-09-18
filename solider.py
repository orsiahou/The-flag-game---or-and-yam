import pygame
import const
import mainField


def where_solider():
    index = []
    for i in range(const.NUM_OF_ROWS):
        for j in range(const.NUM_OF_COLS):
            if const.matrix[i][j] == const.SOLIDER:
                index.append([i, j])
    return index


def can_move_up():
    for i in range(len(where_solider())):
        if where_solider()[i][0] == 0:
            return False
        if const.matrix[where_solider()[i][0] + 1][where_solider()[i][1]] == const.TREE:
            return False
    return True


def can_move_down():
    for i in range(len(where_solider())):
        if where_solider()[i][0] == const.NUM_OF_ROWS - 1:
            return False
        if const.matrix[where_solider()[i][0] - 1][where_solider()[i][1]] == const.TREE:
            return False
    return True


def can_move_right():
    for i in range(len(where_solider())):
        if where_solider()[i][1] == const.NUM_OF_COLS - 1:
            return False
        if const.matrix[where_solider()[i][0]][where_solider()[i][1] + 1] == const.TREE:
            return False
    return True


def can_move_left():
    for i in range(len(where_solider())):
        if where_solider()[i][1] == 0:
            return False
        if const.matrix[where_solider()[i][0]][where_solider()[i][1] - 1] == const.TREE:
            return False
    return True


def move():
    if mainField.where_to_go() == const.UP and can_move_up():
        for i in range(len(where_solider())):
            const.matrix[where_solider()[i][0]][where_solider()[i][1]] = const.EMPTY_CELL
            const.matrix[where_solider()[i][0] + 1][where_solider()[i][1]] = const.SOLIDER
    if mainField.where_to_go() == const.DOWN and can_move_down():
        for i in range(len(where_solider())):
            const.matrix[where_solider()[i][0]][where_solider()[i][1]] = const.EMPTY_CELL
            const.matrix[where_solider()[i][0] - 1][where_solider()[i][1]] = const.SOLIDER
    if mainField.where_to_go() == const.RIGHT and can_move_right():
        for i in range(len(where_solider())):
            const.matrix[where_solider()[i][0]][where_solider()[i][1]] = const.EMPTY_CELL
            const.matrix[where_solider()[i][0]][where_solider()[i][1] + 1] = const.SOLIDER
    if mainField.where_to_go() == const.LEFT and can_move_left():
        for i in range(len(where_solider())):
            const.matrix[where_solider()[i][0]][where_solider()[i][1]] = const.EMPTY_CELL
            const.matrix[where_solider()[i][0]][where_solider()[i][1] - 1] = const.SOLIDER
