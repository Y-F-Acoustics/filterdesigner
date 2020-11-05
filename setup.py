#!/usr/bin/env python

import os
from setuptools import setup, find_packages
__version__ = "0.0.1"

def read(fname):
    try:
        with open(os.path.join(os.path.dirname(__file__), fname)) as fp:
            return fp.read()
    except IOError:
        return ""

setup(
    name='filterdesigner',
    version=__version__,
    packages=find_packages(),
    """
    package_data={
      'filterdesigner': []
    },
    """
    install_requires=['numpy', 'scipy', 'matplotlib'],
    zip_safe=False,
    include_package_data=True,
    author="Yuki Fukuda",
    #author_email="giuseppe.g.venturini@ieee.org",
    description="A MATLAB-like and simple digital filter design library for python.",
    """
    long_description=''.join([read('pypi_description.rst'), '\n\n',
                              read('CHANGES.rst')]),
    """
    license="BSD",
    keywords="digital filter",
    url="https://github.com/Y-F-Acoustics/filterdesigner",
    test_suite = "filterdesigner.tests",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        "Natural Language :: English",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ]
)
