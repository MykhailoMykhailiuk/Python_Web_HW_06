# Знайти студента із найвищим середнім балом з певного предмета.

from connect import create_connection, database
from table_view import table

print("Завдання: Знайти студента із найвищим середнім балом з певного предмета.")
subject = input('Введіть предмет: ')

query = """SELECT students.name, students.lastname,subjects.name, AVG(marks.mark) as a_mark
            FROM students
            JOIN marks ON students.id = marks.students_id
            JOIN subjects ON marks.subjects_id = subjects.id
            WHERE subjects.name = ?
            GROUP BY students.id
            ORDER BY a_mark DESC
            LIMIT 1
        """

with create_connection(database) as conn:
    
    cursor = conn.cursor()
    cursor.execute(query, (subject.capitalize(), ))
    
    data = cursor.fetchall()
    field_name = ['name', 'lastname', 'subject', 'averege mark']
    print(table(field_name, data))