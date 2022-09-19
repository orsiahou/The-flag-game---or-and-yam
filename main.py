import pygame
import const
import mainField
import solider
import Screen

screen = pygame.display.set_mode(const.size)
mainField.solider_matrix()

finish = False
while not finish:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print('111')



# finish_the_game = False
# screen = pygame.display.set_mode(const.size)
#
# mainField.solider_matrix()
# while not finish_the_game:
#     Screen.grass_screen2(screen)
#
#     solider.move()
#     if solider.step_on_bomb():
#         Screen.losser(screen)
#         Screen.loss(screen)
#         finish = True
#     if solider.step_on_flag():
#         Screen.win(screen)
#         finish = True
#     if mainField.want_to_show_boom():
#         Screen.grid_screen(screen)




