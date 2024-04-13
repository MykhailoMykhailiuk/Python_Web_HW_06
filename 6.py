# Знайти список студентів у певній групі


from connect import create_connection, database
from table_view import table

print("Завдання: Знайти список студентів у певній групі")
group_num = input('Введіть номер групи: ')

query = """SELECT  groups.name, students.name, students.lastname
            FROM groups
            JOIN students ON students.groups_id = groups.id
            WHERE groups.name = ?
            ORDER BY students.lastname
        """


with create_connection(database) as conn:
    cursor = conn.cursor()
    cursor.execute(query, (group_num, ))
    data = cursor.fetchall()
    fields_name = ['group', 'name', 'lastname']
    print(table(fields_name, data))

