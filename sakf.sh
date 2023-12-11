#!/bin/sh
set -e
SRC=SAKF
DST=sakf
python3 main.py $SRC $DST
make -s -C $DST TARGET=J0
make -s -C $DST TARGET=J1
# make -s -C $DST TARGET=J2
# make -s -C $DST TARGET=E0
# make -s -C $DST TARGET=P0
sha1sum -c $DST.sha1
