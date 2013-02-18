import re
from . import cfg


# Precompile regexes
RE_TITLE = re.compile(cfg.RE_SUBPG_TITLE, re.UNICODE | re.IGNORECASE)
RE_MENU = re.compile(cfg.RE_SUBPG_MENU, re.UNICODE | re.IGNORECASE)


class Subpage(object):
    def __init__(self, content, filename=None):
        self.content = content
        self.has_title = False
        self.title = ''
        self.has_menu = False
        self.menu = ''
        match = RE_TITLE.search(content)
        if match:
            self.title = match.group(1)
            self.has_title = True
        match = RE_MENU.search(content)
        if match:
            self.menu = match.group(1)
            self.has_menu = True

    def get_html(self):
        return self.content


class MarkdownSubpage(Subpage):
    def get_html(self):
        raise NotImplementedError  # TODO use markdown parser for converting
