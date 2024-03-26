import os

import vars
import defs
import files_interaction as f


__main_path = os.getcwd()
__textures_path = os.path.join(__main_path, 'textures')


__texture_line = ' + — — — — — — — — — — — — — — — +'

__worm_head_texture = {
    'up': vars.Color.default + '^' + vars.Color.disabled,
    'down': vars.Color.default + 'v' + vars.Color.disabled,
    'left': vars.Color.default + '<' + vars.Color.disabled,
    'right': vars.Color.default + '>' + vars.Color.disabled
    }
__worm_tail = vars.Color.default + 'o' + vars.Color.disabled

__point_plus = vars.Color.gold + '+' + vars.Color.disabled
__point_separator = vars.Color.red + ':' + vars.Color.disabled


def __clear():
    os.system('cls')


def __text_in_line(text: str, space_amount: int = 16, align: str = 'center'):
    space = ' '
    half_text_len = len(text) // 2

    space_amount1 = space_amount
    space_amount2 = space_amount
    match align:
        case 'center':
            space_amount1 = space_amount - half_text_len - 1
            space_amount2 = space_amount1
            if len(text) % 2 == 0:
                space_amount2 += 1
        
        case 'left':
            space_amount1 = 8
            space_amount2 = 2*(space_amount - half_text_len) - space_amount1 - 1
            if len(text) % 2 != 0:
                space_amount2 -= 1
        
    complete_line1 = space * space_amount1
    complete_line2 = space * space_amount2
    
    return f' |{complete_line1 + text + complete_line2}|'


def __printlines(*lines):
    lines = defs.adapted_list(lines)
    print('\n'.join(lines))


def __printfile(filename: str):
    texture_file_path = os.path.join(__textures_path, f'{filename}.txt')
    texture_file_content = f.get(texture_file_path)
    print(texture_file_content)


def input_error():
    __clear()
    __printfile('input_error')


def menu():
    texture_text_wormer_ver = __text_in_line('Wormer - 0.4')
    texture_text_score = __text_in_line(f'Best score: {defs.get_best_score()}')
    
    __clear()
    __printlines(
            __texture_line,
            texture_text_wormer_ver,
            __texture_line,
            texture_text_score,
            __texture_line,
        )
    __printfile('menu_controls')


def back_to_menu_text():
    __printfile('back_to_menu_text')


def game_map(score: int, worm, point_plus, point_separator):
    texture_border = ' | '
    
    score_lines = [
        __texture_line,
        __text_in_line(f'Score: {score}', space_amount=16),
        __texture_line
    ]
    
    # generate cords for worm
    field = {}
    y_count = [14 - x for x in range(15)]
    for y in y_count:
        field[y] = list(15 * ' ')
    
    # place worm on cords
    for bodypart in worm.body:
        if bodypart.is_head:
            field[bodypart.y][bodypart.x] = __worm_head_texture[worm.direction]
        else:
            field[bodypart.y][bodypart.x] = __worm_tail

    if point_plus.exists:
        field[point_plus.y][point_plus.x] = __point_plus
    if point_separator.exists:
        field[point_separator.y][point_separator.x] = __point_separator

    # render map
    map_lines = list()
    map_lines.append(vars.Color.disabled)
    map_lines.append(__texture_line)
    for y in field:
        map_lines.append(texture_border + (' '.join(x for x in field[y])) + texture_border)
    map_lines.append(__texture_line)
    map_lines.append(vars.Color.default)
    
    __clear()
    __printlines(score_lines)
    __printlines(map_lines)
    __printfile('back_to_menu_control')


def you_lose():
    __clear()
    __printfile('you_lose')


def level_select():
    levels = list(range(1, 5))
    level_options_lines = list()
    level_options_lines.append(__texture_line)
    for level in levels:
        level_options_lines.append(__text_in_line(f'{level} - level {level}', align='left'))
    level_options_lines.append(__texture_line)
    
    __clear()
    __printfile('level_select_title')
    __printlines(
        __texture_line,
        __text_in_line(f'Current level: {defs.get_current_level()}'),
        __texture_line
    )
    __printlines(level_options_lines)
    __printfile('back_to_menu_control')


def controls():
    all_controls = defs.get_controls().in_list
    all_controls_text = ['up', 'left', 'down', 'right']
    
    text_list = []
    for i in range(len(all_controls)):
        text_list.append(
            __text_in_line(f'{all_controls[i]} - {all_controls_text[i]}', align='left'))
    text_list.insert(0, __texture_line)
    text_list.append(__texture_line)
    
    __clear()
    __printfile('controls_title')
    __printlines(text_list)
    __printfile('back_to_menu_control')


def score_reset_question():
    __clear()
    __printfile('score_reset_question')


def score_reset_complete():
    __printfile('score_reset_complete')


def __placeholder():
    __printfile('placeholder')
