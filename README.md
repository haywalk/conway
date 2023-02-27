# Conway's Game of Life

![Screenshot](./screenshots/50x50.png?raw=true)

This is an implementation of [Conway's Game of Life](https://www.conwaylife.com/wiki/Conway%27s_Game_of_Life), a cellular automaton. I first implemented this in August 2019, when I was first learning Python. Over two years later, I was looking for a way to waste some time, so I decided to write a more polished implementation of the algorithm.

The simulation runs on a grid of 'cells,' which are either alive or dead. Each cycle of the simulation is called a 'generation.' Which cells live into the next generation, die, or are born, is determined by the following three rules:

* If a living cell has 2 or 3 living neighbours, it will live into the next generation.
* If a living cell has less than 2 or more than 3 living neighbours, it will die.
* If a dead cell has exactly three living neighbours, it will become alive.

This implementation is written in Python 3.9 and requires the [Pygame](https://www.pygame.org/) library. This program is licensed under the [GNU GPL, version 3](https://www.gnu.org/licenses/gpl-3.0.en.html). It was written by Hayden Walker ([www.haywalk.ca](https://www.haywalk.ca/)) on 2021-11-30. 
