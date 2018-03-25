import importlib


class ClassLoader():
    class_indicator = None
    class_instance = None
    def set_module_path(self, module_name):
        module = importlib.import_module(module_name)
        class_name = module_name.split('.')[-1]
        self.class_indicator = getattr(module, class_name)

    def create_class_instance(self, constructor_parameters=None):
        if None != constructor_parameters:
            self.class_instance = self.class_indicator(**constructor_parameters)
        else:
            self.class_instance = self.class_indicator()

    def execute_function(self, function_name, arguments=None):
        if None != arguments:
            return getattr(self.class_instance, function_name)(**arguments)
        else:
            return getattr(self.class_instance, function_name)()

