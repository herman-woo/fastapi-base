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
   - pip install "fastapi[standard]" sqlmodel alembic
 - For Using and Existing Requirements Doc
   - pip install -r requirements.txt
 - Capturing the Requirements.txt
   - pip freeze > requirements.txt
 - Deactivate the virtual env (wont need to in VSCode, just close the window)
   - deactivate

 ## Architecture
 - main.py
/fastapi_project │-- /app │ │-- /api │ │ │-- /v1 │ │ │ │-- /routes │ │ │ │ │-- product_routes.py │ │ │ │ │-- user_routes.py │ │ │ │-- /services │ │ │ │ │-- product_service.py │ │ │ │ │-- user_service.py │ │ │ │-- init.py │ │-- /models │ │ │-- product_model.py │ │ │-- user_model.py │ │-- /schemas │ │ │-- product_schema.py │ │ │-- user_schema.py │ │-- /repositories │ │ │-- product_repository.py │ │ │-- user_repository.py │ │-- /core │ │ │-- config.py │ │ │-- database.py │ │-- main.py │-- /migrations │-- .env │-- .gitignore │-- requirements.txt │-- Dockerfile │-- docker-compose.yml │-- README.md



 ## Running FastAPI
- fastapi dev main.py

 ## Data Migration w/ Alembic