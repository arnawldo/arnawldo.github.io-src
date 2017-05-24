#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Arnold Taremwa'
SITENAME = "Arnold's Notes"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Africa/Kampala'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# bootstrap settings
THEME = 'themes/pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['i18n_subsites', 'liquid_tags.notebook']

# notebook settings
NOTEBOOK_DIR = 'notebooks' # within content folder

# site tracking and commentting
GOOGLE_ANALYTICS_UNIVERSAL = 'UA-88394833-2'
DISQUS_SITENAME = 'arnawldo'

# about me
ABOUT_ME = 'I\'m Arnold Taremwa, trained in the geosciences. I like to get my hands dirty with data, using statistics and visualizations to derive meaning from it.'

# license
CC_LICENSE = "CC-BY"

ADDTHIS_PROFILE = "ra-59254803a645d109"

