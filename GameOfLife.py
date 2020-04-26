#Modules and packages
import pygame
import time
from random import randint


# Classes
class gen():
    def __init__(self, rows, cols):
        self.cols = cols
        self.rows = rows
        self.gen = 0
        grid = []
        for i in range(0, rows):
            grid.append([])
            for k in range(0, cols):
                grid[i].append([])
                grid[i][k] = randint(0, 1)
        self.grid = grid

    def around(self, row_num, col_num):
        res = []
        # if col_num+1 < self.cols:
        #     res.append(self.grid[row_num][col_num+1])

        # if col_num-1 > -1:
        #     res.append(self.grid[row_num][col_num-1])

        # if row_num+1 < self.rows:
        #     res.append(self.grid[row_num+1][col_num])

        # if row_num-1 > -1:
        #     res.append(self.grid[row_num-1][col_num])

        # if col_num+1 < self.cols and row_num+1 < self.rows:
        #     res.append(self.grid[row_num+1][col_num+1])

        # if col_num+1 < self.cols and row_num-1 > -1:
        #     res.append(self.grid[row_num-1][col_num+1])

        # if col_num-1 > -1 and row_num-1 > -1:
        #     res.append(self.grid[row_num-1][col_num-1])

        # if col_num-1 > -1 and row_num+1 > self.rows:
        #     res.append(self.grid[row_num-1][col_num+1])
        for i in range(max(0, row_num-1), min(row_num+1, self.rows-1)+1):
            for k in range(max(0, col_num-1), min(col_num+1, self.cols-1)+1):
                if i != row_num or k != col_num:
                    res.append(self.grid[i][k])

        return res

    def rule(self, row_num, col_num):
        surround = self.around(row_num, col_num)
        alive = 0
        for i in range(len(surround)):
            if surround[i] == 1:
                alive += 1

        if (alive == 3 or alive == 2) and self.grid[row_num][col_num] == 1:
            return 1
        elif alive == 3 and self.grid[row_num][col_num] == 0:
            return 1

        return 0

    def next_gen(self):
        self.gen += 1
        new_gen = []
        for i in range(self.rows):
            new_gen.append([])
            for k in range(self.cols):
                new_gen[i].append([])
                new_gen[i][k] = self.rule(i, k)

        for i in range(self.rows):
            for k in range(self.cols):
                self.grid[i][k] = new_gen[i][k]


# Variables
row_number = 100
col_number = 100
width_of_a_square = 8

width = width_of_a_square * col_number
height = width_of_a_square * row_number
dead_color = (255, 255, 255)  # #999999
alive_color = (255, 0, 0)   # #990000
black = (0, 0, 0)  # #000000

fps = pygame.time.Clock()

pygame.init()
window = pygame.display.set_mode((width, height))


running = True

grid = gen(row_number, col_number)

# Functions


def draw_the_grid(window, grid):
    for i in range(grid.rows):
        for k in range(grid.cols):
            if grid.grid[i][k] == 1:
                pygame.draw.rect(window, alive_color, (i*width_of_a_square,
                                                       k*width_of_a_square, width_of_a_square, width_of_a_square))
            elif grid.grid[i][k] == 0:
                pygame.draw.rect(window, dead_color, (i*width_of_a_square,
                                                      k*width_of_a_square, width_of_a_square, width_of_a_square))
            pygame.draw.rect(window, black, (i*width_of_a_square, k *
                                             width_of_a_square, width_of_a_square, width_of_a_square), 1)


# Main code
while running:
    window.fill(black)
    draw_the_grid(window, grid)
    grid.next_gen()

    ###controls###
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and not pause:
                hit = 1

            if event.key == pygame.K_LEFT and not pause:
                hit = 0

            if event.key == pygame.K_SPACE:
                pause = not pause
    print(grid.gen)
    ##############
    # fps.tick(120)
    pygame.display.update()
