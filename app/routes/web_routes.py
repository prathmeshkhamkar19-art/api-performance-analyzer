from flask import Blueprint # make group of routes directly used in app.py without complicating file
from flask import redirect,Response,url_for,request,render_template,session
from app.forms.input_form import user_input,url_input,user_login  #this is used to called the form or used to form the Object of that form
from app.models.user_table import Users   # this is used to import the database to connect with form in routes to store data 
from app.models.apilog_table import APIlog
from app import db    # this used to say in which database the the table and the value add
from app.service.analyze import api_analyze_service   #this is for use logic for performance analyse
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
        email = request.form.get("email")  # ERROR OCCUR ***   You passed a **dictionary instead of a single 
        #                                   value (like a string)**   to the database query, so SQLAlchemy couldn’t process it.


        user = Users.query.filter_by(emailid=email).first()   # check that email id with database email_id variable

        if user:    # if found 
            session["user_id"] = user.id   # store this id (not email_id) in session 
            return redirect(url_for("web.analyze"))
        else:
            return "User not found"

    return render_template("login.html",form = obj_for_userloginform)


@web_bp.route("/registration" , methods= ["GET","POST"])    #this is login page 
def registration():
   obj_of_userinputform = user_input()  #creting the object of that form to use initialize the obj with name and then pass it with login
   if request.method == "POST": 
     
     username = obj_of_userinputform.username.data   #we get the data from the object in that from form variale to route variable
     email  =  obj_of_userinputform.email.data      #                                    mostly used same variable name to minimize conflict
     
     existing_user = Users.query.filter_by(emailid=email).first()
     
     if existing_user :
        return "email already register "
     else :
        user = Users(           # this obj of the table name = user 
          username = username,
          emailid = email #dtabase variable  = route variable 
        )
        db.session.add(user)    # we commad that  store that table obj in db name databse 
        db.session.commit()


     return redirect(url_for("web.login"))  # nor,a
   
   return render_template("registration.html",form = obj_of_userinputform)  #with login html we pass that form it is mandatorey







@web_bp.route("/analyze" , methods = ["GET","POST"])
def analyze():
  obj_of_url_input = url_input()  #this used to get the form for url on that page 
  if request.method == "POST" :
   
   url = obj_of_url_input.url.data
   count = request.form.get("requests")

   try:
      count = int(count)
   except (TypeError, ValueError):
    count = 10

   data = api_analyze_service(url,count)
   
   new_record = APIlog(   api_url=data["api_url"],
    status_code=data["status_code"],
    reponse_time=data["response_time"],
    average_time=data["average_time"],
    min_time=data["min_time"],
    max_time=data["max_time"],
    Total_request_send=data["Total_request_send"],
    server=data["server"],
    location=data["location"]
       )
   db.session.add(new_record)
   db.session.commit()

   return redirect(url_for("web.result"))

  return render_template("analyze.html",form = url_input())



@web_bp.route("/result" , methods= ["POST","GET"]) 
def result():
 

 return render_template("result.html")