import os

import vars
import defs
import files_interaction as f


__main_path = os.getcwd()
__textures_path = os.path.join(__main_path, 'textures')


__texture_line = ' + — — — — — — — — — — — — — — — +'


def __printlines(*lines, start: str = ''):
    print(start + '\n'.join(lines))


def __printfile(filename: str):
    texture_file_path = os.path.join(__textures_path, f'{filename}.txt')
    texture_file_content = f.get(texture_file_path)
    print(texture_file_content)


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


def __beautiful_control_icons(controls):
    controls_icons = {
        'up': '^', 
        'left': '<', 
        'down': '>', 
        'right': 'v'}
    for i in range(len(controls)):
        if controls[i] in controls_icons:
            controls[i] = controls_icons[controls[i]]
    return controls


def __rendered_options(options, selected_option):
    options = [option['name'] for option in options]
    options[selected_option] = f'>> {options[selected_option]} <<'
    rendered_options = list()
    rendered_options.append(__texture_line)
    for option in options:
        rendered_options.append(__text_in_line(option))
    rendered_options.append(__texture_line)
    return rendered_options


def clear():
    os.system('cls')


def update():
    print("\033[0;0H", end='')


def render(func, **kwargs):
    try:
        if kwargs:
            func(**kwargs)
        else:
            func()
    except FileNotFoundError:
        placeholder()


def input_error():
    clear()
    __printfile('input_error')


def placeholder():
    __printfile('placeholder')


def menu(**kwargs):
    texture_text_wormer_ver = __text_in_line('Wormer - 0.5')
    texture_text_score = __text_in_line(f'Best score: {defs.Get.best_score()}')

    options = kwargs['options']
    selected_option = kwargs['selected_option']

    menu_options = __rendered_options(options, selected_option)
    
    update()
    __printlines(
            __texture_line,
            texture_text_wormer_ver,
            __texture_line,
            texture_text_score,
            __texture_line,
        )
    __printlines(*menu_options)


def back_to_menu_text():
    __printfile('back_to_menu_text')


def game_map(**kwargs):
    score = kwargs['score']
    worm = kwargs['worm']
    plus = kwargs['plus']
    separator = kwargs['separator']

    texture_border = ' | '

    texture_worm_head = {
        'up': vars.Color.default + '^' + vars.Color.disabled,
        'down': vars.Color.default + 'v' + vars.Color.disabled,
        'left': vars.Color.default + '<' + vars.Color.disabled,
        'right': vars.Color.default + '>' + vars.Color.disabled
        }
    texture_worm_tail = vars.Color.default + 'o' + vars.Color.disabled

    texture_plus = vars.Color.gold + '+' + vars.Color.disabled
    texture_separator = vars.Color.red + ':' + vars.Color.disabled
    
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
            field[bodypart.y][bodypart.x] = texture_worm_head[worm.direction]
        else:
            field[bodypart.y][bodypart.x] = texture_worm_tail

    if plus.exists:
        field[plus.y][plus.x] = texture_plus
    if separator.exists:
        field[separator.y][separator.x] = texture_separator

    # render map
    map_lines = list()
    map_lines.append(vars.Color.disabled)
    map_lines.append(__texture_line)
    for y in field:
        map_lines.append(texture_border + (' '.join(x for x in field[y])) + texture_border)
    map_lines.append(__texture_line)
    map_lines.append(vars.Color.default)
    
    update()
    __printlines(*score_lines, start='\n')
    __printlines(*map_lines)
    __printfile('back_to_menu_control')


def you_lose():
    clear()
    __printfile('you_lose')


def settings(**kwargs):
    options = kwargs['options']
    selected_option = kwargs['selected_option']

    settings_options = __rendered_options(options, selected_option)

    update()
    __printfile('settings_title')
    __printlines(*settings_options)


def level_select():
    update()
    __printfile('level_select_title')
    __printlines(
        __texture_line,
        __text_in_line(f'Current level: {defs.Get.current_level()}'),
        __texture_line
    )
    __printfile('back_to_menu_control')


def controls():
    all_controls = defs.Get.controls().in_list
    all_controls_text = ['up', 'left', 'down', 'right']
    
    all_controls = __beautiful_control_icons(all_controls)
    
    text_list = []
    for i in range(len(all_controls)):
        text_list.append(
            __text_in_line(f'{all_controls[i]} - {all_controls_text[i]}', align='left'))
    text_list.insert(0, __texture_line)
    text_list.append(__texture_line)
    
    clear()
    __printfile('controls_title')
    __printlines(*text_list)
    __printfile('back_to_menu_control')


def control_edit(**kwargs):
    controls = defs.Get.controls().in_dict
    selected_control = kwargs['selected_control']
    
    clear()
    __printfile('controls_edit_title')
    __printlines(
        __texture_line,
        __text_in_line(f'{controls[selected_control]} - {selected_control}'),
        __texture_line
    )
    __printfile('controls_edit_wait_input')


def score_reset_question():
    clear()
    __printfile('score_reset_question')


def score_reset_complete():
    __printfile('score_reset_complete')
