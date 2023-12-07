from flask import *
from flask_mysql_connector import MySQL
from flask_bootstrap import Bootstrap
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL,  CLOUDINARY_API_KEY, CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_SECRET
from flask_wtf.csrf import *
from app.routes import collegeroute, courseroute, studentroute
import cloudinary
from cloudinary.utils import cloudinary_url

mysql = MySQL()
bootstrap = Bootstrap()

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER="root",
        MYSQL_PASSWORD="1234",
        MYSQL_DATABASE="ssisv3",
        MYSQL_HOST=DB_HOST,
        #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )
    bootstrap.init_app(app)
    mysql.init_app(app)
    CSRFProtect(app)

    cloudinary.config(cloud_name=CLOUDINARY_CLOUD_NAME,
                    api_key=CLOUDINARY_API_KEY,
                    api_secret=CLOUDINARY_API_SECRET,
                    )

    @app.route('/')
    def homepage():
        return render_template('index.html')
    
    app.register_blueprint(collegeroute.college_bp)
    app.register_blueprint(courseroute.course_bp)
    app.register_blueprint(studentroute.student_bp)
    
    return app
