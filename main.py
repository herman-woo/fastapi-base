from fastapi import FastAPI
from contextlib import asynccontextmanager
from db import create_db_and_tables, SessionDep
from domains.checkout.routes import router as cart_router
from domains.checkout.models import Cart
from domains.checkout.repository import CartRepository

from fastapi.middleware.cors import CORSMiddleware

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Handles startup and shutdown events in a structured way."""
    print("\n\n           🚀 Starting up Base FastAPI...")
    print("               -By Herman Woo\n\n")
    # Initialize DB tables
    create_db_and_tables()


    yield  # Everything before `yield` runs on startup, everything after runs on shutdown
    print("\n\n           🛑 Shutting down...\n\n")

app = FastAPI(lifespan=lifespan)
# Basic root endpoint
@app.get("/")
async def root():
    return {"message": "FastAPI-Base is Online!"} 


# Register API routes
app.include_router(cart_router, prefix="/cart")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ✅ Allow all origins (for development)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)