# Знайти середній бал у групах з певного предмета.


from connect import create_connection, database
from table_view import table

print("Завдання: Знайти середній бал у групах з певного предмета.")
subject = input('Введіть предмет: ')

query = """SELECT groups.name, subjects.name, ROUND(AVG(marks.mark), 2) as a_mark
            FROM groups
            JOIN marks ON students.id = marks.students_id
            JOIN students ON students.groups_id = groups.id
            JOIN subjects ON marks.subjects_id = subjects.id
            WHERE subjects.name = ?
            GROUP BY students.groups_id
            ORDER BY a_mark DESC
        """


with create_connection(database) as conn:
    cursor = conn.cursor()
    cursor.execute(query, (subject.capitalize(), ))
    data = cursor.fetchall()
    fields_name = ['name', 'subject', 'average mark']
    print(table(fields_name, data))
