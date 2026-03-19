# step 1 of project
# in that create Variable for the secreate key and also create the path for database
# install pymysql package 
class Config:
    SECRET_KEY = "a_random_secure_key_123"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:pratham%40001@localhost/api_analyzer"

    SQLALCHEMY_TRACK_MODIFICATIONS = False #We set SQLALCHEMY_TRACK_MODIFICATIONS = False to improve performance and avoid unnecessary tracking