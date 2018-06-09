import re


class ContainerAbstract():
    match_regex = '^@([0-9a-zA-Z\.\_\-]+)$'
    yaml_entry_point = 'services'
    application_container = None
    data = []

    def can_i_handle_this(self, value):
        return re.match(self.match_regex, value) is not None

    def get_container_key(self, full_key):
        pass

    def add_content_data(self, data):
        self.data.append(data)
        self.data = zip(self.data, self.get_value_binded_item(data))

    def get_parameter(self, key):
        return eval("self.data['" + key.replace(".", "']['") + "']")

    def bind_value(self, value):
        keys_for_bind = re.findall(self.match_regex, str)
        for key in keys_for_bind:
            parameter = self.get_parameter(key)
            value = value.replace(key, parameter)
        return value

    def get_value_binded_item(self, item=None):
        if isinstance(item, list) or isinstance(item, dict):
            iterator = 0
            for item_key in item:
                object_indicatator = iterator if iterator in object else item_key
                value = item[object_indicatator]
                iterator += 1
                if isinstance(value, str):
                    item[object_indicatator] = self.application_container.bind_value(value)
                else:
                    item[object_indicatator] = self.get_value_binded_item(value)
        return item
