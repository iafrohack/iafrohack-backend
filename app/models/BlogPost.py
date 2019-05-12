
from sqlalchemy import Column, Integer, JSON
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class BlogPost(Base):
    __tablename__ = 'blog_posts'
    id = Column(Integer, primary_key=True)
    status_id = Column(Integer, nullable=False)
    category_id = Column(Integer, nullable=False)
    content = Column(JSON, nullable=False)

    def __repr__(self):
        return '<BlogPost %r>' % self.content
