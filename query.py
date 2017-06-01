import config
from datetime import datetime
import common
import psycopg2


def five_latest_questions():
    query = """SELECT * FROM question ORDER BY submission_time DESC
            LIMIT 5;"""
    return config.run_query(query)


def all_question():
    query = """SELECT * FROM question ORDER BY submission_time DESC;"""
    return config.run_query(query)


def list_all_user():
    query = """SELECT username FROM users"""
    rows = config.run_query(query)
    user_names = []
    for name in rows:
        user_names.append(name[0])
    return user_names


def insert_data(title, message, user):
    question_id = get_max_id()
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_id = fetch_user_id(user)[0][0]
    query = """INSERT INTO question
            VALUES (%s, '%s', 0, 0, '%s', '%s', null, '%d') """ % (question_id, dt, title, message, user_id)
    return config.run_query(query)

def fetch_user_id(user):
    query = """ SELECT id FROM users WHERE username = '%s';""" % (user)
    return config.run_query(query)


def insert_answer(message, question_id, user):
    answer_id = get_max_id_answer()
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_id = fetch_user_id(user)[0][0]
    query = """INSERT INTO answer
            VALUES (%s, '%s', 0, '%s', '%s', 0, '%d') """ % (answer_id, dt, question_id, message, user_id)
    return config.run_query(query)


def question(question_idd):
    query = """SELECT * from question WHERE id = %s;""" % question_idd
    return config.run_query(query)


def answer(question_idd):
    query = """SELECT * from answer WHERE question_id = %s ORDER BY id;""" % question_idd
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


def insert_question_comment(message, question_id, user):
    comment_id = get_max_id_comment()
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_id = fetch_user_id(user)[0][0]
    query = """INSERT INTO comment
            VALUES (%s, %s, null, '%s', '%s', '%d') """ % (comment_id, question_id, message, dt, user_id)
    return config.run_query(query)


def question_comment(question_id):
    query = """SELECT submission_time, message from comment WHERE question_id = %s """ % question_id
    rows = config.run_query(query)
    return rows


def update_vote(table, data_id, votenumber):
    query = """
        UPDATE %s
        SET vote_number = %s
        WHERE id = %s;
        """ % (table, votenumber, data_id)
    return config.run_query(query)


def get_answer(answer_id):
    query = """SELECT message from answer WHERE id = %s """ % answer_id
    rows = config.run_query(query)
    return rows


def insert_answer_comment(message, answer_id, user):
    comment_id = get_max_id_comment()
    dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user_id = fetch_user_id(user)[0][0]
    query = """INSERT INTO comment
            VALUES (%s, null, %s, '%s', '%s', '%d') """ % (comment_id, answer_id, message, dt, user_id)
    return config.run_query(query)


def question_id_from_answer(answer_id):
    query = """SELECT question_id from answer WHERE id = %s """ % answer_id
    rows = config.run_query(query)
    return int(rows[0][0])


def insert_username(user):
    try:
        query = """INSERT INTO users (username)
                VALUES ('%s') """ % user
        return config.run_query(query)
    except psycopg2.IntegrityError as error:
        message = "The username is invalid or already exist."
        print(message)


def all_user():
    query = """SELECT username, to_char(registration_time, 'YYYY-MM-DD HH24:MI'), reputation
    FROM users
    ORDER BY reputation DESC;"""
    return config.run_query(query)

