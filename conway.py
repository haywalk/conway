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
'''

'''
Conway's Game of Life
Implemented by Hayden Walker (www.haywalk.ca)
2021-11-30
'''

import random

# Attempt to import Pygame
try:
    import pygame
except ModuleNotFoundError:
    print('This program requires the Pygame library to be installed.')
    quit()


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

        neighbour_positions = [[-1, -1], [-1, 0], [-1, 1],
            [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        for position in neighbour_positions:
            nr = position[0]
            nc = position[1]

            try:
                if cell_array[self.row + nr][self.col + nc].is_living:
                    num_of_neighbours += 1
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
        Draw the cell
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
cell_array = list()

# Add rows of cells to the array
for row in range(dimensions):
    # Create the row as a list of cells
    this_row = list()

    # Add cells to the row
    for col in range(dimensions):
        this_row.append(Cell(random.randint(0, 1), col, row))

    # Add row to list of rows
    cell_array.append(this_row)

# Main loop
while True:
    # Check for quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    
    # Clear screen
    screen.fill((0, 0, 0))

    # Draw each cell
    for row in cell_array:
        for cell in row:
            cell.draw(screen)

    # Update the screen
    pygame.display.update()

    # Make each cell count its neighbours
    for row in cell_array:
        for cell in row:
            cell.get_neighbours(cell_array)

    # Make each cell evolve
    for row in cell_array:
        for cell in row:
            cell.evolve()

    # Wait a second
    pygame.time.delay(delay)



