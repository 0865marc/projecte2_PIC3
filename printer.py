import random
import datetime

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from printer_log import Printer_log, Base

import time

class Printer(object):
    def __init__(self, printer_id):
        self.id = printer_id

    def generate_random_data(self):
        time_now = datetime.datetime.now()
        self.date =  time_now.strftime("%d/%m/%Y")
        self.time = time_now.strftime("%H:%M:%S")
        self.temperature = random.randint(20,40)
        self.humidity = random.randint(0,100)
        self.status = ["Active", "Sleeping"][random.randint(0,1)]


def send_data(printer:Printer):

        printer.generate_random_data()

        new_log = Printer_log(
            printer_id=printer.id,
            date = printer.date,
            time = printer.time,
            temperature = printer.temperature,
            humidity = printer.humidity,
            status = printer.status)

        session.add(new_log)
              


if __name__ == "__main__":

    # Create the connection to the db
    engine = create_engine('sqlite:///' + "test.db", echo=True)
    Base.metadata.create_all(engine)

    # Create the session 
    DBSession = sessionmaker(engine)
    session = DBSession()

    printers = []
    #
    n_printers = input("How many printers do you have?")
    for n in range(int(n_printers)):
        printer_id = input(f"{n+1}: Enter a valid id (any integer number): ")
        printers.append(Printer(printer_id))
    

    while True:

        for printer in printers:
            send_data(printer)

        session.commit() 
        time.sleep(20)