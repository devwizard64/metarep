#!/bin/sh
set -e
SRC=SAKF
DST=sakf
python3 main.py $DST $SRC
make -s -C $DST TARGET=J00
make -s -C $DST TARGET=E00
make -s -C $DST TARGET=P00
sha1sum -c $DST.sha1
