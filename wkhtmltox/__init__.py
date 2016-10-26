# -*- coding: utf-8 -*-
"""
Wkhtmltopx python wrapper to convert html to pdf or image using the webkit rendering engine and qt
"""

__author__ = 'Golovanov Stanislav'
__version__ = '0.5.0'
__license__ = 'MIT'

from .wkhtmltopdf import wkhtmltopdf
from .api import configuration
from .pdf_api import pdf_from_url, pdf_from_file, pdf_from_string
from .img_api import img_from_url, img_from_file, img_from_string
