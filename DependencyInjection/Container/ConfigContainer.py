from DependencyInjection.Container.ContainerAbstract import ContainerAbstract


class ConfigContainer(ContainerAbstract):
    match_regex = '%([0-9a-zA-Z\.\_\-]+)%'
    yaml_entry_point = 'parameters'
    replace_pattern = '%{0}%'
