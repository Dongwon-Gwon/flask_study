from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app
 
from module import dbModule

db_class = dbModule.Database()
query = "insert into admin(admin_id, admin_name) values(3,'Dongwon2')"
db_class.execute(query)
db_class.commit()

