import pygame
import const
import mainField
import solider
import Screen

finish = False
while not finish:
    Screen.grass_screen2()
    Screen.move_solider()
    solider.move()
    if solider.step_on_bomb():
        Screen.losser()
        Screen.loss()
    if solider.step_on_flag():
        Screen.win()



