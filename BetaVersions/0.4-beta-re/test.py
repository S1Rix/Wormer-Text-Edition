def text_in_line(text):
    space = 34 * ' '
    paste_line = ' |{}|'
    half_text_len = len(text) // 2
    half_line_len = len(space) // 2
    if half_text_len % 2 == 0:
        paste_line.format(space[:half_line_len - half_text_len] + text + space[half_line_len - half_text_len:])
    else:
        paste_line.format(space[:(half_line_len - 1) - half_text_len] + text + space[half_line_len - half_text_len:])
    return paste_line