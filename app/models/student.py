from flask_mysql_connector import MySQL
from flask import Flask, request, render_template, redirect

mysql = MySQL()

def student_table():
    cursor = mysql.connection.cursor (dictionary=True)
    query= """
    SELECT students.*, CONCAT(colleges.collegename, ' (',courses.collegecode, ')') AS college_info
    FROM students
    JOIN courses ON students.coursecode = courses.coursecode
    JOIN colleges ON courses.collegecode = colleges.collegecode
    ORDER BY students.id
    """
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


def add_students(id, firstname,lastname, coursecode, yearlevel, gender, image_url):
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO students (id, firstname, lastname, coursecode, yearlevel, gender, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s)", (id, firstname,lastname, coursecode, yearlevel, gender, image_url))
    mysql.connection.commit()
    cursor.close()  

def find_students(searchstudent, filter):
    cursor = mysql.connection.cursor(dictionary=True)
    search_query = "%" + searchstudent + "%"
    
    if filter == 'all':
        query = """
            SELECT s.*, CONCAT(cl.collegename, ' (', cl.collegecode, ')') AS college_info
            FROM students AS s
            JOIN courses AS c ON s.coursecode = c.coursecode
            JOIN colleges AS cl ON c.collegecode = cl.collegecode
            WHERE s.id LIKE %s
            OR s.firstname LIKE %s
            OR s.lastname LIKE %s
            OR s.gender = %s
            OR s.yearlevel LIKE %s
            OR s.coursecode LIKE %s
            OR CONCAT(cl.collegename, ' (', cl.collegecode, ')') LIKE %s
            """
        cursor.execute(query, (search_query, search_query, search_query, searchstudent, search_query, search_query, search_query))
    else:
        if filter == 'gender':
            gender_search = searchstudent
            query = """
                SELECT s.*, CONCAT(cl.collegename, ' (', cl.collegecode, ')') AS college_info
                FROM students AS s
                JOIN courses AS c ON s.coursecode = c.coursecode
                JOIN colleges AS cl ON c.collegecode = cl.collegecode
                WHERE s.gender = %s
            """
            cursor.execute(query, (gender_search,))
        elif filter == 'college_info':
            query = """
                SELECT s.*, CONCAT(cl.collegename, ' (', cl.collegecode, ')') AS college_info
                FROM students AS s
                JOIN courses AS c ON s.coursecode = c.coursecode
                JOIN colleges AS cl ON c.collegecode = cl.collegecode
                WHERE CONCAT(cl.collegename, ' (', cl.collegecode, ')') LIKE %s
            """
            cursor.execute(query, (search_query,))
        else:
            # Use the table alias for collegecode in the WHERE clause
            query = f"""
                SELECT s.*, CONCAT(cl.collegename, ' (', cl.collegecode, ')') AS college_info
                FROM students AS s
                JOIN courses AS c ON s.coursecode = c.coursecode
                JOIN colleges AS cl ON c.collegecode = cl.collegecode
                WHERE s.{filter} LIKE %s
            """
            cursor.execute(query, (search_query,))
    
    students = cursor.fetchall()
    cursor.close()
    return students




def delete_student(student_id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    mysql.connection.commit()
    cursor.close()


def edit_student_student(student_id, first_name, last_name,  year_level, course_code, gender, image_url):
    cursor = mysql.connection.cursor()
    update_query = "UPDATE students SET firstname = %s, lastname = %s, coursecode = %s, yearlevel = %s, gender = %s, image_url= %s  WHERE id = %s"
    cursor.execute(update_query, (first_name, last_name,  course_code, year_level, gender,image_url, student_id))  # Swap course_code and year_level
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

def update_student(student_id, first_name, last_name, year_level, course_code, gender, image_url):
    print(student_id, first_name, last_name, year_level, course_code, gender, image_url)
    cursor = mysql.connection.cursor()
    update_query = "UPDATE students SET firstname = %s, lastname = %s, coursecode = %s, yearlevel = %s, gender = %s, image_url= %s WHERE id = %s"
    cursor.execute(update_query, (first_name, last_name, course_code, year_level, gender,image_url, student_id))
    mysql.connection.commit()
    cursor.close()

