import json


class JsonFile():
    json_objects = []

    def __init__(self, file_name):
        print(file_name)
        json_file = self.load_json_file(file_name)
        json_file = json_file.split("\n")
        for i in json_file:
            try:
                self.json_objects.append(json.loads(i))
            except:
                print('error')

    def load_json_file(self, filename):
        f = open(filename, "r")
        return f.read()

