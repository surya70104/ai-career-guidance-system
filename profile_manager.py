from database import conn, cursor


def update_profile(
    email,
    phone,
    linkedin,
    github,
    location,
    college,
    degree,
    skills,
    objective,
    projects,
    certifications,
    avatar
):

    cursor.execute("""
    UPDATE users
    SET
        phone=?,
        linkedin=?,
        github=?,
        location=?,
        college=?,
        degree=?,
        skills=?,
        objective=?,
        projects=?,
        certifications=?,
        avatar=?
    WHERE email=?
    """, (
        phone,
        linkedin,
        github,
        location,
        college,
        degree,
        skills,
        objective,
        projects,
        certifications,
        avatar,
        email
    ))

    conn.commit()


def get_profile(email):

    cursor.execute("""
    SELECT
        phone,
        linkedin,
        github,
        location,
        college,
        degree,
        skills,
        objective,
        projects,
        certifications,
        avatar
    FROM users
    WHERE email=?
    """, (email,))

    return cursor.fetchone()