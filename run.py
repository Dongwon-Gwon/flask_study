from flask import Flask, jsonify    
from app.views import admin_view
from flask import render_template
count = 0

app = Flask(__name__)
app.register_blueprint(admin_view.blue_admin)

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('404.html')

if __name__ == "__main__":
    

    app.run()

