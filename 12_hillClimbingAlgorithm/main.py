import os
import sys
import numpy as np
np.set_printoptions(threshold=np.inf)
np.get_printoptions()['linewidth']
np.set_printoptions(linewidth=300)

SMALL = True
NEIGHBOURS = [(0, 1), (1, 0), (-1, 0), (0, -1)]
POINTS = [[]]
WIDTH = 0
HEIGHT = 0
QUEUE = []
COUNT = [[]]


def read_file():
    __location__ = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    if SMALL:
        f = open((os.path.join(__location__, "small_input.txt")), "r")
    else:
        f = open((os.path.join(__location__, "large_input.txt")), "r")
    return f.read().splitlines()


def elevation(point):
    if point == 'S':
        return ord('a')
    elif point == 'E':
        return ord('z')
    else:
        return ord(point)


def determine_neigbours_1(yp, xp):
    global COUNT
    point = POINTS[yp][xp]
    elev = elevation(point)
    possible = []
    for dir in NEIGHBOURS:
        (y, x) = tuple(map(sum, zip((yp, xp), dir)))
        if x >= 0 and x < WIDTH and y >= 0 and y < HEIGHT:
            if ((elevation(POINTS[y][x])-elev <= 1) or (POINTS[y][x] == 'E' and (point == 'z' or point == 'y'))):
                possible.append((y, x))
                if COUNT[y][x] == -1 or (COUNT[y][x] > COUNT[yp][xp] + 1):
                    COUNT[y][x] = COUNT[yp][xp] + 1
    return possible


def determine_neigbours_2(yp, xp):
    global COUNT
    point = POINTS[yp][xp]
    elev = elevation(point)
    possible = []
    for dir in NEIGHBOURS:
        (y, x) = tuple(map(sum, zip((yp, xp), dir)))
        if x >= 0 and x < WIDTH and y >= 0 and y < HEIGHT:
            if ((elev - elevation(POINTS[y][x]) <= 1) or (POINTS[y][x] == 'S' and (point == 'a' or point == 'b'))):
                possible.append((y, x))
                if COUNT[y][x] == -1 or (COUNT[y][x] > COUNT[yp][xp] + 1):
                    COUNT[y][x] = COUNT[yp][xp] + 1
    return possible


def bfs_1(visited, coords):
    visited.append(coords)
    QUEUE.append(coords)
    while QUEUE:          # Creating loop to visit each coords
        point = QUEUE.pop(0)
        for neighbour in determine_neigbours_1(point[0], point[1]):
            if neighbour not in visited:
                if POINTS[neighbour[0]][neighbour[1]] == 'E':
                    print('\n'.join(' '.join(str(x) for x in row)
                                    for row in np.core.defchararray.add(POINTS, np.char.mod('%d', COUNT))))
                    return COUNT[neighbour[0]][neighbour[1]]
                visited.append(neighbour)
                QUEUE.append(neighbour)


def bfs_2(visited, coords):
    visited.append(coords)
    QUEUE.append(coords)
    while QUEUE:          # Creating loop to visit each coords
        point = QUEUE.pop(0)
        for neighbour in determine_neigbours_2(point[0], point[1]):
            if neighbour not in visited:
                if POINTS[neighbour[0]][neighbour[1]] == 'a':
                    print('\n'.join(' '.join(str(x) for x in row)
                                    for row in np.core.defchararray.add(POINTS, np.char.mod('%d', COUNT))))
                    return COUNT[neighbour[0]][neighbour[1]]
                visited.append(neighbour)
                QUEUE.append(neighbour)


def solve_1():
    global POINTS, WIDTH, HEIGHT, COUNT
    lines = read_file()
    POINTS = np.array([list(line)for line in lines])
    HEIGHT, WIDTH = POINTS.shape
    COUNT = np.ndarray(shape=(HEIGHT, WIDTH))
    COUNT.fill(-1)
    start_y, start_x = np.argwhere(POINTS == 'S')[0]
    COUNT[start_y][start_x] = 0
    return bfs_1([], (start_y, start_x))


def solve_2():
    global POINTS, WIDTH, HEIGHT, COUNT
    lines = read_file()
    POINTS = np.array([list(line)for line in lines])
    HEIGHT, WIDTH = POINTS.shape
    COUNT = np.ndarray(shape=(HEIGHT, WIDTH))
    COUNT.fill(-1)
    start_y, start_x = np.argwhere(POINTS == 'E')[0]
    COUNT[start_y][start_x] = 0
    return bfs_2([], (start_y, start_x))


if __name__ == "__main__":
    print(solve_2())
