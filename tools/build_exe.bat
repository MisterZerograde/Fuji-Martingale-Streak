@echo off
echo.
echo ===========================================
echo   BUILDING FUJI MARTINGALE STREAK EXE
echo ===========================================
echo.
echo 1. Cleaning up old builds...
if exist dist del /q dist\*
if exist build del /q build\*

echo 2. Compiling into a single hidden EXE...
pyinstaller --onefile --noconsole --name "FujiStreak" fuji_app.py

echo.
echo ===========================================
echo   SUCCESS! Your EXE is in the 'dist' folder.
echo ===========================================
pause
