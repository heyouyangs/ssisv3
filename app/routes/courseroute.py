from flask import *
from app.models.course import *
from flask_wtf import *
from flask import Flask, render_template, request, send_from_directory

from app.models.student import get_course_codes



course_bp = Blueprint('course', __name__)

@course_bp.route('/courses/')
def courses():
    courses = course_table()
    alert_message = request.args.get('alert_message')
    return render_template('courses.html', courses=courses, alert_message=alert_message)

@course_bp.route('/addcourse/', methods=['GET', 'POST'])
def addcourse():
    colleges = get_college_code()
    alert_message = None  # Initialize alert_message to None

    if request.method == 'POST':
        coursecode = request.form['coursecode']
        coursename = request.form['coursename']
        collegecode = request.form['collegecode']

        # Check if the college code exists
        if not collegecode_exists(collegecode):
            alert_message = "College with this Collegecode does not exist."
        else:
            # College code exists, check if the course already exists
            if coursecode_exists(coursecode):
                alert_message = "Course with this Coursecode already exists."
            else:
                # Course doesn't exist, add it to the database
                add_courses(coursecode, coursename, collegecode)
                alert_message = "Course added successfully."
                # Redirect to the courses table (change 'courses_table' to the actual route)
                return redirect(url_for('course.courses', alert_message=alert_message))

    return render_template('addcourses.html', colleges=colleges, alert_message=alert_message)



@course_bp.route('/courses/search', methods=['GET', 'POST'])
def search_courses():
    courses = []
    if request.method == 'POST':
        search_query = request.form.get('coursessearch')
        if search_query:
            courses = find_courses(search_query)
    return render_template('courses.html', courses=courses)
    

@course_bp.route('/courses/delete/<string:course_code>', methods=['DELETE'])
def remove_course(course_code):
    if request.method == 'DELETE':
        delete_course(course_code)
        return jsonify({'success': True})

@course_bp.route('/editcourse', methods=['GET', 'POST'])
def edit_course():
    if request.method == 'POST':
        course_code = request.args.get('course_code')
        course_name = request.form.get('course_name')
        college_code = request.form.get('college_code')
        update_course(course_code, course_name, college_code)
        return redirect('/courses/')
    course_code = request.args.get('course_code')
    course_name = request.args.get('course_name')
    college_code = request.args.get('college_code')

    colleges = get_college_code()
    return render_template('editcourses.html', course_code=course_code, course_name=course_name, colleges=colleges)

