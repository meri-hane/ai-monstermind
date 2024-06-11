import sys
import random
import pygame as pg
import gif_pygame

pg.init()
pg.display.set_caption("Mastermind")


# screen background globals
SCREEN_WIDTH = 475
SCREEN_HEIGHT =  850
LOADING_SCREEN = gif_pygame.load("./assets/loading.gif", loops=1)
BACKGROUND = pg.transform.scale(pg.image.load("assets/background1.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
COVER = pg.transform.scale(pg.image.load("assets/cover.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
COVER1 = pg.transform.scale(pg.image.load("assets/cover1.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
INSTRUCTIONS = pg.transform.scale(pg.image.load("assets/howtoplay.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
ABOUT = pg.transform.scale(pg.image.load("assets/devs.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
HOLE_BACKGROUND = pg.image.load("assets/peg.png")
SCREEN = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_icon(pg.image.load("./assets/ICON.png").convert_alpha())
GAME_FONT = pg.font.Font("assets/KronaOne.ttf", 42)
TEXT_FONT = pg.font.Font("assets/Poppins-Bold.ttf", 20)
TITLE_FONT = pg.font.Font("assets/OstrichSans-Black.otf", 100)
SUB_TITLE_FONT = pg.font.Font("assets/KronaOne.ttf", 20)

# game board globals
GUESS_GRID = [["" for _ in range(5)] for _ in range(6)]
HINT_GRID = [["" for _ in range(5)] for _ in range(6)]
GUESS_GRID_EASY = [["" for _ in range(4)] for _ in range(6)]
HINT_GRID_EASY = [["" for _ in range(4)] for _ in range(6)]
COLOR_CHOICES = ["R", "G", "B", "Y", "P", "O"]
GUESS_RADIUS = 25
HINT_RADIUS = 15
GUESS_COLOR_MAP = {"R": (255, 0, 0),
                    "G": (0, 255, 0),
                    "B": (0, 0, 255),
                    "Y": (255, 255, 0),
                    "P": (255, 0, 255),
                    "O": (254, 126, 15)}

HINT_COLOR_MAP = {"B": (0, 0, 0),
                    "W": (255, 255, 255),
                    "": (1, 122, 1)}

# game state globals
ANSWER = random.choices(COLOR_CHOICES, k=5)
CODEMAKER_ANSWER = ["", "", "", "", ""]
COMPUTER_GUESSES = ["", "", "", "", ""] * 5
COMPUTER_HINTS = ["", "", "", "", ""] * 5

# for easy mode  
ANSWER_EASY = random.choices(COLOR_CHOICES, k=4)
CODEMAKER_ANSWER_EASY = ["", "", "", ""]
COMPUTER_GUESSES_EASY= ["", "", "", ""] * 4
COMPUTER_HINTS_EASY = ["", "", "", ""] * 4
