@echo off
REM Check if miktex-portable.exe exists
if not exist "miktex-portable.exe" (
    echo miktex.exe not found. Please ensure it is in the same directory as this script.
    pause
    exit /b
)

REM Run the MiKTeX installer with silent mode
echo Starting MiKTeX installation...
miktex-portable.exe --unattended
if %errorlevel% neq 0 (
    echo Installation failed with error code %errorlevel%.
    pause
    exit /b
)

echo MiKTeX installed successfully.
pause
