class ParamHandler():
    class_argument = 'original'

    def __init__(self, constructor_parameters):
        self.class_argument = 'changed'

    def handle(self, param):
        print("Handler !", param)
        print("Class argument !", self.class_argument)

    def no_param(self):
        print('No param delivered')
