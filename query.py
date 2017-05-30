import config
from datetime import datetime
import common


def five_latest_questions():
    query = """SELECT * FROM question ORDER BY submission_time DESC
            LIMIT 5;"""
    return config.run_query(query)


def all_question():
    query = """SELECT * FROM question ORDER BY submission_time DESC;"""
    return config.run_query(query)


def insert_data(cursor, title, message):
    question_id = get_max_id(config.connection())
    dt = datetime.now()
    cursor.execute("""
        INSERT INTO question
        VALUES (%s, %s, 0, 0, %s, %s, 0) """, (question_id, dt, title, message))
    return cursor


def insert_answer(cursor, message, question_id):
    answer_id = get_max_id_answer(config.connection())
    dt = datetime.now()
    cursor.execute("""
        INSERT INTO answer
        VALUES (%s, %s, 0, %s, %s, 0) """, (answer_id, dt, question_id, message))
    return cursor


def question(question_idd):
    query = """SELECT * from question WHERE id = %s;""" % question_idd
    return config.run_query(query)


def answer(question_idd):
    query = """SELECT * from answer WHERE question_id = %s;""" % question_idd
    return config.run_query(query)


def get_max_id(cursor):
    cursor.execute("""
        SELECT id from question ORDER BY id DESC LIMIT 1
        ;""")
    rows = cursor.fetchall()
    return int(rows[0][0]) + 1


def get_max_id_answer(cursor):
    cursor.execute("""
        SELECT id from answer ORDER BY id DESC LIMIT 1
        ;""")
    rows = cursor.fetchall()
    return int(rows[0][0]) + 1


def get_max_id_comment(cursor):
    cursor.execute("""
        SELECT id from comment ORDER BY id DESC LIMIT 1
        ;""")
    rows = cursor.fetchall()
    return int(rows[0][0]) + 1


def get_question(cursor, question_id):
    cursor.execute("""
        SELECT title, message from question WHERE id = %s """, (str(question_id)))
    rows = cursor.fetchall()
    return rows


def insert_question_comment(cursor, message, question_id):
    comment_id = get_max_id_comment(config.connection())
    dt = datetime.now()
    cursor.execute("""
        INSERT INTO comment
        VALUES (%s, %s, null, %s, %s) """, (comment_id, question_id, message, dt))
    return cursor

