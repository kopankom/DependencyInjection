class ApplicationContainer():
    handlers = {}

    def register_yaml_handler(self, yaml_handler):
        self.handlers[yaml_handler.yaml_entry_point] = yaml_handler
        self.handlers[yaml_handler.yaml_entry_point].application_container = self

    def add_file_content(self, content):
        for entry in content:
            self.handlers[entry].add_content_data(content[entry])

    def who_can_handle_this(self, content):
        for entry in content:
            if entry in self.handlers:
                self.handlers[entry].add_content_data(content[entry])
            else:
                print('No one can handle name: ', entry)

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
