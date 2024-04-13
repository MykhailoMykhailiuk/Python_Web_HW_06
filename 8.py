# Знайти середній бал, який ставить певний викладач зі своїх предметів.


from connect import create_connection, database
from table_view import table

print("Завдання: Знайти середній бал, який ставить певний викладач зі своїх предметів.")
name, lastname = input('Введіть ім\'я та прізвище викладача: ').split()

query = """SELECT teachers.name, teachers.lastname, subjects.name, ROUND(AVG(mark), 2)
            FROM marks 
            JOIN subjects ON marks.subjects_id = subjects.id 
            JOIN teachers ON subjects.teachers_id = teachers.id
            WHERE teachers.name = ? AND teachers.lastname = ?
            GROUP BY subjects.name 
        """


with create_connection(database) as conn:
    cursor = conn.cursor()
    cursor.execute(query, (name, lastname))
    data = cursor.fetchall()
    fields_name = ['name', 'lastname', 'subject', 'mark']
    print(table(fields_name, data))

