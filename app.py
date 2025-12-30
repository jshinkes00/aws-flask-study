from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>[로컬에서 수정함] [자동화 코딩 완료] 조아람 바보: {now}</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
