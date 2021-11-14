from app.model.db_module import Database
from flask import make_response, jsonify


def read_admin():
    db_class = Database()
    query = f"select * from admin"
    db_class.execute(query)
    db_class.commit()
    row= db_class.execute_all(query)
    return jsonify(row)

def read_admin_by_id(id):
    db_class = Database()
    query = f"select * from admin where admin_id={id}"
    db_class.execute(query)
    db_class.commit()
    row= db_class.execute_all(query)
    return jsonify(row)
