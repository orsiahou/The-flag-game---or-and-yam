import mainField
import pygame
pygame.font.init()

WELCOME_FONT = pygame.font.SysFont("comicsans", 20)
TEXT_FONT = pygame.font.SysFont("comicsans", 100)

BACKGROUND_COLOR = (60, 156, 54)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000
NUM_OF_ROWS = 25
NUM_OF_COLS = 50
EMPTY_CELL = "EMPTY"
TREE = "TREE"
BOOM = "BOOM"
SOLIDER = "SOLIDER"
FLAG = "FLAG"
START_MATRIX = mainField.start_matrix()
NUM_OF_BOOMS = 20
NUM_OF_TREES = 20

COLOR_TO_IGNOR = ()
size = (WINDOW_WIDTH, WINDOW_HEIGHT)

UP = "UP"
DOWN = "DOWN"
LEFT = "LEFT"
RIGHT = "RIGHT"

matrix = START_MATRIX
solider_matrix = START_MATRIX