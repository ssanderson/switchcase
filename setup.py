#!/usr/bin/env python
from setuptools import setup, find_packages
import sys

long_description = ''

if 'upload' in sys.argv:
    with open('README.rst') as f:
        long_description = f.read()

setup(
    name='switchcase',
    version='1.0',
    description='Switch-Case in pure Python',
    author='Scott Sanderson',
    author_email='scott.b.sanderson90@gmail.com',
    packages=find_packages(),
    long_description=long_description,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    url='https://github.com/ssanderson/switchcase',
)
