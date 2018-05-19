import yaml

from DependencyInjection.ClassExecutor import ClassExecutor
from DependencyInjection.FileResolver import FileResolver
from DependencyInjection.Parser.ConfigParser import ConfigParser
from DependencyInjection.Parser.ModuleParser import ModuleParser
from DependencyInjection.Parser.ServiceParser import ServiceParser


def load_yaml_file(filename):
    f = open(filename, "r")
    return yaml.load(f.read())

if __name__ == '__main__':
    # TEST ONLY REMOVE THIS
    # module_path = 'src.App.Handler.ParamHandler'
    # pName = 'param'
    # pValue = ' John '
    # params = {pName : pValue}
    # class_loader = ClassExecutor()
    # class_loader.set_module_path(module_path)
    # class_loader.create_class_instance({'constructor_parameters' : 'changed argument constructoe'})
    # class_loader.execute_function('handle', params)
    # class_loader.execute_function('no_param')
    # END OF TEST


    loadedFile = load_yaml_file("app/config/config.yml")
    config_parser = ConfigParser(loadedFile)
    # processedFile = config_parser.get_parameters()



    modulesYaml = load_yaml_file("app/config/modules.yml")
    modulesList = modulesYaml['modules']

    module_path = 'AppBundle.Handler.ParamHandler'
    file_resolver = FileResolver()
    file_resolver.replace_prefix_list = modulesList

    services_yaml_file = load_yaml_file('app/config/services.yml')

    service_parser = ServiceParser(services_yaml_file['services'], file_resolver, config_parser)
    service_parser.iterate_through_file()
    service_parser.container.get('aws').container_execution()
