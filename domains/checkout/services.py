from sqlalchemy.orm import Session
from .models import Cart, CartItem

TAX_RATE = 0.07

def calculate_cart_totals(cart: Cart):
    """ Recalculates subtotal, tax, and final total for a cart. """
    subtotal = sum(item.price * item.quantity for item in cart.items)
    taxes = subtotal * TAX_RATE
    final_total = subtotal + taxes

    cart.subtotal = subtotal
    cart.taxes = taxes
    cart.final_total = final_total

    return cart

def add_item_to_cart(db: Session, cart_id: int, item_data: dict):
    """ Adds an item to the cart and updates totals. """
    cart = db.get(Cart, cart_id)
    if not cart:
        raise ValueError("Cart not found.")

    new_item = CartItem(cart_id=cart_id, **item_data)
    db.add(new_item)
    db.commit()
    db.refresh(cart)

    # Recalculate totals
    updated_cart = calculate_cart_totals(cart)
    db.commit()
    
    return updated_cart
