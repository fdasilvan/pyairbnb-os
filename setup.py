from setuptools import setup

VERSION = '0.0.1'
DESCRIPTION = 'Airbnb scraper in Python'

setup(
    name="pyairbnb-os",
    version=VERSION,
    author="Adalberto (original author: John Balvin)",
    author_email="<heyadalberto@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    url='https://github.com/fdasilvan/pyairbnb-os',
    long_description=open('README.md').read(),
    keywords=['airbnb', 'scraper', 'crawler','bot','reviews'],
    install_requires=['curl_cffi','bs4'],
)