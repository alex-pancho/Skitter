from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo , ValidationError
from issuetracker import db
from issuetracker.models import User
from wtforms.ext.sqlalchemy.fields import QuerySelectField



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    FirstName = StringField('First Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    LastName = StringField('Last Name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class PostIssueForm(FlaskForm):


    Title = StringField('Title',
                            validators = [ DataRequired(), Length(min=2, max=100)])
    Description = TextAreaField('Description',
                            validators = [ DataRequired() ])
    Createdby = StringField('Createdby',
                            validators = [ DataRequired() ])
    AssignedTo = QuerySelectField('AssignedTo',
        query_factory=lambda: User.query, # you can add order_by(I am not sure)
        allow_blank=False)
        #StringField('AssignedTo', default=Createdby)#, validators = [ DataRequired() ])
    
    Status = BooleanField('Open Status' , default= True)
    submit = SubmitField('Post')

