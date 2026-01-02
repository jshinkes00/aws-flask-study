import sqlite3

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    # guests라는 테이블이 없으면 만들어라 (이름, 내용 저장)
    c.execute('''
        CREATE TABLE IF NOT EXISTS guests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
    print("DB 초기화 완료! database.db 파일이 생성되었습니다.")

if __name__ == '__main__':
    init_db()