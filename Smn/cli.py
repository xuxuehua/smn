#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import yaml
import fire

from Smn.common_func import get_logger
from Smn.constants import CONFIG_FILENAME, DEFAULT_CONFIG
from Smn.md_engine import MarkdownEngine
from Smn.web_engine import WebEngine

logger = get_logger(__name__)


class New:

    def title(self, title, category=None):
        """
        Help for new
        category name
        for new markdown files
        """
        current_dir = os.path.abspath('./')
        if not os.path.exists(current_dir + "/config.yaml"):
            logger.info('Please run smn init to start project')

        new_note = MarkdownEngine(title=title, category_name=category)
        new_note.create_notebook()


class CommandLine:
    """
    usage: smn [options] <command> <subcommand> [<subcommand> ...] [parameters]
    \n
    smn -h/--help
    smn <command> -h/--help
    smn <command> <subcommand> -h/--help
    """

    def __init__(self):
        self.current_dir = os.path.abspath('./')
        self.new = New()

    def init(self):
        """
        Help for init
        :return:
        """
        current_dir = os.path.abspath('./')
        config_path = os.path.join(current_dir, CONFIG_FILENAME)

        data = {'notebook_path': current_dir,
                'default_category': 'default'}
        DEFAULT_CONFIG.update(data)

        with open(config_path, 'w') as f:
            yaml.dump(DEFAULT_CONFIG, f)

    def generate(self):
        notebook = WebEngine()
        notebook.convert_md_to_html()


if __name__ == '__main__':
    fire.Fire(CommandLine)
