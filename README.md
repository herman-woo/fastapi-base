# FastAPI-Base
Custom Boilerplate for setting up any future FastAPI.
Domain Driven Design for Restful API.

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
uvicorn main:app --host 0.0.0.0 --port 8000

 - For running in production
 ```
fastapi run
 ```
 ## Data Migration w/ Alembic