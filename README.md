# FastAPI-Base
Custom Boilerplate for setting up any future FastAPI.
Domain Driven Design for Restful API.

## Preamble
I've built in Django before and it was incredibly helpful with it's batteries included mindset. I found getting off the ground running with FastAPI to be a bit more difficult since its far less opinionated and requires for me to make more decisions.

So for any future FastAPI projects I may build, i wanted to create a starter kit. This kit is one that mainly uses the SQLModel and Alembic to essentailly help with the database/ORM side of things.

So this repository will be filled with comments (more in the future), and documentation to help me remember important things

## Setup
1. Create an ENV
- 
2. Create a Virtual Python Environment
 - python -m venv .venv
 - source .venv/bin/activate
 - .venv\Scripts\activate

3. Install FastAPI dependencies
 - For Fresh install
 ```
 pip install "fastapi[standard]" sqlmodel alembic
 ```

 - For Using an Existing Requirements Doc
 ```
pip install -r requirements.txt
```

 - Capturing the Requirements.txt
 ```
pip freeze > requirements.txt
```

 - Deactivate the virtual env (wont need to in VSCode, just close the window)
```
deactivate
```

 ## Architecture
|- main.py (entry for the api)
|- db.py (configuration to setup database sessions)


 ## Running FastAPI
 - For running in Dev mode
 ```
fastapi dev main.py

 ```

 - For running with uvicorns
 ```
uvicorn main:app --reload

 ```
uvicorn main:app --host 0.0.0.0 --port 8080

 - For running in production
 ```
fastapi run
 ```
 ## Data Migration w/ Alembic