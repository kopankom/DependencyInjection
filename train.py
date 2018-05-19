
class ParameterBag():
    container = {}

    def __init__(self, container = {}):
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

class ConfigBag(ParameterBag):
    pass

cb = ConfigBag()
cb.add('a', '1')
if cb.has('a'):
    cb.set('a', '2')
print(cb.get('a'))


class SC():
    value = 1

class SC1():
    sc = None
    def __init__(self, sc):
        self.sc = sc
        self.sc.value = 190

    def prnt(self):
        print(self.sc.value)

sc = SC()
sc1 = SC1(sc)
# sc.value = 290
sc1.prnt()
print(sc.value)

