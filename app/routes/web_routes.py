from flask import Blueprint # make group of routes directly used in app.py without complicating file
from flask import redirect,Response,url_for,request,render_template,session
from forms.input_form import user_input,url_input,user_login  #this is used to called the form or used to form the Object of that form
from app.models.user_table import Users    # this is used to import the database to connect with form in routes to store data 
from app import db    # this used to say in which database the the table and the value add
# Form using : -- 

# 1 import the form from that module 
# 2 create the object of it 
# 3 then pass the object name in return with login.html 
# 4 use that variable name that you pass in login page to get the form info 
# 5 then store ti in table then database by creating the obj of that  table / model

web_bp = Blueprint("web", (__name__))

@web_bp.route("/", methods=["GET", "POST"])
def login():
    obj_for_userloginform = user_login()
    if request.method == "POST":
        email = obj_for_userloginform.data  # this get the input from form for login and store 

        user = Users.query.filter_by(emailid=email).first()   # check that email id with database email_id variable

        if user:    # if found 
            session["user_id"] = user.id   # store this id (not email_id) in session 
            return redirect(url_for("web.analyze"))
        else:
            return "User not found"

    return render_template("login.html",form = obj_for_userloginform)


@web_bp.route("/registration" , method= ["GET","POST"])    #this is login page 
def registration():
   obj_of_userinputform = user_input()  #creting the object of that form to use initialize the obj with name and then pass it with login
   if request.method == "POST": 
     username = obj_of_userinputform.username.data   #we get the data from the object in that from form variale to route variable
     email  =  obj_of_userinputform.email.data      #                                    mostly used same variable name to minimize conflict
     
     user = Users(           # this obj of the table name = user 
       username = username,
       emailid = email 
#dtabase variable  = route variable
     )
     db.session.add(user)    # we commad that  store that table obj in db name databse 
     db.session.commit()


     return redirect(url_for("web.login"))  # nor,a
   
   return render_template("registration.html",form = obj_of_userinputform)  #with login html we pass that form it is mandatorey







@web_bp.route("/analyze" , method = ["POST"])
def analyze():
  obj_of_url_input = url_input()  #this used to get the form for url on that page 
  if request.method == "POST" :
   

  
   return redirect(url_for("web.result"))

  return render_template("analyze.html")



@web_bp.route("/result" , method= ["POST" "GET"]) 
def result():
 

 return render_template("result.html")