import re

class YamlParser():
    VARIABLE_CHARACTER = '%'
    VARIABLE_FORMAT = VARIABLE_CHARACTER + '{}' + VARIABLE_CHARACTER
    VARIABLE_REGEX = VARIABLE_CHARACTER + '([a-zA-Z0-9\.\_]+)' + VARIABLE_CHARACTER

    original_config_object = None

    def __init__(self, yaml_object):
        self.original_config_object = yaml_object

    def _prepare_value(self, value):
        if (self._has_variable(value)):
            varArray = re.findall(self.VARIABLE_REGEX, value)
            for i in varArray:
                if self.get_parameter(i):
                    value = value.replace(self.VARIABLE_FORMAT.format(i), str(self.get_parameter(i)))
        return value

    def _has_variable(self, string):
        return -1 != string.find(self.VARIABLE_CHARACTER)

    def _is_list_or_dict(self, object):
        return isinstance(object, list) or isinstance(object, dict)

    def _obtain_object_indicator(self, indicator1, indicator2, object):
        if indicator1 in object:
            return indicator1
        else:
            return indicator2

    def get_parameter(self, key):
        return eval("self.arr['" + key.replace(".", "']['") + "']")

    def get_value_binded_item(self, item=None):
        if self._is_list_or_dict(item):
            iterator = 0
            for i in item:
                object_indicatator = self._obtain_object_indicator(iterator, i, item)
                value = item[object_indicatator]
                iterator += 1
                if isinstance(value, str):
                    item[object_indicatator] = self._prepare_value(value)
                else:
                    item[object_indicatator] = self.get_value_binded_item(value)
        return item
