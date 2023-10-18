from flask import *
from app.models.college import *
from flask_wtf import *

college_bp = Blueprint('college', __name__)

@college_bp.route('/colleges/')
def colleges():
    return render_template('colleges.html')