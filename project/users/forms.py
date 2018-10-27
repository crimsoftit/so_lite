from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    username = TextField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegForm(FlaskForm):
    username = TextField(
            "username",
            validators=[DataRequired(), Length(min=3, max=25)]
        )
    email = TextField(
            "email",
            validators=[DataRequired(), Email(message=None), Length(min=6, max=40)]
        )
    password = PasswordField(
            "password",
            validators=[DataRequired(), Length(min=6, max=25)]
        )
    confirm = PasswordField(
            "repeat password",
            validators=[DataRequired(), EqualTo("password", message="passwords MUST match")]
        )
