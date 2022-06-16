# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2022/6/15 16:53
# @Author : way
# @Site : 
# @Describe:

"""
打包流程：
python setup.py sdist bdist_wheel
twine upload dist/*
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = "DorisClient",
    version = "0.1.1",
    description = "python for doris",
    license = "MIT Licence",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url = "https://github.com/TurboWay/DorisClient",
    author = "Way",
    author_email = "1143496751@qq.com",
    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = ["requests", "mysqlclient"]
)
