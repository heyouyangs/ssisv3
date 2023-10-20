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
        add_students(id, firstname,lastname, coursecode, yearlevel, gender)
        return redirect('/students/') 
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

