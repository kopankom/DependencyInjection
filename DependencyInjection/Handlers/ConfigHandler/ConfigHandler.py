from DependencyInjection.Handlers.HandlerAbstract import HandlerAbstract

class ConfigHandler(HandlerAbstract):
    match_regex = '%([0-9a-zA-Z\.\_\-]+)%'
    yaml_entry_point = 'parameters'
    replace_pattern = '%{0}%'
