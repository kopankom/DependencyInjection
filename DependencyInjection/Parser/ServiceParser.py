from DependencyInjection.ClassExecutor import ClassExecutor
from DependencyInjection.ParameterBag import ParameterBag
from DependencyInjection.Parser.YamlParser import YamlParser


class ServiceParser(YamlParser):
    container = ParameterBag()
    file_resolver = None
    config = None

    def __init__(self, yaml_object, file_resolver, config):
        self.file_resolver = file_resolver
        self.config = config
        super(ServiceParser, self).__init__(yaml_object)

    def get_container(self):
        pass

    def bind_values(self, object):
        for key in object:
            if object[key].startswith('@'):
                service_name = object[key].replace('@', '')
                if self.container.has(service_name):
                    object[key] = self.container.get(service_name)
                    print('mam w kontenerze servis', service_name)
                print("starts with", object[key])
            else:
                object[key] = self.config._prepare_value(object[key])
        return object

    def iterate_through_file(self):
        for config_key in self.original_config_object:
            current_object = self.original_config_object[config_key]
            class_loader = ClassExecutor()
            class_loader.set_module_path(self.file_resolver.build_class_path(current_object['class']))
            if 'arguments' in current_object:
                arguments = current_object['arguments']
                arguments = self.bind_values(arguments)
                class_loader.create_class_instance(arguments)
            else:
                class_loader.create_class_instance()

            if 'calls' in current_object:
                for method in current_object['calls']:
                    arguments = self.bind_values(current_object['calls'][method])
                    class_loader.execute_function(method, arguments)

            self.container.add(config_key, class_loader.class_instance)
