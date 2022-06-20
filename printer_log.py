from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Printer_log(Base):        
        __tablename__ = 'PRINTERS_LOG'
        
        id = Column(Integer, primary_key=True) 
        printer_id = Column(Integer)
        date = Column(String())
        time = Column(String())
        temperature = Column(Integer)
        humidity = Column(Integer)
        status = Column(String)

        def __repr__(self):
                return "<Printer {} (log number={})>".format(self.printer_id, self.id)

        def create_dict(self):
                dict = {
                        "printer_id" : self.printer_id,
                        "date" : self.date,
                        "time" : self.time,
                        "temperature" : self.temperature,
                        "humidity" : self.humidity,
                        "status" : self.status
                        }
                return dict

# Create all tables in the engine. This is equivalent to "Create Table" statements in raw SQL.
from sqlalchemy import create_engine
path_to_db = "test.db"
engine = create_engine('sqlite:///' + path_to_db, echo=True)
Base.metadata.create_all(engine)
