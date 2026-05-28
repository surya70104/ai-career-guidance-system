from database import conn, cursor


def register_user(name, email, password):

    try:

        cursor.execute("""
        INSERT INTO users(
            name,
            email,
            password
        )
        VALUES(?,?,?)
        """, (
            name,
            email,
            password
        ))

        conn.commit()

        return True

    except:

        return False


def login_user(email, password):

    cursor.execute("""
    SELECT * FROM users
    WHERE email=? AND password=?
    """, (
        email,
        password
    ))

    user = cursor.fetchone()

    return user