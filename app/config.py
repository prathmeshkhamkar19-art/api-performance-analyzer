# step 1 of project
# in that create Variable for the secreate key and also create the path for database

class Config:
    SECRET_KEY = "a_random_secure_key_123"

    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://pratham:1234@localhost/api_analyzer"

    SQLALCHEMY_TRACK_MODIFICATIONS = False #We set SQLALCHEMY_TRACK_MODIFICATIONS = False to improve performance and avoid unnecessary tracking