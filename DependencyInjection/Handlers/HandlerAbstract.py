import re


class HandlerAbstract():
    match_regex = '^@([0-9a-zA-Z\.\_\-]+)$'
    replace_pattern = '@{0}'
    yaml_entry_point = 'services'
    application_container = None
    data = {}
    raw_data = {}

    def can_i_handle_this(self, value):
        if not isinstance(value, str):
            return False
        return re.search(self.match_regex, value) is not None

    def add_content_data(self, data):
        self.raw_data = {**self.raw_data, **data}

    def compile(self):
        self.data = self.raw_data
        self.data = self.get_value_binded_item(self.data)

    def get_parameter(self, key):
        code_to_eval = "self.data['" + key.replace(".", "']['") + "']"
        code_to_eval = re.sub(r"\'([0-9]+)\'", r'\1', code_to_eval)
        try:
            return eval(code_to_eval)
        except:
            raise KeyError('Parameter not found ', key)

    def bind_value(self, value):
        keys_for_bind = re.findall(self.match_regex, value)
        for key in keys_for_bind:
            parameter = self.get_parameter(key)
            if not isinstance(parameter, str):
                return parameter
            key_for_replace = self.replace_pattern.format(key)
            value = value.replace(key_for_replace, parameter)
        return value

    def get_value_binded_item(self, object):
        if isinstance(object, dict):
            return dict(map(self.get_value_binded_item, object.items()))
        if isinstance(object, list) or isinstance(object, tuple):
            return list(map(self.get_value_binded_item, object))
        if isinstance(object, str) or isinstance(object, int):
            object = self.application_container.bind_value(object)
            if not isinstance(object, str):
                return self.get_value_binded_item(object)
            return object
