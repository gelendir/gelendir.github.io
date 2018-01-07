#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Gregory Fodé Sanderson'
SITENAME = 'Fodé: Le Foté Fou'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = 'fr'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

LINKS = ()

# Social widget
SOCIAL = (
    ('Github', 'https://github.com/gelendir'),
    ('Twitter', 'https://twitter.com/gelendir')
)

#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

STATIC_PATHS = ['images', 'CNAME']

THEME = "/Users/gregory/b/themes/nest"
SITESUBTITLE = "Random thoughts of a crazy dancer who likes coding"

NEST_HEADER_LOGO = '/images/logo_sol.jpg'
#NEST_HEADER_IMAGES = 'background.jpg'

NEST_INDEX_HEAD_TITLE = 'Accueil'
NEST_INDEX_HEADER_TITLE = 'Fodé: Le Foté Fou'
NEST_INDEX_HEADER_SUBTITLE = "Random thoughts of a crazy dancer who likes coding"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
