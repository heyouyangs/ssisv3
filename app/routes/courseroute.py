from flask import *
from app.models.course import *
from flask_wtf import *

course_bp = Blueprint('course', __name__)

@course_bp.route('/courses/')
def courses():
    return render_template('courses.html')