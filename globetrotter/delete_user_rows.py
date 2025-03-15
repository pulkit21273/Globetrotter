from database.db import engine
from models.user import User
from sqlalchemy.orm import sessionmaker


Session = sessionmaker(bind=engine)
session = Session()

session.query(User).delete()

session.commit()

print("All rows from the 'User' table have been deleted successfully")
