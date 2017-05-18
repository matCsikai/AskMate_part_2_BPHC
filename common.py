

def fetch_data(cursor):
    rows = list(cursor.fetchall())
    rows.insert(0, [row[0] for row in cursor.description])
    return rows


# def generate_data_id(cursor):
#     value = query.get_max_id()
#     print(value)

# generate_data_id(get_max_id(cursor))
