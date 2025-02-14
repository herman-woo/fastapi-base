# Setup
1. Create an ENV
- 
2. Create a Virtual Python Environment
 - python -m venv .venv
 - source .venv/bin/activate
 - .venv\Scripts\activate

3. Install FastAPI dependencies 
 - pip install "fastapi[standard]" sqlmodel alembic
 - pip install -r requirements.txt
 - pip freeze > requirements.txt
 - deactivate (if you need to go to another python env)