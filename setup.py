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
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    package_data={
        'redbrick': ['LICENSE'],
    },
    include_package_data=True,
    license=about['__license__'],
    zip_safe=False,
    install_requires=requires,
)
