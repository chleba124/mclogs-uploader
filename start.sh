#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    exit 1
fi

# Run main.py
python3 main.py
