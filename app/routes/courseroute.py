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
