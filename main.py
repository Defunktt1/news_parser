from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from base import Base
from bi_market_info_block import News

import json

# get data from json config file
with open('config.json') as c:
    config = json.load(c)

# get database config
db_config = config['database']

# set connection to database
engine = create_engine(
    'postgresql://{0}:{1}@{2}:{3}/{4}'.format(
        db_config['username'],
        db_config['password'],
        db_config['host'],
        db_config['port'],
        db_config['database']
    )
)

# check if module was connected to database
try:
    engine.connect().close()
    print('connected')
# or raise exception
except OperationalError as e:
    exit(e)

# create tables by models if not exist
Base.metadata.create_all(engine, checkfirst=True)

