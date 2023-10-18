from flask import *
from app.models.student import *
from flask_wtf import *

student_bp = Blueprint('student', __name__)


@student_bp.route('/students/')
def students():
    students = student_table()
    return render_template('student.html', students=students)

@student_bp.route('/addstudent/')
def addstudents():
    return render_template('addstudent.html')

@student_bp.route('/addstudent/', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        id = request.form['id']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        coursecode = request.form['coursecode']
        yearlevel = request.form['yearlevel']
        gender = request.form['gender']
        add_students(id, firstname, lastname, coursecode, yearlevel, gender)
        return redirect('/students/') 
    return render_template('addstudent.html')

