# python-mini-project3-Shortest-Path-Finder
Terminal-based Maze Solver using BFS algorithm and Python's curses library.

# 🧭 BFS Maze Solver

**Terminal-based Maze Solver using BFS algorithm and Python's curses library.**  
This project visually demonstrates how the **Breadth-First Search (BFS)** algorithm finds the shortest path through a maze.

---

## 📌 Features

- ✅ Real-time pathfinding animation in the terminal
- 🔍 BFS (Breadth-First Search) algorithm for shortest-path search
- 🎯 Visualizes the path from Start (`O`) to Goal (`M`)
- 🧩 Maze is customizable via a 2D list
- 🐍 Built with Python and the `curses` module

---

## 🖥️ Requirements

- Python 3.x
- Works best in Unix-based terminals (Linux/macOS)  
  On **Windows**, install `windows-curses`:

```bash
pip install windows-curses
▶️ How to Run
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/bfs-maze-solver.git
cd bfs-maze-solver
Run the script:

bash
Copy code
python maze_solver.py
🧠 How It Works
The maze is a 2D list where:

"1" = wall

" " = walkable path

"O" = start

"M" = goal

BFS (Breadth-First Search) explores the maze level by level to find the shortest path.

The path is visualized live using curses as the search progresses.

📁 File Structure
bash
Copy code
bfs-maze-solver/
│
├── maze_solver.py     # Main script with BFS and visualization
├── README.md          # Project documentation
