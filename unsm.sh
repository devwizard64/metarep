#!/bin/sh
set -e
SRC=UNSM
DST=unsm
python3 main.py $SRC $DST
# make -s -C $DST TARGET=J0
make -s -C $DST TARGET=E0
# make -s -C $DST TARGET=DD
# make -s -C $DST TARGET=G0
sha1sum -c $DST.sha1
