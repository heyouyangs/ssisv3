from flask_mysql_connector import MySQL
from flask import Flask, request, render_template, redirect

mysql = MySQL()

def student_table():
    cursor = mysql.connection.cursor (dictionary=True)
    query= "SELECT * FROM students"
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    return students

def student_exists(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT id FROM students WHERE id = %s", (student_id,))
    result = cursor.fetchone()
    cursor.close()
    return result is not None


def add_students(id, firstname,lastname, coursecode, yearlevel, gender):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO students (id, firstname, lastname, coursecode, yearlevel, gender) VALUES (%s, %s, %s, %s, %s, %s)", (id, firstname,lastname, coursecode, yearlevel, gender))
    mysql.connection.commit()
    cursor.close()  

def find_students(search_query):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + search_query + "%"
    
    # SQL query to search for students by name, college code, and other details
    query = "SELECT * FROM students WHERE (id LIKE %s OR firstname LIKE %s OR lastname LIKE %s OR coursecode IN (SELECT coursecode FROM courses WHERE collegecode LIKE %s) OR yearlevel = %s OR gender LIKE %s)"

    cursor.execute(query, (search_query, search_query, search_query, search_query, search_query, search_query))
    students = cursor.fetchall()
    cursor.close()
    return students  


def delete_student(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    mysql.connection.commit()
    cursor.close()


def edit_student_student(student_id, first_name, last_name,  year_level, course_code, gender):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE students SET firstname = %s, lastname = %s, coursecode = %s, yearlevel = %s, gender = %s WHERE id = %s"
    cursor.execute(update_query, (first_name, last_name,  course_code, year_level, gender, student_id))  # Swap course_code and year_level
    mysql.connection.commit()
    cursor.close()

def remove_student(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    mysql.connection.commit()
    cursor.close()
    
def get_course_codes():
    cursor = mysql.connection.cursor(dictionary=True)
    query = "SELECT coursecode FROM courses"
    cursor.execute(query)
    course_code = cursor.fetchall()
    cursor.close()
    return course_code

def update_student(student_id, first_name, last_name, year_level, course_code, gender):
    print(student_id, first_name, last_name, year_level, course_code, gender)
    cursor = mysql.connection.cursor()
    update_query = "UPDATE students SET firstname = %s, lastname = %s, coursecode = %s, yearlevel = %s, gender = %s WHERE id = %s"
    cursor.execute(update_query, (first_name, last_name, course_code, year_level, gender, student_id))
    mysql.connection.commit()
    cursor.close()

