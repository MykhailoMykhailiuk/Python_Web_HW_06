# Знайти які курси читає певний викладач.


from connect import create_connection, database
from table_view import table

print("Завдання: Знайти які курси читає певний викладач.")
name, lastname = input('Введіть ім\'я та прізвище викладача: ').split()

query = """SELECT teachers.name, teachers.lastname, subjects.name
            FROM subjects
            JOIN teachers ON subjects.teachers_id = teachers.id
            WHERE teachers.name = ? AND teachers.lastname = ?
            ORDER BY teachers.lastname 
        """


with create_connection(database) as conn:
    cursor = conn.cursor()
    cursor.execute(query, (name, lastname))
    data = cursor.fetchall()
    fields_name = ['name', 'lastname', 'subjects']
    print(table(fields_name, data))

