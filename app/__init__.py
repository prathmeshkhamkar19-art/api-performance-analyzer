# step 2 of project 
#in that we create the function that create the app with importing the config.py file
#import flask and SQLALchemy and connect the database when we initialize or create the app
#create the object of that SQLALchemy (globaly)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config


db = SQLAlchemy() #THIS IS OBJECT with variable db

def create_app():  #this function we used to create any app only import to that file 
  
  app = Flask (__name__)
  app.config.from_object(Config)  #Import all uppercase variables from Config class into Flask app

  db.init_app(app)  #this connect the database to the app
  from .models import user_table,apilog_table   # ERROR solve- we moved becuse if we mwntion it on above it repwatedly 
                                                #import module (circulerly) but db in not initialize then how process go further

  return app 