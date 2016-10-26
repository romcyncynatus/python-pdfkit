# -*- coding: utf-8 -*-

from .wkhtmltox import Configuration


def configuration(**kwargs):
    """
    Constructs and returns a :class:`Configuration` with given options

    :param wkhtmltopdf: path to binary
    :param meta_tag_prefix: the prefix for ``wkhtmltopdf`` specific meta tags
    """

    return Configuration(**kwargs)