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
 

  *(PHASE 4)
 ## 🔧 Challenges & Solutions  
 
 * Package install - cryptography   used for pymysql drive
  
  1.

 ### Circular Import Issue in Flask

While structuring the Flask application, a circular import error occurred between the application initialization file and the database models.

**Problem:**
- Models were importing the database instance (`db`) from the main app module
- The app module was simultaneously importing models
- This caused a circular dependency and prevented the application from starting

**Solution:**
- Implemented the Flask App Factory pattern
- Used relative imports (`from .. import db`) inside models
- Moved model imports inside the `create_app()` function to ensure proper initialization order

**Outcome:**
- Resolved import conflicts
- Improved project structure and scalability


2.

### Database Integration & Configuration Issues

While connecting the Flask application with MySQL using SQLAlchemy, multiple database-related issues were encountered during setup and initialization.

**Problems:**
- Missing required dependencies for MySQL connection (`flask_sqlalchemy`, `cryptography`)
- MySQL authentication errors (invalid username/password)
- Incorrect database URI formatting
- Database not existing before table creation
- Foreign key reference errors due to mismatched table names
- Case-sensitive mistakes in SQLAlchemy methods (e.g., `Foreignkey` vs `ForeignKey`)

**Solutions:**
- Installed required dependencies (`flask_sqlalchemy`, `pymysql`, `cryptography`)
- Verified MySQL credentials and used correct username (`root`)
- Corrected the database connection string format
- Manually created the database before running `db.create_all()`
- Ensured foreign key references matched correct table names
- Fixed syntax and case-sensitivity issues in SQLAlchemy models

**Outcome:**
- Successfully established connection between Flask and MySQL
- Database and tables created without errors
- Improved understanding of SQLAlchemy ORM and database workflows

__________________________________________________________________________________________________________________________________________________
