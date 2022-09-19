import pygame
import const
import mainField
import Screen
import solider

screen = pygame.display.set_mode(const.size)
mainField.solider_matrix()
Screen.grass_screen2(screen)

for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT and solider.can_move_right():
            solider.move_right()
            if solider.step_on_bomb():
                Screen.move_solider(screen)
                Screen.losser(screen)
                Screen.loss(screen)
            elif solider.step_on_flag():
                Screen.win(screen)
            Screen.move_solider(screen)
        elif event.key == pygame.K_LEFT and solider.can_move_left():
            solider.move_left()
            if solider.step_on_bomb():
                Screen.move_solider(screen)
                Screen.losser(screen)
                Screen.loss(screen)
            elif solider.step_on_flag():
                Screen.win(screen)
            Screen.move_solider(screen)
        elif event.key == pygame.K_UP:
            solider.move_up()
            if solider.step_on_bomb():
                Screen.move_solider(screen)
                Screen.losser(screen)
                Screen.loss(screen)
            elif solider.step_on_flag():
                Screen.win(screen)
            Screen.move_solider(screen)
        elif event.key == pygame.K_DOWN:
            solider.move_down()
            if solider.step_on_bomb():
                Screen.move_solider(screen)
                Screen.losser(screen)
                Screen.loss(screen)
            elif solider.step_on_flag():
                Screen.win(screen)
                Screen.move_solider(screen)
        elif event.key == pygame.K_ENTER:
            Screen.grid_screen()
