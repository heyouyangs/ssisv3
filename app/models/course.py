from flask_mysql_connector import MySQL

mysql = MySQL()

def course_table():
    cursor = mysql.connection.cursor (dictionary=True)
    query= "SELECT * FROM courses"
    cursor.execute(query)
    courses = cursor.fetchall()
    cursor.close()
    return courses

def add_courses(coursecode, coursename, collegecode):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO courses (coursecode, coursename, collegecode) VALUES (%s, %s, %s)", (coursecode, coursename, collegecode))
    mysql.connection.commit()
    cursor.close()

def find_courses(searchcourses):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + searchcourses + "%"
    cursor.execute("SELECT * FROM courses WHERE coursecode LIKE %s OR coursename LIKE %s OR collegecode LIKE %s", (search_query, search_query, search_query))
    courses = cursor.fetchall()
    cursor.close()
    return courses


def delete_course(course_code):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM courses WHERE coursecode = %s", (course_code,))
    mysql.connection.commit()
    cursor.close()

