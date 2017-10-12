#!/usr/bin/env python

from datetime import datetime
from setuptools import setup

setup(
    name='JustWatch Scraper',
    version=datetime.now().strftime('%Y.%m.%d.%H%M%S'),
    packages=['justwatch'],
    # If you directly `import` packages, put them here.
    # The full dependency tree with specific versions goes in requirements.txt
    install_requires=[ 'splinter'],
    entry_points={
        'console_scripts': [
            'justwatch = justwatch.main:main',
        ],
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ],
)
