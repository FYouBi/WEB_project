from flask import Flask, render_template, url_for, redirect, request
import datetime

from werkzeug.datastructures import CombinedMultiDict
from data.ads import Ads
from forms import LoginForm, RegisterForm, CreateAd, List
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def check_password(data):
    if len(data) < 8:
        return 'Мало символов(Нужно больше 8)'
    elif ('%' in data) or ('@' in data) or ('#' in data) or ('$' in data) or ('!' in data) or ('^' in data) or \
            ('&' in data) or ('*' in data) or ('=' in data) or ('+' in data) or ('-' in data) or ('`' in data) \
            or (' ' in data):
        return 'Недопустимые символы'
    elif len(data) > 30:
        return 'Слишком много символов(Нужно меньше 30)'
    elif data.isdigit():
        return 'Нужны буквы'
    elif data.isalpha():
        return 'Нужны цифры'
    return True


def check_phone(data):
    data = data[1::] if data[0] == '+' else data
    if len(data) < 16:
        for i in data:
            if not i.isdigit():
                return False
        return True
    else:
        return False


@app.route('/register', methods=['GET', 'POST'])
def register():
    global USER
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data

        if [user for user in session.query(User).filter(User.phone_number == data['phone_number'])]:
            return render_template('register.html', title='Авторизация', form=form,
                                   message='Данный номер телефона уже зарегистрирован')
        if not check_phone(data['phone_number']):
            return render_template('register.html', title='Авторизация', form=form,
                                   message='Неверный формат номера')
        if type(check_password(data['password'])) != bool:
            return render_template('register.html', title='Авторизация', form=form,
                                   message=f'{check_password(data["password"])}')
        new_user = User(name=data['name'],
                        phone_number=data['phone_number'],
                        password=data['password'],
                        address=data['address'])
        session.add(new_user)
        USER = [user for user in session.query(User).filter(User.phone_number == data['phone_number'])][0]
        session.commit()
        return redirect('/')
    return render_template('register.html', title='Авторизация', form=form, message='')


@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    global USER
    form = LoginForm()
    if form.validate_on_submit():
        phone_number, password = form.data['phone_number'], form.data['password']
        for user in session.query(User).all():
            if str(user.phone_number) == phone_number:
                if user.password == password:
                    USER = \
                        [user for user in session.query(User).filter(User.phone_number == form.data['phone_number'])][0]
                    session.commit()
                    return redirect('/')
                return render_template('log_in.html', title='log_in', message='Неверный пароль',
                                       form=form)
        return render_template('log_in.html', title='log_in', message='Неверный номер телефона',
                               form=form)
    return render_template('log_in.html', title='log_in', message='',
                           form=form)


@app.route('/create_ad', methods=['GET', 'POST'])
def create_ad():
    form = CreateAd()
    if form.validate_on_submit():
        file = form.image.data
        new_ad = Ads(image=file, name=form.data['name'], description=form.data['description'],
                     type=form.select.data, user=USER)
        session.add(new_ad)
        session.commit()
        return redirect('/')
    return render_template('create_ad.html', form=form, user=USER)


@app.route('/view_ad/<int:id>')
def view_ad(id):
    ad = list_of_ad[id - 1]
    return render_template('view_ad.html', img=ad[1], name=ad[2], description=ad[3], author=ad[5])


@app.route('/', methods=['GET', 'POST'])
def base():
    form = List()
    k = 'all'
    if form.validate_on_submit():
        print(form.select.data)
        k = form.select.data
    list_of_ad = update_list(k)
    return render_template('essential.html', list_of_ad=list_of_ad, user=USER, form=form)


def update_list(k):
    global list_of_ad
    list_of_ad = []
    if k != 'all':
        for ad in session.query(Ads).filter(Ads.type == k):
            list_of_ad.append([ad.id, ad.image, ad.name, ad.description, ad.user.address, ad.user])
    else:
        for ad in session.query(Ads).all():
            list_of_ad.append([ad.id, ad.image, ad.name, ad.description, ad.user.address, ad.user])
    return list_of_ad


if __name__ == '__main__':
    db_session.global_init('db/users.db')
    session = db_session.create_session()
    list_of_ad = []
    update_list('all')
    USER = None
    app.run(port=8080, host='127.0.0.1')
