from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import json

with open('config.json') as c:
    config = json.load(c)

db_config = config['database']
engine = create_engine(
    'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        db_config['username'],
        db_config['password'],
        db_config['host'],
        db_config['port'],
        db_config['database']
    )
)

Session = sessionmaker(bind=engine)

Base = declarative_base()
