import yaml

from DependencyInjection.ClassExecutor import ClassExecutor
from DependencyInjection.FileResolver import FileResolver
from DependencyInjection.Parser.ConfigParser import ConfigParser

def load_yaml_file(filename):
    f = open(filename, "r")
    return yaml.load(f.read())

if __name__ == '__main__':
    # TEST ONLY REMOVE THIS
    module_path = 'src.App.Handler.ParamHandler'
    pName = 'param'
    pValue = ' John '
    params = {pName : pValue}
    class_loader = ClassExecutor()
    class_loader.set_module_path(module_path)
    class_loader.create_class_instance({'constructor_parameters' : 'changed argument constructoe'})
    class_loader.execute_function('handle', params)
    class_loader.execute_function('no_param')
    # END OF TEST


    loadedFile = load_yaml_file("app/config/config.yml")
    config_parser = ConfigParser(loadedFile)
    processedFile = config_parser.get_config_by_yaml_object()

    print(config_parser.get_value_from_config('db.mongo.host'))


    modulesYaml = load_yaml_file("app/config/modules.yml")
    modulesList = modulesYaml['modules']

    module_path = 'AppBundle.Handler.ParamHandler'
    file_resolver = FileResolver()
    file_resolver.replace_prefix_list = modulesList
    print(file_resolver.build_class_path(module_path))

    services_yaml_file = load_yaml_file('app/config/services.yml')


    # print(yaml.dump())


    # print(yaml.dump(processedFile))
