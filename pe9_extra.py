import random

def generate_path(maze, N, M):
    # 生成從(0, 0)到(N-1, M-1)的隨機路徑
    x, y = 0, 0
    maze[(x, y)] = 2
    while x < N - 1 or y < M - 1:
        if x < N - 1 and (y == M - 1 or random.choice([True, False])):
            x += 1
        else:
            y += 1
        maze[(x, y)] = 2

def add_obstacles(maze, min_obstacles, N, M):
    empty_cells = [(i, j) for i in range(N) for j in range(M) if maze[(i, j)] == 0]
    while min_obstacles > 0 and empty_cells:
        i, j = random.choice(empty_cells)
        maze[(i, j)] = 1
        empty_cells.remove((i, j))
        min_obstacles -= 1

def set_obstacle(maze, N, M):
    try:
        x, y = map(int, input("Enter the coordinates to set an obstacle (row, column): ").split())
        if (x, y) in maze and maze[(x, y)] == 0:
            maze[(x, y)] = 1
        else:
            print("Error: Cannot place obstacle on the path or invalid coordinates.")
    except ValueError:
        print("Error: Invalid input. Please enter row and column as integers.")
    except KeyError:
        print("Error: Coordinates out of bounds.")

def remove_obstacle(maze, N, M):
    try:
        x, y = map(int, input("Enter the coordinates to remove an obstacle (row, column): ").split())
        if (x, y) in maze and maze[(x, y)] == 1:
            maze[(x, y)] = 0
        else:
            print("Error: No obstacle at given coordinates or invalid coordinates.")
    except ValueError:
        print("Error: Invalid input. Please enter row and column as integers.")
    except KeyError:
        print("Error: Coordinates out of bounds.")

def print_maze(maze, N, M):
    for i in range(N):
        for j in range(M):
            if maze[(i, j)] == 0:
                print('   ', end='')
            elif maze[(i, j)] == 1:
                print(' X ', end='')
            elif maze[(i, j)] == 2:
                print(' O ', end='')
        print()

def main():
    try:
        filename = input("Enter the maze blueprint filename (e.g., grid77.txt or grid99.txt): ")
        with open(filename, 'r') as file:
            blueprint = [line.strip() for line in file]
        
        N = len(blueprint)
        M = len(blueprint[0])
        
        maze = {(i, j): int(blueprint[i][j]) for i in range(N) for j in range(M)}
        generate_path(maze, N, M)
        
        min_obstacles = int(input("Enter the minimum number of obstacles to add: "))
        if min_obstacles < 0 or min_obstacles > (N * M - N - M + 1):
            raise ValueError("Invalid number of obstacles.")
        
        add_obstacles(maze, min_obstacles, N, M)
        
        while True:
            print_maze(maze, N, M)
            option = input("Choose an option (set, remove, exit): ").strip().lower()
            
            if option == "set":
                set_obstacle(maze, N, M)
            elif option == "remove":
                remove_obstacle(maze, N, M)
            elif option == "exit":
                break
            else:
                print("Invalid option. Please choose 'set', 'remove', or 'exit'.")
    
    except FileNotFoundError:
        print("Error: File not found. Please enter a valid file name.")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
