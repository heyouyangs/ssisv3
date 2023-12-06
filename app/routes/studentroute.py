from flask import *
from app.models.student import *
from flask_wtf import *
import re
from flask import flash

student_bp = Blueprint('student', __name__)

@student_bp.route('/students/')
def students():
    students = student_table()
    return render_template('student.html', students=students)

@student_bp.route('/addstudent/', methods=['GET', 'POST'])
def addstudents():
    alert_message = None  # Initialize alert_message to None

    if request.method == 'POST':
        id = request.form['id']
        # Check if the ID is in the correct format
        if not re.match(r'\d{4}-\d{4}', id):
            flash("Incorrect ID format. Please enter ID in the format YYYY-NNNN.", 'error')
            return render_template('addstudent.html', courses=get_course_codes())
                
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        coursecode = request.form['coursecode']
        yearlevel = request.form['yearlevel']
        gender = request.form['gender']
        # Check if the student already exists
        if student_exists(id):
            flash('Student with this ID Number already exists!', 'error')
        else:
            # Student doesn't exist, add them to the database
            add_students(id, firstname, lastname, coursecode, yearlevel, gender)
            flash('Student added successfully!', 'success')
            # Redirect to the students table (change 'students_table' to the actual route)
            return redirect(url_for('student.students'))

    courses = get_course_codes()
    return render_template('addstudent.html', courses=courses, alert_message=alert_message)



@student_bp.route('/students/search', methods=['GET', 'POST'])
def search_students():
    students = []
    if request.method == 'POST':
        search_query = request.form.get('studentsearch')
        if search_query:
            students = find_students(search_query)
    return render_template('student.html', students=students)






    
@student_bp.route('/students/delete/<string:id>', methods=['DELETE'])
def remove_college(id):
    if request.method == 'DELETE':
        print(id)
        delete_student(id)
        return jsonify({'success': True})
    
from flask import redirect, url_for, flash

@student_bp.route('/editstudent', methods=['GET', 'POST'])
def edit_student():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        first_name = request.form.get('first_name').title()
        last_name = request.form.get('last_name').title()
        year_level = int(request.form.get('year_level'))  # Convert to integer
        course_code = request.form.get('coursecode')
        gender = request.form.get('gender').capitalize()

        # Check if the course code is provided before updating
        if course_code is not None:
            edit_student_student(student_id, first_name, last_name, year_level, course_code, gender)
            flash('Student edited successfully!', 'success')
            return redirect(url_for('student.students'))  # Redirect to the students page after successful edit

    student_id = request.args.get('student_id')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    year_level = request.args.get('year_level')
    course_code = request.args.get('course_code')
    gender = request.args.get('gender')
    courses = get_course_codes()

    return render_template('editstudents.html', student_id=student_id, first_name=first_name, last_name=last_name, year_level=year_level, course_code=course_code, gender=gender, courses=courses)
