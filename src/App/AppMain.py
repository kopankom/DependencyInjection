import hashlib
import os
import random


class AppMain():
    json_objects = None
    file_checker = None
    objects_filter = None

    def __init__(self, json_objects, file_checker, objects_filter):
        self.json_objects = json_objects.json_objects
        self.file_checker = file_checker
        self.objects_filter = objects_filter

    def check(self):
        for i in self.json_objects:
            self.file_checker.check_file(i['pictureUrl'])

    def get_object_by_image(self, picture_url):
        return self.objects_filter.filter_by_image(picture_url)

    def make_thumbnail(self, video_url, output_filename):
        command = 'ffmpeg -i {} -ss 00:00:00.5 -vframes 1 {}'.format(video_url, output_filename)
        os.system(command)

    def download_video(self, video_url):
        name_out = hashlib.md5(str(random.getrandbits(256)).encode('utf-8')).hexdigest()
        video_name_out = '/tmp/' + name_out + '.mp4'
        picture_name_out = '/tmp/' + name_out + '.png'
        command = 'wget "{}" -O "{}"'.format(video_url, video_name_out)
        os.system(command)
        self.make_thumbnail(video_name_out, picture_name_out)


