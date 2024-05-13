#!/bin/bash

# Define the name of the virtual environment directory
VENV_DIR="venv"

# Check if virtual environment directory exists
if [ -d "$VENV_DIR" ]; then
    echo "Virtual environment already exists."
else
    # Create a virtual environment
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# Activate the virtual environment
echo "Activating virtual environment..."
source $VENV_DIR/bin/activate

# Upgrade pip and setuptools
echo "Upgrading pip and setuptools..."
pip install --upgrade pip setuptools

# Install required packages
echo "Installing required packages..."
pip install -r requirements.txt

echo "Setup completed successfully."
