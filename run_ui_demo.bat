@echo off
setlocal

echo Installing dependencies...
python -m pip install -r requirements.txt
if errorlevel 1 goto :error

echo Running tests and generating themed report...
python -m pytest
if errorlevel 1 goto :error

echo Opening UI pages...
start "" "ui\index.html"
start "" "ui\report.html"
echo Done.
exit /b 0

:error
echo.
echo Something failed. Please check the logs above.
exit /b 1
