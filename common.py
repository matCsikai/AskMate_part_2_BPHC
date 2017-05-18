
def display_data(cursor):
    rows = list(cursor.fetchall())
    rows.insert(0, [row[0] for row in cursor.description])
    return rows


def generate_data_id(filename):
    all_data = read_data(filename)
    list_of_data_id = []

    if all_data == []:
        list_of_data_id.append(0)
    else:
        for data in all_data:
            list_of_data_id.append(int(data[0]))

    return max(list_of_data_id) + 1
