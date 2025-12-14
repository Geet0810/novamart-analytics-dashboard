@echo off
REM NovaMart Analytics Dashboard Launcher
REM Double-click this file to run the dashboard

echo ============================================
echo   NovaMart Analytics Dashboard Launcher
echo ============================================
echo.
echo Starting Streamlit dashboard...
echo.

cd /d "%~dp0"

REM Run Streamlit using the virtual environment Python
.\.venv\Scripts\python.exe -m streamlit run app.py

pause
