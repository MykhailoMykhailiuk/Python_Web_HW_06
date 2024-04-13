from sqlite3 import Error

from connect import create_connection, database


def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':

    sql_create_groups_table = """
    CREATE TABLE IF NOT EXISTS groups (
     id integer PRIMARY KEY AUTOINCREMENT,
     name integer NOT NULL
    );
    """
        
    sql_create_students_table = """
    CREATE TABLE IF NOT EXISTS students (
     id integer PRIMARY KEY AUTOINCREMENT,
     name text NOT NULL,
     lastname text NOT NULL,
     groups_id integer NOT NULL,
     FOREIGN KEY (groups_id) REFERENCES groups (id)
    );
    """

    sql_create_teachers_table = """
    CREATE TABLE IF NOT EXISTS teachers (
     id integer PRIMARY KEY AUTOINCREMENT,
     name integer NOT NULL,
     lastname text NOT NULL
    );
    """

    sql_create_subjects_table = """
    CREATE TABLE IF NOT EXISTS subjects (
     id integer PRIMARY KEY AUTOINCREMENT,
     name text NOT NULL,
     teachers_id integer NOT NULL,
     FOREIGN KEY (teachers_id) REFERENCES teachers (id)
    );
    """

    sql_create_marks_table = """
    CREATE TABLE IF NOT EXISTS marks (
     id integer PRIMARY KEY AUTOINCREMENT,
     mark integer NOT NULL,
     subjects_id integer NOT NULL,
     students_id integer NOT NULL,
     date date NOT NULL,
     FOREIGN KEY (students_id) REFERENCES students (id),
     FOREIGN KEY (subjects_id) REFERENCES subjects (id)
    );
    """

    with create_connection(database) as conn:
        if conn is not None:
            create_table(conn, sql_create_groups_table)
            create_table(conn, sql_create_students_table)
            create_table(conn, sql_create_teachers_table)
            create_table(conn, sql_create_subjects_table)
            create_table(conn, sql_create_marks_table)
        else:
            print("Error! cannot create the database connection.")
