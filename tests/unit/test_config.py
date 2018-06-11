import os
import unittest

import yaml
from DependencyInjection.ApplicationContainer import ApplicationContainer
from DependencyInjection.Handlers.ConfigHandler.ConfigHandler import ConfigHandler
from DependencyInjection.Handlers.ServiceHandler.ServiceHandler import ServiceHandler


class AppTest(unittest.TestCase):
    app = None

    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        loadedFile = self.load_yaml_file(dir_path + "/app_test/config/config_1.yml")
        loadedFile1 = self.load_yaml_file(dir_path + "/app_test/config/config_2.yml")
        loadedFileServices = self.load_yaml_file("tests/unit/app_test/config/services.yml")
        self.app = ApplicationContainer()
        config_handler = ConfigHandler()
        services_handler = ServiceHandler()
        self.app.register_yaml_handler(config_handler)
        self.app.register_yaml_handler(services_handler)
        self.app.add_file_content(loadedFile)
        self.app.add_file_content(loadedFile1)
        self.app.add_file_content(loadedFileServices)

    def test(self):
        print(self.app.get('services').get_parameter('json_objects').test())

        print(self.app.get('parameters').get_parameter('param6.sub1.test.t1'))
        print(self.app.get('parameters').get_parameter('param6.sub0.a1'))
        print(self.app.get('parameters').get_parameter('param3.0'))
        print(self.app.get('parameters').get_parameter('param3.1'))
        print(self.app.get('parameters').get_parameter('param2'))
        self.assertFalse(False)

    def load_yaml_file(self, filename):
        with open(filename) as input:
            content = yaml.load(input.read())
        return content

if __name__ == '__main__':
    unittest.main()
