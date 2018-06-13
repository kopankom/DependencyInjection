class Class1():
    init_param = "Should not see this"
    def __init__(self, init_param):
        self.init_param = init_param

    def return_something(self):
        return 'Something'
