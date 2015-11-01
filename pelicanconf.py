# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys
sys.path.append('.')


AUTHOR = u'Thomas Stieglmaier'
SITENAME = u'stieglmaier'
SITEURL = '//stieglmaier.me'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

RELATIVE_URLS = False

# Formatting for dates
DEFAULT_DATE_FORMAT = ('%Y-%m-%dT%H:%M:%SZ')

ARTICLE_DIR = 'blog'
ARTICLE_URL = "blog/{slug}"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

PAGE_DIR = 'pages'
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'

THEME = "themes/myTemplate"

STATIC_PATHS = ['css',
                'pics',
                'uploads']

DISPLAY_PAGES_ON_MENU = True
