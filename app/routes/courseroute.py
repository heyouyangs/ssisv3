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
    return render_template('editcourses.html', course_code=course_code, course_name=course_name, college_code=college_code)

