
def fetch_data(cursor):
    rows = list(cursor.fetchall())
    # rows.insert(0, [row[0] for row in cursor.description])
    return rows
