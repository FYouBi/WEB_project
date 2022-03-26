from flask import Flask, render_template, url_for, request, redirect
import datetime
from data.ads import Jobs
from forms import LoginForm, Protection, LoadPhoto, RegisterForm
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/register', methods=['GET', 'POST'])
def register():
    global USER
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        print(data)
        new_user = User(surname=data['surname'],
                        name=data['name'],
                        phone_number=data['phone_number'],
                        password=data['password'],
                        address=data['address'])
        session.add(new_user)
        USER = [user for user in session.query(User).filter(User.phone_number == data['phone_number'])]
        session.commit()
        return render_template('essential.html', list_of_ad=list_of_ad, user=USER)
    return render_template('register.html', title='Авторизация', form=form)


@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    global USER
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        phone_number, password = form.data['phone_number'], form.data['password']
        for user in db_sess.query(User).all():
            if str(user.phone_number) == phone_number:
                if user.password == password:
                    USER = [user for user in session.query(User).filter(User.phone_number == form.data['phone_number'])]
                    return render_template('essential.html', list_of_ad=list_of_ad, user=USER)
                return render_template('log_in.html', title='log_in', message='Неверный пароль',
                                       form=form, list=[form.phone_number, form.password])
        return render_template('log_in.html', title='log_in', message='Неверный номер телефона',
                               form=form, list=[form.phone_number, form.password])
    return render_template('log_in.html', title='log_in', message='',
                           form=form, list=[form.phone_number, form.password])


@app.route('/')
def base():
    return render_template('essential.html', list_of_ad=list_of_ad, user=USER)


if __name__ == '__main__':
    db_session.global_init('db/users.db')
    session = db_session.create_session()
    list_of_ad = [['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS'],
                  ['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS'],
                  ['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS'],
                  ['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS'],
                  ['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS'],
                  ['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS'],
                  ['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS'],
                  ['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS'],
                  ['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS'],
                  ['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS'],
                  ['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS'],
                  ['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS'],
                  ['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS'],
                  ['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS'],
                  ['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS'],
                  ['static/img/img.png', 'NAME', 'ADDRESS'], ['static/img/img.png', 'NAME', 'ADDRESS']
                  ]
    USER = None
    app.run(port=8080, host='127.0.0.1')
