from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, exc
from datetime import datetime
from pass_validator import pass_val
import constants

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_storage.db'
db = SQLAlchemy(app)
app.secret_key = 'abc'


class Enrollment(db.Model):
    user_id = db.Column(db.Integer, ForeignKey('user.id'), primary_key=True)
    course_id = db.Column(db.Integer, ForeignKey('course.id'), primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    course = db.relationship('Course', back_populates='users')
    user = db.relationship('User', back_populates='courses')


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    courses = db.relationship('Enrollment', back_populates='user')

    def __repr__(self):
        return '<User %r>' % self.username


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    date_of_event = db.Column(db.DateTime, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    users = db.relationship('Enrollment', back_populates='course')

    def __repr__(self):
        return '<Course %r>' % self.id


@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return render_template('index.html')


@app.route('/login/', methods=['POST', 'GET'])
def login():
    try:
        if request.method == "POST":
            login_user = request.form['username']
            login_password = request.form['password']
            registered_user = User.query.filter_by(username=login_user).first()
        else:
            return render_template('login.html')

        if not registered_user:
            return constants.WRONG_USERNAME

        if login_password != registered_user.password:
            return constants.WRONG_PASSWORD

        session['username'] = registered_user.username
        session['name'] = registered_user.name
        session['id'] = registered_user.id
        return redirect('/enrollment/')

    except:
        return constants.WRONG_LOGIN


@app.route('/logout/')
def log_out():
    session.pop('username', None)
    session.pop('name', None)
    return redirect('/')


@app.route('/sign_up/', methods=['POST', 'GET'])
def sign_up():
    if request.method == "POST":
        new_name = request.form['name']
        new_username = request.form['username']
        new_email = request.form['email']
        new_password = request.form['password']

        if new_name == '' or new_username == '' or new_email == '' or new_password == '':
            return constants.EMPTY_FIELDS

        if not pass_val(new_password):
            return constants.MISSED_REQUIREMENTS

        if User.query.filter_by(username=new_username).first():
            return constants.USERNAME_EXISTS

        create_new_user(new_name, new_username, new_email, new_password)
        return redirect('/login/')

    return render_template('sign_up.html')


def create_new_user(new_name, new_username, new_email, new_password):
    new_user = User(name=new_name, username=new_username, email=new_email, password=new_password)
    try:
        db.session.add(new_user)
        db.session.commit()
    except:
        return constants.WRONG_ADDING


@app.route('/enrollment/', methods=['POST', 'GET'])
def enrollment():
    active_courses = Course.query.all()
    if request.method == "POST":
        for course in active_courses:
            if request.form.get(course.name):
                create_enrollment(session['id'], course.id)
    if 'username' in session:
        user_courses = User.query.filter_by(id=session['id']).first().courses

        return render_template('enrollment.html', username=session['username'], name=session['name'],
                               courses=active_courses, user_courses=user_courses)
    return render_template('login.html')


@app.route('/delete/<int:user_course_id>')
def delete(user_course_id):
    enrollment_to_delete = \
        Enrollment.query.filter_by(course_id=user_course_id).filter_by(user_id=session['id']).first()
    try:
        db.session.delete(enrollment_to_delete)
        db.session.commit()
        return redirect('/enrollment/')
    except:
        return constants.WRONG_DELETING


def create_enrollment(user_id, course_id):
    new_enrollment = Enrollment(user_id=user_id, course_id=course_id)
    try:
        db.session.add(new_enrollment)
        db.session.commit()
    except exc.IntegrityError:
        db.session.rollback()
        return constants.WRONG_ADDING


def create_course(date_of_event, name, description):
    new_course = Course(date_of_event=date_of_event, name=name, description=description)
    try:
        db.session.add(new_course)
        db.session.commit()
    except:
        return constants.WRONG_ADDING


if __name__ == "__main__":
    app.run(debug=True)
