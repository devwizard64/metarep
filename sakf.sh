#!/bin/sh
set -e
SRC=SAKF
DST=sakf
rm -rf $DST
cp -rf $SRC $DST
rm -rf $DST/__* $DST/*.pyc $DST/*.py
python3 main.py $DST $SRC
make -C $DST VERSION=J0
make -C $DST VERSION=E0
make -C $DST VERSION=P0
sha1sum -c $DST.sha1
