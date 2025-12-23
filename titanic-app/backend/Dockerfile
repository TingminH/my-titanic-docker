# 1. 基礎鏡像 (基礎環境)
FROM python:3.11-slim

# 2. 設定容器內部的工作目錄 (就像進到容器後的 cd /app)
WORKDIR /app

# 3. 安裝連線 MySQL 所需的 Python 套件
# 這些會被燒錄進 Image 的第二層
RUN pip install --no-cache-dir flask flask-cors mysql-connector-python

# 4. 把你寫好的 app.py 複製進去
# 這會被燒錄進 Image 的最上層
COPY app.py .

# 5. 告訴系統這台機器預計對外開放 5000 埠
EXPOSE 5000

# 6. 當容器啟動時，最後要執行的指令
CMD ["python", "app.py"]
