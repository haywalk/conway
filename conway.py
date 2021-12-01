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
except:
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
        Given the array of cells, count this cell's living neighbours
        '''

        # Check if cell is on an edge
        l_edge = self.col == 0
        r_edge = self.col == len(cell_array) - 1
        t_edge = self.row == 0
        b_edge = self.row == len(cell_array) - 1

        # Count neighbours
        num_of_neighbours = 0

        # Check left
        if not l_edge:
            if cell_array[self.row][self.col - 1].is_living:
                num_of_neighbours += 1
        # Check top-left
        if not l_edge and not t_edge:
            if cell_array[self.row - 1][self.col - 1].is_living:
                num_of_neighbours += 1
        # Check bottom-left
        if not l_edge and not b_edge:
            if cell_array[self.row + 1][self.col - 1].is_living:
                num_of_neighbours += 1
        # Check top
        if not t_edge:
            if cell_array[self.row - 1][self.col].is_living:
                num_of_neighbours += 1
        # Check bottom
        if not b_edge:
            if cell_array[self.row + 1][self.col].is_living:
                num_of_neighbours += 1
        # Check right
        if not r_edge:
            if cell_array[self.row][self.col + 1].is_living:
                num_of_neighbours += 1
        # Check top-right
        if not r_edge and not t_edge:
            if cell_array[self.row - 1][self.col + 1].is_living:
                num_of_neighbours += 1
        # Check bottom-right
        if not r_edge and not b_edge:
            if cell_array[self.row + 1][self.col + 1].is_living:
                num_of_neighbours += 1

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



