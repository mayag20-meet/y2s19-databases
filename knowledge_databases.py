from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(article_id, name, topic, link, rating):
	aricle_object=Knowledge(
		article_id = article_id,
		name=name,
        topic=topic,
        link =link,
        rating=rating)
	session.add(aricle_object)
	session.commit()

add_article(1,"python","computer scirnce","https://en.wikipedia.org/wiki/Python_(programming_language)",4)
add_article(2,"Pythonidae","animals","https://en.wikipedia.org/wiki/Pythonidae",7)
	

def query_all_articles():
	article = session.query(
		Knowledge).all()
	return article
print(query_all_articles())


def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
