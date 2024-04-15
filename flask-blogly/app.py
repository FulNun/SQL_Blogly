from flask import Flask, redirect, render_template, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User
from users_routes import users_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///blogly"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ihaveasecret'

toolbar = DebugToolbarExtension(app)

# Initialize SQLAlchemy and connect to app
db.init_app(app)
connect_db(app)

# Register users blueprint
app.register_blueprint(users_bp)

@app.route('/')
def root():
    """Homepage redirects to list of users."""
    return redirect("/users")

if __name__ == '__main__':
    app.run(debug=True)
