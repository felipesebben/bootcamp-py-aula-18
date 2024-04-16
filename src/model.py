from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database import Base

class Pokemon(Base):
    """
    Classe pokemon para gerenciar modelo 
    """
    __tablename__ = "pokemons"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(String)
    created_at = Column(DateTime, default=func.now()) 