import re

from DependencyInjection.Handlers.HandlerAbstract import HandlerAbstract
from DependencyInjection.Handlers.ServiceHandler.ClassExecutor import ClassExecutor
from DependencyInjection.ParameterBag import ParameterBag


class ServiceHandler(HandlerAbstract):
    match_regex = '^@([0-9a-zA-Z\.\_\-]+)$'
    yaml_entry_point = 'services'
    replace_pattern = '@{0}'
    data = ParameterBag()

    def get_parameter(self, key):
        return self.data.get(key)

    def bind_value(self, value):
        service_name = re.findall(self.match_regex, value)
        if len(service_name) != 1:
            raise KeyError('Service not found!', service_name)
        service_name = service_name[0]
        if not self.data.has(service_name):
            raise KeyError('Service not found!', service_name)
        return self.data.get(service_name)

    def compile(self):
        self.parse_services(self.raw_data)

    def parse_services(self, item=None):
        for config_key in item:
            current_object = item[config_key]
            class_loader = ClassExecutor()
            item[config_key] = self.get_value_binded_item(item[config_key])
            class_loader.set_module_path(current_object['class'])
            if 'arguments' in current_object:
                arguments = current_object['arguments']
                class_loader.create_class_instance(arguments)
            else:
                class_loader.create_class_instance()

            if 'calls' in current_object:
                for method in current_object['calls']:
                    arguments = current_object['calls'][method]
                    class_loader.execute_function(method, arguments)

            self.data.add(config_key, class_loader.class_instance)
