# Wormer: Text Edition
# ver. 0.4
# By LooNuH
# Date of beginning - 26.05.23
# Date of release - never

import os
from time import sleep as s
import msvcrt as m
from random import randint as r


# Clear function - clears console

#                  mode - 'def' - clear console
#                       'debug' - skip clear function - good for debugging
def clear(mode='def'):
    if mode == 'def':
        os.system('cls')
    if mode == 'debug':
        return


# Colors class
class Color:
    disabled = '\033[1;30m'
    header = '\033[95m'
    bold = '\033[1m'
    underline = '\033[4m'
    warning = '\033[93m'
    fail = '\033[91m'
    end = '\033[0m'


class Data:
    @staticmethod
    def Import(what='all'):
        if what == 'all':
            Data.Import('controls')
            Data.Import('best')

        if what == 'controls':
            controlsIn = open('data/controls', 'r')

            Game.Controls.up = controlsIn.readline()[:-1]
            Game.Controls.left = controlsIn.readline()[:-1]
            Game.Controls.down = controlsIn.readline()[:-1]
            Game.Controls.right = controlsIn.readline()[:-1]

            controlsIn.close()

        if what == 'best':
            bestIn = open('data/best', 'r')

            Game.bestScore = int(bestIn.readline())

            bestIn.close()

    @staticmethod
    def Export(what='all'):
        if what == 'all':
            Data.Export('controls')
            Data.Export('best')

        if what == 'controls':
            controlsOut = open('data/controls', 'w')

            controlsOut.write(Game.Controls.up + '\n')
            controlsOut.write(Game.Controls.left + '\n')
            controlsOut.write(Game.Controls.down + '\n')
            controlsOut.write(Game.Controls.right + '\n')

            controlsOut.close()

        if what == 'best':
            bestOut = open('data/best', 'w')

            bestOut.write(str(Game.bestScore) + '\n')

            bestOut.close()


