#!/bin/sh
set -e
SRC=SAKF
DST=sakf
python3 main.py $DST $SRC
make -s -C $DST VERSION=J00
make -s -C $DST VERSION=E00
make -s -C $DST VERSION=P00
sha1sum -c $DST.sha1
