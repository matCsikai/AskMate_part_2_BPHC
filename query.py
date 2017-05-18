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


def all_answers(cursor, question_idd):
    cursor.execute("""
                    SELECT question.id, question.submission_time, question.title, question.message, answer.message FROM question
                    INNER JOIN answer
                    ON question.id = answer.question_id;
                ;""")
    rows = cursor.fetchall()
    question_idd_int = int(question_idd)
    return rows[question_idd_int]


def get_max_id(cursor):
    cursor.execute("""
        SELECT id from question ORDER BY id DESC LIMIT 1
        ;""")
    rows = cursor.fetchall()
    return int(rows[0][0]) + 1

# print(all_answers(config.connection(), 0))
