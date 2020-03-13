from flask import Flask, render_template, url_for, jsonify, flash, redirect
from mining import PreditLR
from flask import request
from forms import LoginForm, BookingForm
from flask_login import login_user
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_login import logout_user, login_required
from flask_moment import Moment
from datetime import date, timedelta
import os
basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
DEBUG = True

app = Flask(__name__)
app.secret_key = 'development key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///HDP.sqlite3'
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_view = 'login'
moment = Moment(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % self.username

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date=db.Column(db.DateTime)
    appointnum= db.Column(db.Integer)
    time=db.Column(db.Float)
    patientname = db.Column(db.String(64), index=True, unique=False)
    NIC= db.Column(db.String(11), index=True, unique=False)
    Phonenum= db.Column(db.Integer, index=True, unique=False)

    # def __repr__(self):
    #     return '<User %r>' % self.username

def get_today():
        return date.today()
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route("/", methods=['GET'])
def home():
    return render_template("home.html")

@app.route('/adminlogin', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.password==form.password.data:
            flash('Invalid username or password')
            return redirect('/login')
        login_user(user, remember=form.remember_me.data)
        return redirect('/index')
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@app.route("/channeling", methods=['GET', 'POST'])
def channel():
    return render_template('channeling.html')

@app.route("/healthtips", methods=['GET', 'POST'])
def healthtips():
    return render_template('Healthtipspage.html')

@app.route("/booking", methods=['GET', 'POST'])
def booking():
    today = get_today()
    delta=timedelta(days=1)
    d1=today+delta
    d2=d1+delta
    d3=d2+delta
    d4=d3+delta
    d5=d4+delta
    d6=d5+delta
    d7=d6+delta

    return render_template('booking.html', d1=d1, d2=d2, d3=d3, d4=d4, d5=d5, d6=d6, d7=d7)

@app.route("/bookingd1", methods=['GET', 'POST'])
def bookingd1():
    form = BookingForm()
    today = get_today()
    delta=timedelta(days=1)
    d1=today+delta
    Booking1=Booking.query.all()
    count=0

    for booking1 in Booking1:
        if booking1.date.strftime("%d/%m/%y") == d1.strftime("%d/%m/%y"):
            count+=1
    appnum1=count+1
    apptime=count+10
    if request.method == 'POST':
        booking = Booking(date=d1, appointnum=appnum1, time=apptime, patientname=form.patientname.data, NIC=form.NIC.data, Phonenum=form.Phonenum.data)
        db.session.add(booking)
        db.session.commit()
        return render_template('booking_success.html', date=d1, appointnum=appnum1, appointime=apptime)
    return render_template('booking1.html', form=form)

@app.route("/bookingd2", methods=['GET', 'POST'])
def bookingd2():
    form = BookingForm()
    today = get_today()
    delta=timedelta(days=1)
    d2=today+2*delta
    Booking1=Booking.query.all()
    count=0

    for booking1 in Booking1:
        if booking1.date.strftime("%d/%m/%y") == d2.strftime("%d/%m/%y"):
            count+=1
    appnum=count
    appnum1=appnum+1
    apptime=appnum+10
    if request.method == 'POST':
        booking = Booking(date=d2, appointnum=appnum1, time=apptime, patientname=form.patientname.data, NIC=form.NIC.data, Phonenum=form.Phonenum.data)
        db.session.add(booking)
        db.session.commit()
        return render_template('booking_success.html', date=d2, appointnum=appnum1, appointime=apptime)
    return render_template('booking1.html', form=form)

@app.route("/bookingd3", methods=['GET', 'POST'])
def bookingd3():
    form = BookingForm()
    today = get_today()
    delta=timedelta(days=1)
    d3=today+3*delta
    Booking1=Booking.query.all()
    count=0

    for booking1 in Booking1:
        if booking1.date.strftime("%d/%m/%y") == d3.strftime("%d/%m/%y"):
            count+=1
    appnum=count
    appnum1=appnum+1
    apptime=appnum+10
    if request.method == 'POST':
        booking = Booking(date=d3, appointnum=appnum1, time=apptime, patientname=form.patientname.data, NIC=form.NIC.data, Phonenum=form.Phonenum.data)
        db.session.add(booking)
        db.session.commit()
        return render_template('booking_success.html', date=d3, appointnum=appnum1, appointime=apptime)
    return render_template('booking1.html', form=form)

@app.route("/bookingd4", methods=['GET', 'POST'])
def bookingd4():
    form = BookingForm()
    today = get_today()
    delta=timedelta(days=1)
    d4=today+4*delta
    Booking1=Booking.query.all()
    count=0

    for booking1 in Booking1:
        if booking1.date.strftime("%d/%m/%y") == d4.strftime("%d/%m/%y"):
            count+=1
    appnum=count
    appnum1=appnum+1
    apptime=appnum+10
    if request.method == 'POST':
        booking = Booking(date=d4, appointnum=appnum1, time=apptime, patientname=form.patientname.data, NIC=form.NIC.data, Phonenum=form.Phonenum.data)
        db.session.add(booking)
        db.session.commit()
        return render_template('booking_success.html', date=d4, appointnum=appnum1, appointime=apptime)
    return render_template('booking1.html', form=form)

@app.route("/bookingd5", methods=['GET', 'POST'])
def bookingd5():
    form = BookingForm()
    today = get_today()
    delta=timedelta(days=1)
    d5=today+5*delta
    Booking1=Booking.query.all()
    count=0

    for booking1 in Booking1:
        if booking1.date.strftime("%d/%m/%y") == d5.strftime("%d/%m/%y"):
            count+=1
    appnum=count
    appnum1=appnum+1
    apptime=appnum+10
    if request.method == 'POST':
        booking = Booking(date=d5, appointnum=appnum1, time=apptime, patientname=form.patientname.data, NIC=form.NIC.data, Phonenum=form.Phonenum.data)
        db.session.add(booking)
        db.session.commit()
        return render_template('booking_success.html', date=d5, appointnum=appnum1, appointime=apptime)
    return render_template('booking1.html', form=form)

@app.route("/bookingd6", methods=['GET', 'POST'])
def bookingd6():
    form = BookingForm()
    today = get_today()
    delta=timedelta(days=1)
    d6=today+6*delta
    Booking1=Booking.query.all()
    count=0

    for booking1 in Booking1:
        if booking1.date.strftime("%d/%m/%y") == d6.strftime("%d/%m/%y"):
            count+=1
    appnum=count
    appnum1=appnum+1
    apptime=appnum+10
    if request.method == 'POST':
        booking = Booking(date=d6, appointnum=appnum1, time=apptime, patientname=form.patientname.data, NIC=form.NIC.data, Phonenum=form.Phonenum.data)
        db.session.add(booking)
        db.session.commit()
        return render_template('booking_success.html', date=d6, appointnum=appnum1, appointime=apptime)
    return render_template('booking1.html', form=form)

@app.route("/bookingd7", methods=['GET', 'POST'])
def bookingd7():
    form = BookingForm()
    today = get_today()
    delta=timedelta(days=1)
    d7=today+7*delta
    Booking1=Booking.query.all()
    count=0

    for booking1 in Booking1:
        if booking1.date.strftime("%d/%m/%y") == d7.strftime("%d/%m/%y"):
            count+=1
    appnum=count
    appnum1=appnum+1
    apptime=appnum+10
    if request.method == 'POST':
        booking = Booking(date=d7, appointnum=appnum1, time=apptime, patientname=form.patientname.data, NIC=form.NIC.data, Phonenum=form.Phonenum.data)
        db.session.add(booking)
        db.session.commit()
        return render_template('booking_success.html', date=d7, appointnum=appnum1, appointime=apptime)
    return render_template('booking1.html', form=form)




@app.route('/index')
@login_required
def show_all():
    today = get_today()
    delta=timedelta(days=1)
    d1=today+delta
    d2=d1+delta
    d3=d2+delta
    d4=d3+delta
    d5=d4+delta
    d6=d5+delta
    d7=d6+delta

    Booking1=Booking.query.all()
    Day1=[]
    Day2=[]
    Day3=[]
    Day4=[]
    Day5=[]
    Day6=[]
    Day7=[]


    for booking in Booking1:
        if booking.date.strftime("%d/%m/%y") == d1.strftime("%d/%m/%y"):
            Day1.append(booking)

        if booking.date.strftime("%d/%m/%y") == d2.strftime("%d/%m/%y"):
            Day2.append(booking)

        if booking.date.strftime("%d/%m/%y") == d3.strftime("%d/%m/%y"):
            Day3.append(booking)

        if booking.date.strftime("%d/%m/%y") == d4.strftime("%d/%m/%y"):
            Day4.append(booking)

        if booking.date.strftime("%d/%m/%y") == d5.strftime("%d/%m/%y"):
            Day5.append(booking)

        if booking.date.strftime("%d/%m/%y") == d6.strftime("%d/%m/%y"):
            Day6.append(booking)

        if booking.date.strftime("%d/%m/%y") == d7.strftime("%d/%m/%y"):
            Day7.append(booking)




    return render_template('show_all.html', d1=d1, d2=d2, d3=d3, d4=d4, d5=d5, d6=d6, d7=d7,
                           # Booking1=db.session.query(Booking).filter(Booking.date == d1))
           Day1=Day1, Day2=Day2, Day3=Day3, Day4=Day4, Day5=Day5, Day6=Day6, Day7=Day7)

@app.route('/delete', methods=['POST'])
def delete_entry():
    id=request.form['booking_id']
    b=Booking.query.get(id)
    db.session.delete(b)
    db.session.commit()
    return redirect('/index')

@app.route("/predict", methods=['GET', 'POST'])
def predictPage():
    return render_template('Prediction Page Frontend.html')




@app.route("/result", methods=['GET', 'POST'])
def resultPage():
    if request.method == 'POST': 
        to_predict_list = request.form.to_dict() 
        to_predict_list = list(to_predict_list.values()) 
        to_predict_list = list(map(int, to_predict_list)) 
        to_predict_list = [to_predict_list]
        prediction = PreditLR(to_predict_list)
        return render_template("result.html", prediction = prediction) 

if __name__ == "__main__":
    app.run(debug=True)
