from flask import *
from app.models.student import *
from flask_wtf import *

student_bp = Blueprint('student', __name__)

@student_bp.route('/students/')
def students():
    students = student_table()
    return render_template('student.html', students=students)

@student_bp.route('/addstudent/', methods=['GET', 'POST'])
def addstudents():
    if request.method == 'POST':
        id = request.form['id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        coursecode = request.form['coursecode']
        yearlevel = request.form['yearlevel']
        gender = request.form['gender']

        # Check if the student already exists
        if student_exists(id):
            flash("Student with this ID already exists.", "error")
        else:
            # Student doesn't exist, add them to the database
            add_students(id, firstname, lastname, coursecode, yearlevel, gender)
            flash("Student added successfully.", "success")
            return redirect('/students/')  # Redirect after adding a student

    return render_template('addstudent.html')



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
    

@student_bp.route('/editstudent', methods=['GET', 'POST'])
def edit_student():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        first_name = request.form.get('first_name').title()
        last_name = request.form.get('last_name').title()
        year_level = request.form.get('year_level')
        course_code = request.form.get('course_code').upper()
        gender = request.form.get('gender').capitalize()
        update_student(student_id, first_name, last_name, year_level, course_code, gender)
        return redirect('/students/') 
    student_id = request.args.get('student_id')
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    year_level = request.args.get('year_level')
    course_code = request.args.get('course_code')
    gender = request.args.get('gender')
    courses = get_course_codes()
    return render_template('editstudents.html', student_id=student_id, first_name=first_name, last_name=last_name,  year_level=year_level, course_code=course_code, gender=gender, courses=courses)

