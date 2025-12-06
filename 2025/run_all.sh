#!/bin/bash

# Directory containing Python solutions
SOL_DIR="solutions"
# Directory containing input files
INPUT_DIR="inputs"

# Loop over all Python files in the solutions directory
for pyfile in "$SOL_DIR"/*.py; do
    # Extract the base name without extension
    base=$(basename "$pyfile" .py)
    # Construct corresponding input file path
    input_file="$INPUT_DIR/$base.txt"

    # Check if input file exists
    if [[ -f "$input_file" ]]; then
        echo "Running $pyfile with input $input_file..."
        python3 "$pyfile" "$input_file"
        echo "----------------------------------------"
    else
        echo "Input file $input_file not found, skipping $pyfile."
    fi
done


