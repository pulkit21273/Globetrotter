from database.db import engine, Base
from models.user import User
from models.destination import Destination
from models.clue import Clue  
from models.funfact import FunFact  
from models.trivia import Trivia 

# Create all tables in the database
# Base.metadata.create_all(engine, tables=[User.__table__])
Base.metadata.create_all(engine)

print("All database tables created successfully!")
