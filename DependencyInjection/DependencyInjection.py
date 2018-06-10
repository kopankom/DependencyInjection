import yaml

from DependencyInjection.Container.ApplicationContainer import ApplicationContainer
from DependencyInjection.Container.ConfigContainer import ConfigContainer
from DependencyInjection.Container.ServiceHandler import ServiceHandler


class DependencyInjection():

    def __init__(self):
        loadedFile = self.load_yaml_file("app/config/config.yml")
        loadedFile1 = self.load_yaml_file("app/config/config1.yml")
        loadedFileServices = self.load_yaml_file("app/config/services.yml")
        app = ApplicationContainer()
        config_handler = ConfigContainer()
        services_handler = ServiceHandler()
        app.register_yaml_handler(config_handler)
        app.register_yaml_handler(services_handler)
        app.add_file_content(loadedFile)
        app.add_file_content(loadedFile1)
        app.add_file_content(loadedFileServices)



        print(app.get('services').get_parameter('json_objects').test())

        print(app.get('parameters').get_parameter('param6.sub1.test.t1'))
        print(app.get('parameters').get_parameter('param6.sub0.a1'))
        print(app.get('parameters').get_parameter('param3.0'))
        print(app.get('parameters').get_parameter('param3.1'))
        print(app.get('parameters').get_parameter('param2'))


    def load_yaml_file(self, filename):
        with open(filename) as input:
            content = yaml.load(input.read())
        return content
