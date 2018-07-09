class DependencyInjectionContainer():
    handlers = {}

    def register_yaml_handler(self, yaml_handler, container_name):
        yaml_handler.application_container = self
        self.handlers[container_name] = yaml_handler

    def add_file_content(self, content):
        for entry in content:
            handler = self.get_handler_able_to_handle_this_entry_key(entry)
            handler.add_content_data(content[entry])

    def get_handler_able_to_handle_this_entry_key(self, key):
        return [handler for handler in self.handlers.values() if handler.yaml_entry_point == key][0]

    def get_handler_able_to_handle_value(self, value):
        for handler in self.handlers.values():
            return handler if handler.can_i_handle_this(value) else None

    def bind_value(self, value):
        handler = self.get_handler_able_to_handle_value(value)
        if not handler:
            return value
        value = handler.bind_value(value)
        return self.bind_value(value)

    def compile_all_handlers(self):
        [handler.compile() for handler in self.handlers.values()]

    def get_container(self, key):
        return self.handlers[key]
