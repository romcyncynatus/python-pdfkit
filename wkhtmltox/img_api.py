# -*- coding: utf-8 -*-

from .wkhtmltoimage import wkhtmltoimage


def img_from_url(url, output_path, options=None, configuration=None, format=None):
    """
    Convert file of files from URLs to PDF document

    :param url: URL or list of URLs to be saved
    :param output_path: path to output PDF file. False means file will be returned as string.
    :param options: (optional) dict with wkhtmltoimage global and page options, with or w/o '--'
    :param configuration: (optional) instance of wkhtmltoimage.configuration.Configuration()
    :param format: (optional) image format (can be one of 'jpg', 'png', 'svg', etc...)

    Returns: True on success
    """

    r = wkhtmltoimage(url, 'url', options=options, configuration=configuration, format=format)

    return r.execute(output_path)


def img_from_file(input, output_path, options=None, configuration=None, css=None, format=None):
    """
    Convert HTML file or files to PDF document

    :param url: URL or list of URLs to be saved
    :param output_path: path to output PDF file. False means file will be returned as string.
    :param options: (optional) dict with wkhtmltoimage global and page options, with or w/o '--'
    :param configuration: (optional) instance of wkhtmltoimage.configuration.Configuration()
    :param css: (optional) string with path to css file which will be added to a single input file
    :param format: (optional) image format (can be one of 'jpg', 'png', 'svg', etc...)

    Returns: True on success
    """

    r = wkhtmltoimage(input, 'file', options=options, configuration=configuration, css=css, format=format)

    return r.execute(output_path)


def img_from_string(input, output_path, options=None, configuration=None, css=None, format=None):
    """
    Convert given string or strings to PDF document

    :param url: URL or list of URLs to be saved
    :param output_path: path to output PDF file. False means file will be returned as string.
    :param options: (optional) dict with wkhtmltoimage global and page options, with or w/o '--'
    :param configuration: (optional) instance of wkhtmltoimage.configuration.Configuration()
    :param css: (optional) string with path to css file which will be added to a single input file
    :param format: (optional) image format (can be one of 'jpg', 'png', 'svg', etc...)

    Returns: True on success
    """

    r = wkhtmltoimage(input, 'string', options=options, configuration=configuration, css=css, format=format)

    return r.execute(output_path)
