import os
import yaml

from Smn.constants import DEFAULT_CONFIG, CONFIG_FILENAME


def parse_config_yaml():
    config_yaml = os.path.join(os.path.abspath('./'), CONFIG_FILENAME)
    if not os.path.exists(config_yaml):
        raise RuntimeError("{0} not exists".format(config_yaml))

    with open(config_yaml, 'r') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)

    DEFAULT_CONFIG.update(config)
    return DEFAULT_CONFIG
