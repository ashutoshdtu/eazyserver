#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import os
import glob

with open('VERSION') as version_file:
    version = version_file.read().strip()

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open('AUTHORS.rst') as authors_file:
    authors = authors_file.read()

with open('CONTRIBUTING.rst') as contributing_file:
    contributing = contributing_file.read()

requirements = ['Click>=6.0', ]
with open('requirements_dev.txt') as f:
    requirments = f.read().splitlines()

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Ashutosh Mishra",
    author_email='ashutoshdtu@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="A simple python web framework for creating RESTful and JSON-RPC services",
    entry_points={
        'console_scripts': [
            'eazyserver=eazyserver.cli:cli',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='eazyserver',
    name='eazyserver',
    packages=find_packages("src", include=['eazyserver']),
    package_dir={"": "src"},
    py_modules=[os.path.splitext(os.path.basename(i))[0] for i in glob.glob("src/*.py")],
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ashutoshdtu/eazyserver',
    version=version,
    zip_safe=False,
)
