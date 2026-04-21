from sqlalchemy import Column, Integer, String, Float
from app.db.base_class import Base

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String, nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(String, default="PENDING")