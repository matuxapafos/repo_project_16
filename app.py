from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")

app.secret_key = '1F7VkTpXpSB09P6UskV9Kq$23QWD9FG440'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///info.db'
db = SQLAlchemy(app)


class Guests(db.Model):
    __tableName__ = 'Guests'
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    father_name = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)
    go_in = db.Column(db.String, nullable=False)
    go_out = db.Column(db.String, nullable=False)

    def __init__(self, surname, name, father_name, phone_number, email, go_in, go_out):
        self.surname = surname
        self.name = name
        self.father_name = father_name
        self.phone_number = phone_number
        self.email = email
        self.go_in = go_in
        self.go_out = go_out


class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rate = db.Column(db.String, nullable=False)
    count_guests = db.Column(db.Integer,primary_key=True)
    square = db.Column(db.Integer,primary_key=True)
    bathroom = db.Column(db.String, nullable=False)
    balcony = db.Column(db.String, nullable=False)
    free = db.Column(db.String, nullable=False)

    def __init__(self, rate, count_guests, square, bathroom, balcony):
        self.rate = rate
        self.count_guests = count_guests
        self.square = square
        self.bathroom = bathroom
        self.balcony = balcony


@app.route('/')
def reg():
    return render_template('reg.html')


@app.route('/regi', methods=['POST'])#/regi не работает, это нужно чтобы работал /
def regi():
    name = request.form['name']
    surname = request.form['surname']
    father_name = request.form['father_name']
    number = request.form['number']
    email = request.form['email']
    go_in = request.form['go_in']
    go_out = request.form['go_out']
    user = Guests(surname, name, father_name, number, email, go_in, go_out)
    db.session.add(user)
    db.session.flush()
    db.session.commit()
    return redirect('/good')


@app.route('/yes')
def yes():
    return render_template('yes.html')


@app.route('/no')
def no():
    return render_template("no.html")


@app.route('/login', methods=['POST']) #/login не работает, это нужно чтобы работал /admin
def login():
    surname = request.form['surname']
    number = request.form['number']
    for users in Guests.query.all():
        print(users.surname)
        print(users.phone_number)
    if (users.surname == surname) and (users.phone_number == number):
        return redirect('/yes')
    else:
        return redirect('/no')


@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/good')
def good():
    return render_template('good.html')

@app.route('/room_list')
def room_list():

    a =[]
    for room1 in Room.query.all():
        print(room1.rate)
        print(room1.count_guests)
        print(room1.square)
        print(room1.bathroom)
        print(room1.balcony)
        print(room1.free)
        a.append(room1.rate)
        a.append(room1.count_guests)
        a.append(room1.square)
        a.append(room1.bathroom)
        a.append(room1.balcony)
        a.append(room1.free)
    return str(a)


if __name__ == '__main__':
    app.run(debug=True)
