from flask import Blueprint # make group of routes directly used in app.py without complicating file
from flask import redirect,Response,url_for,request,render_template
from forms.input_form import user_input,url_input  #this is used to called the form or used to form the Object of that form
from app.models.user_table import users    # this is used to import the database to connect with form in routes to store data 
from app import db    # this used to say in which database the the table and the value add
# Form using : -- 

# 1 import the form from that module 
# 2 create the object of it 
# 3 then pass the object name in return with login.html 
# 4 use that variable name that you pass in login page to get the form info 
# 5 then store ti in table then database by creating the obj of that  table / model

web_bp = Blueprint("web", (__name__))

@web_bp.route("/" , method= ["GET","POST"])    #this is login page 
def login():
   obj_of_userinputform = user_input()  #creting the object of that form to use initialize the obj with name and then pass it with login
   if request.method == "POST": 
     username = obj_of_userinputform.username.data   #we get the data from the object in that from form variale to route variable
     email  =  obj_of_userinputform.email.data      #                                    mostly used same variable name to minimize conflict
     
     user = users(           # this obj of the table name = user 
       username = username,
       emailid = email 
#dtabase variable  = route variable
     )
     db.session.add(user)    # we commad that  store that table obj in db name databse 
     db.session.commit()


     return redirect(url_for("web.analyze"))  # nor,a
   
   return render_template("login.html",form = obj_of_userinputform)  #with login html we pass that form it is mandatorey

@web_bp.route("/analyze" , method = ["POST"])
def analyze():
  if request.method == "POST" :

  
   return redirect(url_for("web.result"))

  return render_template("analyze.html")



@web_bp.route("/result" , method= ["POST" "GET"]) 
def result():
 

 return render_template("result.html")