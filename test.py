class Function:
    l = []
    
    @staticmethod
    def set(func):
        Function.init = func


def test():
    def hi():
        print('hello')
    
    Function.set(hi)
    do({'def': hi})

def do(func_dict):
    func_dict['def']()

test()
Function.init()