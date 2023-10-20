from flask_mysql_connector import MySQL

mysql = MySQL()

def student_table():
    cursor = mysql.connection.cursor (dictionary=True)
    query= "SELECT * FROM students"
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    return students


def add_students(id, firstname,lastname, coursecode, yearlevel, gender):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO students (id, firstname, lastname, coursecode, yearlevel, gender) VALUES (%s, %s, %s, %s, %s, %s)", (id, firstname,lastname, coursecode, yearlevel, gender))
    mysql.connection.commit()
    cursor.close()    

def find_students(searchstudent):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + searchstudent + "%"
    cursor.execute("SELECT * FROM students WHERE id LIKE %s OR firstname LIKE %s OR lastname LIKE %s OR coursecode LIKE %s OR yearlevel LIKE %s OR gender LIKE %s", (search_query, search_query, search_query, search_query, search_query, search_query))
    students = cursor.fetchall()
    cursor.close()
    return students

def delete_student(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    mysql.connection.commit()
    cursor.close()

