#!/bin/bash

DIR="$(dirname "$(which "$0")")"
python $DIR/dict.py $1
