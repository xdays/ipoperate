#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from distutils.core import setup
import ipopt

setup(
    name='ipopt',
    version=ipopt.__VERSION__,
    description='magic functions to operate ips and nets',
    license='License :: OSI Approved :: MIT License',
    platforms='Platform Independent',
    author='Alair Zhang (xdays)',
    author_email='easedays@gmail.com',
    url='http://www.xdays.info',
    packages=['ipopt'],
    keywords=['ipopt', 'ip2net', 'nets2net', 'ip2bin'],
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
) 
