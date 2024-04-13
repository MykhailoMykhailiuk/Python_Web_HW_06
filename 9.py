# Знайти список курсів, які відвідує студент.


from connect import create_connection, database
from table_view import table

print("Завдання: Знайти список курсів, які відвідує студент.")
name, lastname = input('Введіть ім\'я та прізвище студента: ').split()

query = """SELECT students.name, students.lastname, subjects.name
            FROM students
            JOIN marks ON students.id = marks.students_id
            JOIN subjects ON marks.subjects_id = subjects.id
            WHERE students.name = ? AND students.lastname = ?
            GROUP BY subjects.name
        """

with create_connection(database) as conn:
    cursor = conn.cursor()
    cursor.execute(query, (name, lastname))
    data = cursor.fetchall()
    fields_name = ['name', 'lastname', 'subject']
    print(table(fields_name, data))

