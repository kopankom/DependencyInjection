class MongoDB():
    def __init__(self, db_host, db_name):
        print(db_host, db_name)

    def setKey(self, key):
        print("key from class ", key)

    def setPassword(self, password):
        print(password)

    def getSomething(self):
        return 'something'
