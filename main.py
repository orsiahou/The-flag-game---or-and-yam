import pygame
import const
import mainField
import screen
import solider

_screen = pygame.display.set_mode(const.size)
mainField.solider_matrix()
screen.grass_screen2(_screen)


while True:
    game_events = pygame.event.get()

    if len(game_events) > 0:
        event = game_events.pop(0)
    else:
        continue

    if event.type == pygame.QUIT:
        break

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT and solider.can_move_right():
            solider.move_right()
            if solider.step_on_bomb():
                screen.move_solider(_screen)
                screen.losser(_screen)
                screen.loss(_screen)
            elif solider.step_on_flag():
                screen.win(_screen)
            screen.move_solider(_screen)
        elif event.key == pygame.K_LEFT and solider.can_move_left():
            solider.move_left()
            if solider.step_on_bomb():
                screen.move_solider(_screen)
                screen.losser(_screen)
                screen.loss(_screen)
            elif solider.step_on_flag():
                screen.win(_screen)
            screen.move_solider(_screen)
        elif event.key == pygame.K_UP:
            solider.move_up()
            if solider.step_on_bomb():
                screen.move_solider(_screen)
                screen.losser(_screen)
                screen.loss(_screen)
            elif solider.step_on_flag():
                screen.win(_screen)
            screen.move_solider(_screen)
        elif event.key == pygame.K_DOWN:
            solider.move_down()
            if solider.step_on_bomb():
                screen.move_solider(_screen)
                screen.losser(_screen)
                screen.loss(_screen)
            elif solider.step_on_flag():
                screen.win(_screen)
                screen.move_solider(_screen)
        elif event.key == pygame.K_ENTER:
            screen.grid_screen()
