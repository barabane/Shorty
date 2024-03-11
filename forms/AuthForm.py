from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField
from wtforms.validators import Email, DataRequired, Length


class AuthForm(FlaskForm):
    email = EmailField('email', validators=[
        DataRequired(message='Введите Email'),
        Email(message='Введите валидный Email')
    ])
    password = PasswordField('password', validators=[
        DataRequired(message='Введите пароль'),
        Length(min=8, message='Минимальная длинна пароля 8 символов'),
        Length(max=20, message='Максимальная длинна пароля 20 символов')
    ])
