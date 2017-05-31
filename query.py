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


def insert_data(title, message):
    question_id = get_max_id()
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query = """INSERT INTO question
            VALUES (%s, '%s', 0, 0, '%s', '%s', null) """ % (question_id, dt, title, message)
    return config.run_query(query)


def insert_answer(message, question_id):
    answer_id = get_max_id_answer()
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query = """INSERT INTO answer
            VALUES (%s, '%s', 0, '%s', '%s', 0) """ % (answer_id, dt, question_id, message)
    return config.run_query(query)


def question(question_idd):
    query = """SELECT * from question WHERE id = %s;""" % question_idd
    return config.run_query(query)


def answer(question_idd):
    query = """SELECT * from answer WHERE question_id = %s;""" % question_idd
    return config.run_query(query)


def get_max_id():
    query = """SELECT id from question ORDER BY id DESC LIMIT 1;"""
    rows = config.run_query(query)
    return int(rows[0][0]) + 1


def get_max_id_answer():
    query = """SELECT id from answer ORDER BY id DESC LIMIT 1;"""
    rows = config.run_query(query)
    return int(rows[0][0]) + 1


def get_max_id_comment():
    query = """SELECT id from comment ORDER BY id DESC LIMIT 1;"""
    rows = config.run_query(query)
    return int(rows[0][0]) + 1


def get_question(question_id):
    query = """SELECT title, message from question WHERE id = %s """ % question_id
    rows = config.run_query(query)
    return rows


def insert_question_comment(message, question_id):
    comment_id = get_max_id_comment()
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    query = """INSERT INTO comment
            VALUES (%s, %s, null, '%s', '%s') """ % (comment_id, question_id, message, dt)
    return config.run_query(query)


def question_comment(question_id):
    query = """SELECT submission_time, message from comment WHERE question_id = %s """ % question_id
    rows = config.run_query(query)
    return rows


def insert_username(user):
    query = """INSERT INTO users (username)
            VALUES ('%s') """ % user
    return config.run_query(query)

