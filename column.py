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

def column_correct(sudoku: list, column_no: int):
    column= sudoku[column_no]
    found_numbers = [False] * 9  # Índices 0-8 corresponden a números 1-9

    for row in sudoku:
        number = row[column_no]
        if number != 0:  # Ignorar los ceros (casillas vacías)
            if number < 1 or number > 9 or found_numbers[number - 1]:
                return False  # Si el número no está en el rango 1-9 o ya fue encontrado
            found_numbers[number - 1] = True  # Marcar el número como encontrado

    return True  # Si todos los números son únicos y válidos

print(column_correct(sudoku, 0))
print(column_correct(sudoku, 1))