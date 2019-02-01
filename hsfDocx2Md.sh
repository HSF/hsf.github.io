#! /bin/bash

# Convert input docx files to markdown using pandoc and apply 
# a standard tidy up (or simply tidy the input markdown files).
# This is useful for converting Google Docs into HSF minutes.
# See https://hepsoftwarefoundation.org/jekyll-beginners.html.

# Pandoc recipe by Michel Jouvin and Graeme Stewart (2016-2018).
# Python tidy up script by Graeme Stewart (2018).
# Bash wrapper and python conversion to sed by Andrea Valassi (2019).

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

if ! sed --version >& /dev/null; then 
  echo "ERROR! sed not found"
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

\cp -dp ${file}.md ${file}.md.bak1
mac2unix ${file}.md >& /dev/null

#echo Converting ${file}.md to unix format using dos2unix

\cp -dp ${file}.md ${file}.md.bak2
dos2unix ${file}.md >& /dev/null

#echo Tidying up ${file}.md using sed

\cp -dp ${file}.md ${file}.md.bak3
cat ${file}.md.bak3 \
  | sed 's/{\.underline}//g' \
  | sed 's/\[\[/[/g' \
  | sed 's/\]\]/]/g' \
  | sed 's/^\( \+\)> /\1/g' \
  | sed 's/^\( \+\)- > /\1- /g' \
  | sed '/^ *$/d' \
  > ${file}.md

# Remove bak files

\rm ${file}.md.bak*
