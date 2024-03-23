import os

import vars
import defs
import files_interaction as f

__main_path = os.getcwd()
__textures_path = os.path.join(__main_path, 'textures')


__texture_text_line = ' + — — — — — — — — — — — — — — — — +'

__worm_head_up = vars.Color.default + '^' + vars.Color.disabled
__worm_head_down = vars.Color.default + 'v' + vars.Color.disabled
__worm_head_left = vars.Color.default + '<' + vars.Color.disabled
__worm_head_right = vars.Color.default + '>' + vars.Color.disabled
__worm_tail = vars.Color.default + 'o' + vars.Color.disabled

__point_plus = vars.Color.gold + '+' + vars.Color.disabled
__point_separator = vars.Color.red + ':' + vars.Color.disabled


def __clear():
    os.system('cls')


def __text_in_line(text, align='center'):
    def_space_amount = 17
    space = ' '
    half_text_len = len(text) // 2
    
    match align:
        case 'center':
            space_amount1 = def_space_amount - half_text_len - 1
            space_amount2 = space_amount1
            if len(text) % 2 == 0:
                space_amount2 += 1
        
        case 'left':
            space_amount1 = 8
            space_amount2 = 2*(def_space_amount - half_text_len) - space_amount1 - 1
            if len(text) % 2 != 0:
                space_amount2 -= 1
        
    complete_line1 = space * space_amount1
    complete_line2 = space * space_amount2
    
    return f' |{complete_line1 + text + complete_line2}|'


def __printlines(lines: list):
    print('\n'.join(lines))


def __printfile(filename: str):
    texture_file_path = os.path.join(__textures_path, f'{filename}.txt')
    texture_file_content = f.get(texture_file_path)
    print(texture_file_content)


def menu():
    texture_text_wormer_ver = __text_in_line('Wormer - 0.4')
    texture_text_score = __text_in_line(f'Best score: {defs.get_best_score()}')
    
    __clear()
    __printlines([
            __texture_text_line,
            texture_text_wormer_ver,
            __texture_text_line,
            texture_text_score,
            __texture_text_line,
        ])
    __printfile('menu_controls')


def back_to_menu_text():
    __printfile('back_to_menu_text')


def controls():
    all_controls = defs.get_controls()
    all_controls_text = ['up', 'left', 'down', 'right']
    
    text_list = []
    for i in range(len(all_controls)):
        text_list.append(
            __text_in_line(f'{all_controls[i]} - {all_controls_text[i]}', align='left'))
    text_list.insert(0, __texture_text_line)
    text_list.append(__texture_text_line)
    
    __clear()
    __printfile('controls_title')
    __printlines(text_list)
    __printfile('back_to_menu_control')


def score_reset_question():
    __clear()
    __printfile('score_reset_question')


def score_reset_complete():
    __printfile('score_reset_complete')


def placeholder():
    __printfile('placeholder')
