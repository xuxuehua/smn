import datetime
import io
import os

from Smn.common_func import get_logger
from Smn.config import parse_config_yaml
from Smn.constants import MARKDOWN_META, FILE_EXTENSION

logger = get_logger(__name__)


class MarkdownEngine:

    def __init__(self, title, category_name=None):
        self.title = title
        self.notebook_path = parse_config_yaml().get('notebook_path')
        self.category_dirname = parse_config_yaml().get('md_dirname')
        self.category_name = category_name

    def create_notebook(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

        notebook_meta = {
            'title': self.title,
            'category': self.category_name,
            'date': now
        }

        current_notebook_meta = MARKDOWN_META.format(**notebook_meta)

        category_full_path = os.path.join(self.notebook_path, self.category_dirname, self.category_name)
        notebook_name = self.title + FILE_EXTENSION.MD
        notebook_full_path = os.path.join(category_full_path, notebook_name)

        if not os.path.exists(category_full_path):
            os.makedirs(category_full_path)
            logger.info(f"New category={self.category_name} has been created.")
        else:
            logger.info(f"Skipped operation because category={self.category_name} already existed.")

        if not os.path.exists(notebook_full_path):
            with io.open(notebook_full_path, 'wt', encoding='utf-8') as new_f:
                new_f.write(current_notebook_meta)
            logger.info(f"New notebook={notebook_name} has been created.")
        else:
            logger.info(f"Skipped operation because notebook={notebook_name} already existed.")

    def preview_notebook(self):
        pass
