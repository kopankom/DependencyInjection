class ParameterBag():
    container = {}

    def __init__(self, container={}):
        self.container = container

    def has(self, key):
        return key in self.container

    def get(self, key):
        return self.container[key]

    def add(self, key, value):
        if key in self.container:
            raise Exception("Key '{0}' already exists!".format(key))
        self.container[key] = value

    def set(self, key, value):
        self.container[key] = value
