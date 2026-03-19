# this table is used to store the information that comes from the api that user send 
#like  - time taken(responce) ,status code

from app import db

class apilog_table(db.Model):  #this create thetable for apilog_table
    id =db.Column(db.Integer,primary_key = True)
    api_url = db.Column(db.String(255),nullable = False)
    status_code = db.Column(db.Integer)
    reponse_time = db.Column(db.Float)
    

    #foreign_key which store the primary key of 'user table'
    user_id = db.Column(db.Integer,db.Foreignkey('user.id'))