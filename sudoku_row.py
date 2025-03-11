sudoku = [
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

def row_correct(sudoku: list, row_no: int):
    row= sudoku[row_no]
    found_numbers = [False] * 9  # Índices 0-8 corresponden a números 1-9

    for number in row:
        if number != 0:  # Ignorar los ceros (casillas vacías)
            if number < 1 or number > 9 or found_numbers[number - 1]:
                return False  # Si el número no está en el rango 1-9 o ya fue encontrado
            found_numbers[number - 1] = True  # Marcar el número como encontrado

    return True  # Si todos los números son únicos y válidos


print(row_correct(sudoku, 0))
print(row_correct(sudoku, 1))