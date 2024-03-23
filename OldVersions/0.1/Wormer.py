# Wormer: Text Edition
# ver. 0.1
# By LooNuH
# Date of beginning - 20.04.23
# Date of release - 20.04.23

import os
import time
import msvcrt
import random as r

class Text:
    line20 = ' --------------------'
    wormer = '        Wormer'
    start = '   p - Play'
    level = '   l - Change level'
    controls = '   c - Controls'
    exit = '   e - Exit'
    controlsm = '        Controls'
    w = '   w - Move up'
    a = '   a - Move left'
    s = '   s - Move down'
    d = '   d - Move right'
    menu = '   b - Back to menu'
    whatlevel = ' Enter difficulty level'
    line37 = '-------------------------------------'
    lose = '   You lose!'


class Worm:

    head = {'x': 4, 'y': 4}

    tail = [0, ]

    length = len(tail)
    way = 'up'
    speed = [1, 1, 0.75, 0.5, 0.25, 0.1, 0.05]


class Timer:
    seconds1 = 0
    seconds0 = 0
    minutes1 = 0
    minutes0 = 0


class Game:
    level = Worm.speed[0]
    hasPoint = False

    class Point:
        class Pos:
            x = 0
            y = 0


def clear(mode='def'):
    if mode == 'def':
        os.system('cls' if os.name == 'nt' else 'clear')
    if mode == 'debug':
        return


def ans(where):

    if where == 'game':
        time.sleep(Game.level)
    else:
        time.sleep(0.25)

    answer = ask()

    if type(answer) == bool:
        if where == 'game':
            return
        else:
            ans(where)

    else:
        answer = answer.decode()

    if where == 'menu':

        if answer == 'p':
            game()

        if answer == 'l':
            level()

        if answer == 'c':
            controls()

        if answer == 'e':
            quit()

    if where == 'controls':

        if answer == 'b':
            menu()

    if where == 'game':

        if answer == 'w':
            Worm.way = 'up'

        if answer == 'a':
            Worm.way = 'left'

        if answer == 's':
            Worm.way = 'down'

        if answer == 'd':
            Worm.way = 'right'


def ask():
    x = msvcrt.kbhit()
    if x:
        ret = msvcrt.getch()
    else:
        ret = False
    return ret


def menu():
    clear()

    print(Text.line20, '\n',
          Text.wormer, '\n',
          Text.line20, '\n',
          Text.start, '\n',
          Text.level, '\n',
          Text.controls, '\n',
          Text.exit, '\n',
          Text.line20, '\n',
          sep='')

    ans('menu')


def level():
    clear()

    print(Text.whatlevel)

    try:
        Game.level = Worm.speed[int(input('>>> '))]
    except ValueError:
        level()
    except IndexError:
        level()

    menu()


def controls():
    clear()

    print(Text.line20, '\n',
          Text.controlsm, '\n',
          Text.line20, '\n',
          Text.w, '\n',
          Text.a, '\n',
          Text.s, '\n',
          Text.d, '\n',
          Text.line20, '\n',
          Text.menu, '\n',
          Text.line20, '\n',
          sep='')

    ans('controls')


def game():

    clear()

    if Worm.way == 'up':
        Worm.head['y'] += 1

    if Worm.way == 'down':
        Worm.head['y'] -= 1

    if Worm.way == 'left':
        Worm.head['x'] -= 1

    if Worm.way == 'right':
        Worm.head['x'] += 1

    field = {
        8: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        7: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        6: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        5: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        4: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        3: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        2: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        1: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        0: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    }

    if Worm.head['y'] == Game.Point.Pos.y and Worm.head['x'] == Game.Point.Pos.x:
        Worm.length += 1
        Game.hasPoint = False

    if not Game.hasPoint:
        Game.Point.Pos.x = r.randint(0, 8)
        Game.Point.Pos.y = r.randint(0, 8)
        Game.hasPoint = True

    field[Game.Point.Pos.y][Game.Point.Pos.x] = '*'

    error = False

    try:
        if Worm.way == 'up':
            field[Worm.head['y']][Worm.head['x']] = '^'

        if Worm.way == 'down':
            field[Worm.head['y']][Worm.head['x']] = 'v'

        if Worm.way == 'left':
            field[Worm.head['y']][Worm.head['x']] = '<'

        if Worm.way == 'right':
            field[Worm.head['y']][Worm.head['x']] = '>'

    except KeyError:
        error = True
    except IndexError:
        error = True

    if error:

        Worm.head['x'] = 4
        Worm.head['y'] = 4
        Worm.way = 'up'

        print(Text.lose)
        time.sleep(2)
        menu()

    timer = str(Timer.minutes1 // 1) + str(Timer.minutes0 // 1) + ':' + str(Timer.seconds1 // 1) + str(round(Timer.seconds0 // 1))

    print(Text.line37, '\n',
          '     Time: ', timer, '        Score: ', (Worm.length - 1), '\n',
          Text.line37,
          sep='')
    print('+ — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[8][0], ' | ', field[8][1], ' | ', field[8][2], ' | ', field[8][3], ' | ', field[8][4], ' | ', field[8][5], ' | ', field[8][6], ' | ', field[8][7], ' | ', field[8][8], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[7][0], ' | ', field[7][1], ' | ', field[7][2], ' | ', field[7][3], ' | ', field[7][4], ' | ', field[7][5], ' | ', field[7][6], ' | ', field[7][7], ' | ', field[7][8], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[6][0], ' | ', field[6][1], ' | ', field[6][2], ' | ', field[6][3], ' | ', field[6][4], ' | ', field[6][5], ' | ', field[6][6], ' | ', field[6][7], ' | ', field[6][8], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[5][0], ' | ', field[5][1], ' | ', field[5][2], ' | ', field[5][3], ' | ', field[5][4], ' | ', field[5][5], ' | ', field[5][6], ' | ', field[5][7], ' | ', field[5][8], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[4][0], ' | ', field[4][1], ' | ', field[4][2], ' | ', field[4][3], ' | ', field[4][4], ' | ', field[4][5], ' | ', field[4][6], ' | ', field[4][7], ' | ', field[4][8], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[3][0], ' | ', field[3][1], ' | ', field[3][2], ' | ', field[3][3], ' | ', field[3][4], ' | ', field[3][5], ' | ', field[3][6], ' | ', field[3][7], ' | ', field[3][8], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[2][0], ' | ', field[2][1], ' | ', field[2][2], ' | ', field[2][3], ' | ', field[2][4], ' | ', field[2][5], ' | ', field[2][6], ' | ', field[2][7], ' | ', field[2][8], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[1][0], ' | ', field[1][1], ' | ', field[1][2], ' | ', field[1][3], ' | ', field[1][4], ' | ', field[1][5], ' | ', field[1][6], ' | ', field[1][7], ' | ', field[1][8], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[0][0], ' | ', field[0][1], ' | ', field[0][2], ' | ', field[0][3], ' | ', field[0][4], ' | ', field[0][5], ' | ', field[0][6], ' | ', field[0][7], ' | ', field[0][8], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — +',
          sep='')

    ans('game')

    Timer.seconds0 += Game.level

    if round(Timer.seconds0 // 1) > 9:
        Timer.seconds1 += 1
        Timer.seconds0 = 0

    if Timer.seconds1 // 1 > 6:
        Timer.minutes0 += 1
        Timer.seconds1 = 0

    if Timer.minutes0 // 1 > 6:
        Timer.minutes1 += 1
        Timer.minutes0 = 0

    game()


menu()
