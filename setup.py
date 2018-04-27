"""setup.py file."""
import re
from codecs import open
from glob import glob
from setuptools import setup
import os
import shutil

version = ''
with open('ntc_templates/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Cannot find version information')

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()


long_description = readme + '\n\n' + history


template_files = glob('templates/*')

if os.path.islink('ntc_templates/templates'):
    os.unlink('ntc_templates/templates')
elif os.path.isdir('ntc_templates/templates'):
    shutil.rmtree('ntc_templates/templates')

os.symlink('../templates', 'ntc_templates/templates')
config = {
    'name': 'ntc_templates',
    # 'package_dir': {'': 'lib'},
    'packages': ['ntc_templates'],
    'version': version,
    'package_data': {'ntc_templates': template_files},
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
                    'Programming Language :: Python :: 2.7']
}

setup(**config)

if os.path.islink('ntc_templates/templates'):
    os.unlink('ntc_templates/templates')
