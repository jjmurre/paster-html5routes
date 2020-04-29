# -*- coding: utf-8 -*-
"""\
===========
html5routes
===========

WSGI middleware for html5-based routes
"""

# FIXME: Please read http://pythonhosted.org/setuptools/setuptools.html to
#        customize in depth your setup script

from setuptools import setup, find_packages
import os

version = '0.0.2'

this_directory = os.path.abspath(os.path.dirname(__file__))


def read(*names):
    return open(os.path.join(this_directory, *names), 'r').read().strip()

long_description = '\n\n'.join(
    [read(*paths) for paths in (('README.rst',), ('CHANGES.rst',))]
)
dev_require = []


setup(name='html5routes',
      version=version,
      description="WSGI middleware for html5-based routes",
      long_description=long_description,
      # FIXME: Add more classifiers from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
          "Programming Language :: Python",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)"
      ],
      keywords='wsgi',  # FIXME: Add whatefer fits
      author='Jan Murre',
      author_email='jan.murre@gmail.com',
      url='http://pypi.python.org/pypi/html5routes',
      license='GPLv3',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # 3rd party
          'setuptools'
          # Others
      ],
      entry_points={
          "paste.filter_app_factory": ["html5routes = html5routes:filter_app_factory"],
      },
      tests_require=dev_require,
      test_suite='tests.all_tests',
      extras_require={
          'development': dev_require
      })