# Main menu and it's settings
class Menu:
    # Menu text
    class Text:
        line35 = ' + — — — — — — — — — — — — — — — — +'
        line35paste = ' |                                  |'
        wormer = 'Wormer - 0.4'
        best = 'Best score:'
        start = 'p - Play'
        level = 'l - Change level'
        controls = 'c - Controls'
        resetb = 'r - Reset best score'
        exit = 'e - Exit'

        whatlevel = ' Change difficulty level'
        curlevel = ' Current level: '
        level14 = '1-4 - Level 1-4'

        controlst = 'Controls'
        up = ' - Move up'
        left = ' - Move left'
        down = ' - Move down'
        right = ' - Move right'

        resetc = 'r - Reset controls'
        menu = 'b - Back to menu'

    class Controls:
        play = 'p'
        level = 'l'
        controls = 'c'
        reset = 'r'
        menuBack = 'b'
        exit = 'e'

    # Menu itself (autostart)
    @staticmethod
    def __init__():
        clear()

        Data.Import()

        print(Menu.Text.line35, '\n',
              Menu.Text.line35paste[:12], Menu.Text.wormer, Menu.Text.line35paste[13 + len(Menu.Text.wormer):], '\n',
              Menu.Text.line35, '\n',
              Menu.Text.line35paste[:11], Menu.Text.best, Menu.Text.line35paste[15:16], Game.bestScore, Menu.Text.line35paste[24 + len(str(Game.bestScore)):], '\n',
              Menu.Text.line35, '\n',
              Menu.Text.line35paste[:9], Menu.Text.start, Menu.Text.line35paste[10 + len(Menu.Text.start):], '\n',
              Menu.Text.line35paste[:9], Menu.Text.level, Menu.Text.line35paste[10 + len(Menu.Text.level):], '\n',
              Menu.Text.line35paste[:9], Menu.Text.controls, Menu.Text.line35paste[10 + len(Menu.Text.controls):], '\n',
              Menu.Text.line35paste[:9], Menu.Text.resetb, Menu.Text.line35paste[10 + len(Menu.Text.resetb):], '\n',
              Menu.Text.line35paste[:9], Menu.Text.exit, Menu.Text.line35paste[10 + len(Menu.Text.exit):], '\n',
              Menu.Text.line35, '\n',
              sep='')

        Menu.__keyinput('menu')

    @staticmethod
    def __keyinput(where):
        def ask():
            if m.kbhit():
                def decode(what):
                    try:
                        return what.decode().lower()
                    except UnicodeDecodeError:
                        return
                return decode(m.getch())
            return

        s(0.5)
        answer = ask()

        if where == 'menu':

            if answer == Menu.Controls.play:
                Game.start()

            if answer == Menu.Controls.level:
                Menu.__level()

            if answer == Menu.Controls.controls:
                Menu.__controls()

            if answer == Menu.Controls.reset:
                Menu.__reset('best')

            if answer == Menu.Controls.exit:
                quit()

            Menu()

        if where == 'level':

            if answer == '1' and Game.Map.level != Game.Map.levels[1]:
                Game.Map.level = Game.Map.levels[1]

            if answer == '2' and Game.Map.level != Game.Map.levels[2]:
                Game.Map.level = Game.Map.levels[2]

            if answer == '3' and Game.Map.level != Game.Map.levels[3]:
                Game.Map.level = Game.Map.levels[3]

            if answer == '4' and Game.Map.level != Game.Map.levels[4]:
                Game.Map.level = Game.Map.levels[4]

            if answer == 'b':
                Menu()

            else:
                Menu.__level()

            Menu()

        if where == 'controls':

            if answer == Game.Controls.up:
                print('Bind new control key')
                Menu.__keyinput('editcontrolup')

            if answer == Game.Controls.left:
                print('Bind new control key')
                Menu.__keyinput('editcontrolleft')

            if answer == Game.Controls.down:
                print('Bind new control key')
                Menu.__keyinput('editcontroldown')

            if answer == Game.Controls.right:
                print('Bind new control key')
                Menu.__keyinput('editcontrolright')

            if answer == 'r':
                Menu.__reset('controls')

            if answer == 'b':
                Menu()

            Menu.__controls()

        if 'editcontrol' in where:

            if not answer or \
                    answer == Game.Controls.up or \
                    answer == Game.Controls.down or \
                    answer == Game.Controls.left or \
                    answer == Game.Controls.right or \
                    \
                    answer == Menu.Controls.play or \
                    answer == Menu.Controls.level or \
                    answer == Menu.Controls.controls or \
                    answer == Menu.Controls.reset or \
                    answer == Menu.Controls.menuBack or \
                    answer == Menu.Controls.exit:
                Menu.__keyinput(where)

            if where == 'editcontrolup':
                Game.Controls.up = answer

            if where == 'editcontrolleft':
                Game.Controls.left = answer

            if where == 'editcontroldown':
                Game.Controls.down = answer

            if where == 'editcontrolright':
                Game.Controls.right = answer

            Data.Export('controls')

            Menu.__controls()

    # Level settings menu
    @staticmethod
    def __level():
        clear()

        print(Menu.Text.line35, '\n',
              Menu.Text.line35paste[:6], Menu.Text.whatlevel, Menu.Text.line35paste[7 + len(Menu.Text.whatlevel):], '\n',
              Menu.Text.line35paste[:10], Menu.Text.curlevel, Game.Map.levels.index(Game.Map.level), Menu.Text.line35paste[12 + len(Menu.Text.curlevel):], '\n',
              Menu.Text.line35, '\n',
              Menu.Text.line35paste[:12], Menu.Text.level14, Menu.Text.line35paste[13 + len(Menu.Text.level14):], '\n',
              Menu.Text.line35, '\n',
              Menu.Text.line35paste[:11], Menu.Text.menu, Menu.Text.line35paste[12 + len(Menu.Text.menu):], '\n',
              Menu.Text.line35, '\n',
              sep='')

        Menu.__keyinput('level')

        Menu()

    # Controls settings menu
    @staticmethod
    def __controls():
        clear()

        print(Menu.Text.line35, '\n',
              Menu.Text.line35paste[:14], Menu.Text.controlst, Menu.Text.line35paste[15 + len(Menu.Text.controlst):], '\n',
              Menu.Text.line35, '\n',
              Menu.Text.line35paste[:11], Game.Controls.up, Menu.Text.up, Menu.Text.line35paste[12 + len(Game.Controls.up) + len(Menu.Text.up):], '\n',
              Menu.Text.line35paste[:11], Game.Controls.left, Menu.Text.left, Menu.Text.line35paste[12 + len(Game.Controls.left) + len(Menu.Text.left):], '\n',
              Menu.Text.line35paste[:11], Game.Controls.down, Menu.Text.down, Menu.Text.line35paste[12 + len(Game.Controls.down) + len(Menu.Text.down):], '\n',
              Menu.Text.line35paste[:11], Game.Controls.right, Menu.Text.right, Menu.Text.line35paste[12 + len(Game.Controls.right) + len(Menu.Text.right):], '\n',
              Menu.Text.line35, '\n',
              Menu.Text.line35paste[:9], Menu.Text.resetc, Menu.Text.line35paste[10 + len(Menu.Text.resetc):], '\n',
              Menu.Text.line35paste[:10], Menu.Text.menu, Menu.Text.line35paste[11 + len(Menu.Text.menu):], '\n',
              Menu.Text.line35, '\n',
              sep='')

        Menu.__keyinput('controls')

    # Reset controls or best score menu
    @staticmethod
    def __reset(what):
        if what == 'controls':
            Game.Controls.up = 'w'
            Game.Controls.left = 'a'
            Game.Controls.down = 's'
            Game.Controls.right = 'd'
            Data.Export('controls')
            Menu.__controls()

        if what == 'best':
            Game.bestScore = 0
            Data.Export('best')
            Menu()


