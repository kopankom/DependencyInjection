import re


class ConfigParser():
    VARIABLE_CHARACTER = '%'
    VARIABLE_FORMAT = VARIABLE_CHARACTER + '{}' + VARIABLE_CHARACTER
    VARIABLE_REGEX = VARIABLE_CHARACTER + '([a-zA-Z0-9\.\_]+)' + VARIABLE_CHARACTER
    original_config_object = None

    def _prepare_value(self, value):
        if (self._has_variable(value)):
            varArray = re.findall(self.VARIABLE_REGEX, value)
            for i in varArray:
                value = value.replace(self.VARIABLE_FORMAT.format(i), self.get_value_from_config(i))
        return value

    def _has_variable(self, string):
        return -1 != string.find(self.VARIABLE_CHARACTER)

    def _is_object(self, object):
        return isinstance(object, list) or isinstance(object, dict)

    def _obtain_object_indicator(self, indicator1, indicator2, object):
        try:
            object[indicator1]
            return indicator1
        except:
            return indicator2

    def get_value_from_config(self, key, configArray=None):
        if None == configArray:
            return self.get_value_from_config(key, self.original_config_object)
        if -1 == key.find('.'):
            return configArray[key]

        splittedValue = key.split('.')
        newConfigArray = configArray[splittedValue[0]]
        del splittedValue[0]
        newKey = '.'.join(splittedValue)
        return self.get_value_from_config(newKey, newConfigArray)

    def set_yaml_object(self, yaml_object):
        self.original_config_object = yaml_object

    def get_config_by_yaml_object(self, yaml_object=None):
        if None == yaml_object:
            yaml_object = self.original_config_object
        if self._is_object(yaml_object):
            iterator = 0
            for i in yaml_object:
                objectIndicator = self._obtain_object_indicator(iterator, i, yaml_object)
                value = yaml_object[objectIndicator]
                iterator += 1
                if isinstance(value, str):
                    yaml_object[objectIndicator] = self._prepare_value(value)
                else:
                    yaml_object[objectIndicator] = self.get_config_by_yaml_object(value)
        return yaml_object
