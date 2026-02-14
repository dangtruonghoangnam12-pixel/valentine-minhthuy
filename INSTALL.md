# 🚀 Hướng Dẫn Cài Đặt Nhanh

## ⚡ Cách 1: Sử dụng Script Tự Động (Khuyến nghị)

### Windows:
```bash
# Chỉ cần double-click file run.bat
# Hoặc chạy trong terminal:
run.bat
```

### macOS/Linux:
```bash
# Chạy trong terminal:
chmod +x run.sh
./run.sh
```

Script sẽ tự động:
- ✅ Tạo môi trường ảo Python
- ✅ Cài đặt tất cả thư viện cần thiết
- ✅ Kiểm tra file cấu hình
- ✅ Chạy ứng dụng

## 📝 Cách 2: Cài Đặt Thủ Công

### Bước 1: Tạo môi trường ảo

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Bước 2: Cài đặt thư viện

```bash
pip install -r requirements.txt
```

### Bước 3: Cấu hình API Key

1. Copy file mẫu:
```bash
cp .env.example .env
```

2. Mở file `.env` và thêm API key của bạn:
```
GEMINI_API_KEY=your_api_key_here
```

**Lấy API Key miễn phí tại:** https://makersuite.google.com/app/apikey

### Bước 4: Chạy ứng dụng

```bash
streamlit run app.py
```

## 🎯 Mở trong VSCode

1. Mở folder trong VSCode:
```bash
code .
```

2. Chọn Python interpreter (Ctrl/Cmd + Shift + P):
   - Gõ: "Python: Select Interpreter"
   - Chọn: `./venv/bin/python`

3. Chạy/Debug:
   - Nhấn F5 hoặc vào menu Run > Start Debugging
   - Chọn configuration "Streamlit: Run App"

## ❓ Xử Lý Lỗi

### Lỗi: "python not found"
- Cài đặt Python 3.8+ từ https://www.python.org/downloads/

### Lỗi: "pip not found"
- Windows: `python -m ensurepip --upgrade`
- macOS/Linux: `python3 -m ensurepip --upgrade`

### Lỗi: "GEMINI_API_KEY not found"
- Đảm bảo đã tạo file `.env` và thêm API key

### Lỗi: "Port 8501 already in use"
- Chạy: `streamlit run app.py --server.port 8502`

## 📞 Cần Giúp Đỡ?

Nếu gặp vấn đề, hãy kiểm tra:
1. ✅ Python đã cài đặt đúng chưa: `python --version`
2. ✅ Môi trường ảo đã được kích hoạt chưa
3. ✅ File `.env` có API key chưa
4. ✅ Tất cả thư viện đã cài đặt: `pip list`

---

**Chúc bạn thành công! 💖**
