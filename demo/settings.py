from pathlib import Path
import yaml


def load_config(conf_file=None):
    default_file = Path(__file__).parent / 'config.yaml'
    with open(default_file, 'r') as file:
        config = yaml.safe_load(file)

    cf_dict = {}
    if conf_file:
        cf_dict = yaml.safe_load(conf_file)

    config.update(**cf_dict)

    return config
