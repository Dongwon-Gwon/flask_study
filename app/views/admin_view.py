from flask import Blueprint, jsonify
from app.models import admin_model
from app.models import admin_model2
from app.database import db_session
from app.models.admin_model3 import Admin
blue_admin = Blueprint('admin', __name__, url_prefix='/admin')


@blue_admin.route('/name', methods=["Get"])
def get_admin_all():
    return jsonify({"data":Admin.query.all()})

@blue_admin.route('/name/<id>', methods=["Get"])
def get_admin_by_id(id):
    # return str(Admin.query.filter_by(admin_id=id).first())
    return admin_model.read_admin_by_id(id)