# this table is used to store the information that comes from the api that user send 
#like  - time taken(responce) ,status code

from .. import db   #either using app we use ( .. ) this go back folder 

class apilog_table(db.Model):  #this create thetable for apilog_table
    id =db.Column(db.Integer,primary_key = True)
    api_url = db.Column(db.String(255),nullable = False)
    status_code = db.Column(db.Integer)
    reponse_time = db.Column(db.Float)
    average_time = db.Column(db.Float)
    min_time =     db.Column(db.Float)
    max_time =     db.Column(db.Float)
    Total_request_send  = db.Column(db.Integer)
    server          =  db.Column(db.String(50))
    location        =  db.Column(db.String(50))
    

    #foreign_key which store the primary key of 'user table'
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))   #case sensitive use lower case only even table is pascal case