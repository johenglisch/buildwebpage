# buildwebpage

## DESCRIPTION

The `buildwebpage` script builds a static webpage by inserting a number of
subpages into a template.

Features:
 * Specification of a title for a subpage which can be referenced by the
   template
 * Assignment of an menu item to a subpage so it can be formatted distinctively
 * Markdown support for subpages


## REQUIREMENTS

 * Python 2.7
 * Markdown


## USAGE

### Creating a webpage

The template file has to contain the comment `<!-- content -->` which is then
replaced by the content of the subpages.  By default all files starting with an
underscore `_` will be used as subpages.  This can be overridden by naming
subpages manually using either the command-line or the configuration file.

Apart from HTML this script supports input files using Markdown.  A file can be
set to be Markdown by inserting the comment `<!-- markdown -->`.  It will then
automatically converted to HTML when included into the template.

Each subpage can be assigned a title by including the HTML comment
`<!-- title: SOME TITLE TEXT -->`.  The title text given here will be inserted
in place of any occurence of `<!-- title -->` in the template.

Additionally one can mark a specific tag in the template to be the menu item
associated with a subpage by refering to its id using the
`<!-- menu: TAG ID -->` comment.  Any tag that contains the attribute
`id='TAG ID'` will be added a `class='menu-current'` which can then be
formatted using css.

The resulting webpage files will be created in the directory which is set to be
the destination folder.

### Command-line arguments

    buildwebpage [-h] [-c FILE] [-d DIR] [--gen-config]
                 [template] [subpage [subpage ...]]
    
    positional arguments:
      template              template for the webpage (defaults to
                            'template.html')
      subpage               subpage of the webpage (defaults to '_*')
    
    optional arguments:
      -h, --help            show this help message and exit
      -c FILE, --conf FILE  configuration file (defaults to 'buildwebpage.cfg')
      -d DIR, --dest DIR    destination folder of the finished webpage
                            (defaults to 'build/')
      --gen-config          save current configuration to the file specified by
                            the -c/--config argument

### The configuration file

The `buildwebpage` configuration file, called `buildwebpage.cfg` by default,
uses a simple `option = value` format to store settings.  All options set in
the configuration file can be overridden by passing command-line arguments to
`buildwebpage`.  The file consists of two sections:

The `[settings]` section contains settings for the `buildwebpage` script, which
include following options:

 * template: the name of the template file
 * dest: the destination folder where the finished website will reside

The `[subpages]` section contains a list of all subpages to be inserted into
the template.

The configuration file can be generated by passing the `--gen-config`
command-line option to `buildwebpage`.

Example configuration file:

    [settings]
    template = some-other-template.html
    dest = finished_website/
    
    [subpages]
    index.html
    somescript.php
    othersubpage.html


## LICENSE

Copyright (c) 2013 Johannes Englisch

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
