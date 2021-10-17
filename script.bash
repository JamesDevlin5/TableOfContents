#!/usr/bin/env bash

if [[ $# -lt 1 ]]; then
    echo "No input file given!"
    exit 1
fi

TARGET_FILE="$1"

rg -N -e '^#{1,6}.*' "$TARGET_FILE" | tr '#' ' '

