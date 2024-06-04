from model.Sudoku import Sudoku


def main():
    path = str(input("Path of .txt\n"))
    grid = []
    with open(path, 'r') as f:
        for line in f:
            row = list(map(int, line.split()))
            grid.append(row)
    sudoku = Sudoku(grid)
    sudoku.solve()
    solution = sudoku.__repr__()
    with open(f'solution_{path}', 'w') as f:
        f.write(solution)


def process(s):
    if len(s) != 81:
        print('Error')
        return []
    grid = []
    for char in s:
        if char == '_':
            grid.append(None)
        else:
            grid.append(int(char))
    return grid


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
