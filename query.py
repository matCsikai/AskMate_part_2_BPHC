import config


def five_latest_questions(cursor):
    cursor.execute("""SELECT * FROM question ORDER BY submission_time DESC
                    LIMIT 5
                   ;""")
    return cursor


def all_question(cursor):
    cursor.execute("""SELECT * FROM question ORDER BY submission_time DESC;""")
    return cursor



