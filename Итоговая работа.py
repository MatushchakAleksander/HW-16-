import time
import random
import sys


def instrukciya():
    print('''
        Приветствую Вас! Это игра "Крестики-нолики".
    Чтобы сделать ход, введи номер клетки,куда хочешь поставить свой символ:

                            1 | 2 | 3
                            ---------
                            4 | 5 | 6
                            ---------
                            7 | 8 | 9
''')


instrukciya()


def drawBoard(board):
    # Эта функция выводит на экран игровое поле, клетки которого будут заполняться.
    # "board" - это список из  строк, для прорисовки игрового поля (индекс 0 игнорируется).
    print(" " * 50 + board[1] + " ║ " + board[2] + " ║ " + board[3])
    print(" " * 50 + "══╦═══╦══")
    print(" " * 50 + board[4] + " ║ " + board[5] + " ║ " + board[6])
    print(" " * 50 + "══╦═══╦══")
    print(" " * 50 + board[7] + " ║ " + board[8] + " ║ " + board[9])
    print()
    print('***************************************************************')
    print()


def inputPlayerLetter():
    # Разрешение игроку ввести букву, которую он выбирает.
    # Возвращает список, в котором буква игрока - первый элемент, а буква компьютера - второй.

    letter = ""
    letter = input("Вы выбираете X или О?").upper()
    while not (letter == "X" or letter == "O"):
        letter = input("Ошибка!Повторите!Вы выбираете X или О?").upper()
    else:
        print("Вы сделали свой выбор!")
        time.sleep(0.6)
    print("Ok..✔")
    print()
    print('***************************************************************')
    print()

    # Первым элементом списка является буква игрока, вторым - буква ПК.
    if letter == "X":
        return ["X", "O"]
    else:
        return ["O", "X"]


def whoGoesFirst():
    # Случайный выбор игрока, который ходит первым.
    if random.randint(0, 1) == 0:
        print("Ожидаем жребий первого хода..... ██████████████] 99% ")
        time.sleep(1.0)
        return "Компьютер"
    else:
        print("Ожидаем жребий первого хода... ")
        time.sleep(1.0)
        return "Человек"


def makeMove(board, letter, move):
    board[move] = letter


def isWinner(bo, le):
    # Учитывая заполнение игрового поля и буквы игрока, эта функция возвращает True,
    # если игрок выиграл.
    # Мы используем "bo" вместо "board" и "le" вместо "letter".
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # через вверх
            (bo[4] == le and bo[5] == le and bo[6] == le) or  # через центр
            (bo[1] == le and bo[2] == le and bo[3] == le) or  # через низ
            (bo[7] == le and bo[4] == le and bo[1] == le) or  # вниз по левой стороне
            (bo[8] == le and bo[5] == le and bo[2] == le) or  # вниз по центру
            (bo[9] == le and bo[6] == le and bo[3] == le) or  # вниз по правой стороне
            (bo[7] == le and bo[5] == le and bo[3] == le) or  # по диагонали
            (bo[9] == le and bo[5] == le and bo[1] == le))  # по диагонали


def getBoardCopy(board):
    # Создает копию игрового поля и возвращает его
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy


def isSpaceFree(board, move):
    # Возвращает True, если сделан ход в свободную клетку 
    return board[move] == " "


def getPlayerMove(board):
    # разрешение игроку сделать ход
    move = " "
    move = input("Ваш следующий ход!\n❶ ❷ ❸\n❹ ❺ ❻ \n❼ ❽ ❾..►► ")
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(move)):
        print("Некорректный ввод!Повторите...")
        move = input()
    else:
        time.sleep(0.5)
        print("Вы сделали свой ход.✔")
        time.sleep(1.0)
        print("Ждём ответный ход компьютера....㋛ ")
        time.sleep(1.0)
    return int(move)


def chooseRandomMoveFromList(board, moveList):
    # Возвращает допустимый ход, учитывая список сделанных ходов и список заполненных клеток.
    # Возвращает значение None, если больше нет допустимых ходов.
    possibleMoves = []
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None


def getComputerMove(board, computerLetter):
    # Учитывая заполнение игрового поля и букву компьютера,
    # определяет допустимый ход и возвращает его.
    if computerLetter == "X":
        playerLetter = "O"
    else:
        playerLetter = "X"

    # Это алгоритм для искусственного интеллекта "Крестиков-Ноликов":
    # Проверяем победим ли мы, сделав ход.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
        if isWinner(boardCopy, computerLetter):
            return i

    # проверяем - победит ли игрок, сделав следующий ход, и блокируем его.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
        if isWinner(boardCopy, playerLetter):
            return i

    # Пробуем занять один из углов, если есть свободные.
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    # пробуем занять центр
    if isSpaceFree(board, 5):
        return 5

    # делаем ход по одной стороне
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    # Возвращает True, если клетка на игровом поле занята.
    # В противном случае возвращает False.
    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
    return True


print('Игра начинается!\nНе забываем переключиться на английскую раскладку клавиатуры:')

while True:
    # перезагрузка игрового поля
    theBoard = [" "] * 10
    playerLetter, computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print("" + turn + " ходит первым.")
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == "Человек":
            # ход игрока
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Ура! Вы выиграли!")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("Ничья!")
                    break
                else:
                    turn = "Компьютер"

        else:
            # ход компьютера
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("Компьютер победил! Вы проиграли.")
                gameIsPlaying = False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("Ничья!")
                    break
                else:
                    turn = "Человек"

    print("Сыграем еще раз? (продолжить : y ; выход : n)")
    if not input().lower().startswith("y"):
        break

sys.exit("Игра окончена! ")
