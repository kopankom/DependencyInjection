import yaml

from DependencyInjection.FileResolver import FileResolver
from DependencyInjection.Parser.ConfigParser import ConfigParser
from DependencyInjection.Parser.ServiceParser import ServiceParser


class DependencyInjection():

    def __init__(self):
        loadedFile = self.load_yaml_file("app/config/config.yml")
        config_parser = ConfigParser(loadedFile)

        modulesYaml = self.load_yaml_file("app/config/modules.yml")
        modulesList = modulesYaml['modules']

        file_resolver = FileResolver()
        file_resolver.replace_prefix_list = modulesList

        services_yaml_file = self.load_yaml_file('app/config/services.yml')

        service_parser = ServiceParser(services_yaml_file['services'], file_resolver, config_parser)
        service_parser.iterate_through_file()
        service_parser.container.get('aws').container_execution()

    def load_yaml_file(self, filename):
        f = open(filename, "r")
        return yaml.load(f.read())

    def load_modules_definitions(self):
        pass

    def load_config(self):
        pass

    def load_services(self):
        pass

    def get_container(self):
        pass
