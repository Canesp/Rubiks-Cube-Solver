import pygame
import numpy as np

# window size 
window_size = (500, 500)

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
    score_surface = score_font.render('Score : ' + str(score), True, color_dict["w"])

    # Creates a rectangular object that fits the score text object.
    score_rect = score_surface.get_rect()
    # Renders the text in window.
    game_window.blit(score_surface, score_rect)

# cube colors 
color_dict = {

    "r": pygame.Color(255, 0, 0),
    "g": pygame.Color(0, 255, 0),
    "b": pygame.Color(0, 0, 255),
    "y": pygame.Color(255, 255, 0),
    "o": pygame.Color(255, 165, 0),
    "w": pygame.Color(255, 255, 255)
}

# dict with matrix of cubes sides in rows and cols. 
cube_dict = {

    "front": np.array(["r", "r", "w", "r", "r", "r", "r", "r", "r"]).reshape(3, 3),
    "back": np.array(["r", "r", "r", "r", "r", "r", "r", "r", "r"]).reshape(3, 3),
    "top": np.array(["r", "r", "r", "r", "r", "r", "r", "r", "r"]).reshape(3, 3),
    "right": np.array(["r", "r", "r", "r", "g", "r", "r", "r", "r"]).reshape(3, 3),
    "left": np.array(["r", "r", "r", "r", "r", "r", "r", "r", "r"]).reshape(3, 3),
    "bottom": np.array(["r", "r", "r", "b", "r", "r", "r", "r", "r"]).reshape(3, 3)

}

def draw_cubes(cube_array: np.array, cube_width: int, cube_height: int, margin: int, start_pos: tuple):

    # sets start pos (top right of cube).
    col_pos = start_pos[0]
    row_pos = start_pos[1]

    # loops through the array.
    for y in cube_array:

        # resets col pos.
        col_pos = start_pos[0]

        for x in y:
            
            # Draw the cubes.
            pygame.draw.rect(game_window, color_dict[x], pygame.Rect(col_pos, row_pos, cube_width, cube_height))
            col_pos += cube_width + margin # moves one step in col.

        # moves down on row.
        row_pos += cube_height + margin

def display_cube(cube_dict: dict, cube_width: int, cube_height: int, margin: int):

    center_x = (window_size[0] / 2) - (cube_width / 2)
    center_y = (window_size[1] / 2) - (cube_height / 2)

    for i in cube_dict:

        if i == "front":
            # Calculate start pos for front side.
            col_pos = center_x - cube_width - margin
            row_pos = center_y - cube_height - margin

            # Draw the side.
            draw_cubes(cube_dict[i], cube_width, cube_height, margin, start_pos=(col_pos, row_pos))

        if i == "top":
            # Calculate start pos for top side.
            col_pos = center_x - cube_width - margin 
            row_pos = center_y - cube_height - margin - ((margin + cube_height) * 3)

            # Draw the side.
            draw_cubes(cube_dict[i], cube_width, cube_height, margin, start_pos=(col_pos, row_pos))

        if i == "bottom":
            # Calculate start pos for bottom side.
            col_pos = center_x - cube_width - margin 
            row_pos = center_y - cube_height - margin + ((margin + cube_height) * 3)

            # Draw the side.
            draw_cubes(cube_dict[i], cube_width, cube_height, margin, start_pos=(col_pos, row_pos))
        
        if i == "back":
            # Calculate start pos for back side.
            col_pos = center_x - cube_width - margin 
            row_pos = center_y - cube_height - margin + ((margin + cube_height) * 6)

            # Draw the side.
            draw_cubes(cube_dict[i], cube_width, cube_height, margin, start_pos=(col_pos, row_pos))

        if i == "right":
            # Calculate start pos for right side.
            col_pos = center_x - cube_width - margin + ((margin + cube_width) * 3)
            row_pos = center_y - cube_height - margin 

            # Draw the side.
            draw_cubes(cube_dict[i], cube_width, cube_height, margin, start_pos=(col_pos, row_pos))

        if i == "left":
            # Calculate start pos for left side.
            col_pos = center_x - cube_width - margin - ((margin + cube_width) * 3)
            row_pos = center_y - cube_height - margin 

            # Draw the side.
            draw_cubes(cube_dict[i], cube_width, cube_height, margin, start_pos=(col_pos, row_pos))

    

        
                



while True:

    game_window.fill(pygame.Color(0, 0, 0))
    display_score()

    #pygame.draw.rect(game_window, white, pygame.Rect(245, 245, 10, 10))

    

    

    display_cube(cube_dict, 20, 20, margin= 5)

    pygame.display.update()

    fps.tick(4)

    # to stop the game from craching and a way to close the game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:

                pygame.quit()
                quit()