import os
import psycopg2

def init_db():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS games (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        release_date DATE NOT NULL,
        genre VARCHAR(50) NOT NULL
    )
    ''')
    conn.commit()
    cur.close()
    conn.close()

def insert_game(name, release_date, genre):
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    cur = conn.cursor()
    cur.execute(
        'INSERT INTO games (name, release_date, genre) VALUES (%s, %s, %s)',
        (name, release_date, genre)
    )
    conn.commit()
    cur.close()
    conn.close()

def get_games():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    cur = conn.cursor()
    cur.execute('SELECT id, name, release_date, genre FROM games')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": row[0], "name": row[1], "release_date": row[2], "genre": row[3]} for row in rows]
