from flask import Flask
from extensions import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///desserts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

from views import *

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # create tables from models
    app.run(debug=True)
