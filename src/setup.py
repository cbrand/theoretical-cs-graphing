# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import os
import sys

from setuptools import setup, find_packages

requires = [
    "funcparserlib",
    "zope.interface",
    "zope.component",
    "networkx",
    "matplotlib",
]

setup(
    name='scnet.grapher',
    version='1.0.0dev',
    description='Tool used for a university class of mine'
                'Graphical',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    author='Christoph Brand',
    author_email='ch.brand@scolterius.net',
    url='http://github.com',
    keywords='',
    packages=find_packages(),
    namespace_packages=['scnet'],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points="""\

    """,
)
