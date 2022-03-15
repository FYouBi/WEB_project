from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, TextAreaField, \
    RadioField, SelectField, PasswordField, FileField, EmailField
from wtforms.validators import DataRequired


class LoginForm_(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    education = SelectField('Ваше образование', choices=[('общее', 'общее'),
                                                         ('среднее', 'среднее'), ('высшее', 'высшее')])
    radio_prof = RadioField('Ваша специальность', choices=['инженер-исследователь', 'врач', 'климатолог',
                                                           'пилот', 'строитель', 'экзобиолог', 'киберинженер'])
    radio_sex = RadioField('Ваш пол', choices=['Мужской', 'Женский'])
    comment = TextAreaField('Почему вы хотите принять участие в миссии?')
    remember_me = BooleanField('Готовы ли вы остаться на Марсе?')
    submit = SubmitField('Войти')


class Protection(FlaskForm):
    id_1 = StringField('id астронавта', validators=[DataRequired()])
    password_1 = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_2 = StringField('id капитана', validators=[DataRequired()])
    password_2 = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


class LoadPhoto(FlaskForm):
    photo = FileField('Приложите фотографию', validators=[DataRequired()])
    submit = SubmitField('Отправить')


class RegisterForm(FlaskForm):
    login_email = StringField('login/email', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    repeat_password = StringField('repeat password', validators=[DataRequired()])
    surname = StringField('surname', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    age = StringField('age', validators=[DataRequired()])
    position = StringField('position', validators=[DataRequired()])
    speciality = StringField('speciality', validators=[DataRequired()])
    address = StringField('address', validators=[DataRequired()])
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')
