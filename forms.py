from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
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
    name = StringField('Имя', validators=[DataRequired()])
    # surname = StringField('Фамилия', validators=[DataRequired()])
    phone_number = StringField('Номер телефона', validators=[DataRequired()])
    password = StringField('Пароль', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    submit = SubmitField('Войти')


class LoginForm(FlaskForm):
    phone_number = EmailField('Номер телефона', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class CreateAd(FlaskForm):
    image = FileField('Приложите фотографию', validators=[DataRequired(), FileAllowed(['jpg', 'png'], 'Images only!')])
    name = StringField('Название', validators=[DataRequired()])
    description = TextAreaField('Описание', validators=[DataRequired()])
    select = SelectField('Название', choices=[('doc', 'Документы'),
                                              ('animal', 'Животные'), ('technical', 'Техника'),
                                              ('other', 'Другое')])
    submit = SubmitField('Разместить')


class List(FlaskForm):
    select = SelectField('Название', choices=[('all', 'Всё'), ('doc', 'Документы'),
                                              ('animal', 'Животные'), ('technical', 'Техника'),
                                              ('other', 'Другое')])
    submit = SubmitField('Поиск')
