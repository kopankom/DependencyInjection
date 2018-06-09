import yaml

from DependencyInjection.FileResolver import FileResolver
from DependencyInjection.Parser.ConfigParser import ConfigParser
from DependencyInjection.Parser.ServiceParser import ServiceParser


class DependencyInjection():
    service_parser = None
    config_parser = None
    container = None

    def __init__(self):
        loadedFile = self.load_yaml_file("app/config/config.yml")
        self.config_parser = ConfigParser(loadedFile)

        modulesYaml = self.load_yaml_file("app/config/modules.yml")
        modulesList = modulesYaml['modules']

        file_resolver = FileResolver()
        file_resolver.replace_prefix_list = modulesList

        services_yaml_file = self.load_yaml_file('app/config/services.yml')

        self.service_parser = ServiceParser(services_yaml_file['services'], file_resolver, self.config_parser)
        self.service_parser.iterate_through_file()

        self.container = self.service_parser.container

    def load_yaml_file(self, filename):
        with open(filename) as input:
            content = yaml.load(input.read())
        return content
