from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from decimal import Decimal

class CartItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cart_id: int = Field(foreign_key="cart.id")  # Foreign key linking to Cart
    product_name: str
    price: Decimal  # Use Decimal for accurate financial calculations
    quantity: int

    # Define relationship to Cart
    cart: Optional["Cart"] = Relationship(back_populates="items")

class Cart(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    subtotal: Decimal = Field(default=Decimal(0))
    taxes: Decimal = Field(default=Decimal(0))
    final_total: Decimal = Field(default=Decimal(0))

    # Define the One-to-Many relationship with CartItem
    items: List["CartItem"] = Relationship(back_populates="cart", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
