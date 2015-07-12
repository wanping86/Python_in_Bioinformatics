#!/usr/local/bin/env python3.4
# 2015-7-12

import re

pattern = re.compile(r'hello')
match = pattern.match('hello world!')
if match:
	print (match.group())

### output ###
# hello