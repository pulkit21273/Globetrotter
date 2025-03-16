from database.db import engine, Base
from models.user import User
from models.destination import Destination
from models.clue import Clue  
from models.funfact import FunFact  
from models.trivia import Trivia 
from sqlalchemy import text


Base.metadata.drop_all(engine)


print("All tables dropped successfully")
