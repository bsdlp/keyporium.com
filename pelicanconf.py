#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Jon Chen'
SITENAME = 'Keyporium'
SITEURL = 'http://keyporium.com'

TIMEZONE = 'Etc/UTC'

DEFAULT_LANG = 'en'

# plugins
PLUGIN_PATH = './plugins'
PLUGINS = ['assets']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DEFAULT_PAGINATION = 10

CSSJAWNS = True

# CNAME file for GitHub Project Pages
STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
