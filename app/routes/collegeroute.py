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

@college_bp.route('/colleges/search', methods=['GET', 'POST'])
def search_college():
    colleges = []
    if request.method == 'POST':
        search_query = request.form.get('collegesearch')
        if search_query:
            colleges = find_college(search_query)
    return render_template('colleges.html', colleges=colleges)

@college_bp.route('/colleges/delete/<string:college_code>', methods=['DELETE'])
def remove_college(college_code):
    if request.method == 'DELETE':
        delete_college(college_code)
        return jsonify({'success': True})

@college_bp.route('/editcollege', methods=['GET', 'POST'])
def edit_college():
    if request.method == 'POST':
        college_code = request.form.get('college_code').upper()
        college_name = request.form.get('college_name')
        
        update_college(college_code, college_name)
        return redirect('/colleges/') 
    college_code = request.args.get('college_code')
    college_name = request.args.get('college_name')
    return render_template('editcolleges.html', college_code=college_code, college_name=college_name)


    



