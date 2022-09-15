from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class BlogModel(Base):
    """
        This model is for make the mapping between hubtran to shipwell objects
        (Tables in Confluence)
    """
    __tablename__ = 'posts'
    index = Column(Integer, primary_key=True, index=True)
    id = Column(String)
    title = Column(String)
    body = Column(String)
    created = Column(String)
    author_id = Column(Integer)
    username = Column(String)