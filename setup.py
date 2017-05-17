# coding: utf-8
from __future__ import absolute_import

import os
import sys
from codecs import open

from pyspark_loglikelihood import __version__

from setuptools import find_packages, setup

# root path
root_path = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, root_path)


# Get the long description from the README file
with open(os.path.join(root_path, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name="pyspark_loglikelihood",

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=__version__,

    description=("PySpark Loglikelihood Similarity Examples"),
    long_description=long_description,

    # author
    author="Tal Almagor",
    author_email="almagoric@gmail.com",

    # Choose your license
    license="MIT",

    # Project URL
    url="https://github.com/talmago/pyspark-loglikelihood",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[],

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'

    data_files=[("", ["README.md"])],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=['docopt'],

    # shell scripts
    scripts=[
        'examples/item-similarity-ml-100k-dataset'
    ],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        'console_scripts': [
        ]
    }
)
