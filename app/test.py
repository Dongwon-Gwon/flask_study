from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask import current_app as current_app
 
from app.module import dbModule

db_class = dbModule.Database()
query = "select * from admin"
row= db_class.executeAll(query)
print(row)