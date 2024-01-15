# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Vijil'
copyright = '2024, Vijil Inc'
author = 'Subho Majumdar'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    # Our custom extension, only meant for Furo's own documentation.
    # External stuff
    "myst_parser",
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_title = ' '
html_logo = '_static/vijil_wide.png'
# html_logo = 'https://assets-global.website-files.com/656632658074164265ceea17/6566346c1d4278e1ca3d0306_vijil_logo.svg'
html_favicon = 'https://assets-global.website-files.com/656632658074164265ceea17/6570d66fa750acafb3a837ac_favicon.png'

