"""
Wormer: Text Edition
ver. 0.4
By LooNuH
Date of beginning - 22.03.24
Date of release - 22.03.24
"""

import os

import keyboard as kb_1
import msvcrt as kb_2

from time import sleep as pause

from random import randint as random

import vars
import render
import defs
import files_interaction as f


def __pressed_key(*expected_keys, wait_for_input: bool = True, exit_after: float = None):
    if expected_keys:
        expected_keys = defs.adapted_list(expected_keys)
        key_pressed = None
        while True:
            if exit_after is None:
                for key in expected_keys:
                    if kb_1.is_pressed(key):
                        key_pressed = key
            else:
                pause(exit_after)
                if kb_2.kbhit():
                    key = kb_2.getwch()
                    if key in expected_keys:
                        key_pressed = key
            if wait_for_input:
                if key_pressed:
                    return key_pressed
            else:
                return key_pressed
    else:
        return False


def main_menu():
    while True:
        render.menu()
        match __pressed_key('1', '2', '3', '4', 'e'):
            case '1':
                __play()
            case '2':
                __level_select()
            case '3':
                __controls()
            case '4':
                __score_reset()
            case 'e':
                quit()


def __back_to_menu(pause_time: int = 1):
    render.back_to_menu_text()
    pause(pause_time)


def __play():
    class MapObject:
        def __init__(self, x, y):
            self.x: int = x
            self.y: int = y

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

    class Point(MapObject):
        def __init__(self):
            super().__init__(-1, -1)
            self.exists: bool = False

        def spawn(self, collide_check):
            while True:
                self.x = random(0, 14)
                self.y = random(0, 14)
                _worm = collide_check
                point_collides_with_worm = False
                for bodypart in _worm.body:
                    if self.collides_with(bodypart):
                        point_collides_with_worm = True
                        break
                if not point_collides_with_worm:
                    break
            self.exists = True

        def respawn(self, collide_check):
            self.delete()
            self.spawn(collide_check)

        def delete(self):
            self.x = -1
            self.y = -1
            self.exists = False

    class Worm:
        head = 0
        end = -1

        class BodyPart(MapObject):
            def __init__(self, x, y, is_head=False):
                super().__init__(x, y)
                self.is_head: bool = is_head

        def __init__(self) -> None:
            self.body: list = [self.BodyPart(7, 7, is_head=True), self.BodyPart(7, 6)]
            self.direction: str = 'up'

        def __len__(self):
            return len(self.body)

        def show_body(self):
            print([part.info() for part in self.body])

        def move(self):
            self.body.insert(1, self.BodyPart(self.body[Worm.head].x, self.body[Worm.head].y))
            self.body.pop()

            if self.direction == 'up':
                self.body[Worm.head].y += 1
            elif self.direction == 'down':
                self.body[Worm.head].y -= 1
            elif self.direction == 'left':
                self.body[Worm.head].x -= 1
            elif self.direction == 'right':
                self.body[Worm.head].x += 1

            if not (0 <= self.body[Worm.head].x <= 14) or not (0 <= self.body[Worm.head].y <= 14):
                raise GameOver
            if self.collides_with_body():
                raise GameOver

        def change_direction(self, direction):
            direction_opposite = {
                'up': 'down',
                'down': 'up',
                'left': 'right',
                'right': 'left'
            }
            if self.direction != direction_opposite[direction]:
                self.direction = direction

        def add_tail(self):
            self.body.append(self.body[Worm.end])

        def collides_with_body(self):
            for part in range(1, len(self.body)):
                if self.body[Worm.head].collides_with(self.body[part]):
                    return True
            return False

    class GameOver(Exception):
        pass

    def you_lose():
        if score > defs.get_best_score():
            defs.set_best_score(score)
        render.you_lose()
        __back_to_menu(pause_time=2)

    worm = Worm()
    plus = Point()
    separator = Point()

    level_times = (1.5, 0.75, 0.5, 0.25, 0.1)
    current_level_time = level_times[defs.get_current_level()]

    event_counter = 0

    while True:
        score = len(worm) - 1

        if not plus.exists:
            plus.spawn(collide_check=worm)

        try:
            worm.move()
        except GameOver:
            you_lose()
            break

        if plus.collides_with(worm.body[Worm.head]):
            worm.add_tail()
            plus.respawn(collide_check=worm)

        render.game_map(score, worm, plus, separator)

        controls = defs.get_controls()
        controls_list = controls.in_list
        controls_list.append('b')
        pressed_key = __pressed_key(controls_list, wait_for_input=False, exit_after=current_level_time)
        if pressed_key:
            if pressed_key == controls.in_dict['up']:
                worm.change_direction('up')
            elif pressed_key == controls.in_dict['left']:
                worm.change_direction('left')
            elif pressed_key == controls.in_dict['down']:
                worm.change_direction('down')
            elif pressed_key == controls.in_dict['right']:
                worm.change_direction('right')

            elif pressed_key == 'b':
                __back_to_menu()
                break

        elif pressed_key is False:
            render.input_error()
            __back_to_menu(pause_time=2)
            break


def __level_select():
    while True:
        render.level_select()
        choice = __pressed_key('1', '2', '3', '4', 'b')
        if choice in ('1', '2', '3', '4'):
            f.update(vars.files_data_current_level, choice)
        else:
            __back_to_menu()
            return


def __controls():
    render.controls()
    options = 'b'
    
    """
    use this string when you implement key binding feature
    options = defs.get_controls().in_list
    options.append('b')
    """
    
    match __pressed_key(options):
        case 'b':
            __back_to_menu()


def __score_reset():
    render.score_reset_question()
    match __pressed_key('y', 'n'):
        case 'y':
            f.update(vars.files_data_best_score, 0)
            render.score_reset_complete()
        case 'n':
            pass
    __back_to_menu(pause_time=2)


if __name__ == "__main__":
    try:
        main_menu()
    except Exception:
        defs.show_error()
    os.system('pause')
