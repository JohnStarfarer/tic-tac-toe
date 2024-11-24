def check_winner(board):    # Проверка строк
    for row in board:        if row[0] == row[1] == row[2] == "X" or row[0] == row[1] == row[2] == "0":
            return True
    # Проверка столбцов    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == "X" or board[0][col] == board[1][col] == board[2][col] == "0" :            return True
    # Проверка диагоналей
    if board[0][0] == board[1][1] == board[2][2] == "X" or board[0][0] == board[1][1] == board[2][2] == "0":        return True
    if board[0][2] == board[1][1] == board[2][0] == "X" or board[0][2] == board[1][1] == board[2][0] == "0":
        return True
    return False
def vivod(board):    for a in board:
        print('|'.join(a))
def proverka(x,y,board):    if x<3 and x>=0 and y<3 and y>=0 and board[x][y] == '.' :
        return True    else:
        return False
print('Игра крестики-нолики!!!')maps = [['.','.','.'],['.','.','.'],['.','.','.']]
i = 1current_player = 'X'
vivod(maps)
while i != 9:    print(f'Cейчах ходят - {current_player}')
    x, y = map(int,input('введите координаты x(0-2),y(0,2) - ' ).split())    #проверяем правильность ввода
    if proverka(x,y,maps):        maps[x][y] = current_player
        vivod(maps)        #меняем ход
        current_player = '0' if current_player == 'X' else 'X'        i +=1
    else:        print('Неверный ввод')
    #проверяем условие победы    if check_winner(maps):
        current_player = '0' if current_player == 'X' else 'X'        print(f'Выйграли! - {current_player}')
        break
if check_winner(maps) == False:    print('Ничья!')
