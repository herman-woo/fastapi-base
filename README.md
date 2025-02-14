# FastAPI-Base
Custom Boilerplate for setting up any future FastAPI

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
 - For Using and Existing Requirements Doc
 ```
   - pip install -r requirements.txt
   ```
 - Capturing the Requirements.txt
 ```
   - pip freeze > requirements.txt
   ```
 - Deactivate the virtual env (wont need to in VSCode, just close the window)
 ```
   - deactivate
```
 ## Architecture
 - main.py


 ## Running FastAPI
- fastapi dev main.py

 ## Data Migration w/ Alembic