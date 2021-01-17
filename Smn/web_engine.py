import io
import os
import re
import markdown
import yaml

from Smn.common_func import get_logger
from Smn.config import parse_config_yaml
from Smn.constants import FILE_EXTENSION, SmnMetaName

logger = get_logger(__name__)


class WebEngine:

    def __init__(self):
        self.html_dirname = parse_config_yaml().get('html_dirname')
        self.md_dirname = parse_config_yaml().get('md_dirname')
        self.notebook_path = parse_config_yaml().get('notebook_path')

    def markdown_to_html(self, md_content):
        markdown_extensions = self._customized_markdown_extenstions()
        html_content = markdown.markdown(md_content, extensions=markdown_extensions)
        return html_content

    def _customized_markdown_extenstions(self):
        return []

    def parse_md_header(self, md_header):
        try:
            md_header_dict = yaml.load(md_header, Loader=yaml.FullLoader)
        except yaml.YAMLError as e:
            logger.error(f"Can not parse md_header with error={e}")
        return md_header_dict

    def parse_md_content(self, md_filepath):
        regex = re.compile('(?sm)^---(?P<header>.*?)^---(?P<body>.*)')
        with io.open(md_filepath, 'rt', encoding='utf-8') as md_f:
            matched_obj = re.match(regex, md_f.read())

        md_header = matched_obj.group('header')
        md_body = matched_obj.group('body')
        print(type(md_header), md_header)
        return md_header, md_body

    def convert_md_to_html(self):
        for dirpath, dirnames, filenames in os.walk(self.md_dirname):
            for f in filenames:
                md_filepath = os.path.join(dirpath, f)
                md_header, md_body = self.parse_md_content(md_filepath)
                md_header_dict = self.parse_md_header(md_header)
                html_content = self.markdown_to_html(md_content=md_body)
                html_filename = md_header_dict[SmnMetaName.title] + FILE_EXTENSION.HTML

                html_category_path = os.path.join(self.notebook_path,
                                                  self.html_dirname,
                                                  md_header_dict[SmnMetaName.category])

                if not os.path.exists(html_category_path):
                    os.makedirs(html_category_path)

                html_fullpath = os.path.join(html_category_path, html_filename)
                with io.open(html_fullpath, 'w+', encoding='utf-8') as new_f:
                    new_f.write(html_content)






