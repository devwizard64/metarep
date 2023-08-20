#!/bin/sh
set -e
SRC=UNSM
DST=unsm
python3 main.py $DST $SRC
# make -s -C $DST TARGET=J0
make -s -C $DST TARGET=E0
sha1sum -c $DST.sha1
