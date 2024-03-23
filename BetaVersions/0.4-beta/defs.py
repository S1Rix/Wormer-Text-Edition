import traceback

import vars
import files_interaction as f


def show_error():
    traceback.print_exc()


def get_best_score():
    return f.get(vars.files_data_best_score)


def get_controls():
    return f.get_list(vars.files_data_controls)
