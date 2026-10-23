# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
from pathlib import Path

import django

# Raíz del proyecto (donde está manage.py), calculada desde la ubicación de este archivo
RAIZ = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(RAIZ))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce_project.settings')
django.setup()



project = 'NexusShop'
copyright = '2026, Equipo5_TallerIngSoftaware'
author = 'Equipo5_TallerIngSoftaware'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',    # lee los docstrings del código
    'sphinx.ext.napoleon',   # entiende el formato Google de docstrings
    'sphinx.ext.viewcode',   # agrega enlaces para ver el código fuente
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
