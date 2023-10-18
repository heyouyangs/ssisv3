from flask import *
from app.models.college import *
from flask_wtf import *

college_bp = Blueprint('college', __name__)

@college_bp.route('/colleges/')
def colleges():
    colleges = college_table()
    return render_template('colleges.html', colleges=colleges)

@college_bp.route('/addcollege/', methods=['GET', 'POST'])
def addcolleges():
    if request.method == 'POST':
        collegecode = request.form['collegecode']
        collegename = request.form['collegename']
        add_college(collegecode, collegename)
        return redirect('/colleges/') 
    return render_template('addcolleges.html')
