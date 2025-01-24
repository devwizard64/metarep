#!/bin/sh
set -e
SRC=HMA
DST=hma
python3 main.py $SRC $DST
make -s -C $DST
sha1sum -c $DST.sha1
