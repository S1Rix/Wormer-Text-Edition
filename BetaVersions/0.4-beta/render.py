import os

import vars
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


def __text_in_line(text):
    def_space_amount = 17
    space = ' '
    half_text_len = len(text) // 2
    
    space_amount1 = (def_space_amount - 1) - half_text_len
    complete_line1 = space * space_amount1
    
    if len(text) % 2 == 0:
        space_amount2 = def_space_amount - half_text_len
    else:
        space_amount2 = def_space_amount - (half_text_len + 1)
    complete_line2 = space * space_amount2
    
    return f' |{complete_line1 + text + complete_line2}|'


def printlines(lines: list):
    print('\n'.join(lines))


def menu():
    files_textures_menu_choice = os.path.join(__textures_path, 'menu.txt')
    
    texture_text_wormer_ver = __text_in_line('Wormer - 0.4')
    texture_text_score = __text_in_line(f'Best score: {f.get(vars.files_data_best_score)}')
    texture_choice = f.get(files_textures_menu_choice)
    
    __clear()
    printlines([
            __texture_text_line,
            texture_text_wormer_ver,
            __texture_text_line,
            texture_text_score,
            __texture_text_line,
            texture_choice
        ])


def reset_score_question():
    files_textures_reset_score = os.path.join(__textures_path, 'reset_score.txt')
    texture_reset_score = f.get(files_textures_reset_score)
    print(texture_reset_score)


def placeholder():
    files_textures_placeholder = os.path.join(__textures_path, 'placeholder.txt')
    texture_placeholder = f.get(files_textures_placeholder)
    print(texture_placeholder)
