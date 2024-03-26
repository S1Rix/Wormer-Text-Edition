import traceback

from datetime import datetime

import vars
import files_interaction as f


def show_error():
    traceback.print_exc()


class Get:
    def best_score():
        return f.get(vars.files_data_best_score)

    def controls():
        class Container:
            def __init__(self, __controls_list):
                self.in_list = __controls_list
                self.in_dict = {
                    'up': __controls_list[0],
                    'left': __controls_list[1],
                    'down': __controls_list[2],
                    'right': __controls_list[3]
                }
        controls_list = f.get_list(vars.files_data_controls)
        return Container(controls_list)

    def current_level():
        return f.get(vars.files_data_current_level)


class Set:
    def best_score(arg: int):
        f.update(vars.files_data_best_score, arg)


def adapted_list(args):
    if type(args[0]) is list:
        return args[0]
    else:
        return args


def seconds_passed(__saved_time: datetime, __current_time: datetime):
    saved_seconds = float(f'{__saved_time.second}.{__saved_time.microsecond}')
    current_seconds = float(f'{__current_time.second}.{__current_time.microsecond}')
    if __current_time.minute > __saved_time.minute:
        current_seconds += 60
    elif __current_time.minute < __saved_time.minute:
        saved_seconds += 60
    __seconds_passed = round(current_seconds - saved_seconds, 3)
    return __seconds_passed
