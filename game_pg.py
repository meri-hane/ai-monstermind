import os
import pickle
import pygame as pg

from setup import *
from solver import MastermindSolver


class Mastermind:

    def __init__(self):
        self.guesses_left = 6
        self.current_hole = 0
        self.game_status = "start"
        self.win_status = None
        self.difficulty = None
        self.pegs = 5  # Default to average difficulty
        self.guess_grid = []
        self.hint_grid = []
        self.answer = []

        FileStore = open("stored_objects/average.pickle", "rb")
        self.lookup_table = pickle.load(FileStore)
        FileStore.close()
        # FileStore = open("stored_objects/easy.pickle", "rb")
        # self.lookup_table2 = pickle.load(FileStore)
        # FileStore.close()

    def draw_front_screen(self):
        image_rect = COVER.get_rect()
        image_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        SCREEN.blit(COVER, image_rect)

        play_button_rect = pg.Rect(0, 0, 200, 50)
        play_button_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.55)
        play_button_word = SUB_TITLE_FONT.render("PLAY", True, (0, 0, 0))
        play_button_word_rect = play_button_word.get_rect(center=play_button_rect.center)
        SCREEN.blit(play_button_word, play_button_word_rect)

        howToPlay_button_rect = pg.Rect(0, 0, 200, 50)
        howToPlay_button_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.36)
        howToPlay_button_word = SUB_TITLE_FONT.render("HOW TO PLAY", True, (0, 0, 0))
        howToPlay_button_word_rect = howToPlay_button_word.get_rect(center=howToPlay_button_rect.center)
        SCREEN.blit(howToPlay_button_word, howToPlay_button_word_rect)

        aboutUs_button_rect = pg.Rect(0, 0, 200, 50)
        aboutUs_button_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.21)
        aboutUs_button_word = SUB_TITLE_FONT.render("ABOUT US", True, (0, 0, 0))
        aboutUs_button_word_rect = aboutUs_button_word.get_rect(center=aboutUs_button_rect.center)
        SCREEN.blit(aboutUs_button_word, aboutUs_button_word_rect)

        return play_button_rect, howToPlay_button_rect, aboutUs_button_rect
    
    
    def draw_difficulty_screen(self):
        image_rect = COVER1.get_rect()
        image_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        SCREEN.blit(COVER1, image_rect)

        easy_button_rect = pg.Rect(0, 0, 200, 50)
        easy_button_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.55)
        easy_button_word = SUB_TITLE_FONT.render("EASY", True, (0, 0, 0))
        easy_button_word_rect = easy_button_word.get_rect(center=easy_button_rect.center)
        SCREEN.blit(easy_button_word, easy_button_word_rect)

        average_button_rect = pg.Rect(0, 0, 200, 50)
        average_button_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.36)
        average_button_word = SUB_TITLE_FONT.render("AVERAGE", True, (0, 0, 0))
        average_button_word_rect = average_button_word.get_rect(center=average_button_rect.center)
        SCREEN.blit(average_button_word, average_button_word_rect)


        return easy_button_rect, average_button_rect
    
    def codemaker_difficulty_screen(self):
        image_rect = COVER1.get_rect()
        image_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        SCREEN.blit(COVER1, image_rect)

        easy_codemaker_rect = pg.Rect(0, 0, 200, 50)
        easy_codemaker_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.55)
        easy_codemaker_word = SUB_TITLE_FONT.render("EASY", True, (0, 0, 0))
        easy_codemaker_word_rect = easy_codemaker_word.get_rect(center=easy_codemaker_rect.center)
        SCREEN.blit(easy_codemaker_word, easy_codemaker_word_rect)

        average_codemaker_rect = pg.Rect(0, 0, 200, 50)
        average_codemaker_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.36)
        average_codemaker_word = SUB_TITLE_FONT.render("AVERAGE", True, (0, 0, 0))
        average_codemaker_word_rect = average_codemaker_word.get_rect(center=average_codemaker_rect.center)
        SCREEN.blit(average_codemaker_word, average_codemaker_word_rect)


        return easy_codemaker_rect, average_codemaker_rect


    def draw_how_to_play_screen(self):
    # Draw instructions image
        image_rect = INSTRUCTIONS.get_rect()
        image_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        SCREEN.blit(INSTRUCTIONS, image_rect)

        # Draw title
        title_word = GAME_FONT.render("HOW TO PLAY:", True, (241, 245, 249))
        title_rect = title_word.get_rect()
        title_rect.center = (SCREEN_WIDTH / 2.1, SCREEN_HEIGHT / 11)
        SCREEN.blit(title_word, title_rect)

        return 


    def draw_about_us_screen(self):
        image_rect = ABOUT.get_rect()
        image_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        SCREEN.blit(ABOUT, image_rect)

        title_word = GAME_FONT.render("ABOUT US:", True, (241, 245, 249))
        title_rect = title_word.get_rect()
        title_rect.center = (SCREEN_WIDTH / 2.7, SCREEN_HEIGHT / 14)
        SCREEN.blit(title_word, title_rect)

        return

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty
        if difficulty == "easy":
            self.pegs = 4
        elif difficulty == "average":
            self.pegs = 5
        self.reset_game()


    @staticmethod
    def draw_guess_grid(guess_grid, x, y):
        grid_y = y
        for row in guess_grid:
            grid_x = x
            for val in row:
                SCREEN.blit(pg.transform.scale(HOLE_BACKGROUND, (40, 40)), (grid_x - 20, grid_y - 20))
                if val:
                    pg.draw.circle(SCREEN, GUESS_COLOR_MAP[val], (grid_x, grid_y), GUESS_RADIUS)
                grid_x += 60
            grid_y += 110

    @staticmethod
    def draw_hint_grid(hint_grid, x, y, pegs):
        grid_y = y
        for row in hint_grid:
            # draw empty peg when there is no hint peg to draw
            row = [let for let in row]
            if len(row) < pegs:
                row.extend([""] * (pegs - len(row)))

            grid_x = x
            for i, val in enumerate(row):
                if i < 2:
                    SCREEN.blit(pg.transform.scale(HOLE_BACKGROUND, (30, 30)), (grid_x - 15, grid_y - 15))
                    if val:
                        pg.draw.circle(SCREEN, HINT_COLOR_MAP[val], (grid_x, grid_y), HINT_RADIUS)
                    grid_x += 60
                elif i == 2:
                    SCREEN.blit(pg.transform.scale(HOLE_BACKGROUND, (30, 30)), (grid_x - 90 - 15, grid_y + 30 - 15))
                    if val:
                        pg.draw.circle(SCREEN, HINT_COLOR_MAP[val], (grid_x - 90, grid_y + 30), HINT_RADIUS)
                    grid_x = 55
                else:
                    SCREEN.blit(pg.transform.scale(HOLE_BACKGROUND, (30, 30)), (grid_x - 15, grid_y + 60 - 15))
                    if val:
                        pg.draw.circle(SCREEN, HINT_COLOR_MAP[val], (grid_x, grid_y + 60), HINT_RADIUS)
                    grid_x += 60
            grid_y += 110

    @staticmethod
    def draw_choices(choice_grid, x, y):
        choice_rects = []
        pg.draw.rect(SCREEN, (46, 66, 77), (160, 675, 350, 400))
        for val in choice_grid:
            choice_rects.append(pg.draw.circle(SCREEN, GUESS_COLOR_MAP[val], (x, y), GUESS_RADIUS))
            x += 50
        return choice_rects

    @staticmethod
    def draw_separators():
        # draw separator between guesses and choices
        pg.draw.line(SCREEN, (0, 0, 0), (0, 670), (500, 670), 10)

        # draw separator between guess and hints
        pg.draw.line(SCREEN, (0, 0, 0), (155, 0), (155, 900), 10)

    @staticmethod
    def draw_button(x, y, word):
        button_rect = pg.Rect(0, 0, 90, 40)
        button_rect.center = x, y
        pg.draw.rect(SCREEN, (0, 0, 0), button_rect, 1)
        button_word = GAME_FONT.render(word, True, (0, 0, 0))
        button_word_rect = button_word.get_rect(center=button_rect.center)
        SCREEN.blit(button_word, button_word_rect)
        return button_rect

    def draw_win_screen(self, status):
        if status:
            status_text = TITLE_FONT.render(f"You {status}!", True, (0, 0, 0))
            status_rect = status_text.get_rect()
            status_rect.center = (SCREEN_WIDTH / 2 + 75, SCREEN_HEIGHT / 2 - 30)
            SCREEN.blit(status_text, status_rect)

            self.draw_button(SCREEN_WIDTH / 2 + 75, SCREEN_HEIGHT / 2 + 75, "RESET")

        if status == "LOSE":
            self.draw_choices(self.answer, 200, 710)

    def draw_codebreaker_screen(self):
        self.draw_guess_grid(self.guess_grid, 200, 65)
        self.draw_hint_grid(self.hint_grid, 55, 35, self.pegs)
        self.draw_choices(COLOR_CHOICES, 200, 710)
        self.draw_separators()
        self.draw_button(75, 710, "SUBMIT")

    def draw_solver_screen(self):
        self.draw_guess_grid(GUESS_GRID, 200, 65)
        self.draw_hint_grid(HINT_GRID, 55, 35, self.pegs)
        self.draw_separators()
        self.draw_choices(CODEMAKER_ANSWER, 200, 710)
        self.draw_button(75, SCREEN_HEIGHT - 40, "RESET")

    def draw_codemaker_screen(self):

        # draw explainer text
        instruction_text1 = SUB_TITLE_FONT.render("Choose a secret code", True, (0, 0, 0))
        instruction_rect1 = instruction_text1.get_rect()
        instruction_rect1.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3.5)
        SCREEN.blit(instruction_text1, instruction_rect1)

        instruction_text2 = SUB_TITLE_FONT.render("For computer to guess", True, (0, 0, 0))
        instruction_rect2 = instruction_text2.get_rect()
        instruction_rect2.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.8)
        SCREEN.blit(instruction_text2, instruction_rect2)

        # draw secret answer
        self.draw_guess_grid([CODEMAKER_ANSWER], x=SCREEN_WIDTH / 3.75, y=SCREEN_HEIGHT / 2 - 30)

        # draw choices
        self.draw_choices(COLOR_CHOICES, x=SCREEN_WIDTH / 3.75, y=SCREEN_HEIGHT / 2 + 30)

        # draw submit button
        self.draw_button(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2 + 150, word="SUBMIT")

    
    def draw_codemaker_easy_screen(self):

        # draw explainer text
        instruction_text1 = SUB_TITLE_FONT.render("Choose a secret code", True, (0, 0, 0))
        instruction_rect1 = instruction_text1.get_rect()
        instruction_rect1.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3.5)
        SCREEN.blit(instruction_text1, instruction_rect1)

        instruction_text2 = SUB_TITLE_FONT.render("For computer to guess", True, (0, 0, 0))
        instruction_rect2 = instruction_text2.get_rect()
        instruction_rect2.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2.8)
        SCREEN.blit(instruction_text2, instruction_rect2)

        # draw secret answer
        self.draw_guess_grid([CODEMAKER_ANSWER_EASY], x=SCREEN_WIDTH / 3.75, y=SCREEN_HEIGHT / 2 - 30)

        # draw choices
        self.draw_choices(COLOR_CHOICES, x=SCREEN_WIDTH / 3.75, y=SCREEN_HEIGHT / 2 + 30)

        # draw submit button
        self.draw_button(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2 + 150, word="SUBMIT")


    
    def draw_start_screen(self):
        image_rect = COVER1.get_rect()
        image_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        SCREEN.blit(COVER1, image_rect)

        breaker_button_rect = pg.Rect(0, 0, 200, 50)
        breaker_button_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.55)
        breaker_button_word = SUB_TITLE_FONT.render("SOLO MODE", True, (0, 0, 0))
        breaker_button_word_rect = breaker_button_word.get_rect(center=breaker_button_rect.center)
        SCREEN.blit(breaker_button_word, breaker_button_word_rect)

        maker_button_rect = pg.Rect(0, 0, 200, 50)
        maker_button_rect.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.36)
        maker_button_word = SUB_TITLE_FONT.render("AI MODE", True, (0, 0, 0))
        maker_button_word_rect = maker_button_word.get_rect(center=maker_button_rect.center)
        SCREEN.blit(maker_button_word, maker_button_word_rect)

        return breaker_button_rect, maker_button_rect
    

    @staticmethod
    def validate_guess(guess, ans):
        # iterates through guess and answer lists element-by-element. Whenever it finds a match,
        # removes the value from a copy of answer so that nothing is double counted.
        hints = []
        ans_temp = ans.copy()
        guess_temp = guess.copy()
        # first pass for black pegs
        for i, (guess_elem, ans_elem) in enumerate(zip(guess_temp, ans_temp)):
            if guess_elem == ans_elem:
                hints.append("B")
                ans_temp[i] = ""
                guess_temp[i] = ""

        # second pass for white pegs
        for guess_elem, ans_elem in zip(guess_temp, ans_temp):
            if guess_elem in ans_temp and guess_elem:
                hints.append("W")
                ans_temp[ans_temp.index(guess_elem)] = ""

        return hints

    def reset_game(self):
        self.game_status = "play"
        self.win_status = None
        self.guesses_left = 6
        self.current_hole = 0
        self.guess_grid = [["" for _ in range(self.pegs)] for _ in range(6)]
        self.hint_grid = [["" for _ in range(self.pegs)] for _ in range(6)]
        self.answer = random.choices(COLOR_CHOICES, k=self.pegs)


    def play(self):
        current_time = pg.time.get_ticks()
        self.game_status = "front"  # Set initial game status to "front"
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pg.mouse.get_pos()

                    # Check if the button on the front screen is clicked
                    if self.game_status == "front":
                        play_button_rect, howToPlay_button_rect, aboutUs_button_rect = self.draw_front_screen()
                        if play_button_rect.collidepoint(mouse_x, mouse_y):
                            # Set game difficulty to easy
                            self.game_status = "play"
                        elif howToPlay_button_rect.collidepoint(mouse_x, mouse_y):
                            # Set game difficulty to average
                            self.game_status = "howToPlay"
                        elif aboutUs_button_rect.collidepoint(mouse_x, mouse_y):
                            # Set game difficulty to hard
                            self.game_status = "aboutUs"
                    
                    elif self.game_status == "play":
                        breaker_button_rect, maker_button_rect = self.draw_start_screen()
                        if breaker_button_rect.collidepoint(mouse_x, mouse_y):
                            self.game_status = "difficulty"
                        elif maker_button_rect.collidepoint(mouse_x, mouse_y):
                            self.game_status = "codemaker_difficulty"


                    elif self.game_status == "difficulty":
                        easy_button_rect, average_button_rect = self.draw_difficulty_screen()
                        if easy_button_rect.collidepoint(mouse_x, mouse_y):
                            # Set game difficulty to easy
                            self.set_difficulty("easy")
                            self.game_status = "codebreaker"
                        elif average_button_rect.collidepoint(mouse_x, mouse_y):
                            # Set game difficulty to average
                            self.set_difficulty("average")
                            self.game_status = "codebreaker"

                    elif self.game_status == "codemaker_difficulty":
                        easy_codemaker_rect, average_codemaker_rect = self.codemaker_difficulty_screen()
                        if easy_codemaker_rect.collidepoint(mouse_x, mouse_y):
                            # Set game difficulty to easy
                            # self.set_difficulty("easy")
                            self.game_status = "codemaker_easy"
                        elif average_codemaker_rect.collidepoint(mouse_x, mouse_y):
                            # Set game difficulty to average
                            # self.set_difficulty("average")
                            self.game_status = "codemaker"

                    # # Check if the button on the how to play screen is clicked
                    # elif self.game_status == "how_to_play":
                    #     back_button_rect = self.draw_how_to_play_screen()
                    #     if back_button_rect.collidepoint(mouse_x, mouse_y):
                    #         self.game_status = "front"

                    # # Check if the button on the about us screen is clicked
                    # elif self.game_status == "about_us":
                    #     back_button_rect = self.draw_about_us_screen()
                    #     if back_button_rect.collidepoint(mouse_x, mouse_y):
                    #         self.game_status = "front"

                    # elif self.game_status == "start":
                    #     breaker_rect = self.draw_codebreaker()
                    #     maker_rect = self.draw_codemaker()
                    #     if breaker_rect.collidepoint(mouse_x, mouse_y):
                    #         self.game_status = "difficulty"
                    #     elif maker_rect.collidepoint(mouse_x, mouse_y):
                    #         self.game_status = "codemaker"

                    # elif self.game_status == "difficulty":
                    #     easy_rect, average_rect, hard_rect = self.draw_difficulty_screen()
                    #     if easy_rect.collidepoint(mouse_x, mouse_y):
                    #         self.set_difficulty("easy")
                    #         self.game_status = "codebreaker"
                    #     elif average_rect.collidepoint(mouse_x, mouse_y):
                    #         self.set_difficulty("average")
                    #         self.game_status = "codebreaker"
                    #     elif hard_rect.collidepoint(mouse_x, mouse_y):
                    #         self.set_difficulty("hard")
                    #         self.game_status = "codebreaker"

                    elif self.game_status == "codebreaker":
                        # choosing which colors to play
                        choice_rects = self.draw_choices(COLOR_CHOICES, 200, 710)
                        for color, rect in zip(COLOR_CHOICES, choice_rects):
                            if rect.collidepoint(mouse_x, mouse_y):
                                if self.current_hole < self.pegs:
                                    self.guess_grid[6 - self.guesses_left][self.current_hole] = color
                                    self.current_hole += 1

                        # submitting a guess
                        submit_rect = self.draw_button(75, 710, "SUBMIT")
                        if submit_rect.collidepoint(mouse_x, mouse_y):
                            if self.current_hole == self.pegs:
                                guess = self.guess_grid[6 - self.guesses_left]
                                hints = self.validate_guess(guess, self.answer)
                                random.shuffle(hints)
                                self.hint_grid[6 - self.guesses_left] = hints
                                self.guesses_left -= 1
                                self.current_hole = 0

                                if guess == self.answer:
                                    self.win_status = "WIN"

                                elif guess != self.answer and self.guesses_left == 0:
                                    self.win_status = "LOSE"

                        if self.win_status in ("WIN", "LOSE"):
                            exit_rect = self.draw_button(SCREEN_WIDTH / 2 + 75, SCREEN_HEIGHT / 2 + 75, "RESET")
                            if exit_rect.collidepoint(mouse_x, mouse_y):
                                self.reset_game()

                    elif self.game_status == "codemaker":
                        # choosing which colors to play
                        choice_rects = self.draw_choices(COLOR_CHOICES, x=SCREEN_WIDTH / 3.75, y=SCREEN_HEIGHT / 2 + 45)
                        for color, rect in zip(COLOR_CHOICES, choice_rects):
                            if rect.collidepoint(mouse_x, mouse_y):
                                if self.current_hole < 5:
                                    CODEMAKER_ANSWER[self.current_hole] = color
                                    self.current_hole += 1

                        submit_rect = self.draw_button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150, "SUBMIT")
                        if submit_rect.collidepoint(mouse_x, mouse_y):
                            if self.current_hole == 5:
                                guesses = self.lookup_table[tuple(CODEMAKER_ANSWER)]
                                self.current_hole = 0
                                for i, guess in enumerate(guesses):
                                    COMPUTER_GUESSES[i] = guess
                                    COMPUTER_HINTS[i] = self.validate_guess([let for let in guess], CODEMAKER_ANSWER)
                                self.game_status = "solver_showcase"

                    elif self.game_status == "codemaker_easy":
                        # choosing which colors to play
                        choice_rects = self.draw_choices(COLOR_CHOICES, x=SCREEN_WIDTH / 3.75, y=SCREEN_HEIGHT / 2 + 45)
                        for color, rect in zip(COLOR_CHOICES, choice_rects):
                            if rect.collidepoint(mouse_x, mouse_y):
                                if self.current_hole < 4:
                                    CODEMAKER_ANSWER_EASY[self.current_hole] = color
                                    self.current_hole += 1

                        submit_rect = self.draw_button(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 150, "SUBMIT")
                        if submit_rect.collidepoint(mouse_x, mouse_y):
                            if self.current_hole == 4:
                                guesses = self.lookup_table2[tuple(CODEMAKER_ANSWER_EASY)]
                                self.current_hole = 0
                                for i, guess in enumerate(guesses):
                                    COMPUTER_GUESSES_EASY[i] = guess
                                    COMPUTER_HINTS_EASY[i] = self.validate_guess([let for let in guess], CODEMAKER_ANSWER_EASY)
                                self.game_status = "solver_showcase"

                    elif self.game_status == "solver_showcase":
                        exit_rect = self.draw_button(50, SCREEN_HEIGHT - 40, "RESET")
                        if exit_rect.collidepoint(mouse_x, mouse_y):
                            self.reset_game()

                if self.game_status == "codebreaker":
                    # changing color choices before submitting
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_BACKSPACE:
                            if self.current_hole > 0:
                                self.current_hole -= 1
                                self.guess_grid[6 - self.guesses_left][self.current_hole] = ""

    

            SCREEN.blit(BACKGROUND, (0, 0))
            if self.game_status == "front":
                self.draw_front_screen()
            elif self.game_status == "play":
                self.draw_start_screen()
            elif self.game_status == "howToPlay":
                 self.draw_how_to_play_screen()
            elif self.game_status == "aboutUs":
                self.draw_about_us_screen()
            # elif self.game_status == "title":
            #     self.draw_difficulty_title()
            elif self.game_status == "difficulty":
                self.draw_difficulty_screen()
            elif self.game_status == "codemaker_difficulty":
                self.codemaker_difficulty_screen()
            elif self.game_status == "codebreaker":
                self.draw_codebreaker_screen()
                self.draw_win_screen(self.win_status)
            elif self.game_status == "codemaker":
                self.draw_codemaker_screen()
            elif self.game_status == "codemaker_easy":
                self.draw_codemaker_easy_screen()
            elif self.game_status == "solver_showcase":
                self.draw_solver_screen()
                if pg.time.get_ticks() - current_time > 1500:
                    i = self.current_hole
                    if COMPUTER_GUESSES[i]:
                        GUESS_GRID[i] = COMPUTER_GUESSES[i]
                        HINT_GRID[i] = COMPUTER_HINTS[i]
                        current_time = pg.time.get_ticks()
                        self.current_hole += 1

            pg.display.update()


Mastermind().play()