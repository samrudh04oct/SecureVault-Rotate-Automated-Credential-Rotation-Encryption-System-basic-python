@echo off
setlocal

echo [1/3] Setting up virtual environment...
if not exist "venv" (
    python -m venv venv
)

echo [2/3] Installing dependencies...
call venv\Scripts\activate
pip install -r requirements.txt

echo [3/3] Starting Secure Vault Manager...
python gui.py

pause
