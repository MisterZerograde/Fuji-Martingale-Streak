@echo off
setlocal enabledelayedexpansion
echo.
echo ===========================================
echo   BUILDING FUJI MARTINGALE STREAK EXE
echo ===========================================
echo.

echo 1. Updating application logic from UI source...
python prebuild.py
if !errorlevel! neq 0 (
    echo Error during prebuild phase.
    pause
    exit /b !errorlevel!
)

echo 2. Cleaning up old builds...
cd ..
if exist dist rd /s /q dist
if exist build rd /s /q build

echo 3. Compiling into a single EXE...
pyinstaller --onefile --noconsole --name "FujiStreak" app/src/main.py

echo.
echo ===========================================
echo   SUCCESS! Your EXE is in the 'dist' folder.
echo ===========================================
pause

