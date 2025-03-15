from database.db import engine, Base
from models.user import User
from models.destination import Destination
from models.clue import Clue  
from models.funfact import FunFact  
from models.trivia import Trivia 


Base.metadata.drop_all(engine, tables=[User.__table__])

print("Tables dropped successfully")
