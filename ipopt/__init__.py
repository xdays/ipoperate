#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
__VERSION__ = '0.1' 
__AUTHOR__ = 'xdays'

try:
    from .ipopt import *
except:
    error = 'import error'
