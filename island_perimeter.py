#!/usr/bin/env python
# -*- coding: utf-8 -*-

def islandPerimeter(grid):
    """TODO: Docstring for islandPerimeter.

    :grid: TODO
    :returns: TODO

    """
    result = 0
    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            if col:
                result += 4
                if j > 0 and grid[i][j-1]:
                    result -= 2
                if i > 0 and grid[i-1][j]:
                    result -= 2
    return result

print islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
