from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from .database import Base

# Every table in the database will have its corresponding model
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    # Make sure to hash the password before saving it
    hashed_password = Column(String(80), unique=False, nullable=False)
    is_active = Column(Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    
    name = Column(String(120), unique=False, nullable=True)
    last_name = Column(String(120), unique=False, nullable=True)
    email = Column(String(120), unique=False, nullable=True)
    password = Column(String(120), unique=False, nullable=True)
    planet_id = mapped_column(ForeignKey("planets.id"))
    planet = relationship("Planet", back_populates="residents")

    def __repr__(self):
        return '<People %r>' % self.full_name()
    

    def full_name(self):
        return self.name +  " " + self.last_name


class Planet(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True, nullable=True)
    residents = relationship("People", back_populates="planet")

