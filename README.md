****🌍 ✈️ GlobeTrotter – The Ultimate Travel Trivia Game****



🚀 Test your geography knowledge! Guess destinations based on clues, use hints wisely, and compete for the highest score!


----------------------------------------------------------------------------------

## 🚨 MESSAGE FROM RENDER (Backend Host) 🚨  

### **⚠️ Your free instance will spin down with inactivity, which can delay requests by 50 seconds or more.**  

Due to inactivity, it will spin down and may take a few seconds when used after a certain time (one-time up duration).  

**Please don't consider it as an issue, as I am using a Free hosting plan.**

----------------------------------------------------------------------------------

🎯 Game Rules  

- Guess the destination using provided clues.  
- Use up to one hint (but it reduces your score).  
- Select the correct answer from multiple options.  


****🏆 Scoring System****

- ✅ Correct Answer (No Hint) → +10 points
- ✅ Correct Answer (With 1 Hint) → +5 points
- ❌ Incorrect Answer → -5 points


💡 Pro Tip: Try to guess without hints to maximize your score!



----------------------------------------------------------------------------------



**🛠 Tech Stack**

**Backend**
- Framework: Sanic (Fast, async Python web framework)
- Database: PostgreSQL (Relational Database)
- ORM: SQLAlchemy (For seamless database interactions)
- API Format: REST API with JSON payloads



----------------------------------------------------------------------------------



****🎮 Game Flow (Backend Process)****

_**👤 User Creation :**_

- 1️⃣ Player enters a username (min: 8, max: 20 characters).
- 2️⃣ Backend stores user details in PostgreSQL.
- 3️⃣ Returns a unique user ID to track game progress.

_**❓ Fetching a New Question :**_

- 1️⃣ The game requests a new question from the backend.
- 2️⃣ Backend selects clues from the database.
- 3️⃣ Sends a list of clues and four answer options.

_**✅ Answer Submission & Validation :**_

- 1️⃣ User selects an answer.
- 2️⃣ Backend validates the answer & updates the score.
- 3️⃣ Returns correct/incorrect status.
- 4️⃣ If correct, a fun fact is included in the response.

_**📊 Fetching User Score :**_

- 1️⃣ Frontend requests the user’s current score.
- 2️⃣ Backend fetches score data from the database.

_**💡 Hint System :**_

- 1️⃣ User can request a hint for help.
- 2️⃣ Backend returns a trivia hint related to the question.



----------------------------------------------------------------------------------



****🌐 API Endpoints****

_**Method	Endpoint	Description**_

1. User Creation :
POST /users/create_user → Create a new user

2. Fetching a New Question :
POST /game/question → Fetch a new question with clues & options

3. Answer Submission & Validation :
POST /game/correct_answer → Validate answer & update score

4. Fetching User Score :
GET /game/score?user_id={id} → Retrieve user score

5. Hint System :
GET /game/hint?clue_id={id} → Fetch a hint for the current question


----------------------------------------------------------------------------------



**🗂 Tables Created**
- users – Stores user data (ID, username, scores
- destinations – Stores destinations (city, country)
- clues – Stores clues to guess destinations
- fun_facts – Stores fun facts about each destination
- trivia – Stores trivia (extra hints) about each destination

Storing Trivia, Clues, Funfacts in separate tables **enhances scalability** by allowing easy extension of features—for eg, adding an **image_clues** table without modifying existing structures.  This also helps maintain data clarity, avoid redundancy, and optimize retrieval based on its specific use case in the game.




----------------------------------------------------------------------------------



**Globetrotter dataset JSON generation :**

I have used few-shot and one-shot methods in GPT3.5 to generate unique and accurate dataset for the game, and along with that I allowed it to access the internet also to maintain fact-correctness.



