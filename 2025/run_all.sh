#!/bin/bash

SOL_DIR="solutions"
INPUT_DIR="inputs"
EXAMPLES_DIR="examples"

for pyfile in "$SOL_DIR"/*.py; do
    base=$(basename "$pyfile" .py)
    input_file="$INPUT_DIR/$base.txt"
    example_file="$EXAMPLES_DIR/$base.txt"

    if [[ -f "$input_file" ]]; then
        echo "Running $pyfile with example $input_file"
        python3 "$pyfile" "$example_file"
        echo "Running $pyfile with input $input_file"
        python3 "$pyfile" "$input_file"
        echo "----------------------------------------"
    else
        echo "Input file $input_file not found, skipping $pyfile."
    fi
done


