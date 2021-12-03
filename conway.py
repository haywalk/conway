'''
conway.py

Copyright 2021 Hayden D. Walker <planethaywalk@aol.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Conway's Game of Life
Implemented by Hayden Walker (www.haywalk.ca)
2021-11-30
'''

import random
import sys

# Attempt to import Pygame
try:
    import pygame
except ModuleNotFoundError:
    print('This program requires the Pygame library to be installed.')
    sys.exit()


class Cell:
    '''
    One cell in Conway's Game of Life
    '''
    def __init__(self, is_living, col, row):
        '''
        Class constructor
        '''
        self.is_living = is_living
        self.col = col
        self.row = row
        self.neighbours = 0

    def get_neighbours(self, cell_array):
        '''
        Count the cell's neighbours
        '''
        num_of_neighbours = 0

        # All of the neighbouring cells' relative positions
        neighbour_positions = [[-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        for pos in neighbour_positions:
            try:
                if cell_array[self.row + pos[0]][self.col + pos[1]].is_living:
                    num_of_neighbours += 1

                    # Compensate for python's negative indexes
                    if self.row + pos[0] < 0 or self.col + pos[1] < 0:
                        num_of_neighbours -= 1
            
            except IndexError:
                continue

        self.neighbours = num_of_neighbours

    def evolve(self):
        '''
        Decide if the cell will live to next generation
        '''
        if self.is_living:
            if self.neighbours < 2 or self.neighbours > 3:
                self.is_living = False
        else:
            if self.neighbours == 3:
                self.is_living = True

    def draw(self, win):
        '''
        Draw the cell to a window
        '''
        if self.is_living:
            pygame.draw.rect(win, (255, 255, 0), (self.col * 10, self.row * 10, 10, 10))
        else:
            pygame.draw.rect(win, (0, 0, 0), (self.col * 10, self.row * 10, 10, 10))

# Get number of rows and columns
dimensions = int(input('Number of rows and columns: '))
delay = int(input('Delay between cycles (ms): '))

# Initialize the pygame window
pygame.init()
screen = pygame.display.set_mode((dimensions * 10, dimensions * 10))
pygame.display.set_caption("Life")

# Create array of rows of cells
cells = []

# Add rows of cells to the array
for cellrow in range(dimensions):
    # Create the row as a list of cells
    this_row = []

    # Add cells to the row
    for column in range(dimensions):
        this_row.append(Cell(random.randint(0, 1), column, cellrow))

    # Add row to list of rows
    cells.append(this_row)

# Main loop
while True:
    # Check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # Clear screen
    screen.fill((0, 0, 0))

    # Draw each cell and count neighbours
    for cellrow in cells:
        for cell in cellrow:
            cell.draw(screen)
            cell.get_neighbours(cells)

    # Update the screen
    pygame.display.update()

    # Make each cell evolve
    for cellrow in cells:
        for cell in cellrow:
            cell.evolve()

    # Wait a second
    pygame.time.delay(delay)
