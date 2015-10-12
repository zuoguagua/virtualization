#!/usr/bin/env python

import sys
import os

absdir = os.path.abspath(".")

print absdir
dirname = os.path.join(absdir,"utils")

print dirname

sys.path.append(dirname)

