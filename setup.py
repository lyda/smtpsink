#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import smtpsinkd

setup(
    name='smtpsink',
    version=smtpsinkd.VERSION,
    license='GPLv3',
    description='An SMTP Sink with a Web UI.',
    long_description=open('README.md').read(),
    scripts=['smtpsinkd.py'],
    author='Kevin Lyda',
    author_email='kevin@ie.suberic.net',
    install_requires=open('requirements.txt').read().split('\n')[:-1],
    url='http://github.com/lyda/smtpsink',
    keywords='smtp mail sink fake development test testing',
)
