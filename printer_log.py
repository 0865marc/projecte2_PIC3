from telnetlib import STATUS
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Printer_log(Base):
     __tablename__ = 'PRINTERS_LOG'
     
     id = Column(Integer, primary_key=True) 
     printer_id = Column(Integer)
     temperature = Column(Integer)
     status = Column(String)
     def __repr__(self):
        return "<Printer(printer_id={})>".format(self.printer_id)

# Create all tables in the engine. This is equivalent to "Create Table" statements in raw SQL.
from sqlalchemy import create_engine
path_to_db = "test.db"
engine = create_engine('sqlite:///' + path_to_db, echo=True)
Base.metadata.create_all(engine)



DBSession = sessionmaker(engine)
session = DBSession()
 
# Insert a User in the user table
new_user1 = Printer_log(printer_id=324, temperature=34, status="Active")
session.add(new_user1)
new_user2 = Printer_log(printer_id=324, temperature=34, status="Active")
session.add(new_user2)
new_user2 = Printer_log(printer_id=324, temperature=34, status="Active")
session.add(new_user2)
session.commit()
