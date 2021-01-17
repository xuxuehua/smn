import os
import unittest

from Smn.config import parse_config_yaml


class MyTestCase(unittest.TestCase):

    def test_parse_config_yaml(self):

        config_yaml_path = os.path.join(os.path.dirname(__file__), 'test_config.yml')
        parse_config_yaml(config_yaml=config_yaml_path)


if __name__ == '__main__':
    unittest.main()
