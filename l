#!/bin/bash

DIR="$(dirname "$(which "$0")")"
OUTPUT="$(python $DIR/dict.py $1)"
EXITCODE=$?
echo "$OUTPUT" | more

if [ $EXITCODE != 0 ]; then
  exit 1;
fi
