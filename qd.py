#!/usr/bin/env python

import quopri
import argparse
import codecs
import fileinput

s = ''
for line in fileinput.input():
    s += line

quoted_text = s

decoded = quopri.decodestring(quoted_text)
decoded = decoded.replace('\r\n', '\n');

print decoded
