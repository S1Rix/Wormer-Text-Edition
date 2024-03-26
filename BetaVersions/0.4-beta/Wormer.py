"""
Wormer: Text Edition
ver. 0.4
By LooNuH
Date of beginning - 22.03.24
Date of release - 22.03.24
"""

import os

import msvcrt as menu_kb
import keyboard as game_kb

from time import sleep as pause

from random import randint as random

import vars
import render
import defs
import files_interaction as f


def __pressed_key(*expected_keys):
    if expected_keys:
        expected_keys = defs.adapted_list(expected_keys)
        while True:
            if menu_kb.kbhit():
                key = menu_kb.getwch()
                if key in expected_keys:
                    return key
    else:
        render.input_error()
        __back_to_menu(pause_time=2)


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

    def check_input(event):
        global last_input
        if event.event_type == game_kb.KEY_DOWN:
            last_input = event.name
    
    def you_lose(kb_hook, show_lose_text: bool = True):
        if score > defs.Get.best_score():
            defs.Set.best_score(score)
        if show_lose_text:
            render.you_lose()
        game_kb.unhook(kb_hook)
        __back_to_menu(pause_time=2)

    worm = Worm()
    plus = Point()
    separator = Point()

    level_times = (1.5, 0.75, 0.5, 0.25, 0.1)
    current_level_time = level_times[defs.Get.current_level()]

    event_counter = 0

    kb_hook = game_kb.hook(check_input)
    last_input = None
    controls = defs.Get.controls()
    controls_list = controls.in_list
    controls_list.append('b')

    while True:
        score = len(worm) - 1

        if not plus.exists:
            plus.spawn(collide_check=worm)

        try:
            worm.move()
        except GameOver:
            you_lose(kb_hook)
            break

        if plus.collides_with(worm.body[Worm.head]):
            worm.add_tail()
            plus.respawn(collide_check=worm)

        render.game_map(score, worm, plus, separator)
        
        pause(current_level_time)

        last_input_backup = last_input
        if last_input:
            last_input = None
            if last_input_backup == controls.in_dict['up']:
                worm.change_direction('up')
            elif last_input_backup == controls.in_dict['left']:
                worm.change_direction('left')
            elif last_input_backup == controls.in_dict['down']:
                worm.change_direction('down')
            elif last_input_backup == controls.in_dict['right']:
                worm.change_direction('right')
            elif last_input_backup == 'b':
                you_lose(kb_hook, show_lose_text=False)
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
    options = defs.Get.controls().in_list
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
