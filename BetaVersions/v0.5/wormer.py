"""
Wormer: Text Edition
ver. 0.5
By LooNuH
Date of beginning - 28.03.24
Date of release - 29.03.24
"""

import os
import traceback
import keyboard
from time import sleep as pause
from random import randint as random

try:
    import vars
    import renders
    from renders import render
    import defs
    import files_interaction as f
except Exception:
    traceback.print_exc()
    os.system('pause')
    quit()


class __Keyboard:
    def __init__(self):
        self.__last_input = None
        self.__kb_hook = None
        self.__key_pressed = False

    def __input_catcher(self, event):
        if event.event_type == keyboard.KEY_DOWN:
            self.__last_input = event.name
            self.__key_pressed = True
        elif event.event_type == keyboard.KEY_UP:
            self.__key_pressed = False

    def get_input(self):
        return self.__last_input

    def key_pressed(self):
        return self.__key_pressed

    def reset_input(self):
        self.__last_input = None

    def hook(self):
        self.__kb_hook = keyboard.hook(self.__input_catcher)

    def unhook(self):
        keyboard.unhook(self.__kb_hook)
        self.reset_input()

    @staticmethod
    def detect(*expected_buttons):
        while True:
            for button in expected_buttons:
                if keyboard.is_pressed(button):
                    return button


def __build_menu(menu, options):
    kb = __Keyboard()
    selected_option = 0
    max_option = len(options) - 1
    renders.clear()
    while True:
        render(menu, options=options, selected_option=selected_option)
        kb.hook()
        while True:
            if not kb.key_pressed():
                last_input = kb.get_input()
                if last_input == 'up' and selected_option > 0:
                    kb.reset_input()
                    selected_option -= 1
                    break
                elif last_input == 'down' and selected_option < max_option:
                    kb.reset_input()
                    selected_option += 1
                    break
                elif last_input == 'enter':
                    kb.unhook()
                    options[selected_option]['def']()
                    return


def main_menu():
    menu_options = [
        {'name': 'Play', 'def': __play},
        {'name': 'Settings', 'def': __settings},
        {'name': 'Exit', 'def': quit},
    ]
    while True:
        __build_menu(renders.menu, menu_options)


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

    def game_over(show_lose_text: bool = True):
        if score > defs.Get.best_score():
            defs.Set.best_score(score)
        if show_lose_text:
            render(renders.you_lose)
        else:
            render(renders.back_to_menu_text)
        kb.unhook()
        pause(2)

    kb = __Keyboard()
    worm = Worm()
    plus = Point()
    separator = Point()

    level_times = (1.5, 0.75, 0.5, 0.25, 0.1)
    current_level_time = level_times[defs.Get.current_level()]

    event_counter = 0

    kb.hook()
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
            game_over()
            break

        if plus.collides_with(worm.body[Worm.head]):
            worm.add_tail()
            plus.respawn(collide_check=worm)

        render(renders.game_map, score=score, worm=worm, plus=plus, separator=separator)
        
        pause(current_level_time)

        last_input = kb.get_input()
        if last_input:
            kb.reset_input()
            if last_input == controls.in_dict['up']:
                worm.change_direction('up')
            elif last_input == controls.in_dict['left']:
                worm.change_direction('left')
            elif last_input == controls.in_dict['down']:
                worm.change_direction('down')
            elif last_input == controls.in_dict['right']:
                worm.change_direction('right')
            elif last_input == 'b':
                renders.clear()
                game_over(show_lose_text=False)
                break


def __settings():
    class BackToMenu(Exception):
        pass

    def back_to_menu():
        raise BackToMenu

    def level_select():
        kb = __Keyboard()
        renders.clear()
        while True:
            current_level = f.get(vars.files_data_current_level)
            render(renders.level_select)
            kb.hook()
            while True:
                if not kb.key_pressed():
                    last_input = kb.get_input()
                    if last_input == 'left' and current_level > 1:
                        kb.reset_input()
                        f.update(vars.files_data_current_level, current_level - 1)
                        break
                    elif last_input == 'right' and current_level < 4:
                        kb.reset_input()
                        f.update(vars.files_data_current_level, current_level + 1)
                        break
                    elif last_input == 'b':
                        kb.unhook()
                        render(renders.back_to_menu_text)
                        pause(1)
                        return

    def controls():
        while True:
            render(renders.controls)

            options_list = defs.Get.controls().in_list
            options_list.append('b')

            button = __Keyboard.detect(*options_list)
            if button in options_list[:-1]:
                edit_control(button)
            elif button == 'b':
                render(renders.back_to_menu_text)
                pause(1)
                return

    def edit_control(button):
        controls_list = defs.Get.controls().in_list
        controls_dict = defs.Get.controls().in_dict

        action = defs.find_key_in(controls_dict, button)

        render(renders.control_edit, action=action)

        kb = __Keyboard()
        kb.hook()
        while True:
            if not kb.key_pressed():
                button = kb.get_input()
                if button in controls_list:
                    kb.reset_input()
                    print('you can not bind this key')
                elif button is not None:
                    kb.unhook()
                    controls_dict[action] = button
                    defs.Set.controls(list(controls_dict.values()))
                    pause(0.25)
                    return

    def score_reset():
        render(renders.score_reset_question)
        match __Keyboard.detect('y', 'n'):
            case 'y':
                f.update(vars.files_data_best_score, 0)
                render(renders.score_reset_complete)
            case 'n':
                render(renders.back_to_menu_text)
        pause(2)

    settings_options = [
        {'name': 'Level change', 'def': level_select},
        {'name': 'Controls', 'def': controls},
        {'name': 'Reset best score', 'def': score_reset},
        {'name': 'Back to menu', 'def': back_to_menu},
    ]
    while True:
        try:
            __build_menu(renders.settings, settings_options)
        except BackToMenu:
            break


if __name__ == "__main__":
    try:
        main_menu()
    except Exception:
        defs.show_error()
    os.system('pause')
