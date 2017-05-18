import config
from datetime import datetime
import common


def five_latest_questions(cursor):
    cursor.execute("""SELECT * FROM question ORDER BY submission_time DESC
                    LIMIT 5
                   ;""")
    return cursor


def all_question(cursor):
    cursor.execute("""SELECT * FROM question ORDER BY submission_time DESC;""")
    return cursor


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


def question(cursor, question_idd):
    question_idd_int = int(question_idd)
    cursor.execute("""
                    SELECT * from question WHERE id = %s;""", (question_idd_int, ))
    rows = list(cursor.fetchall())
    return rows


def answer(cursor, question_idd):
    question_idd_int = int(question_idd)
    cursor.execute("""
                    SELECT * from answer WHERE question_id = %s;""", (question_idd_int, ))
    rows = list(cursor.fetchall())
    return rows


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


def get_question(cursor, question_id):
    cursor.execute("""
        SELECT title, message from question WHERE id = %s """, (str(question_id)))
    rows = cursor.fetchall()
    return rows