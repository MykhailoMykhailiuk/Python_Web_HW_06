import random
from datetime import datetime

from connect import create_connection, database
from faker import Faker 

Faker.seed(1)
fd = Faker(locale='uk-UA')

with create_connection(database) as conn:
    cursor = conn.cursor()

    # Groups
    for _ in range(3):
        cursor.execute("INSERT INTO groups (name) VALUES (?)",
                        (fd.random_number(digits=3, fix_len=True),))

    # Teachers
    for _ in range(5):
        cursor.execute("INSERT INTO teachers (name, lastname) VALUES (?, ?)",
                        (fd.first_name(), fd.last_name()))

    # Subjects
    subjects = [
        'Математика',
        'Фізика',
        'Комп\'ютерні науки',
        'Інженарія',
        'Психологія',
        'Соціологія',
        'Полоітологія',
        'Філософія'
    ]

    teachers = cursor.execute("SELECT id FROM teachers").fetchall()
    for i in subjects:
        cursor.execute("INSERT INTO subjects (name, teachers_id) VALUES (?, ?)",
                       (i, random.choice(teachers)[0]))

    # Students
    groups = cursor.execute("SELECT id FROM groups").fetchall()
    for _ in range(50):
        cursor.execute("INSERT INTO students (name, lastname, groups_id) VALUES (?, ?, ?)",
                       (fd.first_name(), fd.last_name(), random.choice(groups)[0]))
        
    # Marks
    subjects = cursor.execute("SELECT id FROM subjects").fetchall()
    students = cursor.execute("SELECT id FROM students").fetchall()

    for student in students:
        for _ in range(20):
            cursor.execute("INSERT INTO marks (mark, subjects_id, students_id, date) VALUES (?, ?, ?, ?)", 
                    (random.randint(1, 5), 
                     random.choice(subjects)[0], 
                     student[0], 
                     fd.date_between_dates(date_start=datetime(2023,1,1), date_end=datetime(2023,6,1))))

    conn.commit()