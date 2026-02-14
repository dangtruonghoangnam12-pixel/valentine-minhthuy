# 💝 Món Quà Valentine Cho Minh Thùy - Python Version

Ứng dụng web Valentine lãng mạn được viết bằng Python với Streamlit và Google Gemini AI.

## ✨ Tính năng

- 🎁 Giao diện mở quà Valentine đẹp mắt
- 🤖 Tạo lời nhắn yêu thương tự động bằng AI (Google Gemini)
- 💖 Hiệu ứng animation và màu sắc lãng mạn
- 🎨 Giao diện responsive, dễ sử dụng
- ❤️ Đếm số lần "Thương"

## 📋 Yêu cầu

- Python 3.8 trở lên
- Google Gemini API Key (miễn phí tại [Google AI Studio](https://makersuite.google.com/app/apikey))

## 🚀 Cài đặt

### 1. Clone hoặc tải project về

```bash
cd valentine_python
```

### 2. Tạo môi trường ảo (khuyến nghị)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Cài đặt các thư viện cần thiết

```bash
pip install -r requirements.txt
```

### 4. Cấu hình API Key

Tạo file `.env` trong thư mục gốc và thêm API key của bạn:

```bash
# Copy file mẫu
cp .env.example .env
```

Sau đó mở file `.env` và thêm API key:

```
GEMINI_API_KEY=your_actual_api_key_here
```

**Lấy API Key:**
1. Truy cập [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Đăng nhập bằng tài khoản Google
3. Nhấn "Create API Key"
4. Copy API key và dán vào file `.env`

## ▶️ Chạy ứng dụng

```bash
streamlit run app.py
```

Ứng dụng sẽ tự động mở trong trình duyệt tại `http://localhost:8501`

## 🎯 Sử dụng

1. Mở ứng dụng trong trình duyệt
2. Nhấn nút "Mở quà ngay 💖"
3. Chờ AI tạo lời nhắn yêu thương
4. Nhấn "Thương" để tăng số lần thương
5. Nhấn "Gửi lại" để tạo lời nhắn mới

## 📁 Cấu trúc thư mục

```
valentine_python/
│
├── app.py                 # File chính của ứng dụng
├── requirements.txt       # Các thư viện Python cần thiết
├── .env.example          # Mẫu file cấu hình
├── .env                  # File cấu hình (không commit)
├── .gitignore           # File gitignore
└── README.md            # File hướng dẫn này
```

## 🎨 Tùy chỉnh

### Thay đổi tên người nhận

Mở file `app.py` và tìm dòng:

```python
st.session_state.ai_message = generate_love_message("Minh Thùy")
```

Thay "Minh Thùy" thành tên bạn muốn.

### Thay đổi màu sắc

Chỉnh sửa phần CSS trong file `app.py` (dòng 24-135)

### Thay đổi nội dung lời nhắn

Chỉnh sửa hàm `generate_love_message()` trong file `app.py`

## 🔧 VSCode Setup

### 1. Cài đặt Python extension

Trong VSCode, cài đặt extension:
- Python (Microsoft)
- Python Debugger (Microsoft)

### 2. Chọn Python Interpreter

1. Nhấn `Ctrl+Shift+P` (Windows/Linux) hoặc `Cmd+Shift+P` (Mac)
2. Gõ "Python: Select Interpreter"
3. Chọn interpreter từ môi trường ảo (venv)

### 3. Debug Configuration

Tạo file `.vscode/launch.json`:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Streamlit",
            "type": "python",
            "request": "launch",
            "module": "streamlit",
            "args": [
                "run",
                "app.py"
            ]
        }
    ]
}
```

## 🐛 Xử lý lỗi thường gặp

### Lỗi: "GEMINI_API_KEY not found"
- Đảm bảo đã tạo file `.env` với API key đúng

### Lỗi: "Module not found"
- Chạy lại: `pip install -r requirements.txt`

### Lỗi: Port 8501 đã được sử dụng
- Chạy: `streamlit run app.py --server.port 8502`

## 📝 License

Free to use for personal purposes. Made with ❤️

## 👤 Author

Made with love for Minh Thùy 💕

---

**Happy Valentine's Day! 🌹💖**
