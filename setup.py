"""setup.py file."""
from ntc_templates import __version__
from codecs import open
from setuptools import setup

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

long_description = readme + '\n\n' + history

config = {
    'name': 'ntc_templates',
    'packages': ['ntc_templates'],
    'version': __version__,
    'package_data': {'ntc_templates': ['templates/*']},
    'description': 'Package to return structured data from the output of network devices.',
    'long_description': long_description,
    'author': 'network.toCode()',
    'author_email': 'info@networktocode.com',
    'url': 'https://github.com/networktocode/ntc-templates',
    'install_requires': [
        'textfsm',
        'terminal',
    ],
    'classifiers': ['Development Status :: 4 - Beta',
                    'Intended Audience :: Developers',
                    'Intended Audience :: System Administrators',
                    'Programming Language :: Python :: 2.7'],
    'zip_safe': False
}

setup(**config)
