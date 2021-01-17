import datetime
import tzlocal


class SmnMetaName:
    title = 'title'
    category = 'category'


DEFAULT_CONFIG = {
    "url": "",
    "title": "",
    "keywords": "",
    "description": "",
    "author": "",
    "root": "/",
    "md_dirname": "md_contents",
    "html_dirname": "html_outputs",
    "attach": "attach",
    "themes_dir": "themes",
    "theme": "simple2",
    "default_category": "",
    "pygments": True,
    "debug": False,
    "time": str(datetime.datetime.now(tzlocal.get_localzone())),
}

MARKDOWN_META = "\n".join([
    "---",
    "title: \"{title}\"",
    "category: \"{category}\"",
    "date: {date}",
    "---",
    "\n\n",
    "[TOC]"
]) + "\n\n"


class FILE_EXTENSION:
    MD = '.md'
    YAML = '.yaml'
    HTML = '.html'


CONFIG_FILENAME = 'config' + FILE_EXTENSION.YAML

