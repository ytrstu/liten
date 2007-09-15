#!/usr/bin/env python

# liten 0.1.2 -- deduplication command line tool
#
# Author: Noah Gift

from ez_setup import use_setuptools
use_setuptools(min_version="0.6a9")

from setuptools import Extension, find_packages, setup


setup(name='liten',
      version='0.1.2',
      description='a de-duplication command line tool',
      long_description="This command line tool will examine a file system and report back duplicates using a md5 checksum hash algorithm.",
      author='Noah Gift',
      author_email='noah.gift@gmail.com',
      url='http://code.google.com/p/liten/',
      license='GNU GPL3',
      packages=find_packages(),
      classifiers=trove_classifiers,
      zip_safe=False,
      )

