
# Игра печатает пустое поле
enter_field = '         '
list_el = [i for i in enter_field]  # [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


# Ф-я разбивающая список на три подсписка
def split(elements):
    return elements[0:3], elements[3:6], elements[6:9]


# Создание двумерного списка
matrix = [i for i in split(list_el)]  # [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]


# Перебераю эл-ты через цикл и вывожу
def printer():
    print('---------')
    for row in matrix:
        print('|', end=' ')
        for col in row:
            print(col, end=' ')
        print('|')
    print('---------')


printer()

# Gamers - Ход начинается с X
for gamer in range(1, 11):
    if gamer % 2 == 0:
        gamer = 'second'
    else:
        gamer = 'first'

    # Проверка на победителя, если ничья или победа, выход из цикла

    diagonals_1 = [matrix[i][i] for i in range(3)]  # diag
    diagonals_2 = [matrix[i][2 - i] for i in range(3)]  # diag
    diagonals_3 = [matrix[i][0] for i in range(3)]  # left_col
    diagonals_4 = [matrix[i][2] for i in range(3)]  # right_col
    diagonals_5 = [matrix[i][1] for i in range(3)]  # central_col
    diagonals_6 = [matrix[0][i] for i in range(3)]  # top_row
    diagonals_7 = [matrix[1][i] for i in range(3)]  # central_row
    diagonals_8 = [matrix[2][i] for i in range(3)]  # bottom_row
    all_diagonals = [diagonals_1, diagonals_2, diagonals_3, diagonals_4,
                     diagonals_5, diagonals_6, diagonals_7, diagonals_8]

    all_row = [diagonals_6, diagonals_7, diagonals_8]

    x_wins = [x for x in all_diagonals if x == ['X', 'X', 'X']]
    if x_wins:
        print('X wins')
        break

    o_wins = [o for o in all_diagonals if o == ['O', 'O', 'O']]
    if o_wins:
        print('O wins')
        break

    # Когда ни на одной стороне нет тройки в ряд и не осталось пустых ячеек;
    x_draw = [diagonals for diagonals in all_diagonals if diagonals.count('X') != 3]
    o_draw = [diagonals for diagonals in all_diagonals if diagonals.count('O') != 3]
    draw = [diagonals.count(' ') == 0 for diagonals in all_row]

    if x_draw and all(draw):
        print('Draw')
        break

    if o_draw and all(draw):
        print('Draw')
        break

    # Ввести координаты ячейки
    coordinates = input('Enter the coordinates: ').split()  # ['1', '2']

    try:
        coordinates = [int(i) for i in coordinates]  # [1, 2]   class integer

    except ValueError:
        print("You should enter numbers!")
        continue

    if coordinates[0] > 3 or coordinates[1] > 3:
        print("Coordinates should be from 1 to 3!")
        continue

    if gamer == 'first':
        if coordinates == [1, 1]:
            coordinates = matrix[2][0]
            if matrix[2][0] != ' ':  # не равен пробелу
                print("This cell is occupied! Choose another one!")
            else:
                matrix[2][0] = 'X'
                printer()
                continue
        elif coordinates == [1, 2]:
            coordinates = matrix[1][0]
            if matrix[1][0] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[1][0] = 'X'
                printer()
                continue
        elif coordinates == [1, 3]:
            coordinates = matrix[0][0]
            if matrix[0][0] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[0][0] = 'X'
                printer()
                continue
        elif coordinates == [2, 1]:
            coordinates = matrix[2][1]
            if matrix[2][1] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[2][1] = 'X'
                printer()
                continue
        elif coordinates == [2, 2]:
            coordinates = matrix[1][1]
            if matrix[1][1] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[1][1] = 'X'
                printer()
                continue
        elif coordinates == [2, 3]:
            coordinates = matrix[0][1]
            if matrix[0][1] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[0][1] = 'X'
                printer()
                continue
        elif coordinates == [3, 1]:
            coordinates = matrix[2][2]
            if matrix[2][2] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[2][2] = 'X'
                printer()
                continue
        elif coordinates == [3, 2]:
            coordinates = matrix[1][2]
            if matrix[1][2] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[1][2] = 'X'
                printer()
                continue
        elif coordinates == [3, 3]:
            coordinates = matrix[0][2]
            if matrix[0][2] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[0][2] = 'X'
                printer()
                continue

    if gamer == 'second':
        if coordinates == [1, 1]:
            coordinates = matrix[2][0]
            if matrix[2][0] != ' ':  # не равен пробелу
                print("This cell is occupied! Choose another one!")
            else:
                matrix[2][0] = 'O'
                printer()
                continue
        elif coordinates == [1, 2]:
            coordinates = matrix[1][0]
            if matrix[1][0] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[1][0] = 'O'
                printer()
                continue
        elif coordinates == [1, 3]:
            coordinates = matrix[0][0]
            if matrix[0][0] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[0][0] = 'O'
                printer()
                continue
        elif coordinates == [2, 1]:
            coordinates = matrix[2][1]
            if matrix[2][1] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[2][1] = 'O'
                printer()
                continue
        elif coordinates == [2, 2]:
            coordinates = matrix[1][1]
            if matrix[1][1] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[1][1] = 'O'
                printer()
                continue
        elif coordinates == [2, 3]:
            coordinates = matrix[0][1]
            if matrix[0][1] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[0][1] = 'O'
                printer()
                continue
        elif coordinates == [3, 1]:
            coordinates = matrix[2][2]
            if matrix[2][2] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[2][2] = 'O'
                printer()
                continue
        elif coordinates == [3, 2]:
            coordinates = matrix[1][2]
            if matrix[1][2] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[1][2] = 'O'
                printer()
                continue
        elif coordinates == [3, 3]:
            coordinates = matrix[0][2]
            if matrix[0][2] != ' ':
                print("This cell is occupied! Choose another one!")
            else:
                matrix[0][2] = 'O'
                printer()
                continue
