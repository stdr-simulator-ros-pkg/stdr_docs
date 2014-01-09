#!/usr/bin/env python
'''
script for generating documentation automatically
using rosdoc_lite, given a collection of ros packages

USAGE: ./generate_doc.py <path_to_root_of_pkgs> <output dir>

Author: Chris Zalidis
'''
import os
import sys

root_dir = str(sys.argv[1])

dirnames = os.walk(root_dir).next()[1]

if '.git' in dirnames:
  dirnames.remove('.git')

out = str(sys.argv[2])

if not os.path.isdir(out):
  os.mkdir(out)

rosdoc = 'rosdoc_lite '

for package in dirnames:
  cmd = rosdoc + '-o ' + os.path.join(out, package) + ' ' + os.path.abspath(os.path.join(root_dir, package))
  print cmd
  os.system(cmd)
