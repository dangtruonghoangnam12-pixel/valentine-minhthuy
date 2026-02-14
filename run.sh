#!/bin/bash

echo "================================"
echo "   Valentine App - Starting"
echo "================================"
echo ""

# Kiểm tra môi trường ảo
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo ""
fi

# Kích hoạt môi trường ảo
echo "Activating virtual environment..."
source venv/bin/activate
echo ""

# Cài đặt dependencies
echo "Installing dependencies..."
pip install -r requirements.txt
echo ""

# Kiểm tra file .env
if [ ! -f ".env" ]; then
    echo "WARNING: .env file not found!"
    echo "Please create .env file with your GEMINI_API_KEY"
    echo "Copying .env.example to .env..."
    cp .env.example .env
    echo ""
    echo "Please edit .env file and add your API key, then run this script again."
    exit 1
fi

# Chạy ứng dụng
echo "Starting Valentine App..."
echo ""
echo "App will open in your browser at http://localhost:8501"
echo "Press Ctrl+C to stop the app"
echo ""
streamlit run app.py
