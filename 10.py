# Список курсів, які певному студенту читає певний викладач


from connect import create_connection, database
from table_view import table

print("Завдання: Список курсів, які певному студенту читає певний викладач.")
s_name, s_lastname = input('Введіть ім\'я та прізвище студента: ').split()
t_name, t_lastname = input('Введіть ім\'я та прізвище викладача: ').split()

query = """SELECT students.name, students.lastname, teachers.name, teachers.lastname, subjects.name
            FROM students
            JOIN marks ON students.id = marks.students_id
            JOIN subjects ON marks.subjects_id = subjects.id
            JOIN teachers ON subjects.teachers_id = teachers.id
            WHERE students.name = ? AND students.lastname = ? AND teachers.name = ? AND teachers.lastname = ? 
            GROUP BY subjects.name
        """

with create_connection(database) as conn:
    cursor = conn.cursor()
    cursor.execute(query, (s_name, s_lastname, t_name, t_lastname))
    data = cursor.fetchall()
    fields_name = [
                   'studnet name',
                   'student lastname',
                   'teacher name',
                   'teacher lastname',
                   'subject'
                   ]
    
    print(table(fields_name, data))

