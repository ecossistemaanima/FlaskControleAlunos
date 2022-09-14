from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

#Instanciar os dois objetos
db = SQLAlchemy()
migrate = Migrate()
