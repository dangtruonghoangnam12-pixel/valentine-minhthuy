@echo off
echo ================================
echo    Valentine App - Starting
echo ================================
echo.

REM Kiểm tra môi trường ảo
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
    echo.
)

REM Kích hoạt môi trường ảo
echo Activating virtual environment...
call venv\Scripts\activate.bat
echo.

REM Cài đặt dependencies
echo Installing dependencies...
pip install -r requirements.txt
echo.

REM Kiểm tra file .env
if not exist ".env" (
    echo WARNING: .env file not found!
    echo Please create .env file with your GEMINI_API_KEY
    echo Copying .env.example to .env...
    copy .env.example .env
    echo.
    echo Please edit .env file and add your API key, then run this script again.
    pause
    exit
)

REM Chạy ứng dụng
echo Starting Valentine App...
echo.
echo App will open in your browser at http://localhost:8501
echo Press Ctrl+C to stop the app
echo.
streamlit run app.py

pause
