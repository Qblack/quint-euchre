"""Sphinx configuration."""
project = "Quint Euchre"
author = "Quinton Black"
copyright = "2023, Quinton Black"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
