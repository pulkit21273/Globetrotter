from database.db import engine
from models import User, FunFact, Trivia, Clue, Destination
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()

session.query(User).delete()
session.query(FunFact).delete()
session.query(Trivia).delete()
session.query(Clue).delete()
session.query(Destination).delete()

session.commit()

print("All rows from the 'User' table have been deleted successfully")
