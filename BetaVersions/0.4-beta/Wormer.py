"""
Wormer: Text Edition
ver. 0.4
By LooNuH
Date of beginning - 22.03.24
Date of release - 22.03.24
"""

import os

from time import sleep as pause

import keyboard as kb

import render
import defs
import vars
import files_interaction as f


main_path = os.getcwd()


class MapObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def info(self):
        return {
            'x': self.x,
            'y': self.y
        }

    def collides_with(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False


class Worm:
    class BodyPart(MapObject):
        def __init__(self, x, y):
            super().__init__(x, y)
            
    def __init__(self) -> None:
        self.__head = 0
        self.__body = [self.BodyPart(7, 6), self.BodyPart(7, 5)]
        self.__direction = 'up'

    def show_body(self):
        head = self.__head
        body = self.__body
        print([part.info() for part in body])
    
    def move(self):
        head = self.__head
        body = self.__body
        try:
            body.insert(1, body[head])
            body.pop()
            
            if self.__direction == 'up':
                body[head].y += 1
            elif self.__direction == 'down':
                body[head].y -= 1
            elif self.__direction == 'left':
                body[head].x -= 1
            elif self.__direction == 'right':
                body[head].x += 1
        
        except Exception:
            defs.show_error()
    
    def change_direction(self, direction):
        direction_opposite = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }
        if self.__direction != direction_opposite[direction]:
            self.__direction = direction
    
    def add_tail(self):
        head = self.__head
        body = self.__body
        body.append(body[-1])
    
    def collides_with_body(self):
        head = self.__head
        body = self.__body
        for part in range(1, len(body)):
            if body[head].collides_with(body[part]):
                return True
        return False


def __kb_input(*keys: str, pause_time: float = 0.1):
    if keys:
        while True:
            for key in keys:
                if kb.is_pressed(key):
                    return key
            pause(pause_time)
    else:
        print('NO KEYS BINDED!')


def main_menu():
    render.menu()
    match __kb_input('1', '2', '3', '4', 'e'):
        case '1':
            __play()
        case '2':
            __level()
        case '3':
            __controls()
        case '4':
            __reset_score()
        case 'e':
            quit()


def __play():
    worm = Worm()
    worm.show_body()
    while True:
        break
    render.placeholder()


def __level():
    render.placeholder()


def __controls():
    render.placeholder()


def __reset_score():
    render.reset_score_question()
    match __kb_input('y', 'n'):
        case 'y':
            f.reset(vars.files_data_controls)
        case 'n':
            pass
    main_menu()


if __name__ == "__main__":
    try:
        main_menu()
    except Exception:
        defs.show_error()
        os.system('pause')
