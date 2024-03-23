# Wormer: Text Edition
# ver. 0.2
# By LooNuH
# Date of beginning - 20.04.23
# Date of release - 01.05.23

import os
import time
import msvcrt
import random as r

class Text:
    blank = ' '
    line20 = ' --------------------'
    wormer = 'Wormer'
    start = 'p - Play'
    level = 'l - Change level'
    controls = 'c - Controls'
    exit = 'e - Exit'
    controlst = 'Controls'
    up = ' - Move up'
    left = ' - Move left'
    down = ' - Move down'
    right = ' - Move right'
    menu = 'b - Back to menu'
    whatlevel = ' Enter difficulty level (1-6)'
    line61 = '-------------------------------------------------------------'
    youlose = 'You lose!'

class Tex:
    headUp = '^'
    headDown = 'v'
    headLeft = '<'
    headRight = '>'
    tail = '0'
    dot = '*'

class Game:

    class Timer:
        seconds1 = 0
        seconds0 = 0
        minutes1 = 0
        minutes0 = 0

    class Controls:
        up = 'w'
        down = 's'
        left = 'a'
        right = 'd'

    class Worm:
        body = [0, {'x': 7, 'y': 6, 'way': 'up'}]
        bodydef = None

    class Map:
        levels = [1, 1, 0.75, 0.5, 0.25, 0.1, 0.05]
        level = levels[0]

        hasPoint = False

        class Point:
            class Pos:
                x = 0
                y = 0


def clear(mode='def'):
    if mode == 'def':
        os.system('cls')
    if mode == 'debug':
        return


def ans(where):

    def ask():
        if msvcrt.kbhit():
            return msvcrt.getch()
        return False

    if where == 'game':
        time.sleep(Game.Map.level)
    else:
        time.sleep(0.25)

    answer = ask()

    if not answer:
        if where == 'game':
            return
        else:
            ans(where)

    else:
        answer = answer.decode()

        if where == 'menu':

            if answer == 'p':
                Game.Worm.bodydef = Game.Worm.body
                game()

            if answer == 'l':
                level()

            if answer == 'c':
                controls()

            if answer == 'e':
                quit()

            menu()

        if where == 'controls':

            if answer == Game.Controls.up:
                print('Bind new control key')
                ans('editcontrolup')

            if answer == Game.Controls.left:
                print('Bind new control key')
                ans('editcontrolleft')

            if answer == Game.Controls.down:
                print('Bind new control key')
                ans('editcontroldown')

            if answer == Game.Controls.right:
                print('Bind new control key')
                ans('editcontrolright')

            if answer == 'b':
                menu()

            controls()


        if 'editcontrol' in where:

            if not answer:
                ans(where)

            if where == 'editcontrolup':
                Game.Controls.up = answer

            if where == 'editcontrolleft':
                Game.Controls.left = answer

            if where == 'editcontroldown':
                Game.Controls.down = answer

            if where == 'editcontrolright':
                Game.Controls.right = answer

            controls()

        if where == 'game':

            if answer == Game.Controls.up:
                Game.Worm.body[1]['way'] = 'up'

            if answer == Game.Controls.left:
                Game.Worm.body[1]['way'] = 'left'

            if answer == Game.Controls.down:
                Game.Worm.body[1]['way'] = 'down'

            if answer == Game.Controls.right:
                Game.Worm.body[1]['way'] = 'right'


def menu():
    clear()

    print(Text.line20, '\n',
          Text.blank*8, Text.wormer, '\n',
          Text.line20, '\n',
          Text.blank*3, Text.start, '\n',
          Text.blank*3, Text.level, '\n',
          Text.blank*3, Text.controls, '\n',
          Text.blank*3, Text.exit, '\n',
          Text.line20, '\n',
          sep='')

    ans('menu')


def level():
    clear()

    print(Text.whatlevel)

    try:
        Game.Map.level = Game.Map.levels[int(input('>>> '))]
    except ValueError:
        level()
    except IndexError:
        level()

    menu()


def controls():
    clear()

    print(Text.line20, '\n',
          Text.blank*8, Text.controlst, '\n',
          Text.line20, '\n',
          Text.blank*3, Game.Controls.up, Text.up, '\n',
          Text.blank*3, Game.Controls.left, Text.left, '\n',
          Text.blank*3, Game.Controls.down, Text.down, '\n',
          Text.blank*3, Game.Controls.right, Text.right, '\n',
          Text.line20, '\n',
          Text.blank*3, Text.menu, '\n',
          Text.line20, '\n',
          sep='')

    ans('controls')


