#!/usr/bin/env python3

"""Setup script."""

from setuptools import setup


setup(
    name="hangman",
    version="0.0.0",
    author="Dmitriy Shulchevskiy",
    author_email="dshulchevskii@gmail.com",
    packages=[
        'hangman',
    ],
    scripts=[
        'hangman/bin/hangman',
    ],
    install_requires=[
    ],
    setup_requires=[
        "pytest-runner",
        "pytest-pylint",
        "pytest-pycodestyle",
        "pytest-pep257",
        "pytest-cov",
    ],
    tests_require=[
        "pytest",
        "pylint",
        "pycodestyle",
        "pep257",
    ],
)
