from os import path
from helpers import load_yaml_file, get_current_directory

dirname = get_current_directory()
config_file = path.join(dirname, "config.yml")

def getConfig():
    """Load configuration from YAML file."""
    config_file = path.join(dirname, "config.yml")
    return load_yaml_file(config_file)




