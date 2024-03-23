"""
Wormer: Text Edition
ver. 0.4 RE
By LooNuH
Date of beginning - 22.03.24
Date of release - 22.03.24
"""

import os
import files_interaction as f


main_path = os.getcwd()

__files_data_best_score = os.path.join(main_path, 'data', 'best')
__files_textures_menu_choice = os.path.join(main_path, 'textures', 'menu')

__color_disabled = '\033[1;30m'
__color_header = '\033[95m'
__color_bold = '\033[1m'
__color_underline = '\033[4m'
__color_warning = '\033[93m'
__color_fail = '\033[91m'
__color_end = '\033[0m'


def text_in_line(text):
    space = 34 * ' '
    paste_line = ' |{}|'
    half_text_len = len(space) // 2
    half_line_len = len(paste_line) // 2
    if half_text_len % 2:
        paste_line.format(space[:half_line_len - half_text_len] + text + space[half_line_len - half_text_len:])
    else:
        paste_line.format(space[:(half_line_len - 1) - half_text_len] + text + space[half_line_len - half_text_len:])
    return paste_line


def update_score():
    global __texture_text_score
    __texture_text_score = text_in_line(f'Best score: {f.get(__files_data_best_score)}')


__texture_text_line = ' + — — — — — — — — — — — — — — — — +'
__texture_text_wormer_ver = text_in_line('Wormer - 0.4')
__texture_text_score = None
update_score()
__texture_choice = f.get(__files_textures_menu_choice)

headUp = __color_end + '^' + __color_disabled
headDown = __color_end + 'v' + __color_disabled
headLeft = __color_end + '<' + __color_disabled
headRight = __color_end + '>' + __color_disabled
tail = __color_end + 'o' + __color_disabled

point = __color_end + '+' + __color_disabled
separator = __color_fail + ':' + __color_disabled


class __Worm:
    def __init__(self) -> None:
        self.body = [{'x': 7, 'y': 6}, {'x': 7, 'y': 5}]
        self.direction = 'up'
    
    def move(self):
        try:
            if self.direction == 'up':
                self.body[0]['y'] += 1
            elif self.direction == 'down':
                self.body[0]['y'] -= 1
            elif self.direction == 'left':
                self.body[0]['x'] -= 1
            elif self.direction == 'right':
                self.body[0]['x'] += 1

            self.body.insert(1, {'x': self.body[0]['x'], 'y': self.body[0]['y']})
            self.body.pop()
        
        except Exception:
            pass
    
    def change_direction(self, direction):
        direction_opposite = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }
        if self.direction != direction_opposite[direction]:
            self.direction == direction
    
    def collides_with_body(self):
        for body in range(1, len(self.body)):
            if (self.body[0]['x'] == self.body[body]['x']
                    and self.body[0]['y'] == self.body[body]['y']):
                return True
        return False


def __render_menu():
    update_score()
    print('\n'.join(
        [
            __texture_text_line,
            __texture_text_wormer_ver,
            __texture_text_line,
            __texture_text_score,
            __texture_text_line,
            __texture_choice
        ]))


def main_menu():
    __render_menu()


main_menu()
input()