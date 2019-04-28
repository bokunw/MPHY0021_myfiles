# -*- coding: utf-8 -*-
"""
Tue Nov 20 2018

@author: Bokun Wei

This is a setup python file to make the code package installable. It specifies
the name, author, version, dependencies and entry points of the package.
"""

from setuptools import setup, find_packages

setup(
    name="alchemist",
    version="1.0.0",
    packages=find_packages(exclude=['*tests']),
    author='Bokun Wei',
    install_requires=[  # specify dependencies
        'pyyaml'
    ],
    entry_points={
        'console_scripts': [
            'abracadabra = alchemist.command:abracadabra'
        ]})
