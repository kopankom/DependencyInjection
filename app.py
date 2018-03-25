import importlib
import yaml

from DependencyInjection.ClassLoader.ClassLoader import ClassLoader
from DependencyInjection.Parser.ConfigParser import ConfigParser

if __name__ == '__main__':
    module_path = 'src.AppBundle.Handler.ParamHandler'
    pName = 'param'
    pValue = ' John '
    params = {pName : pValue}
    class_loader = ClassLoader()
    class_loader.set_module_path(module_path)
    class_loader.create_class_instance({'constructor_parameters' : 'changed argument constructoe'})
    class_loader.execute_function('handle', params)
    class_loader.execute_function('no_param')

    f = open("app/config/config.yml", "r")  # opens file with name of "test.txt"
    loadedFile = yaml.load(f.read())
    config_parser = ConfigParser()
    config_parser.original_config_object = loadedFile
    config_parser.set_yaml_object(loadedFile)
    processedFile = config_parser.get_config_by_yaml_object()
    print(yaml.dump(processedFile))
    # print(yaml.dump(bindVariables.configDictionary))
