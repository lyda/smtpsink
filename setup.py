#!/usr/bin/env python

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='smtpsink',
    version='0.0.1',
    license='GPLv3',
    description='An SMTP Sink with a Web UI.',
    long_description=open('README.md').read(),
    packages=['smtpsink'],
    author='Kevin Lyda',
    author_email='kevin@ie.suberic.net',
    install_requires=open('requirements.txt').read().split('\n')[:-1],
    url='http://github.com/lyda/smtpsink',
    keywords='smtp mail sink fake development test testing',
)
