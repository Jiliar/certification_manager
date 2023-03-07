from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.utils.config import Config as config
        
connection_string = "mysql+mysqldb://{0}:{1}@{3}:{4}/{2}"
connection_string = connection_string.format(config.get_param('db', 'user'),
                                             config.get_param('db', 'password'),
                                             config.get_param('db', 'database'),
                                             config.get_param('db', 'server'),
                                             config.get_param('db', 'port'))
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()