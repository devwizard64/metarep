#!/bin/sh
set -e
SRC=SAKF
DST=sakf
python3 main.py $DST $SRC
make -C $DST -s VERSION=J0
make -C $DST -s VERSION=E0
make -C $DST -s VERSION=P0
sha1sum -c $DST.sha1
