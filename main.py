import pygame
import const
import mainField
import solider
import Screen

finish = False
screen = pygame.display.set_mode(const.size)
mainField.solider_matrix()
while not finish:
    Screen.grass_screen2(screen)

    solider.move(screen)
    if solider.step_on_bomb():
        Screen.losser(screen)
        Screen.loss(screen)
        finish = True
    if solider.step_on_flag():
        Screen.win(screen)
        finish = True
    if mainField.want_to_show_boom():
        Screen.grid_screen(screen)




