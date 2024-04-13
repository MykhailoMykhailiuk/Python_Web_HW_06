# Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

from connect import create_connection, database
from table_view import table

print("Завдання: Знайти 5 студентів із найбільшим середнім балом з усіх предметів")

query = """SELECT name, lastname, AVG(mark) as a_mark
            FROM marks
            JOIN students ON marks.students_id = students.id
            GROUP BY marks.students_id
            ORDER BY a_mark DESC
            LIMIT 5
        """


with create_connection(database) as conn:
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    fields_name = ['name', 'lastname', 'average mark']
    print(table(fields_name, data))
