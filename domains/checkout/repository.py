from sqlmodel import Session, select
from .models import Cart
from db import engine

class CartRepository:
    def __init__(self, session: Session):
        self.session = session

    def save(self, cart: Cart):
        """Insert or update a Cart in the database."""
        self.session.add(cart)
        self.session.commit()
        self.session.refresh(cart)
        return cart

    def find_by_id(self, cart_id: int) -> Cart | None:
        """Retrieve a Cart by its ID."""
        return self.session.exec(select(Cart).where(Cart.id == cart_id)).first()

    def find_all(self):
        """Retrieve all carts."""
        return self.session.exec(select(Cart)).all()
    
    def delete(self, cart_id: int):
        """Delete a cart by ID."""
        cart = self.find_by_id(cart_id)
        if cart:
            self.session.delete(cart)
            self.session.commit()
            return True
        return False