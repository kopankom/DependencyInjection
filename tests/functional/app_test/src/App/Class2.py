class Class2():
    class1 = None
    init_param = "You should not see this"

    def __init__(self, class1):
        self.class1 = class1

    def set_init_param(self, init_param):
        self.init_param = init_param

    def some_function(self):
        return self.init_param + ' ' + self.class1.init_param
