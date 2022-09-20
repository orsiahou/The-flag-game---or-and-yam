import const
import mainField

SOLIDER_POSITION = [0, 0]
def move_right():
    if SOLIDER_POSITION[0] != 50:
        SOLIDER_POSITION[0] += 1

def move_left():
    if SOLIDER_POSITION[0] != 0:
        SOLIDER_POSITION[0] -= 1

def move_up():
    if SOLIDER_POSITION[1] != 0:
        SOLIDER_POSITION[1] -= 1

def move_down():
    if SOLIDER_POSITION[1] != 50:
        SOLIDER_POSITION[1] += 1









def where_solider():
    index = []
    for i in range(const.NUM_OF_ROWS):
        for j in range(const.NUM_OF_COLS):
            if const.solider_matrix[i][j] == const.SOLIDER:
                index.append([i, j])
    return index


def can_move_up():
    for i in range(len(where_solider())):
        if where_solider()[i][0] == 0:
            return False
    return True


def can_move_down():
    for i in range(len(where_solider())):
        if where_solider()[i][0] == const.NUM_OF_ROWS - 1:
            return False
    return True


def can_move_right():
    for i in range(len(where_solider())):
        if where_solider()[i][1] == const.NUM_OF_COLS - 1:
            return False
    return True


def can_move_left():
    for i in range(len(where_solider())):
        if where_solider()[i][1] == 0:
            return False
    return True


def move():
    if mainField.where_to_go() == const.UP and can_move_up():
        for i in range(len(where_solider())):
            const.solider_matrix[where_solider()[i][0]][where_solider()[i][1]] = const.EMPTY_CELL
            const.solider_matrix[where_solider()[i][0] - 1][where_solider()[i][1]] = const.SOLIDER
    if mainField.where_to_go() == const.DOWN and can_move_down():
        for i in range(len(where_solider())):
            const.solider_matrix[where_solider()[i][0]][where_solider()[i][1]] = const.EMPTY_CELL
            const.solider_matrix[where_solider()[i][0] + 1][where_solider()[i][1]] = const.SOLIDER
    if mainField.where_to_go() == const.RIGHT and can_move_right():
        for i in range(len(where_solider())):
            const.solider_matrix[where_solider()[i][0]][where_solider()[i][1]] = const.EMPTY_CELL
            const.solider_matrix[where_solider()[i][0]][where_solider()[i][1] + 1] = const.SOLIDER
    if mainField.where_to_go() == const.LEFT and can_move_left():
        for i in range(len(where_solider())):
            const.solider_matrix[where_solider()[i][0]][where_solider()[i][1]] = const.EMPTY_CELL
            const.solider_matrix[where_solider()[i][0]][where_solider()[i][1] - 1] = const.SOLIDER
'''
def move_right():
    solider_index = where_solider()
    for i in range(len(solider_index)):
        if i % 2 == 0:
            const.solider_matrix[solider_index[i][0]][solider_index[i][1]] = const.EMPTY_CELL
            const.solider_matrix[solider_index[i][0]][solider_index[i][1] + 2] = const.SOLIDER


def move_left():
    solider_index = where_solider()
    for i in range(len(solider_index)):
        if i % 2 != 0:
            const.solider_matrix[solider_index[i][0]][solider_index[i][1]] = const.EMPTY_CELL
            const.solider_matrix[solider_index[i][0]][solider_index[i][1] - 2] = const.SOLIDER


def move_up():
<<<<<<< HEAD
    solider_index = where_solider()
    for i in range(2):
            const.solider_matrix[solider_index[i][0]][solider_index[i][1]] = const.EMPTY_CELL
            const.solider_matrix[solider_index[i][0] - 4][solider_index[i][1]] = const.SOLIDER
=======
    if where_solider()[1][0] > 0:
        solider_index = where_solider()
        for i in range(2):
                const.solider_matrix[solider_index[i][0]][solider_index[i][1]] = const.EMPTY_CELL
                const.solider_matrix[solider_index[i][0]-2][solider_index[i][1]] = const.SOLIDER
>>>>>>> 5cfb47fc5b1fe515770cf180b12fc747b7a0a94b


def move_down():
    solider_index = where_solider()
    for i in range(2):
        const.solider_matrix[solider_index[i][0]][solider_index[i][1]] = const.EMPTY_CELL
        const.solider_matrix[solider_index[i][0] + 4][solider_index[i][1]] = const.SOLIDER

'''

