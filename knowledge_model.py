from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'articles'
	article_id = Column(Integer, primary_key=True)
	name = Column(String)
	topic = Column(String)
	link = Column (String)
	rating = Column(Integer)
	
	def __repr__(self):
   		return("This article {}\n" "is about {}\n" "and is rated {}\n."
   				"click link to read {}\n").format(
   				self.name,
   				self.topic,
   				self.rating,
   				self.link)