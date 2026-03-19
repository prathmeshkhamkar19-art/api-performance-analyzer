# in that file we seprately code logic to create the databse for any app
# to create the databse we need app and the database that we mentioned 

from app import create_app,db     #function and databse

app = create_app()  # this create the app geting from function

with app.app_context():    #this tell we create or working on same enviorment where this class already exist
    db.create_all()   # ead all models . convert it in table create the table in db
    print("Tables created!")
    hgh