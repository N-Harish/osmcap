from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.fields.html5 import DateField
from wtforms_validators import AlphaNumeric
from osm.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(),Length(min=2,max=20)])
    email = StringField('Email',
                        validators=[DataRequired(),Email()])
    password = PasswordField('Password',
                             validators=[DataRequired(),Length(min=6,max=10)])
    confirm_password = PasswordField('Confirm Password',
                             validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exist. Please choose a different one.')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exist. Please choose a valid email')

    def validate_password(self,password):
        #user = User.query.filter_by(username=username.data).first()
        SpecialSym =['$', '@', '#', '%'] 
        if not any(char.isdigit() for char in password.data): 
            raise ValidationError('Password should have at least one numeral') 
        
        if not any(char.isupper() for char in password.data): 
            raise ValidationError('Password should have at least one uppercase letter') 
        
        if not any(char.islower() for char in password.data): 
            raise ValidationError('Password should have at least one lowercase letter') 
            
        if not any(char in SpecialSym for char in password.data): 
            raise ValidationError('Password should have at least one of the symbols $@#') 
            
    


class LoginForm(FlaskForm):
    username = StringField('Username', 
                            validators=[DataRequired(),Length(min=2,max=20)])
    password = PasswordField('Password',
                             validators=[DataRequired(),Length(min=6,max=10)])
    #remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')

    def validate_password(self,password):
        #user = User.query.filter_by(username=username.data).first()
        SpecialSym =['$', '@', '#', '%'] 
        if not any(char.isdigit() for char in password.data): 
            raise ValidationError('Password should have at least one numeral') 
        
        if not any(char.isupper() for char in password.data): 
            raise ValidationError('Password should have at least one uppercase letter') 
        
        if not any(char.islower() for char in password.data): 
            raise ValidationError('Password should have at least one lowercase letter') 
            
        if not any(char in SpecialSym for char in password.data): 
            raise ValidationError('Password should have at least one of the symbols $@#') 

class InfoForm(FlaskForm):
    subject = StringField('Enter Subject',
                           validators=[DataRequired()])
    branch = StringField('Enter Branch',
                          validators=[DataRequired()])
    semester = StringField('Enter Semester',
                            validators=[DataRequired()])
    sem_type = SelectField('Select Sem-type',
                            choices=[('C.B.C.G.S.','C.B.C.G.S.'),('C.B.S.G.S.','C.B.S.G.S.')],
                            validators=[DataRequired()])
    paper_type = SelectField('Enter Paper-type',
                            choices=[('Regular','Regular'),('K.T.','K.T.')],
                            validators=[DataRequired()])                        
    date_accessed = DateField('Enter Date',validators=[DataRequired()])
    faculty = StringField('Enter Faculty',
                          validators=[DataRequired()])
    target = IntegerField('Enter Target',
                          validators=[DataRequired('Requires numeric values')])
    paper_accessed = IntegerField('Paper Accessed',
                                  validators=[DataRequired()])
    paper_moderated = IntegerField('Paper Moderated',
                                default=0)
    submit = SubmitField('Submit')
    