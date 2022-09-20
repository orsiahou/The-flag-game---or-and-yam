import pygame
import const
import mainField
import screen
import solider

_screen = pygame.display.set_mode(const.size)
mainField.solider_matrix()
random_grass_list = screen.random_grass()
random_boom_list = screen.random_grass()
screen.grass_screen2(_screen, random_grass_list)
screen.move_solider(_screen)


while True:
    #game_events = pygame.event.get()

    #if len(game_events) > 0:
        #event = game_events.pop(0)
    #else:
        #continue
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and solider.can_move_right():
                screen.grass_screen2(_screen, random_grass_list)
                solider.move_right()
                if solider.step_on_bomb():
                    screen.move_solider(_screen)
                    screen.losser(_screen)
                    screen.loss(_screen)
                elif solider.step_on_flag():
                    screen.win(_screen)
                else:
                    screen.move_solider(_screen)
            elif event.key == pygame.K_LEFT and solider.can_move_left():
                screen.grass_screen2(_screen, random_grass_list)
                solider.move_left()
                if solider.step_on_bomb():
                    screen.move_solider(_screen)
                    screen.losser(_screen)
                    screen.loss(_screen)
                elif solider.step_on_flag():
                    screen.win(_screen)
                else:
                    screen.move_solider(_screen)
            elif event.key == pygame.K_UP:
                screen.grass_screen2(_screen, random_grass_list)
                solider.move_up()
                if solider.step_on_bomb():
                    screen.move_solider(_screen)
                    screen.losser(_screen)
                    screen.loss(_screen)
                elif solider.step_on_flag():
                    screen.win(_screen)
                else:
                    screen.move_solider(_screen)
            elif event.key == pygame.K_DOWN:
                screen.grass_screen2(_screen, random_grass_list)
                solider.move_down()
                if solider.step_on_bomb():
                    screen.move_solider(_screen)
                    screen.losser(_screen)
                    screen.loss(_screen)
                elif solider.step_on_flag():
                    screen.win(_screen)
                    screen.move_solider(_screen)
                else:
                    screen.move_solider(_screen)
            elif event.key == pygame.K_KP_ENTER:
                screen.grid_screen(_screen, random_boom_list)
