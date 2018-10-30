#!/usr/bin/env python

from distutils.core import setup

setup(name='Understanding',
      version='0.2',
      description='Understanding module for chat bots',
      author='Koen van Eijk',
      author_email='koen@bottist.com',
      url='https://bottist.com/',
      packages=['understanding'],
      install_requires=[
          'requests>=2.20.0',
      ],
     )
