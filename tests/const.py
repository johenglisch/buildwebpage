'''Constant strings for all tests to share.'''


# template strings
TEMPLATE = '''<html>
<head><title>\xf6\u044b - {0}</title></head>
<body><p id='test_menuitem'>Menu</p>
{1}
</body></html>
'''
TMPL_TITLE = '<!-- title -->'
TMPL_CONTENT = '<!-- content -->'

# subpage strings
SUBPAGE = 'ASCII \xdcnic\xf6de \u044e\u043d\u0438\u043a\u043e\u0434'
SUB_TITLE = '<!-- title: This is a test page! -->'
SUB_MENUOK = '<!-- menu: test_menuitem -->'
SUB_MENUBAD = '<!-- menu: test_nonexistent -->'
SUB_MARKDOWN = '''<!-- markdown -->
# Test
`ASCII`
\xdcnic\xf6de
*\u044e\u043d\u0438\u043a\u043e\u0434*'''


# comparison strings
CMP_BARE = '''<html>
<head><title>\xf6\u044b - </title></head>
<body><p id='test_menuitem'>Menu</p>
ASCII \xdcnic\xf6de \u044e\u043d\u0438\u043a\u043e\u0434
</body></html>
'''
CMP_TITLE = '''<html>
<head><title>\xf6\u044b - This is a test page!</title></head>
<body><p id='test_menuitem'>Menu</p>

ASCII \xdcnic\xf6de \u044e\u043d\u0438\u043a\u043e\u0434
</body></html>
'''
CMP_MENU = '''<html>
<head><title>\xf6\u044b - </title></head>
<body><p id='test_menuitem' class='menu-current' >Menu</p>

ASCII \xdcnic\xf6de \u044e\u043d\u0438\u043a\u043e\u0434
</body></html>
'''
CMP_MENUBAD = '''<html>
<head><title>\xf6\u044b - </title></head>
<body><p id='test_menuitem'>Menu</p>

ASCII \xdcnic\xf6de \u044e\u043d\u0438\u043a\u043e\u0434
</body></html>
'''
CMP_MARKDOWN = '''<html>
<head><title>\xf6\u044b - This is a test page!</title></head>
<body><p id='test_menuitem'>Menu</p>
<h1>Test</h1>
<p><code>ASCII</code>
\xdcnic\xf6de
<em>\u044e\u043d\u0438\u043a\u043e\u0434</em></p>
</body></html>
'''
