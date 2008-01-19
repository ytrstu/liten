#!/usr/bin/env python

# liten 0.1.3 -- deduplication command line tool
#
# Author: Noah Gift

from setuptools import Extension, find_packages, setup


setup(name='liten',
      version='0.1.3',
      description='a de-duplication command line tool',
      long_description="This command line tool will examine a file system and \
      report back duplicates using a md5 checksum hash algorithm.",
      author='Noah Gift',
      author_email='noah.gift@gmail.com',
      url='http://code.google.com/p/liten/',
      license='MIT',
      packages=find_packages(),
      zip_safe=False,
      entry_points="""
      py_modules=['liten']
      [console_scripts]
      liten = liten:main
      """,
      )