def game():

    clear()

    field = {
        14: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        13: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        12: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        11: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        10: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        9: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        8: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        7: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        6: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        5: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        4: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        3: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        2: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        1: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        0: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    }

    error = False

    if Game.Worm.body[1]['y'] == Game.Map.Point.Pos.y and Game.Worm.body[1]['x'] == Game.Map.Point.Pos.x:
        Game.Worm.body.append({'x': Game.Worm.body[-1]['x'], 'y': Game.Worm.body[-1]['y']})
        Game.Map.hasPoint = False

    if not Game.Map.hasPoint:

        def pointCreate():
            Game.Map.Point.Pos.x = r.randint(0, 14)
            Game.Map.Point.Pos.y = r.randint(0, 14)

        def pointCheck():
            for pointcheck in range(2, len(Game.Worm.body)):
                if Game.Map.Point.Pos.x == Game.Worm.body[pointcheck]['x'] and Game.Map.Point.Pos.y == Game.Worm.body[pointcheck]['y']:
                    pointCreate()
                    pointCheck()

        pointCreate()
        pointCheck()

        Game.Map.hasPoint = True

    field[Game.Map.Point.Pos.y][Game.Map.Point.Pos.x] = Tex.dot

    if len(Game.Worm.body) > 2:
        Game.Worm.body.insert(2, {'x': Game.Worm.body[1]['x'], 'y': Game.Worm.body[1]['y']})
        Game.Worm.body.pop()

    if len(Game.Worm.body) > 2:
        for taildots in range(2, len(Game.Worm.body)):
            field[Game.Worm.body[taildots]['y']][Game.Worm.body[taildots]['x']] = Tex.tail

    if Game.Worm.body[1]['way'] == 'up':
        Game.Worm.body[1]['y'] += 1

    if Game.Worm.body[1]['way'] == 'down':
        Game.Worm.body[1]['y'] -= 1

    if Game.Worm.body[1]['way'] == 'left':
        Game.Worm.body[1]['x'] -= 1

    if Game.Worm.body[1]['way'] == 'right':
        Game.Worm.body[1]['x'] += 1

    for check in range(2, len(Game.Worm.body)):
        if Game.Worm.body[1]['x'] == Game.Worm.body[check]['x'] and Game.Worm.body[1]['y'] == Game.Worm.body[check]['y']:
            error = True

    try:

        if Game.Worm.body[1]['way'] == 'up':
            field[Game.Worm.body[1]['y']][Game.Worm.body[1]['x']] = Tex.headUp

        if Game.Worm.body[1]['way'] == 'down':
            field[Game.Worm.body[1]['y']][Game.Worm.body[1]['x']] = Tex.headDown

        if Game.Worm.body[1]['way'] == 'left':
            field[Game.Worm.body[1]['y']][Game.Worm.body[1]['x']] = Tex.headLeft

        if Game.Worm.body[1]['way'] == 'right':
            field[Game.Worm.body[1]['y']][Game.Worm.body[1]['x']] = Tex.headRight

    except KeyError:
        error = True
    except IndexError:
        error = True

    if Game.Worm.body[1]['x'] < 0 or Game.Worm.body[1]['y'] < 0:
        error = True

    if error:
        Game.Worm.body = Game.Worm.bodydef

        Game.Timer.seconds0 = 0
        Game.Timer.seconds1 = 0
        Game.Timer.minutes0 = 0
        Game.Timer.minutes1 = 0

        print(Text.blank*3, Text.youlose)
        time.sleep(2)
        menu()

    timer = str(Game.Timer.minutes1) + str(Game.Timer.minutes0) + ':' + str(Game.Timer.seconds1) + str(round(Game.Timer.seconds0 // 1))

    print(Text.line61, '\n',
          '             Time: ', timer, '                Score: ', (len(Game.Worm.body) - 2), '\n',
          Text.line61, '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[14][0], ' | ', field[14][1], ' | ', field[14][2], ' | ', field[14][3], ' | ', field[14][4], ' | ', field[14][5], ' | ', field[14][6], ' | ', field[14][7], ' | ', field[14][8], ' | ', field[14][9], ' | ', field[14][10], ' | ', field[14][11], ' | ', field[14][12], ' | ', field[14][13], ' | ', field[14][14], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[13][0], ' | ', field[13][1], ' | ', field[13][2], ' | ', field[13][3], ' | ', field[13][4], ' | ', field[13][5], ' | ', field[13][6], ' | ', field[13][7], ' | ', field[13][8], ' | ', field[13][9], ' | ', field[13][10], ' | ', field[13][11], ' | ', field[13][12], ' | ', field[13][13], ' | ', field[13][14], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[12][0], ' | ', field[12][1], ' | ', field[12][2], ' | ', field[12][3], ' | ', field[12][4], ' | ', field[12][5], ' | ', field[12][6], ' | ', field[12][7], ' | ', field[12][8], ' | ', field[12][9], ' | ', field[12][10], ' | ', field[12][11], ' | ', field[12][12], ' | ', field[12][13], ' | ', field[12][14], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[11][0], ' | ', field[11][1], ' | ', field[11][2], ' | ', field[11][3], ' | ', field[11][4], ' | ', field[11][5], ' | ', field[11][6], ' | ', field[11][7], ' | ', field[11][8], ' | ', field[11][9], ' | ', field[11][10], ' | ', field[11][11], ' | ', field[11][12], ' | ', field[11][13], ' | ', field[11][14], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[10][0], ' | ', field[10][1], ' | ', field[10][2], ' | ', field[10][3], ' | ', field[10][4], ' | ', field[10][5], ' | ', field[10][6], ' | ', field[10][7], ' | ', field[10][8], ' | ', field[10][9], ' | ', field[10][10], ' | ', field[10][11], ' | ', field[10][12], ' | ', field[10][13], ' | ', field[10][14], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[9][0], ' | ', field[9][1], ' | ', field[9][2], ' | ', field[9][3], ' | ', field[9][4], ' | ', field[9][5], ' | ', field[9][6], ' | ', field[9][7], ' | ', field[9][8], ' | ', field[9][9], ' | ', field[9][10], ' | ', field[9][11], ' | ', field[9][12], ' | ', field[9][13], ' | ', field[9][14], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[8][0], ' | ', field[8][1], ' | ', field[8][2], ' | ', field[8][3], ' | ', field[8][4], ' | ', field[8][5], ' | ', field[8][6], ' | ', field[8][7], ' | ', field[8][8], ' | ', field[8][9], ' | ', field[8][10], ' | ', field[8][11], ' | ', field[8][12], ' | ', field[8][13], ' | ', field[8][14], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[7][0], ' | ', field[7][1], ' | ', field[7][2], ' | ', field[7][3], ' | ', field[7][4], ' | ', field[7][5], ' | ', field[7][6], ' | ', field[7][7], ' | ', field[7][8], ' | ', field[7][9], ' | ', field[7][10], ' | ', field[7][11], ' | ', field[7][12], ' | ', field[7][13], ' | ', field[7][14], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[6][0], ' | ', field[6][1], ' | ', field[6][2], ' | ', field[6][3], ' | ', field[6][4], ' | ', field[6][5], ' | ', field[6][6], ' | ', field[6][7], ' | ', field[6][8], ' | ', field[6][9], ' | ', field[6][10], ' | ', field[6][11], ' | ', field[6][12], ' | ', field[6][13], ' | ', field[6][14], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[5][0], ' | ', field[5][1], ' | ', field[5][2], ' | ', field[5][3], ' | ', field[5][4], ' | ', field[5][5], ' | ', field[5][6], ' | ', field[5][7], ' | ', field[5][8], ' | ', field[5][9], ' | ', field[5][10], ' | ', field[5][11], ' | ', field[5][12], ' | ', field[5][13], ' | ', field[5][14], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[4][0], ' | ', field[4][1], ' | ', field[4][2], ' | ', field[4][3], ' | ', field[4][4], ' | ', field[4][5], ' | ', field[4][6], ' | ', field[4][7], ' | ', field[4][8], ' | ', field[4][9], ' | ', field[4][10], ' | ', field[4][11], ' | ', field[4][12], ' | ', field[4][13], ' | ', field[4][14], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[3][0], ' | ', field[3][1], ' | ', field[3][2], ' | ', field[3][3], ' | ', field[3][4], ' | ', field[3][5], ' | ', field[3][6], ' | ', field[3][7], ' | ', field[3][8], ' | ', field[3][9], ' | ', field[3][10], ' | ', field[3][11], ' | ', field[3][12], ' | ', field[3][13], ' | ', field[3][14], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[2][0], ' | ', field[2][1], ' | ', field[2][2], ' | ', field[2][3], ' | ', field[2][4], ' | ', field[2][5], ' | ', field[2][6], ' | ', field[2][7], ' | ', field[2][8], ' | ', field[2][9], ' | ', field[2][10], ' | ', field[2][11], ' | ', field[2][12], ' | ', field[2][13], ' | ', field[2][14], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +', '\n',
          '| ', field[1][0], ' | ', field[1][1], ' | ', field[1][2], ' | ', field[1][3], ' | ', field[1][4], ' | ', field[1][5], ' | ', field[1][6], ' | ', field[1][7], ' | ', field[1][8], ' | ', field[1][9], ' | ', field[1][10], ' | ', field[1][11], ' | ', field[1][12], ' | ', field[1][13], ' | ', field[1][14], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +', '\n',
           '| ', field[0][0], ' | ', field[0][1], ' | ', field[0][2], ' | ', field[0][3], ' | ', field[0][4], ' | ', field[0][5], ' | ', field[0][6], ' | ', field[0][7], ' | ', field[0][8], ' | ', field[0][9], ' | ', field[0][10], ' | ', field[0][11], ' | ', field[0][12], ' | ', field[0][13], ' | ', field[0][14], ' |', '\n',
          '+ — + — + — + — + — + — + — + — + — + — + — + — + — + — + — +',
          sep='')


    ans('game')


    Game.Timer.seconds0 += Game.Map.level

    if round(Game.Timer.seconds0 // 1) > 9:
        Game.Timer.seconds1 += 1
        Game.Timer.seconds0 = 0

    if Game.Timer.seconds1 > 5:
        Game.Timer.minutes0 += 1
        Game.Timer.seconds1 = 0

    if Game.Timer.minutes0 > 9:
        Game.Timer.minutes1 += 1
        Game.Timer.minutes0 = 0


    game()


menu()
