#!/bin/bash

# check if python installed
if ! command -v python3 &> /dev/null; then
    exit 1
fi

# install
python3 -m pip install -r requirements.txt
