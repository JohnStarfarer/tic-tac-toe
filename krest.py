board = [['.','.','.'], #глобальный массив состояния поля
         ['.','.','.'],
         ['.','.','.']]

def Check_Winner(): #функция проверки победы на данный момент
    # Проверка строк
    for row in board:
        if row[0] == row[1] == row[2] == "X" or row[0] == row[1] == row[2] == "0":
            return True
    # Проверка столбцов
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == "X" or board[0][col] == board[1][col] == board[2][col] == "0" :
            return True
    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] == "X" or board[0][0] == board[1][1] == board[2][2] == "0":
        return True
    if board[0][2] == board[1][1] == board[2][0] == "X" or board[0][2] == board[1][1] == board[2][0] == "0":
        return True
    # Победителя нет
    return False

def PrintBoard(): #функция вывода поля
    for el in board:
        print('|'.join(el))
    
def Move(current_player): #функция хода текущего игрока
    print(f'Cейчах ходят - {current_player}')
    input_player = True #флаг для ввода координат
    break_game = False #флаг для прекращения игры (try-except не позволяют закрыть терминал Ctrl^C) (exit() тоже не помогает)
    while input_player:
        try:
            PrintBoard()
            xy = input('Введите номер строки и столбца (для выхода введите 0): ')
            if xy == '0':
                input_player = False
                break_game = True
            else:
                x, y = map(int, xy.split())
                x -= 1 # вводить/читать по координатам 0-2 неудобно
                y -= 1
                if board[x][y] != '.':
                    print('\tЭта ячейка занята!')
                else: input_player = False
        except:
            print('\tНеверный ввод!')
    
    print() #отступ, если ход верный
    if break_game: return 'BREAK' #exit() не работает

    board[x][y] = current_player
    if Check_Winner(): #победил данный игрок в этом ходе или нет
        return current_player
    else:
        return False

#основной блок кода
print('Игра крестики-нолики!!!')
current_player = 'X'
winner = False

while '.' in [el for el_list in board for el in el_list] and not(winner): #пока существуют "пустые" ячейки и нет победителя / итерация ходов
    winner = Move(current_player)
    if winner == 'BREAK':
        break
    elif winner:
        print(f'Выигрывает {winner}!')
    else:
        current_player = '0' if current_player == 'X' else 'X' #смена игроков

if not(Check_Winner()):
    print('Ничья!')