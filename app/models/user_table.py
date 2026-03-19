#Phase 4  - create the models/Table 

#in this file we create the table to get the data from user like her name and the email addres 
# also try to create the registration option 
# first import the object of database that hold information of the path of databse (db) from app

from app import db

class users (db.Model):  # class = table
    id = db.Column(db.Integer,primery_key = True)     # variable = column
    username = db.Column(db.String(100) , nullable = False)
    emailid = db.Column(db.String(150), nullable = False , unique = True )

  # so one user send many api reuset ro check performanc then we create realtionship 
    api_logs = db.relationship('apilog_table', backtref = 'user', lazy = True)