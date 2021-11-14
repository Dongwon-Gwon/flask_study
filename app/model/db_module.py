import pymysql

class Database():


    def __init__(self):
        self.db = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            db="car_rental_system"
        )
        self.cursor = self.db.cursor(pymysql.cursors.DictCursor)
    
    def execute(self, query, args=()):
        self.cursor.execute(query, args)
    
    def execute_one(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchone()
        return row
 
    def execute_all(self, query, args={}):
        self.cursor.execute(query, args)
        row= self.cursor.fetchall()
        return row

    def commit(self):
        self.db.commit()
        
