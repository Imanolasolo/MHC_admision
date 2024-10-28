import sqlite3

def clear_users():
    conn = sqlite3.connect('hospital.db')
    c = conn.cursor()
    c.execute('DELETE FROM users')
    conn.commit()
    conn.close()

clear_users()
