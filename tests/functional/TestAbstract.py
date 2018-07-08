import unittest
import yaml


from DependencyInjection.DependencyInjectionContainer import DependencyInjectionContainer
from DependencyInjection.Handlers.ConfigHandler.ConfigHandler import ConfigHandler
from DependencyInjection.Handlers.ServiceHandler.ServiceHandler import ServiceHandler

class TestAbstract(unittest.TestCase):
    app = None

    def setUp(self):
        self.app = DependencyInjectionContainer()
        config_handler = ConfigHandler()
        services_handler = ServiceHandler()
        self.app.register_yaml_handler(config_handler, 'config')
        self.app.register_yaml_handler(services_handler, 'services')

    def setDown(self):
        self.app = None

    def recompile_all(self):
        self.app.compile_all_handlers()

    def add_file(self, file_name):
        file_content = self.load_yaml_file("tests/functional/app_test/config/" + file_name)
        self.app.add_file_content(file_content)

    def load_yaml_file(self, filename):
        with open(filename) as input:
            content = yaml.load(input.read())
        return content
