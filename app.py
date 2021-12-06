from flask import Flask
import uuid
import logging
from flask import Flask, render_template, request, redirect, session, abort, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from route import routes
app = Flask(__name__)
app.secret_key = '79537d00f4834892986f09a100aa1edf' 
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://doadmin:aioqbEX6a6KKkICM@db-mysql-nyc3-76425-do-user-3938218-0.b.db.ondigitalocean.com:25060/defaultdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
app.register_blueprint(routes)