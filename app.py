from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    # DB에서 글 다 긁어오기
    cur = conn.cursor()
    cur.execute('SELECT * FROM guests ORDER BY id DESC')
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

@app.route('/add', methods=['POST'])
def add_guest():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        
        # DB에 저장하기
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO guests (name, message) VALUES (?, ?)", (name, message))
        conn.commit()
        conn.close()
        
        return redirect(url_for('index'))


@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # sql 핵심 guests 테이블에서 id가 일치하는 행을 지워라
    c.execute('DELETE FROM guests WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    # 지우고 나면 다시 방명록 메인 화면으로 이동
    return redirect('/')



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)