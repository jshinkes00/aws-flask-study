from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>[로컬에서 수정함] 현재 서버 시간: {now}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
