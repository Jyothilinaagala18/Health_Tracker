from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from email_validator import validate_email, EmailNotValidError

# Custom Email Validator
def email_validator(form, field):
    try:
        # Validate email
        validate_email(field.data)
    except EmailNotValidError as e:
        # Raise validation error with the appropriate message
        raise ValidationError(str(e))

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)], render_kw={"placeholder": "Username"})
    email = StringField('Email',
                        validators=[DataRequired(), email_validator], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password', 'Passwords must match')],
                                     render_kw={"placeholder": "Confirm Password"})

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), email_validator], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[DataRequired()], render_kw={"placeholder": "Password"})
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
