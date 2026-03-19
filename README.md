# api-performance-analyzer
A Flask-based tool that analyzes API response time and performance.
## Development Phases

✅ Phase 1 — Project Idea  
✅ Phase 2 — Project Structure  
✅ Phase 3 — Flask Initialization  
✅ Phase 4 — Database Models  
⬜ Phase 5 — API Routes  
⬜ Phase 6 — API Analyzer Logic  
⬜ Phase 7 — Final Demo


_______________________________________________________________________________________________________________________________________________

*Phase 3 - Flask Initialization 
 
 *Package install 
    - Flask        (pip install flask)
    - SQLALchemy   (pip install flask_sqlalchemy)
    - pymysql      (pip install pymysql)

- config.py - 
     
     Write code in config.py that create the SECRET_KEY and the path or uri for database also install pymysql package
- __init__.py -

    In __init__.py i import flask,sqlalchemy and config
      - then create the object of database(globly)
      - get the variable or all data from config in app line(app.config.form_object(app))
      -connect databse with app line(db.init_app(app))
      - then return the app
- run.py - 
    - import the create_app function from app
    - then get the output in app variable which is return from the create_app function 
    - and run it 

_______________________________________________________________________________________________________________________________________________

*phase 4 - Database models
 
 *No Package installed 

  - in models folder
    - created new file to create the table importing the db from app with class
    - 1 file create to store data of user and other for apilog
    - in user file/table it is show rearion to many ap request (one to many) thats why we created reationship column in it 
    - name as api_logs
    -in aplog_table file/table we show extra col foreign key to connect the table with primarey key of user_table.py
 
  - in create_database.py 
     - to create the table we need app to start and create the table in that databse 
     - se we also need database
     -from app import create_app() #function and db 
     - then using with app_context() function tell the we working on same env where the app already exist 
     -then create the function in database (db) using db.create_all() function 


__________________________________________________________________________________________________________________________________________________