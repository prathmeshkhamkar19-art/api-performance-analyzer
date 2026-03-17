# api-performance-analyzer
A Flask-based tool that analyzes API response time and performance.
## Development Phases

✅ Phase 1 — Project Idea  
✅ Phase 2 — Project Structure  
⬜ Phase 3 — Flask Initialization  
⬜ Phase 4 — Database Models  
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