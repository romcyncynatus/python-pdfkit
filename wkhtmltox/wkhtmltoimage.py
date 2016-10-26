# -*- coding: utf-8 -*-

from .wkhtmltox import wkhtmltox

class wkhtmltoimage(wkhtmltox):
    """
    Main class that does all generation routine.

    :param url_or_file: str - either a URL, a path to a file or a string containing HTML
                       to convert
    :param type_: str - either 'url', 'file' or 'string'
    :param options: dict (optional) with wkhtmltoimage options, with or w/o '--'
    :param configuration: (optional) instance of pdfkit.configuration.Configuration()
    :param format: (optional) image format (can be one of 'jpg', 'png', 'svg', etc...)
    """

    def __init__(self, url_or_file, type_, options=None, css=None, configuration=None, format=''):
        super(wkhtmltoimage, self).__init__(url_or_file, type_, options=options, css=css, configuration=configuration)

        self.executable = self.configuration.wkhtmltoimage.decode('utf-8')

        self.format = format

    def _builtinargs(self):
        if self.format:
            yield '--format'
            yield self.format