# Game itself - all Wormer game logic
class Game:

    # Text class - contains all in-game messages
    class Text:
        sline33 = '+                               +'
        gline33 = '+ — — — — — — — — — — — — — — — +'
        blank = ' '
        sep = ' | '
        youlose = 'You lose!'

    # Texture class - contains worm textures
    class Texture:
        headUp = Color.end + '^' + Color.disabled
        headDown = Color.end + 'v' + Color.disabled
        headLeft = Color.end + '<' + Color.disabled
        headRight = Color.end + '>' + Color.disabled
        tail = Color.end + 'o' + Color.disabled
        dot = Color.end + '+' + Color.disabled
        sep = Color.fail + ':' + Color.disabled

    # Worm data - coordinates
    wormBody = [{'x': 7, 'y': 6, 'way': 'up'}, {'x': 7, 'y': 5}]

    # Controls data
    class Controls:
        up = None
        down = None
        left = None
        right = None

    # Map data - levels and points
    class Map:
        # Levels tuple
        levels = (2, 1, 0.5, 0.25, 0.1)
        level = levels[1]

        ycountdown = (14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0)

        # Point coordinates data
        class Point:
            exists = False

            class Pos:
                x = 0
                y = 0

        class SepPoint:
            exists = False
            spawntime = 0

            class Pos:
                x = None
                y = None

    # Best score var
    bestScore = 0

    # Timer data
    timer = [0, 0, 0, 0]

    # Counter for random orbs spawn
    eventcounter = 0

    @staticmethod
    def __keyinput():
        def ask():
            if m.kbhit():
                def decode(what):
                    try:
                        return what.decode().lower()
                    except UnicodeDecodeError:
                        return
                return decode(m.getch())
            return

        s(Game.Map.level)
        answer = ask()

        if answer == Game.Controls.up and Game.wormBody[0]['way'] != 'down':
            Game.wormBody[0]['way'] = 'up'

        if answer == Game.Controls.left and Game.wormBody[0]['way'] != 'right':
            Game.wormBody[0]['way'] = 'left'

        if answer == Game.Controls.down and Game.wormBody[0]['way'] != 'up':
            Game.wormBody[0]['way'] = 'down'

        if answer == Game.Controls.right and Game.wormBody[0]['way'] != 'left':
            Game.wormBody[0]['way'] = 'right'

        if answer == 'z':
            Game.__lose()
            Menu()

    @staticmethod
    def start():
        clear()
        field = {}
        for y in Game.Map.ycountdown:
            field[y] = list(15 * ' ')

        class Point:
            @staticmethod
            def Create(what):

                if what == 'score':
                    Game.Map.Point.Pos.x = r(0, 14)
                    Game.Map.Point.Pos.y = r(0, 14)
                    Game.Map.Point.exists = True

                if what == 'sep':
                    Game.Map.SepPoint.Pos.x = r(0, 14)
                    Game.Map.SepPoint.Pos.y = r(0, 14)
                    Game.Map.SepPoint.exists = True

                Point.Check(what)

            @staticmethod
            def Check(what='all'):
                if what == 'all':
                    Point.Check('score')
                    Point.Check('sep')

                if what == 'score':
                    if Game.Map.Point.exists:
                        for pointcheck in range(1, len(Game.wormBody)):
                            if Game.Map.Point.Pos.x == Game.wormBody[pointcheck]['x'] and \
                                    Game.Map.Point.Pos.y == Game.wormBody[pointcheck]['y']:
                                Point.Create(what)

                        if Game.wormBody[0]['y'] == Game.Map.Point.Pos.y and \
                                Game.wormBody[0]['x'] == Game.Map.Point.Pos.x:
                            Game.wormBody.append({'x': Game.wormBody[-1]['x'], 'y': Game.wormBody[-1]['y']})
                            Point.Create(what)

                    else:
                        Point.Create(what)

                if what == 'sep':
                    if Game.Map.SepPoint.exists:
                        for pointcheck in range(1, len(Game.wormBody)):
                            if Game.Map.SepPoint.Pos.x == Game.wormBody[pointcheck]['x'] and \
                                    Game.Map.SepPoint.Pos.y == Game.wormBody[pointcheck]['y']:
                                Point.Create(what)

                        if Game.wormBody[0]['y'] == Game.Map.SepPoint.Pos.y and \
                                Game.wormBody[0]['x'] == Game.Map.SepPoint.Pos.x:
                            for col in range(len(Game.wormBody) // 2):
                                Game.wormBody.pop()
                            Game.Map.SepPoint.exists = False

                    elif Game.Map.SepPoint.spawntime == 0:
                        Game.Map.SepPoint.spawntime = r(1, 10)

                    elif round(Game.eventcounter // 1) == Game.Map.SepPoint.spawntime:
                        Point.Create(what)

        try:

            error = False

            def update():
                Game.wormBody.insert(1, {'x': Game.wormBody[0]['x'], 'y': Game.wormBody[0]['y']})
                Game.wormBody.pop()

            update()

            if Game.wormBody[0]['way'] == 'up':
                Game.wormBody[0]['y'] += 1

            if Game.wormBody[0]['way'] == 'down':
                Game.wormBody[0]['y'] -= 1

            if Game.wormBody[0]['way'] == 'left':
                Game.wormBody[0]['x'] -= 1

            if Game.wormBody[0]['way'] == 'right':
                Game.wormBody[0]['x'] += 1

            for check in range(1, len(Game.wormBody)):
                if Game.wormBody[0]['x'] == Game.wormBody[check]['x'] and \
                        Game.wormBody[0]['y'] == Game.wormBody[check]['y']:
                    error = True

            Point.Check()

            class ObjectsRender:
                if Game.Map.Point.exists:
                    field[Game.Map.Point.Pos.y][Game.Map.Point.Pos.x] = Game.Texture.dot
                if Game.Map.SepPoint.exists:
                    field[Game.Map.SepPoint.Pos.y][Game.Map.SepPoint.Pos.x] = Game.Texture.sep

                for taildots in range(1, len(Game.wormBody)):
                    field[Game.wormBody[taildots]['y']][Game.wormBody[taildots]['x']] = Game.Texture.tail

                if Game.wormBody[0]['way'] == 'up':
                    field[Game.wormBody[0]['y']][Game.wormBody[0]['x']] = Game.Texture.headUp
                if Game.wormBody[0]['way'] == 'down':
                    field[Game.wormBody[0]['y']][Game.wormBody[0]['x']] = Game.Texture.headDown
                if Game.wormBody[0]['way'] == 'left':
                    field[Game.wormBody[0]['y']][Game.wormBody[0]['x']] = Game.Texture.headLeft
                if Game.wormBody[0]['way'] == 'right':
                    field[Game.wormBody[0]['y']][Game.wormBody[0]['x']] = Game.Texture.headRight

        except KeyError:
            error = True
        except IndexError:
            error = True

        if Game.wormBody[0]['x'] < 0 or Game.wormBody[0]['y'] < 0:
            error = True

        if error:
            Game.__lose()
            print(Game.Text.blank * 3, Game.Text.youlose)
            s(2)
            Menu()

        timer = ''
        for o in range(len(Game.timer)):
            if o != 3:
                timer += str(Game.timer[o])
            else:
                timer += str(round(Game.timer[o] // 1))
            if o == 1:
                timer += ':'

        print(Game.Text.sline33, '\n',
              '         Time: ', timer, ' ( ', round(Game.eventcounter // 1), ' ) ', '\n', '        Score: ', (len(Game.wormBody) - 2), '\n',
              Game.Text.sline33,
              sep='')

        fieldfinale = Game.Text.gline33 + '\n'
        for y in Game.Map.ycountdown:
            fieldfinale += Game.Text.sep[1:]
            for x in range(15):
                fieldfinale += field[y][x] + ' '
            fieldfinale += Game.Text.sep[1:] + '\n'
        fieldfinale += Game.Text.gline33 + '\n'

        print(Color.disabled + fieldfinale + Color.end)

        class TimerLogic:
            if Game.Map.level == Game.Map.levels[0] or \
                    Game.Map.level == Game.Map.levels[1] or \
                    Game.Map.level == Game.Map.levels[2]:
                Game.timer[3] += Game.Map.level
                Game.eventcounter += Game.Map.level

            if Game.Map.level == Game.Map.levels[3]:
                Game.timer[3] += 1.375 * Game.Map.level
                Game.eventcounter += 1.375 * Game.Map.level

            if Game.Map.level == Game.Map.levels[4]:
                Game.timer[3] += 1.5 * Game.Map.level
                Game.eventcounter += 1.5 * Game.Map.level

            if Game.eventcounter >= 120:
                Game.eventcounter = 0

            if Game.timer[3] // 1 > 9:
                Game.timer[2] += 1
                Game.timer[3] = 0

            if Game.timer[2] > 5:
                Game.timer[1] += 1
                Game.timer[2] = 0

            if Game.timer[2] > 9:
                Game.timer[0] += 1
                Game.timer[1] = 0

        Game.__keyinput()
        Game.start()

    @staticmethod
    def __lose():
        if (len(Game.wormBody) - 2) > Game.bestScore:
            Game.bestScore = (len(Game.wormBody) - 2)
            Data.Export('best')

        Game.wormBody = [{'x': 7, 'y': 6, 'way': 'up'}, {'x': 7, 'y': 5}]
        Game.timer = [0, 0, 0, 0]
        Game.eventcounter = 0

        Game.Map.Point.exists = False
        Game.Map.SepPoint.exists = False


# Program start
Menu()
