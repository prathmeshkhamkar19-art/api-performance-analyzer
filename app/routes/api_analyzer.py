from app.service.analyze import api_aalyzer_service

from flask import Blueprint,request   #Blueprint make group of all route then to use this routes simply write
                #app.register_blueprint(api_bp)


 # this is my api that 
api_bp = Blueprint("api", (__name__))

@api_bp.route("/Analyzer", methods="POST")
def analyzer():
    url = request.json.get("url")    #get the url using json to

    result = api_analyze_service()
    
    return result , 200  #return result in json file 