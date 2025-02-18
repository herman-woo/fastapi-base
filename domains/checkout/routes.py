from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from .models import Cart, CartItem
from .services import calculate_cart_totals
from .repository import CartRepository
from db import SessionDep  # Import the session dependency

router = APIRouter(prefix="", tags=["Cart"])

@router.post("/")
def create_cart(db: SessionDep):
    """Create a new shopping cart."""
    cart_repo = CartRepository(db)
    cart = Cart()  # Create an empty cart
    saved_cart = cart_repo.save(cart)
    return {"message": "Cart created", "cart_id": saved_cart.id}

@router.get("/{cart_id}")
def get_cart(cart_id: int, db: SessionDep):
    """Retrieve a cart by ID."""
    cart_repo = CartRepository(db)
    cart = cart_repo.find_by_id(cart_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")
    return {"cart": cart}

@router.post("/{cart_id}/add-item")
def add_item(cart_id: int, item_data: dict, db: SessionDep):
    """Add an item to a cart and recalculate totals."""
    cart_repo = CartRepository(db)
    cart = cart_repo.find_by_id(cart_id)
    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    # Create CartItem from request data
    new_item = CartItem(cart_id=cart_id, **item_data)
    db.add(new_item)
    db.commit()
    db.refresh(cart)

    # Recalculate totals
    updated_cart = calculate_cart_totals(cart)
    db.commit()

    return {"message": "Item added", "cart": updated_cart}

@router.delete("/{cart_id}")
def delete_cart(cart_id: int, db: SessionDep):
    """Delete a cart by ID."""
    cart_repo = CartRepository(db)
    success = cart_repo.delete(cart_id)
    if not success:
        raise HTTPException(status_code=404, detail="Cart not found")
    return {"message": "Cart deleted"}


@router.delete("/item/{item_id}")
def delete_cart(cart_id: int, db: SessionDep):
    """Delete an item by ID."""
    cart_repo = CartRepository(db)
    success = cart_repo.delete(cart_id)
    if not success:
        raise HTTPException(status_code=404, detail="Cart not found")
    return {"message": "Cart deleted"}
