import re


class HandlerAbstract():
    match_regex = '^@([0-9a-zA-Z\.\_\-]+)$'
    replace_pattern = '@{0}'
    yaml_entry_point = 'services'
    application_container = None
    data = {}

    def can_i_handle_this(self, value):
        if not isinstance(value, str):
            return False
        return re.search(self.match_regex, value) is not None

    def add_content_data(self, data):
        self.data = {**self.data, **data}
        self.data = self.get_value_binded_item(self.data)

    def get_parameter(self, key):
        code_to_eval = "self.data['" + key.replace(".", "']['") + "']"
        code_to_eval = re.sub(r"\'([0-9]+)\'", r'\1', code_to_eval)
        return eval(code_to_eval)

    def bind_value(self, value):
        keys_for_bind = re.findall(self.match_regex, value)
        for key in keys_for_bind:
            parameter = self.get_parameter(key)
            if not isinstance(parameter, str):
                return parameter
            key = self.replace_pattern.format(key)
            value = value.replace(key, parameter)
        return value

    def get_value_binded_item(self, item=None):
        if isinstance(item, list) or isinstance(item, dict):
            iterator = 0
            for item_key in item:
                object_indicatator = iterator if isinstance(item, list) else item_key
                value = item[object_indicatator]
                iterator += 1
                if isinstance(value, str):
                    item[object_indicatator] = self.application_container.bind_value(value)
                else:
                    item[object_indicatator] = self.get_value_binded_item(value)
        else:
            if isinstance(item, str):
                item = self.application_container.bind_value(item)
        return item
