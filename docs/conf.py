# -*- coding: utf-8 -*-
# icalendar documentation build configuration file
import pkg_resources
import datetime
import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode'
]
source_suffix = '.rst'
master_doc = 'index'

project = u'icalendar'
this_year = datetime.date.today().year
copyright = u'{}, Plone Foundation'.format(this_year)
version = pkg_resources.get_distribution('icalendar').version
release = version

exclude_patterns = ['_build', 'lib', 'bin', 'include', 'local']
pygments_style = 'sphinx'

htmlhelp_basename = 'icalendardoc'

man_pages = [
    ('index', 'icalendar', u'icalendar Documentation',
     [u'Plone Foundation'], 1)
]
