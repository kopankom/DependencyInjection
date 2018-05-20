from DependencyInjection.DependencyInjection import DependencyInjection

if __name__ == '__main__':
    dependency_injection = DependencyInjection()
    # dependency_injection.container.get('app_main').check()
    object = dependency_injection.container.get('app_main').get_object_by_image('http://vidiimedia-dev.s3.amazonaws.com/whatson/picture/476c37229cd95c9d637ee19fedffe572-thumbnail.jpg')
    # object = dependency_injection.container.get('app_main').get_object_by_image('NULL')
    dependency_injection.container.get('app_main').download_video(object['videoUrl'])
    print(object['videoUrl'])
    print('finished')
