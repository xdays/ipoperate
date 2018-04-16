#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup
import ipoperate
import os


setup(
    name='ipoperate',
    version=ipoperate.__VERSION__,
    description='magic functions to operate ips and nets',
    long_description = open('README.md').read(),
    long_description_content_type='text/markdown',
    license='License :: OSI Approved :: MIT License',
    platforms='Platform Independent',
    author='Alair Zhang (xdays)',
    author_email='easedays@gmail.com',
    url='http://xdays.me',
    packages=['ipoperate'],
    keywords=['ipoperate', 'ip2net', 'nets2net', 'ip2bin'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    scripts=['bin/iprange']
) 
