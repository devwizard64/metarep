#!/bin/sh
set -e
SRC=UNSM
DST=unsm
python3 main.py $DST $SRC
# make -s -C $DST VERSION=J0
make -s -C $DST VERSION=E0
sha1sum -c $DST.sha1
