# this is form file used to get input from using flask-wtf

from flask_wtf import Flaskform  # Flaskform is class from parent flask_wtf class
from wtforms import StringField,EmailField,PasswordField,URLField,SubmitField   #this is function 
from wtforms.validators import DataRequired,ValidationError,Email,URL

class user_input(Flaskform):  #need to inherit the class to use form

    name = StringField(label= "Enter the name :", validators= [DataRequired()])    #this use to take input username as name  (database)
    email = EmailField(label= "Enter the Email" , validators=[ DataRequired(),Email()])   # this takle input for emailid as email (database)
    submit = SubmitField(label="Submit")
    
    
class url_input(Flaskform):  #in analyze page need to create object of this class to get url

    url = URLField(label="Enter the URL...",validators=[ DataRequired(),URL(message="Please enter a valid URL")]) #this ios uesd to take input as url
    submit = SubmitField("Analyze")

class user_login(Flaskform) :
    email = StringField(label=" enter email to check" ,validators=[DataRequired(), Email()])  # that is for login page store email and check from db
    submit= SubmitField(label="submit")