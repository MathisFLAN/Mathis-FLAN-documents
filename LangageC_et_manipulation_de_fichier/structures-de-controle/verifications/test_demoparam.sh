#!/bin/bash

reference=$1
shift

TMP_DIR=~/tmp
mkdir -p "$TMP_DIR"

./demoparam.sh "$@" > "$TMP_DIR/sortie_test"

if diff "$reference" "$TMP_DIR/sortie_test" > /dev/null
then
    echo "OK"
    exit 0
else
    echo "FAIL"
    exit 1
fi
