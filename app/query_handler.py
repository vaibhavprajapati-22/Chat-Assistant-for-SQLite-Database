import sqlite3

DB_PATH = "../database/company.db"

def fetch_from_db(query, params=()):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    try:
        cursor.execute(query, params)
        result = cursor.fetchall()
    except sqlite3.Error as e:
        result = f"Database error: {str(e)}"
    
    conn.close()
    return result
