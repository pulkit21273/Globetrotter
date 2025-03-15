import json
from sqlalchemy.orm import Session
from database.db import engine
from models.destination import Destination
from models.clue import Clue
from models.funfact import FunFact
from models.trivia import Trivia

# Load dataset
with open("globetrotter_dataset.json", "r", encoding="utf-8") as file:
    dataset = json.load(file)

# Open a session
session = Session(bind=engine)

try:
    for data in dataset:
        # Create Destination entry
        destination = Destination(city=data["city"], country=data["country"])
        session.add(destination)
        session.commit()

        # Insert Clues
        for clue_text in data["clues"]:
            clue = Clue(destination_id=destination.id, text=clue_text)
            session.add(clue)

        # Insert Fun Facts
        for fact_text in data["fun_fact"]:
            fact = FunFact(destination_id=destination.id, text=fact_text)
            session.add(fact)

        # Insert Trivia
        for trivia_text in data["trivia"]:
            trivia = Trivia(destination_id=destination.id, text=trivia_text)
            session.add(trivia)

        session.commit()

    print("Database seeded successfully!")

except Exception as e:
    session.rollback()
    print(f"Error seeding database: {e}")

finally:
    session.close()
