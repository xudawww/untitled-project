from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from route import routes
app = Flask(__name__)
app.secret_key = '79537d00f4834892986f09a100aa1edf'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root@localhost/groceryapp"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
app.register_blueprint(routes)