def index_of_Rleg():
    index_Rleg = [SOLIDER_POSITION[0]+1, SOLIDER_POSITION[1]+3]
    return index_Rleg


def index_of_Lleg():
    index_Lleg = [SOLIDER_POSITION[0], SOLIDER_POSITION[1]+3]
    return index_Lleg


def index_of_Rhead():
    index_Rhead = [SOLIDER_POSITION[0]+1, SOLIDER_POSITION[1]]
    return index_Rhead


def index_of_Lhead():
    index_Lhead = [SOLIDER_POSITION[0], SOLIDER_POSITION[1]]
    return index_Lhead


def index_of_Rsholder():
    index_Rsholder = [SOLIDER_POSITION[0]+1, SOLIDER_POSITION[1]+1]
    return index_Rsholder


def index_of_Lsholder():
    index_Lsholder = [SOLIDER_POSITION[0], SOLIDER_POSITION[1]+1]
    return index_Lsholder
"""
def index_of_Rleg(where_is_solider):
    index_Rleg = where_is_solider()[7]
    return index_Rleg


def index_of_Lleg(where_is_solider):
    index_Lleg = where_is_solider()[6]
    return index_Lleg


def index_of_Rhead(where_is_solider):
    index_Rhead = where_is_solider()[1]
    return index_Rhead


def index_of_Lhead(where_is_solider):
    index_Lhead = where_is_solider()[0]
    return index_Lhead


def index_of_Rsholder(where_is_solider):
    index_Rsholder = where_is_solider()[3]
    return index_Rsholder


def index_of_Lsholder(where_is_solider):
    index_Lsholder = where_is_solider()[2]
    return index_Lsholder


def step_on_bomb():
    if mainField.where_to_go() == const.UP and can_move_up():
        if const.matrix[index_of_Lleg(where_solider())[0]][index_of_Lleg(where_solider())[1]] == const.BOOM or \
           const.matrix[index_of_Rleg(where_solider())[0]][index_of_Rleg(where_solider())[1]] == const.BOOM:
            return True
    if mainField.where_to_go() == const.DOWN and can_move_down():
        if const.matrix[index_of_Lleg(where_solider())[0]][index_of_Lleg(where_solider())[1]] == const.BOOM or \
           const.matrix[index_of_Rleg(where_solider())[0]][index_of_Rleg(where_solider())[1]] == const.BOOM:
            return True
    if  mainField.where_to_go() == const.RIGHT and can_move_right():
        if const.matrix[index_of_Lleg(where_solider())[0]][index_of_Lleg(where_solider())[1]] == const.BOOM or \
           const.matrix[index_of_Rleg(where_solider())[0]][index_of_Rleg(where_solider())[1]] == const.BOOM:
            return True
    if  mainField.where_to_go() == const.LEFT and can_move_left():
        if const.matrix[index_of_Lleg(where_solider())[0]][index_of_Lleg(where_solider())[1]] == const.BOOM or \
           const.matrix[index_of_Rleg(where_solider())[0]][index_of_Rleg(where_solider())[1]] == const.BOOM:
            return True


def step_on_flag():
    if mainField.where_to_go() == const.DOWN and can_move_down():
        count = 0
        if const.matrix[index_of_Rhead()[0] + 1][index_of_Rhead()[1]] == const.FLAG:
            count +=1
        if const.matrix[index_of_Lhead()[0] + 1][index_of_Lhead()[1]] == const.FLAG:
            count +=1
        if const.matrix[index_of_Rsholder()[0] + 1][index_of_Rsholder()[1]] == const.FLAG:
            count +=1
        if const.matrix[index_of_Lsholder()[0] + 1][index_of_Lsholder()[1]] == const.FLAG:
            count +=1
        if count >=2:
            return True
    if mainField.where_to_go() == const.RIGHT and can_move_right():
        count = 0
        if const.matrix[index_of_Rhead()[0]][index_of_Rhead()[1] + 1] == const.FLAG:
            count +=1
        if const.matrix[index_of_Lhead()[0]][index_of_Lhead()[1] + 1] == const.FLAG:
            count +=1
        if const.matrix[index_of_Rsholder()[0]][index_of_Rsholder()[1] + 1] == const.FLAG:
            count +=1
        if const.matrix[index_of_Lsholder()[0]][index_of_Lsholder()[1] + 1] == const.FLAG:
            count +=1
        if count >=2:
            return True
"""
