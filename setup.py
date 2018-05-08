#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', ]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author="Myst Fox",
    author_email='myst@focks.pw',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        # Doesn't have a gui but most of what it does is pointless w/o X
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Desktop Environment',
        'Topic :: Utilities',
    ],
    description="An attempt to unify many theming methods.",
    entry_points={
        'console_scripts': [
            'unitheme=unitheme.cli:main',
        ],
    },
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='unitheme',
    name='unitheme',
    packages=find_packages(include=['unitheme']),
    python_requires=">=3.6",
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/mystfox/unitheme',
    version='0.1.0',
    zip_safe=False,
)
