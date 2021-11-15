from config import db, ma

class Admin(db.Model):
    __tablename__ = 'admin'
    admin_id = db.Column(db.Integer, primary_key=True)
    admin_name = db.Column(db.String(32), unique=True)



class AdminSchema(ma.ModelSchema):
    class Meta:
        model = Admin
        sqla_session = db.session    


