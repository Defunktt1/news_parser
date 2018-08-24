"""
News model
"""

from sqlalchemy import Column, Integer, DateTime, VARCHAR, String
from base import Base
import datetime


class News(Base):
    __tablename__ = 'bi_market_info_block'

    id = Column(Integer, primary_key=True)
    load_date = Column(DateTime, default=str(datetime.datetime.now()), nullable=False)
    source_site_code = Column(VARCHAR(20), nullable=False)
    news_date = Column(DateTime, nullable=False)
    news_header = Column(VARCHAR(4000), nullable=False)
    news_snippet = Column(VARCHAR(1000), nullable=False)
    news_body_type = Column(VARCHAR(20), nullable=False)
    news_body = Column(String, nullable=False)
    news_source = Column(VARCHAR(4000), nullable=True)
    news_picture = Column(VARCHAR(4000), nullable=True)
    news_ref = Column(VARCHAR(4000), nullable=False)
