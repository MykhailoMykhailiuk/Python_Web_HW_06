# Знайти середній бал на потоці (по всій таблиці оцінок).


from connect import create_connection, database
from table_view import table

print("Завдання: Знайти середній бал на потоці (по всій таблиці оцінок).")

query = """SELECT groups.name, ROUND(AVG(marks.mark), 2) as a_mark
            FROM groups
            JOIN marks ON students.id = marks.students_id
            JOIN students ON students.groups_id = groups.id
            GROUP BY students.groups_id
            ORDER BY a_mark DESC
        """


with create_connection(database) as conn:
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    fields_name = ['name', 'average mark']
    print(table(fields_name, data))
