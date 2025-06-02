import os
import re

from setuptools import find_packages, setup


def get_requirements(req_path: str):
    with open(req_path, encoding="utf8") as f:
        return f.read().splitlines()


INSTALL_REQUIRES = get_requirements("requirements.txt")


def get_long_description():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base_dir, "README.md"), encoding="utf-8") as f:
        return f.read()


def get_version():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    version_file = os.path.join(current_dir, "codecplus", "__init__.py")
    with open(version_file, encoding="utf-8") as f:
        return re.search(r'^__version__ = [\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)


def get_author():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    init_file = os.path.join(current_dir, "codecplus", "__init__.py")
    with open(init_file, encoding="utf-8") as f:
        return re.search(r'^__author__ = [\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)


def get_license():
    current_dir = os.path.abspath(os.path.dirname(__file__))
    init_file = os.path.join(current_dir, "codecplus", "__init__.py")
    with open(init_file, encoding="utf-8") as f:
        return re.search(r'^__license__ = [\'"]([^\'"]*)[\'"]', f.read(), re.M).group(1)


setup(
    name="codecplus",
    version=get_version(),
    description="Audio codec models implementation library",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author=get_author(),
    author_email="kadir.nar@example.com",
    url="https://github.com/kadirnar/CodecPlus",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=INSTALL_REQUIRES,
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
