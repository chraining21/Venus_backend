from sqlalchemy import Column, Integer, String
from database import Base

class ingredient(Base):
    __tablename__ = 'ingres'
    id = Column(Integer, primary_key = True)
    name = Column(String(200))
    irr = Column(String(5))
    com = Column(String(5))
    tier = Column(String(50))
class i_alia(Base):
    __tablename__ = 'ingres_alia'
    name = Column(String(200))
    id = Column(Integer)
    ingres_aliacol = Column(Integer, primary_key=True)
class whattheydo(Base):
    __tablename__ = 'whattheydo'
    id = Column(Integer, primary_key=True)
    func = Column(String(200))
class whatitdoes(Base):
    __tablename__ = 'funcs'
    ingres_id = Column(Integer)
    func_id = Column(Integer)
    funcscol = Column(Integer, primary_key=True)