@echo off
REM filepath: c:\Users\veikk\Documents\GitHub\Ufotutkija-Pekka\Start_initialize_game.bat

REM Initialize database
echo Initializing the ufo_peli database...
cd C:\Users\veikk\Documents\GitHub\Ufotutkija-Pekka
mariadb -u root -p1234 --database=ufo_peli < "%~dp0C:\Users\veikk\Documents\GitHub\Ufotutkija-Pekka\ufo_peli.sql" 2>nul

if %errorlevel% neq 0 (
    echo Database initialization failed. Possible reasons:
    echo 1. MariaDB not in system PATH
    echo 2. Incorrect root password
    echo 3. Missing ufo_peli.sql file or incorrect path
    pause
    exit /b
)

echo Database initialized successfully.

REM Launch game
echo Starting game...
py "C:\Users\veikk\Documents\GitHub\Ufotutkija-Pekka\Source\game.py"

if %errorlevel% neq 0 (
    echo Game failed to start. Verify:
    echo 1. Python 3.6+ installed
    echo 2. Required packages installed (check requirements.txt)
    echo 3. Game files in Source\ directory
    pause
    exit /b
)

pause
