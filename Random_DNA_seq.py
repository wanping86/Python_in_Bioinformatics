#!/usr/local/bin/env python3.4
# 2015-7-25

import random

seq = ''

for i in range(0,100,1):
	base = (''.join(random.sample(['a','c','t','g'], 1)))
	seq = seq + base

print (seq)
