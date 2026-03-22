from flask import Blueprint # make group of routes directly used in app.py without complicating file
from flask import redirect,Response,url_for,request,render_template
from forms.input_form import user_input,url_input  #this is used to called the form or used to form the Object of that form


web_bp = Blueprint("web", (__name__))

@web_bp.route("/" , method= ["GET","POST"])    #this is login page 
def login():
   obj_of_userinputform = user_input()
   if request.method == "POST": 


     return redirect(url_for("web.analyze"))  # nor,a
   
   return render_template("login.html")

@web_bp.route("/analyze" , method = ["POST"])
def analyze():
  if request.method == "POST" :

  
   return redirect(url_for("web.result"))

  return render_template("analyze.html")



@web_bp.route("/result" , method= ["POST" "GET"]) 
def result():
 

 return render_template("result.html")