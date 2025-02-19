from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from decimal import Decimal

class CartItem(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cart_id: int = Field(foreign_key="cart.id",index=True)  # Foreign key linking to Cart
    product_name: str
    price: float
    quantity: int

    # Define relationship back to Cart
    cart: Optional["Cart"] = Relationship(back_populates="items")

class Cart(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    subtotal: float = Field(default=Decimal(0))
    taxes: float = Field(default=Decimal(0))
    final_total: float = Field(default=Decimal(0))

    # ✅ Ensure `items` is automatically loaded when fetching a Cart
    items: List["CartItem"] = Relationship(
        back_populates="cart", sa_relationship_kwargs={"lazy": "joined"}
    )
