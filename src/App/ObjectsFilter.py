class ObjectsFilter():
    json_objects = None

    def __init__(self, json_objects):
        self.json_objects = json_objects.json_objects

    def filter_by_image(self, picture_url):
        for object in self.json_objects:
            if picture_url == object['pictureUrl']:
                return object

        return None
