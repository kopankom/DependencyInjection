class AppMain():
    json_objects = None
    objects_filter = None

    def __init__(self, json_objects, objects_filter):
        self.json_objects = json_objects.json_objects
        self.objects_filter = objects_filter

    def check(self):
        emails = set()
        for i in self.json_objects:
            emails.add(i['email'])
        file = open('emails.csv', 'w')


        for i in emails:
            print(i)
            file.write(i + "\n")
        file.close()
