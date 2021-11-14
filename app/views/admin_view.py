from flask import Blueprint
from app.model import admin_model

blue_admin = Blueprint('admin', __name__, url_prefix='/admin')



@blue_admin.route('/name', methods=["Get"])
def get_admin_all():
    return admin_model.read_admin()

@blue_admin.route('/name/<id>', methods=["Get"])
def get_admin_by_id(id):
    return admin_model.read_admin_by_id(id)