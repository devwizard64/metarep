#!/bin/sh
set -e
SRC=SAKF
DST=sakf
rm -rf $DST
cp -rf $SRC $DST
rm -rf $DST/__* $DST/*.pyc $DST/*.py
python3 main.py $DST $SRC
make --no-print-directory -C $DST -j$nproc VERSION=J0
make --no-print-directory -C $DST -j$nproc VERSION=E0
make --no-print-directory -C $DST -j$nproc VERSION=P0
sha1sum -c $DST.sha1
