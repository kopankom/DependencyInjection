class ApplicationContainer():
    handlers = []

    def register_yaml_handler(self, yaml_handler):
        self.handlers[yaml_handler.yaml_entry_point] = yaml_handler

    def add_file_content(self, content):
        for entry in content:
            self.handlers[entry].add_content_data(content[entry])

    def who_can_handle_this(self, content):
        for entry in content:
            if entry in self.handlers:
                self.handlers[entry].add_content_data(content[entry])
            else:
                print('No one can handle name: ', entry)

    def bind_value(self, value):
        for handle in self.handlers:
            if self.handlers[handle].can_i_handle_this(value):
                value = self.handlers[handle].bind_value(value)
        return value
