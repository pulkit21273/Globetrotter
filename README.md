**📌 Project Documentation – GlobeTrotter**


A step-by-step guide to understanding the backend architecture of my project.

**Tech Stack**
_Backend_
Backend Framework: Sanic (Fast, async Python web framework)
Database: PostgreSQL (Relational Database)
ORM: SQLAlchemy (For database interaction)
API Format: REST API with JSON payloads




**🚀 How the Game Works (Backend Flow)**


_User Creation_

The user enters a username (min length=8 and max length=20)
Backend stores the user in PostgreSQL.
Returns a user ID to track progress.

_Fetching a New Question_

The game requests a new question.
The backend selects respective clues from the database.
Sends a list of clues and 4 options.

_Answer Submission & Validation_

User selects an answer.
Backend validates the answer and updates the score.
Returns whether the answer was correct or incorrect.
If correct, a fun fact is included in the response.

_Fetching User Score_

The frontend requests the user’s current score.
The backend fetches score data from the database.

_Hint System_

User can request a hint.
The backend returns a trivia hint for the current question.




**Endpoints**

POST /users/create_user
POST /game/question
POST /game/correct_answer
GET /game/score?user_id=1
GET /game/hint?clue_id=8




**Game Rules**

You will be given clues to guess a destination.
You can use 1 hint.
Select the correct answer from multiple options.


**Scoring System**

+10 points if you guess correctly without additional hint.
+5 points if you guess correctly with 1 hint.
-5 points if you answer incorrectly.
