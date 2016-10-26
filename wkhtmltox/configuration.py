# -*- coding: utf-8 -*-
import subprocess
import sys


class Configuration(object):
    def __init__(self, wkhtmltopdf='', wkhtmltoimage='', meta_tag_prefix='pdfkit-'):
        self.meta_tag_prefix = meta_tag_prefix
        
        self._set_executable('wkhtmltopdf', wkhtmltopdf)
        self._set_executable('wkhtmltoimage', wkhtmltoimage)
        

    def _set_executable(self, executable_name, executable_path=''):
        if not executable_path:
            if sys.platform == 'win32':
                executable_path = subprocess.Popen(
                    ['where', executable_name], stdout=subprocess.PIPE).communicate()[0].strip()
            else:
                executable_path = subprocess.Popen(
                    ['which', executable_name], stdout=subprocess.PIPE).communicate()[0].strip()

        try:
            with open(executable_path) as f:
                pass
        except IOError:
            raise IOError('No wkhtmltopdf executable found: "%s"\n'
                          'If this file exists please check that this process can '
                          'read it. Otherwise please install wkhtmltopdf - '
                          'https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf' % self.wkhtmltopdf)
        else:
            setattr(self, executable_name, executable_path)