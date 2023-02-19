import pygame
import numpy as np

# window size 
window_size = (500, 500)

# cube colors 
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
yellow= pygame.Color(255, 255, 0)
orange = pygame.Color(255, 165, 0)
white = pygame.Color(255, 255, 255)

pygame.init()

pygame.display.set_caption("Rubiks Cube Game")
game_window = pygame.display.set_mode(window_size)

fps = pygame.time.Clock()

score = 0 

# function to display/show the score text.
def display_score():

    # Creates the font object with font and size.
    score_font = pygame.font.SysFont("arial", 20)
    # Score surface object that renders the font + score. 
    score_surface = score_font.render('Score : ' + str(score), True, white)

    # Creates a rectangular object that fits the score text object.
    score_rect = score_surface.get_rect()
    # Renders the text in window.
    game_window.blit(score_surface, score_rect)


cube_dict = {

    "front": np.array(["r", "r", "r", "r", "r", "r", "r", "r", "r"]).reshape(3, 3),
    "back": np.array(["r", "r", "r", "r", "r", "r", "r", "r", "r"]).reshape(3, 3),
    "top": np.array(["r", "r", "r", "r", "r", "r", "r", "r", "r"]).reshape(3, 3),
    "right": np.array(["r", "r", "r", "r", "r", "r", "r", "r", "r"]).reshape(3, 3),
    "left": np.array(["r", "r", "r", "r", "r", "r", "r", "r", "r"]).reshape(3, 3),
    "bottom": np.array(["r", "r", "r", "r", "r", "r", "r", "r", "r"]).reshape(3, 3)

}

def draw_cube(cube_dict: dict, cube_width: int, cube_height: int, margin: int):

    center_x = (window_size[0] / 2) - (cube_width / 2)
    center_y = (window_size[1] / 2) - (cube_height / 2)

    for i in cube_dict:

        if i == "front":

            col_pos = center_x - cube_width - margin
            row_pos = center_y - cube_height - margin

            for y in cube_dict[i]:

                # resets col pos 
                col_pos = center_x - cube_width - margin

                for x in y:
                    print(col_pos, row_pos)
                    pygame.draw.rect(game_window, white, pygame.Rect(col_pos, row_pos, cube_width, cube_height))
                    col_pos += cube_width + margin

                row_pos += cube_height + margin

        if i == "top":

            col_pos = center_x - cube_width - margin 
            row_pos = center_y - cube_height - margin - ((margin + cube_height) * 3)

            for y in cube_dict[i]:

                # resets col pos 
                col_pos = center_x - cube_width - margin

                for x in y:
                    print(col_pos, row_pos)
                    pygame.draw.rect(game_window, red, pygame.Rect(col_pos, row_pos, cube_width, cube_height))
                    col_pos += cube_width + margin

                row_pos += cube_height + margin
                



while True:

    game_window.fill(pygame.Color(0, 0, 0))
    display_score()

    #pygame.draw.rect(game_window, white, pygame.Rect(245, 245, 10, 10))

    

    

    draw_cube(cube_dict, 20, 20, margin= 5)

    pygame.display.update()

    fps.tick(4)

    # to stop the game from craching and a way to close the game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:

                pygame.quit()
                quit()