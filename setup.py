#!/usr/bin/env python

from setuptools import setup, find_packages
from codecs import open
from os import path

# Get the long description from DESCRIPTION.rst
with open(
    path.join(path.abspath(path.dirname(__file__)), "DESCRIPTION.rst"), encoding="utf-8"
) as f:
    long_description = f.read()

tests_require = ["moto >=0.4.1"]

setup(
    name="majorkirby",
    version="1.0.0",
    description="Puts CloudFormation stacks into motion.",
    author="Sharp Hall",
    author_email="shall@azavea.com",
    keywords="aws cloudformation",
    packages=find_packages(exclude=["tests"]),
    install_requires=["troposphere>=0.7.2", "boto>=2.38.0"],
    extras_require={"dev": [], "test": tests_require},
    test_suite="tests",
    tests_require=tests_require,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
)
