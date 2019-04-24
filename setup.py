import re
from codecs import open
from setuptools import setup, find_packages

version = ''
with open('lib/ntc_templates/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

long_description = readme + '\n\n' + history

config = {
    'name': 'ntc_templates',
    'package_dir': {'': 'lib'},
    'packages': find_packages('lib'),
    'version': version,
    'package_data': {'ntc_templates': ['templates/*']},
    'description': 'Package to return structured data from the output of network devices.',
    'long_description': long_description,
    'long_description_content_type': 'text/markdown',
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
                    'Programming Language :: Python :: 3'],
    'zip_safe': False
}

setup(**config)
