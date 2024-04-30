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
import sys
sys.path.insert(0, os.path.abspath('.'))



# -- Project information -----------------------------------------------------

project = 'SQream Blue'
copyright = '2024 SQream'
author = 'SQream Documentation'


html_title = "BLUE Documentation"

sphinxemoji_style = 'twemoji'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "notfound.extension", # 404 handling
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "sphinx_favicon",
    "sphinxemoji.sphinxemoji",
    "sphinx_design" 
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
html_theme = "furo"
html_static_path = ['_static']

images_dir = os.path.join(html_static_path[0], 'images')
html_static_path.append(images_dir)

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

favicons = [
    "Favicon - Documentation.png"
]

html_css_files = [
    'css/custom.css', # Relative to the _static path
]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'solarized-light'



# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#
show_authors = False

# Hide "Sphinx" details

html_show_sphinx = False
html_show_copyright = True



#Hide the sidebar
html_sidebars = {}




# furo theme specifics

html_theme_options = {
   'logo_only': True # Hide "SQream Blue" title and only show logo
   , 'display_version': False # Display version at the top
   , 'navigation_depth': -1
   , 'collapse_navigation': False
   , 'titles_only': True
   , 'top_of_page_button': "edit"
   , 'dark_logo': 'images/SQream_logo_dark_mode.png'
   , 'light_logo': 'images/SQream_logo_bright_mode.png'
   , "sidebar_hide_name": True
   , "footer_icons": 'None'
   , "rst-versions": False
   , "light_css_variables": {
        "font-stack": "Arial, sans-serif",
        "font-stack--monospace": "Courier, monospace",
    }
}
   



latex_engine = 'xelatex'

latex_elements = {
    'preamble': r'''
\usepackage[utf8x]{inputenc} 
'''
}

# For version replaces in some pages (like client drivers page)

#base_version = release.split('-')[0]
#rst_epilog = """
#.. |latest_version| replace:: v{}
#""".format(base_version)
