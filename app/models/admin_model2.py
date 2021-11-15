from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost:3306/car_rental_system'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Admin(db.Model):
    admin_id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.admin_name