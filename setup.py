#!/usr/bin/env python
import os
from codecs import open

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


here = os.path.dirname(__file__)
if here:
    os.chdir(here)

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()
with open('CHANGES.rst', 'r', 'utf-8') as f:
    changes = f.read()

requires = ['selenium']

setup(
    name='page-objects',
    version='1.1.0',
    description='Page Objects for Python',
    long_description=readme + '\n\n' + changes,
    author='Edward Easton',
    author_email='eeaston@gmail.com',
    url='http://github.com/eeaston/page-objects',
    packages=['page_objects'],
    package_data={'': ['LICENSE']},
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    zip_safe=True,
    classifiers=(
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Browsers',
        'Topic :: Software Development :: Testing',
    ),
    extras_require={
    },
)
