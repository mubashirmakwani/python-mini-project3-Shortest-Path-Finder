#SIt uses BFS(Breath First Search) Algorithm:



import curses
from curses import wrapper
import queue 
import time

maze = [
    ["1","1","1","1","1","O","1","1","1"],
    ["1"," "," "," "," "," "," "," ","1"],
    ["1"," ","1","1"," ","1","1"," ","1"],
    ["1"," ","1"," "," "," ","1"," ","1"],
    ["1"," ","1"," ","1"," ","1"," ","1"],
    ["1"," ","1"," ","1"," ","1"," ","1"],
    ["1"," ","1"," ","1"," ","1","1","1"],
    ["1"," "," "," "," "," "," "," ","1"],
    ["1","1","1","1","1","1","1","M","1"]
]

def print_maze(maze, stdscr, path=[]):
    GREEN = curses.color_pair(1)
    BLUE = curses.color_pair(2)

    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if (i, j) in path:
                stdscr.addstr(i, j * 2, "M", BLUE)
            else:
                stdscr.addstr(i, j * 2, value, GREEN)

def find_start(maze, start_char):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start_char:
                return i, j
    return None

def find_neighbors(maze, row, col):
    neighbors = []
    if row > 0:
        neighbors.append((row - 1, col))
    if row + 1 < len(maze):
        neighbors.append((row + 1, col))
    if col > 0:
        neighbors.append((row, col - 1))
    if col + 1 < len(maze[0]):
        neighbors.append((row, col + 1))
    return neighbors

def find_path(maze, stdscr):
    start = "O"
    end = "M"
    start_pos = find_start(maze, start)
    q = queue.Queue()
    q.put((start_pos, [start_pos]))
    visited = set()

    while not q.empty():
        current_pos, path = q.get()
        row, col = current_pos

        stdscr.clear()
        print_maze(maze, stdscr, path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col] == end:
            return path

        for neighbor in find_neighbors(maze, row, col):
            if neighbor in visited:
                continue
            r, c = neighbor
            if maze[r][c] == "1":
                continue
            visited.add(neighbor)
            new_path = path + [neighbor]
            q.put((neighbor, new_path))

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
    stdscr.clear()
    print_maze(maze, stdscr)
    stdscr.refresh()
    find_path(maze, stdscr)
    stdscr.getch()

wrapper(main)
