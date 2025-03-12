def row_correct(sudoku: list, row_no: int):
    row= sudoku[row_no]
    found_numbers = [False] * 9  # Índices 0-8 corresponden a números 1-9

    for number in row:
        if number != 0:  # Ignorar los ceros (casillas vacías)
            if number < 1 or number > 9 or found_numbers[number - 1]:
                return False  # Si el número no está en el rango 1-9 o ya fue encontrado
            found_numbers[number - 1] = True  # Marcar el número como encontrado

    return True  # Si todos los números son únicos y válidos

def column_correct(sudoku: list, column_no: int):
    column= sudoku[column_no]
    found_numbers = [False] * 9  

    for row in sudoku:
        number = row[column_no]
        if number != 0:  
            if number < 1 or number > 9 or found_numbers[number - 1]:
                return False 
            found_numbers[number - 1] = True  

    return True  


def block_correct(sudoku: list, row_no: int, column_no: int):
    row = sudoku[row_no]
    column = row[column_no]
    found_numbers = [False] *9 
    for i in range(3):
        for j in range(3):
            number = sudoku[row_no + i][column_no + j]
            if number != 0:
                if number < 1 or number > 9 or found_numbers[number - 1]:
                    return False
                    fund_numbers[number - 1] = True  

            return True  


def  sudoku_grid_correct(sudoku: list):
    for i in range(9):
        if not row_correct(sudoku, i) or not column_correct(sudoku, i):
            return False
    
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            if not block_correct(sudoku, row, col):
                return False
    
    return True


sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
]

print(sudoku_grid_correct(sudoku1))

sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
]

print(sudoku_grid_correct(sudoku2))
