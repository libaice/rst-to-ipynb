"""
WHAT THIS FILE DOES:
    converts an RST file to a .ipynb file
HOW THIS FILE WORKS:
    1. calls pandoc to convert between .rst and .md
    2. calls notedown to convert between .md and .ipynb
TODO:
    * properly parse command line args (escape chars etc)
    * Features notedown needs:
        * figure emedding
        * unicode
DEPS:
    * [notedown], [pandoc]

[notedown]:https://github.com/aaren/notedown
[pandoc]:http://pandoc.org
"""

import io
import os
pjoin = os.path.join
import sys
from subprocess import Popen, PIPE
import argparse


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument("input_file", nargs='?', help="the input .rst file. Include the .rst")
parser.add_argument("output_file", help="the .ipynb output file. Include .ipynb")
args = parser.parse_args()

here = os.path.dirname(__file__)

if args.input_file:
    input_text = io.open(args.input_file).read()
else:
    input_text = sys.stdin.read()
input_text = '\n'.join([
    # add default-role: math for sage rst
    '.. default-role:: math',
    input_text])
# pandoc doesn't properly handle : immediately-following close-`
input_text = input_text.replace('`:', '` :')

# convert rst->markdown with pandoc
p = Popen([
        'pandoc',
        '--filter', pjoin(here, 'sageblockfilter.py'),
        '--atx-headers',
        '--from', 'rst',
        '--to', 'markdown',
    ], stdout=PIPE, stdin=PIPE)

intermediate_md, _ = p.communicate(input_text.encode('utf8'))

if p.returncode:
    sys.exit("pandoc failed: %s" % p.returncode)

intermediate_md = intermediate_md.decode('utf8', 'replace')

# define some math macros for mathjax
intermediate_md = '\n'.join([
    # add some sage-defined macros:
    '$$',
    r'\def\CC{\bf C}',
    r'\def\QQ{\bf Q}',
    r'\def\RR{\bf R}',
    r'\def\ZZ{\bf Z}',
    '$$',
    intermediate_md])

# write intermediate markdown for debugging:
# with open('tmp.md', 'wb') as f:
#     f.write(intermediate_md)

# md->ipynb via notedown
p = Popen([
    'notedown', '-o', args.output_file,
], stdin=PIPE)
p.communicate(intermediate_md.encode('utf8'))
if p.returncode:
    sys.exit("notedown failed: %s" % p.returncode)
