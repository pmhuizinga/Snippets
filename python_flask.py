# DIRECTORY STRUCTURE
# main_folder/project.py : flask application instance

# main_folder/app/__init__.py : flask init file
# main_folder/app/routes.py : contains routing
# main_folder/app/models.py : contains database stuff (sqlalchemy)
# main_folder/app/forms.py :  contains form stuff

# main_folder/app/templates/.. : contains html files

# set flask app (in terminal): set FLASK_APP=project.py
# run flask app (in termina): flask run


# ADD DATABASE MIGRATION 
# requires a models.py file with tables as class
# import flask-migrate
# In terminal:
# create migrations dir: flask db init 
# migrate: flask db migrate -m "<table name> table"
# upgrade: flask db upgrade


