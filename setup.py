import os
import re
from billow import __version__
from setuptools import setup, find_packages

setup(
    name='billow',
    version=__version__,
    author="Chris Maxwell",
    author_email="chris@wrathofchris.com",
    description="a large undulating mass of cloud services",
    url="https://github.com/WrathOfChris/billow",
    download_url='https://github.com/WrathOfChris/billow/tarball/%s' % __version__,
    license="BSD",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        'boto',
        'PyYAML'
    ],
    entry_points={
        "console_scripts": [
            "billow-list = billow.cli:billow_list",
            "billow-get = billow.cli:billow_get",
            "billow-find-configs = billow.cli:billow_find_configs",
            "billow-list-configs = billow.cli:billow_list_configs",
            "billow-find-images = billow.cli:billow_find_images",
            "billow-list-images = billow.cli:billow_list_images"
        ]
    }
)
