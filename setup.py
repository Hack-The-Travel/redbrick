import os
from codecs import open
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

packages = ['redbrick']

requires = list()

about = dict()
with open(os.path.join(here, 'redbrick', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=about['__description__'],
    url=about['__url__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    license=about['__license__'],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: API clients',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    packages=packages,
    install_requires=requires,
    extras_require={
        'test': ['pytest'],
    },
)
