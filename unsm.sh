#!/bin/sh
set -e
SRC=UNSM
DST=unsm
rm -rf $DST
cp -rf $SRC $DST
rm -rf $DST/__* $DST/*.pyc $DST/*.py $DST/exe/__* $DST/exe/*.pyc
python3 main.py $DST $SRC
# make -C $DST VERSION=J0
make -C $DST VERSION=E0
sha1sum -c $DST.sha1
