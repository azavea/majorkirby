#!/usr/bin/env python

from distutils.core import setup

setup(name='majorkirby',
      version='0.0.0',
      description='Puts cloudformation stacks into motion',
      author='Sharp Hall',
      author_email='shall@azavea.com',
      packages=['majorkirby'],
      requires=['troposphere (>=0.7.2)', 'boto (>=2.38.0)']
      )
