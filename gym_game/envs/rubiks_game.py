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

# list if all side names
side_list = ["front", "back", "top", "right", "left", "bottom"]

def generate_cube(color_dict: dict, side_names: list):

    # list that holds all colors for the cube.
    cube_list = []
    # dict that holds all cube information.
    cube_dict = {}

    # fills the list with colors 
    for i in color_dict:

        for _ in range(9):

            cube_list.append(i)

    # shuffles the list for random 
    np.random.shuffle(cube_list)
    
    num_cubes = int(len(cube_list) / len(side_names))

    for x, i in enumerate(side_names):

        cube_dict[i] = np.array(cube_list[(x * num_cubes):(num_cubes * (x + 1))]).reshape(3, 3)

    return cube_dict

cube_dict = generate_cube(color_dict, side_list)

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



def cube_movement(cube_dict: dict, rules: list, col: int, forwards: bool, T: bool):

    # Creates a new cube dict.
    new_cube = {}

    # checks what way to rotate cube and switches f and t. 
    if forwards == True:
        f, t = 1, 0

    else:
        f, t = 0, 1

    # loops through the rules list. 
    for i in rules:
        
        # if one of the rules have rotate in it. 
        if i[0] == "rotate":

            # Creates a new matrix and rotates it 90 deg forward or backwards.
            new_vector = np.rot90(cube_dict[i[1]], k=i[2], axes=(0, 1))

            # add the matrix to new cube dict.
            new_cube[i[1]] = new_vector
        
        # if rules dont have rotate.
        else:

            if T == True:

                # creates a new vector dict. 
                vector_dict = {}

                # gets the range of vector (len of row).
                n = range(0, len(cube_dict[i[f]][f]))

                # adds the row of new cube to dict. 
                vector_dict[col] = cube_dict[i[f]].T[col]
                
                # Creates a list of all columns. [0, 1, 2]
                m = list(n)
                # Removes the chosen column.
                m.remove(col)

                # loops throg the remaining columns.
                for x in m:
                    
                    # add the remaing columns to new vector dict.
                    vector_dict[x] = cube_dict[i[t]].T[x]

                # sorts and creates a new matrix based on vector dict (sorts so rows goes in right order).
                new_vector = np.array([vector_dict[y] for y in range(len(vector_dict))]).reshape(3, 3).T

                # add new matrix to new cube dict.
                new_cube[i[t]] = new_vector
            
            else: 

                # creates a new vector dict. 
                vector_dict = {}

                # gets the range of vector (len of row).
                n = range(0, len(cube_dict[i[f]][f]))

                # adds the row of new cube to dict. 
                vector_dict[col] = cube_dict[i[f]][col]
                
                # Creates a list of all columns. [0, 1, 2]
                m = list(n)
                # Removes the chosen column.
                m.remove(col)

                # loops throg the remaining columns.
                for x in m:
                    
                    # add the remaing columns to new vector dict.
                    vector_dict[x] = cube_dict[i[t]][x]

                # sorts and creates a new matrix based on vector dict (sorts so rows goes in right order).
                new_vector = np.array([vector_dict[y] for y in range(len(vector_dict))]).reshape(3, 3)

                # add new matrix to new cube dict.
                new_cube[i[t]] = new_vector

    # returns new cube dict. 
    return new_cube

        

        
                



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
            
            # quit()
            if event.key == pygame.K_UP:
                pygame.quit()
                quit()

            # reset colors / randomze 
            if event.key == pygame.K_DOWN:

                cube_dict = generate_cube(color_dict, side_list)
                
            # rotate backwards 
            if event.key == pygame.K_KP1:

                rules_up = [["front", "top"], ["top", "back"], ["back", "bottom"], ["bottom", "front"], ["rotate", "left", 1], ["right", "right"]]
                cube_dict = cube_movement(cube_dict= cube_dict, rules= rules_up, col= 0, forwards= False, T= True)
            
            if event.key == pygame.K_KP2:

                rules_up = [["front", "top"], ["top", "back"], ["back", "bottom"], ["bottom", "front"], ["left", "left"], ["right", "right"]]
                cube_dict = cube_movement(cube_dict= cube_dict, rules= rules_up, col= 1, forwards= False, T= True)

            if event.key == pygame.K_KP3:

                rules_up = [["front", "top"], ["top", "back"], ["back", "bottom"], ["bottom", "front"], ["left", "left"], ["rotate", "right", -1]]
                cube_dict = cube_movement(cube_dict= cube_dict, rules= rules_up, col= 2, forwards= False, T= True)

            # rotate forwards 
            if event.key == pygame.K_KP4:

                rules_up = [["front", "top"], ["top", "back"], ["back", "bottom"], ["bottom", "front"], ["rotate", "left", -1], ["right", "right"]]
                cube_dict = cube_movement(cube_dict= cube_dict, rules= rules_up, col= 0, forwards= True, T= True)
            
            if event.key == pygame.K_KP5:

                rules_up = [["front", "top"], ["top", "back"], ["back", "bottom"], ["bottom", "front"], ["left", "left"], ["right", "right"]]
                cube_dict = cube_movement(cube_dict= cube_dict, rules= rules_up, col= 1, forwards= True, T= True)

            if event.key == pygame.K_KP6:

                rules_up = [["front", "top"], ["top", "back"], ["back", "bottom"], ["bottom", "front"], ["left", "left"], ["rotate", "right", 1]]
                cube_dict = cube_movement(cube_dict= cube_dict, rules= rules_up, col= 2, forwards= True, T= True)

            # rotate right
            if event.key == pygame.K_KP7:

                rules_up = [["front", "right"], ["right", "back"], ["back", "left"], ["left", "front"], ["rotate", "top", 1], ["bottom", "bottom"]]
                cube_dict = cube_movement(cube_dict= cube_dict, rules= rules_up, col= 0, forwards= False, T= False)

            if event.key == pygame.K_KP8:

                rules_up = [["front", "right"], ["right", "back"], ["back", "left"], ["left", "front"], ["top", "top"], ["bottom", "bottom"]]
                cube_dict = cube_movement(cube_dict= cube_dict, rules= rules_up, col= 1, forwards= False, T= False)

            if event.key == pygame.K_KP9:

                rules_up = [["front", "right"], ["right", "back"], ["back", "left"], ["left", "front"], ["top", "top"], ["rotate", "bottom", -1]]
                cube_dict = cube_movement(cube_dict= cube_dict, rules= rules_up, col= 2, forwards= False, T= False)

            # rotate left 
            if event.key == pygame.K_b:

                rules_up = [["front", "right"], ["right", "back"], ["back", "left"], ["left", "front"], ["rotate", "top", -1], ["bottom", "bottom"]]
                cube_dict = cube_movement(cube_dict= cube_dict, rules= rules_up, col= 0, forwards= True, T= False)

            if event.key == pygame.K_n:

                rules_up = [["front", "right"], ["right", "back"], ["back", "left"], ["left", "front"], ["top", "top"], ["bottom", "bottom"]]
                cube_dict = cube_movement(cube_dict= cube_dict, rules= rules_up, col= 1, forwards= True, T= False)

            if event.key == pygame.K_m:

                rules_up = [["front", "right"], ["right", "back"], ["back", "left"], ["left", "front"], ["top", "top"], ["rotate", "bottom", 1]]
                cube_dict = cube_movement(cube_dict= cube_dict, rules= rules_up, col= 2, forwards= True, T= False)
                

                