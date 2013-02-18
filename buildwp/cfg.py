# Default input and output files
DEFAULT_FILE_WILDCARD = '_*'
DEFAULT_TEMPLATE = 'template.html'
BUILD_DEST = './build/'

# Keywords
SUBST_CONTENT = 'content'
SUBST_TITLE = 'title'
SUBST_MENU = 'menu'
SUBST_ATTRIBUTE = 'id'
SUBST_CURRENTMENU = 'menu_current'

# Html templates
HTML_COMMENT = '<!-- {0} -->'

# Partial regexes
_RE_COMMENT = r'<!--\s*{0}\s*-->'
_RE_SUBST_PROPERTY = r'{0}\s*:\s*(.+?)'
_RE_ATTRIBUTE = '(<.*?{0}\s*=\s*[\'"]{1}[\'"])(.*?>)'

# Regexes
RE_TEMPL_TITLE = _RE_COMMENT.format(SUBST_TITLE)
RE_TEMPL_CONTENT = _RE_COMMENT.format(SUBST_CONTENT)
# We don't know what the menuid will be, so the regex gets a replacement field
RE_TEMPL_MENUID = _RE_ATTRIBUTE.format(SUBST_ATTRIBUTE , '{0}')
RE_SUBPG_TITLE = _RE_COMMENT.format(_RE_SUBST_PROPERTY.format(SUBST_TITLE))
RE_SUBPG_MENU = _RE_COMMENT.format(_RE_SUBST_PROPERTY.format(SUBST_MENU))