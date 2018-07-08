class DependencyInjectionContainer():
    handlers = {}

    def register_yaml_handler(self, yaml_handler, handler_name):
        yaml_handler.application_container = self
        self.handlers[handler_name] = yaml_handler

    def add_file_content(self, content):
        for entry in content:
            handler = self.get_handler_able_to_handle_this_entry_key(entry)
            handler.add_content_data(content[entry])

    def get_handler_able_to_handle_this_entry_key(self, key):
        return [handler for handler in self.handlers.values() if handler.yaml_entry_point == key][0]

    def get_handler_able_to_handle_value(self, value):
        for handle in self.handlers:
            if self.handlers[handle].can_i_handle_this(value):
                return self.handlers[handle]
        return None

    def bind_value(self, value):
        handler = self.get_handler_able_to_handle_value(value)
        if None == handler:
            return value
        value = handler.bind_value(value)
        return self.bind_value(value)

    def compile_all_handlers(self):
        for handle in self.handlers:
            self.handlers[handle].compile()

    def get(self, key):
        return self.handlers[key]
