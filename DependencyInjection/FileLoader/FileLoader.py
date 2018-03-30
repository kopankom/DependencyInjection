class FileLoader():
    base_path = 'src'
    replace_prefix_list = {}
    concatenation_char_for_class_path = ':'
    concatenation_char_desired_for_class_path = '.'

    def build_class_path(self, path):
        result = self.base_path + self.concatenation_char_desired_for_class_path
        for module_name in self.replace_prefix_list:
            if path.startswith(module_name):
                result += path.replace(module_name, self.replace_prefix_list[module_name])
                result = result.replace(self.concatenation_char_for_class_path, self.concatenation_char_desired_for_class_path)
                return result
        result += path
        result = result.replace(self.concatenation_char_for_class_path, self.concatenation_char_desired_for_class_path)
        return result

    def get_class_path(self, class_suffix):
        pass
