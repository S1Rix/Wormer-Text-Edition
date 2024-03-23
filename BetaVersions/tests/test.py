from time import sleep as s
import msvcrt as m


def keyinput():
    def ask():
        if m.kbhit():
            def decode(what):
                try:
                    return what.decode()
                except UnicodeDecodeError:
                    return
            return decode(m.getch())
        return
    s(1)
    print(ask())
    keyinput()
keyinput()
