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
    cart_repo = CartRepository(db)
    cart = cart_repo.find_by_id(cart_id)

    if not cart:
        raise HTTPException(status_code=404, detail="Cart not found")

    # 🔥 Explicitly convert `Cart` to a dictionary, including `items`
    return {
        "id": cart.id,
        "subtotal": float(cart.subtotal),  # Convert Decimal to float for JSON compatibility
        "taxes": float(cart.taxes),
        "final_total": float(cart.final_total),
        "items": [
            {
                "id": item.id,
                "cart_id": item.cart_id,
                "product_name": item.product_name,
                "price": float(item.price),  # Convert Decimal to float
                "quantity": item.quantity
            }
            for item in cart.items
        ]
    }

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


@router.delete("/delete-item/{cart_id}/{item_id}")
def delete_cart(cart_id: int, item_id: int,db: SessionDep):
    # """Delete an item by ID."""
    cart_repo = CartRepository(db)
    cart = cart_repo.find_by_id(cart_id)
    success = cart_repo.delete_item(item_id)
    updated_cart = calculate_cart_totals(cart)
    db.commit()
    if not success:
        raise HTTPException(status_code=404, detail="Cart not found")

    return {"message": "Item deleted"}


@router.get("/{cart_id}/items")
def get_cart_items(cart_id: int, db: SessionDep):
    """Retrieve all items in a cart by cart_id."""
    cart_repo = CartRepository(db)
    cart_items = cart_repo.get_items_by_cart_id(cart_id)

    if not cart_items:
        raise HTTPException(status_code=404, detail="No items found for this cart")

    return {"cart_id": cart_id, "items": cart_items}
