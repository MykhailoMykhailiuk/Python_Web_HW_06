# Знайти оцінки студентів у окремій групі з певного предмета.


from connect import create_connection, database
from table_view import table

print("Завдання: Знайти оцінки студентів у окремій групі з певного предмета.")
group_num = input('Введіть номер групи: ')
subject = input('Введіть назву предмета: ')

query = """SELECT groups.name, students.name, students.lastname, subjects.name, marks.mark, marks.date
            FROM marks
            JOIN students ON marks.students_id = students.id
            JOIN subjects ON marks.subjects_id = subjects.id
            JOIN groups ON students.groups_id = groups.id
            WHERE groups.name = ? AND subjects.name = ?
            ORDER BY students.lastname
        """


with create_connection(database) as conn:
    cursor = conn.cursor()
    cursor.execute(query, (group_num, subject.capitalize()))
    data = cursor.fetchall()
    fields_name = ['group', 'name', 'lastname', 'subject', 'mark', 'date']
    print(table(fields_name, data))

