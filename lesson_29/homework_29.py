import os
import psycopg2


def get_conn():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )


def setup_module(module):
    """Создание таблицы при старте"""
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT,
            email TEXT
        )
    """)
    conn.commit()
    conn.close()


def test_insert_user():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", ("Alice", "alice@example.com"))
    conn.commit()
    cur.execute("SELECT * FROM users WHERE name = %s", ("Alice",))
    result = cur.fetchone()
    assert result is not None
    conn.close()


def test_update_user():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE users SET email = %s WHERE name = %s", ("newalice@example.com", "Alice"))
    conn.commit()
    cur.execute("SELECT email FROM users WHERE name = %s", ("Alice",))
    email = cur.fetchone()[0]
    assert email == "newalice@example.com"
    conn.close()


def test_delete_user():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE name = %s", ("Alice",))
    conn.commit()
    cur.execute("SELECT * FROM users WHERE name = %s", ("Alice",))
    result = cur.fetchone()
    assert result is None
    conn.close()
