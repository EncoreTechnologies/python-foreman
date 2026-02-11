#!/usr/bin/env python
from setuptools import setup

PACKAGE_NAME = 'python-foreman'
URL = 'https://github.com/EncoreTechnologies/python-foreman'
VERSION = '0.4.0'


if __name__ == '__main__':
    setup(
        version=VERSION,
        install_requires=[
            'requests',
            'six',
        ],
        name=PACKAGE_NAME,
        include_package_data=True,
        packages=['foreman', 'foreman_plugins'],
        description=(
            'Simple low-level client library to access the Foreman API'
        ),
        author='David Caro',
        author_email='david@dcaro.es',
        url=URL,
        license='GPLv2',
        classifiers=[
            'Intended Audience :: Developers',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
        ],
    )
