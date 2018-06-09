from DependencyInjection.DependencyInjection import DependencyInjection

if __name__ == '__main__':
    dependency_injection = DependencyInjection()
    object = dependency_injection.container.get('app_main').get_object_by_image('http://vidiimedia-dev.s3.amazonaws.com/whatson/picture/8adf0084ea6c46e19a15a1454bc8c78d-thumbnail.jpg')
    new_picture_url = dependency_injection.container.get('app_main').download_video(object['videoUrl'])
