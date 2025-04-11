# Sử dụng Python base image
FROM python:3.10-slim

# Tạo thư mục làm việc
WORKDIR /app

# Copy code vào container
COPY app/ ./app/
COPY requirements.txt .

# Cài thư viện
RUN pip install --no-cache-dir -r requirements.txt

# Tạo thư mục lưu ảnh
RUN mkdir -p /app/data/images

# Lệnh mặc định khi container khởi chạy
CMD ["python", "app/save.py"]
