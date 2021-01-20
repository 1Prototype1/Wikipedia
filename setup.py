# -*- coding: utf-8 -*-
import codecs
import os
import re
import setuptools


def local_file(file):
  return codecs.open(
    os.path.join(os.path.dirname(__file__), file), 'r', 'utf-8'
  )

install_reqs = [
  line.strip()
  for line in local_file('requirements.txt').readlines()
  if line.strip() != ''
]

setuptools.setup(
  name = "wikipedia",
  version = "1.4.1",
  author = "Jonathan Goldsmith",
  maintainer = "1Prototype1",
  maintainer_email = "astonlopes1999@gmail.com",
  description = "Wikipedia API for Python",
  license = "MIT",
  keywords = "python wikipedia API",
  url = "https://github.com/1Prototype1/Wikipedia",
  install_requires = install_reqs,
  packages = ['wikipedia'],
  long_description = local_file('README.rst').read(),
  classifiers = [
    'Development Status :: 4 - Beta',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3'
  ]
)
