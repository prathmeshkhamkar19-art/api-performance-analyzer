# this is form file used to get input from using flask-wtf

from flask_wtf import Flaskform  # Flaskform is class from parent flask_wtf class
from wtforms import StringField,EmailField,PasswordField,URLField,SubmitField   #this is function 
from wtforms.validators import DataRequired,ValidationError,Email,URL

class user_input(Flaskform):  #need to inherit the class to use form

    name = StringField(label= "Enter the name :", validators= [DataRequired()])    #this use to take input username as name  (database)
    email = EmailField(label= "Enter the Email" , validators=[ DataRequired(),Email()])   # this takle input for emailid as email (database)
    submit = SubmitField(label="Submit")
    
    
class url_input(Flaskform):

    url = URLField(label="Enter the URL...",validators=[ DataRequired(),URL(message="Please enter a valid URL")])
    submit = SubmitField("Analyze")