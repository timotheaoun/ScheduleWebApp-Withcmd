cd /d "%~dp0"
start "" /min "Starter.bat"
start "" agent.py
python -m http.server 8000
python -m http.server 8080
