@echo off

:: Define the name of the virtual environment directory
set VENV_DIR=venv

:: Check if virtual environment directory exists
if exist %VENV_DIR% (
    echo Virtual environment already exists.
) else (
    :: Create a virtual environment
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
)

:: Activate the virtual environment
echo Activating virtual environment...
call %VENV_DIR%\Scripts\activate

:: Upgrade pip and setuptools
echo Upgrading pip and setuptools...
pip install --upgrade pip setuptools

:: Install required packages
echo Installing required packages...
pip install -r requirements.txt

echo Setup completed successfully.
