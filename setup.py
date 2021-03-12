#!/usr/bin/env python
from setuptools import setup

PACKAGE_NAME = 'python-foreman'
URL = 'https://github.com/david-caro/python-foreman'

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as fn:
        return fn.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()
    for package in required:


if __name__ == '__main__':
    setup(
        autosemver=True,
        install_requires=required,
        name='python-foreman',
        include_package_data=True,
        packages=['foreman'],
        description=(
            'Simple low-level client library to access the Foreman API'
        ),
        author='David Caro',
        author_email='david@dcaro.es',
        url='https://github.com/david-caro/python-foreman',
        bugtracker_url='https://github.com/david-caro/python-foreman/issues/',
        license='GPLv2',
        classifiers=[
            'Intended Audience :: Developers',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.4',
        ],
    )
