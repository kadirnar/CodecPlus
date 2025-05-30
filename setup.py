#!/usr/bin/env python

import os
import re

from setuptools import find_packages, setup

# Read version from __init__.py
with open(os.path.join("codecplus", "__init__.py"), encoding="utf-8") as f:
    version = re.search(r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read()).group(1)

# Read the README.md for the long description
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

# Read the requirements
with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().strip().split("\n")

setup(
    name="codecplus",
    version=version,
    description="Audio codec models implementation library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Kadir Nar",
    author_email="kadir.nar@example.com",
    url="https://github.com/kadirnar/CodecPlus",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    keywords="audio, codec, deep learning, machine learning, artificial intelligence",
)
