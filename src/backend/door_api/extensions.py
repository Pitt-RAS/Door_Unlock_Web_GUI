from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy, event
from sqlalchemy.engine import Engine

db = SQLAlchemy()
ma = Marshmallow()


@event.listens_for(Engine, 'connect')
def _sqliteEnableForeignKeys(dbConnection, connectionRecord):
    cursor = dbConnection.cursor()
    cursor.execute('PRAGMA foreign_keys=ON')
    cursor.close()
