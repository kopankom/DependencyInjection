import unittest
import yaml


from DependencyInjection.ApplicationContainer import ApplicationContainer
from DependencyInjection.Handlers.ConfigHandler.ConfigHandler import ConfigHandler
from DependencyInjection.Handlers.ServiceHandler.ServiceHandler import ServiceHandler

class TestAbstract(unittest.TestCase):
    app = None

    def setUp(self):
        self.app = ApplicationContainer()
        config_handler = ConfigHandler()
        services_handler = ServiceHandler()
        self.app.register_yaml_handler(config_handler)
        self.app.register_yaml_handler(services_handler)

    def add_file(self, file_name):
        file_content = self.load_yaml_file("tests/functional/app_test/config/" + file_name)
        self.app.add_file_content(file_content)

    def load_yaml_file(self, filename):
        with open(filename) as input:
            content = yaml.load(input.read())
        return content
