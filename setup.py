#!/usr/bin/env python
from distutils.core import setup

version = '1.0'

setup(name='bitdata',
      version=version,
      description="An API for bitly's data apis",
      author='Wes Madrigal',
      author_email='wes@spartzinc.com',
      url='https://github.com/wesmadrigal/bitdata',
      license='Apache Software License',
      packages=['bitdata'],
      include_package_data=True,
)
