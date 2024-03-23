import os


__main_path = os.getcwd()


class Color:
    disabled = '\033[1;30m'
    header = '\033[95m'
    bold = '\033[1m'
    underline = '\033[4m'
    gold = '\033[93m'
    red = '\033[91m'
    default = '\033[0m'


files_data_best_score = os.path.join(__main_path, 'data', 'best_score.txt')
files_data_controls = os.path.join(__main_path, 'data', 'controls.txt')
