#! /bin/bash

# Convert input docx files to markdown using pandoc and apply 
# a standard tidy up (or simply tidy the input markdown files).
# This is useful for converting Google Docs into HSF minutes.
# See https://hepsoftwarefoundation.org/jekyll-beginners.html.

# Pandoc recipe by Michel Jouvin and Graeme Stewart (2016-2018).
# Python tidy up script by Graeme Stewart (2018).
# Bash wrapper by Andrea Valassi (2019).

function usage()
{
  echo "Usage: $(basename $0) <file>.docx"
  echo "       to convert <file>.docx to <file>.md and tidy it up"
  echo ""
  echo "Usage: $(basename $0) <file>.md"
  echo "       to tidy up <file>.md"
  exit 1
}

#
# Check input parameters
#

if [ "$1" == "" ] || [ "$2" != "" ]; then

  usage

elif [ "${1%.docx}" != "$1" ]; then

  docx=1
  file=${1%.docx}
  if [ ! -f ${file}.docx ]; then
    echo "ERROR! ${file}.docx not found"
    exit 1
  fi

elif [ "${1%.md}" != "$1" ]; then

  docx=0
  file=${1%.md}
  if [ ! -f ${file}.md ]; then
    echo "ERROR! ${file}.md not found"
    exit 1
  fi

else

  usage

fi

#
# Check installed packages
#

if [ "$docx" == "1" ]; then
  if ! pandoc -v > /dev/null; then 
    echo "ERROR! pandoc not found"
    exit 1
  elif [ "$(pandoc --version | grep ^pandoc)" != "pandoc 2.5" ]; then
    echo "ERROR! this script requires pandoc 2.5"
    exit 1
  fi
fi

if ! mac2unix -V >& /dev/null; then 
  echo "ERROR! mac2unix not found"
  exit 1
fi

if ! dos2unix -V >& /dev/null; then 
  echo "ERROR! dos2unix not found"
  exit 1
fi

if ! python -V >& /dev/null; then 
  echo "ERROR! python not found"
  exit 1
fi

#
# Convert docx to md
#

if [ "$docx" == "1" ]; then

  #echo Converting ${file}.docx to ${file}.md using pandoc

  pandoc -t gfm --base-header-level=2 --atx-header -o ${file}.md ${file}.docx

fi

#
# Tidy up md
#

#echo Converting ${file}.md to unix format using mac2unix

mac2unix ${file}.md >& /dev/null

#echo Converting ${file}.md to unix format using dos2unix

dos2unix ${file}.md >& /dev/null

#echo Tidying up ${file}.md using python

python - ${file}.md <<EOF
from __future__ import print_function 
import argparse
import os
import re
import sys
relist = [
    [r'\{\.underline\}', ''],
    [r'\[\[', '['],
    [r'\]\]', ']'],
    [r'^(\s+)> ', '\g<1>'],
    # This gets rid of a lot of excess space, but some do need to 
    # put back (before section headers), but doing that properly
    # would be complicated...
    [r'^(\s+)$', ''],
    ]
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input', help='Input file to process')
    parser.add_argument('--backup', help='Backup filename for original file (default is INPUTNAME.bak)')
    options = parser.parse_args()
    if options.backup == None:
        options.backup = options.input + '.bak'
    os.rename(options.input, options.backup)
    with open(options.backup) as filein, open(options.input, 'w') as fileout:
        for line in filein:
            try:
                for regexpair in relist:
                    line = re.sub(regexpair[0], regexpair[1], line)
                print(line, end='', file=fileout)
            except Exception as e:
                print('Exception raised processing \'{0}\': {1}', line, e)
if __name__ == '__main__':
    main()
 
EOF

#echo Tidying up ${file}.md using sed

\mv ${file}.md ${file}.md.bak

cat ${file}.md.bak | sed "s/ - > / - /" > ${file}.md

\rm ${file}.md.bak

