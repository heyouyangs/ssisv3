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

def get_colleges_codes():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT collegecode FROM colleges"
    cursor.execute(query)
    course_code = cursor.fetchall()
    cursor.close()
    return course_code

def update_course(course_code, course_name, college_code):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE courses SET coursename = %s, collegecode = %s WHERE coursecode = %s"
    cursor.execute(update_query, (course_name, college_code, course_code))
    mysql.connection.commit()
    cursor.close()
