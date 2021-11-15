from sqlalchemy import Column, Integer, String
from app.database import Base

class Admin(Base):
    __tablename__ = 'admin'
    admin_id = Column(Integer, primary_key=True)
    admin_name = Column(String(50), unique=True)

    def __init__(self, admin_name=None):
        self.admin_name = admin_name

    def __repr__(self):
        return f'<User {self.admin_name!r}>'
