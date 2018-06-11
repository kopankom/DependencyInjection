from DependencyInjection.DependencyInjection import DependencyInjection

if __name__ == '__main__':
    dependency_injection = DependencyInjection()
    # dependency_injection.container.get('app_main').check()
    object = dependency_injection.container.get('app_main').check()
