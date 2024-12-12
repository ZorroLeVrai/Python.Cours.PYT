"""
Sodoku Solver
Utilisation du backtracking pour résoudre un sudoku
"""

sudoku_grid = [[5,3,0,0,7,0,0,0,0],
               [6,0,0,1,9,5,0,0,0],
               [0,9,8,0,0,0,0,6,0],
               [8,0,0,0,6,0,0,0,3],
               [4,0,0,8,0,3,0,0,1],
               [7,0,0,0,2,0,0,0,6],
               [0,6,0,0,0,0,2,8,0],
               [0,0,0,4,1,9,0,0,5],
               [0,0,0,0,8,0,0,7,9]]


def print_sudoku(grid):
    for row in grid:
        for number in row:
            print(number, end=" ")
        print()

def is_possible(grid, y, x, n):
    #vérifier la ligne
    for i in range(9):
        if grid[y][i] == n:
            return False
    #vérifier la colonne
    for i in range(9):
        if grid[i][x] == n:
            return False
    #vérifier le carré 3x3
    x0 = (x//3) * 3
    y0 = (y//3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False
    #Le nombre n'est pas présent dans la ligne, la colonne ou le carré 3x3
    return True

def solve_sudoku(grid):
    results = []
    def solve_sudoku_local(grid):
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    for n in range(1, 10):
                        if is_possible(grid, y, x, n):
                            grid[y][x] = n
                            solve_sudoku_local(grid)
                            grid[y][x] = 0
                    return
        
        #Ajouter une copie de la grille à la liste des résultats
        results.append([row[:] for row in grid])

    solve_sudoku_local(grid)
    return results


def print_solutions(grid):
    solutions = solve_sudoku(grid)
    nb_solutions = len(solutions)
    if nb_solutions == 0:
        print("Pas de solution")
        return
    
    for index in range(nb_solutions):
        print(f"Solution {index + 1}:")
        print_sudoku(solutions[index])
        print()


print_solutions(sudoku_grid)