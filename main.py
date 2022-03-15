from flask import Flask, render_template, url_for, request, redirect
import datetime
from data.jobs import Jobs
from forms import LoginForm, Protection, LoadPhoto, RegisterForm
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        print(data)
        new_user = User(name=data['name'], surname=data['surname'],
                        age=int(data['age']), position=data['position'], hashed_password=data['password'],
                        speciality=data['speciality'], address=data['address'], email=data['login_email'])
        session.add(new_user)
        session.commit()
        return 'ok'
    return render_template('register.html', title='Авторизация', form=form)


@app.route('/authorization', methods=['GET', 'POST'])
def authorization():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        email, password = form.data['email'], form.data['password']
        for user in db_sess.query(User).all():
            if user.email == email:
                if user.hashed_password == password:
                    return render_template('base.html')
                return render_template('authorization.html', title='Authorization', message='Неверный пароль',
                                       form=form, list=[form.email, form.password])
        return render_template('authorization.html', title='Authorization', message='Неверный логин',
                               form=form, list=[form.email, form.password])
    return render_template('authorization.html', title='Authorization', message='',
                           form=form, list=[form.email, form.password])


@app.route('/')
def base():
    return render_template('base.html')


if __name__ == '__main__':
    db_session.global_init('db/users.db')
    session = db_session.create_session()
    app.run(port=8080, host='127.0.0.1')
