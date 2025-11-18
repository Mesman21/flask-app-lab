from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, Regexp


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[
        DataRequired(),
        Length(min=4, max=23)
    ])

    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])

    phone = StringField('Phone', validators=[
        DataRequired(),
        Regexp(r'^\+380\d{9}$', message='Невірний формат. Використовуйте +380XXXXXXXXX')
    ])

    subject = SelectField('Subject', choices=[
        ('general', 'Загальне питання'),
        ('project', 'Співпраця по проекту'),
        ('other', 'Інше')
    ], validators=[DataRequired()])

    message = TextAreaField('Message', validators=[
        DataRequired(),
        Length(max=500)
    ])

    submit = SubmitField('Send')


class LoginForm(FlaskForm):
    username = StringField('Username/Email', validators=[DataRequired()])

    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=4, max=23)
    ])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Sign In')