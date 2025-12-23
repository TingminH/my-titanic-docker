from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)
CORS(app)  # 關鍵：允許跨網域存取，否則前端網頁會抓不到資料

def get_db_connection():
    # 這裡的資訊要對齊你的 .env 與 docker-compose 設定
    return mysql.connector.connect(
        host="db",          # 這是 docker-compose 中的服務名稱
        user="root",
        password=os.getenv("MYSQL_ROOT_PASSWORD"),
        database=os.getenv("MYSQL_DATABASE")
    )

@app.route('/api/passengers')
def get_passengers():
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True) # 以字典格式回傳，方便轉成 JSON
        cursor.execute("SELECT * FROM full_passengers LIMIT 20")
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # 必須設定為 0.0.0.0 才能讓容器外的請求進來
    app.run(host='0.0.0.0', port=5000)
