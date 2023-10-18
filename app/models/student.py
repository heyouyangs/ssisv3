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