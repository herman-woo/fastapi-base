from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handles startup and shutdown events in a structured way."""
    print("\n\n           🚀 Starting up Base FastAPI...")
    print("               -By Herman Woo\n\n")
    # Initialize DB tables
    # create_db_and_tables()
    
    # Ensure tables exists
    # with SessionDep() as session:
        # RaterRepository(session).create_table()


    yield  # Everything before `yield` runs on startup, everything after runs on shutdown
    print("\n\n           🛑 Shutting down...\n\n")

app = FastAPI(lifespan=lifespan)
# Basic root endpoint
@app.get("/")
async def root():
    return {"message": "Hello World"} 
