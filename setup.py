#
# Copyright 2021 Antoine Sanner
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

import glob
import re

from setuptools import setup, find_packages


setup(
    name="sacs",
    scripts=[],
    packages=find_packages(),
    package_data={'': ['ChangeLog.md']},
    include_package_data=True,
    # metadata for upload to PyPI
    author="Antoine Sanner",
    author_email="antoine.pastewka@imtek.uni-freiburg.de",
    description="Antoine Sanner's code snippets",
    license="MIT",
    test_suite='tests',
    # dependencies
    python_requires='>=3.6.0',
    use_scm_version=True,
    setup_requires=[
        'setuptools_scm>=3.5.0',
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    install_requires=[
    ]
)
