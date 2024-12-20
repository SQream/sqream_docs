# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os

# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True

import sphinx_rtd_theme
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# -- Project information -----------------------------------------------------

project = 'SQreamDB'
copyright = '2024 SQreamDB'
author = 'SQreamDB Documentation'


# The full version, including alpha/beta/rc tags
release = '4.9'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx_rtd_theme",
    "notfound.extension", # 404 handling
    "sphinx_favicon"
]

# Mark 'index' as the main page
master_doc = 'index'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'



# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    'css/custom.css', # Relative to the _static path
]

html_logo = '_static/images/SQream_logo_without background-15.png'

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#
show_authors = False

# Hide "Sphinx" details
html_show_sphinx = False


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'autumn'

html_show_copyright = True

# RTD theme specifics

html_theme_options = {
   'logo_only': True # Hide "SQream DB" title and only show logo
   , 'display_version': True # Display version at the top
   , 'style_external_links': True # Show little icon next to external links
   , 'style_nav_header_background': '#133148' # SQream teal
   , 'navigation_depth': -1
   , 'collapse_navigation': False
   , 'titles_only': True
   , 'flyout_display': 'attached'

}

latex_engine = 'xelatex'

latex_elements = {
    'preamble': r'''
\usepackage[utf8x]{inputenc} 
'''
}

# For version replaces in some pages (like client drivers page)

base_version = release.split('-')[0]
rst_epilog = """
.. |latest_version| replace:: v{}
""".format(base_version)
