from flask import Flask, render_template, request, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, exc
from datetime import datetime
import constants


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///company.db'
db = SQLAlchemy(app)
app.secret_key = 'abc'


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(50), nullable=False, unique=True)
    employees = db.relationship('Employee')

    def __repr__(self):
        return '<Department %r>' % self.username


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.Integer)
    email = db.Column(db.String(50), nullable=False, unique=True)
    department_id = db.Column(db.Integer, ForeignKey('department.id'))

    def __repr__(self):
        return '<Employee %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        new_department_name = request.form['department_name']
        if new_department_name != '':
            new_department = Department(name=new_department_name)
            try:
                db.session.add(new_department)
                db.session.commit()
            except exc.IntegrityError:
                return constants.WRONG_ADDING1
        else:
            return constants.MISSED_REQUIREMENTS

    departments = Department.query.order_by(Department.date_created).all()
    return render_template('index.html', departments=departments)


@app.route('/delete/<int:id>')
def delete(id):
    department_to_delete = Department.query.get_or_404(id)

    try:
        db.session.delete(department_to_delete)
        db.session.commit()
        return redirect('/')

    except:
        return constants.WRONG_DELETING


@app.route('/delete_employee/<int:id>')
def delete_employee(id):
    employee_to_delete = Employee.query.get_or_404(id)

    try:
        db.session.delete(employee_to_delete)
        db.session.commit()
        return redirect('/employees/')

    except:
        return constants.WRONG_DELETING


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    department = Department.query.get_or_404(id)

    if request.method == 'POST':
        department.name = request.form['department_name']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return constants.WRONG_UPDATING1

    else:
        return render_template('update.html', department=department)


@app.route('/update_employee/<int:id>', methods=['GET', 'POST'])
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    if request.method == 'POST':
        employee.name = request.form['employee_name']
        employee.phone = request.form['employee_phone']
        employee.email = request.form['employee_email']
        if employee.name == '' or employee.email == '' or not phone_number_valid(employee.phone):
            return constants.MISSED_REQUIREMENTS
        try:
            db.session.commit()
            return redirect('/employees/')
        except:
            return constants.WRONG_UPDATING2

    else:
        return render_template('update_employee.html', employee=employee)


@app.route('/employees/', methods=['POST', 'GET'])
def employees():
    department_id = session['id']
    if request.method == "POST":
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']

        if name == '' or email == '' or not phone_number_valid(phone):
            return constants.MISSED_REQUIREMENTS

        new_employee = Employee(name=name, phone=phone, email=email, department_id=department_id)
        try:
            db.session.add(new_employee)
            db.session.commit()
        except:
            return constants.WRONG_ADDING2

    department_employees = Employee.query.filter_by(department_id=department_id).all()
    department_name = Department.query.filter_by(id=department_id).first().name
    return render_template('employees.html', employees=department_employees, current_department_id=department_id,
                           current_department_name=department_name)


@app.route('/dep_session/<int:id>')
def dep_session(id):
    session['id'] = id
    return redirect('/employees/')


def create_employee(name, phone, email, department_id):
    if name == '' or email == '' or department_id == '' or not phone_number_valid(phone):
        return constants.MISSED_REQUIREMENTS
    new_employee = Employee(name=name, phone=phone, email=email, department_id=department_id)
    try:
        db.session.add(new_employee)
        db.session.commit()
    except:
        return constants.WRONG_ADDING


def phone_number_valid(number):
    try:
        if len(str(number)) == 9 and number[0] != '0' and int(number):
            return True
    except:
        return False


if __name__ == "__main__":
    app.run(debug=True)