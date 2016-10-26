# -*- coding: utf-8 -*-

from .wkhtmltox import wkhtmltox

class wkhtmltopdf(wkhtmltox):
    """
    Main class that does all generation routine.

    :param url_or_file: str - either a URL, a path to a file or a string containing HTML
                       to convert
    :param type_: str - either 'url', 'file' or 'string'
    :param options: dict (optional) with wkhtmltopdf options, with or w/o '--'
    :param toc: dict (optional) - toc-specific wkhtmltopdf options, with or w/o '--'
    :param cover: str (optional) - url/filename with a cover html page
    :param configuration: (optional) instance of pdfkit.configuration.Configuration()
    """

    def __init__(self, url_or_file, type_, options=None, toc=None, cover=None,
                 css=None, configuration=None, cover_first=False):
        super(wkhtmltopdf, self).__init__(url_or_file, type_, options=options, css=css, configuration=configuration)

        self.executable = self.configuration.wkhtmltopdf.decode('utf-8')

        self.toc = {} if toc is None else toc
        self.cover = cover
        self.cover_first = cover_first

    def _builtinargs(self):
        if self.cover and self.cover_first:
            yield 'cover'
            yield self.cover

        if self.toc:
            yield 'toc'
            for argpart in self._genargs(self.toc):
                if argpart:
                    yield argpart

        if self.cover and not self.cover_first:
            yield 'cover'
            yield self.cover
