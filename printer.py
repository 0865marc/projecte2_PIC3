import random
import datetime

class Printer(object):

    def __init__(self, printer_id):
        self.id = printer_id

        # Check if this printer exists in the printers table

    def generate_random_data(self):
        self.date = datetime.date.today()
        #self.time = 
        self.temperature = random.randint(20,40)
        self.humidity = random.randint(0,100)
        
    def send_data(self)

