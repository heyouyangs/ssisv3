from flask import *
from app.models.course import *
from flask_wtf import *

course_bp = Blueprint('course', __name__)


@course_bp.route('/courses/')
def courses():
    courses = course_table()
    return render_template('courses.html',courses=courses)


@course_bp.route('/addcourse/')
def addcourses():
    return render_template('addcourses.html')

@course_bp.route('/addcourse/', methods=['GET', 'POST'])
def addcourse():
    if request.method == 'POST':
        coursecode = request.form['coursecode']
        coursename = request.form['coursename']
        collegecode = request.form['collegecode']
        add_courses(coursecode, coursename, collegecode)
        return redirect('/courses/') 
    return render_template('addcourses.html')

@course_bp.route('/courses/search', methods=['GET', 'POST'])
def search_courses():
    courses = []
    if request.method == 'POST':
        search_query = request.form.get('coursessearch')
        if search_query:
            courses = find_courses(search_query)



@course_bp.route('/courses/delete/<string:course_code>', methods=['DELETE'])
def remove_course(course_code):
    if request.method == 'DELETE':
        delete_course(course_code)
        return jsonify({'success': True})
    


@course_bp.route('/updatestudent', methods=['GET', 'POST'])
def edit_course():
    student = None
    message = None  # Initialize the message variable

    if request.method == 'GET':
        coursecode = request.args.get('coursecode')
        if coursecode:
            course = get_student_by_id(coursecode)

    elif request.method == 'POST':
        coursecode = request.form['coursecode']
        coursename = request.form['coursename']
        collegecode = request.form['collegecode']
       

        # Update the student's information in the database
        update_course(coursecode, coursename, collegecode)
        flash('Course updated successfully!', 'success')  # Flash the success message

        # Redirect to the students list with the success message
        return redirect(url_for('courses.courses'))

    return render_template('editcourses.html', course=course)


